# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpgradeConfigurationRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'parameters': 'list[str]'
    }

    attribute_map = {
        'parameters': 'parameters'
    }

    def __init__(self, parameters=None):
        r"""UpgradeConfigurationRequestBody

        The model defined in huaweicloud sdk

        :param parameters: **参数解释**：  需要更新的差异参数名称列表。 - 若参数有值传入：将该参数更新为系统默认模板的值。 - 若参数传入空值或未传入：保留自定义模板中的原有值。  **约束限制**：  不涉及。
        :type parameters: list[str]
        """
        
        

        self._parameters = None
        self.discriminator = None

        if parameters is not None:
            self.parameters = parameters

    @property
    def parameters(self):
        r"""Gets the parameters of this UpgradeConfigurationRequestBody.

        **参数解释**：  需要更新的差异参数名称列表。 - 若参数有值传入：将该参数更新为系统默认模板的值。 - 若参数传入空值或未传入：保留自定义模板中的原有值。  **约束限制**：  不涉及。

        :return: The parameters of this UpgradeConfigurationRequestBody.
        :rtype: list[str]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        r"""Sets the parameters of this UpgradeConfigurationRequestBody.

        **参数解释**：  需要更新的差异参数名称列表。 - 若参数有值传入：将该参数更新为系统默认模板的值。 - 若参数传入空值或未传入：保留自定义模板中的原有值。  **约束限制**：  不涉及。

        :param parameters: The parameters of this UpgradeConfigurationRequestBody.
        :type parameters: list[str]
        """
        self._parameters = parameters

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
        if not isinstance(other, UpgradeConfigurationRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
