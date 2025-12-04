# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ParamGroupParameterDiff:

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
        'source_value': 'str',
        'target_value': 'str'
    }

    attribute_map = {
        'name': 'name',
        'source_value': 'source_value',
        'target_value': 'target_value'
    }

    def __init__(self, name=None, source_value=None, target_value=None):
        r"""ParamGroupParameterDiff

        The model defined in huaweicloud sdk

        :param name: **参数解释**：  参数名称  **约束限制**：  不涉及。
        :type name: str
        :param source_value: **参数解释**：  源模板参数值。  **约束限制**：  不涉及。
        :type source_value: str
        :param target_value: **参数解释**：  目标模板参数值。  **约束限制**：  不涉及。
        :type target_value: str
        """
        
        

        self._name = None
        self._source_value = None
        self._target_value = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if source_value is not None:
            self.source_value = source_value
        if target_value is not None:
            self.target_value = target_value

    @property
    def name(self):
        r"""Gets the name of this ParamGroupParameterDiff.

        **参数解释**：  参数名称  **约束限制**：  不涉及。

        :return: The name of this ParamGroupParameterDiff.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ParamGroupParameterDiff.

        **参数解释**：  参数名称  **约束限制**：  不涉及。

        :param name: The name of this ParamGroupParameterDiff.
        :type name: str
        """
        self._name = name

    @property
    def source_value(self):
        r"""Gets the source_value of this ParamGroupParameterDiff.

        **参数解释**：  源模板参数值。  **约束限制**：  不涉及。

        :return: The source_value of this ParamGroupParameterDiff.
        :rtype: str
        """
        return self._source_value

    @source_value.setter
    def source_value(self, source_value):
        r"""Sets the source_value of this ParamGroupParameterDiff.

        **参数解释**：  源模板参数值。  **约束限制**：  不涉及。

        :param source_value: The source_value of this ParamGroupParameterDiff.
        :type source_value: str
        """
        self._source_value = source_value

    @property
    def target_value(self):
        r"""Gets the target_value of this ParamGroupParameterDiff.

        **参数解释**：  目标模板参数值。  **约束限制**：  不涉及。

        :return: The target_value of this ParamGroupParameterDiff.
        :rtype: str
        """
        return self._target_value

    @target_value.setter
    def target_value(self, target_value):
        r"""Sets the target_value of this ParamGroupParameterDiff.

        **参数解释**：  目标模板参数值。  **约束限制**：  不涉及。

        :param target_value: The target_value of this ParamGroupParameterDiff.
        :type target_value: str
        """
        self._target_value = target_value

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
        if not isinstance(other, ParamGroupParameterDiff):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
