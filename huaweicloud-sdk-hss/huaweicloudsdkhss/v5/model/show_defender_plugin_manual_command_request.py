# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDefenderPluginManualCommandRequest:

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
        'opt': 'str',
        'network': 'str',
        'agent_type': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'opt': 'opt',
        'network': 'network',
        'agent_type': 'agent_type'
    }

    def __init__(self, enterprise_project_id=None, opt=None, network=None, agent_type=None):
        r"""ShowDefenderPluginManualCommandRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param opt: **参数解释**： 操作类型 **约束限制**： 必填 **取值范围**： - install：安装 - uninstall：卸载  **默认取值**： 不涉及 
        :type opt: str
        :param network: **参数解释**： 网络类型，用于指定返回的命令中使用的下载地址和服务端地址的网络类型 **约束限制**： 非必填 **取值范围**： - public：公网 - internal：内网  **默认取值**： internal 
        :type network: str
        :param agent_type: **参数解释**： 智能体类型，用于区分OpenClaw和自研Claw **约束限制**： 必填 **取值范围**： - OpenClaw：OpenClaw - SelfDevelopedClaw：自研claw  **默认取值**： OpenClaw 
        :type agent_type: str
        """
        
        

        self._enterprise_project_id = None
        self._opt = None
        self._network = None
        self._agent_type = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.opt = opt
        if network is not None:
            self.network = network
        self.agent_type = agent_type

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowDefenderPluginManualCommandRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ShowDefenderPluginManualCommandRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowDefenderPluginManualCommandRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ShowDefenderPluginManualCommandRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def opt(self):
        r"""Gets the opt of this ShowDefenderPluginManualCommandRequest.

        **参数解释**： 操作类型 **约束限制**： 必填 **取值范围**： - install：安装 - uninstall：卸载  **默认取值**： 不涉及 

        :return: The opt of this ShowDefenderPluginManualCommandRequest.
        :rtype: str
        """
        return self._opt

    @opt.setter
    def opt(self, opt):
        r"""Sets the opt of this ShowDefenderPluginManualCommandRequest.

        **参数解释**： 操作类型 **约束限制**： 必填 **取值范围**： - install：安装 - uninstall：卸载  **默认取值**： 不涉及 

        :param opt: The opt of this ShowDefenderPluginManualCommandRequest.
        :type opt: str
        """
        self._opt = opt

    @property
    def network(self):
        r"""Gets the network of this ShowDefenderPluginManualCommandRequest.

        **参数解释**： 网络类型，用于指定返回的命令中使用的下载地址和服务端地址的网络类型 **约束限制**： 非必填 **取值范围**： - public：公网 - internal：内网  **默认取值**： internal 

        :return: The network of this ShowDefenderPluginManualCommandRequest.
        :rtype: str
        """
        return self._network

    @network.setter
    def network(self, network):
        r"""Sets the network of this ShowDefenderPluginManualCommandRequest.

        **参数解释**： 网络类型，用于指定返回的命令中使用的下载地址和服务端地址的网络类型 **约束限制**： 非必填 **取值范围**： - public：公网 - internal：内网  **默认取值**： internal 

        :param network: The network of this ShowDefenderPluginManualCommandRequest.
        :type network: str
        """
        self._network = network

    @property
    def agent_type(self):
        r"""Gets the agent_type of this ShowDefenderPluginManualCommandRequest.

        **参数解释**： 智能体类型，用于区分OpenClaw和自研Claw **约束限制**： 必填 **取值范围**： - OpenClaw：OpenClaw - SelfDevelopedClaw：自研claw  **默认取值**： OpenClaw 

        :return: The agent_type of this ShowDefenderPluginManualCommandRequest.
        :rtype: str
        """
        return self._agent_type

    @agent_type.setter
    def agent_type(self, agent_type):
        r"""Sets the agent_type of this ShowDefenderPluginManualCommandRequest.

        **参数解释**： 智能体类型，用于区分OpenClaw和自研Claw **约束限制**： 必填 **取值范围**： - OpenClaw：OpenClaw - SelfDevelopedClaw：自研claw  **默认取值**： OpenClaw 

        :param agent_type: The agent_type of this ShowDefenderPluginManualCommandRequest.
        :type agent_type: str
        """
        self._agent_type = agent_type

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
        if not isinstance(other, ShowDefenderPluginManualCommandRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
