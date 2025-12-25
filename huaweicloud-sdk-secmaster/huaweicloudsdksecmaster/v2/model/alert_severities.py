# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlertSeverities:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'severity_category': 'str',
        'metric': 'MetricMap'
    }

    attribute_map = {
        'severity_category': 'severity_category',
        'metric': 'metric'
    }

    def __init__(self, severity_category=None, metric=None):
        r"""AlertSeverities

        The model defined in huaweicloud sdk

        :param severity_category: **参数解释**: 目录 - SEVERITY 严重性  **约束限制** 不涉及 **取值范围**: - SEVERITY  **默认值** 不涉及  
        :type severity_category: str
        :param metric: 
        :type metric: :class:`huaweicloudsdksecmaster.v2.MetricMap`
        """
        
        

        self._severity_category = None
        self._metric = None
        self.discriminator = None

        if severity_category is not None:
            self.severity_category = severity_category
        if metric is not None:
            self.metric = metric

    @property
    def severity_category(self):
        r"""Gets the severity_category of this AlertSeverities.

        **参数解释**: 目录 - SEVERITY 严重性  **约束限制** 不涉及 **取值范围**: - SEVERITY  **默认值** 不涉及  

        :return: The severity_category of this AlertSeverities.
        :rtype: str
        """
        return self._severity_category

    @severity_category.setter
    def severity_category(self, severity_category):
        r"""Sets the severity_category of this AlertSeverities.

        **参数解释**: 目录 - SEVERITY 严重性  **约束限制** 不涉及 **取值范围**: - SEVERITY  **默认值** 不涉及  

        :param severity_category: The severity_category of this AlertSeverities.
        :type severity_category: str
        """
        self._severity_category = severity_category

    @property
    def metric(self):
        r"""Gets the metric of this AlertSeverities.

        :return: The metric of this AlertSeverities.
        :rtype: :class:`huaweicloudsdksecmaster.v2.MetricMap`
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        r"""Sets the metric of this AlertSeverities.

        :param metric: The metric of this AlertSeverities.
        :type metric: :class:`huaweicloudsdksecmaster.v2.MetricMap`
        """
        self._metric = metric

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
        if not isinstance(other, AlertSeverities):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
