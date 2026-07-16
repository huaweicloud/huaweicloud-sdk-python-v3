# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoreRunWarmUpProbeConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'initial_delay_seconds': 'int',
        'timeout_seconds': 'int',
        'period_seconds': 'int',
        'success_threshold': 'int',
        'failure_threshold': 'int',
        'failure_threshold_seconds': 'int',
        'initial_delay_milliseconds': 'int',
        'timeout_milliseconds': 'int',
        'period_milliseconds': 'int'
    }

    attribute_map = {
        'initial_delay_seconds': 'initial_delay_seconds',
        'timeout_seconds': 'timeout_seconds',
        'period_seconds': 'period_seconds',
        'success_threshold': 'success_threshold',
        'failure_threshold': 'failure_threshold',
        'failure_threshold_seconds': 'failure_threshold_seconds',
        'initial_delay_milliseconds': 'initial_delay_milliseconds',
        'timeout_milliseconds': 'timeout_milliseconds',
        'period_milliseconds': 'period_milliseconds'
    }

    def __init__(self, initial_delay_seconds=None, timeout_seconds=None, period_seconds=None, success_threshold=None, failure_threshold=None, failure_threshold_seconds=None, initial_delay_milliseconds=None, timeout_milliseconds=None, period_milliseconds=None):
        r"""CoreRunWarmUpProbeConfig

        The model defined in huaweicloud sdk

        :param initial_delay_seconds: **参数解释**: 容器启动后多少秒开始探测 
        :type initial_delay_seconds: int
        :param timeout_seconds: **参数解释**: 探测超时时间（秒） 
        :type timeout_seconds: int
        :param period_seconds: **参数解释**: 探测间隔（秒） 
        :type period_seconds: int
        :param success_threshold: **参数解释**: 探测连续成功次数阈值 
        :type success_threshold: int
        :param failure_threshold: **参数解释**: 探测连续失败次数阈值 
        :type failure_threshold: int
        :param failure_threshold_seconds: **参数解释**: 就绪检查连续失败时长阈值（秒） 
        :type failure_threshold_seconds: int
        :param initial_delay_milliseconds: **参数解释**: 开始探测的延迟检查时间（毫秒） 
        :type initial_delay_milliseconds: int
        :param timeout_milliseconds: **参数解释**: 探测超时时间（毫秒） 
        :type timeout_milliseconds: int
        :param period_milliseconds: **参数解释**: 探测间隔（毫秒） 
        :type period_milliseconds: int
        """
        
        

        self._initial_delay_seconds = None
        self._timeout_seconds = None
        self._period_seconds = None
        self._success_threshold = None
        self._failure_threshold = None
        self._failure_threshold_seconds = None
        self._initial_delay_milliseconds = None
        self._timeout_milliseconds = None
        self._period_milliseconds = None
        self.discriminator = None

        if initial_delay_seconds is not None:
            self.initial_delay_seconds = initial_delay_seconds
        if timeout_seconds is not None:
            self.timeout_seconds = timeout_seconds
        if period_seconds is not None:
            self.period_seconds = period_seconds
        if success_threshold is not None:
            self.success_threshold = success_threshold
        if failure_threshold is not None:
            self.failure_threshold = failure_threshold
        if failure_threshold_seconds is not None:
            self.failure_threshold_seconds = failure_threshold_seconds
        if initial_delay_milliseconds is not None:
            self.initial_delay_milliseconds = initial_delay_milliseconds
        if timeout_milliseconds is not None:
            self.timeout_milliseconds = timeout_milliseconds
        if period_milliseconds is not None:
            self.period_milliseconds = period_milliseconds

    @property
    def initial_delay_seconds(self):
        r"""Gets the initial_delay_seconds of this CoreRunWarmUpProbeConfig.

        **参数解释**: 容器启动后多少秒开始探测 

        :return: The initial_delay_seconds of this CoreRunWarmUpProbeConfig.
        :rtype: int
        """
        return self._initial_delay_seconds

    @initial_delay_seconds.setter
    def initial_delay_seconds(self, initial_delay_seconds):
        r"""Sets the initial_delay_seconds of this CoreRunWarmUpProbeConfig.

        **参数解释**: 容器启动后多少秒开始探测 

        :param initial_delay_seconds: The initial_delay_seconds of this CoreRunWarmUpProbeConfig.
        :type initial_delay_seconds: int
        """
        self._initial_delay_seconds = initial_delay_seconds

    @property
    def timeout_seconds(self):
        r"""Gets the timeout_seconds of this CoreRunWarmUpProbeConfig.

        **参数解释**: 探测超时时间（秒） 

        :return: The timeout_seconds of this CoreRunWarmUpProbeConfig.
        :rtype: int
        """
        return self._timeout_seconds

    @timeout_seconds.setter
    def timeout_seconds(self, timeout_seconds):
        r"""Sets the timeout_seconds of this CoreRunWarmUpProbeConfig.

        **参数解释**: 探测超时时间（秒） 

        :param timeout_seconds: The timeout_seconds of this CoreRunWarmUpProbeConfig.
        :type timeout_seconds: int
        """
        self._timeout_seconds = timeout_seconds

    @property
    def period_seconds(self):
        r"""Gets the period_seconds of this CoreRunWarmUpProbeConfig.

        **参数解释**: 探测间隔（秒） 

        :return: The period_seconds of this CoreRunWarmUpProbeConfig.
        :rtype: int
        """
        return self._period_seconds

    @period_seconds.setter
    def period_seconds(self, period_seconds):
        r"""Sets the period_seconds of this CoreRunWarmUpProbeConfig.

        **参数解释**: 探测间隔（秒） 

        :param period_seconds: The period_seconds of this CoreRunWarmUpProbeConfig.
        :type period_seconds: int
        """
        self._period_seconds = period_seconds

    @property
    def success_threshold(self):
        r"""Gets the success_threshold of this CoreRunWarmUpProbeConfig.

        **参数解释**: 探测连续成功次数阈值 

        :return: The success_threshold of this CoreRunWarmUpProbeConfig.
        :rtype: int
        """
        return self._success_threshold

    @success_threshold.setter
    def success_threshold(self, success_threshold):
        r"""Sets the success_threshold of this CoreRunWarmUpProbeConfig.

        **参数解释**: 探测连续成功次数阈值 

        :param success_threshold: The success_threshold of this CoreRunWarmUpProbeConfig.
        :type success_threshold: int
        """
        self._success_threshold = success_threshold

    @property
    def failure_threshold(self):
        r"""Gets the failure_threshold of this CoreRunWarmUpProbeConfig.

        **参数解释**: 探测连续失败次数阈值 

        :return: The failure_threshold of this CoreRunWarmUpProbeConfig.
        :rtype: int
        """
        return self._failure_threshold

    @failure_threshold.setter
    def failure_threshold(self, failure_threshold):
        r"""Sets the failure_threshold of this CoreRunWarmUpProbeConfig.

        **参数解释**: 探测连续失败次数阈值 

        :param failure_threshold: The failure_threshold of this CoreRunWarmUpProbeConfig.
        :type failure_threshold: int
        """
        self._failure_threshold = failure_threshold

    @property
    def failure_threshold_seconds(self):
        r"""Gets the failure_threshold_seconds of this CoreRunWarmUpProbeConfig.

        **参数解释**: 就绪检查连续失败时长阈值（秒） 

        :return: The failure_threshold_seconds of this CoreRunWarmUpProbeConfig.
        :rtype: int
        """
        return self._failure_threshold_seconds

    @failure_threshold_seconds.setter
    def failure_threshold_seconds(self, failure_threshold_seconds):
        r"""Sets the failure_threshold_seconds of this CoreRunWarmUpProbeConfig.

        **参数解释**: 就绪检查连续失败时长阈值（秒） 

        :param failure_threshold_seconds: The failure_threshold_seconds of this CoreRunWarmUpProbeConfig.
        :type failure_threshold_seconds: int
        """
        self._failure_threshold_seconds = failure_threshold_seconds

    @property
    def initial_delay_milliseconds(self):
        r"""Gets the initial_delay_milliseconds of this CoreRunWarmUpProbeConfig.

        **参数解释**: 开始探测的延迟检查时间（毫秒） 

        :return: The initial_delay_milliseconds of this CoreRunWarmUpProbeConfig.
        :rtype: int
        """
        return self._initial_delay_milliseconds

    @initial_delay_milliseconds.setter
    def initial_delay_milliseconds(self, initial_delay_milliseconds):
        r"""Sets the initial_delay_milliseconds of this CoreRunWarmUpProbeConfig.

        **参数解释**: 开始探测的延迟检查时间（毫秒） 

        :param initial_delay_milliseconds: The initial_delay_milliseconds of this CoreRunWarmUpProbeConfig.
        :type initial_delay_milliseconds: int
        """
        self._initial_delay_milliseconds = initial_delay_milliseconds

    @property
    def timeout_milliseconds(self):
        r"""Gets the timeout_milliseconds of this CoreRunWarmUpProbeConfig.

        **参数解释**: 探测超时时间（毫秒） 

        :return: The timeout_milliseconds of this CoreRunWarmUpProbeConfig.
        :rtype: int
        """
        return self._timeout_milliseconds

    @timeout_milliseconds.setter
    def timeout_milliseconds(self, timeout_milliseconds):
        r"""Sets the timeout_milliseconds of this CoreRunWarmUpProbeConfig.

        **参数解释**: 探测超时时间（毫秒） 

        :param timeout_milliseconds: The timeout_milliseconds of this CoreRunWarmUpProbeConfig.
        :type timeout_milliseconds: int
        """
        self._timeout_milliseconds = timeout_milliseconds

    @property
    def period_milliseconds(self):
        r"""Gets the period_milliseconds of this CoreRunWarmUpProbeConfig.

        **参数解释**: 探测间隔（毫秒） 

        :return: The period_milliseconds of this CoreRunWarmUpProbeConfig.
        :rtype: int
        """
        return self._period_milliseconds

    @period_milliseconds.setter
    def period_milliseconds(self, period_milliseconds):
        r"""Sets the period_milliseconds of this CoreRunWarmUpProbeConfig.

        **参数解释**: 探测间隔（毫秒） 

        :param period_milliseconds: The period_milliseconds of this CoreRunWarmUpProbeConfig.
        :type period_milliseconds: int
        """
        self._period_milliseconds = period_milliseconds

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
        if not isinstance(other, CoreRunWarmUpProbeConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
