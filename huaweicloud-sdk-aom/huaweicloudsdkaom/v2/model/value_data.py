# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ValueData:

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
        'type': 'str',
        'unit': 'str',
        'value': 'float'
    }

    attribute_map = {
        'metric_name': 'metric_name',
        'type': 'type',
        'unit': 'unit',
        'value': 'value'
    }

    def __init__(self, metric_name=None, type=None, unit=None, value=None):
        """ValueData

        The model defined in huaweicloud sdk

        :param metric_name: 指标名称。长度1~255。
        :type metric_name: str
        :param type: 数据的类型。取值范围只能是\&quot;int\&quot;或\&quot;float\&quot;。
        :type type: str
        :param unit: 数据的单位。长度不超过32个字符。
        :type unit: str
        :param value: 指标数据的值。取值范围有效的数值类型。
        :type value: float
        """
        
        

        self._metric_name = None
        self._type = None
        self._unit = None
        self._value = None
        self.discriminator = None

        self.metric_name = metric_name
        if type is not None:
            self.type = type
        if unit is not None:
            self.unit = unit
        self.value = value

    @property
    def metric_name(self):
        """Gets the metric_name of this ValueData.

        指标名称。长度1~255。

        :return: The metric_name of this ValueData.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """Sets the metric_name of this ValueData.

        指标名称。长度1~255。

        :param metric_name: The metric_name of this ValueData.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def type(self):
        """Gets the type of this ValueData.

        数据的类型。取值范围只能是\"int\"或\"float\"。

        :return: The type of this ValueData.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ValueData.

        数据的类型。取值范围只能是\"int\"或\"float\"。

        :param type: The type of this ValueData.
        :type type: str
        """
        self._type = type

    @property
    def unit(self):
        """Gets the unit of this ValueData.

        数据的单位。长度不超过32个字符。

        :return: The unit of this ValueData.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this ValueData.

        数据的单位。长度不超过32个字符。

        :param unit: The unit of this ValueData.
        :type unit: str
        """
        self._unit = unit

    @property
    def value(self):
        """Gets the value of this ValueData.

        指标数据的值。取值范围有效的数值类型。

        :return: The value of this ValueData.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ValueData.

        指标数据的值。取值范围有效的数值类型。

        :param value: The value of this ValueData.
        :type value: float
        """
        self._value = value

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
        if not isinstance(other, ValueData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
