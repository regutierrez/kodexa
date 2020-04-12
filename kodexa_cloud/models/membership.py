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


class Membership(object):
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
        'organization': 'Organization',
        'role': 'str',
        'updated_by': 'str',
        'updated_on': 'Timestamp',
        'user': 'PlatformUser',
        'uuid': 'str'
    }

    attribute_map = {
        'created_by': 'createdBy',
        'created_on': 'createdOn',
        'id': 'id',
        'organization': 'organization',
        'role': 'role',
        'updated_by': 'updatedBy',
        'updated_on': 'updatedOn',
        'user': 'user',
        'uuid': 'uuid'
    }

    def __init__(self, created_by=None, created_on=None, id=None, organization=None, role=None, updated_by=None, updated_on=None, user=None, uuid=None):  # noqa: E501
        """Membership - a model defined in Swagger"""  # noqa: E501
        self._created_by = None
        self._created_on = None
        self._id = None
        self._organization = None
        self._role = None
        self._updated_by = None
        self._updated_on = None
        self._user = None
        self._uuid = None
        self.discriminator = None
        if created_by is not None:
            self.created_by = created_by
        if created_on is not None:
            self.created_on = created_on
        if id is not None:
            self.id = id
        if organization is not None:
            self.organization = organization
        if role is not None:
            self.role = role
        if updated_by is not None:
            self.updated_by = updated_by
        if updated_on is not None:
            self.updated_on = updated_on
        if user is not None:
            self.user = user
        if uuid is not None:
            self.uuid = uuid

    @property
    def created_by(self):
        """Gets the created_by of this Membership.  # noqa: E501


        :return: The created_by of this Membership.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Membership.


        :param created_by: The created_by of this Membership.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def created_on(self):
        """Gets the created_on of this Membership.  # noqa: E501


        :return: The created_on of this Membership.  # noqa: E501
        :rtype: Timestamp
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this Membership.


        :param created_on: The created_on of this Membership.  # noqa: E501
        :type: Timestamp
        """

        self._created_on = created_on

    @property
    def id(self):
        """Gets the id of this Membership.  # noqa: E501


        :return: The id of this Membership.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Membership.


        :param id: The id of this Membership.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def organization(self):
        """Gets the organization of this Membership.  # noqa: E501


        :return: The organization of this Membership.  # noqa: E501
        :rtype: Organization
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this Membership.


        :param organization: The organization of this Membership.  # noqa: E501
        :type: Organization
        """

        self._organization = organization

    @property
    def role(self):
        """Gets the role of this Membership.  # noqa: E501


        :return: The role of this Membership.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this Membership.


        :param role: The role of this Membership.  # noqa: E501
        :type: str
        """
        allowed_values = ["OWNER", "READ", "WRITE"]  # noqa: E501
        if role not in allowed_values:
            raise ValueError(
                "Invalid value for `role` ({0}), must be one of {1}"  # noqa: E501
                .format(role, allowed_values)
            )

        self._role = role

    @property
    def updated_by(self):
        """Gets the updated_by of this Membership.  # noqa: E501


        :return: The updated_by of this Membership.  # noqa: E501
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this Membership.


        :param updated_by: The updated_by of this Membership.  # noqa: E501
        :type: str
        """

        self._updated_by = updated_by

    @property
    def updated_on(self):
        """Gets the updated_on of this Membership.  # noqa: E501


        :return: The updated_on of this Membership.  # noqa: E501
        :rtype: Timestamp
        """
        return self._updated_on

    @updated_on.setter
    def updated_on(self, updated_on):
        """Sets the updated_on of this Membership.


        :param updated_on: The updated_on of this Membership.  # noqa: E501
        :type: Timestamp
        """

        self._updated_on = updated_on

    @property
    def user(self):
        """Gets the user of this Membership.  # noqa: E501


        :return: The user of this Membership.  # noqa: E501
        :rtype: PlatformUser
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Membership.


        :param user: The user of this Membership.  # noqa: E501
        :type: PlatformUser
        """

        self._user = user

    @property
    def uuid(self):
        """Gets the uuid of this Membership.  # noqa: E501


        :return: The uuid of this Membership.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this Membership.


        :param uuid: The uuid of this Membership.  # noqa: E501
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
        if issubclass(Membership, dict):
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
        if not isinstance(other, Membership):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
