# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAlertRuleTemplateMetricsResponseBodyStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metric': 'ListAlertRuleTemplateMetricsResponseBodyStatusMetric',
        'category': 'str'
    }

    attribute_map = {
        'metric': 'metric',
        'category': 'category'
    }

    def __init__(self, metric=None, category=None):
        r"""ListAlertRuleTemplateMetricsResponseBodyStatus

        The model defined in huaweicloud sdk

        :param metric: 
        :type metric: :class:`huaweicloudsdksecmaster.v2.ListAlertRuleTemplateMetricsResponseBodyStatusMetric`
        :param category: 分类方式
        :type category: str
        """
        
        

        self._metric = None
        self._category = None
        self.discriminator = None

        if metric is not None:
            self.metric = metric
        if category is not None:
            self.category = category

    @property
    def metric(self):
        r"""Gets the metric of this ListAlertRuleTemplateMetricsResponseBodyStatus.

        :return: The metric of this ListAlertRuleTemplateMetricsResponseBodyStatus.
        :rtype: :class:`huaweicloudsdksecmaster.v2.ListAlertRuleTemplateMetricsResponseBodyStatusMetric`
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        r"""Sets the metric of this ListAlertRuleTemplateMetricsResponseBodyStatus.

        :param metric: The metric of this ListAlertRuleTemplateMetricsResponseBodyStatus.
        :type metric: :class:`huaweicloudsdksecmaster.v2.ListAlertRuleTemplateMetricsResponseBodyStatusMetric`
        """
        self._metric = metric

    @property
    def category(self):
        r"""Gets the category of this ListAlertRuleTemplateMetricsResponseBodyStatus.

        分类方式

        :return: The category of this ListAlertRuleTemplateMetricsResponseBodyStatus.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ListAlertRuleTemplateMetricsResponseBodyStatus.

        分类方式

        :param category: The category of this ListAlertRuleTemplateMetricsResponseBodyStatus.
        :type category: str
        """
        self._category = category

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
        if not isinstance(other, ListAlertRuleTemplateMetricsResponseBodyStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
