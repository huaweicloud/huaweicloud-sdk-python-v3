# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateHealthCheckOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'protocol': 'HealthCheckProtocol',
        'port': 'int',
        'interval': 'int',
        'timeout': 'int',
        'max_retries': 'int',
        'enabled': 'bool'
    }

    attribute_map = {
        'protocol': 'protocol',
        'port': 'port',
        'interval': 'interval',
        'timeout': 'timeout',
        'max_retries': 'max_retries',
        'enabled': 'enabled'
    }

    def __init__(self, protocol=None, port=None, interval=None, timeout=None, max_retries=None, enabled=None):
        r"""UpdateHealthCheckOption

        The model defined in huaweicloud sdk

        :param protocol: 
        :type protocol: :class:`huaweicloudsdkga.v1.HealthCheckProtocol`
        :param port: 健康检查的端口。
        :type port: int
        :param interval: 健康检查的时间间隔，单位为秒。
        :type interval: int
        :param timeout: 健康检查的超时时间，单位为秒。建议该值小于interval的值。
        :type timeout: int
        :param max_retries: 最大重试次数。将终端节点的状态从“健康”设置为“不健康”或从“不健康”设置为“健康”所需的连续健康检查次数。
        :type max_retries: int
        :param enabled: 是否开启健康检查。
        :type enabled: bool
        """
        
        

        self._protocol = None
        self._port = None
        self._interval = None
        self._timeout = None
        self._max_retries = None
        self._enabled = None
        self.discriminator = None

        if protocol is not None:
            self.protocol = protocol
        if port is not None:
            self.port = port
        if interval is not None:
            self.interval = interval
        if timeout is not None:
            self.timeout = timeout
        if max_retries is not None:
            self.max_retries = max_retries
        if enabled is not None:
            self.enabled = enabled

    @property
    def protocol(self):
        r"""Gets the protocol of this UpdateHealthCheckOption.

        :return: The protocol of this UpdateHealthCheckOption.
        :rtype: :class:`huaweicloudsdkga.v1.HealthCheckProtocol`
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this UpdateHealthCheckOption.

        :param protocol: The protocol of this UpdateHealthCheckOption.
        :type protocol: :class:`huaweicloudsdkga.v1.HealthCheckProtocol`
        """
        self._protocol = protocol

    @property
    def port(self):
        r"""Gets the port of this UpdateHealthCheckOption.

        健康检查的端口。

        :return: The port of this UpdateHealthCheckOption.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this UpdateHealthCheckOption.

        健康检查的端口。

        :param port: The port of this UpdateHealthCheckOption.
        :type port: int
        """
        self._port = port

    @property
    def interval(self):
        r"""Gets the interval of this UpdateHealthCheckOption.

        健康检查的时间间隔，单位为秒。

        :return: The interval of this UpdateHealthCheckOption.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        r"""Sets the interval of this UpdateHealthCheckOption.

        健康检查的时间间隔，单位为秒。

        :param interval: The interval of this UpdateHealthCheckOption.
        :type interval: int
        """
        self._interval = interval

    @property
    def timeout(self):
        r"""Gets the timeout of this UpdateHealthCheckOption.

        健康检查的超时时间，单位为秒。建议该值小于interval的值。

        :return: The timeout of this UpdateHealthCheckOption.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        r"""Sets the timeout of this UpdateHealthCheckOption.

        健康检查的超时时间，单位为秒。建议该值小于interval的值。

        :param timeout: The timeout of this UpdateHealthCheckOption.
        :type timeout: int
        """
        self._timeout = timeout

    @property
    def max_retries(self):
        r"""Gets the max_retries of this UpdateHealthCheckOption.

        最大重试次数。将终端节点的状态从“健康”设置为“不健康”或从“不健康”设置为“健康”所需的连续健康检查次数。

        :return: The max_retries of this UpdateHealthCheckOption.
        :rtype: int
        """
        return self._max_retries

    @max_retries.setter
    def max_retries(self, max_retries):
        r"""Sets the max_retries of this UpdateHealthCheckOption.

        最大重试次数。将终端节点的状态从“健康”设置为“不健康”或从“不健康”设置为“健康”所需的连续健康检查次数。

        :param max_retries: The max_retries of this UpdateHealthCheckOption.
        :type max_retries: int
        """
        self._max_retries = max_retries

    @property
    def enabled(self):
        r"""Gets the enabled of this UpdateHealthCheckOption.

        是否开启健康检查。

        :return: The enabled of this UpdateHealthCheckOption.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this UpdateHealthCheckOption.

        是否开启健康检查。

        :param enabled: The enabled of this UpdateHealthCheckOption.
        :type enabled: bool
        """
        self._enabled = enabled

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
        if not isinstance(other, UpdateHealthCheckOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
