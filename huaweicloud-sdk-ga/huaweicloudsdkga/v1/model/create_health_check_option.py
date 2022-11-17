# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateHealthCheckOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'endpoint_group_id': 'str',
        'protocol': 'HealthCheckProtocol',
        'port': 'int',
        'interval': 'int',
        'timeout': 'int',
        'max_retries': 'int',
        'enabled': 'bool'
    }

    attribute_map = {
        'endpoint_group_id': 'endpoint_group_id',
        'protocol': 'protocol',
        'port': 'port',
        'interval': 'interval',
        'timeout': 'timeout',
        'max_retries': 'max_retries',
        'enabled': 'enabled'
    }

    def __init__(self, endpoint_group_id=None, protocol=None, port=None, interval=None, timeout=None, max_retries=None, enabled=None):
        """CreateHealthCheckOption

        The model defined in huaweicloud sdk

        :param endpoint_group_id: 终端节点组ID。
        :type endpoint_group_id: str
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
        
        

        self._endpoint_group_id = None
        self._protocol = None
        self._port = None
        self._interval = None
        self._timeout = None
        self._max_retries = None
        self._enabled = None
        self.discriminator = None

        self.endpoint_group_id = endpoint_group_id
        self.protocol = protocol
        self.port = port
        self.interval = interval
        self.timeout = timeout
        self.max_retries = max_retries
        self.enabled = enabled

    @property
    def endpoint_group_id(self):
        """Gets the endpoint_group_id of this CreateHealthCheckOption.

        终端节点组ID。

        :return: The endpoint_group_id of this CreateHealthCheckOption.
        :rtype: str
        """
        return self._endpoint_group_id

    @endpoint_group_id.setter
    def endpoint_group_id(self, endpoint_group_id):
        """Sets the endpoint_group_id of this CreateHealthCheckOption.

        终端节点组ID。

        :param endpoint_group_id: The endpoint_group_id of this CreateHealthCheckOption.
        :type endpoint_group_id: str
        """
        self._endpoint_group_id = endpoint_group_id

    @property
    def protocol(self):
        """Gets the protocol of this CreateHealthCheckOption.

        :return: The protocol of this CreateHealthCheckOption.
        :rtype: :class:`huaweicloudsdkga.v1.HealthCheckProtocol`
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this CreateHealthCheckOption.

        :param protocol: The protocol of this CreateHealthCheckOption.
        :type protocol: :class:`huaweicloudsdkga.v1.HealthCheckProtocol`
        """
        self._protocol = protocol

    @property
    def port(self):
        """Gets the port of this CreateHealthCheckOption.

        健康检查的端口。

        :return: The port of this CreateHealthCheckOption.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this CreateHealthCheckOption.

        健康检查的端口。

        :param port: The port of this CreateHealthCheckOption.
        :type port: int
        """
        self._port = port

    @property
    def interval(self):
        """Gets the interval of this CreateHealthCheckOption.

        健康检查的时间间隔，单位为秒。

        :return: The interval of this CreateHealthCheckOption.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this CreateHealthCheckOption.

        健康检查的时间间隔，单位为秒。

        :param interval: The interval of this CreateHealthCheckOption.
        :type interval: int
        """
        self._interval = interval

    @property
    def timeout(self):
        """Gets the timeout of this CreateHealthCheckOption.

        健康检查的超时时间，单位为秒。建议该值小于interval的值。

        :return: The timeout of this CreateHealthCheckOption.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this CreateHealthCheckOption.

        健康检查的超时时间，单位为秒。建议该值小于interval的值。

        :param timeout: The timeout of this CreateHealthCheckOption.
        :type timeout: int
        """
        self._timeout = timeout

    @property
    def max_retries(self):
        """Gets the max_retries of this CreateHealthCheckOption.

        最大重试次数。将终端节点的状态从“健康”设置为“不健康”或从“不健康”设置为“健康”所需的连续健康检查次数。

        :return: The max_retries of this CreateHealthCheckOption.
        :rtype: int
        """
        return self._max_retries

    @max_retries.setter
    def max_retries(self, max_retries):
        """Sets the max_retries of this CreateHealthCheckOption.

        最大重试次数。将终端节点的状态从“健康”设置为“不健康”或从“不健康”设置为“健康”所需的连续健康检查次数。

        :param max_retries: The max_retries of this CreateHealthCheckOption.
        :type max_retries: int
        """
        self._max_retries = max_retries

    @property
    def enabled(self):
        """Gets the enabled of this CreateHealthCheckOption.

        是否开启健康检查。

        :return: The enabled of this CreateHealthCheckOption.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this CreateHealthCheckOption.

        是否开启健康检查。

        :param enabled: The enabled of this CreateHealthCheckOption.
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
        if not isinstance(other, CreateHealthCheckOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
