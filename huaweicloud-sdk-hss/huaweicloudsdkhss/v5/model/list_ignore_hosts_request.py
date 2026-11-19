# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListIgnoreHostsRequest:

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
        'version': 'str',
        'agent_status': 'str',
        'detect_result': 'str',
        'host_name': 'str',
        'host_id': 'str',
        'host_status': 'str',
        'os_type': 'str',
        'private_ip': 'str',
        'public_ip': 'str',
        'ip_addr': 'str',
        'protect_status': 'str',
        'group_id': 'str',
        'group_name': 'str',
        'policy_group_id': 'str',
        'policy_group_name': 'str',
        'charging_mode': 'str',
        'asset_value': 'str',
        'label': 'str',
        'has_intrusion': 'bool',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'version': 'version',
        'agent_status': 'agent_status',
        'detect_result': 'detect_result',
        'host_name': 'host_name',
        'host_id': 'host_id',
        'host_status': 'host_status',
        'os_type': 'os_type',
        'private_ip': 'private_ip',
        'public_ip': 'public_ip',
        'ip_addr': 'ip_addr',
        'protect_status': 'protect_status',
        'group_id': 'group_id',
        'group_name': 'group_name',
        'policy_group_id': 'policy_group_id',
        'policy_group_name': 'policy_group_name',
        'charging_mode': 'charging_mode',
        'asset_value': 'asset_value',
        'label': 'label',
        'has_intrusion': 'has_intrusion',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, enterprise_project_id=None, version=None, agent_status=None, detect_result=None, host_name=None, host_id=None, host_status=None, os_type=None, private_ip=None, public_ip=None, ip_addr=None, protect_status=None, group_id=None, group_name=None, policy_group_id=None, policy_group_name=None, charging_mode=None, asset_value=None, label=None, has_intrusion=None, offset=None, limit=None):
        r"""ListIgnoreHostsRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param version: **参数解释**： 主机开通的版本 **约束限制**: 不涉及 **取值范围**： 包含如下7种输入。 - hss.version.null ：无。 - hss.version.basic ：基础版。 - hss.version.advanced ：专业版。 - hss.version.enterprise ：企业版。 - hss.version.premium ：旗舰版。 - hss.version.wtp ：网页防篡改版。 - hss.version.container.enterprise：容器版。 - hss.version.container.wtp：容器网页防篡改增值项。  **默认取值**: 不涉及
        :type version: str
        :param agent_status: **参数解释**： Agent状态 **约束限制**: 不涉及 **取值范围**： - installed：已安装 - not_installed：未安装 - online：在线 - offline：离线 - install_failed：安装失败 - installing：安装中  **默认取值**: 不涉及 
        :type agent_status: str
        :param detect_result: **参数解释**: 检测结果 **约束限制**: 不涉及 **取值范围**: 包含如下4种： - undetected：未检测 - clean：无风险 - risk：有风险 - scanning：检测中  **默认取值**: 不涉及 
        :type detect_result: str
        :param host_name: **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 
        :type host_name: str
        :param host_id: **参数解释**: 服务器的唯一标识ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 
        :type host_id: str
        :param host_status: **参数解释**: 主机状态 **约束限制**: 不涉及 **取值范围**: 包含如下4种： - ACTIVE：正在运行 - SHUTOFF：关机 - BUILDING：创建中 - ERROR：故障  **默认取值**: 不涉及 
        :type host_status: str
        :param os_type: **参数解释**: 操作系统类型。 **约束限制**: 不涉及 **取值范围**: - Linux：Linux操作系统。 - Windows：Windows操作系统。  **默认取值**: 无 
        :type os_type: str
        :param private_ip: **参数解释**: 服务器私有IP **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 
        :type private_ip: str
        :param public_ip: **参数解释**: 服务器弹性IP地址 **约束限制**: 不涉及 **取值范围**: IPv4格式（长度7-15位）、IPv6格式（长度15-39位） **默认取值**: 无 
        :type public_ip: str
        :param ip_addr: **参数解释**: 公网或私网IP **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 
        :type ip_addr: str
        :param protect_status: **参数解释**: 防护状态 **约束限制**: 不涉及 **取值范围**: 包含如下3种： - closed：关闭 - opened：开启 - protection_exception：防护异常  **默认取值**: 不涉及 
        :type protect_status: str
        :param group_id: **参数解释**: 服务器组的唯一标识ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 
        :type group_id: str
        :param group_name: **参数解释**: 服务器组名称。 **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 无 
        :type group_name: str
        :param policy_group_id: **参数解释**: 策略组ID **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 
        :type policy_group_id: str
        :param policy_group_name: **参数解释**: 策略组名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 
        :type policy_group_name: str
        :param charging_mode: **参数解释**： 收费模式 **约束限制**: 不涉及 **取值范围**: - packet_cycle ：包年/包月。 - on_demand ：按需。  **默认取值**: 不涉及
        :type charging_mode: str
        :param asset_value: **参数解释**: 资产重要性 **约束限制**: 不涉及 **取值范围**： - important：重要资产 - common：一般资产 - test：测试资产  **默认取值**: 不涉及 
        :type asset_value: str
        :param label: **参数解释**: 服务器标签，格式为\&quot;key:value\&quot; **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 
        :type label: str
        :param has_intrusion: **参数解释**: 存在告警事件 **约束限制**: 不涉及 **取值范围**: true或者false **默认取值**: 不涉及 
        :type has_intrusion: bool
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 
        :type offset: int
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        """
        
        

        self._enterprise_project_id = None
        self._version = None
        self._agent_status = None
        self._detect_result = None
        self._host_name = None
        self._host_id = None
        self._host_status = None
        self._os_type = None
        self._private_ip = None
        self._public_ip = None
        self._ip_addr = None
        self._protect_status = None
        self._group_id = None
        self._group_name = None
        self._policy_group_id = None
        self._policy_group_name = None
        self._charging_mode = None
        self._asset_value = None
        self._label = None
        self._has_intrusion = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if version is not None:
            self.version = version
        if agent_status is not None:
            self.agent_status = agent_status
        if detect_result is not None:
            self.detect_result = detect_result
        if host_name is not None:
            self.host_name = host_name
        if host_id is not None:
            self.host_id = host_id
        if host_status is not None:
            self.host_status = host_status
        if os_type is not None:
            self.os_type = os_type
        if private_ip is not None:
            self.private_ip = private_ip
        if public_ip is not None:
            self.public_ip = public_ip
        if ip_addr is not None:
            self.ip_addr = ip_addr
        if protect_status is not None:
            self.protect_status = protect_status
        if group_id is not None:
            self.group_id = group_id
        if group_name is not None:
            self.group_name = group_name
        if policy_group_id is not None:
            self.policy_group_id = policy_group_id
        if policy_group_name is not None:
            self.policy_group_name = policy_group_name
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if asset_value is not None:
            self.asset_value = asset_value
        if label is not None:
            self.label = label
        if has_intrusion is not None:
            self.has_intrusion = has_intrusion
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListIgnoreHostsRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListIgnoreHostsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListIgnoreHostsRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListIgnoreHostsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def version(self):
        r"""Gets the version of this ListIgnoreHostsRequest.

        **参数解释**： 主机开通的版本 **约束限制**: 不涉及 **取值范围**： 包含如下7种输入。 - hss.version.null ：无。 - hss.version.basic ：基础版。 - hss.version.advanced ：专业版。 - hss.version.enterprise ：企业版。 - hss.version.premium ：旗舰版。 - hss.version.wtp ：网页防篡改版。 - hss.version.container.enterprise：容器版。 - hss.version.container.wtp：容器网页防篡改增值项。  **默认取值**: 不涉及

        :return: The version of this ListIgnoreHostsRequest.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ListIgnoreHostsRequest.

        **参数解释**： 主机开通的版本 **约束限制**: 不涉及 **取值范围**： 包含如下7种输入。 - hss.version.null ：无。 - hss.version.basic ：基础版。 - hss.version.advanced ：专业版。 - hss.version.enterprise ：企业版。 - hss.version.premium ：旗舰版。 - hss.version.wtp ：网页防篡改版。 - hss.version.container.enterprise：容器版。 - hss.version.container.wtp：容器网页防篡改增值项。  **默认取值**: 不涉及

        :param version: The version of this ListIgnoreHostsRequest.
        :type version: str
        """
        self._version = version

    @property
    def agent_status(self):
        r"""Gets the agent_status of this ListIgnoreHostsRequest.

        **参数解释**： Agent状态 **约束限制**: 不涉及 **取值范围**： - installed：已安装 - not_installed：未安装 - online：在线 - offline：离线 - install_failed：安装失败 - installing：安装中  **默认取值**: 不涉及 

        :return: The agent_status of this ListIgnoreHostsRequest.
        :rtype: str
        """
        return self._agent_status

    @agent_status.setter
    def agent_status(self, agent_status):
        r"""Sets the agent_status of this ListIgnoreHostsRequest.

        **参数解释**： Agent状态 **约束限制**: 不涉及 **取值范围**： - installed：已安装 - not_installed：未安装 - online：在线 - offline：离线 - install_failed：安装失败 - installing：安装中  **默认取值**: 不涉及 

        :param agent_status: The agent_status of this ListIgnoreHostsRequest.
        :type agent_status: str
        """
        self._agent_status = agent_status

    @property
    def detect_result(self):
        r"""Gets the detect_result of this ListIgnoreHostsRequest.

        **参数解释**: 检测结果 **约束限制**: 不涉及 **取值范围**: 包含如下4种： - undetected：未检测 - clean：无风险 - risk：有风险 - scanning：检测中  **默认取值**: 不涉及 

        :return: The detect_result of this ListIgnoreHostsRequest.
        :rtype: str
        """
        return self._detect_result

    @detect_result.setter
    def detect_result(self, detect_result):
        r"""Sets the detect_result of this ListIgnoreHostsRequest.

        **参数解释**: 检测结果 **约束限制**: 不涉及 **取值范围**: 包含如下4种： - undetected：未检测 - clean：无风险 - risk：有风险 - scanning：检测中  **默认取值**: 不涉及 

        :param detect_result: The detect_result of this ListIgnoreHostsRequest.
        :type detect_result: str
        """
        self._detect_result = detect_result

    @property
    def host_name(self):
        r"""Gets the host_name of this ListIgnoreHostsRequest.

        **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :return: The host_name of this ListIgnoreHostsRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ListIgnoreHostsRequest.

        **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :param host_name: The host_name of this ListIgnoreHostsRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_id(self):
        r"""Gets the host_id of this ListIgnoreHostsRequest.

        **参数解释**: 服务器的唯一标识ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :return: The host_id of this ListIgnoreHostsRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ListIgnoreHostsRequest.

        **参数解释**: 服务器的唯一标识ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :param host_id: The host_id of this ListIgnoreHostsRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_status(self):
        r"""Gets the host_status of this ListIgnoreHostsRequest.

        **参数解释**: 主机状态 **约束限制**: 不涉及 **取值范围**: 包含如下4种： - ACTIVE：正在运行 - SHUTOFF：关机 - BUILDING：创建中 - ERROR：故障  **默认取值**: 不涉及 

        :return: The host_status of this ListIgnoreHostsRequest.
        :rtype: str
        """
        return self._host_status

    @host_status.setter
    def host_status(self, host_status):
        r"""Sets the host_status of this ListIgnoreHostsRequest.

        **参数解释**: 主机状态 **约束限制**: 不涉及 **取值范围**: 包含如下4种： - ACTIVE：正在运行 - SHUTOFF：关机 - BUILDING：创建中 - ERROR：故障  **默认取值**: 不涉及 

        :param host_status: The host_status of this ListIgnoreHostsRequest.
        :type host_status: str
        """
        self._host_status = host_status

    @property
    def os_type(self):
        r"""Gets the os_type of this ListIgnoreHostsRequest.

        **参数解释**: 操作系统类型。 **约束限制**: 不涉及 **取值范围**: - Linux：Linux操作系统。 - Windows：Windows操作系统。  **默认取值**: 无 

        :return: The os_type of this ListIgnoreHostsRequest.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this ListIgnoreHostsRequest.

        **参数解释**: 操作系统类型。 **约束限制**: 不涉及 **取值范围**: - Linux：Linux操作系统。 - Windows：Windows操作系统。  **默认取值**: 无 

        :param os_type: The os_type of this ListIgnoreHostsRequest.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def private_ip(self):
        r"""Gets the private_ip of this ListIgnoreHostsRequest.

        **参数解释**: 服务器私有IP **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The private_ip of this ListIgnoreHostsRequest.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this ListIgnoreHostsRequest.

        **参数解释**: 服务器私有IP **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param private_ip: The private_ip of this ListIgnoreHostsRequest.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def public_ip(self):
        r"""Gets the public_ip of this ListIgnoreHostsRequest.

        **参数解释**: 服务器弹性IP地址 **约束限制**: 不涉及 **取值范围**: IPv4格式（长度7-15位）、IPv6格式（长度15-39位） **默认取值**: 无 

        :return: The public_ip of this ListIgnoreHostsRequest.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this ListIgnoreHostsRequest.

        **参数解释**: 服务器弹性IP地址 **约束限制**: 不涉及 **取值范围**: IPv4格式（长度7-15位）、IPv6格式（长度15-39位） **默认取值**: 无 

        :param public_ip: The public_ip of this ListIgnoreHostsRequest.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def ip_addr(self):
        r"""Gets the ip_addr of this ListIgnoreHostsRequest.

        **参数解释**: 公网或私网IP **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The ip_addr of this ListIgnoreHostsRequest.
        :rtype: str
        """
        return self._ip_addr

    @ip_addr.setter
    def ip_addr(self, ip_addr):
        r"""Sets the ip_addr of this ListIgnoreHostsRequest.

        **参数解释**: 公网或私网IP **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param ip_addr: The ip_addr of this ListIgnoreHostsRequest.
        :type ip_addr: str
        """
        self._ip_addr = ip_addr

    @property
    def protect_status(self):
        r"""Gets the protect_status of this ListIgnoreHostsRequest.

        **参数解释**: 防护状态 **约束限制**: 不涉及 **取值范围**: 包含如下3种： - closed：关闭 - opened：开启 - protection_exception：防护异常  **默认取值**: 不涉及 

        :return: The protect_status of this ListIgnoreHostsRequest.
        :rtype: str
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        r"""Sets the protect_status of this ListIgnoreHostsRequest.

        **参数解释**: 防护状态 **约束限制**: 不涉及 **取值范围**: 包含如下3种： - closed：关闭 - opened：开启 - protection_exception：防护异常  **默认取值**: 不涉及 

        :param protect_status: The protect_status of this ListIgnoreHostsRequest.
        :type protect_status: str
        """
        self._protect_status = protect_status

    @property
    def group_id(self):
        r"""Gets the group_id of this ListIgnoreHostsRequest.

        **参数解释**: 服务器组的唯一标识ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :return: The group_id of this ListIgnoreHostsRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ListIgnoreHostsRequest.

        **参数解释**: 服务器组的唯一标识ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :param group_id: The group_id of this ListIgnoreHostsRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def group_name(self):
        r"""Gets the group_name of this ListIgnoreHostsRequest.

        **参数解释**: 服务器组名称。 **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 无 

        :return: The group_name of this ListIgnoreHostsRequest.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this ListIgnoreHostsRequest.

        **参数解释**: 服务器组名称。 **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 无 

        :param group_name: The group_name of this ListIgnoreHostsRequest.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def policy_group_id(self):
        r"""Gets the policy_group_id of this ListIgnoreHostsRequest.

        **参数解释**: 策略组ID **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The policy_group_id of this ListIgnoreHostsRequest.
        :rtype: str
        """
        return self._policy_group_id

    @policy_group_id.setter
    def policy_group_id(self, policy_group_id):
        r"""Sets the policy_group_id of this ListIgnoreHostsRequest.

        **参数解释**: 策略组ID **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param policy_group_id: The policy_group_id of this ListIgnoreHostsRequest.
        :type policy_group_id: str
        """
        self._policy_group_id = policy_group_id

    @property
    def policy_group_name(self):
        r"""Gets the policy_group_name of this ListIgnoreHostsRequest.

        **参数解释**: 策略组名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :return: The policy_group_name of this ListIgnoreHostsRequest.
        :rtype: str
        """
        return self._policy_group_name

    @policy_group_name.setter
    def policy_group_name(self, policy_group_name):
        r"""Sets the policy_group_name of this ListIgnoreHostsRequest.

        **参数解释**: 策略组名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :param policy_group_name: The policy_group_name of this ListIgnoreHostsRequest.
        :type policy_group_name: str
        """
        self._policy_group_name = policy_group_name

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this ListIgnoreHostsRequest.

        **参数解释**： 收费模式 **约束限制**: 不涉及 **取值范围**: - packet_cycle ：包年/包月。 - on_demand ：按需。  **默认取值**: 不涉及

        :return: The charging_mode of this ListIgnoreHostsRequest.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this ListIgnoreHostsRequest.

        **参数解释**： 收费模式 **约束限制**: 不涉及 **取值范围**: - packet_cycle ：包年/包月。 - on_demand ：按需。  **默认取值**: 不涉及

        :param charging_mode: The charging_mode of this ListIgnoreHostsRequest.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def asset_value(self):
        r"""Gets the asset_value of this ListIgnoreHostsRequest.

        **参数解释**: 资产重要性 **约束限制**: 不涉及 **取值范围**： - important：重要资产 - common：一般资产 - test：测试资产  **默认取值**: 不涉及 

        :return: The asset_value of this ListIgnoreHostsRequest.
        :rtype: str
        """
        return self._asset_value

    @asset_value.setter
    def asset_value(self, asset_value):
        r"""Sets the asset_value of this ListIgnoreHostsRequest.

        **参数解释**: 资产重要性 **约束限制**: 不涉及 **取值范围**： - important：重要资产 - common：一般资产 - test：测试资产  **默认取值**: 不涉及 

        :param asset_value: The asset_value of this ListIgnoreHostsRequest.
        :type asset_value: str
        """
        self._asset_value = asset_value

    @property
    def label(self):
        r"""Gets the label of this ListIgnoreHostsRequest.

        **参数解释**: 服务器标签，格式为\"key:value\" **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :return: The label of this ListIgnoreHostsRequest.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        r"""Sets the label of this ListIgnoreHostsRequest.

        **参数解释**: 服务器标签，格式为\"key:value\" **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :param label: The label of this ListIgnoreHostsRequest.
        :type label: str
        """
        self._label = label

    @property
    def has_intrusion(self):
        r"""Gets the has_intrusion of this ListIgnoreHostsRequest.

        **参数解释**: 存在告警事件 **约束限制**: 不涉及 **取值范围**: true或者false **默认取值**: 不涉及 

        :return: The has_intrusion of this ListIgnoreHostsRequest.
        :rtype: bool
        """
        return self._has_intrusion

    @has_intrusion.setter
    def has_intrusion(self, has_intrusion):
        r"""Sets the has_intrusion of this ListIgnoreHostsRequest.

        **参数解释**: 存在告警事件 **约束限制**: 不涉及 **取值范围**: true或者false **默认取值**: 不涉及 

        :param has_intrusion: The has_intrusion of this ListIgnoreHostsRequest.
        :type has_intrusion: bool
        """
        self._has_intrusion = has_intrusion

    @property
    def offset(self):
        r"""Gets the offset of this ListIgnoreHostsRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :return: The offset of this ListIgnoreHostsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListIgnoreHostsRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :param offset: The offset of this ListIgnoreHostsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListIgnoreHostsRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListIgnoreHostsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListIgnoreHostsRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListIgnoreHostsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListIgnoreHostsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
