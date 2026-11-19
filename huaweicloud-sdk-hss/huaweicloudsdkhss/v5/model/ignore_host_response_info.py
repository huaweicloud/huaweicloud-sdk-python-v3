# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IgnoreHostResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agent_id': 'str',
        'host_id': 'str',
        'host_name': 'str',
        'private_ip': 'str',
        'public_ip': 'str',
        'os_name': 'str',
        'os_type': 'str',
        'host_status': 'str',
        'agent_status': 'str',
        'agent_version': 'str',
        'group_id': 'str',
        'group_name': 'str',
        'asset_value': 'str',
        'enterprise_project_id': 'str',
        'enterprise_project_name': 'str',
        'os_bit': 'str',
        'os_version': 'str',
        'protect_status': 'str',
        'detect_result': 'str',
        'charging_mode': 'str',
        'resource_id': 'str',
        'policy_group_id': 'str',
        'policy_group_name': 'str',
        'expire_time': 'int',
        'open_time': 'int',
        'agent_create_time': 'int',
        'agent_update_time': 'int',
        'upgradable': 'bool',
        'outside_host': 'bool',
        'container_type': 'str',
        'wtp_protect_status': 'str'
    }

    attribute_map = {
        'agent_id': 'agent_id',
        'host_id': 'host_id',
        'host_name': 'host_name',
        'private_ip': 'private_ip',
        'public_ip': 'public_ip',
        'os_name': 'os_name',
        'os_type': 'os_type',
        'host_status': 'host_status',
        'agent_status': 'agent_status',
        'agent_version': 'agent_version',
        'group_id': 'group_id',
        'group_name': 'group_name',
        'asset_value': 'asset_value',
        'enterprise_project_id': 'enterprise_project_id',
        'enterprise_project_name': 'enterprise_project_name',
        'os_bit': 'os_bit',
        'os_version': 'os_version',
        'protect_status': 'protect_status',
        'detect_result': 'detect_result',
        'charging_mode': 'charging_mode',
        'resource_id': 'resource_id',
        'policy_group_id': 'policy_group_id',
        'policy_group_name': 'policy_group_name',
        'expire_time': 'expire_time',
        'open_time': 'open_time',
        'agent_create_time': 'agent_create_time',
        'agent_update_time': 'agent_update_time',
        'upgradable': 'upgradable',
        'outside_host': 'outside_host',
        'container_type': 'container_type',
        'wtp_protect_status': 'wtp_protect_status'
    }

    def __init__(self, agent_id=None, host_id=None, host_name=None, private_ip=None, public_ip=None, os_name=None, os_type=None, host_status=None, agent_status=None, agent_version=None, group_id=None, group_name=None, asset_value=None, enterprise_project_id=None, enterprise_project_name=None, os_bit=None, os_version=None, protect_status=None, detect_result=None, charging_mode=None, resource_id=None, policy_group_id=None, policy_group_name=None, expire_time=None, open_time=None, agent_create_time=None, agent_update_time=None, upgradable=None, outside_host=None, container_type=None, wtp_protect_status=None):
        r"""IgnoreHostResponseInfo

        The model defined in huaweicloud sdk

        :param agent_id: **参数解释**: 主机上安装的杀毒Agent的唯一标识ID，用于关联主机与杀毒服务 **取值范围**: 字符长度1-64位 
        :type agent_id: str
        :param host_id: **参数解释**: 服务器的唯一标识ID **取值范围**: 字符长度1-64位 
        :type host_id: str
        :param host_name: **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 
        :type host_name: str
        :param private_ip: **参数解释**: 服务器私有IP **取值范围**: 字符长度1-128位 
        :type private_ip: str
        :param public_ip: **参数解释**: 服务器弹性IP地址 **取值范围**: IPv4格式（长度7-15位）、IPv6格式（长度15-39位） 
        :type public_ip: str
        :param os_name: **参数解释**: 操作系统名称 **取值范围**: 字符长度1-64位 
        :type os_name: str
        :param os_type: **参数解释**： 操作系统类型 **取值范围**： - Linux：Linux - Windows：Windows 
        :type os_type: str
        :param host_status: **参数解释**： 服务器状态 **取值范围**： - ACTIVE：运行中 - SHUTOFF：关机 - BUILDING：创建中 - ERROR：故障 
        :type host_status: str
        :param agent_status: **参数解释**： Agent状态 **取值范围**： - installed：已安装 - not_installed：未安装 - online：在线 - offline：离线 - install_failed：安装失败 - installing：安装中 
        :type agent_status: str
        :param agent_version: **参数解释**： agent版本 **取值范围**： 字符长度1-32位 
        :type agent_version: str
        :param group_id: **参数解释**: 服务器组ID **取值范围**: 字符范围1-64位 
        :type group_id: str
        :param group_name: **参数解释**: 服务器组名称 **取值范围**: 字符范围1-128位 
        :type group_name: str
        :param asset_value: **参数解释**: 资产重要性 **约束限制**: 不涉及 **取值范围**： - important：重要资产 - common：一般资产 - test：测试资产  **默认取值**: 不涉及 
        :type asset_value: str
        :param enterprise_project_id: **参数解释** 企业项目ID **取值范围** 字符长度0-64位 
        :type enterprise_project_id: str
        :param enterprise_project_name: **参数解释** 企业项目名称 **取值范围** 字符长度0-256位 
        :type enterprise_project_name: str
        :param os_bit: **参数解释** 操作系统位数 **取值范围** 字符长度0-64位 
        :type os_bit: str
        :param os_version: **参数解释** 操作系统版本 **取值范围** 字符长度0-64位 
        :type os_version: str
        :param protect_status: **参数解释** 防护状态 **取值范围** - closed：关闭 - opened：开启 - protection_exception：防护异常 
        :type protect_status: str
        :param detect_result: **参数解释** 检测结果 **取值范围** - undetected：未检测 - clean：无风险 - risk：有风险 - scanning：检测中 
        :type detect_result: str
        :param charging_mode: **参数解释** 计费模式 **取值范围** 字符长度0-32位 
        :type charging_mode: str
        :param resource_id: **参数解释** 主机资源ID **取值范围** 字符长度0-128位 
        :type resource_id: str
        :param policy_group_id: **参数解释** 策略组ID **取值范围** 字符长度0-128位 
        :type policy_group_id: str
        :param policy_group_name: **参数解释** 策略组名称 **取值范围** 字符长度0-256位 
        :type policy_group_name: str
        :param expire_time: **参数解释** 主机防护版本到期时间，毫秒级时间戳 **取值范围** 0-9223372036854775807 
        :type expire_time: int
        :param open_time: **参数解释** 开通防护时间，毫秒级时间戳 **取值范围** 0-9223372036854775807 
        :type open_time: int
        :param agent_create_time: **参数解释** Agent安装时间，毫秒级时间戳 **取值范围** 0-9223372036854775807 
        :type agent_create_time: int
        :param agent_update_time: **参数解释** Agent更新时间，毫秒级时间戳 **取值范围** 0-9223372036854775807 
        :type agent_update_time: int
        :param upgradable: **参数解释** Agent是否可升级 **取值范围** true或者false 
        :type upgradable: bool
        :param outside_host: **参数解释** 是否非本账号主机 **取值范围** true或者false 
        :type outside_host: bool
        :param container_type: **参数解释** 容器类型 **取值范围** 字符长度0-32位 
        :type container_type: str
        :param wtp_protect_status: **参数解释** 网页防篡改防护状态 **取值范围** - closed：关闭 - opened：开启 
        :type wtp_protect_status: str
        """
        
        

        self._agent_id = None
        self._host_id = None
        self._host_name = None
        self._private_ip = None
        self._public_ip = None
        self._os_name = None
        self._os_type = None
        self._host_status = None
        self._agent_status = None
        self._agent_version = None
        self._group_id = None
        self._group_name = None
        self._asset_value = None
        self._enterprise_project_id = None
        self._enterprise_project_name = None
        self._os_bit = None
        self._os_version = None
        self._protect_status = None
        self._detect_result = None
        self._charging_mode = None
        self._resource_id = None
        self._policy_group_id = None
        self._policy_group_name = None
        self._expire_time = None
        self._open_time = None
        self._agent_create_time = None
        self._agent_update_time = None
        self._upgradable = None
        self._outside_host = None
        self._container_type = None
        self._wtp_protect_status = None
        self.discriminator = None

        if agent_id is not None:
            self.agent_id = agent_id
        if host_id is not None:
            self.host_id = host_id
        if host_name is not None:
            self.host_name = host_name
        if private_ip is not None:
            self.private_ip = private_ip
        if public_ip is not None:
            self.public_ip = public_ip
        if os_name is not None:
            self.os_name = os_name
        if os_type is not None:
            self.os_type = os_type
        if host_status is not None:
            self.host_status = host_status
        if agent_status is not None:
            self.agent_status = agent_status
        if agent_version is not None:
            self.agent_version = agent_version
        if group_id is not None:
            self.group_id = group_id
        if group_name is not None:
            self.group_name = group_name
        if asset_value is not None:
            self.asset_value = asset_value
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if enterprise_project_name is not None:
            self.enterprise_project_name = enterprise_project_name
        if os_bit is not None:
            self.os_bit = os_bit
        if os_version is not None:
            self.os_version = os_version
        if protect_status is not None:
            self.protect_status = protect_status
        if detect_result is not None:
            self.detect_result = detect_result
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if resource_id is not None:
            self.resource_id = resource_id
        if policy_group_id is not None:
            self.policy_group_id = policy_group_id
        if policy_group_name is not None:
            self.policy_group_name = policy_group_name
        if expire_time is not None:
            self.expire_time = expire_time
        if open_time is not None:
            self.open_time = open_time
        if agent_create_time is not None:
            self.agent_create_time = agent_create_time
        if agent_update_time is not None:
            self.agent_update_time = agent_update_time
        if upgradable is not None:
            self.upgradable = upgradable
        if outside_host is not None:
            self.outside_host = outside_host
        if container_type is not None:
            self.container_type = container_type
        if wtp_protect_status is not None:
            self.wtp_protect_status = wtp_protect_status

    @property
    def agent_id(self):
        r"""Gets the agent_id of this IgnoreHostResponseInfo.

        **参数解释**: 主机上安装的杀毒Agent的唯一标识ID，用于关联主机与杀毒服务 **取值范围**: 字符长度1-64位 

        :return: The agent_id of this IgnoreHostResponseInfo.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this IgnoreHostResponseInfo.

        **参数解释**: 主机上安装的杀毒Agent的唯一标识ID，用于关联主机与杀毒服务 **取值范围**: 字符长度1-64位 

        :param agent_id: The agent_id of this IgnoreHostResponseInfo.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def host_id(self):
        r"""Gets the host_id of this IgnoreHostResponseInfo.

        **参数解释**: 服务器的唯一标识ID **取值范围**: 字符长度1-64位 

        :return: The host_id of this IgnoreHostResponseInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this IgnoreHostResponseInfo.

        **参数解释**: 服务器的唯一标识ID **取值范围**: 字符长度1-64位 

        :param host_id: The host_id of this IgnoreHostResponseInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        r"""Gets the host_name of this IgnoreHostResponseInfo.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 

        :return: The host_name of this IgnoreHostResponseInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this IgnoreHostResponseInfo.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 

        :param host_name: The host_name of this IgnoreHostResponseInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def private_ip(self):
        r"""Gets the private_ip of this IgnoreHostResponseInfo.

        **参数解释**: 服务器私有IP **取值范围**: 字符长度1-128位 

        :return: The private_ip of this IgnoreHostResponseInfo.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this IgnoreHostResponseInfo.

        **参数解释**: 服务器私有IP **取值范围**: 字符长度1-128位 

        :param private_ip: The private_ip of this IgnoreHostResponseInfo.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def public_ip(self):
        r"""Gets the public_ip of this IgnoreHostResponseInfo.

        **参数解释**: 服务器弹性IP地址 **取值范围**: IPv4格式（长度7-15位）、IPv6格式（长度15-39位） 

        :return: The public_ip of this IgnoreHostResponseInfo.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this IgnoreHostResponseInfo.

        **参数解释**: 服务器弹性IP地址 **取值范围**: IPv4格式（长度7-15位）、IPv6格式（长度15-39位） 

        :param public_ip: The public_ip of this IgnoreHostResponseInfo.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def os_name(self):
        r"""Gets the os_name of this IgnoreHostResponseInfo.

        **参数解释**: 操作系统名称 **取值范围**: 字符长度1-64位 

        :return: The os_name of this IgnoreHostResponseInfo.
        :rtype: str
        """
        return self._os_name

    @os_name.setter
    def os_name(self, os_name):
        r"""Sets the os_name of this IgnoreHostResponseInfo.

        **参数解释**: 操作系统名称 **取值范围**: 字符长度1-64位 

        :param os_name: The os_name of this IgnoreHostResponseInfo.
        :type os_name: str
        """
        self._os_name = os_name

    @property
    def os_type(self):
        r"""Gets the os_type of this IgnoreHostResponseInfo.

        **参数解释**： 操作系统类型 **取值范围**： - Linux：Linux - Windows：Windows 

        :return: The os_type of this IgnoreHostResponseInfo.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this IgnoreHostResponseInfo.

        **参数解释**： 操作系统类型 **取值范围**： - Linux：Linux - Windows：Windows 

        :param os_type: The os_type of this IgnoreHostResponseInfo.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def host_status(self):
        r"""Gets the host_status of this IgnoreHostResponseInfo.

        **参数解释**： 服务器状态 **取值范围**： - ACTIVE：运行中 - SHUTOFF：关机 - BUILDING：创建中 - ERROR：故障 

        :return: The host_status of this IgnoreHostResponseInfo.
        :rtype: str
        """
        return self._host_status

    @host_status.setter
    def host_status(self, host_status):
        r"""Sets the host_status of this IgnoreHostResponseInfo.

        **参数解释**： 服务器状态 **取值范围**： - ACTIVE：运行中 - SHUTOFF：关机 - BUILDING：创建中 - ERROR：故障 

        :param host_status: The host_status of this IgnoreHostResponseInfo.
        :type host_status: str
        """
        self._host_status = host_status

    @property
    def agent_status(self):
        r"""Gets the agent_status of this IgnoreHostResponseInfo.

        **参数解释**： Agent状态 **取值范围**： - installed：已安装 - not_installed：未安装 - online：在线 - offline：离线 - install_failed：安装失败 - installing：安装中 

        :return: The agent_status of this IgnoreHostResponseInfo.
        :rtype: str
        """
        return self._agent_status

    @agent_status.setter
    def agent_status(self, agent_status):
        r"""Sets the agent_status of this IgnoreHostResponseInfo.

        **参数解释**： Agent状态 **取值范围**： - installed：已安装 - not_installed：未安装 - online：在线 - offline：离线 - install_failed：安装失败 - installing：安装中 

        :param agent_status: The agent_status of this IgnoreHostResponseInfo.
        :type agent_status: str
        """
        self._agent_status = agent_status

    @property
    def agent_version(self):
        r"""Gets the agent_version of this IgnoreHostResponseInfo.

        **参数解释**： agent版本 **取值范围**： 字符长度1-32位 

        :return: The agent_version of this IgnoreHostResponseInfo.
        :rtype: str
        """
        return self._agent_version

    @agent_version.setter
    def agent_version(self, agent_version):
        r"""Sets the agent_version of this IgnoreHostResponseInfo.

        **参数解释**： agent版本 **取值范围**： 字符长度1-32位 

        :param agent_version: The agent_version of this IgnoreHostResponseInfo.
        :type agent_version: str
        """
        self._agent_version = agent_version

    @property
    def group_id(self):
        r"""Gets the group_id of this IgnoreHostResponseInfo.

        **参数解释**: 服务器组ID **取值范围**: 字符范围1-64位 

        :return: The group_id of this IgnoreHostResponseInfo.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this IgnoreHostResponseInfo.

        **参数解释**: 服务器组ID **取值范围**: 字符范围1-64位 

        :param group_id: The group_id of this IgnoreHostResponseInfo.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def group_name(self):
        r"""Gets the group_name of this IgnoreHostResponseInfo.

        **参数解释**: 服务器组名称 **取值范围**: 字符范围1-128位 

        :return: The group_name of this IgnoreHostResponseInfo.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this IgnoreHostResponseInfo.

        **参数解释**: 服务器组名称 **取值范围**: 字符范围1-128位 

        :param group_name: The group_name of this IgnoreHostResponseInfo.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def asset_value(self):
        r"""Gets the asset_value of this IgnoreHostResponseInfo.

        **参数解释**: 资产重要性 **约束限制**: 不涉及 **取值范围**： - important：重要资产 - common：一般资产 - test：测试资产  **默认取值**: 不涉及 

        :return: The asset_value of this IgnoreHostResponseInfo.
        :rtype: str
        """
        return self._asset_value

    @asset_value.setter
    def asset_value(self, asset_value):
        r"""Sets the asset_value of this IgnoreHostResponseInfo.

        **参数解释**: 资产重要性 **约束限制**: 不涉及 **取值范围**： - important：重要资产 - common：一般资产 - test：测试资产  **默认取值**: 不涉及 

        :param asset_value: The asset_value of this IgnoreHostResponseInfo.
        :type asset_value: str
        """
        self._asset_value = asset_value

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this IgnoreHostResponseInfo.

        **参数解释** 企业项目ID **取值范围** 字符长度0-64位 

        :return: The enterprise_project_id of this IgnoreHostResponseInfo.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this IgnoreHostResponseInfo.

        **参数解释** 企业项目ID **取值范围** 字符长度0-64位 

        :param enterprise_project_id: The enterprise_project_id of this IgnoreHostResponseInfo.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def enterprise_project_name(self):
        r"""Gets the enterprise_project_name of this IgnoreHostResponseInfo.

        **参数解释** 企业项目名称 **取值范围** 字符长度0-256位 

        :return: The enterprise_project_name of this IgnoreHostResponseInfo.
        :rtype: str
        """
        return self._enterprise_project_name

    @enterprise_project_name.setter
    def enterprise_project_name(self, enterprise_project_name):
        r"""Sets the enterprise_project_name of this IgnoreHostResponseInfo.

        **参数解释** 企业项目名称 **取值范围** 字符长度0-256位 

        :param enterprise_project_name: The enterprise_project_name of this IgnoreHostResponseInfo.
        :type enterprise_project_name: str
        """
        self._enterprise_project_name = enterprise_project_name

    @property
    def os_bit(self):
        r"""Gets the os_bit of this IgnoreHostResponseInfo.

        **参数解释** 操作系统位数 **取值范围** 字符长度0-64位 

        :return: The os_bit of this IgnoreHostResponseInfo.
        :rtype: str
        """
        return self._os_bit

    @os_bit.setter
    def os_bit(self, os_bit):
        r"""Sets the os_bit of this IgnoreHostResponseInfo.

        **参数解释** 操作系统位数 **取值范围** 字符长度0-64位 

        :param os_bit: The os_bit of this IgnoreHostResponseInfo.
        :type os_bit: str
        """
        self._os_bit = os_bit

    @property
    def os_version(self):
        r"""Gets the os_version of this IgnoreHostResponseInfo.

        **参数解释** 操作系统版本 **取值范围** 字符长度0-64位 

        :return: The os_version of this IgnoreHostResponseInfo.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        r"""Sets the os_version of this IgnoreHostResponseInfo.

        **参数解释** 操作系统版本 **取值范围** 字符长度0-64位 

        :param os_version: The os_version of this IgnoreHostResponseInfo.
        :type os_version: str
        """
        self._os_version = os_version

    @property
    def protect_status(self):
        r"""Gets the protect_status of this IgnoreHostResponseInfo.

        **参数解释** 防护状态 **取值范围** - closed：关闭 - opened：开启 - protection_exception：防护异常 

        :return: The protect_status of this IgnoreHostResponseInfo.
        :rtype: str
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        r"""Sets the protect_status of this IgnoreHostResponseInfo.

        **参数解释** 防护状态 **取值范围** - closed：关闭 - opened：开启 - protection_exception：防护异常 

        :param protect_status: The protect_status of this IgnoreHostResponseInfo.
        :type protect_status: str
        """
        self._protect_status = protect_status

    @property
    def detect_result(self):
        r"""Gets the detect_result of this IgnoreHostResponseInfo.

        **参数解释** 检测结果 **取值范围** - undetected：未检测 - clean：无风险 - risk：有风险 - scanning：检测中 

        :return: The detect_result of this IgnoreHostResponseInfo.
        :rtype: str
        """
        return self._detect_result

    @detect_result.setter
    def detect_result(self, detect_result):
        r"""Sets the detect_result of this IgnoreHostResponseInfo.

        **参数解释** 检测结果 **取值范围** - undetected：未检测 - clean：无风险 - risk：有风险 - scanning：检测中 

        :param detect_result: The detect_result of this IgnoreHostResponseInfo.
        :type detect_result: str
        """
        self._detect_result = detect_result

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this IgnoreHostResponseInfo.

        **参数解释** 计费模式 **取值范围** 字符长度0-32位 

        :return: The charging_mode of this IgnoreHostResponseInfo.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this IgnoreHostResponseInfo.

        **参数解释** 计费模式 **取值范围** 字符长度0-32位 

        :param charging_mode: The charging_mode of this IgnoreHostResponseInfo.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def resource_id(self):
        r"""Gets the resource_id of this IgnoreHostResponseInfo.

        **参数解释** 主机资源ID **取值范围** 字符长度0-128位 

        :return: The resource_id of this IgnoreHostResponseInfo.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this IgnoreHostResponseInfo.

        **参数解释** 主机资源ID **取值范围** 字符长度0-128位 

        :param resource_id: The resource_id of this IgnoreHostResponseInfo.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def policy_group_id(self):
        r"""Gets the policy_group_id of this IgnoreHostResponseInfo.

        **参数解释** 策略组ID **取值范围** 字符长度0-128位 

        :return: The policy_group_id of this IgnoreHostResponseInfo.
        :rtype: str
        """
        return self._policy_group_id

    @policy_group_id.setter
    def policy_group_id(self, policy_group_id):
        r"""Sets the policy_group_id of this IgnoreHostResponseInfo.

        **参数解释** 策略组ID **取值范围** 字符长度0-128位 

        :param policy_group_id: The policy_group_id of this IgnoreHostResponseInfo.
        :type policy_group_id: str
        """
        self._policy_group_id = policy_group_id

    @property
    def policy_group_name(self):
        r"""Gets the policy_group_name of this IgnoreHostResponseInfo.

        **参数解释** 策略组名称 **取值范围** 字符长度0-256位 

        :return: The policy_group_name of this IgnoreHostResponseInfo.
        :rtype: str
        """
        return self._policy_group_name

    @policy_group_name.setter
    def policy_group_name(self, policy_group_name):
        r"""Sets the policy_group_name of this IgnoreHostResponseInfo.

        **参数解释** 策略组名称 **取值范围** 字符长度0-256位 

        :param policy_group_name: The policy_group_name of this IgnoreHostResponseInfo.
        :type policy_group_name: str
        """
        self._policy_group_name = policy_group_name

    @property
    def expire_time(self):
        r"""Gets the expire_time of this IgnoreHostResponseInfo.

        **参数解释** 主机防护版本到期时间，毫秒级时间戳 **取值范围** 0-9223372036854775807 

        :return: The expire_time of this IgnoreHostResponseInfo.
        :rtype: int
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this IgnoreHostResponseInfo.

        **参数解释** 主机防护版本到期时间，毫秒级时间戳 **取值范围** 0-9223372036854775807 

        :param expire_time: The expire_time of this IgnoreHostResponseInfo.
        :type expire_time: int
        """
        self._expire_time = expire_time

    @property
    def open_time(self):
        r"""Gets the open_time of this IgnoreHostResponseInfo.

        **参数解释** 开通防护时间，毫秒级时间戳 **取值范围** 0-9223372036854775807 

        :return: The open_time of this IgnoreHostResponseInfo.
        :rtype: int
        """
        return self._open_time

    @open_time.setter
    def open_time(self, open_time):
        r"""Sets the open_time of this IgnoreHostResponseInfo.

        **参数解释** 开通防护时间，毫秒级时间戳 **取值范围** 0-9223372036854775807 

        :param open_time: The open_time of this IgnoreHostResponseInfo.
        :type open_time: int
        """
        self._open_time = open_time

    @property
    def agent_create_time(self):
        r"""Gets the agent_create_time of this IgnoreHostResponseInfo.

        **参数解释** Agent安装时间，毫秒级时间戳 **取值范围** 0-9223372036854775807 

        :return: The agent_create_time of this IgnoreHostResponseInfo.
        :rtype: int
        """
        return self._agent_create_time

    @agent_create_time.setter
    def agent_create_time(self, agent_create_time):
        r"""Sets the agent_create_time of this IgnoreHostResponseInfo.

        **参数解释** Agent安装时间，毫秒级时间戳 **取值范围** 0-9223372036854775807 

        :param agent_create_time: The agent_create_time of this IgnoreHostResponseInfo.
        :type agent_create_time: int
        """
        self._agent_create_time = agent_create_time

    @property
    def agent_update_time(self):
        r"""Gets the agent_update_time of this IgnoreHostResponseInfo.

        **参数解释** Agent更新时间，毫秒级时间戳 **取值范围** 0-9223372036854775807 

        :return: The agent_update_time of this IgnoreHostResponseInfo.
        :rtype: int
        """
        return self._agent_update_time

    @agent_update_time.setter
    def agent_update_time(self, agent_update_time):
        r"""Sets the agent_update_time of this IgnoreHostResponseInfo.

        **参数解释** Agent更新时间，毫秒级时间戳 **取值范围** 0-9223372036854775807 

        :param agent_update_time: The agent_update_time of this IgnoreHostResponseInfo.
        :type agent_update_time: int
        """
        self._agent_update_time = agent_update_time

    @property
    def upgradable(self):
        r"""Gets the upgradable of this IgnoreHostResponseInfo.

        **参数解释** Agent是否可升级 **取值范围** true或者false 

        :return: The upgradable of this IgnoreHostResponseInfo.
        :rtype: bool
        """
        return self._upgradable

    @upgradable.setter
    def upgradable(self, upgradable):
        r"""Sets the upgradable of this IgnoreHostResponseInfo.

        **参数解释** Agent是否可升级 **取值范围** true或者false 

        :param upgradable: The upgradable of this IgnoreHostResponseInfo.
        :type upgradable: bool
        """
        self._upgradable = upgradable

    @property
    def outside_host(self):
        r"""Gets the outside_host of this IgnoreHostResponseInfo.

        **参数解释** 是否非本账号主机 **取值范围** true或者false 

        :return: The outside_host of this IgnoreHostResponseInfo.
        :rtype: bool
        """
        return self._outside_host

    @outside_host.setter
    def outside_host(self, outside_host):
        r"""Sets the outside_host of this IgnoreHostResponseInfo.

        **参数解释** 是否非本账号主机 **取值范围** true或者false 

        :param outside_host: The outside_host of this IgnoreHostResponseInfo.
        :type outside_host: bool
        """
        self._outside_host = outside_host

    @property
    def container_type(self):
        r"""Gets the container_type of this IgnoreHostResponseInfo.

        **参数解释** 容器类型 **取值范围** 字符长度0-32位 

        :return: The container_type of this IgnoreHostResponseInfo.
        :rtype: str
        """
        return self._container_type

    @container_type.setter
    def container_type(self, container_type):
        r"""Sets the container_type of this IgnoreHostResponseInfo.

        **参数解释** 容器类型 **取值范围** 字符长度0-32位 

        :param container_type: The container_type of this IgnoreHostResponseInfo.
        :type container_type: str
        """
        self._container_type = container_type

    @property
    def wtp_protect_status(self):
        r"""Gets the wtp_protect_status of this IgnoreHostResponseInfo.

        **参数解释** 网页防篡改防护状态 **取值范围** - closed：关闭 - opened：开启 

        :return: The wtp_protect_status of this IgnoreHostResponseInfo.
        :rtype: str
        """
        return self._wtp_protect_status

    @wtp_protect_status.setter
    def wtp_protect_status(self, wtp_protect_status):
        r"""Sets the wtp_protect_status of this IgnoreHostResponseInfo.

        **参数解释** 网页防篡改防护状态 **取值范围** - closed：关闭 - opened：开启 

        :param wtp_protect_status: The wtp_protect_status of this IgnoreHostResponseInfo.
        :type wtp_protect_status: str
        """
        self._wtp_protect_status = wtp_protect_status

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
        if not isinstance(other, IgnoreHostResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
