# coding: utf-8

import pprint
import re

import six





class ProtectPolicyOption:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'operation_protection': 'bool'
    }

    attribute_map = {
        'operation_protection': 'operation_protection'
    }

    def __init__(self, operation_protection=None):
        """ProtectPolicyOption - a model defined in huaweicloud sdk"""
        
        

        self._operation_protection = None
        self.discriminator = None

        self.operation_protection = operation_protection

    @property
    def operation_protection(self):
        """Gets the operation_protection of this ProtectPolicyOption.

        是否开启操作保护，开启为\"true\"，未开启为\"false\"。

        :return: The operation_protection of this ProtectPolicyOption.
        :rtype: bool
        """
        return self._operation_protection

    @operation_protection.setter
    def operation_protection(self, operation_protection):
        """Sets the operation_protection of this ProtectPolicyOption.

        是否开启操作保护，开启为\"true\"，未开启为\"false\"。

        :param operation_protection: The operation_protection of this ProtectPolicyOption.
        :type: bool
        """
        self._operation_protection = operation_protection

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
        if not isinstance(other, ProtectPolicyOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
