# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TimeoutConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'connect_timeout': 'int',
        'send_timeout': 'int',
        'read_timeout': 'int'
    }

    attribute_map = {
        'connect_timeout': 'connect_timeout',
        'send_timeout': 'send_timeout',
        'read_timeout': 'read_timeout'
    }

    def __init__(self, connect_timeout=None, send_timeout=None, read_timeout=None):
        """TimeoutConfig

        The model defined in huaweicloud sdk

        :param connect_timeout: WAF连接源站超时配置
        :type connect_timeout: int
        :param send_timeout: WAF发送请求到源站超时配置
        :type send_timeout: int
        :param read_timeout: WAF接收源站响应超时配置
        :type read_timeout: int
        """
        
        

        self._connect_timeout = None
        self._send_timeout = None
        self._read_timeout = None
        self.discriminator = None

        if connect_timeout is not None:
            self.connect_timeout = connect_timeout
        if send_timeout is not None:
            self.send_timeout = send_timeout
        if read_timeout is not None:
            self.read_timeout = read_timeout

    @property
    def connect_timeout(self):
        """Gets the connect_timeout of this TimeoutConfig.

        WAF连接源站超时配置

        :return: The connect_timeout of this TimeoutConfig.
        :rtype: int
        """
        return self._connect_timeout

    @connect_timeout.setter
    def connect_timeout(self, connect_timeout):
        """Sets the connect_timeout of this TimeoutConfig.

        WAF连接源站超时配置

        :param connect_timeout: The connect_timeout of this TimeoutConfig.
        :type connect_timeout: int
        """
        self._connect_timeout = connect_timeout

    @property
    def send_timeout(self):
        """Gets the send_timeout of this TimeoutConfig.

        WAF发送请求到源站超时配置

        :return: The send_timeout of this TimeoutConfig.
        :rtype: int
        """
        return self._send_timeout

    @send_timeout.setter
    def send_timeout(self, send_timeout):
        """Sets the send_timeout of this TimeoutConfig.

        WAF发送请求到源站超时配置

        :param send_timeout: The send_timeout of this TimeoutConfig.
        :type send_timeout: int
        """
        self._send_timeout = send_timeout

    @property
    def read_timeout(self):
        """Gets the read_timeout of this TimeoutConfig.

        WAF接收源站响应超时配置

        :return: The read_timeout of this TimeoutConfig.
        :rtype: int
        """
        return self._read_timeout

    @read_timeout.setter
    def read_timeout(self, read_timeout):
        """Sets the read_timeout of this TimeoutConfig.

        WAF接收源站响应超时配置

        :param read_timeout: The read_timeout of this TimeoutConfig.
        :type read_timeout: int
        """
        self._read_timeout = read_timeout

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
        if not isinstance(other, TimeoutConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
