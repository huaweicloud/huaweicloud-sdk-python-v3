# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProbeDetail:

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
        'http_get': 'HttpGetDetail',
        'initial_delay_seconds': 'int',
        'timeout_seconds': 'int'
    }

    attribute_map = {
        'exec_command': 'exec_command',
        'http_get': 'http_get',
        'initial_delay_seconds': 'initial_delay_seconds',
        'timeout_seconds': 'timeout_seconds'
    }

    def __init__(self, exec_command=None, http_get=None, initial_delay_seconds=None, timeout_seconds=None):
        """ProbeDetail

        The model defined in huaweicloud sdk

        :param exec_command: 执行探测的命令行命令，长度1-10240内的字符串
        :type exec_command: str
        :param http_get: 
        :type http_get: :class:`huaweicloudsdkief.v1.HttpGetDetail`
        :param initial_delay_seconds: 表示从工作负载启动后从多久开始探测，大于0且不大于3600的整数，默认为10
        :type initial_delay_seconds: int
        :param timeout_seconds: 表示探测超时时间，大于0且不大于3600的整数，默认为1
        :type timeout_seconds: int
        """
        
        

        self._exec_command = None
        self._http_get = None
        self._initial_delay_seconds = None
        self._timeout_seconds = None
        self.discriminator = None

        if exec_command is not None:
            self.exec_command = exec_command
        if http_get is not None:
            self.http_get = http_get
        if initial_delay_seconds is not None:
            self.initial_delay_seconds = initial_delay_seconds
        if timeout_seconds is not None:
            self.timeout_seconds = timeout_seconds

    @property
    def exec_command(self):
        """Gets the exec_command of this ProbeDetail.

        执行探测的命令行命令，长度1-10240内的字符串

        :return: The exec_command of this ProbeDetail.
        :rtype: str
        """
        return self._exec_command

    @exec_command.setter
    def exec_command(self, exec_command):
        """Sets the exec_command of this ProbeDetail.

        执行探测的命令行命令，长度1-10240内的字符串

        :param exec_command: The exec_command of this ProbeDetail.
        :type exec_command: str
        """
        self._exec_command = exec_command

    @property
    def http_get(self):
        """Gets the http_get of this ProbeDetail.


        :return: The http_get of this ProbeDetail.
        :rtype: :class:`huaweicloudsdkief.v1.HttpGetDetail`
        """
        return self._http_get

    @http_get.setter
    def http_get(self, http_get):
        """Sets the http_get of this ProbeDetail.


        :param http_get: The http_get of this ProbeDetail.
        :type http_get: :class:`huaweicloudsdkief.v1.HttpGetDetail`
        """
        self._http_get = http_get

    @property
    def initial_delay_seconds(self):
        """Gets the initial_delay_seconds of this ProbeDetail.

        表示从工作负载启动后从多久开始探测，大于0且不大于3600的整数，默认为10

        :return: The initial_delay_seconds of this ProbeDetail.
        :rtype: int
        """
        return self._initial_delay_seconds

    @initial_delay_seconds.setter
    def initial_delay_seconds(self, initial_delay_seconds):
        """Sets the initial_delay_seconds of this ProbeDetail.

        表示从工作负载启动后从多久开始探测，大于0且不大于3600的整数，默认为10

        :param initial_delay_seconds: The initial_delay_seconds of this ProbeDetail.
        :type initial_delay_seconds: int
        """
        self._initial_delay_seconds = initial_delay_seconds

    @property
    def timeout_seconds(self):
        """Gets the timeout_seconds of this ProbeDetail.

        表示探测超时时间，大于0且不大于3600的整数，默认为1

        :return: The timeout_seconds of this ProbeDetail.
        :rtype: int
        """
        return self._timeout_seconds

    @timeout_seconds.setter
    def timeout_seconds(self, timeout_seconds):
        """Sets the timeout_seconds of this ProbeDetail.

        表示探测超时时间，大于0且不大于3600的整数，默认为1

        :param timeout_seconds: The timeout_seconds of this ProbeDetail.
        :type timeout_seconds: int
        """
        self._timeout_seconds = timeout_seconds

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
        if not isinstance(other, ProbeDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
