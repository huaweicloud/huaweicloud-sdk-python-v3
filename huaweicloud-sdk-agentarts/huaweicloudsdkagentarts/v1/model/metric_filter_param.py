# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetricFilterParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'label_name': 'str',
        'label_value': 'str',
        'operator': 'str'
    }

    attribute_map = {
        'label_name': 'label_name',
        'label_value': 'label_value',
        'operator': 'operator'
    }

    def __init__(self, label_name=None, label_value=None, operator=None):
        r"""MetricFilterParam

        The model defined in huaweicloud sdk

        :param label_name: 标签名
        :type label_name: str
        :param label_value: 标签值
        :type label_value: str
        :param operator: 操作类型
        :type operator: str
        """
        
        

        self._label_name = None
        self._label_value = None
        self._operator = None
        self.discriminator = None

        if label_name is not None:
            self.label_name = label_name
        if label_value is not None:
            self.label_value = label_value
        if operator is not None:
            self.operator = operator

    @property
    def label_name(self):
        r"""Gets the label_name of this MetricFilterParam.

        标签名

        :return: The label_name of this MetricFilterParam.
        :rtype: str
        """
        return self._label_name

    @label_name.setter
    def label_name(self, label_name):
        r"""Sets the label_name of this MetricFilterParam.

        标签名

        :param label_name: The label_name of this MetricFilterParam.
        :type label_name: str
        """
        self._label_name = label_name

    @property
    def label_value(self):
        r"""Gets the label_value of this MetricFilterParam.

        标签值

        :return: The label_value of this MetricFilterParam.
        :rtype: str
        """
        return self._label_value

    @label_value.setter
    def label_value(self, label_value):
        r"""Sets the label_value of this MetricFilterParam.

        标签值

        :param label_value: The label_value of this MetricFilterParam.
        :type label_value: str
        """
        self._label_value = label_value

    @property
    def operator(self):
        r"""Gets the operator of this MetricFilterParam.

        操作类型

        :return: The operator of this MetricFilterParam.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        r"""Sets the operator of this MetricFilterParam.

        操作类型

        :param operator: The operator of this MetricFilterParam.
        :type operator: str
        """
        self._operator = operator

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
        if not isinstance(other, MetricFilterParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
