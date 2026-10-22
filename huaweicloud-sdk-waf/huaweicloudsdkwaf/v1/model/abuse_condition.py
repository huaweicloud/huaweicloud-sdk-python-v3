# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AbuseCondition:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dimension': 'str',
        'metric': 'str',
        'value': 'int'
    }

    attribute_map = {
        'dimension': 'dimension',
        'metric': 'metric',
        'value': 'value'
    }

    def __init__(self, dimension=None, metric=None, value=None):
        r"""AbuseCondition

        The model defined in huaweicloud sdk

        :param dimension: 算力消耗统计维度。input: 仅输入, output: 仅输出, input_output: 输入+输出。call_count仅支持input
        :type dimension: str
        :param metric: 阈值指标类型。call_count: 调用次数, char_count: 字符数
        :type metric: str
        :param value: 阈值数值，必须大于0；call_count最大1000000，char_count最大100000000000000
        :type value: int
        """
        
        

        self._dimension = None
        self._metric = None
        self._value = None
        self.discriminator = None

        if dimension is not None:
            self.dimension = dimension
        if metric is not None:
            self.metric = metric
        if value is not None:
            self.value = value

    @property
    def dimension(self):
        r"""Gets the dimension of this AbuseCondition.

        算力消耗统计维度。input: 仅输入, output: 仅输出, input_output: 输入+输出。call_count仅支持input

        :return: The dimension of this AbuseCondition.
        :rtype: str
        """
        return self._dimension

    @dimension.setter
    def dimension(self, dimension):
        r"""Sets the dimension of this AbuseCondition.

        算力消耗统计维度。input: 仅输入, output: 仅输出, input_output: 输入+输出。call_count仅支持input

        :param dimension: The dimension of this AbuseCondition.
        :type dimension: str
        """
        self._dimension = dimension

    @property
    def metric(self):
        r"""Gets the metric of this AbuseCondition.

        阈值指标类型。call_count: 调用次数, char_count: 字符数

        :return: The metric of this AbuseCondition.
        :rtype: str
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        r"""Sets the metric of this AbuseCondition.

        阈值指标类型。call_count: 调用次数, char_count: 字符数

        :param metric: The metric of this AbuseCondition.
        :type metric: str
        """
        self._metric = metric

    @property
    def value(self):
        r"""Gets the value of this AbuseCondition.

        阈值数值，必须大于0；call_count最大1000000，char_count最大100000000000000

        :return: The value of this AbuseCondition.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this AbuseCondition.

        阈值数值，必须大于0；call_count最大1000000，char_count最大100000000000000

        :param value: The value of this AbuseCondition.
        :type value: int
        """
        self._value = value

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
        if not isinstance(other, AbuseCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
