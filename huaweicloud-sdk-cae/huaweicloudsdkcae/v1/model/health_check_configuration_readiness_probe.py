# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HealthCheckConfigurationReadinessProbe:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'period_seconds': 'int',
        'initial_delay_seconds': 'int',
        'timeout_seconds': 'int',
        'success_threshold': 'int',
        'failure_threshold': 'int',
        'http_get': 'HealthCheckConfigurationHttpGet',
        'tcp_socket': 'HealthCheckConfigurationTcpSocket',
        '_exec': 'HealthCheckConfigurationExec'
    }

    attribute_map = {
        'period_seconds': 'periodSeconds',
        'initial_delay_seconds': 'initialDelaySeconds',
        'timeout_seconds': 'timeoutSeconds',
        'success_threshold': 'successThreshold',
        'failure_threshold': 'failureThreshold',
        'http_get': 'httpGet',
        'tcp_socket': 'tcpSocket',
        '_exec': 'exec'
    }

    def __init__(self, period_seconds=None, initial_delay_seconds=None, timeout_seconds=None, success_threshold=None, failure_threshold=None, http_get=None, tcp_socket=None, _exec=None):
        """HealthCheckConfigurationReadinessProbe

        The model defined in huaweicloud sdk

        :param period_seconds: 检测周期，单位为s。
        :type period_seconds: int
        :param initial_delay_seconds: 延迟时间，单位为s。
        :type initial_delay_seconds: int
        :param timeout_seconds: 超时时间，单位为s。
        :type timeout_seconds: int
        :param success_threshold: 成功阈值。
        :type success_threshold: int
        :param failure_threshold: 最大失败次数。
        :type failure_threshold: int
        :param http_get: 
        :type http_get: :class:`huaweicloudsdkcae.v1.HealthCheckConfigurationHttpGet`
        :param tcp_socket: 
        :type tcp_socket: :class:`huaweicloudsdkcae.v1.HealthCheckConfigurationTcpSocket`
        :param _exec: 
        :type _exec: :class:`huaweicloudsdkcae.v1.HealthCheckConfigurationExec`
        """
        
        

        self._period_seconds = None
        self._initial_delay_seconds = None
        self._timeout_seconds = None
        self._success_threshold = None
        self._failure_threshold = None
        self._http_get = None
        self._tcp_socket = None
        self.__exec = None
        self.discriminator = None

        if period_seconds is not None:
            self.period_seconds = period_seconds
        if initial_delay_seconds is not None:
            self.initial_delay_seconds = initial_delay_seconds
        if timeout_seconds is not None:
            self.timeout_seconds = timeout_seconds
        if success_threshold is not None:
            self.success_threshold = success_threshold
        if failure_threshold is not None:
            self.failure_threshold = failure_threshold
        if http_get is not None:
            self.http_get = http_get
        if tcp_socket is not None:
            self.tcp_socket = tcp_socket
        if _exec is not None:
            self._exec = _exec

    @property
    def period_seconds(self):
        """Gets the period_seconds of this HealthCheckConfigurationReadinessProbe.

        检测周期，单位为s。

        :return: The period_seconds of this HealthCheckConfigurationReadinessProbe.
        :rtype: int
        """
        return self._period_seconds

    @period_seconds.setter
    def period_seconds(self, period_seconds):
        """Sets the period_seconds of this HealthCheckConfigurationReadinessProbe.

        检测周期，单位为s。

        :param period_seconds: The period_seconds of this HealthCheckConfigurationReadinessProbe.
        :type period_seconds: int
        """
        self._period_seconds = period_seconds

    @property
    def initial_delay_seconds(self):
        """Gets the initial_delay_seconds of this HealthCheckConfigurationReadinessProbe.

        延迟时间，单位为s。

        :return: The initial_delay_seconds of this HealthCheckConfigurationReadinessProbe.
        :rtype: int
        """
        return self._initial_delay_seconds

    @initial_delay_seconds.setter
    def initial_delay_seconds(self, initial_delay_seconds):
        """Sets the initial_delay_seconds of this HealthCheckConfigurationReadinessProbe.

        延迟时间，单位为s。

        :param initial_delay_seconds: The initial_delay_seconds of this HealthCheckConfigurationReadinessProbe.
        :type initial_delay_seconds: int
        """
        self._initial_delay_seconds = initial_delay_seconds

    @property
    def timeout_seconds(self):
        """Gets the timeout_seconds of this HealthCheckConfigurationReadinessProbe.

        超时时间，单位为s。

        :return: The timeout_seconds of this HealthCheckConfigurationReadinessProbe.
        :rtype: int
        """
        return self._timeout_seconds

    @timeout_seconds.setter
    def timeout_seconds(self, timeout_seconds):
        """Sets the timeout_seconds of this HealthCheckConfigurationReadinessProbe.

        超时时间，单位为s。

        :param timeout_seconds: The timeout_seconds of this HealthCheckConfigurationReadinessProbe.
        :type timeout_seconds: int
        """
        self._timeout_seconds = timeout_seconds

    @property
    def success_threshold(self):
        """Gets the success_threshold of this HealthCheckConfigurationReadinessProbe.

        成功阈值。

        :return: The success_threshold of this HealthCheckConfigurationReadinessProbe.
        :rtype: int
        """
        return self._success_threshold

    @success_threshold.setter
    def success_threshold(self, success_threshold):
        """Sets the success_threshold of this HealthCheckConfigurationReadinessProbe.

        成功阈值。

        :param success_threshold: The success_threshold of this HealthCheckConfigurationReadinessProbe.
        :type success_threshold: int
        """
        self._success_threshold = success_threshold

    @property
    def failure_threshold(self):
        """Gets the failure_threshold of this HealthCheckConfigurationReadinessProbe.

        最大失败次数。

        :return: The failure_threshold of this HealthCheckConfigurationReadinessProbe.
        :rtype: int
        """
        return self._failure_threshold

    @failure_threshold.setter
    def failure_threshold(self, failure_threshold):
        """Sets the failure_threshold of this HealthCheckConfigurationReadinessProbe.

        最大失败次数。

        :param failure_threshold: The failure_threshold of this HealthCheckConfigurationReadinessProbe.
        :type failure_threshold: int
        """
        self._failure_threshold = failure_threshold

    @property
    def http_get(self):
        """Gets the http_get of this HealthCheckConfigurationReadinessProbe.

        :return: The http_get of this HealthCheckConfigurationReadinessProbe.
        :rtype: :class:`huaweicloudsdkcae.v1.HealthCheckConfigurationHttpGet`
        """
        return self._http_get

    @http_get.setter
    def http_get(self, http_get):
        """Sets the http_get of this HealthCheckConfigurationReadinessProbe.

        :param http_get: The http_get of this HealthCheckConfigurationReadinessProbe.
        :type http_get: :class:`huaweicloudsdkcae.v1.HealthCheckConfigurationHttpGet`
        """
        self._http_get = http_get

    @property
    def tcp_socket(self):
        """Gets the tcp_socket of this HealthCheckConfigurationReadinessProbe.

        :return: The tcp_socket of this HealthCheckConfigurationReadinessProbe.
        :rtype: :class:`huaweicloudsdkcae.v1.HealthCheckConfigurationTcpSocket`
        """
        return self._tcp_socket

    @tcp_socket.setter
    def tcp_socket(self, tcp_socket):
        """Sets the tcp_socket of this HealthCheckConfigurationReadinessProbe.

        :param tcp_socket: The tcp_socket of this HealthCheckConfigurationReadinessProbe.
        :type tcp_socket: :class:`huaweicloudsdkcae.v1.HealthCheckConfigurationTcpSocket`
        """
        self._tcp_socket = tcp_socket

    @property
    def _exec(self):
        """Gets the _exec of this HealthCheckConfigurationReadinessProbe.

        :return: The _exec of this HealthCheckConfigurationReadinessProbe.
        :rtype: :class:`huaweicloudsdkcae.v1.HealthCheckConfigurationExec`
        """
        return self.__exec

    @_exec.setter
    def _exec(self, _exec):
        """Sets the _exec of this HealthCheckConfigurationReadinessProbe.

        :param _exec: The _exec of this HealthCheckConfigurationReadinessProbe.
        :type _exec: :class:`huaweicloudsdkcae.v1.HealthCheckConfigurationExec`
        """
        self.__exec = _exec

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
        if not isinstance(other, HealthCheckConfigurationReadinessProbe):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
