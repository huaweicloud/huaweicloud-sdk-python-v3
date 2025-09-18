# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRuleReq:

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
        'name': 'str',
        'layout_content': 'str',
        'plugin_id': 'str',
        'plugin_name': 'str',
        'plugin_version': 'str',
        'content': 'list[RuleContent]'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'layout_content': 'layout_content',
        'plugin_id': 'plugin_id',
        'plugin_name': 'plugin_name',
        'plugin_version': 'plugin_version',
        'content': 'content'
    }

    def __init__(self, type=None, name=None, layout_content=None, plugin_id=None, plugin_name=None, plugin_version=None, content=None):
        r"""CreateRuleReq

        The model defined in huaweicloud sdk

        :param type: **参数解释**： 创建规则的类型。 **约束限制**： 不涉及。 **取值范围**： - Build。 - Gate。 - Deploy。 - Test。 - Normal。 **默认取值**： 不涉及。 
        :type type: str
        :param name: **参数解释**： 规则名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type name: str
        :param layout_content: **参数解释**： 布局内容。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type layout_content: str
        :param plugin_id: **参数解释**： 扩展插件唯一ID。可以通过[查询插件版本详情](ShowPluginVersion.xml)接口，获取响应参数中unique_id。 **约束限制**： 不涉及。 **取值范围**： 32位字符，由数字和字母组成。 **默认取值**： 不涉及。 
        :type plugin_id: str
        :param plugin_name: **参数解释**： 扩展插件名称。 **约束限制**： 仅支持输入大小写英文字母、数字、&#39;-&#39;、&#39;_&#39;。 **取值范围**： 1到50位字符。 **默认取值**： 不涉及。 
        :type plugin_name: str
        :param plugin_version: **参数解释**： 插件版本号。 **约束限制**： 必须是类似 x.xx.xx 的格式，其中：x 是 1 到 2 位的数字（范围 0 到 99）。xx 是点后跟随的数字部分，且每部分可以是 1 位或 2 位数字。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type plugin_version: str
        :param content: **参数解释**： 规则属性分组列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type content: list[:class:`huaweicloudsdkcodeartspipeline.v2.RuleContent`]
        """
        
        

        self._type = None
        self._name = None
        self._layout_content = None
        self._plugin_id = None
        self._plugin_name = None
        self._plugin_version = None
        self._content = None
        self.discriminator = None

        self.type = type
        self.name = name
        self.layout_content = layout_content
        if plugin_id is not None:
            self.plugin_id = plugin_id
        if plugin_name is not None:
            self.plugin_name = plugin_name
        if plugin_version is not None:
            self.plugin_version = plugin_version
        self.content = content

    @property
    def type(self):
        r"""Gets the type of this CreateRuleReq.

        **参数解释**： 创建规则的类型。 **约束限制**： 不涉及。 **取值范围**： - Build。 - Gate。 - Deploy。 - Test。 - Normal。 **默认取值**： 不涉及。 

        :return: The type of this CreateRuleReq.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateRuleReq.

        **参数解释**： 创建规则的类型。 **约束限制**： 不涉及。 **取值范围**： - Build。 - Gate。 - Deploy。 - Test。 - Normal。 **默认取值**： 不涉及。 

        :param type: The type of this CreateRuleReq.
        :type type: str
        """
        self._type = type

    @property
    def name(self):
        r"""Gets the name of this CreateRuleReq.

        **参数解释**： 规则名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The name of this CreateRuleReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateRuleReq.

        **参数解释**： 规则名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param name: The name of this CreateRuleReq.
        :type name: str
        """
        self._name = name

    @property
    def layout_content(self):
        r"""Gets the layout_content of this CreateRuleReq.

        **参数解释**： 布局内容。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The layout_content of this CreateRuleReq.
        :rtype: str
        """
        return self._layout_content

    @layout_content.setter
    def layout_content(self, layout_content):
        r"""Sets the layout_content of this CreateRuleReq.

        **参数解释**： 布局内容。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param layout_content: The layout_content of this CreateRuleReq.
        :type layout_content: str
        """
        self._layout_content = layout_content

    @property
    def plugin_id(self):
        r"""Gets the plugin_id of this CreateRuleReq.

        **参数解释**： 扩展插件唯一ID。可以通过[查询插件版本详情](ShowPluginVersion.xml)接口，获取响应参数中unique_id。 **约束限制**： 不涉及。 **取值范围**： 32位字符，由数字和字母组成。 **默认取值**： 不涉及。 

        :return: The plugin_id of this CreateRuleReq.
        :rtype: str
        """
        return self._plugin_id

    @plugin_id.setter
    def plugin_id(self, plugin_id):
        r"""Sets the plugin_id of this CreateRuleReq.

        **参数解释**： 扩展插件唯一ID。可以通过[查询插件版本详情](ShowPluginVersion.xml)接口，获取响应参数中unique_id。 **约束限制**： 不涉及。 **取值范围**： 32位字符，由数字和字母组成。 **默认取值**： 不涉及。 

        :param plugin_id: The plugin_id of this CreateRuleReq.
        :type plugin_id: str
        """
        self._plugin_id = plugin_id

    @property
    def plugin_name(self):
        r"""Gets the plugin_name of this CreateRuleReq.

        **参数解释**： 扩展插件名称。 **约束限制**： 仅支持输入大小写英文字母、数字、'-'、'_'。 **取值范围**： 1到50位字符。 **默认取值**： 不涉及。 

        :return: The plugin_name of this CreateRuleReq.
        :rtype: str
        """
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, plugin_name):
        r"""Sets the plugin_name of this CreateRuleReq.

        **参数解释**： 扩展插件名称。 **约束限制**： 仅支持输入大小写英文字母、数字、'-'、'_'。 **取值范围**： 1到50位字符。 **默认取值**： 不涉及。 

        :param plugin_name: The plugin_name of this CreateRuleReq.
        :type plugin_name: str
        """
        self._plugin_name = plugin_name

    @property
    def plugin_version(self):
        r"""Gets the plugin_version of this CreateRuleReq.

        **参数解释**： 插件版本号。 **约束限制**： 必须是类似 x.xx.xx 的格式，其中：x 是 1 到 2 位的数字（范围 0 到 99）。xx 是点后跟随的数字部分，且每部分可以是 1 位或 2 位数字。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The plugin_version of this CreateRuleReq.
        :rtype: str
        """
        return self._plugin_version

    @plugin_version.setter
    def plugin_version(self, plugin_version):
        r"""Sets the plugin_version of this CreateRuleReq.

        **参数解释**： 插件版本号。 **约束限制**： 必须是类似 x.xx.xx 的格式，其中：x 是 1 到 2 位的数字（范围 0 到 99）。xx 是点后跟随的数字部分，且每部分可以是 1 位或 2 位数字。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param plugin_version: The plugin_version of this CreateRuleReq.
        :type plugin_version: str
        """
        self._plugin_version = plugin_version

    @property
    def content(self):
        r"""Gets the content of this CreateRuleReq.

        **参数解释**： 规则属性分组列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The content of this CreateRuleReq.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.RuleContent`]
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this CreateRuleReq.

        **参数解释**： 规则属性分组列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param content: The content of this CreateRuleReq.
        :type content: list[:class:`huaweicloudsdkcodeartspipeline.v2.RuleContent`]
        """
        self._content = content

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
        if not isinstance(other, CreateRuleReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
