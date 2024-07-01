"""
Utilities and base implementation of Connectors that allow a document to access a source native file or
stream upon which the document is based or derived.
"""

import fnmatch
import inspect
import io
import logging
import mimetypes
import os
import tempfile
import urllib
from os.path import join
from typing import Dict, Type

from kodexa.model import Document, DocumentMetadata, SourceMetadata
from security import safe_requests

logger = logging.getLogger()


def get_caller_dir():
    """Returns the absolute path of the directory containing the file that called this function.

    This function uses the `inspect` module to retrieve the stack frame of the caller and extract its file path. The file path is then converted to an absolute path using the `os.path` module.

    Returns:
        str: The absolute path of the caller's directory.

    Example:
        >>> get_caller_dir()
        '/path/to/caller/directory'
    """
    # get the caller's stack frame and extract its file path
    frame_info = inspect.stack()[3]
    filepath = frame_info.filename
    del frame_info
    # drop the reference to the stack frame to avoid reference cycles

    # make the path absolute (optional)
    filepath = os.path.dirname(os.path.abspath(filepath))
    return filepath


class FolderConnector:
    """ """

    @staticmethod
    def get_name():
        """ """
        return "folder"

    def __init__(
        self,
        path,
        file_filter="*",
        recursive=False,
        relative=False,
        caller_path=get_caller_dir(),
        unpack=False,
    ):
        self.path = path
        self.file_filter = file_filter
        self.recursive = recursive
        self.relative = relative
        self.caller_path = caller_path
        self.unpack = unpack

        if not self.path:
            raise ValueError("You must provide a path")

        self.files = self.__get_files__()
        self.index = 0

    @staticmethod
    def get_source(document):
        """

        Args:
          document:

        Returns:

        """
        return open(
            join(document.source.original_path, document.source.original_filename), "rb"
        )

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > len(self.files) - 1:
            raise StopIteration

        self.index += 1
        if self.unpack:
            return Document.from_kdxa(self.files[self.index - 1])

        document = Document(
            DocumentMetadata(
                {
                    "source_path": self.files[self.index - 1],
                    "connector": self.get_name(),
                    "mime_type": mimetypes.guess_type(self.files[self.index - 1]),
                    "connector_options": {
                        "path": self.path,
                        "file_filter": self.file_filter,
                    },
                }
            )
        )
        document.source.original_filename = os.path.basename(self.files[self.index - 1])
        document.source.original_path = self.path
        document.source.connector = self.get_name()

        # TODO we need to get the checksum and last_updated and created times
        return document

    def __get_files__(self):
        all_files = []
        base_path = self.path

        if self.relative:
            base_path = os.path.join(self.caller_path, base_path)
        for dp, dn, fn in os.walk(os.path.expanduser(base_path)):
            for f in fn:
                file_name = os.path.join(dp, f)
                if fnmatch.fnmatch(f, self.file_filter):
                    all_files.append(file_name)

            if not self.recursive:
                break

        return all_files


class FileHandleConnector:
    """
    A File Handle Connector can be used to create a document from a file path (e.g. a file like object)
    """

    @staticmethod
    def get_name():
        """ """
        return "file-handle"

    def __init__(self, original_path: str):
        self.file = original_path
        self.index = 0
        self.completed = False

    @staticmethod
    def get_source(document: Document):
        """

        Args:
          document:

        Returns:

        """
        return open(document.source.original_path, "rb")

    def __iter__(self):
        return self

    def __next__(self):
        if self.completed:
            raise StopIteration

        document = Document(
            DocumentMetadata(
                {
                    "source_path": self.file,
                    "connector": self.get_name(),
                    "mime_type": mimetypes.guess_type(self.file),
                    "connector_options": {"file": self.file},
                }
            )
        )
        document.source.original_filename = self.file
        document.source.original_path = os.path.basename(self.file)
        document.source.connector = self.get_name()
        return document


class UrlConnector:
    """ """

    @staticmethod
    def get_name():
        """ """
        return "url"

    def __init__(self, original_path, headers=None):
        if headers is None:
            headers = {}
        self.url = original_path
        self.headers = headers
        self.index = 0
        self.completed = False

    @staticmethod
    def get_source(document):
        """

        Args:
          document:

        Returns:

        """

        # If we have an http URL then we should use requests, it is much
        # cleaner
        if document.source.original_path.startswith("http"):
            response = safe_requests.get(document.source.original_path, headers=document.source.headers
            )
            return io.BytesIO(response.content)

        if document.source.headers:
            opener = urllib.request.build_opener()
            for header in document.source.headers:
                opener.addheaders = [(header, document.source.headers[header])]
            urllib.request.install_opener(opener)
        from kodexa import KodexaPlatform

        with tempfile.NamedTemporaryFile(
            delete=True, dir=KodexaPlatform.get_tempdir()
        ) as tmp_file:
            urllib.request.urlretrieve(document.source.original_path, tmp_file.name)

            return open(tmp_file.name, "rb")

    def __iter__(self):
        return self

    def __next__(self):
        if self.completed:
            raise StopIteration

        self.completed = True
        document = Document(
            DocumentMetadata(
                {
                    "connector": self.get_name(),
                    "connector_options": {"url": self.url, "headers": self.headers},
                }
            )
        )
        document.source.connector = self.get_name()
        document.source.original_path = self.url
        document.source.headers = self.headers
        return document


# The registered connectors
registered_connectors: Dict[str, Type] = {}


def get_connectors():
    """
    Returns the keys of the registered connectors.

    Returns:
        A list of keys representing the registered connectors.
    """
    return registered_connectors.keys()


def get_connector(connector: str, source: SourceMetadata):
    """Get a connector based on the provided connector name and source metadata.

    Args:
        connector (str): The name of the connector.
        source (SourceMetadata): The metadata of the source.

    Returns:
        The registered connector with the given name.

    Raises:
        Exception: If the connector is not found.

    Example:
        >>> get_connector('mysql', source_metadata)
        <mysql_connector>
    """
    if connector in registered_connectors:
        logger.info(f"Getting registered connector {connector}")
        return registered_connectors[connector]

    logging.error(f"Unable to find connector {connector}")
    raise Exception(f"Unable to find connector {connector}")


def add_connector(connector):
    """Adds a connector to the list of registered connectors.

    Args:
        connector: The connector object to be added.

    Returns:
        None

    Raises:
        None
    """
    registered_connectors[connector.get_name()] = connector


def get_source(document):
    """
    Returns the source of a document using the specified connector.

    Args:
        document (Document): The document object for which to retrieve the source.

    Returns:
        str: The source of the document.

    Raises:
        ValueError: If the document source connector is invalid.

    Example:
        >>> document = Document(...)
        >>> source = get_source(document)
        >>> print(source)
        This is the source of the document.
    """
    connector = get_connector(document.source.connector, document.source)
    return connector.get_source(document)


class DocumentStoreConnector:
    """
    A class for connecting to a document store.

    Methods:
    - get_name: Get the name of the document store.
    - get_source: Get the source of a document from the document store.
    """

    @staticmethod
    def get_name():
        """ """
        return "document-store"

    @staticmethod
    def get_source(document):
        """
        Get the source of a document from the document store.

        Args:
        document (object): The document object.

        Returns:
        io.BytesIO: The source of the document as a BytesIO object.

        Raises:
        Exception: If the source of the document cannot be retrieved.
        """
        from kodexa import KodexaClient

        client = KodexaClient()
        from kodexa.platform.client import DocumentStoreEndpoint

        document_store: DocumentStoreEndpoint = client.get_object_by_ref(
            "store", document.source.headers["ref"]
        )
        from kodexa.platform.client import DocumentFamilyEndpoint

        family: DocumentFamilyEndpoint = document_store.get_family(
            document.source.headers["family"]
        )
        document_bytes = family.get_native()
        if document_bytes is None:
            raise Exception(
                f"Unable to get source, document with id {document.source.headers['id']} is missing?"
            )

        import io

        return io.BytesIO(document_bytes)


add_connector(DocumentStoreConnector)

add_connector(FolderConnector)
add_connector(FileHandleConnector)
add_connector(UrlConnector)
