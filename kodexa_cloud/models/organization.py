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


class Organization(object):
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
        'created_by': 'str',
        'created_on': 'Timestamp',
        'description': 'str',
        'id': 'str',
        'name': 'str',
        'public_access': 'bool',
        'slug': 'str',
        'updated_by': 'str',
        'updated_on': 'Timestamp',
        'uuid': 'str'
    }

    attribute_map = {
        'created_by': 'createdBy',
        'created_on': 'createdOn',
        'description': 'description',
        'id': 'id',
        'name': 'name',
        'public_access': 'publicAccess',
        'slug': 'slug',
        'updated_by': 'updatedBy',
        'updated_on': 'updatedOn',
        'uuid': 'uuid'
    }

    def __init__(self, created_by=None, created_on=None, description=None, id=None, name=None, public_access=None, slug=None, updated_by=None, updated_on=None, uuid=None):  # noqa: E501
        """Organization - a model defined in Swagger"""  # noqa: E501
        self._created_by = None
        self._created_on = None
        self._description = None
        self._id = None
        self._name = None
        self._public_access = None
        self._slug = None
        self._updated_by = None
        self._updated_on = None
        self._uuid = None
        self.discriminator = None
        if created_by is not None:
            self.created_by = created_by
        if created_on is not None:
            self.created_on = created_on
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if public_access is not None:
            self.public_access = public_access
        if slug is not None:
            self.slug = slug
        if updated_by is not None:
            self.updated_by = updated_by
        if updated_on is not None:
            self.updated_on = updated_on
        if uuid is not None:
            self.uuid = uuid

    @property
    def created_by(self):
        """Gets the created_by of this Organization.  # noqa: E501


        :return: The created_by of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Organization.


        :param created_by: The created_by of this Organization.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def created_on(self):
        """Gets the created_on of this Organization.  # noqa: E501


        :return: The created_on of this Organization.  # noqa: E501
        :rtype: Timestamp
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this Organization.


        :param created_on: The created_on of this Organization.  # noqa: E501
        :type: Timestamp
        """

        self._created_on = created_on

    @property
    def description(self):
        """Gets the description of this Organization.  # noqa: E501


        :return: The description of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Organization.


        :param description: The description of this Organization.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this Organization.  # noqa: E501


        :return: The id of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Organization.


        :param id: The id of this Organization.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Organization.  # noqa: E501


        :return: The name of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Organization.


        :param name: The name of this Organization.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def public_access(self):
        """Gets the public_access of this Organization.  # noqa: E501


        :return: The public_access of this Organization.  # noqa: E501
        :rtype: bool
        """
        return self._public_access

    @public_access.setter
    def public_access(self, public_access):
        """Sets the public_access of this Organization.


        :param public_access: The public_access of this Organization.  # noqa: E501
        :type: bool
        """

        self._public_access = public_access

    @property
    def slug(self):
        """Gets the slug of this Organization.  # noqa: E501


        :return: The slug of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this Organization.


        :param slug: The slug of this Organization.  # noqa: E501
        :type: str
        """

        self._slug = slug

    @property
    def updated_by(self):
        """Gets the updated_by of this Organization.  # noqa: E501


        :return: The updated_by of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this Organization.


        :param updated_by: The updated_by of this Organization.  # noqa: E501
        :type: str
        """

        self._updated_by = updated_by

    @property
    def updated_on(self):
        """Gets the updated_on of this Organization.  # noqa: E501


        :return: The updated_on of this Organization.  # noqa: E501
        :rtype: Timestamp
        """
        return self._updated_on

    @updated_on.setter
    def updated_on(self, updated_on):
        """Sets the updated_on of this Organization.


        :param updated_on: The updated_on of this Organization.  # noqa: E501
        :type: Timestamp
        """

        self._updated_on = updated_on

    @property
    def uuid(self):
        """Gets the uuid of this Organization.  # noqa: E501


        :return: The uuid of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this Organization.


        :param uuid: The uuid of this Organization.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

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
        if issubclass(Organization, dict):
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
        if not isinstance(other, Organization):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
