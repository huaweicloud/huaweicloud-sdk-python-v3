# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SparkJobMetricStatistics:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'retry_attempt': 'int',
        'metric_time': 'int',
        'current_cpu': 'int',
        'current_memory': 'int',
        'total_cu_hours': 'float'
    }

    attribute_map = {
        'retry_attempt': 'retry_attempt',
        'metric_time': 'metric_time',
        'current_cpu': 'current_cpu',
        'current_memory': 'current_memory',
        'total_cu_hours': 'total_cu_hours'
    }

    def __init__(self, retry_attempt=None, metric_time=None, current_cpu=None, current_memory=None, total_cu_hours=None):
        r"""SparkJobMetricStatistics

        The model defined in huaweicloud sdk

        :param retry_attempt: **参数解释**：当前第几次重试，用于区分同一作业不同重试批次的指标 **取值范围**：最小值为1。
        :type retry_attempt: int
        :param metric_time: **参数解释**：指标生成时间。 **取值范围**：unix时间戳，单位为毫秒。
        :type metric_time: int
        :param current_cpu: **参数解释**：当前CPU使用量，单位毫核。 **取值范围**：大于等于1000。
        :type current_cpu: int
        :param current_memory: **参数解释**：当前内存使用量，单位MB。 **取值范围**：大于等于1024。
        :type current_memory: int
        :param total_cu_hours: **参数解释**：估算 CU 时（折算后的小时数，保留4位小数，如 2.3500）。 **取值范围**：大于等于0。
        :type total_cu_hours: float
        """
        
        

        self._retry_attempt = None
        self._metric_time = None
        self._current_cpu = None
        self._current_memory = None
        self._total_cu_hours = None
        self.discriminator = None

        if retry_attempt is not None:
            self.retry_attempt = retry_attempt
        if metric_time is not None:
            self.metric_time = metric_time
        if current_cpu is not None:
            self.current_cpu = current_cpu
        if current_memory is not None:
            self.current_memory = current_memory
        if total_cu_hours is not None:
            self.total_cu_hours = total_cu_hours

    @property
    def retry_attempt(self):
        r"""Gets the retry_attempt of this SparkJobMetricStatistics.

        **参数解释**：当前第几次重试，用于区分同一作业不同重试批次的指标 **取值范围**：最小值为1。

        :return: The retry_attempt of this SparkJobMetricStatistics.
        :rtype: int
        """
        return self._retry_attempt

    @retry_attempt.setter
    def retry_attempt(self, retry_attempt):
        r"""Sets the retry_attempt of this SparkJobMetricStatistics.

        **参数解释**：当前第几次重试，用于区分同一作业不同重试批次的指标 **取值范围**：最小值为1。

        :param retry_attempt: The retry_attempt of this SparkJobMetricStatistics.
        :type retry_attempt: int
        """
        self._retry_attempt = retry_attempt

    @property
    def metric_time(self):
        r"""Gets the metric_time of this SparkJobMetricStatistics.

        **参数解释**：指标生成时间。 **取值范围**：unix时间戳，单位为毫秒。

        :return: The metric_time of this SparkJobMetricStatistics.
        :rtype: int
        """
        return self._metric_time

    @metric_time.setter
    def metric_time(self, metric_time):
        r"""Sets the metric_time of this SparkJobMetricStatistics.

        **参数解释**：指标生成时间。 **取值范围**：unix时间戳，单位为毫秒。

        :param metric_time: The metric_time of this SparkJobMetricStatistics.
        :type metric_time: int
        """
        self._metric_time = metric_time

    @property
    def current_cpu(self):
        r"""Gets the current_cpu of this SparkJobMetricStatistics.

        **参数解释**：当前CPU使用量，单位毫核。 **取值范围**：大于等于1000。

        :return: The current_cpu of this SparkJobMetricStatistics.
        :rtype: int
        """
        return self._current_cpu

    @current_cpu.setter
    def current_cpu(self, current_cpu):
        r"""Sets the current_cpu of this SparkJobMetricStatistics.

        **参数解释**：当前CPU使用量，单位毫核。 **取值范围**：大于等于1000。

        :param current_cpu: The current_cpu of this SparkJobMetricStatistics.
        :type current_cpu: int
        """
        self._current_cpu = current_cpu

    @property
    def current_memory(self):
        r"""Gets the current_memory of this SparkJobMetricStatistics.

        **参数解释**：当前内存使用量，单位MB。 **取值范围**：大于等于1024。

        :return: The current_memory of this SparkJobMetricStatistics.
        :rtype: int
        """
        return self._current_memory

    @current_memory.setter
    def current_memory(self, current_memory):
        r"""Sets the current_memory of this SparkJobMetricStatistics.

        **参数解释**：当前内存使用量，单位MB。 **取值范围**：大于等于1024。

        :param current_memory: The current_memory of this SparkJobMetricStatistics.
        :type current_memory: int
        """
        self._current_memory = current_memory

    @property
    def total_cu_hours(self):
        r"""Gets the total_cu_hours of this SparkJobMetricStatistics.

        **参数解释**：估算 CU 时（折算后的小时数，保留4位小数，如 2.3500）。 **取值范围**：大于等于0。

        :return: The total_cu_hours of this SparkJobMetricStatistics.
        :rtype: float
        """
        return self._total_cu_hours

    @total_cu_hours.setter
    def total_cu_hours(self, total_cu_hours):
        r"""Sets the total_cu_hours of this SparkJobMetricStatistics.

        **参数解释**：估算 CU 时（折算后的小时数，保留4位小数，如 2.3500）。 **取值范围**：大于等于0。

        :param total_cu_hours: The total_cu_hours of this SparkJobMetricStatistics.
        :type total_cu_hours: float
        """
        self._total_cu_hours = total_cu_hours

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
        if not isinstance(other, SparkJobMetricStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
