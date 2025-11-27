# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchInspectionLostPointsDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'risk_level': 'str',
        'metric': 'str',
        'metric_value': 'float',
        'deducted_points': 'float',
        'deducted_condition': 'str',
        'deducted_formula': 'str',
        'suggestions': 'str'
    }

    attribute_map = {
        'risk_level': 'risk_level',
        'metric': 'metric',
        'metric_value': 'metric_value',
        'deducted_points': 'deducted_points',
        'deducted_condition': 'deducted_condition',
        'deducted_formula': 'deducted_formula',
        'suggestions': 'suggestions'
    }

    def __init__(self, risk_level=None, metric=None, metric_value=None, deducted_points=None, deducted_condition=None, deducted_formula=None, suggestions=None):
        r"""BatchInspectionLostPointsDetail

        The model defined in huaweicloud sdk

        :param risk_level: 风险等级
        :type risk_level: str
        :param metric: 检查项
        :type metric: str
        :param metric_value: 指标值
        :type metric_value: float
        :param deducted_points: 扣分值
        :type deducted_points: float
        :param deducted_condition: 扣分条件
        :type deducted_condition: str
        :param deducted_formula: 扣分规则
        :type deducted_formula: str
        :param suggestions: 优化建议
        :type suggestions: str
        """
        
        

        self._risk_level = None
        self._metric = None
        self._metric_value = None
        self._deducted_points = None
        self._deducted_condition = None
        self._deducted_formula = None
        self._suggestions = None
        self.discriminator = None

        self.risk_level = risk_level
        self.metric = metric
        self.metric_value = metric_value
        self.deducted_points = deducted_points
        self.deducted_condition = deducted_condition
        self.deducted_formula = deducted_formula
        self.suggestions = suggestions

    @property
    def risk_level(self):
        r"""Gets the risk_level of this BatchInspectionLostPointsDetail.

        风险等级

        :return: The risk_level of this BatchInspectionLostPointsDetail.
        :rtype: str
        """
        return self._risk_level

    @risk_level.setter
    def risk_level(self, risk_level):
        r"""Sets the risk_level of this BatchInspectionLostPointsDetail.

        风险等级

        :param risk_level: The risk_level of this BatchInspectionLostPointsDetail.
        :type risk_level: str
        """
        self._risk_level = risk_level

    @property
    def metric(self):
        r"""Gets the metric of this BatchInspectionLostPointsDetail.

        检查项

        :return: The metric of this BatchInspectionLostPointsDetail.
        :rtype: str
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        r"""Sets the metric of this BatchInspectionLostPointsDetail.

        检查项

        :param metric: The metric of this BatchInspectionLostPointsDetail.
        :type metric: str
        """
        self._metric = metric

    @property
    def metric_value(self):
        r"""Gets the metric_value of this BatchInspectionLostPointsDetail.

        指标值

        :return: The metric_value of this BatchInspectionLostPointsDetail.
        :rtype: float
        """
        return self._metric_value

    @metric_value.setter
    def metric_value(self, metric_value):
        r"""Sets the metric_value of this BatchInspectionLostPointsDetail.

        指标值

        :param metric_value: The metric_value of this BatchInspectionLostPointsDetail.
        :type metric_value: float
        """
        self._metric_value = metric_value

    @property
    def deducted_points(self):
        r"""Gets the deducted_points of this BatchInspectionLostPointsDetail.

        扣分值

        :return: The deducted_points of this BatchInspectionLostPointsDetail.
        :rtype: float
        """
        return self._deducted_points

    @deducted_points.setter
    def deducted_points(self, deducted_points):
        r"""Sets the deducted_points of this BatchInspectionLostPointsDetail.

        扣分值

        :param deducted_points: The deducted_points of this BatchInspectionLostPointsDetail.
        :type deducted_points: float
        """
        self._deducted_points = deducted_points

    @property
    def deducted_condition(self):
        r"""Gets the deducted_condition of this BatchInspectionLostPointsDetail.

        扣分条件

        :return: The deducted_condition of this BatchInspectionLostPointsDetail.
        :rtype: str
        """
        return self._deducted_condition

    @deducted_condition.setter
    def deducted_condition(self, deducted_condition):
        r"""Sets the deducted_condition of this BatchInspectionLostPointsDetail.

        扣分条件

        :param deducted_condition: The deducted_condition of this BatchInspectionLostPointsDetail.
        :type deducted_condition: str
        """
        self._deducted_condition = deducted_condition

    @property
    def deducted_formula(self):
        r"""Gets the deducted_formula of this BatchInspectionLostPointsDetail.

        扣分规则

        :return: The deducted_formula of this BatchInspectionLostPointsDetail.
        :rtype: str
        """
        return self._deducted_formula

    @deducted_formula.setter
    def deducted_formula(self, deducted_formula):
        r"""Sets the deducted_formula of this BatchInspectionLostPointsDetail.

        扣分规则

        :param deducted_formula: The deducted_formula of this BatchInspectionLostPointsDetail.
        :type deducted_formula: str
        """
        self._deducted_formula = deducted_formula

    @property
    def suggestions(self):
        r"""Gets the suggestions of this BatchInspectionLostPointsDetail.

        优化建议

        :return: The suggestions of this BatchInspectionLostPointsDetail.
        :rtype: str
        """
        return self._suggestions

    @suggestions.setter
    def suggestions(self, suggestions):
        r"""Sets the suggestions of this BatchInspectionLostPointsDetail.

        优化建议

        :param suggestions: The suggestions of this BatchInspectionLostPointsDetail.
        :type suggestions: str
        """
        self._suggestions = suggestions

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
        if not isinstance(other, BatchInspectionLostPointsDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
