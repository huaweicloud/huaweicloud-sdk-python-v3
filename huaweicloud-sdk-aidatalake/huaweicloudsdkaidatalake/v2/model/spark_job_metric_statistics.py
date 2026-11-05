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
        'current_cpu': 'int',
        'current_memory': 'int',
        'total_cu_seconds': 'int'
    }

    attribute_map = {
        'current_cpu': 'current_cpu',
        'current_memory': 'current_memory',
        'total_cu_seconds': 'total_cu_seconds'
    }

    def __init__(self, current_cpu=None, current_memory=None, total_cu_seconds=None):
        r"""SparkJobMetricStatistics

        The model defined in huaweicloud sdk

        :param current_cpu: **参数解释**：当前CPU使用量，单位毫核。 **取值范围**：大于等于1000。
        :type current_cpu: int
        :param current_memory: **参数解释**：当前内存使用量，单位MB。 **取值范围**：大于等于1024。
        :type current_memory: int
        :param total_cu_seconds: **参数解释**：估算 CU 秒（折算后的秒数，四舍五入取整，如 262）。
        :type total_cu_seconds: int
        """
        
        

        self._current_cpu = None
        self._current_memory = None
        self._total_cu_seconds = None
        self.discriminator = None

        if current_cpu is not None:
            self.current_cpu = current_cpu
        if current_memory is not None:
            self.current_memory = current_memory
        if total_cu_seconds is not None:
            self.total_cu_seconds = total_cu_seconds

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
    def total_cu_seconds(self):
        r"""Gets the total_cu_seconds of this SparkJobMetricStatistics.

        **参数解释**：估算 CU 秒（折算后的秒数，四舍五入取整，如 262）。

        :return: The total_cu_seconds of this SparkJobMetricStatistics.
        :rtype: int
        """
        return self._total_cu_seconds

    @total_cu_seconds.setter
    def total_cu_seconds(self, total_cu_seconds):
        r"""Sets the total_cu_seconds of this SparkJobMetricStatistics.

        **参数解释**：估算 CU 秒（折算后的秒数，四舍五入取整，如 262）。

        :param total_cu_seconds: The total_cu_seconds of this SparkJobMetricStatistics.
        :type total_cu_seconds: int
        """
        self._total_cu_seconds = total_cu_seconds

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
