# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHostStatusRequest:

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
        'vpc_id': 'str',
        'region': 'str',
        'has_intrusion': 'bool',
        'has_vul': 'bool',
        'has_baseline': 'bool',
        'sort_key': 'str',
        'sort_dir': 'str',
        'policy_group_id': 'str',
        'policy_group_name': 'str',
        'charging_mode': 'str',
        'refresh': 'bool',
        'get_common_login_locations': 'bool',
        'above_version': 'bool',
        'outside_host': 'bool',
        'asset_value': 'str',
        'label': 'str',
        'server_group': 'str',
        'agent_upgradable': 'bool',
        'install_mode': 'bool',
        'binding_key': 'bool',
        'protect_interrupt': 'bool',
        'incluster': 'bool',
        'protect_degradation': 'bool',
        'limit': 'int',
        'offset': 'int'
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
        'vpc_id': 'vpc_id',
        'region': 'region',
        'has_intrusion': 'has_intrusion',
        'has_vul': 'has_vul',
        'has_baseline': 'has_baseline',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'policy_group_id': 'policy_group_id',
        'policy_group_name': 'policy_group_name',
        'charging_mode': 'charging_mode',
        'refresh': 'refresh',
        'get_common_login_locations': 'get_common_login_locations',
        'above_version': 'above_version',
        'outside_host': 'outside_host',
        'asset_value': 'asset_value',
        'label': 'label',
        'server_group': 'server_group',
        'agent_upgradable': 'agent_upgradable',
        'install_mode': 'install_mode',
        'binding_key': 'binding_key',
        'protect_interrupt': 'protect_interrupt',
        'incluster': 'incluster',
        'protect_degradation': 'protect_degradation',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, enterprise_project_id=None, version=None, agent_status=None, detect_result=None, host_name=None, host_id=None, host_status=None, os_type=None, private_ip=None, public_ip=None, ip_addr=None, protect_status=None, group_id=None, group_name=None, vpc_id=None, region=None, has_intrusion=None, has_vul=None, has_baseline=None, sort_key=None, sort_dir=None, policy_group_id=None, policy_group_name=None, charging_mode=None, refresh=None, get_common_login_locations=None, above_version=None, outside_host=None, asset_value=None, label=None, server_group=None, agent_upgradable=None, install_mode=None, binding_key=None, protect_interrupt=None, incluster=None, protect_degradation=None, limit=None, offset=None):
        r"""ListHostStatusRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。
        :type enterprise_project_id: str
        :param version: 主机开通的版本，包含如下7种输入。   - hss.version.null ：无。   - hss.version.basic ：基础版。   - hss.version.advanced ：专业版。   - hss.version.enterprise ：企业版。   - hss.version.premium ：旗舰版。   - hss.version.wtp ：网页防篡改版。   - hss.version.container.enterprise：容器版。
        :type version: str
        :param agent_status: Agent状态，包含如下6种。   - installed ：已安装。   - not_installed ：未安装。   - online ：在线。   - offline ：离线。   - install_failed ：安装失败。   - installing ：安装中。   - not_online ：不在线的（除了在线以外的所有状态，仅作为查询条件）。
        :type agent_status: str
        :param detect_result: 检测结果，包含如下4种。   - undetected ：未检测。   - clean ：无风险。   - risk ：有风险。   - scanning ：检测中。
        :type detect_result: str
        :param host_name: 服务器名称
        :type host_name: str
        :param host_id: 服务器ID
        :type host_id: str
        :param host_status: 主机状态，包含如下4种。   - ACTIVE ：正在运行。   - SHUTOFF ：关机。   - BUILDING ：创建中。   - ERROR ：故障。
        :type host_status: str
        :param os_type: 操作系统类型，包含如下2种。   - Linux ：Linux。   - Windows ：Windows。
        :type os_type: str
        :param private_ip: 服务器私有IP
        :type private_ip: str
        :param public_ip: 服务器公网IP
        :type public_ip: str
        :param ip_addr: 公网或私网IP
        :type ip_addr: str
        :param protect_status: 防护状态，包含如下2种。   - closed ：关闭。   - opened ：开启。   - protection_exception ：防护异常。
        :type protect_status: str
        :param group_id: 服务器组ID
        :type group_id: str
        :param group_name: 服务器组名称
        :type group_name: str
        :param vpc_id: vpc id
        :type vpc_id: str
        :param region: Region ID
        :type region: str
        :param has_intrusion: 存在告警事件
        :type has_intrusion: bool
        :param has_vul: 存在漏洞风险
        :type has_vul: bool
        :param has_baseline: 存在基线风险
        :type has_baseline: bool
        :param sort_key: 排序字段，只支持risk_num - risk_num：风险总量
        :type sort_key: str
        :param sort_dir: 排序的顺序 - asc: 正序 - desc: 倒序
        :type sort_dir: str
        :param policy_group_id: 策略组ID
        :type policy_group_id: str
        :param policy_group_name: 策略组名称
        :type policy_group_name: str
        :param charging_mode: 收费模式，包含如下2种。   - packet_cycle ：包年/包月。   - on_demand ：按需。
        :type charging_mode: str
        :param refresh: 是否强制从ECS同步主机
        :type refresh: bool
        :param get_common_login_locations: 是否获取主机常用登录地信息
        :type get_common_login_locations: bool
        :param above_version: 是否返回比当前版本高的所有版本
        :type above_version: bool
        :param outside_host: 是否华为云主机
        :type outside_host: bool
        :param asset_value: 资产重要性，包含如下4种   - important ：重要资产   - common ：一般资产   - test ：测试资产
        :type asset_value: str
        :param label: 资产标签
        :type label: str
        :param server_group: 资产服务器组
        :type server_group: str
        :param agent_upgradable: agent是否可升级
        :type agent_upgradable: bool
        :param install_mode: 是否安装模式场景
        :type install_mode: bool
        :param binding_key: 是否绑定DEW密钥
        :type binding_key: bool
        :param protect_interrupt: 是否防护中断
        :type protect_interrupt: bool
        :param incluster: 是否集群内节点
        :type incluster: bool
        :param protect_degradation: 是否防护降级
        :type protect_degradation: bool
        :param limit: 每页显示数量
        :type limit: int
        :param offset: 偏移量：指定返回记录的开始位置
        :type offset: int
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
        self._vpc_id = None
        self._region = None
        self._has_intrusion = None
        self._has_vul = None
        self._has_baseline = None
        self._sort_key = None
        self._sort_dir = None
        self._policy_group_id = None
        self._policy_group_name = None
        self._charging_mode = None
        self._refresh = None
        self._get_common_login_locations = None
        self._above_version = None
        self._outside_host = None
        self._asset_value = None
        self._label = None
        self._server_group = None
        self._agent_upgradable = None
        self._install_mode = None
        self._binding_key = None
        self._protect_interrupt = None
        self._incluster = None
        self._protect_degradation = None
        self._limit = None
        self._offset = None
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
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if region is not None:
            self.region = region
        if has_intrusion is not None:
            self.has_intrusion = has_intrusion
        if has_vul is not None:
            self.has_vul = has_vul
        if has_baseline is not None:
            self.has_baseline = has_baseline
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if policy_group_id is not None:
            self.policy_group_id = policy_group_id
        if policy_group_name is not None:
            self.policy_group_name = policy_group_name
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if refresh is not None:
            self.refresh = refresh
        if get_common_login_locations is not None:
            self.get_common_login_locations = get_common_login_locations
        if above_version is not None:
            self.above_version = above_version
        if outside_host is not None:
            self.outside_host = outside_host
        if asset_value is not None:
            self.asset_value = asset_value
        if label is not None:
            self.label = label
        if server_group is not None:
            self.server_group = server_group
        if agent_upgradable is not None:
            self.agent_upgradable = agent_upgradable
        if install_mode is not None:
            self.install_mode = install_mode
        if binding_key is not None:
            self.binding_key = binding_key
        if protect_interrupt is not None:
            self.protect_interrupt = protect_interrupt
        if incluster is not None:
            self.incluster = incluster
        if protect_degradation is not None:
            self.protect_degradation = protect_degradation
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListHostStatusRequest.

        主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。

        :return: The enterprise_project_id of this ListHostStatusRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListHostStatusRequest.

        主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。

        :param enterprise_project_id: The enterprise_project_id of this ListHostStatusRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def version(self):
        r"""Gets the version of this ListHostStatusRequest.

        主机开通的版本，包含如下7种输入。   - hss.version.null ：无。   - hss.version.basic ：基础版。   - hss.version.advanced ：专业版。   - hss.version.enterprise ：企业版。   - hss.version.premium ：旗舰版。   - hss.version.wtp ：网页防篡改版。   - hss.version.container.enterprise：容器版。

        :return: The version of this ListHostStatusRequest.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ListHostStatusRequest.

        主机开通的版本，包含如下7种输入。   - hss.version.null ：无。   - hss.version.basic ：基础版。   - hss.version.advanced ：专业版。   - hss.version.enterprise ：企业版。   - hss.version.premium ：旗舰版。   - hss.version.wtp ：网页防篡改版。   - hss.version.container.enterprise：容器版。

        :param version: The version of this ListHostStatusRequest.
        :type version: str
        """
        self._version = version

    @property
    def agent_status(self):
        r"""Gets the agent_status of this ListHostStatusRequest.

        Agent状态，包含如下6种。   - installed ：已安装。   - not_installed ：未安装。   - online ：在线。   - offline ：离线。   - install_failed ：安装失败。   - installing ：安装中。   - not_online ：不在线的（除了在线以外的所有状态，仅作为查询条件）。

        :return: The agent_status of this ListHostStatusRequest.
        :rtype: str
        """
        return self._agent_status

    @agent_status.setter
    def agent_status(self, agent_status):
        r"""Sets the agent_status of this ListHostStatusRequest.

        Agent状态，包含如下6种。   - installed ：已安装。   - not_installed ：未安装。   - online ：在线。   - offline ：离线。   - install_failed ：安装失败。   - installing ：安装中。   - not_online ：不在线的（除了在线以外的所有状态，仅作为查询条件）。

        :param agent_status: The agent_status of this ListHostStatusRequest.
        :type agent_status: str
        """
        self._agent_status = agent_status

    @property
    def detect_result(self):
        r"""Gets the detect_result of this ListHostStatusRequest.

        检测结果，包含如下4种。   - undetected ：未检测。   - clean ：无风险。   - risk ：有风险。   - scanning ：检测中。

        :return: The detect_result of this ListHostStatusRequest.
        :rtype: str
        """
        return self._detect_result

    @detect_result.setter
    def detect_result(self, detect_result):
        r"""Sets the detect_result of this ListHostStatusRequest.

        检测结果，包含如下4种。   - undetected ：未检测。   - clean ：无风险。   - risk ：有风险。   - scanning ：检测中。

        :param detect_result: The detect_result of this ListHostStatusRequest.
        :type detect_result: str
        """
        self._detect_result = detect_result

    @property
    def host_name(self):
        r"""Gets the host_name of this ListHostStatusRequest.

        服务器名称

        :return: The host_name of this ListHostStatusRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ListHostStatusRequest.

        服务器名称

        :param host_name: The host_name of this ListHostStatusRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_id(self):
        r"""Gets the host_id of this ListHostStatusRequest.

        服务器ID

        :return: The host_id of this ListHostStatusRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ListHostStatusRequest.

        服务器ID

        :param host_id: The host_id of this ListHostStatusRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_status(self):
        r"""Gets the host_status of this ListHostStatusRequest.

        主机状态，包含如下4种。   - ACTIVE ：正在运行。   - SHUTOFF ：关机。   - BUILDING ：创建中。   - ERROR ：故障。

        :return: The host_status of this ListHostStatusRequest.
        :rtype: str
        """
        return self._host_status

    @host_status.setter
    def host_status(self, host_status):
        r"""Sets the host_status of this ListHostStatusRequest.

        主机状态，包含如下4种。   - ACTIVE ：正在运行。   - SHUTOFF ：关机。   - BUILDING ：创建中。   - ERROR ：故障。

        :param host_status: The host_status of this ListHostStatusRequest.
        :type host_status: str
        """
        self._host_status = host_status

    @property
    def os_type(self):
        r"""Gets the os_type of this ListHostStatusRequest.

        操作系统类型，包含如下2种。   - Linux ：Linux。   - Windows ：Windows。

        :return: The os_type of this ListHostStatusRequest.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this ListHostStatusRequest.

        操作系统类型，包含如下2种。   - Linux ：Linux。   - Windows ：Windows。

        :param os_type: The os_type of this ListHostStatusRequest.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def private_ip(self):
        r"""Gets the private_ip of this ListHostStatusRequest.

        服务器私有IP

        :return: The private_ip of this ListHostStatusRequest.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this ListHostStatusRequest.

        服务器私有IP

        :param private_ip: The private_ip of this ListHostStatusRequest.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def public_ip(self):
        r"""Gets the public_ip of this ListHostStatusRequest.

        服务器公网IP

        :return: The public_ip of this ListHostStatusRequest.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this ListHostStatusRequest.

        服务器公网IP

        :param public_ip: The public_ip of this ListHostStatusRequest.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def ip_addr(self):
        r"""Gets the ip_addr of this ListHostStatusRequest.

        公网或私网IP

        :return: The ip_addr of this ListHostStatusRequest.
        :rtype: str
        """
        return self._ip_addr

    @ip_addr.setter
    def ip_addr(self, ip_addr):
        r"""Sets the ip_addr of this ListHostStatusRequest.

        公网或私网IP

        :param ip_addr: The ip_addr of this ListHostStatusRequest.
        :type ip_addr: str
        """
        self._ip_addr = ip_addr

    @property
    def protect_status(self):
        r"""Gets the protect_status of this ListHostStatusRequest.

        防护状态，包含如下2种。   - closed ：关闭。   - opened ：开启。   - protection_exception ：防护异常。

        :return: The protect_status of this ListHostStatusRequest.
        :rtype: str
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        r"""Sets the protect_status of this ListHostStatusRequest.

        防护状态，包含如下2种。   - closed ：关闭。   - opened ：开启。   - protection_exception ：防护异常。

        :param protect_status: The protect_status of this ListHostStatusRequest.
        :type protect_status: str
        """
        self._protect_status = protect_status

    @property
    def group_id(self):
        r"""Gets the group_id of this ListHostStatusRequest.

        服务器组ID

        :return: The group_id of this ListHostStatusRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ListHostStatusRequest.

        服务器组ID

        :param group_id: The group_id of this ListHostStatusRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def group_name(self):
        r"""Gets the group_name of this ListHostStatusRequest.

        服务器组名称

        :return: The group_name of this ListHostStatusRequest.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this ListHostStatusRequest.

        服务器组名称

        :param group_name: The group_name of this ListHostStatusRequest.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this ListHostStatusRequest.

        vpc id

        :return: The vpc_id of this ListHostStatusRequest.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this ListHostStatusRequest.

        vpc id

        :param vpc_id: The vpc_id of this ListHostStatusRequest.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def region(self):
        r"""Gets the region of this ListHostStatusRequest.

        Region ID

        :return: The region of this ListHostStatusRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ListHostStatusRequest.

        Region ID

        :param region: The region of this ListHostStatusRequest.
        :type region: str
        """
        self._region = region

    @property
    def has_intrusion(self):
        r"""Gets the has_intrusion of this ListHostStatusRequest.

        存在告警事件

        :return: The has_intrusion of this ListHostStatusRequest.
        :rtype: bool
        """
        return self._has_intrusion

    @has_intrusion.setter
    def has_intrusion(self, has_intrusion):
        r"""Sets the has_intrusion of this ListHostStatusRequest.

        存在告警事件

        :param has_intrusion: The has_intrusion of this ListHostStatusRequest.
        :type has_intrusion: bool
        """
        self._has_intrusion = has_intrusion

    @property
    def has_vul(self):
        r"""Gets the has_vul of this ListHostStatusRequest.

        存在漏洞风险

        :return: The has_vul of this ListHostStatusRequest.
        :rtype: bool
        """
        return self._has_vul

    @has_vul.setter
    def has_vul(self, has_vul):
        r"""Sets the has_vul of this ListHostStatusRequest.

        存在漏洞风险

        :param has_vul: The has_vul of this ListHostStatusRequest.
        :type has_vul: bool
        """
        self._has_vul = has_vul

    @property
    def has_baseline(self):
        r"""Gets the has_baseline of this ListHostStatusRequest.

        存在基线风险

        :return: The has_baseline of this ListHostStatusRequest.
        :rtype: bool
        """
        return self._has_baseline

    @has_baseline.setter
    def has_baseline(self, has_baseline):
        r"""Sets the has_baseline of this ListHostStatusRequest.

        存在基线风险

        :param has_baseline: The has_baseline of this ListHostStatusRequest.
        :type has_baseline: bool
        """
        self._has_baseline = has_baseline

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListHostStatusRequest.

        排序字段，只支持risk_num - risk_num：风险总量

        :return: The sort_key of this ListHostStatusRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListHostStatusRequest.

        排序字段，只支持risk_num - risk_num：风险总量

        :param sort_key: The sort_key of this ListHostStatusRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListHostStatusRequest.

        排序的顺序 - asc: 正序 - desc: 倒序

        :return: The sort_dir of this ListHostStatusRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListHostStatusRequest.

        排序的顺序 - asc: 正序 - desc: 倒序

        :param sort_dir: The sort_dir of this ListHostStatusRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def policy_group_id(self):
        r"""Gets the policy_group_id of this ListHostStatusRequest.

        策略组ID

        :return: The policy_group_id of this ListHostStatusRequest.
        :rtype: str
        """
        return self._policy_group_id

    @policy_group_id.setter
    def policy_group_id(self, policy_group_id):
        r"""Sets the policy_group_id of this ListHostStatusRequest.

        策略组ID

        :param policy_group_id: The policy_group_id of this ListHostStatusRequest.
        :type policy_group_id: str
        """
        self._policy_group_id = policy_group_id

    @property
    def policy_group_name(self):
        r"""Gets the policy_group_name of this ListHostStatusRequest.

        策略组名称

        :return: The policy_group_name of this ListHostStatusRequest.
        :rtype: str
        """
        return self._policy_group_name

    @policy_group_name.setter
    def policy_group_name(self, policy_group_name):
        r"""Sets the policy_group_name of this ListHostStatusRequest.

        策略组名称

        :param policy_group_name: The policy_group_name of this ListHostStatusRequest.
        :type policy_group_name: str
        """
        self._policy_group_name = policy_group_name

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this ListHostStatusRequest.

        收费模式，包含如下2种。   - packet_cycle ：包年/包月。   - on_demand ：按需。

        :return: The charging_mode of this ListHostStatusRequest.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this ListHostStatusRequest.

        收费模式，包含如下2种。   - packet_cycle ：包年/包月。   - on_demand ：按需。

        :param charging_mode: The charging_mode of this ListHostStatusRequest.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def refresh(self):
        r"""Gets the refresh of this ListHostStatusRequest.

        是否强制从ECS同步主机

        :return: The refresh of this ListHostStatusRequest.
        :rtype: bool
        """
        return self._refresh

    @refresh.setter
    def refresh(self, refresh):
        r"""Sets the refresh of this ListHostStatusRequest.

        是否强制从ECS同步主机

        :param refresh: The refresh of this ListHostStatusRequest.
        :type refresh: bool
        """
        self._refresh = refresh

    @property
    def get_common_login_locations(self):
        r"""Gets the get_common_login_locations of this ListHostStatusRequest.

        是否获取主机常用登录地信息

        :return: The get_common_login_locations of this ListHostStatusRequest.
        :rtype: bool
        """
        return self._get_common_login_locations

    @get_common_login_locations.setter
    def get_common_login_locations(self, get_common_login_locations):
        r"""Sets the get_common_login_locations of this ListHostStatusRequest.

        是否获取主机常用登录地信息

        :param get_common_login_locations: The get_common_login_locations of this ListHostStatusRequest.
        :type get_common_login_locations: bool
        """
        self._get_common_login_locations = get_common_login_locations

    @property
    def above_version(self):
        r"""Gets the above_version of this ListHostStatusRequest.

        是否返回比当前版本高的所有版本

        :return: The above_version of this ListHostStatusRequest.
        :rtype: bool
        """
        return self._above_version

    @above_version.setter
    def above_version(self, above_version):
        r"""Sets the above_version of this ListHostStatusRequest.

        是否返回比当前版本高的所有版本

        :param above_version: The above_version of this ListHostStatusRequest.
        :type above_version: bool
        """
        self._above_version = above_version

    @property
    def outside_host(self):
        r"""Gets the outside_host of this ListHostStatusRequest.

        是否华为云主机

        :return: The outside_host of this ListHostStatusRequest.
        :rtype: bool
        """
        return self._outside_host

    @outside_host.setter
    def outside_host(self, outside_host):
        r"""Sets the outside_host of this ListHostStatusRequest.

        是否华为云主机

        :param outside_host: The outside_host of this ListHostStatusRequest.
        :type outside_host: bool
        """
        self._outside_host = outside_host

    @property
    def asset_value(self):
        r"""Gets the asset_value of this ListHostStatusRequest.

        资产重要性，包含如下4种   - important ：重要资产   - common ：一般资产   - test ：测试资产

        :return: The asset_value of this ListHostStatusRequest.
        :rtype: str
        """
        return self._asset_value

    @asset_value.setter
    def asset_value(self, asset_value):
        r"""Sets the asset_value of this ListHostStatusRequest.

        资产重要性，包含如下4种   - important ：重要资产   - common ：一般资产   - test ：测试资产

        :param asset_value: The asset_value of this ListHostStatusRequest.
        :type asset_value: str
        """
        self._asset_value = asset_value

    @property
    def label(self):
        r"""Gets the label of this ListHostStatusRequest.

        资产标签

        :return: The label of this ListHostStatusRequest.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        r"""Sets the label of this ListHostStatusRequest.

        资产标签

        :param label: The label of this ListHostStatusRequest.
        :type label: str
        """
        self._label = label

    @property
    def server_group(self):
        r"""Gets the server_group of this ListHostStatusRequest.

        资产服务器组

        :return: The server_group of this ListHostStatusRequest.
        :rtype: str
        """
        return self._server_group

    @server_group.setter
    def server_group(self, server_group):
        r"""Sets the server_group of this ListHostStatusRequest.

        资产服务器组

        :param server_group: The server_group of this ListHostStatusRequest.
        :type server_group: str
        """
        self._server_group = server_group

    @property
    def agent_upgradable(self):
        r"""Gets the agent_upgradable of this ListHostStatusRequest.

        agent是否可升级

        :return: The agent_upgradable of this ListHostStatusRequest.
        :rtype: bool
        """
        return self._agent_upgradable

    @agent_upgradable.setter
    def agent_upgradable(self, agent_upgradable):
        r"""Sets the agent_upgradable of this ListHostStatusRequest.

        agent是否可升级

        :param agent_upgradable: The agent_upgradable of this ListHostStatusRequest.
        :type agent_upgradable: bool
        """
        self._agent_upgradable = agent_upgradable

    @property
    def install_mode(self):
        r"""Gets the install_mode of this ListHostStatusRequest.

        是否安装模式场景

        :return: The install_mode of this ListHostStatusRequest.
        :rtype: bool
        """
        return self._install_mode

    @install_mode.setter
    def install_mode(self, install_mode):
        r"""Sets the install_mode of this ListHostStatusRequest.

        是否安装模式场景

        :param install_mode: The install_mode of this ListHostStatusRequest.
        :type install_mode: bool
        """
        self._install_mode = install_mode

    @property
    def binding_key(self):
        r"""Gets the binding_key of this ListHostStatusRequest.

        是否绑定DEW密钥

        :return: The binding_key of this ListHostStatusRequest.
        :rtype: bool
        """
        return self._binding_key

    @binding_key.setter
    def binding_key(self, binding_key):
        r"""Sets the binding_key of this ListHostStatusRequest.

        是否绑定DEW密钥

        :param binding_key: The binding_key of this ListHostStatusRequest.
        :type binding_key: bool
        """
        self._binding_key = binding_key

    @property
    def protect_interrupt(self):
        r"""Gets the protect_interrupt of this ListHostStatusRequest.

        是否防护中断

        :return: The protect_interrupt of this ListHostStatusRequest.
        :rtype: bool
        """
        return self._protect_interrupt

    @protect_interrupt.setter
    def protect_interrupt(self, protect_interrupt):
        r"""Sets the protect_interrupt of this ListHostStatusRequest.

        是否防护中断

        :param protect_interrupt: The protect_interrupt of this ListHostStatusRequest.
        :type protect_interrupt: bool
        """
        self._protect_interrupt = protect_interrupt

    @property
    def incluster(self):
        r"""Gets the incluster of this ListHostStatusRequest.

        是否集群内节点

        :return: The incluster of this ListHostStatusRequest.
        :rtype: bool
        """
        return self._incluster

    @incluster.setter
    def incluster(self, incluster):
        r"""Sets the incluster of this ListHostStatusRequest.

        是否集群内节点

        :param incluster: The incluster of this ListHostStatusRequest.
        :type incluster: bool
        """
        self._incluster = incluster

    @property
    def protect_degradation(self):
        r"""Gets the protect_degradation of this ListHostStatusRequest.

        是否防护降级

        :return: The protect_degradation of this ListHostStatusRequest.
        :rtype: bool
        """
        return self._protect_degradation

    @protect_degradation.setter
    def protect_degradation(self, protect_degradation):
        r"""Sets the protect_degradation of this ListHostStatusRequest.

        是否防护降级

        :param protect_degradation: The protect_degradation of this ListHostStatusRequest.
        :type protect_degradation: bool
        """
        self._protect_degradation = protect_degradation

    @property
    def limit(self):
        r"""Gets the limit of this ListHostStatusRequest.

        每页显示数量

        :return: The limit of this ListHostStatusRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListHostStatusRequest.

        每页显示数量

        :param limit: The limit of this ListHostStatusRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListHostStatusRequest.

        偏移量：指定返回记录的开始位置

        :return: The offset of this ListHostStatusRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListHostStatusRequest.

        偏移量：指定返回记录的开始位置

        :param offset: The offset of this ListHostStatusRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListHostStatusRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
