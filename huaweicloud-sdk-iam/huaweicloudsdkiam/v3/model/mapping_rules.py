# coding: utf-8

import pprint
import re

import six





class MappingRules:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'local': 'list[dict(str, RulesLocalAdditional)]',
        'remote': 'list[RulesRemote]'
    }

    attribute_map = {
        'local': 'local',
        'remote': 'remote'
    }

    def __init__(self, local=None, remote=None):
        """MappingRules - a model defined in huaweicloud sdk"""
        
        

        self._local = None
        self._remote = None
        self.discriminator = None

        self.local = local
        self.remote = remote

    @property
    def local(self):
        """Gets the local of this MappingRules.

        表示联邦用户在本系统中的用户信息。 user：联邦用户在本系统中的用户名称。group：联邦用户在本系统中所属用户组。   

        :return: The local of this MappingRules.
        :rtype: list[dict(str, RulesLocalAdditional)]
        """
        return self._local

    @local.setter
    def local(self, local):
        """Sets the local of this MappingRules.

        表示联邦用户在本系统中的用户信息。 user：联邦用户在本系统中的用户名称。group：联邦用户在本系统中所属用户组。   

        :param local: The local of this MappingRules.
        :type: list[dict(str, RulesLocalAdditional)]
        """
        self._local = local

    @property
    def remote(self):
        """Gets the remote of this MappingRules.

        表示联邦用户在IdP中的用户信息。由断言属性及运算符组成的表达式，取值由断言决定。

        :return: The remote of this MappingRules.
        :rtype: list[RulesRemote]
        """
        return self._remote

    @remote.setter
    def remote(self, remote):
        """Sets the remote of this MappingRules.

        表示联邦用户在IdP中的用户信息。由断言属性及运算符组成的表达式，取值由断言决定。

        :param remote: The remote of this MappingRules.
        :type: list[RulesRemote]
        """
        self._remote = remote

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
        if not isinstance(other, MappingRules):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
