# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Trigger:

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
        'metric_value': 'str',
        'comparison_operator': 'str',
        'evaluation_periods': 'int'
    }

    attribute_map = {
        'metric_name': 'metric_name',
        'metric_value': 'metric_value',
        'comparison_operator': 'comparison_operator',
        'evaluation_periods': 'evaluation_periods'
    }

    def __init__(self, metric_name=None, metric_value=None, comparison_operator=None, evaluation_periods=None):
        """Trigger

        The model defined in huaweicloud sdk

        :param metric_name: 指标名称。 该触发条件会依据该名称对应指标的值来进行判断。 最大长度为64个字符。
        :type metric_name: str
        :param metric_value: 指标阈值。  触发该条件的指标阈值，只允许输入整数或者带两位小数的数。
        :type metric_value: str
        :param comparison_operator: 指标判断逻辑运算符，包括： - LT：小于 - GT：大于 - LTOE：小于等于 - GTOE：大于等于
        :type comparison_operator: str
        :param evaluation_periods: 判断连续满足指标阈值的周期数(一个周期为5分钟)。 取值范围[1～288]
        :type evaluation_periods: int
        """
        
        

        self._metric_name = None
        self._metric_value = None
        self._comparison_operator = None
        self._evaluation_periods = None
        self.discriminator = None

        self.metric_name = metric_name
        self.metric_value = metric_value
        if comparison_operator is not None:
            self.comparison_operator = comparison_operator
        self.evaluation_periods = evaluation_periods

    @property
    def metric_name(self):
        """Gets the metric_name of this Trigger.

        指标名称。 该触发条件会依据该名称对应指标的值来进行判断。 最大长度为64个字符。

        :return: The metric_name of this Trigger.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """Sets the metric_name of this Trigger.

        指标名称。 该触发条件会依据该名称对应指标的值来进行判断。 最大长度为64个字符。

        :param metric_name: The metric_name of this Trigger.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def metric_value(self):
        """Gets the metric_value of this Trigger.

        指标阈值。  触发该条件的指标阈值，只允许输入整数或者带两位小数的数。

        :return: The metric_value of this Trigger.
        :rtype: str
        """
        return self._metric_value

    @metric_value.setter
    def metric_value(self, metric_value):
        """Sets the metric_value of this Trigger.

        指标阈值。  触发该条件的指标阈值，只允许输入整数或者带两位小数的数。

        :param metric_value: The metric_value of this Trigger.
        :type metric_value: str
        """
        self._metric_value = metric_value

    @property
    def comparison_operator(self):
        """Gets the comparison_operator of this Trigger.

        指标判断逻辑运算符，包括： - LT：小于 - GT：大于 - LTOE：小于等于 - GTOE：大于等于

        :return: The comparison_operator of this Trigger.
        :rtype: str
        """
        return self._comparison_operator

    @comparison_operator.setter
    def comparison_operator(self, comparison_operator):
        """Sets the comparison_operator of this Trigger.

        指标判断逻辑运算符，包括： - LT：小于 - GT：大于 - LTOE：小于等于 - GTOE：大于等于

        :param comparison_operator: The comparison_operator of this Trigger.
        :type comparison_operator: str
        """
        self._comparison_operator = comparison_operator

    @property
    def evaluation_periods(self):
        """Gets the evaluation_periods of this Trigger.

        判断连续满足指标阈值的周期数(一个周期为5分钟)。 取值范围[1～288]

        :return: The evaluation_periods of this Trigger.
        :rtype: int
        """
        return self._evaluation_periods

    @evaluation_periods.setter
    def evaluation_periods(self, evaluation_periods):
        """Sets the evaluation_periods of this Trigger.

        判断连续满足指标阈值的周期数(一个周期为5分钟)。 取值范围[1～288]

        :param evaluation_periods: The evaluation_periods of this Trigger.
        :type evaluation_periods: int
        """
        self._evaluation_periods = evaluation_periods

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
        if not isinstance(other, Trigger):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
