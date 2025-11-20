# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PluginControlRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'plugin_code': 'str',
        'operate_all': 'bool',
        'host_id_list': 'list[str]'
    }

    attribute_map = {
        'plugin_code': 'plugin_code',
        'operate_all': 'operate_all',
        'host_id_list': 'host_id_list'
    }

    def __init__(self, plugin_code=None, operate_all=None, host_id_list=None):
        r"""PluginControlRequestBody

        The model defined in huaweicloud sdk

        :param plugin_code: **参数解释**： 插件编码 **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 
        :type plugin_code: str
        :param operate_all: **参数解释**： 是否是全量操作，优先级高于host_id_list，若取值为true且host_id_list不为空，仍执行全量操作 **约束限制**: 不涉及 **取值范围**: - true：全量操作，启动/停止所有符合条件的插件 - false: 非全量操作，仅对host_id_list内服务器执行启动/停止插件操作 **默认取值**: false 
        :type operate_all: bool
        :param host_id_list: **参数解释**： 服务器ID列表 **约束限制**: 不涉及 **取值范围**: 不涉及 **默认取值**: 不涉及 
        :type host_id_list: list[str]
        """
        
        

        self._plugin_code = None
        self._operate_all = None
        self._host_id_list = None
        self.discriminator = None

        self.plugin_code = plugin_code
        if operate_all is not None:
            self.operate_all = operate_all
        if host_id_list is not None:
            self.host_id_list = host_id_list

    @property
    def plugin_code(self):
        r"""Gets the plugin_code of this PluginControlRequestBody.

        **参数解释**： 插件编码 **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :return: The plugin_code of this PluginControlRequestBody.
        :rtype: str
        """
        return self._plugin_code

    @plugin_code.setter
    def plugin_code(self, plugin_code):
        r"""Sets the plugin_code of this PluginControlRequestBody.

        **参数解释**： 插件编码 **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :param plugin_code: The plugin_code of this PluginControlRequestBody.
        :type plugin_code: str
        """
        self._plugin_code = plugin_code

    @property
    def operate_all(self):
        r"""Gets the operate_all of this PluginControlRequestBody.

        **参数解释**： 是否是全量操作，优先级高于host_id_list，若取值为true且host_id_list不为空，仍执行全量操作 **约束限制**: 不涉及 **取值范围**: - true：全量操作，启动/停止所有符合条件的插件 - false: 非全量操作，仅对host_id_list内服务器执行启动/停止插件操作 **默认取值**: false 

        :return: The operate_all of this PluginControlRequestBody.
        :rtype: bool
        """
        return self._operate_all

    @operate_all.setter
    def operate_all(self, operate_all):
        r"""Sets the operate_all of this PluginControlRequestBody.

        **参数解释**： 是否是全量操作，优先级高于host_id_list，若取值为true且host_id_list不为空，仍执行全量操作 **约束限制**: 不涉及 **取值范围**: - true：全量操作，启动/停止所有符合条件的插件 - false: 非全量操作，仅对host_id_list内服务器执行启动/停止插件操作 **默认取值**: false 

        :param operate_all: The operate_all of this PluginControlRequestBody.
        :type operate_all: bool
        """
        self._operate_all = operate_all

    @property
    def host_id_list(self):
        r"""Gets the host_id_list of this PluginControlRequestBody.

        **参数解释**： 服务器ID列表 **约束限制**: 不涉及 **取值范围**: 不涉及 **默认取值**: 不涉及 

        :return: The host_id_list of this PluginControlRequestBody.
        :rtype: list[str]
        """
        return self._host_id_list

    @host_id_list.setter
    def host_id_list(self, host_id_list):
        r"""Sets the host_id_list of this PluginControlRequestBody.

        **参数解释**： 服务器ID列表 **约束限制**: 不涉及 **取值范围**: 不涉及 **默认取值**: 不涉及 

        :param host_id_list: The host_id_list of this PluginControlRequestBody.
        :type host_id_list: list[str]
        """
        self._host_id_list = host_id_list

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
        if not isinstance(other, PluginControlRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
