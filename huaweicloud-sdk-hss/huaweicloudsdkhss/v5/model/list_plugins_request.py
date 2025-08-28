# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPluginsRequest:

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
        'host_name': 'str',
        'host_id': 'str',
        'private_ip': 'str',
        'public_ip': 'str',
        'group_id': 'str',
        'asset_value': 'str',
        'limit': 'int',
        'offset': 'int',
        'agent_status': 'str',
        'detect_result': 'str',
        'host_status': 'str',
        'os_type': 'str',
        'ip_addr': 'str',
        'protect_status': 'str',
        'group_name': 'str',
        'policy_group_id': 'str',
        'policy_group_name': 'str',
        'label': 'str',
        'charging_mode': 'str',
        'refresh': 'bool',
        'above_version': 'bool',
        'name': 'str',
        'version': 'str',
        'plugin': 'str',
        'outside_host': 'bool'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'host_name': 'host_name',
        'host_id': 'host_id',
        'private_ip': 'private_ip',
        'public_ip': 'public_ip',
        'group_id': 'group_id',
        'asset_value': 'asset_value',
        'limit': 'limit',
        'offset': 'offset',
        'agent_status': 'agent_status',
        'detect_result': 'detect_result',
        'host_status': 'host_status',
        'os_type': 'os_type',
        'ip_addr': 'ip_addr',
        'protect_status': 'protect_status',
        'group_name': 'group_name',
        'policy_group_id': 'policy_group_id',
        'policy_group_name': 'policy_group_name',
        'label': 'label',
        'charging_mode': 'charging_mode',
        'refresh': 'refresh',
        'above_version': 'above_version',
        'name': 'name',
        'version': 'version',
        'plugin': 'plugin',
        'outside_host': 'outside_host'
    }

    def __init__(self, enterprise_project_id=None, host_name=None, host_id=None, private_ip=None, public_ip=None, group_id=None, asset_value=None, limit=None, offset=None, agent_status=None, detect_result=None, host_status=None, os_type=None, ip_addr=None, protect_status=None, group_name=None, policy_group_id=None, policy_group_name=None, label=None, charging_mode=None, refresh=None, above_version=None, name=None, version=None, plugin=None, outside_host=None):
        r"""ListPluginsRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param host_name: **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 
        :type host_name: str
        :param host_id: **参数解释**: 服务器ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 
        :type host_id: str
        :param private_ip: **参数解释**: 服务器私有IP **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 
        :type private_ip: str
        :param public_ip: 服务器公网IP
        :type public_ip: str
        :param group_id: 服务器组ID
        :type group_id: str
        :param asset_value: 资产重要性，包含如下3种   - important ：重要资产   - common ：一般资产   - test ：测试资产
        :type asset_value: str
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 
        :type offset: int
        :param agent_status: **参数解释**： 客户端状态 **约束限制**： 不涉及 **取值范围**： 字符长度1-256位  **默认取值**： 不涉及 
        :type agent_status: str
        :param detect_result: **参数解释**： 检测结果 **约束限制**： 不涉及 **取值范围**： 字符长度1-256位  **默认取值**： 不涉及 
        :type detect_result: str
        :param host_status: **参数解释**： 主机状态 **约束限制**： 不涉及 **取值范围**： 字符长度1-256位  **默认取值**： 不涉及 
        :type host_status: str
        :param os_type: **参数解释**： 操作系统类型 **约束限制**： 不涉及 **取值范围**： - Linux：Linux操作系统。 - Windows：Windows操作系统。  **默认取值**： 不涉及 
        :type os_type: str
        :param ip_addr: 公网或私网IP
        :type ip_addr: str
        :param protect_status: 防护状态
        :type protect_status: str
        :param group_name: 服务器组名称
        :type group_name: str
        :param policy_group_id: 策略组ID
        :type policy_group_id: str
        :param policy_group_name: 策略组名称
        :type policy_group_name: str
        :param label: 资产标签
        :type label: str
        :param charging_mode: 收费模式
        :type charging_mode: str
        :param refresh: **参数解释**： 是否强制从ECS同步主机 **约束限制**： 不涉及 **取值范围**： - true：是。 - false：否。  **默认取值**： false 
        :type refresh: bool
        :param above_version: 是否返回比当前版本高的所有版本
        :type above_version: bool
        :param name: **参数解释**： 插件名称 **约束限制**： 不涉及 **取值范围**： 字符长度1-256位  **默认取值**： opa-docker-authz 
        :type name: str
        :param version: **参数解释**： 主机开通的版本 **约束限制**： 不涉及 **取值范围**： 字符长度1-256位  **默认取值**： 不涉及 
        :type version: str
        :param plugin: **参数解释**： 插件类型 **约束限制**： 不涉及 **取值范围**： - opa-docker-authz：docker插件。  **默认取值**： opa-docker-authz 
        :type plugin: str
        :param outside_host: **参数解释**： 是否非华为云 **约束限制**： 不涉及 **取值范围**： - true：是。 - false：否。  **默认取值**： false 
        :type outside_host: bool
        """
        
        

        self._enterprise_project_id = None
        self._host_name = None
        self._host_id = None
        self._private_ip = None
        self._public_ip = None
        self._group_id = None
        self._asset_value = None
        self._limit = None
        self._offset = None
        self._agent_status = None
        self._detect_result = None
        self._host_status = None
        self._os_type = None
        self._ip_addr = None
        self._protect_status = None
        self._group_name = None
        self._policy_group_id = None
        self._policy_group_name = None
        self._label = None
        self._charging_mode = None
        self._refresh = None
        self._above_version = None
        self._name = None
        self._version = None
        self._plugin = None
        self._outside_host = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if host_name is not None:
            self.host_name = host_name
        if host_id is not None:
            self.host_id = host_id
        if private_ip is not None:
            self.private_ip = private_ip
        if public_ip is not None:
            self.public_ip = public_ip
        if group_id is not None:
            self.group_id = group_id
        if asset_value is not None:
            self.asset_value = asset_value
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if agent_status is not None:
            self.agent_status = agent_status
        if detect_result is not None:
            self.detect_result = detect_result
        if host_status is not None:
            self.host_status = host_status
        if os_type is not None:
            self.os_type = os_type
        if ip_addr is not None:
            self.ip_addr = ip_addr
        if protect_status is not None:
            self.protect_status = protect_status
        if group_name is not None:
            self.group_name = group_name
        if policy_group_id is not None:
            self.policy_group_id = policy_group_id
        if policy_group_name is not None:
            self.policy_group_name = policy_group_name
        if label is not None:
            self.label = label
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if refresh is not None:
            self.refresh = refresh
        if above_version is not None:
            self.above_version = above_version
        self.name = name
        if version is not None:
            self.version = version
        if plugin is not None:
            self.plugin = plugin
        if outside_host is not None:
            self.outside_host = outside_host

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListPluginsRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListPluginsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListPluginsRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListPluginsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def host_name(self):
        r"""Gets the host_name of this ListPluginsRequest.

        **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :return: The host_name of this ListPluginsRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ListPluginsRequest.

        **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :param host_name: The host_name of this ListPluginsRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_id(self):
        r"""Gets the host_id of this ListPluginsRequest.

        **参数解释**: 服务器ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :return: The host_id of this ListPluginsRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ListPluginsRequest.

        **参数解释**: 服务器ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :param host_id: The host_id of this ListPluginsRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def private_ip(self):
        r"""Gets the private_ip of this ListPluginsRequest.

        **参数解释**: 服务器私有IP **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The private_ip of this ListPluginsRequest.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this ListPluginsRequest.

        **参数解释**: 服务器私有IP **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param private_ip: The private_ip of this ListPluginsRequest.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def public_ip(self):
        r"""Gets the public_ip of this ListPluginsRequest.

        服务器公网IP

        :return: The public_ip of this ListPluginsRequest.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this ListPluginsRequest.

        服务器公网IP

        :param public_ip: The public_ip of this ListPluginsRequest.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def group_id(self):
        r"""Gets the group_id of this ListPluginsRequest.

        服务器组ID

        :return: The group_id of this ListPluginsRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ListPluginsRequest.

        服务器组ID

        :param group_id: The group_id of this ListPluginsRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def asset_value(self):
        r"""Gets the asset_value of this ListPluginsRequest.

        资产重要性，包含如下3种   - important ：重要资产   - common ：一般资产   - test ：测试资产

        :return: The asset_value of this ListPluginsRequest.
        :rtype: str
        """
        return self._asset_value

    @asset_value.setter
    def asset_value(self, asset_value):
        r"""Sets the asset_value of this ListPluginsRequest.

        资产重要性，包含如下3种   - important ：重要资产   - common ：一般资产   - test ：测试资产

        :param asset_value: The asset_value of this ListPluginsRequest.
        :type asset_value: str
        """
        self._asset_value = asset_value

    @property
    def limit(self):
        r"""Gets the limit of this ListPluginsRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListPluginsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListPluginsRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListPluginsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListPluginsRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :return: The offset of this ListPluginsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListPluginsRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :param offset: The offset of this ListPluginsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def agent_status(self):
        r"""Gets the agent_status of this ListPluginsRequest.

        **参数解释**： 客户端状态 **约束限制**： 不涉及 **取值范围**： 字符长度1-256位  **默认取值**： 不涉及 

        :return: The agent_status of this ListPluginsRequest.
        :rtype: str
        """
        return self._agent_status

    @agent_status.setter
    def agent_status(self, agent_status):
        r"""Sets the agent_status of this ListPluginsRequest.

        **参数解释**： 客户端状态 **约束限制**： 不涉及 **取值范围**： 字符长度1-256位  **默认取值**： 不涉及 

        :param agent_status: The agent_status of this ListPluginsRequest.
        :type agent_status: str
        """
        self._agent_status = agent_status

    @property
    def detect_result(self):
        r"""Gets the detect_result of this ListPluginsRequest.

        **参数解释**： 检测结果 **约束限制**： 不涉及 **取值范围**： 字符长度1-256位  **默认取值**： 不涉及 

        :return: The detect_result of this ListPluginsRequest.
        :rtype: str
        """
        return self._detect_result

    @detect_result.setter
    def detect_result(self, detect_result):
        r"""Sets the detect_result of this ListPluginsRequest.

        **参数解释**： 检测结果 **约束限制**： 不涉及 **取值范围**： 字符长度1-256位  **默认取值**： 不涉及 

        :param detect_result: The detect_result of this ListPluginsRequest.
        :type detect_result: str
        """
        self._detect_result = detect_result

    @property
    def host_status(self):
        r"""Gets the host_status of this ListPluginsRequest.

        **参数解释**： 主机状态 **约束限制**： 不涉及 **取值范围**： 字符长度1-256位  **默认取值**： 不涉及 

        :return: The host_status of this ListPluginsRequest.
        :rtype: str
        """
        return self._host_status

    @host_status.setter
    def host_status(self, host_status):
        r"""Sets the host_status of this ListPluginsRequest.

        **参数解释**： 主机状态 **约束限制**： 不涉及 **取值范围**： 字符长度1-256位  **默认取值**： 不涉及 

        :param host_status: The host_status of this ListPluginsRequest.
        :type host_status: str
        """
        self._host_status = host_status

    @property
    def os_type(self):
        r"""Gets the os_type of this ListPluginsRequest.

        **参数解释**： 操作系统类型 **约束限制**： 不涉及 **取值范围**： - Linux：Linux操作系统。 - Windows：Windows操作系统。  **默认取值**： 不涉及 

        :return: The os_type of this ListPluginsRequest.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this ListPluginsRequest.

        **参数解释**： 操作系统类型 **约束限制**： 不涉及 **取值范围**： - Linux：Linux操作系统。 - Windows：Windows操作系统。  **默认取值**： 不涉及 

        :param os_type: The os_type of this ListPluginsRequest.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def ip_addr(self):
        r"""Gets the ip_addr of this ListPluginsRequest.

        公网或私网IP

        :return: The ip_addr of this ListPluginsRequest.
        :rtype: str
        """
        return self._ip_addr

    @ip_addr.setter
    def ip_addr(self, ip_addr):
        r"""Sets the ip_addr of this ListPluginsRequest.

        公网或私网IP

        :param ip_addr: The ip_addr of this ListPluginsRequest.
        :type ip_addr: str
        """
        self._ip_addr = ip_addr

    @property
    def protect_status(self):
        r"""Gets the protect_status of this ListPluginsRequest.

        防护状态

        :return: The protect_status of this ListPluginsRequest.
        :rtype: str
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        r"""Sets the protect_status of this ListPluginsRequest.

        防护状态

        :param protect_status: The protect_status of this ListPluginsRequest.
        :type protect_status: str
        """
        self._protect_status = protect_status

    @property
    def group_name(self):
        r"""Gets the group_name of this ListPluginsRequest.

        服务器组名称

        :return: The group_name of this ListPluginsRequest.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this ListPluginsRequest.

        服务器组名称

        :param group_name: The group_name of this ListPluginsRequest.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def policy_group_id(self):
        r"""Gets the policy_group_id of this ListPluginsRequest.

        策略组ID

        :return: The policy_group_id of this ListPluginsRequest.
        :rtype: str
        """
        return self._policy_group_id

    @policy_group_id.setter
    def policy_group_id(self, policy_group_id):
        r"""Sets the policy_group_id of this ListPluginsRequest.

        策略组ID

        :param policy_group_id: The policy_group_id of this ListPluginsRequest.
        :type policy_group_id: str
        """
        self._policy_group_id = policy_group_id

    @property
    def policy_group_name(self):
        r"""Gets the policy_group_name of this ListPluginsRequest.

        策略组名称

        :return: The policy_group_name of this ListPluginsRequest.
        :rtype: str
        """
        return self._policy_group_name

    @policy_group_name.setter
    def policy_group_name(self, policy_group_name):
        r"""Sets the policy_group_name of this ListPluginsRequest.

        策略组名称

        :param policy_group_name: The policy_group_name of this ListPluginsRequest.
        :type policy_group_name: str
        """
        self._policy_group_name = policy_group_name

    @property
    def label(self):
        r"""Gets the label of this ListPluginsRequest.

        资产标签

        :return: The label of this ListPluginsRequest.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        r"""Sets the label of this ListPluginsRequest.

        资产标签

        :param label: The label of this ListPluginsRequest.
        :type label: str
        """
        self._label = label

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this ListPluginsRequest.

        收费模式

        :return: The charging_mode of this ListPluginsRequest.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this ListPluginsRequest.

        收费模式

        :param charging_mode: The charging_mode of this ListPluginsRequest.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def refresh(self):
        r"""Gets the refresh of this ListPluginsRequest.

        **参数解释**： 是否强制从ECS同步主机 **约束限制**： 不涉及 **取值范围**： - true：是。 - false：否。  **默认取值**： false 

        :return: The refresh of this ListPluginsRequest.
        :rtype: bool
        """
        return self._refresh

    @refresh.setter
    def refresh(self, refresh):
        r"""Sets the refresh of this ListPluginsRequest.

        **参数解释**： 是否强制从ECS同步主机 **约束限制**： 不涉及 **取值范围**： - true：是。 - false：否。  **默认取值**： false 

        :param refresh: The refresh of this ListPluginsRequest.
        :type refresh: bool
        """
        self._refresh = refresh

    @property
    def above_version(self):
        r"""Gets the above_version of this ListPluginsRequest.

        是否返回比当前版本高的所有版本

        :return: The above_version of this ListPluginsRequest.
        :rtype: bool
        """
        return self._above_version

    @above_version.setter
    def above_version(self, above_version):
        r"""Sets the above_version of this ListPluginsRequest.

        是否返回比当前版本高的所有版本

        :param above_version: The above_version of this ListPluginsRequest.
        :type above_version: bool
        """
        self._above_version = above_version

    @property
    def name(self):
        r"""Gets the name of this ListPluginsRequest.

        **参数解释**： 插件名称 **约束限制**： 不涉及 **取值范围**： 字符长度1-256位  **默认取值**： opa-docker-authz 

        :return: The name of this ListPluginsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListPluginsRequest.

        **参数解释**： 插件名称 **约束限制**： 不涉及 **取值范围**： 字符长度1-256位  **默认取值**： opa-docker-authz 

        :param name: The name of this ListPluginsRequest.
        :type name: str
        """
        self._name = name

    @property
    def version(self):
        r"""Gets the version of this ListPluginsRequest.

        **参数解释**： 主机开通的版本 **约束限制**： 不涉及 **取值范围**： 字符长度1-256位  **默认取值**： 不涉及 

        :return: The version of this ListPluginsRequest.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ListPluginsRequest.

        **参数解释**： 主机开通的版本 **约束限制**： 不涉及 **取值范围**： 字符长度1-256位  **默认取值**： 不涉及 

        :param version: The version of this ListPluginsRequest.
        :type version: str
        """
        self._version = version

    @property
    def plugin(self):
        r"""Gets the plugin of this ListPluginsRequest.

        **参数解释**： 插件类型 **约束限制**： 不涉及 **取值范围**： - opa-docker-authz：docker插件。  **默认取值**： opa-docker-authz 

        :return: The plugin of this ListPluginsRequest.
        :rtype: str
        """
        return self._plugin

    @plugin.setter
    def plugin(self, plugin):
        r"""Sets the plugin of this ListPluginsRequest.

        **参数解释**： 插件类型 **约束限制**： 不涉及 **取值范围**： - opa-docker-authz：docker插件。  **默认取值**： opa-docker-authz 

        :param plugin: The plugin of this ListPluginsRequest.
        :type plugin: str
        """
        self._plugin = plugin

    @property
    def outside_host(self):
        r"""Gets the outside_host of this ListPluginsRequest.

        **参数解释**： 是否非华为云 **约束限制**： 不涉及 **取值范围**： - true：是。 - false：否。  **默认取值**： false 

        :return: The outside_host of this ListPluginsRequest.
        :rtype: bool
        """
        return self._outside_host

    @outside_host.setter
    def outside_host(self, outside_host):
        r"""Sets the outside_host of this ListPluginsRequest.

        **参数解释**： 是否非华为云 **约束限制**： 不涉及 **取值范围**： - true：是。 - false：否。  **默认取值**： false 

        :param outside_host: The outside_host of this ListPluginsRequest.
        :type outside_host: bool
        """
        self._outside_host = outside_host

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
        if not isinstance(other, ListPluginsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
