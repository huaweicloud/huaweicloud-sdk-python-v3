# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DTAggregateMetrics:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'inputs': 'list[MetricInput]',
        'expression': 'str',
        'metric_name': 'str'
    }

    attribute_map = {
        'inputs': 'inputs',
        'expression': 'expression',
        'metric_name': 'metric_name'
    }

    def __init__(self, inputs=None, expression=None, metric_name=None):
        """DTAggregateMetrics

        The model defined in huaweicloud sdk

        :param inputs: 定义指标计算查询的输入资产属性列表
        :type inputs: list[:class:`huaweicloudsdkiotanalytics.v1.MetricInput`]
        :param expression: 指标表达式,最多64个字符
        :type expression: str
        :param metric_name: 指标名，指标计算查询的输出指标名称
        :type metric_name: str
        """
        
        

        self._inputs = None
        self._expression = None
        self._metric_name = None
        self.discriminator = None

        self.inputs = inputs
        self.expression = expression
        self.metric_name = metric_name

    @property
    def inputs(self):
        """Gets the inputs of this DTAggregateMetrics.

        定义指标计算查询的输入资产属性列表

        :return: The inputs of this DTAggregateMetrics.
        :rtype: list[:class:`huaweicloudsdkiotanalytics.v1.MetricInput`]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this DTAggregateMetrics.

        定义指标计算查询的输入资产属性列表

        :param inputs: The inputs of this DTAggregateMetrics.
        :type inputs: list[:class:`huaweicloudsdkiotanalytics.v1.MetricInput`]
        """
        self._inputs = inputs

    @property
    def expression(self):
        """Gets the expression of this DTAggregateMetrics.

        指标表达式,最多64个字符

        :return: The expression of this DTAggregateMetrics.
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """Sets the expression of this DTAggregateMetrics.

        指标表达式,最多64个字符

        :param expression: The expression of this DTAggregateMetrics.
        :type expression: str
        """
        self._expression = expression

    @property
    def metric_name(self):
        """Gets the metric_name of this DTAggregateMetrics.

        指标名，指标计算查询的输出指标名称

        :return: The metric_name of this DTAggregateMetrics.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """Sets the metric_name of this DTAggregateMetrics.

        指标名，指标计算查询的输出指标名称

        :param metric_name: The metric_name of this DTAggregateMetrics.
        :type metric_name: str
        """
        self._metric_name = metric_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DTAggregateMetrics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
