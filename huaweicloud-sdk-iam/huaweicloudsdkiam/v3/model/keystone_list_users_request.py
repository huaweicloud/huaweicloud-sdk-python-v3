# coding: utf-8

import pprint
import re

import six





class KeystoneListUsersRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []
    sensitive_list.append('password_expires_at')

    openapi_types = {
        'domain_id': 'str',
        'enabled': 'bool',
        'name': 'str',
        'password_expires_at': 'str'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'enabled': 'enabled',
        'name': 'name',
        'password_expires_at': 'password_expires_at'
    }

    def __init__(self, domain_id=None, enabled=None, name=None, password_expires_at=None):
        """KeystoneListUsersRequest - a model defined in huaweicloud sdk"""
        
        

        self._domain_id = None
        self._enabled = None
        self._name = None
        self._password_expires_at = None
        self.discriminator = None

        if domain_id is not None:
            self.domain_id = domain_id
        if enabled is not None:
            self.enabled = enabled
        if name is not None:
            self.name = name
        if password_expires_at is not None:
            self.password_expires_at = password_expires_at

    @property
    def domain_id(self):
        """Gets the domain_id of this KeystoneListUsersRequest.


        :return: The domain_id of this KeystoneListUsersRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this KeystoneListUsersRequest.


        :param domain_id: The domain_id of this KeystoneListUsersRequest.
        :type: str
        """
        self._domain_id = domain_id

    @property
    def enabled(self):
        """Gets the enabled of this KeystoneListUsersRequest.


        :return: The enabled of this KeystoneListUsersRequest.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this KeystoneListUsersRequest.


        :param enabled: The enabled of this KeystoneListUsersRequest.
        :type: bool
        """
        self._enabled = enabled

    @property
    def name(self):
        """Gets the name of this KeystoneListUsersRequest.


        :return: The name of this KeystoneListUsersRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this KeystoneListUsersRequest.


        :param name: The name of this KeystoneListUsersRequest.
        :type: str
        """
        self._name = name

    @property
    def password_expires_at(self):
        """Gets the password_expires_at of this KeystoneListUsersRequest.


        :return: The password_expires_at of this KeystoneListUsersRequest.
        :rtype: str
        """
        return self._password_expires_at

    @password_expires_at.setter
    def password_expires_at(self, password_expires_at):
        """Sets the password_expires_at of this KeystoneListUsersRequest.


        :param password_expires_at: The password_expires_at of this KeystoneListUsersRequest.
        :type: str
        """
        self._password_expires_at = password_expires_at

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, KeystoneListUsersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
