# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AggregateMetric:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'inputs': 'list[InputParam]',
        'metric_name': 'str',
        'expression': 'str'
    }

    attribute_map = {
        'inputs': 'inputs',
        'metric_name': 'metric_name',
        'expression': 'expression'
    }

    def __init__(self, inputs=None, metric_name=None, expression=None):
        r"""AggregateMetric

        The model defined in huaweicloud sdk

        :param inputs: 声明属性作为表达式参数
        :type inputs: list[:class:`huaweicloudsdkiotanalytics.v1.InputParam`]
        :param metric_name: 指标名称
        :type metric_name: str
        :param expression: 表达式
        :type expression: str
        """
        
        

        self._inputs = None
        self._metric_name = None
        self._expression = None
        self.discriminator = None

        self.inputs = inputs
        self.metric_name = metric_name
        self.expression = expression

    @property
    def inputs(self):
        r"""Gets the inputs of this AggregateMetric.

        声明属性作为表达式参数

        :return: The inputs of this AggregateMetric.
        :rtype: list[:class:`huaweicloudsdkiotanalytics.v1.InputParam`]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        r"""Sets the inputs of this AggregateMetric.

        声明属性作为表达式参数

        :param inputs: The inputs of this AggregateMetric.
        :type inputs: list[:class:`huaweicloudsdkiotanalytics.v1.InputParam`]
        """
        self._inputs = inputs

    @property
    def metric_name(self):
        r"""Gets the metric_name of this AggregateMetric.

        指标名称

        :return: The metric_name of this AggregateMetric.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        r"""Sets the metric_name of this AggregateMetric.

        指标名称

        :param metric_name: The metric_name of this AggregateMetric.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def expression(self):
        r"""Gets the expression of this AggregateMetric.

        表达式

        :return: The expression of this AggregateMetric.
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        r"""Sets the expression of this AggregateMetric.

        表达式

        :param expression: The expression of this AggregateMetric.
        :type expression: str
        """
        self._expression = expression

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
        if not isinstance(other, AggregateMetric):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
