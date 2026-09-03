# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetricItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metric': 'str',
        'name': 'str',
        'filter': 'str'
    }

    attribute_map = {
        'metric': 'metric',
        'name': 'name',
        'filter': 'filter'
    }

    def __init__(self, metric=None, name=None, filter=None):
        r"""MetricItem

        The model defined in huaweicloud sdk

        :param metric: **参数解释**：  监控指标键名。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type metric: str
        :param name: **参数解释**：  监控指标显示名称。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type name: str
        :param filter: **参数解释**：  监控指标过滤条件。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type filter: str
        """
        
        

        self._metric = None
        self._name = None
        self._filter = None
        self.discriminator = None

        if metric is not None:
            self.metric = metric
        if name is not None:
            self.name = name
        if filter is not None:
            self.filter = filter

    @property
    def metric(self):
        r"""Gets the metric of this MetricItem.

        **参数解释**：  监控指标键名。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The metric of this MetricItem.
        :rtype: str
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        r"""Sets the metric of this MetricItem.

        **参数解释**：  监控指标键名。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param metric: The metric of this MetricItem.
        :type metric: str
        """
        self._metric = metric

    @property
    def name(self):
        r"""Gets the name of this MetricItem.

        **参数解释**：  监控指标显示名称。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The name of this MetricItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this MetricItem.

        **参数解释**：  监控指标显示名称。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param name: The name of this MetricItem.
        :type name: str
        """
        self._name = name

    @property
    def filter(self):
        r"""Gets the filter of this MetricItem.

        **参数解释**：  监控指标过滤条件。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The filter of this MetricItem.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        r"""Sets the filter of this MetricItem.

        **参数解释**：  监控指标过滤条件。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param filter: The filter of this MetricItem.
        :type filter: str
        """
        self._filter = filter

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
        if not isinstance(other, MetricItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
