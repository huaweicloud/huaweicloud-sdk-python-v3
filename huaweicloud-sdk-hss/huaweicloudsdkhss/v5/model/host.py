# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Host:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_name': 'str',
        'host_id': 'str',
        'agent_id': 'str',
        'private_ip': 'str',
        'public_ip': 'str',
        'enterprise_project_id': 'str',
        'enterprise_project_name': 'str',
        'os_name': 'str',
        'os_version': 'str',
        'kernel_version': 'str',
        'host_status': 'str',
        'agent_status': 'str',
        'install_result_code': 'str',
        'version': 'str',
        'protect_status': 'str',
        'os_image': 'str',
        'os_type': 'str',
        'os_bit': 'str',
        'detect_result': 'str',
        'expire_time': 'int',
        'charging_mode': 'str',
        'resource_id': 'str',
        'outside_host': 'bool',
        'group_id': 'str',
        'group_name': 'str',
        'policy_group_id': 'str',
        'policy_group_name': 'str',
        'asset': 'int',
        'vulnerability': 'int',
        'baseline': 'int',
        'intrusion': 'int',
        'asset_value': 'str',
        'labels': 'list[str]',
        'agent_create_time': 'int',
        'agent_update_time': 'int',
        'agent_version': 'str',
        'upgrade_status': 'str',
        'upgrade_result_code': 'str',
        'upgradable': 'bool',
        'open_time': 'int',
        'protect_interrupt': 'bool',
        'protect_degradation': 'bool',
        'host_sources': 'str',
        'interrupt_reason': 'str',
        'degradation_reason': 'str',
        'key_name': 'str',
        'auto_open_version': 'str',
        'install_progress': 'int',
        'vpc_id': 'str',
        'common_login_area_codes': 'list[int]',
        'cluster_name': 'str',
        'cluster_id': 'str'
    }

    attribute_map = {
        'host_name': 'host_name',
        'host_id': 'host_id',
        'agent_id': 'agent_id',
        'private_ip': 'private_ip',
        'public_ip': 'public_ip',
        'enterprise_project_id': 'enterprise_project_id',
        'enterprise_project_name': 'enterprise_project_name',
        'os_name': 'os_name',
        'os_version': 'os_version',
        'kernel_version': 'kernel_version',
        'host_status': 'host_status',
        'agent_status': 'agent_status',
        'install_result_code': 'install_result_code',
        'version': 'version',
        'protect_status': 'protect_status',
        'os_image': 'os_image',
        'os_type': 'os_type',
        'os_bit': 'os_bit',
        'detect_result': 'detect_result',
        'expire_time': 'expire_time',
        'charging_mode': 'charging_mode',
        'resource_id': 'resource_id',
        'outside_host': 'outside_host',
        'group_id': 'group_id',
        'group_name': 'group_name',
        'policy_group_id': 'policy_group_id',
        'policy_group_name': 'policy_group_name',
        'asset': 'asset',
        'vulnerability': 'vulnerability',
        'baseline': 'baseline',
        'intrusion': 'intrusion',
        'asset_value': 'asset_value',
        'labels': 'labels',
        'agent_create_time': 'agent_create_time',
        'agent_update_time': 'agent_update_time',
        'agent_version': 'agent_version',
        'upgrade_status': 'upgrade_status',
        'upgrade_result_code': 'upgrade_result_code',
        'upgradable': 'upgradable',
        'open_time': 'open_time',
        'protect_interrupt': 'protect_interrupt',
        'protect_degradation': 'protect_degradation',
        'host_sources': 'host_sources',
        'interrupt_reason': 'interrupt_reason',
        'degradation_reason': 'degradation_reason',
        'key_name': 'key_name',
        'auto_open_version': 'auto_open_version',
        'install_progress': 'install_progress',
        'vpc_id': 'vpc_id',
        'common_login_area_codes': 'common_login_area_codes',
        'cluster_name': 'cluster_name',
        'cluster_id': 'cluster_id'
    }

    def __init__(self, host_name=None, host_id=None, agent_id=None, private_ip=None, public_ip=None, enterprise_project_id=None, enterprise_project_name=None, os_name=None, os_version=None, kernel_version=None, host_status=None, agent_status=None, install_result_code=None, version=None, protect_status=None, os_image=None, os_type=None, os_bit=None, detect_result=None, expire_time=None, charging_mode=None, resource_id=None, outside_host=None, group_id=None, group_name=None, policy_group_id=None, policy_group_name=None, asset=None, vulnerability=None, baseline=None, intrusion=None, asset_value=None, labels=None, agent_create_time=None, agent_update_time=None, agent_version=None, upgrade_status=None, upgrade_result_code=None, upgradable=None, open_time=None, protect_interrupt=None, protect_degradation=None, host_sources=None, interrupt_reason=None, degradation_reason=None, key_name=None, auto_open_version=None, install_progress=None, vpc_id=None, common_login_area_codes=None, cluster_name=None, cluster_id=None):
        r"""Host

        The model defined in huaweicloud sdk

        :param host_name: 服务器名称
        :type host_name: str
        :param host_id: 服务器ID
        :type host_id: str
        :param agent_id: Agent ID
        :type agent_id: str
        :param private_ip: 私有IP地址
        :type private_ip: str
        :param public_ip: 弹性公网IP地址
        :type public_ip: str
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        :param enterprise_project_name: 所属企业项目名称
        :type enterprise_project_name: str
        :param os_name: 系统名称
        :type os_name: str
        :param os_version: 系统版本
        :type os_version: str
        :param kernel_version: 内核版本
        :type kernel_version: str
        :param host_status: 服务器状态，包含如下4种。   - ACTIVE ：运行中。   - SHUTOFF ：关机。   - BUILDING ：创建中。   - ERROR ：故障。
        :type host_status: str
        :param agent_status: Agent状态，包含如下5种。   - installed ：已安装。   - not_installed ：未安装。   - online ：在线。   - offline ：离线。   - install_failed ：安装失败。   - installing ：安装中。
        :type agent_status: str
        :param install_result_code: 安装结果，包含如下12种。   - install_succeed ：安装成功。   - network_access_timeout ：网络不通，访问超时。   - invalid_port ：无效端口。   - auth_failed ：认证错误，口令不正确。   - permission_denied ：权限错误，被拒绝。   - no_available_vpc ：没有相同VPC的agent在线虚拟机。   - install_exception ：安装异常。   - invalid_param ：参数错误。   - install_failed ：安装失败。   - package_unavailable ：安装包失效。   - os_type_not_support ：系统类型错误。   - os_arch_not_support ：架构类型错误。
        :type install_result_code: str
        :param version: 主机开通的版本，包含如下7种输入。   - hss.version.null ：无。   - hss.version.basic ：基础版。   - hss.version.advanced ：专业版。   - hss.version.enterprise ：企业版。   - hss.version.premium ：旗舰版。   - hss.version.wtp ：网页防篡改版。   - hss.version.container.enterprise ：容器版。
        :type version: str
        :param protect_status: 防护状态，包含如下2种。 - closed ：未防护。 - opened ：防护中。 - protection_exception ：防护异常。
        :type protect_status: str
        :param os_image: 系统镜像
        :type os_image: str
        :param os_type: 操作系统类型，包含如下2种。   - Linux ：Linux。   - Windows ：Windows。
        :type os_type: str
        :param os_bit: 操作系统位数
        :type os_bit: str
        :param detect_result: 云主机安全检测结果，包含如下4种。 - undetected ：未检测。 - clean ：无风险。 - risk ：有风险。 - scanning ：检测中。
        :type detect_result: str
        :param expire_time: 试用版到期时间（-1表示非试用版配额，当值不为-1时为试用版本过期时间）
        :type expire_time: int
        :param charging_mode: 收费模式，包含如下2种。   - packet_cycle ：包年/包月。   - on_demand ：按需。
        :type charging_mode: str
        :param resource_id: 主机安全配额ID（UUID）
        :type resource_id: str
        :param outside_host: 是否非华为云机器
        :type outside_host: bool
        :param group_id: 服务器组ID
        :type group_id: str
        :param group_name: 服务器组名称
        :type group_name: str
        :param policy_group_id: 策略组ID
        :type policy_group_id: str
        :param policy_group_name: 策略组名称
        :type policy_group_name: str
        :param asset: 资产风险
        :type asset: int
        :param vulnerability: 漏洞风险总数，包含Linux软件漏洞、Windows系统漏洞、Web-CMS漏洞、应用漏洞
        :type vulnerability: int
        :param baseline: 基线风险总数，包含配置风险、弱口令
        :type baseline: int
        :param intrusion: 入侵风险总数
        :type intrusion: int
        :param asset_value: 资产重要性，包含如下4种   - important ：重要资产   - common ：一般资产   - test ：测试资产
        :type asset_value: str
        :param labels: 标签列表
        :type labels: list[str]
        :param agent_create_time: agent安装时间，采用时间戳，默认毫秒，
        :type agent_create_time: int
        :param agent_update_time: agent状态修改时间，采用时间戳，默认毫秒，
        :type agent_update_time: int
        :param agent_version: agent版本
        :type agent_version: str
        :param upgrade_status: 升级状态，包含如下4种。   - not_upgrade ：未升级，也就是默认状态，客户还没有给这台机器下发过升级。   - upgrading ：正在升级中。   - upgrade_failed ：升级失败。   - upgrade_succeed ：升级成功。
        :type upgrade_status: str
        :param upgrade_result_code: 升级失败原因，只有当 upgrade_status 为 upgrade_failed 时才显示，包含如下6种。   - package_unavailable ：升级包解析失败，升级文件有错误。   - network_access_timeout ：下载升级包失败，网络异常。   - agent_offline ：agent离线。   - hostguard_abnormal ：agent工作进程异常。   - insufficient_disk_space ：磁盘空间不足。   - failed_to_replace_file ：替换文件失败。
        :type upgrade_result_code: str
        :param upgradable: 该服务器agent是否可升级
        :type upgradable: bool
        :param open_time: 开启防护时间，采用时间戳，默认毫秒，
        :type open_time: int
        :param protect_interrupt: 防护是否中断
        :type protect_interrupt: bool
        :param protect_degradation: 防护是否降级
        :type protect_degradation: bool
        :param host_sources: 服务器来源
        :type host_sources: str
        :param interrupt_reason: 防护中断原因
        :type interrupt_reason: str
        :param degradation_reason: 防护降级原因
        :type degradation_reason: str
        :param key_name: 使用的密钥对名称
        :type key_name: str
        :param auto_open_version: cce购买主机
        :type auto_open_version: str
        :param install_progress: 安装进度
        :type install_progress: int
        :param vpc_id: vpc id
        :type vpc_id: str
        :param common_login_area_codes: 后台识别服务器常用登录地编号
        :type common_login_area_codes: list[int]
        :param cluster_name: 集群名称
        :type cluster_name: str
        :param cluster_id: 集群id
        :type cluster_id: str
        """
        
        

        self._host_name = None
        self._host_id = None
        self._agent_id = None
        self._private_ip = None
        self._public_ip = None
        self._enterprise_project_id = None
        self._enterprise_project_name = None
        self._os_name = None
        self._os_version = None
        self._kernel_version = None
        self._host_status = None
        self._agent_status = None
        self._install_result_code = None
        self._version = None
        self._protect_status = None
        self._os_image = None
        self._os_type = None
        self._os_bit = None
        self._detect_result = None
        self._expire_time = None
        self._charging_mode = None
        self._resource_id = None
        self._outside_host = None
        self._group_id = None
        self._group_name = None
        self._policy_group_id = None
        self._policy_group_name = None
        self._asset = None
        self._vulnerability = None
        self._baseline = None
        self._intrusion = None
        self._asset_value = None
        self._labels = None
        self._agent_create_time = None
        self._agent_update_time = None
        self._agent_version = None
        self._upgrade_status = None
        self._upgrade_result_code = None
        self._upgradable = None
        self._open_time = None
        self._protect_interrupt = None
        self._protect_degradation = None
        self._host_sources = None
        self._interrupt_reason = None
        self._degradation_reason = None
        self._key_name = None
        self._auto_open_version = None
        self._install_progress = None
        self._vpc_id = None
        self._common_login_area_codes = None
        self._cluster_name = None
        self._cluster_id = None
        self.discriminator = None

        if host_name is not None:
            self.host_name = host_name
        if host_id is not None:
            self.host_id = host_id
        if agent_id is not None:
            self.agent_id = agent_id
        if private_ip is not None:
            self.private_ip = private_ip
        if public_ip is not None:
            self.public_ip = public_ip
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if enterprise_project_name is not None:
            self.enterprise_project_name = enterprise_project_name
        if os_name is not None:
            self.os_name = os_name
        if os_version is not None:
            self.os_version = os_version
        if kernel_version is not None:
            self.kernel_version = kernel_version
        if host_status is not None:
            self.host_status = host_status
        if agent_status is not None:
            self.agent_status = agent_status
        if install_result_code is not None:
            self.install_result_code = install_result_code
        if version is not None:
            self.version = version
        if protect_status is not None:
            self.protect_status = protect_status
        if os_image is not None:
            self.os_image = os_image
        if os_type is not None:
            self.os_type = os_type
        if os_bit is not None:
            self.os_bit = os_bit
        if detect_result is not None:
            self.detect_result = detect_result
        if expire_time is not None:
            self.expire_time = expire_time
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if resource_id is not None:
            self.resource_id = resource_id
        if outside_host is not None:
            self.outside_host = outside_host
        if group_id is not None:
            self.group_id = group_id
        if group_name is not None:
            self.group_name = group_name
        if policy_group_id is not None:
            self.policy_group_id = policy_group_id
        if policy_group_name is not None:
            self.policy_group_name = policy_group_name
        if asset is not None:
            self.asset = asset
        if vulnerability is not None:
            self.vulnerability = vulnerability
        if baseline is not None:
            self.baseline = baseline
        if intrusion is not None:
            self.intrusion = intrusion
        if asset_value is not None:
            self.asset_value = asset_value
        if labels is not None:
            self.labels = labels
        if agent_create_time is not None:
            self.agent_create_time = agent_create_time
        if agent_update_time is not None:
            self.agent_update_time = agent_update_time
        if agent_version is not None:
            self.agent_version = agent_version
        if upgrade_status is not None:
            self.upgrade_status = upgrade_status
        if upgrade_result_code is not None:
            self.upgrade_result_code = upgrade_result_code
        if upgradable is not None:
            self.upgradable = upgradable
        if open_time is not None:
            self.open_time = open_time
        if protect_interrupt is not None:
            self.protect_interrupt = protect_interrupt
        if protect_degradation is not None:
            self.protect_degradation = protect_degradation
        if host_sources is not None:
            self.host_sources = host_sources
        if interrupt_reason is not None:
            self.interrupt_reason = interrupt_reason
        if degradation_reason is not None:
            self.degradation_reason = degradation_reason
        if key_name is not None:
            self.key_name = key_name
        if auto_open_version is not None:
            self.auto_open_version = auto_open_version
        if install_progress is not None:
            self.install_progress = install_progress
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if common_login_area_codes is not None:
            self.common_login_area_codes = common_login_area_codes
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if cluster_id is not None:
            self.cluster_id = cluster_id

    @property
    def host_name(self):
        r"""Gets the host_name of this Host.

        服务器名称

        :return: The host_name of this Host.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this Host.

        服务器名称

        :param host_name: The host_name of this Host.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_id(self):
        r"""Gets the host_id of this Host.

        服务器ID

        :return: The host_id of this Host.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this Host.

        服务器ID

        :param host_id: The host_id of this Host.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def agent_id(self):
        r"""Gets the agent_id of this Host.

        Agent ID

        :return: The agent_id of this Host.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this Host.

        Agent ID

        :param agent_id: The agent_id of this Host.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def private_ip(self):
        r"""Gets the private_ip of this Host.

        私有IP地址

        :return: The private_ip of this Host.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this Host.

        私有IP地址

        :param private_ip: The private_ip of this Host.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def public_ip(self):
        r"""Gets the public_ip of this Host.

        弹性公网IP地址

        :return: The public_ip of this Host.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this Host.

        弹性公网IP地址

        :param public_ip: The public_ip of this Host.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this Host.

        企业项目ID

        :return: The enterprise_project_id of this Host.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this Host.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this Host.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def enterprise_project_name(self):
        r"""Gets the enterprise_project_name of this Host.

        所属企业项目名称

        :return: The enterprise_project_name of this Host.
        :rtype: str
        """
        return self._enterprise_project_name

    @enterprise_project_name.setter
    def enterprise_project_name(self, enterprise_project_name):
        r"""Sets the enterprise_project_name of this Host.

        所属企业项目名称

        :param enterprise_project_name: The enterprise_project_name of this Host.
        :type enterprise_project_name: str
        """
        self._enterprise_project_name = enterprise_project_name

    @property
    def os_name(self):
        r"""Gets the os_name of this Host.

        系统名称

        :return: The os_name of this Host.
        :rtype: str
        """
        return self._os_name

    @os_name.setter
    def os_name(self, os_name):
        r"""Sets the os_name of this Host.

        系统名称

        :param os_name: The os_name of this Host.
        :type os_name: str
        """
        self._os_name = os_name

    @property
    def os_version(self):
        r"""Gets the os_version of this Host.

        系统版本

        :return: The os_version of this Host.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        r"""Sets the os_version of this Host.

        系统版本

        :param os_version: The os_version of this Host.
        :type os_version: str
        """
        self._os_version = os_version

    @property
    def kernel_version(self):
        r"""Gets the kernel_version of this Host.

        内核版本

        :return: The kernel_version of this Host.
        :rtype: str
        """
        return self._kernel_version

    @kernel_version.setter
    def kernel_version(self, kernel_version):
        r"""Sets the kernel_version of this Host.

        内核版本

        :param kernel_version: The kernel_version of this Host.
        :type kernel_version: str
        """
        self._kernel_version = kernel_version

    @property
    def host_status(self):
        r"""Gets the host_status of this Host.

        服务器状态，包含如下4种。   - ACTIVE ：运行中。   - SHUTOFF ：关机。   - BUILDING ：创建中。   - ERROR ：故障。

        :return: The host_status of this Host.
        :rtype: str
        """
        return self._host_status

    @host_status.setter
    def host_status(self, host_status):
        r"""Sets the host_status of this Host.

        服务器状态，包含如下4种。   - ACTIVE ：运行中。   - SHUTOFF ：关机。   - BUILDING ：创建中。   - ERROR ：故障。

        :param host_status: The host_status of this Host.
        :type host_status: str
        """
        self._host_status = host_status

    @property
    def agent_status(self):
        r"""Gets the agent_status of this Host.

        Agent状态，包含如下5种。   - installed ：已安装。   - not_installed ：未安装。   - online ：在线。   - offline ：离线。   - install_failed ：安装失败。   - installing ：安装中。

        :return: The agent_status of this Host.
        :rtype: str
        """
        return self._agent_status

    @agent_status.setter
    def agent_status(self, agent_status):
        r"""Sets the agent_status of this Host.

        Agent状态，包含如下5种。   - installed ：已安装。   - not_installed ：未安装。   - online ：在线。   - offline ：离线。   - install_failed ：安装失败。   - installing ：安装中。

        :param agent_status: The agent_status of this Host.
        :type agent_status: str
        """
        self._agent_status = agent_status

    @property
    def install_result_code(self):
        r"""Gets the install_result_code of this Host.

        安装结果，包含如下12种。   - install_succeed ：安装成功。   - network_access_timeout ：网络不通，访问超时。   - invalid_port ：无效端口。   - auth_failed ：认证错误，口令不正确。   - permission_denied ：权限错误，被拒绝。   - no_available_vpc ：没有相同VPC的agent在线虚拟机。   - install_exception ：安装异常。   - invalid_param ：参数错误。   - install_failed ：安装失败。   - package_unavailable ：安装包失效。   - os_type_not_support ：系统类型错误。   - os_arch_not_support ：架构类型错误。

        :return: The install_result_code of this Host.
        :rtype: str
        """
        return self._install_result_code

    @install_result_code.setter
    def install_result_code(self, install_result_code):
        r"""Sets the install_result_code of this Host.

        安装结果，包含如下12种。   - install_succeed ：安装成功。   - network_access_timeout ：网络不通，访问超时。   - invalid_port ：无效端口。   - auth_failed ：认证错误，口令不正确。   - permission_denied ：权限错误，被拒绝。   - no_available_vpc ：没有相同VPC的agent在线虚拟机。   - install_exception ：安装异常。   - invalid_param ：参数错误。   - install_failed ：安装失败。   - package_unavailable ：安装包失效。   - os_type_not_support ：系统类型错误。   - os_arch_not_support ：架构类型错误。

        :param install_result_code: The install_result_code of this Host.
        :type install_result_code: str
        """
        self._install_result_code = install_result_code

    @property
    def version(self):
        r"""Gets the version of this Host.

        主机开通的版本，包含如下7种输入。   - hss.version.null ：无。   - hss.version.basic ：基础版。   - hss.version.advanced ：专业版。   - hss.version.enterprise ：企业版。   - hss.version.premium ：旗舰版。   - hss.version.wtp ：网页防篡改版。   - hss.version.container.enterprise ：容器版。

        :return: The version of this Host.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this Host.

        主机开通的版本，包含如下7种输入。   - hss.version.null ：无。   - hss.version.basic ：基础版。   - hss.version.advanced ：专业版。   - hss.version.enterprise ：企业版。   - hss.version.premium ：旗舰版。   - hss.version.wtp ：网页防篡改版。   - hss.version.container.enterprise ：容器版。

        :param version: The version of this Host.
        :type version: str
        """
        self._version = version

    @property
    def protect_status(self):
        r"""Gets the protect_status of this Host.

        防护状态，包含如下2种。 - closed ：未防护。 - opened ：防护中。 - protection_exception ：防护异常。

        :return: The protect_status of this Host.
        :rtype: str
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        r"""Sets the protect_status of this Host.

        防护状态，包含如下2种。 - closed ：未防护。 - opened ：防护中。 - protection_exception ：防护异常。

        :param protect_status: The protect_status of this Host.
        :type protect_status: str
        """
        self._protect_status = protect_status

    @property
    def os_image(self):
        r"""Gets the os_image of this Host.

        系统镜像

        :return: The os_image of this Host.
        :rtype: str
        """
        return self._os_image

    @os_image.setter
    def os_image(self, os_image):
        r"""Sets the os_image of this Host.

        系统镜像

        :param os_image: The os_image of this Host.
        :type os_image: str
        """
        self._os_image = os_image

    @property
    def os_type(self):
        r"""Gets the os_type of this Host.

        操作系统类型，包含如下2种。   - Linux ：Linux。   - Windows ：Windows。

        :return: The os_type of this Host.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this Host.

        操作系统类型，包含如下2种。   - Linux ：Linux。   - Windows ：Windows。

        :param os_type: The os_type of this Host.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def os_bit(self):
        r"""Gets the os_bit of this Host.

        操作系统位数

        :return: The os_bit of this Host.
        :rtype: str
        """
        return self._os_bit

    @os_bit.setter
    def os_bit(self, os_bit):
        r"""Sets the os_bit of this Host.

        操作系统位数

        :param os_bit: The os_bit of this Host.
        :type os_bit: str
        """
        self._os_bit = os_bit

    @property
    def detect_result(self):
        r"""Gets the detect_result of this Host.

        云主机安全检测结果，包含如下4种。 - undetected ：未检测。 - clean ：无风险。 - risk ：有风险。 - scanning ：检测中。

        :return: The detect_result of this Host.
        :rtype: str
        """
        return self._detect_result

    @detect_result.setter
    def detect_result(self, detect_result):
        r"""Sets the detect_result of this Host.

        云主机安全检测结果，包含如下4种。 - undetected ：未检测。 - clean ：无风险。 - risk ：有风险。 - scanning ：检测中。

        :param detect_result: The detect_result of this Host.
        :type detect_result: str
        """
        self._detect_result = detect_result

    @property
    def expire_time(self):
        r"""Gets the expire_time of this Host.

        试用版到期时间（-1表示非试用版配额，当值不为-1时为试用版本过期时间）

        :return: The expire_time of this Host.
        :rtype: int
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this Host.

        试用版到期时间（-1表示非试用版配额，当值不为-1时为试用版本过期时间）

        :param expire_time: The expire_time of this Host.
        :type expire_time: int
        """
        self._expire_time = expire_time

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this Host.

        收费模式，包含如下2种。   - packet_cycle ：包年/包月。   - on_demand ：按需。

        :return: The charging_mode of this Host.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this Host.

        收费模式，包含如下2种。   - packet_cycle ：包年/包月。   - on_demand ：按需。

        :param charging_mode: The charging_mode of this Host.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def resource_id(self):
        r"""Gets the resource_id of this Host.

        主机安全配额ID（UUID）

        :return: The resource_id of this Host.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this Host.

        主机安全配额ID（UUID）

        :param resource_id: The resource_id of this Host.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def outside_host(self):
        r"""Gets the outside_host of this Host.

        是否非华为云机器

        :return: The outside_host of this Host.
        :rtype: bool
        """
        return self._outside_host

    @outside_host.setter
    def outside_host(self, outside_host):
        r"""Sets the outside_host of this Host.

        是否非华为云机器

        :param outside_host: The outside_host of this Host.
        :type outside_host: bool
        """
        self._outside_host = outside_host

    @property
    def group_id(self):
        r"""Gets the group_id of this Host.

        服务器组ID

        :return: The group_id of this Host.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this Host.

        服务器组ID

        :param group_id: The group_id of this Host.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def group_name(self):
        r"""Gets the group_name of this Host.

        服务器组名称

        :return: The group_name of this Host.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this Host.

        服务器组名称

        :param group_name: The group_name of this Host.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def policy_group_id(self):
        r"""Gets the policy_group_id of this Host.

        策略组ID

        :return: The policy_group_id of this Host.
        :rtype: str
        """
        return self._policy_group_id

    @policy_group_id.setter
    def policy_group_id(self, policy_group_id):
        r"""Sets the policy_group_id of this Host.

        策略组ID

        :param policy_group_id: The policy_group_id of this Host.
        :type policy_group_id: str
        """
        self._policy_group_id = policy_group_id

    @property
    def policy_group_name(self):
        r"""Gets the policy_group_name of this Host.

        策略组名称

        :return: The policy_group_name of this Host.
        :rtype: str
        """
        return self._policy_group_name

    @policy_group_name.setter
    def policy_group_name(self, policy_group_name):
        r"""Sets the policy_group_name of this Host.

        策略组名称

        :param policy_group_name: The policy_group_name of this Host.
        :type policy_group_name: str
        """
        self._policy_group_name = policy_group_name

    @property
    def asset(self):
        r"""Gets the asset of this Host.

        资产风险

        :return: The asset of this Host.
        :rtype: int
        """
        return self._asset

    @asset.setter
    def asset(self, asset):
        r"""Sets the asset of this Host.

        资产风险

        :param asset: The asset of this Host.
        :type asset: int
        """
        self._asset = asset

    @property
    def vulnerability(self):
        r"""Gets the vulnerability of this Host.

        漏洞风险总数，包含Linux软件漏洞、Windows系统漏洞、Web-CMS漏洞、应用漏洞

        :return: The vulnerability of this Host.
        :rtype: int
        """
        return self._vulnerability

    @vulnerability.setter
    def vulnerability(self, vulnerability):
        r"""Sets the vulnerability of this Host.

        漏洞风险总数，包含Linux软件漏洞、Windows系统漏洞、Web-CMS漏洞、应用漏洞

        :param vulnerability: The vulnerability of this Host.
        :type vulnerability: int
        """
        self._vulnerability = vulnerability

    @property
    def baseline(self):
        r"""Gets the baseline of this Host.

        基线风险总数，包含配置风险、弱口令

        :return: The baseline of this Host.
        :rtype: int
        """
        return self._baseline

    @baseline.setter
    def baseline(self, baseline):
        r"""Sets the baseline of this Host.

        基线风险总数，包含配置风险、弱口令

        :param baseline: The baseline of this Host.
        :type baseline: int
        """
        self._baseline = baseline

    @property
    def intrusion(self):
        r"""Gets the intrusion of this Host.

        入侵风险总数

        :return: The intrusion of this Host.
        :rtype: int
        """
        return self._intrusion

    @intrusion.setter
    def intrusion(self, intrusion):
        r"""Sets the intrusion of this Host.

        入侵风险总数

        :param intrusion: The intrusion of this Host.
        :type intrusion: int
        """
        self._intrusion = intrusion

    @property
    def asset_value(self):
        r"""Gets the asset_value of this Host.

        资产重要性，包含如下4种   - important ：重要资产   - common ：一般资产   - test ：测试资产

        :return: The asset_value of this Host.
        :rtype: str
        """
        return self._asset_value

    @asset_value.setter
    def asset_value(self, asset_value):
        r"""Sets the asset_value of this Host.

        资产重要性，包含如下4种   - important ：重要资产   - common ：一般资产   - test ：测试资产

        :param asset_value: The asset_value of this Host.
        :type asset_value: str
        """
        self._asset_value = asset_value

    @property
    def labels(self):
        r"""Gets the labels of this Host.

        标签列表

        :return: The labels of this Host.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this Host.

        标签列表

        :param labels: The labels of this Host.
        :type labels: list[str]
        """
        self._labels = labels

    @property
    def agent_create_time(self):
        r"""Gets the agent_create_time of this Host.

        agent安装时间，采用时间戳，默认毫秒，

        :return: The agent_create_time of this Host.
        :rtype: int
        """
        return self._agent_create_time

    @agent_create_time.setter
    def agent_create_time(self, agent_create_time):
        r"""Sets the agent_create_time of this Host.

        agent安装时间，采用时间戳，默认毫秒，

        :param agent_create_time: The agent_create_time of this Host.
        :type agent_create_time: int
        """
        self._agent_create_time = agent_create_time

    @property
    def agent_update_time(self):
        r"""Gets the agent_update_time of this Host.

        agent状态修改时间，采用时间戳，默认毫秒，

        :return: The agent_update_time of this Host.
        :rtype: int
        """
        return self._agent_update_time

    @agent_update_time.setter
    def agent_update_time(self, agent_update_time):
        r"""Sets the agent_update_time of this Host.

        agent状态修改时间，采用时间戳，默认毫秒，

        :param agent_update_time: The agent_update_time of this Host.
        :type agent_update_time: int
        """
        self._agent_update_time = agent_update_time

    @property
    def agent_version(self):
        r"""Gets the agent_version of this Host.

        agent版本

        :return: The agent_version of this Host.
        :rtype: str
        """
        return self._agent_version

    @agent_version.setter
    def agent_version(self, agent_version):
        r"""Sets the agent_version of this Host.

        agent版本

        :param agent_version: The agent_version of this Host.
        :type agent_version: str
        """
        self._agent_version = agent_version

    @property
    def upgrade_status(self):
        r"""Gets the upgrade_status of this Host.

        升级状态，包含如下4种。   - not_upgrade ：未升级，也就是默认状态，客户还没有给这台机器下发过升级。   - upgrading ：正在升级中。   - upgrade_failed ：升级失败。   - upgrade_succeed ：升级成功。

        :return: The upgrade_status of this Host.
        :rtype: str
        """
        return self._upgrade_status

    @upgrade_status.setter
    def upgrade_status(self, upgrade_status):
        r"""Sets the upgrade_status of this Host.

        升级状态，包含如下4种。   - not_upgrade ：未升级，也就是默认状态，客户还没有给这台机器下发过升级。   - upgrading ：正在升级中。   - upgrade_failed ：升级失败。   - upgrade_succeed ：升级成功。

        :param upgrade_status: The upgrade_status of this Host.
        :type upgrade_status: str
        """
        self._upgrade_status = upgrade_status

    @property
    def upgrade_result_code(self):
        r"""Gets the upgrade_result_code of this Host.

        升级失败原因，只有当 upgrade_status 为 upgrade_failed 时才显示，包含如下6种。   - package_unavailable ：升级包解析失败，升级文件有错误。   - network_access_timeout ：下载升级包失败，网络异常。   - agent_offline ：agent离线。   - hostguard_abnormal ：agent工作进程异常。   - insufficient_disk_space ：磁盘空间不足。   - failed_to_replace_file ：替换文件失败。

        :return: The upgrade_result_code of this Host.
        :rtype: str
        """
        return self._upgrade_result_code

    @upgrade_result_code.setter
    def upgrade_result_code(self, upgrade_result_code):
        r"""Sets the upgrade_result_code of this Host.

        升级失败原因，只有当 upgrade_status 为 upgrade_failed 时才显示，包含如下6种。   - package_unavailable ：升级包解析失败，升级文件有错误。   - network_access_timeout ：下载升级包失败，网络异常。   - agent_offline ：agent离线。   - hostguard_abnormal ：agent工作进程异常。   - insufficient_disk_space ：磁盘空间不足。   - failed_to_replace_file ：替换文件失败。

        :param upgrade_result_code: The upgrade_result_code of this Host.
        :type upgrade_result_code: str
        """
        self._upgrade_result_code = upgrade_result_code

    @property
    def upgradable(self):
        r"""Gets the upgradable of this Host.

        该服务器agent是否可升级

        :return: The upgradable of this Host.
        :rtype: bool
        """
        return self._upgradable

    @upgradable.setter
    def upgradable(self, upgradable):
        r"""Sets the upgradable of this Host.

        该服务器agent是否可升级

        :param upgradable: The upgradable of this Host.
        :type upgradable: bool
        """
        self._upgradable = upgradable

    @property
    def open_time(self):
        r"""Gets the open_time of this Host.

        开启防护时间，采用时间戳，默认毫秒，

        :return: The open_time of this Host.
        :rtype: int
        """
        return self._open_time

    @open_time.setter
    def open_time(self, open_time):
        r"""Sets the open_time of this Host.

        开启防护时间，采用时间戳，默认毫秒，

        :param open_time: The open_time of this Host.
        :type open_time: int
        """
        self._open_time = open_time

    @property
    def protect_interrupt(self):
        r"""Gets the protect_interrupt of this Host.

        防护是否中断

        :return: The protect_interrupt of this Host.
        :rtype: bool
        """
        return self._protect_interrupt

    @protect_interrupt.setter
    def protect_interrupt(self, protect_interrupt):
        r"""Sets the protect_interrupt of this Host.

        防护是否中断

        :param protect_interrupt: The protect_interrupt of this Host.
        :type protect_interrupt: bool
        """
        self._protect_interrupt = protect_interrupt

    @property
    def protect_degradation(self):
        r"""Gets the protect_degradation of this Host.

        防护是否降级

        :return: The protect_degradation of this Host.
        :rtype: bool
        """
        return self._protect_degradation

    @protect_degradation.setter
    def protect_degradation(self, protect_degradation):
        r"""Sets the protect_degradation of this Host.

        防护是否降级

        :param protect_degradation: The protect_degradation of this Host.
        :type protect_degradation: bool
        """
        self._protect_degradation = protect_degradation

    @property
    def host_sources(self):
        r"""Gets the host_sources of this Host.

        服务器来源

        :return: The host_sources of this Host.
        :rtype: str
        """
        return self._host_sources

    @host_sources.setter
    def host_sources(self, host_sources):
        r"""Sets the host_sources of this Host.

        服务器来源

        :param host_sources: The host_sources of this Host.
        :type host_sources: str
        """
        self._host_sources = host_sources

    @property
    def interrupt_reason(self):
        r"""Gets the interrupt_reason of this Host.

        防护中断原因

        :return: The interrupt_reason of this Host.
        :rtype: str
        """
        return self._interrupt_reason

    @interrupt_reason.setter
    def interrupt_reason(self, interrupt_reason):
        r"""Sets the interrupt_reason of this Host.

        防护中断原因

        :param interrupt_reason: The interrupt_reason of this Host.
        :type interrupt_reason: str
        """
        self._interrupt_reason = interrupt_reason

    @property
    def degradation_reason(self):
        r"""Gets the degradation_reason of this Host.

        防护降级原因

        :return: The degradation_reason of this Host.
        :rtype: str
        """
        return self._degradation_reason

    @degradation_reason.setter
    def degradation_reason(self, degradation_reason):
        r"""Sets the degradation_reason of this Host.

        防护降级原因

        :param degradation_reason: The degradation_reason of this Host.
        :type degradation_reason: str
        """
        self._degradation_reason = degradation_reason

    @property
    def key_name(self):
        r"""Gets the key_name of this Host.

        使用的密钥对名称

        :return: The key_name of this Host.
        :rtype: str
        """
        return self._key_name

    @key_name.setter
    def key_name(self, key_name):
        r"""Sets the key_name of this Host.

        使用的密钥对名称

        :param key_name: The key_name of this Host.
        :type key_name: str
        """
        self._key_name = key_name

    @property
    def auto_open_version(self):
        r"""Gets the auto_open_version of this Host.

        cce购买主机

        :return: The auto_open_version of this Host.
        :rtype: str
        """
        return self._auto_open_version

    @auto_open_version.setter
    def auto_open_version(self, auto_open_version):
        r"""Sets the auto_open_version of this Host.

        cce购买主机

        :param auto_open_version: The auto_open_version of this Host.
        :type auto_open_version: str
        """
        self._auto_open_version = auto_open_version

    @property
    def install_progress(self):
        r"""Gets the install_progress of this Host.

        安装进度

        :return: The install_progress of this Host.
        :rtype: int
        """
        return self._install_progress

    @install_progress.setter
    def install_progress(self, install_progress):
        r"""Sets the install_progress of this Host.

        安装进度

        :param install_progress: The install_progress of this Host.
        :type install_progress: int
        """
        self._install_progress = install_progress

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this Host.

        vpc id

        :return: The vpc_id of this Host.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this Host.

        vpc id

        :param vpc_id: The vpc_id of this Host.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def common_login_area_codes(self):
        r"""Gets the common_login_area_codes of this Host.

        后台识别服务器常用登录地编号

        :return: The common_login_area_codes of this Host.
        :rtype: list[int]
        """
        return self._common_login_area_codes

    @common_login_area_codes.setter
    def common_login_area_codes(self, common_login_area_codes):
        r"""Sets the common_login_area_codes of this Host.

        后台识别服务器常用登录地编号

        :param common_login_area_codes: The common_login_area_codes of this Host.
        :type common_login_area_codes: list[int]
        """
        self._common_login_area_codes = common_login_area_codes

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this Host.

        集群名称

        :return: The cluster_name of this Host.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this Host.

        集群名称

        :param cluster_name: The cluster_name of this Host.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this Host.

        集群id

        :return: The cluster_id of this Host.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this Host.

        集群id

        :param cluster_id: The cluster_id of this Host.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

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
        if not isinstance(other, Host):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
