# coding: utf-8

import pprint
import re

import six





class CheckSubcustomerUserReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'search_type': 'str',
        'search_value': 'str'
    }

    attribute_map = {
        'search_type': 'search_type',
        'search_value': 'search_value'
    }

    def __init__(self, search_type=None, search_value=None):
        """CheckSubcustomerUserReq - a model defined in huaweicloud sdk"""
        
        

        self._search_type = None
        self._search_value = None
        self.discriminator = None

        self.search_type = search_type
        self.search_value = search_value

    @property
    def search_type(self):
        """Gets the search_type of this CheckSubcustomerUserReq.

        |参数名称：该字段内容可填为：“email”、“mobile”或“name”| |参数的约束及描述：该参数必填，且只允许字符串|

        :return: The search_type of this CheckSubcustomerUserReq.
        :rtype: str
        """
        return self._search_type

    @search_type.setter
    def search_type(self, search_type):
        """Sets the search_type of this CheckSubcustomerUserReq.

        |参数名称：该字段内容可填为：“email”、“mobile”或“name”| |参数的约束及描述：该参数必填，且只允许字符串|

        :param search_type: The search_type of this CheckSubcustomerUserReq.
        :type: str
        """
        self._search_type = search_type

    @property
    def search_value(self):
        """Gets the search_value of this CheckSubcustomerUserReq.

        |参数名称：手机、邮箱或用户名| |参数的约束及描述：该参数必填，且只允许字符串,手机包括国家码，以00开头，格式：00XX-XXXXXXXX。目前手机号仅仅支持以86为国家码|

        :return: The search_value of this CheckSubcustomerUserReq.
        :rtype: str
        """
        return self._search_value

    @search_value.setter
    def search_value(self, search_value):
        """Sets the search_value of this CheckSubcustomerUserReq.

        |参数名称：手机、邮箱或用户名| |参数的约束及描述：该参数必填，且只允许字符串,手机包括国家码，以00开头，格式：00XX-XXXXXXXX。目前手机号仅仅支持以86为国家码|

        :param search_value: The search_value of this CheckSubcustomerUserReq.
        :type: str
        """
        self._search_value = search_value

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
        if not isinstance(other, CheckSubcustomerUserReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
