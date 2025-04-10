# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProbeDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'exec_command': 'str',
        'tcp_socket': 'TcpSocketDTO',
        'http_get': 'HttpGetDTO',
        'initial_delay_seconds': 'int',
        'timeout_seconds': 'int',
        'period_seconds': 'int',
        'failure_threshold': 'int'
    }

    attribute_map = {
        'exec_command': 'exec_command',
        'tcp_socket': 'tcp_socket',
        'http_get': 'http_get',
        'initial_delay_seconds': 'initial_delay_seconds',
        'timeout_seconds': 'timeout_seconds',
        'period_seconds': 'period_seconds',
        'failure_threshold': 'failure_threshold'
    }

    def __init__(self, exec_command=None, tcp_socket=None, http_get=None, initial_delay_seconds=None, timeout_seconds=None, period_seconds=None, failure_threshold=None):
        r"""ProbeDTO

        The model defined in huaweicloud sdk

        :param exec_command: 执行探测的命令行命令
        :type exec_command: str
        :param tcp_socket: 
        :type tcp_socket: :class:`huaweicloudsdkiotedge.v2.TcpSocketDTO`
        :param http_get: 
        :type http_get: :class:`huaweicloudsdkiotedge.v2.HttpGetDTO`
        :param initial_delay_seconds: 表示从工作负载启动后从多久开始探测
        :type initial_delay_seconds: int
        :param timeout_seconds: 表示探测超时时间
        :type timeout_seconds: int
        :param period_seconds: 检查周期
        :type period_seconds: int
        :param failure_threshold: 失败多少次算不健康
        :type failure_threshold: int
        """
        
        

        self._exec_command = None
        self._tcp_socket = None
        self._http_get = None
        self._initial_delay_seconds = None
        self._timeout_seconds = None
        self._period_seconds = None
        self._failure_threshold = None
        self.discriminator = None

        if exec_command is not None:
            self.exec_command = exec_command
        if tcp_socket is not None:
            self.tcp_socket = tcp_socket
        if http_get is not None:
            self.http_get = http_get
        self.initial_delay_seconds = initial_delay_seconds
        self.timeout_seconds = timeout_seconds
        if period_seconds is not None:
            self.period_seconds = period_seconds
        if failure_threshold is not None:
            self.failure_threshold = failure_threshold

    @property
    def exec_command(self):
        r"""Gets the exec_command of this ProbeDTO.

        执行探测的命令行命令

        :return: The exec_command of this ProbeDTO.
        :rtype: str
        """
        return self._exec_command

    @exec_command.setter
    def exec_command(self, exec_command):
        r"""Sets the exec_command of this ProbeDTO.

        执行探测的命令行命令

        :param exec_command: The exec_command of this ProbeDTO.
        :type exec_command: str
        """
        self._exec_command = exec_command

    @property
    def tcp_socket(self):
        r"""Gets the tcp_socket of this ProbeDTO.

        :return: The tcp_socket of this ProbeDTO.
        :rtype: :class:`huaweicloudsdkiotedge.v2.TcpSocketDTO`
        """
        return self._tcp_socket

    @tcp_socket.setter
    def tcp_socket(self, tcp_socket):
        r"""Sets the tcp_socket of this ProbeDTO.

        :param tcp_socket: The tcp_socket of this ProbeDTO.
        :type tcp_socket: :class:`huaweicloudsdkiotedge.v2.TcpSocketDTO`
        """
        self._tcp_socket = tcp_socket

    @property
    def http_get(self):
        r"""Gets the http_get of this ProbeDTO.

        :return: The http_get of this ProbeDTO.
        :rtype: :class:`huaweicloudsdkiotedge.v2.HttpGetDTO`
        """
        return self._http_get

    @http_get.setter
    def http_get(self, http_get):
        r"""Sets the http_get of this ProbeDTO.

        :param http_get: The http_get of this ProbeDTO.
        :type http_get: :class:`huaweicloudsdkiotedge.v2.HttpGetDTO`
        """
        self._http_get = http_get

    @property
    def initial_delay_seconds(self):
        r"""Gets the initial_delay_seconds of this ProbeDTO.

        表示从工作负载启动后从多久开始探测

        :return: The initial_delay_seconds of this ProbeDTO.
        :rtype: int
        """
        return self._initial_delay_seconds

    @initial_delay_seconds.setter
    def initial_delay_seconds(self, initial_delay_seconds):
        r"""Sets the initial_delay_seconds of this ProbeDTO.

        表示从工作负载启动后从多久开始探测

        :param initial_delay_seconds: The initial_delay_seconds of this ProbeDTO.
        :type initial_delay_seconds: int
        """
        self._initial_delay_seconds = initial_delay_seconds

    @property
    def timeout_seconds(self):
        r"""Gets the timeout_seconds of this ProbeDTO.

        表示探测超时时间

        :return: The timeout_seconds of this ProbeDTO.
        :rtype: int
        """
        return self._timeout_seconds

    @timeout_seconds.setter
    def timeout_seconds(self, timeout_seconds):
        r"""Sets the timeout_seconds of this ProbeDTO.

        表示探测超时时间

        :param timeout_seconds: The timeout_seconds of this ProbeDTO.
        :type timeout_seconds: int
        """
        self._timeout_seconds = timeout_seconds

    @property
    def period_seconds(self):
        r"""Gets the period_seconds of this ProbeDTO.

        检查周期

        :return: The period_seconds of this ProbeDTO.
        :rtype: int
        """
        return self._period_seconds

    @period_seconds.setter
    def period_seconds(self, period_seconds):
        r"""Sets the period_seconds of this ProbeDTO.

        检查周期

        :param period_seconds: The period_seconds of this ProbeDTO.
        :type period_seconds: int
        """
        self._period_seconds = period_seconds

    @property
    def failure_threshold(self):
        r"""Gets the failure_threshold of this ProbeDTO.

        失败多少次算不健康

        :return: The failure_threshold of this ProbeDTO.
        :rtype: int
        """
        return self._failure_threshold

    @failure_threshold.setter
    def failure_threshold(self, failure_threshold):
        r"""Sets the failure_threshold of this ProbeDTO.

        失败多少次算不健康

        :param failure_threshold: The failure_threshold of this ProbeDTO.
        :type failure_threshold: int
        """
        self._failure_threshold = failure_threshold

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
        if not isinstance(other, ProbeDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
