# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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

    def __init__(self, error_code=None, error_msg=None, check_result=None):
        """CheckUserIdentityResponse

        The model defined in huaweicloud sdk

        :param error_code: 状态码。具体请参考状态码。只有失败才会返回这个参数。
        :type error_code: str
        :param error_msg: 错误描述信息。只有失败才会返回这个参数。
        :type error_msg: str
        :param check_result: available：该登录名称/手机号/邮箱有效。used_by_user：该登录名称/手机号/邮箱已被占用。
        :type check_result: str
        """
        
        super(CheckUserIdentityResponse, self).__init__()

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

        状态码。具体请参考状态码。只有失败才会返回这个参数。

        :return: The error_code of this CheckUserIdentityResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this CheckUserIdentityResponse.

        状态码。具体请参考状态码。只有失败才会返回这个参数。

        :param error_code: The error_code of this CheckUserIdentityResponse.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        """Gets the error_msg of this CheckUserIdentityResponse.

        错误描述信息。只有失败才会返回这个参数。

        :return: The error_msg of this CheckUserIdentityResponse.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this CheckUserIdentityResponse.

        错误描述信息。只有失败才会返回这个参数。

        :param error_msg: The error_msg of this CheckUserIdentityResponse.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def check_result(self):
        """Gets the check_result of this CheckUserIdentityResponse.

        available：该登录名称/手机号/邮箱有效。used_by_user：该登录名称/手机号/邮箱已被占用。

        :return: The check_result of this CheckUserIdentityResponse.
        :rtype: str
        """
        return self._check_result

    @check_result.setter
    def check_result(self, check_result):
        """Sets the check_result of this CheckUserIdentityResponse.

        available：该登录名称/手机号/邮箱有效。used_by_user：该登录名称/手机号/邮箱已被占用。

        :param check_result: The check_result of this CheckUserIdentityResponse.
        :type check_result: str
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
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CheckUserIdentityResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
