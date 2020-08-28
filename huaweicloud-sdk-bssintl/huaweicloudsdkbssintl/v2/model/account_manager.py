# coding: utf-8

import pprint
import re

import six





class AccountManager:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'account_name': 'str'
    }

    attribute_map = {
        'account_name': 'account_name'
    }

    def __init__(self, account_name=None):
        """AccountManager - a model defined in huaweicloud sdk"""
        
        

        self._account_name = None
        self.discriminator = None

        if account_name is not None:
            self.account_name = account_name

    @property
    def account_name(self):
        """Gets the account_name of this AccountManager.

        |参数名称：客户经理登录名称。| |参数约束及描述：客户经理登录名称。最大长度128，必填|

        :return: The account_name of this AccountManager.
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this AccountManager.

        |参数名称：客户经理登录名称。| |参数约束及描述：客户经理登录名称。最大长度128，必填|

        :param account_name: The account_name of this AccountManager.
        :type: str
        """
        self._account_name = account_name

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
        if not isinstance(other, AccountManager):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
