# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AgentBatchImportParamNew:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agent_import_param_list': 'list[AgentImportParamNew]',
        'proxy_region_id': 'int',
        'installer_agent_id': 'str',
        'icagent_install_flag': 'bool',
        'plugin_install_base_param': 'PluginInstallBasicParam',
        'version': 'str',
        'public_net_flag': 'bool'
    }

    attribute_map = {
        'agent_import_param_list': 'agent_import_param_list',
        'proxy_region_id': 'proxy_region_id',
        'installer_agent_id': 'installer_agent_id',
        'icagent_install_flag': 'icagent_install_flag',
        'plugin_install_base_param': 'plugin_install_base_param',
        'version': 'version',
        'public_net_flag': 'public_net_flag'
    }

    def __init__(self, agent_import_param_list=None, proxy_region_id=None, installer_agent_id=None, icagent_install_flag=None, plugin_install_base_param=None, version=None, public_net_flag=None):
        r"""AgentBatchImportParamNew

        The model defined in huaweicloud sdk

        :param agent_import_param_list: 导入待安装UniAgent的机器参数列表。
        :type agent_import_param_list: list[:class:`huaweicloudsdkaom.v4.AgentImportParamNew`]
        :param proxy_region_id: 代理区域ID： - 直连接入填0。 - 代理接入填实际代理区域ID。
        :type proxy_region_id: int
        :param installer_agent_id: 安装机（代理机）的agent ID。
        :type installer_agent_id: str
        :param icagent_install_flag: 是否需要安装ICAgent插件： - true：安装ICAgent插件。默认安装最新版本的ICAgent插件。 - false：不安装ICAgent插件。
        :type icagent_install_flag: bool
        :param plugin_install_base_param: 
        :type plugin_install_base_param: :class:`huaweicloudsdkaom.v4.PluginInstallBasicParam`
        :param version: 待安装的UniAgent版本号。
        :type version: str
        :param public_net_flag: 是否公网接入： - true：公网接入设置。 - false：代理接入设置。
        :type public_net_flag: bool
        """
        
        

        self._agent_import_param_list = None
        self._proxy_region_id = None
        self._installer_agent_id = None
        self._icagent_install_flag = None
        self._plugin_install_base_param = None
        self._version = None
        self._public_net_flag = None
        self.discriminator = None

        self.agent_import_param_list = agent_import_param_list
        self.proxy_region_id = proxy_region_id
        self.installer_agent_id = installer_agent_id
        if icagent_install_flag is not None:
            self.icagent_install_flag = icagent_install_flag
        if plugin_install_base_param is not None:
            self.plugin_install_base_param = plugin_install_base_param
        self.version = version
        self.public_net_flag = public_net_flag

    @property
    def agent_import_param_list(self):
        r"""Gets the agent_import_param_list of this AgentBatchImportParamNew.

        导入待安装UniAgent的机器参数列表。

        :return: The agent_import_param_list of this AgentBatchImportParamNew.
        :rtype: list[:class:`huaweicloudsdkaom.v4.AgentImportParamNew`]
        """
        return self._agent_import_param_list

    @agent_import_param_list.setter
    def agent_import_param_list(self, agent_import_param_list):
        r"""Sets the agent_import_param_list of this AgentBatchImportParamNew.

        导入待安装UniAgent的机器参数列表。

        :param agent_import_param_list: The agent_import_param_list of this AgentBatchImportParamNew.
        :type agent_import_param_list: list[:class:`huaweicloudsdkaom.v4.AgentImportParamNew`]
        """
        self._agent_import_param_list = agent_import_param_list

    @property
    def proxy_region_id(self):
        r"""Gets the proxy_region_id of this AgentBatchImportParamNew.

        代理区域ID： - 直连接入填0。 - 代理接入填实际代理区域ID。

        :return: The proxy_region_id of this AgentBatchImportParamNew.
        :rtype: int
        """
        return self._proxy_region_id

    @proxy_region_id.setter
    def proxy_region_id(self, proxy_region_id):
        r"""Sets the proxy_region_id of this AgentBatchImportParamNew.

        代理区域ID： - 直连接入填0。 - 代理接入填实际代理区域ID。

        :param proxy_region_id: The proxy_region_id of this AgentBatchImportParamNew.
        :type proxy_region_id: int
        """
        self._proxy_region_id = proxy_region_id

    @property
    def installer_agent_id(self):
        r"""Gets the installer_agent_id of this AgentBatchImportParamNew.

        安装机（代理机）的agent ID。

        :return: The installer_agent_id of this AgentBatchImportParamNew.
        :rtype: str
        """
        return self._installer_agent_id

    @installer_agent_id.setter
    def installer_agent_id(self, installer_agent_id):
        r"""Sets the installer_agent_id of this AgentBatchImportParamNew.

        安装机（代理机）的agent ID。

        :param installer_agent_id: The installer_agent_id of this AgentBatchImportParamNew.
        :type installer_agent_id: str
        """
        self._installer_agent_id = installer_agent_id

    @property
    def icagent_install_flag(self):
        r"""Gets the icagent_install_flag of this AgentBatchImportParamNew.

        是否需要安装ICAgent插件： - true：安装ICAgent插件。默认安装最新版本的ICAgent插件。 - false：不安装ICAgent插件。

        :return: The icagent_install_flag of this AgentBatchImportParamNew.
        :rtype: bool
        """
        return self._icagent_install_flag

    @icagent_install_flag.setter
    def icagent_install_flag(self, icagent_install_flag):
        r"""Sets the icagent_install_flag of this AgentBatchImportParamNew.

        是否需要安装ICAgent插件： - true：安装ICAgent插件。默认安装最新版本的ICAgent插件。 - false：不安装ICAgent插件。

        :param icagent_install_flag: The icagent_install_flag of this AgentBatchImportParamNew.
        :type icagent_install_flag: bool
        """
        self._icagent_install_flag = icagent_install_flag

    @property
    def plugin_install_base_param(self):
        r"""Gets the plugin_install_base_param of this AgentBatchImportParamNew.

        :return: The plugin_install_base_param of this AgentBatchImportParamNew.
        :rtype: :class:`huaweicloudsdkaom.v4.PluginInstallBasicParam`
        """
        return self._plugin_install_base_param

    @plugin_install_base_param.setter
    def plugin_install_base_param(self, plugin_install_base_param):
        r"""Sets the plugin_install_base_param of this AgentBatchImportParamNew.

        :param plugin_install_base_param: The plugin_install_base_param of this AgentBatchImportParamNew.
        :type plugin_install_base_param: :class:`huaweicloudsdkaom.v4.PluginInstallBasicParam`
        """
        self._plugin_install_base_param = plugin_install_base_param

    @property
    def version(self):
        r"""Gets the version of this AgentBatchImportParamNew.

        待安装的UniAgent版本号。

        :return: The version of this AgentBatchImportParamNew.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this AgentBatchImportParamNew.

        待安装的UniAgent版本号。

        :param version: The version of this AgentBatchImportParamNew.
        :type version: str
        """
        self._version = version

    @property
    def public_net_flag(self):
        r"""Gets the public_net_flag of this AgentBatchImportParamNew.

        是否公网接入： - true：公网接入设置。 - false：代理接入设置。

        :return: The public_net_flag of this AgentBatchImportParamNew.
        :rtype: bool
        """
        return self._public_net_flag

    @public_net_flag.setter
    def public_net_flag(self, public_net_flag):
        r"""Sets the public_net_flag of this AgentBatchImportParamNew.

        是否公网接入： - true：公网接入设置。 - false：代理接入设置。

        :param public_net_flag: The public_net_flag of this AgentBatchImportParamNew.
        :type public_net_flag: bool
        """
        self._public_net_flag = public_net_flag

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
        if not isinstance(other, AgentBatchImportParamNew):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
