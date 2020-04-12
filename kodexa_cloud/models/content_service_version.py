# coding: utf-8

"""
    Kodexa

    Content Intelligence  # noqa: E501

    OpenAPI spec version: 2.0.132
    Contact: suppot@kodexa.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class ContentServiceVersion(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'content_service': 'ContentService',
        'created_by': 'str',
        'created_on': 'Timestamp',
        'id': 'str',
        'metadata': 'object',
        'position': 'int',
        'public_access': 'bool',
        'updated_by': 'str',
        'updated_on': 'Timestamp',
        'uuid': 'str',
        'version': 'str'
    }

    attribute_map = {
        'content_service': 'contentService',
        'created_by': 'createdBy',
        'created_on': 'createdOn',
        'id': 'id',
        'metadata': 'metadata',
        'position': 'position',
        'public_access': 'publicAccess',
        'updated_by': 'updatedBy',
        'updated_on': 'updatedOn',
        'uuid': 'uuid',
        'version': 'version'
    }

    def __init__(self, content_service=None, created_by=None, created_on=None, id=None, metadata=None, position=None, public_access=None, updated_by=None, updated_on=None, uuid=None, version=None):  # noqa: E501
        """ContentServiceVersion - a model defined in Swagger"""  # noqa: E501
        self._content_service = None
        self._created_by = None
        self._created_on = None
        self._id = None
        self._metadata = None
        self._position = None
        self._public_access = None
        self._updated_by = None
        self._updated_on = None
        self._uuid = None
        self._version = None
        self.discriminator = None
        if content_service is not None:
            self.content_service = content_service
        if created_by is not None:
            self.created_by = created_by
        if created_on is not None:
            self.created_on = created_on
        if id is not None:
            self.id = id
        if metadata is not None:
            self.metadata = metadata
        if position is not None:
            self.position = position
        if public_access is not None:
            self.public_access = public_access
        if updated_by is not None:
            self.updated_by = updated_by
        if updated_on is not None:
            self.updated_on = updated_on
        if uuid is not None:
            self.uuid = uuid
        if version is not None:
            self.version = version

    @property
    def content_service(self):
        """Gets the content_service of this ContentServiceVersion.  # noqa: E501


        :return: The content_service of this ContentServiceVersion.  # noqa: E501
        :rtype: ContentService
        """
        return self._content_service

    @content_service.setter
    def content_service(self, content_service):
        """Sets the content_service of this ContentServiceVersion.


        :param content_service: The content_service of this ContentServiceVersion.  # noqa: E501
        :type: ContentService
        """

        self._content_service = content_service

    @property
    def created_by(self):
        """Gets the created_by of this ContentServiceVersion.  # noqa: E501


        :return: The created_by of this ContentServiceVersion.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this ContentServiceVersion.


        :param created_by: The created_by of this ContentServiceVersion.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def created_on(self):
        """Gets the created_on of this ContentServiceVersion.  # noqa: E501


        :return: The created_on of this ContentServiceVersion.  # noqa: E501
        :rtype: Timestamp
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this ContentServiceVersion.


        :param created_on: The created_on of this ContentServiceVersion.  # noqa: E501
        :type: Timestamp
        """

        self._created_on = created_on

    @property
    def id(self):
        """Gets the id of this ContentServiceVersion.  # noqa: E501


        :return: The id of this ContentServiceVersion.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ContentServiceVersion.


        :param id: The id of this ContentServiceVersion.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def metadata(self):
        """Gets the metadata of this ContentServiceVersion.  # noqa: E501


        :return: The metadata of this ContentServiceVersion.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this ContentServiceVersion.


        :param metadata: The metadata of this ContentServiceVersion.  # noqa: E501
        :type: object
        """

        self._metadata = metadata

    @property
    def position(self):
        """Gets the position of this ContentServiceVersion.  # noqa: E501


        :return: The position of this ContentServiceVersion.  # noqa: E501
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this ContentServiceVersion.


        :param position: The position of this ContentServiceVersion.  # noqa: E501
        :type: int
        """

        self._position = position

    @property
    def public_access(self):
        """Gets the public_access of this ContentServiceVersion.  # noqa: E501


        :return: The public_access of this ContentServiceVersion.  # noqa: E501
        :rtype: bool
        """
        return self._public_access

    @public_access.setter
    def public_access(self, public_access):
        """Sets the public_access of this ContentServiceVersion.


        :param public_access: The public_access of this ContentServiceVersion.  # noqa: E501
        :type: bool
        """

        self._public_access = public_access

    @property
    def updated_by(self):
        """Gets the updated_by of this ContentServiceVersion.  # noqa: E501


        :return: The updated_by of this ContentServiceVersion.  # noqa: E501
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this ContentServiceVersion.


        :param updated_by: The updated_by of this ContentServiceVersion.  # noqa: E501
        :type: str
        """

        self._updated_by = updated_by

    @property
    def updated_on(self):
        """Gets the updated_on of this ContentServiceVersion.  # noqa: E501


        :return: The updated_on of this ContentServiceVersion.  # noqa: E501
        :rtype: Timestamp
        """
        return self._updated_on

    @updated_on.setter
    def updated_on(self, updated_on):
        """Sets the updated_on of this ContentServiceVersion.


        :param updated_on: The updated_on of this ContentServiceVersion.  # noqa: E501
        :type: Timestamp
        """

        self._updated_on = updated_on

    @property
    def uuid(self):
        """Gets the uuid of this ContentServiceVersion.  # noqa: E501


        :return: The uuid of this ContentServiceVersion.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this ContentServiceVersion.


        :param uuid: The uuid of this ContentServiceVersion.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def version(self):
        """Gets the version of this ContentServiceVersion.  # noqa: E501


        :return: The version of this ContentServiceVersion.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ContentServiceVersion.


        :param version: The version of this ContentServiceVersion.  # noqa: E501
        :type: str
        """

        self._version = version

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ContentServiceVersion, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ContentServiceVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
