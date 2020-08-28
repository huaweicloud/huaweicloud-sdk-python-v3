# coding: utf-8

import pprint
import re

import six





class KeystoneCheckDomainPermissionForGroupRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'group_id': 'str',
        'role_id': 'str'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'group_id': 'group_id',
        'role_id': 'role_id'
    }

    def __init__(self, domain_id=None, group_id=None, role_id=None):
        """KeystoneCheckDomainPermissionForGroupRequest - a model defined in huaweicloud sdk"""
        
        

        self._domain_id = None
        self._group_id = None
        self._role_id = None
        self.discriminator = None

        self.domain_id = domain_id
        self.group_id = group_id
        self.role_id = role_id

    @property
    def domain_id(self):
        """Gets the domain_id of this KeystoneCheckDomainPermissionForGroupRequest.


        :return: The domain_id of this KeystoneCheckDomainPermissionForGroupRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this KeystoneCheckDomainPermissionForGroupRequest.


        :param domain_id: The domain_id of this KeystoneCheckDomainPermissionForGroupRequest.
        :type: str
        """
        self._domain_id = domain_id

    @property
    def group_id(self):
        """Gets the group_id of this KeystoneCheckDomainPermissionForGroupRequest.


        :return: The group_id of this KeystoneCheckDomainPermissionForGroupRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this KeystoneCheckDomainPermissionForGroupRequest.


        :param group_id: The group_id of this KeystoneCheckDomainPermissionForGroupRequest.
        :type: str
        """
        self._group_id = group_id

    @property
    def role_id(self):
        """Gets the role_id of this KeystoneCheckDomainPermissionForGroupRequest.


        :return: The role_id of this KeystoneCheckDomainPermissionForGroupRequest.
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """Sets the role_id of this KeystoneCheckDomainPermissionForGroupRequest.


        :param role_id: The role_id of this KeystoneCheckDomainPermissionForGroupRequest.
        :type: str
        """
        self._role_id = role_id

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
        if not isinstance(other, KeystoneCheckDomainPermissionForGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
