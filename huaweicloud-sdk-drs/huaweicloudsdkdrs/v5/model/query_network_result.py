# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryNetworkResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ip': 'str',
        'success': 'bool',
        'result': 'str',
        'status': 'str',
        'error_code': 'str',
        'error_msg': 'str'
    }

    attribute_map = {
        'ip': 'ip',
        'success': 'success',
        'result': 'result',
        'status': 'status',
        'error_code': 'error_code',
        'error_msg': 'error_msg'
    }

    def __init__(self, ip=None, success=None, result=None, status=None, error_code=None, error_msg=None):
        r"""QueryNetworkResult

        The model defined in huaweicloud sdk

        :param ip: 测试连接IP。
        :type ip: str
        :param success: 测试连接是否成功。
        :type success: bool
        :param result: 测试连接结果。
        :type result: str
        :param status: 测试连接是否成功。取值： - success：成功。 - failed：不成功。
        :type status: str
        :param error_code: 测试连接失败错误码。
        :type error_code: str
        :param error_msg: 测试连接失败错误内容。
        :type error_msg: str
        """
        
        

        self._ip = None
        self._success = None
        self._result = None
        self._status = None
        self._error_code = None
        self._error_msg = None
        self.discriminator = None

        if ip is not None:
            self.ip = ip
        self.success = success
        if result is not None:
            self.result = result
        self.status = status
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def ip(self):
        r"""Gets the ip of this QueryNetworkResult.

        测试连接IP。

        :return: The ip of this QueryNetworkResult.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this QueryNetworkResult.

        测试连接IP。

        :param ip: The ip of this QueryNetworkResult.
        :type ip: str
        """
        self._ip = ip

    @property
    def success(self):
        r"""Gets the success of this QueryNetworkResult.

        测试连接是否成功。

        :return: The success of this QueryNetworkResult.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this QueryNetworkResult.

        测试连接是否成功。

        :param success: The success of this QueryNetworkResult.
        :type success: bool
        """
        self._success = success

    @property
    def result(self):
        r"""Gets the result of this QueryNetworkResult.

        测试连接结果。

        :return: The result of this QueryNetworkResult.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this QueryNetworkResult.

        测试连接结果。

        :param result: The result of this QueryNetworkResult.
        :type result: str
        """
        self._result = result

    @property
    def status(self):
        r"""Gets the status of this QueryNetworkResult.

        测试连接是否成功。取值： - success：成功。 - failed：不成功。

        :return: The status of this QueryNetworkResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this QueryNetworkResult.

        测试连接是否成功。取值： - success：成功。 - failed：不成功。

        :param status: The status of this QueryNetworkResult.
        :type status: str
        """
        self._status = status

    @property
    def error_code(self):
        r"""Gets the error_code of this QueryNetworkResult.

        测试连接失败错误码。

        :return: The error_code of this QueryNetworkResult.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this QueryNetworkResult.

        测试连接失败错误码。

        :param error_code: The error_code of this QueryNetworkResult.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        r"""Gets the error_msg of this QueryNetworkResult.

        测试连接失败错误内容。

        :return: The error_msg of this QueryNetworkResult.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this QueryNetworkResult.

        测试连接失败错误内容。

        :param error_msg: The error_msg of this QueryNetworkResult.
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
        if not isinstance(other, QueryNetworkResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
