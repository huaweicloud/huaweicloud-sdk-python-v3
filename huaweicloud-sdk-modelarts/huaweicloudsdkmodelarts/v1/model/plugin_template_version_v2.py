# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PluginTemplateVersionV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version': 'str',
        'creation_timestamp': 'str',
        'inputs': 'object',
        'translate': 'object',
        'description': 'str',
        'detail': 'str'
    }

    attribute_map = {
        'version': 'version',
        'creation_timestamp': 'creationTimestamp',
        'inputs': 'inputs',
        'translate': 'translate',
        'description': 'description',
        'detail': 'detail'
    }

    def __init__(self, version=None, creation_timestamp=None, inputs=None, translate=None, description=None, detail=None):
        r"""PluginTemplateVersionV2

        The model defined in huaweicloud sdk

        :param version: **参数解释**：插件模板的版本号。 **取值范围**：不涉及。
        :type version: str
        :param creation_timestamp: **参数解释**：创建时间。 **取值范围**：不涉及。
        :type creation_timestamp: str
        :param inputs: **参数解释**：插件安装参数。
        :type inputs: object
        :param translate: **参数解释**：供界面使用的翻译信息。
        :type translate: object
        :param description: **参数解释**：版本描述信息。 **取值范围**：不涉及。
        :type description: str
        :param detail: **参数解释**：版本描述信息。 **取值范围**：不涉及。
        :type detail: str
        """
        
        

        self._version = None
        self._creation_timestamp = None
        self._inputs = None
        self._translate = None
        self._description = None
        self._detail = None
        self.discriminator = None

        self.version = version
        if creation_timestamp is not None:
            self.creation_timestamp = creation_timestamp
        if inputs is not None:
            self.inputs = inputs
        if translate is not None:
            self.translate = translate
        if description is not None:
            self.description = description
        if detail is not None:
            self.detail = detail

    @property
    def version(self):
        r"""Gets the version of this PluginTemplateVersionV2.

        **参数解释**：插件模板的版本号。 **取值范围**：不涉及。

        :return: The version of this PluginTemplateVersionV2.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this PluginTemplateVersionV2.

        **参数解释**：插件模板的版本号。 **取值范围**：不涉及。

        :param version: The version of this PluginTemplateVersionV2.
        :type version: str
        """
        self._version = version

    @property
    def creation_timestamp(self):
        r"""Gets the creation_timestamp of this PluginTemplateVersionV2.

        **参数解释**：创建时间。 **取值范围**：不涉及。

        :return: The creation_timestamp of this PluginTemplateVersionV2.
        :rtype: str
        """
        return self._creation_timestamp

    @creation_timestamp.setter
    def creation_timestamp(self, creation_timestamp):
        r"""Sets the creation_timestamp of this PluginTemplateVersionV2.

        **参数解释**：创建时间。 **取值范围**：不涉及。

        :param creation_timestamp: The creation_timestamp of this PluginTemplateVersionV2.
        :type creation_timestamp: str
        """
        self._creation_timestamp = creation_timestamp

    @property
    def inputs(self):
        r"""Gets the inputs of this PluginTemplateVersionV2.

        **参数解释**：插件安装参数。

        :return: The inputs of this PluginTemplateVersionV2.
        :rtype: object
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        r"""Sets the inputs of this PluginTemplateVersionV2.

        **参数解释**：插件安装参数。

        :param inputs: The inputs of this PluginTemplateVersionV2.
        :type inputs: object
        """
        self._inputs = inputs

    @property
    def translate(self):
        r"""Gets the translate of this PluginTemplateVersionV2.

        **参数解释**：供界面使用的翻译信息。

        :return: The translate of this PluginTemplateVersionV2.
        :rtype: object
        """
        return self._translate

    @translate.setter
    def translate(self, translate):
        r"""Sets the translate of this PluginTemplateVersionV2.

        **参数解释**：供界面使用的翻译信息。

        :param translate: The translate of this PluginTemplateVersionV2.
        :type translate: object
        """
        self._translate = translate

    @property
    def description(self):
        r"""Gets the description of this PluginTemplateVersionV2.

        **参数解释**：版本描述信息。 **取值范围**：不涉及。

        :return: The description of this PluginTemplateVersionV2.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this PluginTemplateVersionV2.

        **参数解释**：版本描述信息。 **取值范围**：不涉及。

        :param description: The description of this PluginTemplateVersionV2.
        :type description: str
        """
        self._description = description

    @property
    def detail(self):
        r"""Gets the detail of this PluginTemplateVersionV2.

        **参数解释**：版本描述信息。 **取值范围**：不涉及。

        :return: The detail of this PluginTemplateVersionV2.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        r"""Sets the detail of this PluginTemplateVersionV2.

        **参数解释**：版本描述信息。 **取值范围**：不涉及。

        :param detail: The detail of this PluginTemplateVersionV2.
        :type detail: str
        """
        self._detail = detail

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
        if not isinstance(other, PluginTemplateVersionV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
