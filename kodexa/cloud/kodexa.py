from __future__ import annotations

import errno
import json
import logging
import os
import sys
import time
from json import JSONDecodeError

import requests
import yaml
from addict import Dict
from rich import print

from kodexa.connectors import get_source
from kodexa.connectors.connectors import get_caller_dir, FolderConnector
from kodexa.model import Document
from kodexa.model.model import RemoteStore
from kodexa.pipeline import PipelineContext, Pipeline, PipelineStatistics
from kodexa.stores import TableDataStore
from kodexa.stores.stores import LocalDocumentStore
from appdirs import AppDirs

logger = logging.getLogger('kodexa.platform')


dirs = AppDirs("Kodexa", "Kodexa")


def get_config():
    path = os.path.join(dirs.user_config_dir, '.kodexa.json')
    if os.path.exists(path):
        with open(path, 'r') as outfile:
            return json.load(outfile)
    else:
        return {'url': None, 'access_token': None}


def save_config(config_obj):
    path = os.path.join(dirs.user_config_dir, '.kodexa.json')
    if not os.path.exists(os.path.dirname(path)):
        try:
            os.makedirs(os.path.dirname(path))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    with open(path, 'w') as outfile:
        json.dump(config_obj, outfile)


class PipelineMetadataBuilder:
    """
    Build a metadata representation of the pipeline for passing to an instance of the
    Kodexa platform
    """

    def __init__(self, pipeline: Pipeline):
        self.pipeline = pipeline

    def build_steps(self, pipeline_metadata: Dict):
        pipeline_metadata.metadata.steps = []
        pipeline_metadata.metadata.stores = []

        for pipeline_store in self.pipeline.stores:

            if isinstance(pipeline_store.store, RemoteStore):
                pipeline_metadata.metadata.stores.append(
                    {"name": pipeline_store.name, "ref": pipeline_store.store.get_ref()})
            else:
                raise Exception("Pipeline refers to a non-remote store, deployment of local stores is not supported")

        for idx, step in enumerate(self.pipeline.steps):

            step_meta = step.to_dict()
            if step_meta['name'] is None:
                step_meta['name'] = f"Step {idx + 1}"

            if 'script' in step_meta:
                pipeline_metadata.metadata.steps.append({
                    'ref': 'kodexa/python-step',
                    'name': step_meta['name'],
                    'enabled': True,
                    'condition': None,
                    'options': {
                        'function_name': step_meta['function'],
                        'script': step_meta['script']
                    }
                })
            else:
                pipeline_metadata.metadata.steps.append(step_meta)

        return pipeline_metadata


DEFAULT_COLUMNS = {
    'extensionPacks': [
        'orgSlug',
        'slug',
        'version',
        'name',
        'description',
        'type',
        'status'
    ],
    'default': [
        'orgSlug',
        'slug',
        'version',
        'name',
        'description',
        'type'
    ]
}

OBJECT_TYPES = {
    "extensionPacks": {
        "name": "extension pack",
        "plural": "extension packs"
    },
    "pipelines": {
        "name": "pipelines",
        "plural": "pipelines"
    },
    "actions": {
        "name": "action",
        "plural": "actions"
    },
    "stores": {
        "name": "store",
        "plural": "stores"
    },
    "connectors": {
        "name": "connector",
        "plural": "connectors"
    },
    "taxonomies": {
        "name": "taxonomy",
        "plural": "taxonomies"
    },
    "workflows": {
        "name": "workflow",
        "plural": "workflows"
    }
}


def resolve_object_type(obj_type):
    hits = []
    keys = []
    for target_type in OBJECT_TYPES.keys():
        if obj_type in target_type:
            hits.append(OBJECT_TYPES[target_type])
            keys.append(target_type)

    if len(hits) == 1:
        return keys[0], hits[0]

    if len(hits) == 0:
        print(":exclaimation: Unable to find object type {obj_type}")
        sys.exit(1)
    else:
        print(f":exclaimation: To many potential matches for object type ({','.join(keys)}")
        sys.exit(1)


class KodexaPlatform:

    @staticmethod
    def get_access_token():
        kodexa_config = get_config()
        access_token = os.getenv('KODEXA_ACCESS_TOKEN')
        return access_token if access_token is not None else kodexa_config['access_token']

    @staticmethod
    def get_url():
        kodexa_config = get_config()
        env_url = os.getenv('KODEXA_URL', None)
        return env_url if env_url is not None else kodexa_config['url']

    @staticmethod
    def set_access_token(access_token):
        if access_token is not None:
            os.environ["KODEXA_ACCESS_TOKEN"] = access_token

    @staticmethod
    def set_url(url):
        if url is not None:
            os.environ["KODEXA_URL"] = url

    """
    The deployer allows you to take a locally build Pipeline and then push that pipeline
    to a Kodexa platform instance
    """

    @staticmethod
    def get_access_token_details():
        response = requests.get(
            f"{KodexaPlatform.get_url()}/api/account/accessToken",
            headers={"x-access-token": KodexaPlatform.get_access_token()})
        if response.status_code == 200:
            return Dict(response.json())
        else:
            if response.status_code == 404:
                raise Exception("Unable to find access token")
            else:
                raise Exception("An error occurred connecting to the Kodexa platform")

    @staticmethod
    def deploy_extension(metadata):
        response = requests.post(f"{KodexaPlatform.get_url()}/api/extensionPacks/{metadata['orgSlug']}",
                                 json=metadata.to_dict(),
                                 headers={"x-access-token": KodexaPlatform.get_access_token(),
                                          "content-type": "application/json"})
        if response.status_code == 200:
            logger.info("Extension deployed")
        else:
            logger.error(response.text)
            raise Exception("Unable to deploy new extension")

    @staticmethod
    def deploy_extension_from_uri(path, organisation_slug):
        url = f"{KodexaPlatform.get_url()}/api/extensionPacks/{organisation_slug}?uri={path}"
        logger.info(f"Publishing extension pack to organization {organisation_slug}")
        response = requests.post(url,
                                 headers={"x-access-token": KodexaPlatform.get_access_token(),
                                          "content-type": "application/json"})
        if response.status_code == 200:
            logger.info("Extension deployed")
        else:
            logger.error(response.text)
            raise Exception("Unable to deploy new extension")

    @staticmethod
    def resolve_ref(ref: str):
        org_slug = ref.split('/')[0]
        slug = ref.split('/')[1].split(":")[0]

        version = None

        if len(ref.split('/')[1].split(":")) == 2:
            version = ref.split('/')[1].split(":")[1]

        return [org_slug, slug, version]

    @staticmethod
    def deploy(ref: str, kodexa_object, name: str = "A new object", description: str = "A new Kodexa object",
               options=None, public=False, force_replace=False):

        if '/' not in ref:
            logger.error("A ref must be valid, i.e. org_slug/pipeline_slug:version")
            raise Exception("Invalid slug")

        [organization_slug, object_slug, object_version] = KodexaPlatform.resolve_ref(ref)

        if options is None:
            options = {}

        metadata_object = Dict()
        metadata_object.orgSlug = organization_slug
        metadata_object.publicAccess = public
        metadata_object.slug = object_slug
        metadata_object.version = object_version
        metadata_object.name = name
        metadata_object.description = description

        object_url = None

        if isinstance(kodexa_object, Pipeline):

            object_url = "pipelines"

            if "example_urls" not in options:
                example_urls = []
            else:
                example_urls = options["example_urls"]

            if "more_info_url" not in options:
                more_info_url = None
            else:
                more_info_url = options["more_info_url"]

            builder = PipelineMetadataBuilder(kodexa_object)

            metadata_object.type = 'pipeline'
            metadata_object.metadata.parameters = []
            metadata_object.metadata.steps = []
            metadata_object.exampleUrls = example_urls
            metadata_object.moreInfoUrl = more_info_url

            builder.build_steps(metadata_object)

        elif isinstance(kodexa_object, LocalDocumentStore):
            object_url = 'stores'
            metadata_object.type = 'store'
            metadata_object.contentType = 'DOCUMENT'
        else:
            raise Exception("Unknown object type, unable to deploy")

        logger.info(f"Deploying {metadata_object.type} {ref}")

        access_token = KodexaPlatform.get_access_token_details()

        if organization_slug not in access_token.organizationSlugs:
            logger.error(f"You do not have access to the organization {organization_slug}")
            raise Exception("Unable to deploy, no access to organization")

        if object_version:
            url = f"{KodexaPlatform.get_url()}/api/{object_url}/{organization_slug}/{object_slug}/{object_version}"
        else:
            url = f"{KodexaPlatform.get_url()}/api/{object_url}/{organization_slug}/{object_slug}"

        response = requests.get(url,
                                headers={"x-access-token": KodexaPlatform.get_access_token(),
                                         "content-type": "application/json"})

        if response.status_code == 401:
            logger.error(f"You do not have the permissions to access this {metadata_object.type}")
            raise Exception("Not authorized on pipeline")

        if response.status_code == 404:
            logger.info("Object doesn't exist, will deploy")
            response = requests.post(f"{KodexaPlatform.get_url()}/api/{object_url}/{organization_slug}",
                                     json=metadata_object.to_dict(),
                                     headers={"x-access-token": KodexaPlatform.get_access_token(),
                                              "content-type": "application/json"})
            if response.status_code == 200:
                logger.info("Deployed")
            else:
                logger.error(response.text)
                raise Exception("Unable to deploy")
        else:
            logger.info(f"{ref} already exists")
            if force_replace:
                logger.info(f"Replacing {ref}")
                response = requests.put(url,
                                        json=metadata_object.to_dict(),
                                        headers={"x-access-token": KodexaPlatform.get_access_token(),
                                                 "content-type": "application/json"})
                if response.status_code == 200:
                    logger.info("Deployed")
                else:
                    logger.error(response.text)
                    raise Exception("Unable to deploy and replace")
            else:
                logger.warning("Not updating")
                return

    @staticmethod
    def list_objects(organization_slug, object_type):
        list_response = requests.get(f"{KodexaPlatform.get_url()}/api/{object_type}/{organization_slug}",
                                     headers={"x-access-token": KodexaPlatform.get_access_token(),
                                              "content-type": "application/json"})
        if list_response.status_code == 200:
            return list_response.json()
        else:
            logger.error(list_response.text)
            raise Exception("Unable to list objects")

    @staticmethod
    def undeploy(ref: str):
        url_ref = ref.replace(':', '/')
        response = requests.delete(f"{KodexaPlatform.get_url()}/api/pipelines/{url_ref}",
                                   headers={"x-access-token": KodexaPlatform.get_access_token(),
                                            "content-type": "application/json"})
        if response.status_code == 200:
            logger.info("Pipeline undeployed")
        else:
            logger.error(response.text)
            raise Exception("Unable to undeploy and replace existing pipeline")

    @staticmethod
    def delete_object(ref, object_type):
        # Generate a URL ref
        url_ref = ref.replace(':', '/')
        delete_response = requests.delete(f"{KodexaPlatform.get_url()}/api/{object_type}/{url_ref}",
                                          headers={"x-access-token": KodexaPlatform.get_access_token(),
                                                   "content-type": "application/json"})
        if delete_response.status_code != 200:
            logger.error(delete_response.text)
            raise Exception("Unable to list objects")

    @staticmethod
    def get_object(ref, object_type):
        url_ref = ref.replace(':', '/')
        obj_response = requests.get(f"{KodexaPlatform.get_url()}/api/{object_type}/{url_ref}",
                                    headers={"x-access-token": KodexaPlatform.get_access_token(),
                                             "content-type": "application/json"})
        if obj_response.status_code != 200:
            logger.error(obj_response.text)
            raise Exception(f"Unable to get object {ref}")
        else:
            return obj_response.json()

    @classmethod
    def get(cls, object_type, ref):

        object_type, object_type_metadata = resolve_object_type(object_type)

        try:

            # If ref is just the org then we will list them
            if '/' in ref:
                obj = KodexaPlatform.get_object(ref, object_type)
                import yaml
                print(obj)
            else:
                objects = KodexaPlatform.list_objects(ref, object_type)
                cols = DEFAULT_COLUMNS['default']

                if object_type in DEFAULT_COLUMNS:
                    cols = DEFAULT_COLUMNS[object_type]

                print("\n")
                from rich.table import Table

                table = Table(title=f"Listing {object_type_metadata['plural']}")
                for col in cols:
                    table.add_column(col)
                for object_dict in objects['content']:
                    row = []

                    for col in cols:
                        row.append(object_dict[col] if col in object_dict else '')
                    table.add_row(*row)

                print(table)
        except:
            print(f"\n:exclamation: Failed to get {object_type_metadata['name']} [{sys.exc_info()[0]}]")

    @classmethod
    def delete(cls, object_type, ref):
        object_type, object_type_metadata = resolve_object_type(object_type)
        print(f"Deleting {object_type_metadata['name']} [bold]{ref}[/bold]")

        try:
            KodexaPlatform.delete_object(ref, object_type)
            print(f"Deleted {object_type_metadata['name']} [bold]{ref}[/bold] :tada:")
        except:
            print(f"\n:exclamation: Failed to delete {object_type_metadata['name']} [{sys.exc_info()[0]}]")

    @classmethod
    def login(cls, kodexa_url, username, password):
        from requests.auth import HTTPBasicAuth
        obj_response = requests.get(f"{kodexa_url}/api/account/me/token",
                                    auth=HTTPBasicAuth(username, password),
                                    headers={"content-type": "application/json"})
        if obj_response.status_code == 200:
            kodexa_config = get_config()
            kodexa_config['url'] = kodexa_url
            kodexa_config['access_token'] = obj_response.text
            save_config(kodexa_config)
            print("Logged in")
        else:
            print(f"Check your URL and password [{obj_response.status_code}]")

    @classmethod
    def get_server_info(cls):
        return requests.get(f"{KodexaPlatform.get_url()}/api",
                            headers={"x-access-token": KodexaPlatform.get_access_token(),
                                     "content-type": "application/json"}).json()


class RemoteSession:
    """
    A Session on the Kodexa platform for leveraging pipelines and services
    """

    def __init__(self, session_type, slug):
        self.session_type = session_type
        self.slug = slug
        self.cloud_session = None

    def get_action_metadata(self, ref):
        r = requests.get(f"{KodexaPlatform.get_url()}/api/actions/{ref}",
                         headers={"x-access-token": KodexaPlatform.get_access_token()})
        return r.json()

    def start(self):
        logger.info(f"Creating session {self.slug} ({KodexaPlatform.get_url()})")
        r = requests.post(f"{KodexaPlatform.get_url()}/api/sessions", params={self.session_type: self.slug},
                          headers={"x-access-token": KodexaPlatform.get_access_token()})

        if r.status_code != 200:
            logger.error("Unable to create session")
            logger.error(r.text)
            raise Exception("Unable to create a session, check your URL and access token")

        self.cloud_session = Dict(json.loads(r.text))

    def execution_action(self, document, options, attach_source):
        files = {}
        if attach_source:
            logger.info("Attaching source")
            files["file"] = get_source(document)
            files["file_document"] = document.to_msgpack()
        else:
            files["document"] = document.to_msgpack()

        data = {"options": json.dumps(options), "document_metadata_json": json.dumps(document.metadata)}

        logger.info(f"Executing session {self.cloud_session.id}")
        r = requests.post(f"{KodexaPlatform.get_url()}/api/sessions/{self.cloud_session.id}/execute",
                          params={self.session_type: self.slug},
                          data=data,
                          headers={"x-access-token": KodexaPlatform.get_access_token()}, files=files)
        try:
            if r.status_code == 200:
                execution = Dict(json.loads(r.text))
            else:
                logger.error("Execution creation failed [" + r.text + "], response " + str(r.status_code))
                raise Exception("Execution creation failed [" + r.text + "], response " + str(r.status_code))
        except JSONDecodeError:
            logger.error("Unable to handle response [" + r.text + "], response " + str(r.status_code))
            raise

        return execution

    def wait_for_execution(self, execution):

        status = execution.status
        while execution.status == "PENDING" or execution.status == "RUNNING":
            r = requests.get(
                f"{KodexaPlatform.get_url()}/api/sessions/{self.cloud_session.id}/executions/{execution.id}",
                headers={"x-access-token": KodexaPlatform.get_access_token()})
            try:
                execution = Dict(json.loads(r.text))
            except JSONDecodeError:
                logger.error("Unable to handle response [" + r.text + "]")
                raise

            if status != execution.status:
                logger.info(f"Status changed from {status} -> {execution.status}")
                status = execution.status

            time.sleep(1)

        if status == "FAILED":
            logger.error("Execution has failed")
            for step in execution.steps:
                if step.status == 'FAILED':
                    logger.error(f"Step {step.name} has failed. {step.exceptionDetails.message}.")

                    if step.exceptionDetails.errorType == 'Validation':
                        logger.error("Additional validation information has been provided:")
                        for validation_error in step.exceptionDetails.validationErrors:
                            logger.error(f"- {validation_error.option} : {validation_error.message}")

                    if step.exceptionDetails.help:
                        logger.error(f"Additional help is available:\n\n{step.exceptionDetails.help}")

            logger.debug(execution)

            raise Exception("Processing has failed")

        return execution

    def get_output_document(self, execution):
        if execution.outputId:
            doc = requests.get(
                f"{KodexaPlatform.get_url()}/api/sessions/{self.cloud_session.id}/executions/{execution.id}/objects/{execution.outputId}",
                headers={"x-access-token": KodexaPlatform.get_access_token()})
            return Document.from_msgpack(doc.content)
        else:
            return None

    def get_store(self, execution, store):
        response = requests.get(
            f"{KodexaPlatform.get_url()}/api/sessions/{self.cloud_session.id}/executions/{execution.id}/stores/{store.id}",
            headers={"x-access-token": KodexaPlatform.get_access_token()})
        logger.debug(f"Response from server [{response.text}]")
        raw_store = Dict(json.loads(response.text))
        return TableDataStore(raw_store.data.columns, raw_store.data.rows, raw_store.data.source_documents)

    def merge_stores(self, execution, context: PipelineContext):
        for store in execution.stores:
            context.merge_store(store.name, self.get_store(execution, store))


class RemotePipeline:
    """
    Allow you to interact with a pipeline that has been deployed to an instance of Kodexa Platform
    """

    def __init__(self, slug, connector, version=None, attach_source=True, parameters=None, auth=None):
        logger.info(f"Initializing a new pipeline {slug}")

        if isinstance(connector, Document):
            self.connector = [connector]
        else:
            self.connector = connector
        self.sink = None
        self.context: PipelineContext = PipelineContext()

        if auth is None:
            auth = []
        if parameters is None:
            parameters = {}
        self.slug = slug
        self.version = version
        self.attach_source = attach_source
        self.parameters = parameters
        self.auth = auth

    def set_sink(self, sink):
        """
        Set the sink you wish to use, note that it will replace any currently assigned
        sink

            >>> pipeline = Pipeline(FolderConnector(path='/tmp/', file_filter='example.pdf'))
            >>> pipeline.set_sink(ExampleSink())

        :param sink: the sink for the pipeline
        """
        logger.info(f"Setting sink {sink.get_name()} on {self.slug}")
        self.sink = sink

        return self

    def run(self):
        self.context.statistics = PipelineStatistics()

        logger.info(f"Starting remote pipeline {self.slug}")
        cloud_session = RemoteSession("pipeline", self.slug)
        cloud_session.start()

        for document in self.connector:
            logger.info(f"Processing {document}")
            execution = cloud_session.execution_action(document, self.parameters, self.attach_source)
            execution = cloud_session.wait_for_execution(execution)

            result_document = cloud_session.get_output_document(execution)
            self.context.set_output_document(result_document)
            cloud_session.merge_stores(execution, self.context)

            self.context.statistics.processed_document(document)

            if self.sink:
                logger.info(f"Writing to sink {self.sink.get_name()}")
                try:
                    self.sink.sink(document)
                except:
                    if document:
                        document.exceptions.append({
                            "step": self.sink.get_name(),
                            "exception": sys.exc_info()[0]
                        })
                    if self.context.stop_on_exception:
                        raise

        logger.info(f"Completed pipeline {self.slug}")

        return self.context

    @staticmethod
    def from_url(slug: str, url, headers=None) -> RemotePipeline:
        """
        Build a new pipeline with the input being a document created from the given URL

        :param slug: The slug for the remote pipeline
        :param url: The URL ie. https://www.google.com
        :param headers: A dictionary of headers
        :return: A new instance of a remote pipeline
        """
        return RemotePipeline(slug, Document.from_url(url, headers))

    @staticmethod
    def from_file(slug: str, file_path: str) -> RemotePipeline:
        """
        Create a new pipeline using a file path as a source

        :param slug: The slug for the remote pipeline
        :param file_path: The path to the file
        :return: A new pipeline
        :rtype: Pipeline
        """
        return RemotePipeline(slug, Document.from_file(file_path))

    @staticmethod
    def from_text(slug: str, text: str, *args, **kwargs) -> RemotePipeline:
        """
        Build a new pipeline and provide text as the basic to create a document

        :param slug: The slug for the remote pipeline
        :param text: Text to use to create document
        :return: A new pipeline
        :rtype: RemotePipeline
        """
        return RemotePipeline(slug, Document.from_text(text))

    @staticmethod
    def from_folder(slug: str, folder_path: str, filename_filter: str = "*", recursive: bool = False,
                    relative: bool = False,
                    caller_path: str = get_caller_dir()) -> RemotePipeline:
        """
        Create a pipeline that will run against a set of local files from a folder

        :param slug: The slug for the remote pipeline
        :param folder_path: The folder path
        :param filename_filter: The filter for filename (i.e. *.pdf)
        :param recursive: Should we look recursively in sub-directories (default False)
        :param relative: Is the folder path relative to the caller (default False)
        :param caller_path: The caller path (defaults to trying to work this out from the stack)
        :return: A new pipeline
        :rtype: RemotePipeline
        """
        return RemotePipeline(slug, FolderConnector(folder_path, filename_filter, recursive, relative, caller_path))


class RemoteAction:
    """
    Allows you to interact with an action that has been deployed in the Kodexa platform
    """

    def __init__(self, slug, version=None, attach_source=False, options=None, auth=None):
        if auth is None:
            auth = []
        if options is None:
            options = {}
        self.slug = slug
        self.version = version
        self.attach_source = attach_source
        self.options = options
        self.auth = auth

    def to_dict(self):
        return {
            'ref': self.slug,
            'options': self.options
        }

    def get_name(self):
        return f"Remote Action ({self.slug})"

    def process(self, document, context):
        cloud_session = RemoteSession("service", self.slug)
        cloud_session.start()

        logger.info(f"Loading metadata for {self.slug}")
        action_metadata = cloud_session.get_action_metadata(self.slug)

        requires_source = False
        if 'requiresSource' in action_metadata['metadata']:
            requires_source = action_metadata['metadata']['requiresSource']

        execution = cloud_session.execution_action(document, self.options,
                                                   self.attach_source if self.attach_source else requires_source)
        execution = cloud_session.wait_for_execution(execution)

        result_document = cloud_session.get_output_document(execution)
        cloud_session.merge_stores(execution, context)

        return result_document if result_document else document

    def end_processing(self):

        # TODO not yet implemented for remote steps
        pass

    def to_configuration(self):
        """
        Returns a dictionary representing the configuration information for the step

        :return: dictionary representing the configuration of the step
        """
        return {
            "ref": self.slug,
            "options": self.options
        }


class ExtensionHelper:

    @staticmethod
    def load_metadata(path):

        if os.path.exists(os.path.join(path, 'dharma.json')):
            dharma_metadata_file = open(os.path.join(path, 'dharma.json'))
            dharma_metadata = Dict(json.loads(dharma_metadata_file.read()))
        elif os.path.exists(os.path.join(path, 'dharma.yml')):
            dharma_metadata_file = open(os.path.join(path, 'dharma.yml'))
            dharma_metadata = Dict(yaml.safe_load(dharma_metadata_file.read()))
        elif os.path.exists(os.path.join(path, 'kodexa.yml')):
            dharma_metadata_file = open(os.path.join(path, 'kodexa.yml'))
            dharma_metadata = Dict(yaml.safe_load(dharma_metadata_file.read()))
        else:
            raise Exception("Unable to find a kodexa.yml file describing your extension")
        return dharma_metadata
