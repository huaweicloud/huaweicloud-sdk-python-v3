# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class CheckUserIdentityResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'error_code': 'str',
        'error_msg': 'str',
        'check_result': 'str'
    }

    attribute_map = {
        'error_code': 'error_code',
        'error_msg': 'error_msg',
        'check_result': 'check_result'
    }

    def __init__(self, error_code='CBC.0000', error_msg='success', check_result=None):
        """CheckUserIdentityResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._error_code = None
        self._error_msg = None
        self._check_result = None
        self.discriminator = None

        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg
        if check_result is not None:
            self.check_result = check_result

    @property
    def error_code(self):
        """Gets the error_code of this CheckUserIdentityResponse.

        |参数名称：返回码| |参数的约束及描述：该参数必填，且只允许字符串|

        :return: The error_code of this CheckUserIdentityResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this CheckUserIdentityResponse.

        |参数名称：返回码| |参数的约束及描述：该参数必填，且只允许字符串|

        :param error_code: The error_code of this CheckUserIdentityResponse.
        :type: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        """Gets the error_msg of this CheckUserIdentityResponse.

        |参数名称：返回码描述| |参数的约束及描述：该参数必填，且只允许字符串|

        :return: The error_msg of this CheckUserIdentityResponse.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this CheckUserIdentityResponse.

        |参数名称：返回码描述| |参数的约束及描述：该参数必填，且只允许字符串|

        :param error_msg: The error_msg of this CheckUserIdentityResponse.
        :type: str
        """
        self._error_msg = error_msg

    @property
    def check_result(self):
        """Gets the check_result of this CheckUserIdentityResponse.

        |参数名称：是否可以继续注册| |参数的约束及描述：该参数非必填，且只允许字符串,available: 该登录名称/手机号/邮箱可以继续注册,used_by_user: 该登录名称/手机号/邮箱不可以继续注册|

        :return: The check_result of this CheckUserIdentityResponse.
        :rtype: str
        """
        return self._check_result

    @check_result.setter
    def check_result(self, check_result):
        """Sets the check_result of this CheckUserIdentityResponse.

        |参数名称：是否可以继续注册| |参数的约束及描述：该参数非必填，且只允许字符串,available: 该登录名称/手机号/邮箱可以继续注册,used_by_user: 该登录名称/手机号/邮箱不可以继续注册|

        :param check_result: The check_result of this CheckUserIdentityResponse.
        :type: str
        """
        self._check_result = check_result

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
        if not isinstance(other, CheckUserIdentityResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
