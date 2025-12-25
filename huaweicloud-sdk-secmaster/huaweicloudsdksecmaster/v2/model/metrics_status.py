# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetricsStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metrics_category': 'str',
        'status_metric': 'StatusMetric'
    }

    attribute_map = {
        'metrics_category': 'metrics_category',
        'status_metric': 'status_metric'
    }

    def __init__(self, metrics_category=None, status_metric=None):
        r"""MetricsStatus

        The model defined in huaweicloud sdk

        :param metrics_category: **参数解释**: 目录指标 - STATUS 状态  **约束限制** 不涉及 **取值范围**: - STATUS  **默认值** 不涉及  
        :type metrics_category: str
        :param status_metric: 
        :type status_metric: :class:`huaweicloudsdksecmaster.v2.StatusMetric`
        """
        
        

        self._metrics_category = None
        self._status_metric = None
        self.discriminator = None

        if metrics_category is not None:
            self.metrics_category = metrics_category
        if status_metric is not None:
            self.status_metric = status_metric

    @property
    def metrics_category(self):
        r"""Gets the metrics_category of this MetricsStatus.

        **参数解释**: 目录指标 - STATUS 状态  **约束限制** 不涉及 **取值范围**: - STATUS  **默认值** 不涉及  

        :return: The metrics_category of this MetricsStatus.
        :rtype: str
        """
        return self._metrics_category

    @metrics_category.setter
    def metrics_category(self, metrics_category):
        r"""Sets the metrics_category of this MetricsStatus.

        **参数解释**: 目录指标 - STATUS 状态  **约束限制** 不涉及 **取值范围**: - STATUS  **默认值** 不涉及  

        :param metrics_category: The metrics_category of this MetricsStatus.
        :type metrics_category: str
        """
        self._metrics_category = metrics_category

    @property
    def status_metric(self):
        r"""Gets the status_metric of this MetricsStatus.

        :return: The status_metric of this MetricsStatus.
        :rtype: :class:`huaweicloudsdksecmaster.v2.StatusMetric`
        """
        return self._status_metric

    @status_metric.setter
    def status_metric(self, status_metric):
        r"""Sets the status_metric of this MetricsStatus.

        :param status_metric: The status_metric of this MetricsStatus.
        :type status_metric: :class:`huaweicloudsdksecmaster.v2.StatusMetric`
        """
        self._status_metric = status_metric

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
        if not isinstance(other, MetricsStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
