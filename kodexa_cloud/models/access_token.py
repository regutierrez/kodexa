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


class AccessToken(object):
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
        'id': 'str',
        'name': 'str',
        'organization': 'Organization',
        'token': 'str',
        'updated_by': 'str',
        'updated_on': 'Timestamp',
        'uuid': 'str'
    }

    attribute_map = {
        'created_by': 'createdBy',
        'created_on': 'createdOn',
        'id': 'id',
        'name': 'name',
        'organization': 'organization',
        'token': 'token',
        'updated_by': 'updatedBy',
        'updated_on': 'updatedOn',
        'uuid': 'uuid'
    }

    def __init__(self, created_by=None, created_on=None, id=None, name=None, organization=None, token=None, updated_by=None, updated_on=None, uuid=None):  # noqa: E501
        """AccessToken - a model defined in Swagger"""  # noqa: E501
        self._created_by = None
        self._created_on = None
        self._id = None
        self._name = None
        self._organization = None
        self._token = None
        self._updated_by = None
        self._updated_on = None
        self._uuid = None
        self.discriminator = None
        if created_by is not None:
            self.created_by = created_by
        if created_on is not None:
            self.created_on = created_on
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if organization is not None:
            self.organization = organization
        if token is not None:
            self.token = token
        if updated_by is not None:
            self.updated_by = updated_by
        if updated_on is not None:
            self.updated_on = updated_on
        if uuid is not None:
            self.uuid = uuid

    @property
    def created_by(self):
        """Gets the created_by of this AccessToken.  # noqa: E501


        :return: The created_by of this AccessToken.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this AccessToken.


        :param created_by: The created_by of this AccessToken.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def created_on(self):
        """Gets the created_on of this AccessToken.  # noqa: E501


        :return: The created_on of this AccessToken.  # noqa: E501
        :rtype: Timestamp
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this AccessToken.


        :param created_on: The created_on of this AccessToken.  # noqa: E501
        :type: Timestamp
        """

        self._created_on = created_on

    @property
    def id(self):
        """Gets the id of this AccessToken.  # noqa: E501


        :return: The id of this AccessToken.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AccessToken.


        :param id: The id of this AccessToken.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this AccessToken.  # noqa: E501


        :return: The name of this AccessToken.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AccessToken.


        :param name: The name of this AccessToken.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def organization(self):
        """Gets the organization of this AccessToken.  # noqa: E501


        :return: The organization of this AccessToken.  # noqa: E501
        :rtype: Organization
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this AccessToken.


        :param organization: The organization of this AccessToken.  # noqa: E501
        :type: Organization
        """

        self._organization = organization

    @property
    def token(self):
        """Gets the token of this AccessToken.  # noqa: E501


        :return: The token of this AccessToken.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this AccessToken.


        :param token: The token of this AccessToken.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def updated_by(self):
        """Gets the updated_by of this AccessToken.  # noqa: E501


        :return: The updated_by of this AccessToken.  # noqa: E501
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this AccessToken.


        :param updated_by: The updated_by of this AccessToken.  # noqa: E501
        :type: str
        """

        self._updated_by = updated_by

    @property
    def updated_on(self):
        """Gets the updated_on of this AccessToken.  # noqa: E501


        :return: The updated_on of this AccessToken.  # noqa: E501
        :rtype: Timestamp
        """
        return self._updated_on

    @updated_on.setter
    def updated_on(self, updated_on):
        """Sets the updated_on of this AccessToken.


        :param updated_on: The updated_on of this AccessToken.  # noqa: E501
        :type: Timestamp
        """

        self._updated_on = updated_on

    @property
    def uuid(self):
        """Gets the uuid of this AccessToken.  # noqa: E501


        :return: The uuid of this AccessToken.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this AccessToken.


        :param uuid: The uuid of this AccessToken.  # noqa: E501
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
        if issubclass(AccessToken, dict):
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
        if not isinstance(other, AccessToken):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
