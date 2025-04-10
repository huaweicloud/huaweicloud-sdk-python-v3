# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Probe:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        '_exec': 'ModelExec',
        'http_get': 'HttpGetDetail',
        'initial_delay_seconds': 'int',
        'timeout_seconds': 'int'
    }

    attribute_map = {
        '_exec': 'exec',
        'http_get': 'http_get',
        'initial_delay_seconds': 'initial_delay_seconds',
        'timeout_seconds': 'timeout_seconds'
    }

    def __init__(self, _exec=None, http_get=None, initial_delay_seconds=None, timeout_seconds=None):
        r"""Probe

        The model defined in huaweicloud sdk

        :param _exec: 
        :type _exec: :class:`huaweicloudsdkief.v1.ModelExec`
        :param http_get: 
        :type http_get: :class:`huaweicloudsdkief.v1.HttpGetDetail`
        :param initial_delay_seconds: 表示从工作负载启动后从多久开始探测，大于0且不大于3600的整数，默认为10
        :type initial_delay_seconds: int
        :param timeout_seconds: 表示探测超时时间，大于0且不大于3600的整数，默认为1
        :type timeout_seconds: int
        """
        
        

        self.__exec = None
        self._http_get = None
        self._initial_delay_seconds = None
        self._timeout_seconds = None
        self.discriminator = None

        if _exec is not None:
            self._exec = _exec
        if http_get is not None:
            self.http_get = http_get
        if initial_delay_seconds is not None:
            self.initial_delay_seconds = initial_delay_seconds
        if timeout_seconds is not None:
            self.timeout_seconds = timeout_seconds

    @property
    def _exec(self):
        r"""Gets the _exec of this Probe.

        :return: The _exec of this Probe.
        :rtype: :class:`huaweicloudsdkief.v1.ModelExec`
        """
        return self.__exec

    @_exec.setter
    def _exec(self, _exec):
        r"""Sets the _exec of this Probe.

        :param _exec: The _exec of this Probe.
        :type _exec: :class:`huaweicloudsdkief.v1.ModelExec`
        """
        self.__exec = _exec

    @property
    def http_get(self):
        r"""Gets the http_get of this Probe.

        :return: The http_get of this Probe.
        :rtype: :class:`huaweicloudsdkief.v1.HttpGetDetail`
        """
        return self._http_get

    @http_get.setter
    def http_get(self, http_get):
        r"""Sets the http_get of this Probe.

        :param http_get: The http_get of this Probe.
        :type http_get: :class:`huaweicloudsdkief.v1.HttpGetDetail`
        """
        self._http_get = http_get

    @property
    def initial_delay_seconds(self):
        r"""Gets the initial_delay_seconds of this Probe.

        表示从工作负载启动后从多久开始探测，大于0且不大于3600的整数，默认为10

        :return: The initial_delay_seconds of this Probe.
        :rtype: int
        """
        return self._initial_delay_seconds

    @initial_delay_seconds.setter
    def initial_delay_seconds(self, initial_delay_seconds):
        r"""Sets the initial_delay_seconds of this Probe.

        表示从工作负载启动后从多久开始探测，大于0且不大于3600的整数，默认为10

        :param initial_delay_seconds: The initial_delay_seconds of this Probe.
        :type initial_delay_seconds: int
        """
        self._initial_delay_seconds = initial_delay_seconds

    @property
    def timeout_seconds(self):
        r"""Gets the timeout_seconds of this Probe.

        表示探测超时时间，大于0且不大于3600的整数，默认为1

        :return: The timeout_seconds of this Probe.
        :rtype: int
        """
        return self._timeout_seconds

    @timeout_seconds.setter
    def timeout_seconds(self, timeout_seconds):
        r"""Sets the timeout_seconds of this Probe.

        表示探测超时时间，大于0且不大于3600的整数，默认为1

        :param timeout_seconds: The timeout_seconds of this Probe.
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
        if not isinstance(other, Probe):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
