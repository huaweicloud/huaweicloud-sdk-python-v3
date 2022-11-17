# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HealthCheck:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'protocol': 'str',
        'port': 'int',
        'unhealthy': 'int',
        'timeout': 'int',
        'interval': 'int'
    }

    attribute_map = {
        'protocol': 'protocol',
        'port': 'port',
        'unhealthy': 'unhealthy',
        'timeout': 'timeout',
        'interval': 'interval'
    }

    def __init__(self, protocol=None, port=None, unhealthy=None, timeout=None, interval=None):
        """HealthCheck

        The model defined in huaweicloud sdk

        :param protocol: 当前LVS只支持TCP_CHECK
        :type protocol: str
        :param port: 健康检查端口
        :type port: int
        :param unhealthy: 判定后端不健康的阈值，连续探测失败次数
        :type unhealthy: int
        :param timeout: 探测后端的超时时间，单位秒
        :type timeout: int
        :param interval: 探测后端的间隔时间，单位秒
        :type interval: int
        """
        
        

        self._protocol = None
        self._port = None
        self._unhealthy = None
        self._timeout = None
        self._interval = None
        self.discriminator = None

        if protocol is not None:
            self.protocol = protocol
        if port is not None:
            self.port = port
        if unhealthy is not None:
            self.unhealthy = unhealthy
        if timeout is not None:
            self.timeout = timeout
        if interval is not None:
            self.interval = interval

    @property
    def protocol(self):
        """Gets the protocol of this HealthCheck.

        当前LVS只支持TCP_CHECK

        :return: The protocol of this HealthCheck.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this HealthCheck.

        当前LVS只支持TCP_CHECK

        :param protocol: The protocol of this HealthCheck.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def port(self):
        """Gets the port of this HealthCheck.

        健康检查端口

        :return: The port of this HealthCheck.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this HealthCheck.

        健康检查端口

        :param port: The port of this HealthCheck.
        :type port: int
        """
        self._port = port

    @property
    def unhealthy(self):
        """Gets the unhealthy of this HealthCheck.

        判定后端不健康的阈值，连续探测失败次数

        :return: The unhealthy of this HealthCheck.
        :rtype: int
        """
        return self._unhealthy

    @unhealthy.setter
    def unhealthy(self, unhealthy):
        """Sets the unhealthy of this HealthCheck.

        判定后端不健康的阈值，连续探测失败次数

        :param unhealthy: The unhealthy of this HealthCheck.
        :type unhealthy: int
        """
        self._unhealthy = unhealthy

    @property
    def timeout(self):
        """Gets the timeout of this HealthCheck.

        探测后端的超时时间，单位秒

        :return: The timeout of this HealthCheck.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this HealthCheck.

        探测后端的超时时间，单位秒

        :param timeout: The timeout of this HealthCheck.
        :type timeout: int
        """
        self._timeout = timeout

    @property
    def interval(self):
        """Gets the interval of this HealthCheck.

        探测后端的间隔时间，单位秒

        :return: The interval of this HealthCheck.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this HealthCheck.

        探测后端的间隔时间，单位秒

        :param interval: The interval of this HealthCheck.
        :type interval: int
        """
        self._interval = interval

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
        if not isinstance(other, HealthCheck):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
