# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAlertRuleTemplateMetricsResponseBodySeverityMetric:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'high': 'int',
        'tips': 'int',
        'fatal': 'int',
        'low': 'int',
        'medium': 'int'
    }

    attribute_map = {
        'high': 'HIGH',
        'tips': 'TIPS',
        'fatal': 'FATAL',
        'low': 'LOW',
        'medium': 'MEDIUM'
    }

    def __init__(self, high=None, tips=None, fatal=None, low=None, medium=None):
        r"""ListAlertRuleTemplateMetricsResponseBodySeverityMetric

        The model defined in huaweicloud sdk

        :param high: HIGH等级数量
        :type high: int
        :param tips: TIPS等级数量
        :type tips: int
        :param fatal: FATAL等级数量
        :type fatal: int
        :param low: LOW等级数量
        :type low: int
        :param medium: MEDIUM等级数量
        :type medium: int
        """
        
        

        self._high = None
        self._tips = None
        self._fatal = None
        self._low = None
        self._medium = None
        self.discriminator = None

        if high is not None:
            self.high = high
        if tips is not None:
            self.tips = tips
        if fatal is not None:
            self.fatal = fatal
        if low is not None:
            self.low = low
        if medium is not None:
            self.medium = medium

    @property
    def high(self):
        r"""Gets the high of this ListAlertRuleTemplateMetricsResponseBodySeverityMetric.

        HIGH等级数量

        :return: The high of this ListAlertRuleTemplateMetricsResponseBodySeverityMetric.
        :rtype: int
        """
        return self._high

    @high.setter
    def high(self, high):
        r"""Sets the high of this ListAlertRuleTemplateMetricsResponseBodySeverityMetric.

        HIGH等级数量

        :param high: The high of this ListAlertRuleTemplateMetricsResponseBodySeverityMetric.
        :type high: int
        """
        self._high = high

    @property
    def tips(self):
        r"""Gets the tips of this ListAlertRuleTemplateMetricsResponseBodySeverityMetric.

        TIPS等级数量

        :return: The tips of this ListAlertRuleTemplateMetricsResponseBodySeverityMetric.
        :rtype: int
        """
        return self._tips

    @tips.setter
    def tips(self, tips):
        r"""Sets the tips of this ListAlertRuleTemplateMetricsResponseBodySeverityMetric.

        TIPS等级数量

        :param tips: The tips of this ListAlertRuleTemplateMetricsResponseBodySeverityMetric.
        :type tips: int
        """
        self._tips = tips

    @property
    def fatal(self):
        r"""Gets the fatal of this ListAlertRuleTemplateMetricsResponseBodySeverityMetric.

        FATAL等级数量

        :return: The fatal of this ListAlertRuleTemplateMetricsResponseBodySeverityMetric.
        :rtype: int
        """
        return self._fatal

    @fatal.setter
    def fatal(self, fatal):
        r"""Sets the fatal of this ListAlertRuleTemplateMetricsResponseBodySeverityMetric.

        FATAL等级数量

        :param fatal: The fatal of this ListAlertRuleTemplateMetricsResponseBodySeverityMetric.
        :type fatal: int
        """
        self._fatal = fatal

    @property
    def low(self):
        r"""Gets the low of this ListAlertRuleTemplateMetricsResponseBodySeverityMetric.

        LOW等级数量

        :return: The low of this ListAlertRuleTemplateMetricsResponseBodySeverityMetric.
        :rtype: int
        """
        return self._low

    @low.setter
    def low(self, low):
        r"""Sets the low of this ListAlertRuleTemplateMetricsResponseBodySeverityMetric.

        LOW等级数量

        :param low: The low of this ListAlertRuleTemplateMetricsResponseBodySeverityMetric.
        :type low: int
        """
        self._low = low

    @property
    def medium(self):
        r"""Gets the medium of this ListAlertRuleTemplateMetricsResponseBodySeverityMetric.

        MEDIUM等级数量

        :return: The medium of this ListAlertRuleTemplateMetricsResponseBodySeverityMetric.
        :rtype: int
        """
        return self._medium

    @medium.setter
    def medium(self, medium):
        r"""Sets the medium of this ListAlertRuleTemplateMetricsResponseBodySeverityMetric.

        MEDIUM等级数量

        :param medium: The medium of this ListAlertRuleTemplateMetricsResponseBodySeverityMetric.
        :type medium: int
        """
        self._medium = medium

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
        if not isinstance(other, ListAlertRuleTemplateMetricsResponseBodySeverityMetric):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
