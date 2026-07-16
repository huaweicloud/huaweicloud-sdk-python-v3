# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PluginTemplateSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'description': 'str',
        'versions': 'dict(str, PluginTemplateVersionV2)'
    }

    attribute_map = {
        'type': 'type',
        'description': 'description',
        'versions': 'versions'
    }

    def __init__(self, type=None, description=None, versions=None):
        r"""PluginTemplateSpec

        The model defined in huaweicloud sdk

        :param type: **参数解释**：插件模板类型。 **取值范围**：可选值如下： - npu-river：NPU驱动 - gpu-driver：GPU驱动
        :type type: str
        :param description: **参数解释**：插件模板描述。 **取值范围**：不涉及。
        :type description: str
        :param versions: **参数解释**：插件模板版本描述信息。
        :type versions: dict(str, PluginTemplateVersionV2)
        """
        
        

        self._type = None
        self._description = None
        self._versions = None
        self.discriminator = None

        self.type = type
        self.description = description
        self.versions = versions

    @property
    def type(self):
        r"""Gets the type of this PluginTemplateSpec.

        **参数解释**：插件模板类型。 **取值范围**：可选值如下： - npu-river：NPU驱动 - gpu-driver：GPU驱动

        :return: The type of this PluginTemplateSpec.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this PluginTemplateSpec.

        **参数解释**：插件模板类型。 **取值范围**：可选值如下： - npu-river：NPU驱动 - gpu-driver：GPU驱动

        :param type: The type of this PluginTemplateSpec.
        :type type: str
        """
        self._type = type

    @property
    def description(self):
        r"""Gets the description of this PluginTemplateSpec.

        **参数解释**：插件模板描述。 **取值范围**：不涉及。

        :return: The description of this PluginTemplateSpec.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this PluginTemplateSpec.

        **参数解释**：插件模板描述。 **取值范围**：不涉及。

        :param description: The description of this PluginTemplateSpec.
        :type description: str
        """
        self._description = description

    @property
    def versions(self):
        r"""Gets the versions of this PluginTemplateSpec.

        **参数解释**：插件模板版本描述信息。

        :return: The versions of this PluginTemplateSpec.
        :rtype: dict(str, PluginTemplateVersionV2)
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        r"""Sets the versions of this PluginTemplateSpec.

        **参数解释**：插件模板版本描述信息。

        :param versions: The versions of this PluginTemplateSpec.
        :type versions: dict(str, PluginTemplateVersionV2)
        """
        self._versions = versions

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
        if not isinstance(other, PluginTemplateSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
