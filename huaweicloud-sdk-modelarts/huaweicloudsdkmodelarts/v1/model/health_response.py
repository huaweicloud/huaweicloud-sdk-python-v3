# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HealthResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'check_method': 'str',
        'cmd': 'str',
        'url': 'str',
        'protocol': 'str',
        'initial_delay_seconds': 'int',
        'timeout_seconds': 'int',
        'period_seconds': 'int',
        'failure_threshold': 'int'
    }

    attribute_map = {
        'check_method': 'check_method',
        'cmd': 'cmd',
        'url': 'url',
        'protocol': 'protocol',
        'initial_delay_seconds': 'initial_delay_seconds',
        'timeout_seconds': 'timeout_seconds',
        'period_seconds': 'period_seconds',
        'failure_threshold': 'failure_threshold'
    }

    def __init__(self, check_method=None, cmd=None, url=None, protocol=None, initial_delay_seconds=None, timeout_seconds=None, period_seconds=None, failure_threshold=None):
        r"""HealthResponse

        The model defined in huaweicloud sdk

        :param check_method: **参数解释：** 健康检查方式：HTTP 或者 EXEC（命令行）。 **约束限制：** 不涉及。 **取值范围：** - HTTP：超文本传输协议。 - EXEC：命令行。 **默认取值：** 不涉及。
        :type check_method: str
        :param cmd: **参数解释：** 当健康检查方式为EXEC时，配置的命令行。 **约束限制：** 字符长度限制[0, 1024]，不能包含字符：#~^$|%&amp;*&lt;&gt;()&#39;\&quot;[]{} **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type cmd: str
        :param url: **参数解释：** 当健康检查方式为HTTP 时，配置的请求地址。 **约束限制：** 字符长度限制[0, 1024]，首字符为/，后续字符可以是：字母 数字 中划线 下划线 / : **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type url: str
        :param protocol: **参数解释：** 连接协议。默认HTTP。 **约束限制：** 不涉及。 **取值范围：** - HTTPS：超文本传输协议安全版。 - HTTP：超文本传输协议。 - WSS：网络通信协议安全版。 - WS：网络通信协议。 **默认取值：** 不涉及。
        :type protocol: str
        :param initial_delay_seconds: **参数解释：** 执行首次探测时，应该等待的时间，默认30秒，最小1秒。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 默认值为30。
        :type initial_delay_seconds: int
        :param timeout_seconds: **参数解释：** 执行探测的超时时间，默认30秒，最小1秒。 **约束限制：** 不涉及。 **取值范围：** 最小值为1秒。 **默认取值：** 默认值为30秒。
        :type timeout_seconds: int
        :param period_seconds: **参数解释：** 执行健康检查的周期时间，执行探测的频率。默认是10秒，最小1秒。 **约束限制：** 不涉及。 **取值范围：** 最小值为1秒。 **默认取值：** 默认值为10秒。
        :type period_seconds: int
        :param failure_threshold: **参数解释：** 探测成功后，至少连续探测失败多少次才被认定为失败。默认是3。最小值是1。 **约束限制：** 不涉及。 **取值范围：** 最小值为1。 **默认取值：** 默认值为3。
        :type failure_threshold: int
        """
        
        

        self._check_method = None
        self._cmd = None
        self._url = None
        self._protocol = None
        self._initial_delay_seconds = None
        self._timeout_seconds = None
        self._period_seconds = None
        self._failure_threshold = None
        self.discriminator = None

        if check_method is not None:
            self.check_method = check_method
        if cmd is not None:
            self.cmd = cmd
        if url is not None:
            self.url = url
        if protocol is not None:
            self.protocol = protocol
        self.initial_delay_seconds = initial_delay_seconds
        self.timeout_seconds = timeout_seconds
        self.period_seconds = period_seconds
        self.failure_threshold = failure_threshold

    @property
    def check_method(self):
        r"""Gets the check_method of this HealthResponse.

        **参数解释：** 健康检查方式：HTTP 或者 EXEC（命令行）。 **约束限制：** 不涉及。 **取值范围：** - HTTP：超文本传输协议。 - EXEC：命令行。 **默认取值：** 不涉及。

        :return: The check_method of this HealthResponse.
        :rtype: str
        """
        return self._check_method

    @check_method.setter
    def check_method(self, check_method):
        r"""Sets the check_method of this HealthResponse.

        **参数解释：** 健康检查方式：HTTP 或者 EXEC（命令行）。 **约束限制：** 不涉及。 **取值范围：** - HTTP：超文本传输协议。 - EXEC：命令行。 **默认取值：** 不涉及。

        :param check_method: The check_method of this HealthResponse.
        :type check_method: str
        """
        self._check_method = check_method

    @property
    def cmd(self):
        r"""Gets the cmd of this HealthResponse.

        **参数解释：** 当健康检查方式为EXEC时，配置的命令行。 **约束限制：** 字符长度限制[0, 1024]，不能包含字符：#~^$|%&*<>()'\"[]{} **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The cmd of this HealthResponse.
        :rtype: str
        """
        return self._cmd

    @cmd.setter
    def cmd(self, cmd):
        r"""Sets the cmd of this HealthResponse.

        **参数解释：** 当健康检查方式为EXEC时，配置的命令行。 **约束限制：** 字符长度限制[0, 1024]，不能包含字符：#~^$|%&*<>()'\"[]{} **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param cmd: The cmd of this HealthResponse.
        :type cmd: str
        """
        self._cmd = cmd

    @property
    def url(self):
        r"""Gets the url of this HealthResponse.

        **参数解释：** 当健康检查方式为HTTP 时，配置的请求地址。 **约束限制：** 字符长度限制[0, 1024]，首字符为/，后续字符可以是：字母 数字 中划线 下划线 / : **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The url of this HealthResponse.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this HealthResponse.

        **参数解释：** 当健康检查方式为HTTP 时，配置的请求地址。 **约束限制：** 字符长度限制[0, 1024]，首字符为/，后续字符可以是：字母 数字 中划线 下划线 / : **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param url: The url of this HealthResponse.
        :type url: str
        """
        self._url = url

    @property
    def protocol(self):
        r"""Gets the protocol of this HealthResponse.

        **参数解释：** 连接协议。默认HTTP。 **约束限制：** 不涉及。 **取值范围：** - HTTPS：超文本传输协议安全版。 - HTTP：超文本传输协议。 - WSS：网络通信协议安全版。 - WS：网络通信协议。 **默认取值：** 不涉及。

        :return: The protocol of this HealthResponse.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this HealthResponse.

        **参数解释：** 连接协议。默认HTTP。 **约束限制：** 不涉及。 **取值范围：** - HTTPS：超文本传输协议安全版。 - HTTP：超文本传输协议。 - WSS：网络通信协议安全版。 - WS：网络通信协议。 **默认取值：** 不涉及。

        :param protocol: The protocol of this HealthResponse.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def initial_delay_seconds(self):
        r"""Gets the initial_delay_seconds of this HealthResponse.

        **参数解释：** 执行首次探测时，应该等待的时间，默认30秒，最小1秒。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 默认值为30。

        :return: The initial_delay_seconds of this HealthResponse.
        :rtype: int
        """
        return self._initial_delay_seconds

    @initial_delay_seconds.setter
    def initial_delay_seconds(self, initial_delay_seconds):
        r"""Sets the initial_delay_seconds of this HealthResponse.

        **参数解释：** 执行首次探测时，应该等待的时间，默认30秒，最小1秒。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 默认值为30。

        :param initial_delay_seconds: The initial_delay_seconds of this HealthResponse.
        :type initial_delay_seconds: int
        """
        self._initial_delay_seconds = initial_delay_seconds

    @property
    def timeout_seconds(self):
        r"""Gets the timeout_seconds of this HealthResponse.

        **参数解释：** 执行探测的超时时间，默认30秒，最小1秒。 **约束限制：** 不涉及。 **取值范围：** 最小值为1秒。 **默认取值：** 默认值为30秒。

        :return: The timeout_seconds of this HealthResponse.
        :rtype: int
        """
        return self._timeout_seconds

    @timeout_seconds.setter
    def timeout_seconds(self, timeout_seconds):
        r"""Sets the timeout_seconds of this HealthResponse.

        **参数解释：** 执行探测的超时时间，默认30秒，最小1秒。 **约束限制：** 不涉及。 **取值范围：** 最小值为1秒。 **默认取值：** 默认值为30秒。

        :param timeout_seconds: The timeout_seconds of this HealthResponse.
        :type timeout_seconds: int
        """
        self._timeout_seconds = timeout_seconds

    @property
    def period_seconds(self):
        r"""Gets the period_seconds of this HealthResponse.

        **参数解释：** 执行健康检查的周期时间，执行探测的频率。默认是10秒，最小1秒。 **约束限制：** 不涉及。 **取值范围：** 最小值为1秒。 **默认取值：** 默认值为10秒。

        :return: The period_seconds of this HealthResponse.
        :rtype: int
        """
        return self._period_seconds

    @period_seconds.setter
    def period_seconds(self, period_seconds):
        r"""Sets the period_seconds of this HealthResponse.

        **参数解释：** 执行健康检查的周期时间，执行探测的频率。默认是10秒，最小1秒。 **约束限制：** 不涉及。 **取值范围：** 最小值为1秒。 **默认取值：** 默认值为10秒。

        :param period_seconds: The period_seconds of this HealthResponse.
        :type period_seconds: int
        """
        self._period_seconds = period_seconds

    @property
    def failure_threshold(self):
        r"""Gets the failure_threshold of this HealthResponse.

        **参数解释：** 探测成功后，至少连续探测失败多少次才被认定为失败。默认是3。最小值是1。 **约束限制：** 不涉及。 **取值范围：** 最小值为1。 **默认取值：** 默认值为3。

        :return: The failure_threshold of this HealthResponse.
        :rtype: int
        """
        return self._failure_threshold

    @failure_threshold.setter
    def failure_threshold(self, failure_threshold):
        r"""Sets the failure_threshold of this HealthResponse.

        **参数解释：** 探测成功后，至少连续探测失败多少次才被认定为失败。默认是3。最小值是1。 **约束限制：** 不涉及。 **取值范围：** 最小值为1。 **默认取值：** 默认值为3。

        :param failure_threshold: The failure_threshold of this HealthResponse.
        :type failure_threshold: int
        """
        self._failure_threshold = failure_threshold

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, HealthResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
