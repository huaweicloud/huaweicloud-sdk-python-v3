# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateParamsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'success': 'bool',
        'should_restart': 'str',
        'error_code': 'str',
        'error_msg': 'str'
    }

    attribute_map = {
        'success': 'success',
        'should_restart': 'should_restart',
        'error_code': 'error_code',
        'error_msg': 'error_msg'
    }

    def __init__(self, success=None, should_restart=None, error_code=None, error_msg=None):
        r"""UpdateParamsResponse

        The model defined in huaweicloud sdk

        :param success: 修改参数是否成功
        :type success: bool
        :param should_restart: 是否需要重启
        :type should_restart: str
        :param error_code: 错误码
        :type error_code: str
        :param error_msg: 错误信息
        :type error_msg: str
        """
        
        super(UpdateParamsResponse, self).__init__()

        self._success = None
        self._should_restart = None
        self._error_code = None
        self._error_msg = None
        self.discriminator = None

        if success is not None:
            self.success = success
        if should_restart is not None:
            self.should_restart = should_restart
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def success(self):
        r"""Gets the success of this UpdateParamsResponse.

        修改参数是否成功

        :return: The success of this UpdateParamsResponse.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this UpdateParamsResponse.

        修改参数是否成功

        :param success: The success of this UpdateParamsResponse.
        :type success: bool
        """
        self._success = success

    @property
    def should_restart(self):
        r"""Gets the should_restart of this UpdateParamsResponse.

        是否需要重启

        :return: The should_restart of this UpdateParamsResponse.
        :rtype: str
        """
        return self._should_restart

    @should_restart.setter
    def should_restart(self, should_restart):
        r"""Sets the should_restart of this UpdateParamsResponse.

        是否需要重启

        :param should_restart: The should_restart of this UpdateParamsResponse.
        :type should_restart: str
        """
        self._should_restart = should_restart

    @property
    def error_code(self):
        r"""Gets the error_code of this UpdateParamsResponse.

        错误码

        :return: The error_code of this UpdateParamsResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this UpdateParamsResponse.

        错误码

        :param error_code: The error_code of this UpdateParamsResponse.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        r"""Gets the error_msg of this UpdateParamsResponse.

        错误信息

        :return: The error_msg of this UpdateParamsResponse.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this UpdateParamsResponse.

        错误信息

        :param error_msg: The error_msg of this UpdateParamsResponse.
        :type error_msg: str
        """
        self._error_msg = error_msg

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
        if not isinstance(other, UpdateParamsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
