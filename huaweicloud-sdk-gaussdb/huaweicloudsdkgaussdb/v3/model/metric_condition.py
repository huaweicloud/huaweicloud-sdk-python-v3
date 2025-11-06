# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetricCondition:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metric_name': 'str',
        'metric_value': 'int',
        'compare_mode': 'str'
    }

    attribute_map = {
        'metric_name': 'metric_name',
        'metric_value': 'metric_value',
        'compare_mode': 'compare_mode'
    }

    def __init__(self, metric_name=None, metric_value=None, compare_mode=None):
        r"""MetricCondition

        The model defined in huaweicloud sdk

        :param metric_name: **参数描述**:  指标名称。  **约束限制**：  不涉及。  **取值范围**： - cpuTotalUsage：CPU使用率。 - memoryTotalUsage：内存使用率。  **默认取值**：  不涉及。
        :type metric_name: str
        :param metric_value: **参数描述**：  指标变配阈值。  **约束限制**：  取值为百分比的10000倍，比如50%对应的参数值为5000。  **取值范围**：  6000-8000。  **默认取值**：  不涉及。
        :type metric_value: int
        :param compare_mode: **参数描述**：  比较模式。  **约束限制**：  不涉及。。  **取值范围**：  GT：大于。  **默认取值**：  不涉及。
        :type compare_mode: str
        """
        
        

        self._metric_name = None
        self._metric_value = None
        self._compare_mode = None
        self.discriminator = None

        if metric_name is not None:
            self.metric_name = metric_name
        if metric_value is not None:
            self.metric_value = metric_value
        if compare_mode is not None:
            self.compare_mode = compare_mode

    @property
    def metric_name(self):
        r"""Gets the metric_name of this MetricCondition.

        **参数描述**:  指标名称。  **约束限制**：  不涉及。  **取值范围**： - cpuTotalUsage：CPU使用率。 - memoryTotalUsage：内存使用率。  **默认取值**：  不涉及。

        :return: The metric_name of this MetricCondition.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        r"""Sets the metric_name of this MetricCondition.

        **参数描述**:  指标名称。  **约束限制**：  不涉及。  **取值范围**： - cpuTotalUsage：CPU使用率。 - memoryTotalUsage：内存使用率。  **默认取值**：  不涉及。

        :param metric_name: The metric_name of this MetricCondition.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def metric_value(self):
        r"""Gets the metric_value of this MetricCondition.

        **参数描述**：  指标变配阈值。  **约束限制**：  取值为百分比的10000倍，比如50%对应的参数值为5000。  **取值范围**：  6000-8000。  **默认取值**：  不涉及。

        :return: The metric_value of this MetricCondition.
        :rtype: int
        """
        return self._metric_value

    @metric_value.setter
    def metric_value(self, metric_value):
        r"""Sets the metric_value of this MetricCondition.

        **参数描述**：  指标变配阈值。  **约束限制**：  取值为百分比的10000倍，比如50%对应的参数值为5000。  **取值范围**：  6000-8000。  **默认取值**：  不涉及。

        :param metric_value: The metric_value of this MetricCondition.
        :type metric_value: int
        """
        self._metric_value = metric_value

    @property
    def compare_mode(self):
        r"""Gets the compare_mode of this MetricCondition.

        **参数描述**：  比较模式。  **约束限制**：  不涉及。。  **取值范围**：  GT：大于。  **默认取值**：  不涉及。

        :return: The compare_mode of this MetricCondition.
        :rtype: str
        """
        return self._compare_mode

    @compare_mode.setter
    def compare_mode(self, compare_mode):
        r"""Sets the compare_mode of this MetricCondition.

        **参数描述**：  比较模式。  **约束限制**：  不涉及。。  **取值范围**：  GT：大于。  **默认取值**：  不涉及。

        :param compare_mode: The compare_mode of this MetricCondition.
        :type compare_mode: str
        """
        self._compare_mode = compare_mode

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
        if not isinstance(other, MetricCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
