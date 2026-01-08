# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetricDataPointDimensions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'value': 'str',
        'origin_value': 'str'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value',
        'origin_value': 'origin_value'
    }

    def __init__(self, name=None, value=None, origin_value=None):
        r"""MetricDataPointDimensions

        The model defined in huaweicloud sdk

        :param name: **参数解释**： 资源维度名称 **取值范围**： 最小长度1，最大长度32 
        :type name: str
        :param value: **参数解释**： 资源维度值 **取值范围**： 最小长度1，最大长度256 
        :type value: str
        :param origin_value: **参数解释**： 实际维度信息。 **取值范围**： 字符串长度在 1 到 1024 之间。 
        :type origin_value: str
        """
        
        

        self._name = None
        self._value = None
        self._origin_value = None
        self.discriminator = None

        self.name = name
        self.value = value
        if origin_value is not None:
            self.origin_value = origin_value

    @property
    def name(self):
        r"""Gets the name of this MetricDataPointDimensions.

        **参数解释**： 资源维度名称 **取值范围**： 最小长度1，最大长度32 

        :return: The name of this MetricDataPointDimensions.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this MetricDataPointDimensions.

        **参数解释**： 资源维度名称 **取值范围**： 最小长度1，最大长度32 

        :param name: The name of this MetricDataPointDimensions.
        :type name: str
        """
        self._name = name

    @property
    def value(self):
        r"""Gets the value of this MetricDataPointDimensions.

        **参数解释**： 资源维度值 **取值范围**： 最小长度1，最大长度256 

        :return: The value of this MetricDataPointDimensions.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this MetricDataPointDimensions.

        **参数解释**： 资源维度值 **取值范围**： 最小长度1，最大长度256 

        :param value: The value of this MetricDataPointDimensions.
        :type value: str
        """
        self._value = value

    @property
    def origin_value(self):
        r"""Gets the origin_value of this MetricDataPointDimensions.

        **参数解释**： 实际维度信息。 **取值范围**： 字符串长度在 1 到 1024 之间。 

        :return: The origin_value of this MetricDataPointDimensions.
        :rtype: str
        """
        return self._origin_value

    @origin_value.setter
    def origin_value(self, origin_value):
        r"""Sets the origin_value of this MetricDataPointDimensions.

        **参数解释**： 实际维度信息。 **取值范围**： 字符串长度在 1 到 1024 之间。 

        :param origin_value: The origin_value of this MetricDataPointDimensions.
        :type origin_value: str
        """
        self._origin_value = origin_value

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
        if not isinstance(other, MetricDataPointDimensions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
