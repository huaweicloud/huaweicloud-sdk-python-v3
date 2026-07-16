# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PluginTemplateSpecV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'optional': 'bool',
        'type': 'str',
        'logo_url': 'str',
        'description': 'str',
        'versions': 'list[PluginTemplateVersionV2]'
    }

    attribute_map = {
        'optional': 'optional',
        'type': 'type',
        'logo_url': 'logoURL',
        'description': 'description',
        'versions': 'versions'
    }

    def __init__(self, optional=None, type=None, logo_url=None, description=None, versions=None):
        r"""PluginTemplateSpecV2

        The model defined in huaweicloud sdk

        :param optional: **参数解释**：是否为必安装插件。 **取值范围**： - true：是 - false：否
        :type optional: bool
        :param type: **参数解释**：插件模板类型。 **取值范围**：可选值如下： - helm：helm类型 - ccePlugin：CCE类型
        :type type: str
        :param logo_url: **参数解释**：Logo图片地址。 **取值范围**：不涉及。
        :type logo_url: str
        :param description: **参数解释**：插件模板描述。 **取值范围**：不涉及。
        :type description: str
        :param versions: **参数解释**：插件模板版本的详细信息。
        :type versions: list[:class:`huaweicloudsdkmodelarts.v1.PluginTemplateVersionV2`]
        """
        
        

        self._optional = None
        self._type = None
        self._logo_url = None
        self._description = None
        self._versions = None
        self.discriminator = None

        self.optional = optional
        if type is not None:
            self.type = type
        if logo_url is not None:
            self.logo_url = logo_url
        if description is not None:
            self.description = description
        self.versions = versions

    @property
    def optional(self):
        r"""Gets the optional of this PluginTemplateSpecV2.

        **参数解释**：是否为必安装插件。 **取值范围**： - true：是 - false：否

        :return: The optional of this PluginTemplateSpecV2.
        :rtype: bool
        """
        return self._optional

    @optional.setter
    def optional(self, optional):
        r"""Sets the optional of this PluginTemplateSpecV2.

        **参数解释**：是否为必安装插件。 **取值范围**： - true：是 - false：否

        :param optional: The optional of this PluginTemplateSpecV2.
        :type optional: bool
        """
        self._optional = optional

    @property
    def type(self):
        r"""Gets the type of this PluginTemplateSpecV2.

        **参数解释**：插件模板类型。 **取值范围**：可选值如下： - helm：helm类型 - ccePlugin：CCE类型

        :return: The type of this PluginTemplateSpecV2.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this PluginTemplateSpecV2.

        **参数解释**：插件模板类型。 **取值范围**：可选值如下： - helm：helm类型 - ccePlugin：CCE类型

        :param type: The type of this PluginTemplateSpecV2.
        :type type: str
        """
        self._type = type

    @property
    def logo_url(self):
        r"""Gets the logo_url of this PluginTemplateSpecV2.

        **参数解释**：Logo图片地址。 **取值范围**：不涉及。

        :return: The logo_url of this PluginTemplateSpecV2.
        :rtype: str
        """
        return self._logo_url

    @logo_url.setter
    def logo_url(self, logo_url):
        r"""Sets the logo_url of this PluginTemplateSpecV2.

        **参数解释**：Logo图片地址。 **取值范围**：不涉及。

        :param logo_url: The logo_url of this PluginTemplateSpecV2.
        :type logo_url: str
        """
        self._logo_url = logo_url

    @property
    def description(self):
        r"""Gets the description of this PluginTemplateSpecV2.

        **参数解释**：插件模板描述。 **取值范围**：不涉及。

        :return: The description of this PluginTemplateSpecV2.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this PluginTemplateSpecV2.

        **参数解释**：插件模板描述。 **取值范围**：不涉及。

        :param description: The description of this PluginTemplateSpecV2.
        :type description: str
        """
        self._description = description

    @property
    def versions(self):
        r"""Gets the versions of this PluginTemplateSpecV2.

        **参数解释**：插件模板版本的详细信息。

        :return: The versions of this PluginTemplateSpecV2.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.PluginTemplateVersionV2`]
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        r"""Sets the versions of this PluginTemplateSpecV2.

        **参数解释**：插件模板版本的详细信息。

        :param versions: The versions of this PluginTemplateSpecV2.
        :type versions: list[:class:`huaweicloudsdkmodelarts.v1.PluginTemplateVersionV2`]
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
        if not isinstance(other, PluginTemplateSpecV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
