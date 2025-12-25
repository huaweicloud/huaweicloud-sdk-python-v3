# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateMetricDimension:

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
        'value': 'str'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value'
    }

    def __init__(self, name=None, value=None):
        r"""CreateMetricDimension

        The model defined in huaweicloud sdk

        :param name: **参数解释**： 监控维度名称，如ECS的维度为instance_id。各服务资源的指标维度名称可查看：“[服务维度名称](ces_03_0059.xml)”。 **约束限制**： 不涉及。 **取值范围**： 以字母开头，只能包含字母、数字、“_”、“-”。长度[1,32]个字符。 **默认取值**： 不涉及。 
        :type name: str
        :param value: **参数解释**： 必填。监控维度取值，例如ECS的ID。 **约束限制**： 不涉及。 **取值范围**： 长度为[0,256]个字符。 **默认取值**： 不涉及。 
        :type value: str
        """
        
        

        self._name = None
        self._value = None
        self.discriminator = None

        self.name = name
        if value is not None:
            self.value = value

    @property
    def name(self):
        r"""Gets the name of this CreateMetricDimension.

        **参数解释**： 监控维度名称，如ECS的维度为instance_id。各服务资源的指标维度名称可查看：“[服务维度名称](ces_03_0059.xml)”。 **约束限制**： 不涉及。 **取值范围**： 以字母开头，只能包含字母、数字、“_”、“-”。长度[1,32]个字符。 **默认取值**： 不涉及。 

        :return: The name of this CreateMetricDimension.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateMetricDimension.

        **参数解释**： 监控维度名称，如ECS的维度为instance_id。各服务资源的指标维度名称可查看：“[服务维度名称](ces_03_0059.xml)”。 **约束限制**： 不涉及。 **取值范围**： 以字母开头，只能包含字母、数字、“_”、“-”。长度[1,32]个字符。 **默认取值**： 不涉及。 

        :param name: The name of this CreateMetricDimension.
        :type name: str
        """
        self._name = name

    @property
    def value(self):
        r"""Gets the value of this CreateMetricDimension.

        **参数解释**： 必填。监控维度取值，例如ECS的ID。 **约束限制**： 不涉及。 **取值范围**： 长度为[0,256]个字符。 **默认取值**： 不涉及。 

        :return: The value of this CreateMetricDimension.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this CreateMetricDimension.

        **参数解释**： 必填。监控维度取值，例如ECS的ID。 **约束限制**： 不涉及。 **取值范围**： 长度为[0,256]个字符。 **默认取值**： 不涉及。 

        :param value: The value of this CreateMetricDimension.
        :type value: str
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
        if not isinstance(other, CreateMetricDimension):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
