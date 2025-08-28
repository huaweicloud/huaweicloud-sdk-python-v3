# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPluginInstallScriptRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'outside_host': 'bool',
        'batch_install': 'bool',
        'plugin': 'str',
        'operate_type': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'outside_host': 'outside_host',
        'batch_install': 'batch_install',
        'plugin': 'plugin',
        'operate_type': 'operate_type'
    }

    def __init__(self, enterprise_project_id=None, outside_host=None, batch_install=None, plugin=None, operate_type=None):
        r"""ListPluginInstallScriptRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param outside_host: **参数解释**： 是否非华为云 **约束限制**： 不涉及 **取值范围**： - true：是。 - false：否。  **默认取值**： false 
        :type outside_host: bool
        :param batch_install: **参数解释**： 是否批量安装 **约束限制**： 不涉及 **取值范围**： - true：是。 - false：否。  **默认取值**： true 
        :type batch_install: bool
        :param plugin: **参数解释**： 插件类型 **约束限制**： 不涉及 **取值范围**： - opa-docker-authz：docker插件。  **默认取值**： opa-docker-authz 
        :type plugin: str
        :param operate_type: **参数解释**： 操作类型 **约束限制**： 不涉及 **取值范围**： - install：安装。 - upgrade：升级。 - uninstall：卸载。  **默认取值**： install 
        :type operate_type: str
        """
        
        

        self._enterprise_project_id = None
        self._outside_host = None
        self._batch_install = None
        self._plugin = None
        self._operate_type = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if outside_host is not None:
            self.outside_host = outside_host
        if batch_install is not None:
            self.batch_install = batch_install
        self.plugin = plugin
        self.operate_type = operate_type

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListPluginInstallScriptRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListPluginInstallScriptRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListPluginInstallScriptRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListPluginInstallScriptRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def outside_host(self):
        r"""Gets the outside_host of this ListPluginInstallScriptRequest.

        **参数解释**： 是否非华为云 **约束限制**： 不涉及 **取值范围**： - true：是。 - false：否。  **默认取值**： false 

        :return: The outside_host of this ListPluginInstallScriptRequest.
        :rtype: bool
        """
        return self._outside_host

    @outside_host.setter
    def outside_host(self, outside_host):
        r"""Sets the outside_host of this ListPluginInstallScriptRequest.

        **参数解释**： 是否非华为云 **约束限制**： 不涉及 **取值范围**： - true：是。 - false：否。  **默认取值**： false 

        :param outside_host: The outside_host of this ListPluginInstallScriptRequest.
        :type outside_host: bool
        """
        self._outside_host = outside_host

    @property
    def batch_install(self):
        r"""Gets the batch_install of this ListPluginInstallScriptRequest.

        **参数解释**： 是否批量安装 **约束限制**： 不涉及 **取值范围**： - true：是。 - false：否。  **默认取值**： true 

        :return: The batch_install of this ListPluginInstallScriptRequest.
        :rtype: bool
        """
        return self._batch_install

    @batch_install.setter
    def batch_install(self, batch_install):
        r"""Sets the batch_install of this ListPluginInstallScriptRequest.

        **参数解释**： 是否批量安装 **约束限制**： 不涉及 **取值范围**： - true：是。 - false：否。  **默认取值**： true 

        :param batch_install: The batch_install of this ListPluginInstallScriptRequest.
        :type batch_install: bool
        """
        self._batch_install = batch_install

    @property
    def plugin(self):
        r"""Gets the plugin of this ListPluginInstallScriptRequest.

        **参数解释**： 插件类型 **约束限制**： 不涉及 **取值范围**： - opa-docker-authz：docker插件。  **默认取值**： opa-docker-authz 

        :return: The plugin of this ListPluginInstallScriptRequest.
        :rtype: str
        """
        return self._plugin

    @plugin.setter
    def plugin(self, plugin):
        r"""Sets the plugin of this ListPluginInstallScriptRequest.

        **参数解释**： 插件类型 **约束限制**： 不涉及 **取值范围**： - opa-docker-authz：docker插件。  **默认取值**： opa-docker-authz 

        :param plugin: The plugin of this ListPluginInstallScriptRequest.
        :type plugin: str
        """
        self._plugin = plugin

    @property
    def operate_type(self):
        r"""Gets the operate_type of this ListPluginInstallScriptRequest.

        **参数解释**： 操作类型 **约束限制**： 不涉及 **取值范围**： - install：安装。 - upgrade：升级。 - uninstall：卸载。  **默认取值**： install 

        :return: The operate_type of this ListPluginInstallScriptRequest.
        :rtype: str
        """
        return self._operate_type

    @operate_type.setter
    def operate_type(self, operate_type):
        r"""Sets the operate_type of this ListPluginInstallScriptRequest.

        **参数解释**： 操作类型 **约束限制**： 不涉及 **取值范围**： - install：安装。 - upgrade：升级。 - uninstall：卸载。  **默认取值**： install 

        :param operate_type: The operate_type of this ListPluginInstallScriptRequest.
        :type operate_type: str
        """
        self._operate_type = operate_type

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
        if not isinstance(other, ListPluginInstallScriptRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
