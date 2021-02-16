import logging
import os
import shutil
from pathlib import Path
from typing import List, Optional, Dict

import jsonpickle

from kodexa.model import DocumentFamily, DocumentStore, Document, ContentObject
from kodexa.model.document_families import ContentEvent, DocumentRelationship

logger = logging.getLogger('kodexa.stores')


class LocalDocumentStore(DocumentStore):

    def __init__(self, store_path: str, force_initialize: bool = False, mode: str = 'ALL'):

        modes = ['ALL', 'ONLY_NEW']

        if mode not in modes:
            raise Exception(f"LocalDocumentStore mode must be one of {','.join(modes)}")

        self.store_path: str = store_path
        self.index = 0
        self.metastore: List[DocumentFamily] = []
        self.mode = mode
        self.listeners: List = []

        path = Path(store_path)

        if force_initialize and path.exists():
            shutil.rmtree(store_path)

        if path.is_file():
            raise Exception("Unable to load store, since it is pointing to a file?")
        elif not path.exists():
            logger.info(f"Creating new local document store in {store_path}")
            path.mkdir(parents=True)

            # Create an empty index file
            self.metastore = []
            self.write_metastore()

        self.read_metastore()

        logger.info(f"Found {len(self.metastore)} documents in {store_path}")

    def get_ref(self) -> str:
        return self.store_path

    def register_listener(self, listener):
        self.listeners.append(listener)

    def notify_listeners(self, content_event: ContentEvent):
        for listener in self.listeners:
            listener.process_event(content_event)

    def to_dict(self):
        return {
            "type": "DOCUMENT",
            "data": {
                "path": self.store_path
            }
        }

    def accept(self, document: Document):
        if self.mode == 'ALL':
            return True
        if self.mode == 'ONLY_NEW':
            return not self.exists(document)

    def read_metastore(self):
        """
        Read the metadata store
        """
        self.metastore: List[Dict] = []
        with open(os.path.join(self.store_path, 'metastore.json')) as f:
            self.metastore = jsonpickle.decode("".join(f.readlines()))

    def write_metastore(self):
        """
        Method to write the JSON store index back to store path
        """
        with open(os.path.join(self.store_path, 'metastore.json'), 'w') as f:
            f.write(jsonpickle.encode(self.metastore))

    def get_by_uuid(self, uuid: str) -> Optional[Document]:
        for family in self.metastore:
            for content_object in family.content_objects:

                if content_object.id == uuid:
                    return Document.from_kdxa(os.path.join(self.store_path, content_object.id) + ".kdxa")
        return None

    def get_by_path(self, path: str) -> Optional[Document]:
        """
        Return the latest document in the family at the given path

        :param path:
        :return:
        """
        for family in self.metastore:
            if family.path == path:
                # TODO we need to get the latest document from the family

                return Document.from_kdxa(os.path.join(self.store_path, family.get_latest_content().id) + ".kdxa")
        return None

    def get_family_by_path(self, path: str) -> Optional[DocumentFamily]:
        for family in self.metastore:
            if family.path == path:
                return family
        return None

    def list_objects(self) -> List[DocumentFamily]:
        return self.metastore

    def count(self) -> int:
        return len(self.metastore)

    def load_kdxa(self, path: str):
        document = Document.from_kdxa(path)
        self.put(document.uuid, document)

    def add_related_document_to_family(self, document_family_id: str, document_relationship: DocumentRelationship,
                                       document: Document):
        self.read_metastore()
        for family in self.metastore:
            if family.id == document_family_id:
                family.add_document(document, document_relationship)

    def get_document_by_content_object(self, content_object: ContentObject) -> Document:
        return Document.from_kdxa(os.path.join(self.store_path, content_object.id) + ".kdxa")

    def put(self, path: str, document: Document):

        # We can only add a document if it doesn't already exist as a family
        if self.get_family_by_path(path) is None:
            new_document_family = DocumentFamily(path, self.get_ref())
            new_event = new_document_family.add_document(document)
            document.to_kdxa(os.path.join(self.store_path, new_event.content_object.id) + ".kdxa")

            self.metastore.append(new_document_family)
            self.write_metastore()

            # Notify the listeners
            self.notify_listeners(new_event)

        return self.get_family_by_path(path)

    def exists(self, document):
        """
        Look to see if we have document with the same original path and original filename

        :param document: document to check
        :return: True if it is already in the document store
        """

        # Lets just work with original_filename?

        for family in self.metastore:
            if document.source.original_filename == family.path:
                return True
        return False
