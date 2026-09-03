# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlertExpression:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'expression_operator': 'str',
        'metric_name': 'str',
        'metric_operator': 'str',
        'metric_threshold': 'int'
    }

    attribute_map = {
        'expression_operator': 'expression_operator',
        'metric_name': 'metric_name',
        'metric_operator': 'metric_operator',
        'metric_threshold': 'metric_threshold'
    }

    def __init__(self, expression_operator=None, metric_name=None, metric_operator=None, metric_threshold=None):
        r"""AlertExpression

        The model defined in huaweicloud sdk

        :param expression_operator: 表达式操作符
        :type expression_operator: str
        :param metric_name: 指标名称
        :type metric_name: str
        :param metric_operator: 指标操作符
        :type metric_operator: str
        :param metric_threshold: 指标阈值
        :type metric_threshold: int
        """
        
        

        self._expression_operator = None
        self._metric_name = None
        self._metric_operator = None
        self._metric_threshold = None
        self.discriminator = None

        if expression_operator is not None:
            self.expression_operator = expression_operator
        if metric_name is not None:
            self.metric_name = metric_name
        if metric_operator is not None:
            self.metric_operator = metric_operator
        if metric_threshold is not None:
            self.metric_threshold = metric_threshold

    @property
    def expression_operator(self):
        r"""Gets the expression_operator of this AlertExpression.

        表达式操作符

        :return: The expression_operator of this AlertExpression.
        :rtype: str
        """
        return self._expression_operator

    @expression_operator.setter
    def expression_operator(self, expression_operator):
        r"""Sets the expression_operator of this AlertExpression.

        表达式操作符

        :param expression_operator: The expression_operator of this AlertExpression.
        :type expression_operator: str
        """
        self._expression_operator = expression_operator

    @property
    def metric_name(self):
        r"""Gets the metric_name of this AlertExpression.

        指标名称

        :return: The metric_name of this AlertExpression.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        r"""Sets the metric_name of this AlertExpression.

        指标名称

        :param metric_name: The metric_name of this AlertExpression.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def metric_operator(self):
        r"""Gets the metric_operator of this AlertExpression.

        指标操作符

        :return: The metric_operator of this AlertExpression.
        :rtype: str
        """
        return self._metric_operator

    @metric_operator.setter
    def metric_operator(self, metric_operator):
        r"""Sets the metric_operator of this AlertExpression.

        指标操作符

        :param metric_operator: The metric_operator of this AlertExpression.
        :type metric_operator: str
        """
        self._metric_operator = metric_operator

    @property
    def metric_threshold(self):
        r"""Gets the metric_threshold of this AlertExpression.

        指标阈值

        :return: The metric_threshold of this AlertExpression.
        :rtype: int
        """
        return self._metric_threshold

    @metric_threshold.setter
    def metric_threshold(self, metric_threshold):
        r"""Sets the metric_threshold of this AlertExpression.

        指标阈值

        :param metric_threshold: The metric_threshold of this AlertExpression.
        :type metric_threshold: int
        """
        self._metric_threshold = metric_threshold

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
        if not isinstance(other, AlertExpression):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
