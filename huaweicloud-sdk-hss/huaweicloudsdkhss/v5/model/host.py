# coding: utf-8

import re
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
        'host_status': 'str',
        'agent_status': 'str',
        'install_result_code': 'str',
        'version': 'str',
        'protect_status': 'str',
        'os_image': 'str',
        'os_type': 'str',
        'os_bit': 'str',
        'detect_result': 'str',
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
        'upgradable': 'bool'
    }

    attribute_map = {
        'host_name': 'host_name',
        'host_id': 'host_id',
        'agent_id': 'agent_id',
        'private_ip': 'private_ip',
        'public_ip': 'public_ip',
        'enterprise_project_id': 'enterprise_project_id',
        'enterprise_project_name': 'enterprise_project_name',
        'host_status': 'host_status',
        'agent_status': 'agent_status',
        'install_result_code': 'install_result_code',
        'version': 'version',
        'protect_status': 'protect_status',
        'os_image': 'os_image',
        'os_type': 'os_type',
        'os_bit': 'os_bit',
        'detect_result': 'detect_result',
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
        'upgradable': 'upgradable'
    }

    def __init__(self, host_name=None, host_id=None, agent_id=None, private_ip=None, public_ip=None, enterprise_project_id=None, enterprise_project_name=None, host_status=None, agent_status=None, install_result_code=None, version=None, protect_status=None, os_image=None, os_type=None, os_bit=None, detect_result=None, charging_mode=None, resource_id=None, outside_host=None, group_id=None, group_name=None, policy_group_id=None, policy_group_name=None, asset=None, vulnerability=None, baseline=None, intrusion=None, asset_value=None, labels=None, agent_create_time=None, agent_update_time=None, agent_version=None, upgrade_status=None, upgrade_result_code=None, upgradable=None):
        """Host

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
        :param host_status: 服务器状态，包含如下4种。   - ACTIVE ：运行中。   - SHUTOFF ：关机。   - BUILDING ：创建中。   - ERROR ：故障。
        :type host_status: str
        :param agent_status: Agent状态，包含如下5种。   - installed ：已安装。   - not_installed ：未安装。   - online ：在线。   - offline ：离线。   - install_failed ：安装失败。   - installing ：安装中。
        :type agent_status: str
        :param install_result_code: 安装结果，包含如下12种。   - install_succeed ：安装成功。   - network_access_timeout ：网络不通，访问超时。   - invalid_port ：无效端口。   - auth_failed ：认证错误，口令不正确。   - permission_denied ：权限错误，被拒绝。   - no_available_vpc ：没有相同VPC的agent在线虚拟机。   - install_exception ：安装异常。   - invalid_param ：参数错误。   - install_failed ：安装失败。   - package_unavailable ：安装包失效。   - os_type_not_support ：系统类型错误。   - os_arch_not_support ：架构类型错误。
        :type install_result_code: str
        :param version: 主机开通的版本，包含如下6种输入。   - hss.version.null ：无。   - hss.version.basic ：基础版。   - hss.version.enterprise ：企业版。   - hss.version.premium ：旗舰版。   - hss.version.wtp ：网页防篡改版。   - hss.version.container.enterprise ：容器版。
        :type version: str
        :param protect_status: 防护状态，包含如下2种。 - closed ：未防护。 - opened ：防护中。
        :type protect_status: str
        :param os_image: 系统镜像
        :type os_image: str
        :param os_type: 操作系统类型，包含如下2种。   - Linux ：Linux。   - Windows ：Windows。
        :type os_type: str
        :param os_bit: 操作系统位数
        :type os_bit: str
        :param detect_result: 云主机安全检测结果，包含如下4种。 - undetected ：未检测。 - clean ：无风险。 - risk ：有风险。 - scanning ：检测中。
        :type detect_result: str
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
        :param vulnerability: 漏洞风险
        :type vulnerability: int
        :param baseline: 基线风险
        :type baseline: int
        :param intrusion: 入侵风险
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
        :param upgrade_result_code: 升级失败原因，只有当 upgrade_status 为 upgrade_failed 时才显示，包含如下12种。   - package_unavailable ：升级包解析失败，升级文件有错误。   - network_access_timeout ：下载升级包失败，网络异常。   - agent_offline ：agent离线。   - hostguard_abnormal ：agent工作进程异常。   - insufficient_disk_space ：磁盘空间不足。   - failed_to_replace_file ：替换文件失败。
        :type upgrade_result_code: str
        :param upgradable: 该服务器agent是否可升级
        :type upgradable: bool
        """
        
        

        self._host_name = None
        self._host_id = None
        self._agent_id = None
        self._private_ip = None
        self._public_ip = None
        self._enterprise_project_id = None
        self._enterprise_project_name = None
        self._host_status = None
        self._agent_status = None
        self._install_result_code = None
        self._version = None
        self._protect_status = None
        self._os_image = None
        self._os_type = None
        self._os_bit = None
        self._detect_result = None
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

    @property
    def host_name(self):
        """Gets the host_name of this Host.

        服务器名称

        :return: The host_name of this Host.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this Host.

        服务器名称

        :param host_name: The host_name of this Host.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_id(self):
        """Gets the host_id of this Host.

        服务器ID

        :return: The host_id of this Host.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this Host.

        服务器ID

        :param host_id: The host_id of this Host.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def agent_id(self):
        """Gets the agent_id of this Host.

        Agent ID

        :return: The agent_id of this Host.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """Sets the agent_id of this Host.

        Agent ID

        :param agent_id: The agent_id of this Host.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def private_ip(self):
        """Gets the private_ip of this Host.

        私有IP地址

        :return: The private_ip of this Host.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """Sets the private_ip of this Host.

        私有IP地址

        :param private_ip: The private_ip of this Host.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def public_ip(self):
        """Gets the public_ip of this Host.

        弹性公网IP地址

        :return: The public_ip of this Host.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """Sets the public_ip of this Host.

        弹性公网IP地址

        :param public_ip: The public_ip of this Host.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this Host.

        企业项目ID

        :return: The enterprise_project_id of this Host.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this Host.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this Host.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def enterprise_project_name(self):
        """Gets the enterprise_project_name of this Host.

        所属企业项目名称

        :return: The enterprise_project_name of this Host.
        :rtype: str
        """
        return self._enterprise_project_name

    @enterprise_project_name.setter
    def enterprise_project_name(self, enterprise_project_name):
        """Sets the enterprise_project_name of this Host.

        所属企业项目名称

        :param enterprise_project_name: The enterprise_project_name of this Host.
        :type enterprise_project_name: str
        """
        self._enterprise_project_name = enterprise_project_name

    @property
    def host_status(self):
        """Gets the host_status of this Host.

        服务器状态，包含如下4种。   - ACTIVE ：运行中。   - SHUTOFF ：关机。   - BUILDING ：创建中。   - ERROR ：故障。

        :return: The host_status of this Host.
        :rtype: str
        """
        return self._host_status

    @host_status.setter
    def host_status(self, host_status):
        """Sets the host_status of this Host.

        服务器状态，包含如下4种。   - ACTIVE ：运行中。   - SHUTOFF ：关机。   - BUILDING ：创建中。   - ERROR ：故障。

        :param host_status: The host_status of this Host.
        :type host_status: str
        """
        self._host_status = host_status

    @property
    def agent_status(self):
        """Gets the agent_status of this Host.

        Agent状态，包含如下5种。   - installed ：已安装。   - not_installed ：未安装。   - online ：在线。   - offline ：离线。   - install_failed ：安装失败。   - installing ：安装中。

        :return: The agent_status of this Host.
        :rtype: str
        """
        return self._agent_status

    @agent_status.setter
    def agent_status(self, agent_status):
        """Sets the agent_status of this Host.

        Agent状态，包含如下5种。   - installed ：已安装。   - not_installed ：未安装。   - online ：在线。   - offline ：离线。   - install_failed ：安装失败。   - installing ：安装中。

        :param agent_status: The agent_status of this Host.
        :type agent_status: str
        """
        self._agent_status = agent_status

    @property
    def install_result_code(self):
        """Gets the install_result_code of this Host.

        安装结果，包含如下12种。   - install_succeed ：安装成功。   - network_access_timeout ：网络不通，访问超时。   - invalid_port ：无效端口。   - auth_failed ：认证错误，口令不正确。   - permission_denied ：权限错误，被拒绝。   - no_available_vpc ：没有相同VPC的agent在线虚拟机。   - install_exception ：安装异常。   - invalid_param ：参数错误。   - install_failed ：安装失败。   - package_unavailable ：安装包失效。   - os_type_not_support ：系统类型错误。   - os_arch_not_support ：架构类型错误。

        :return: The install_result_code of this Host.
        :rtype: str
        """
        return self._install_result_code

    @install_result_code.setter
    def install_result_code(self, install_result_code):
        """Sets the install_result_code of this Host.

        安装结果，包含如下12种。   - install_succeed ：安装成功。   - network_access_timeout ：网络不通，访问超时。   - invalid_port ：无效端口。   - auth_failed ：认证错误，口令不正确。   - permission_denied ：权限错误，被拒绝。   - no_available_vpc ：没有相同VPC的agent在线虚拟机。   - install_exception ：安装异常。   - invalid_param ：参数错误。   - install_failed ：安装失败。   - package_unavailable ：安装包失效。   - os_type_not_support ：系统类型错误。   - os_arch_not_support ：架构类型错误。

        :param install_result_code: The install_result_code of this Host.
        :type install_result_code: str
        """
        self._install_result_code = install_result_code

    @property
    def version(self):
        """Gets the version of this Host.

        主机开通的版本，包含如下6种输入。   - hss.version.null ：无。   - hss.version.basic ：基础版。   - hss.version.enterprise ：企业版。   - hss.version.premium ：旗舰版。   - hss.version.wtp ：网页防篡改版。   - hss.version.container.enterprise ：容器版。

        :return: The version of this Host.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Host.

        主机开通的版本，包含如下6种输入。   - hss.version.null ：无。   - hss.version.basic ：基础版。   - hss.version.enterprise ：企业版。   - hss.version.premium ：旗舰版。   - hss.version.wtp ：网页防篡改版。   - hss.version.container.enterprise ：容器版。

        :param version: The version of this Host.
        :type version: str
        """
        self._version = version

    @property
    def protect_status(self):
        """Gets the protect_status of this Host.

        防护状态，包含如下2种。 - closed ：未防护。 - opened ：防护中。

        :return: The protect_status of this Host.
        :rtype: str
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        """Sets the protect_status of this Host.

        防护状态，包含如下2种。 - closed ：未防护。 - opened ：防护中。

        :param protect_status: The protect_status of this Host.
        :type protect_status: str
        """
        self._protect_status = protect_status

    @property
    def os_image(self):
        """Gets the os_image of this Host.

        系统镜像

        :return: The os_image of this Host.
        :rtype: str
        """
        return self._os_image

    @os_image.setter
    def os_image(self, os_image):
        """Sets the os_image of this Host.

        系统镜像

        :param os_image: The os_image of this Host.
        :type os_image: str
        """
        self._os_image = os_image

    @property
    def os_type(self):
        """Gets the os_type of this Host.

        操作系统类型，包含如下2种。   - Linux ：Linux。   - Windows ：Windows。

        :return: The os_type of this Host.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this Host.

        操作系统类型，包含如下2种。   - Linux ：Linux。   - Windows ：Windows。

        :param os_type: The os_type of this Host.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def os_bit(self):
        """Gets the os_bit of this Host.

        操作系统位数

        :return: The os_bit of this Host.
        :rtype: str
        """
        return self._os_bit

    @os_bit.setter
    def os_bit(self, os_bit):
        """Sets the os_bit of this Host.

        操作系统位数

        :param os_bit: The os_bit of this Host.
        :type os_bit: str
        """
        self._os_bit = os_bit

    @property
    def detect_result(self):
        """Gets the detect_result of this Host.

        云主机安全检测结果，包含如下4种。 - undetected ：未检测。 - clean ：无风险。 - risk ：有风险。 - scanning ：检测中。

        :return: The detect_result of this Host.
        :rtype: str
        """
        return self._detect_result

    @detect_result.setter
    def detect_result(self, detect_result):
        """Sets the detect_result of this Host.

        云主机安全检测结果，包含如下4种。 - undetected ：未检测。 - clean ：无风险。 - risk ：有风险。 - scanning ：检测中。

        :param detect_result: The detect_result of this Host.
        :type detect_result: str
        """
        self._detect_result = detect_result

    @property
    def charging_mode(self):
        """Gets the charging_mode of this Host.

        收费模式，包含如下2种。   - packet_cycle ：包年/包月。   - on_demand ：按需。

        :return: The charging_mode of this Host.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        """Sets the charging_mode of this Host.

        收费模式，包含如下2种。   - packet_cycle ：包年/包月。   - on_demand ：按需。

        :param charging_mode: The charging_mode of this Host.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def resource_id(self):
        """Gets the resource_id of this Host.

        主机安全配额ID（UUID）

        :return: The resource_id of this Host.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this Host.

        主机安全配额ID（UUID）

        :param resource_id: The resource_id of this Host.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def outside_host(self):
        """Gets the outside_host of this Host.

        是否非华为云机器

        :return: The outside_host of this Host.
        :rtype: bool
        """
        return self._outside_host

    @outside_host.setter
    def outside_host(self, outside_host):
        """Sets the outside_host of this Host.

        是否非华为云机器

        :param outside_host: The outside_host of this Host.
        :type outside_host: bool
        """
        self._outside_host = outside_host

    @property
    def group_id(self):
        """Gets the group_id of this Host.

        服务器组ID

        :return: The group_id of this Host.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this Host.

        服务器组ID

        :param group_id: The group_id of this Host.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def group_name(self):
        """Gets the group_name of this Host.

        服务器组名称

        :return: The group_name of this Host.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this Host.

        服务器组名称

        :param group_name: The group_name of this Host.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def policy_group_id(self):
        """Gets the policy_group_id of this Host.

        策略组ID

        :return: The policy_group_id of this Host.
        :rtype: str
        """
        return self._policy_group_id

    @policy_group_id.setter
    def policy_group_id(self, policy_group_id):
        """Sets the policy_group_id of this Host.

        策略组ID

        :param policy_group_id: The policy_group_id of this Host.
        :type policy_group_id: str
        """
        self._policy_group_id = policy_group_id

    @property
    def policy_group_name(self):
        """Gets the policy_group_name of this Host.

        策略组名称

        :return: The policy_group_name of this Host.
        :rtype: str
        """
        return self._policy_group_name

    @policy_group_name.setter
    def policy_group_name(self, policy_group_name):
        """Sets the policy_group_name of this Host.

        策略组名称

        :param policy_group_name: The policy_group_name of this Host.
        :type policy_group_name: str
        """
        self._policy_group_name = policy_group_name

    @property
    def asset(self):
        """Gets the asset of this Host.

        资产风险

        :return: The asset of this Host.
        :rtype: int
        """
        return self._asset

    @asset.setter
    def asset(self, asset):
        """Sets the asset of this Host.

        资产风险

        :param asset: The asset of this Host.
        :type asset: int
        """
        self._asset = asset

    @property
    def vulnerability(self):
        """Gets the vulnerability of this Host.

        漏洞风险

        :return: The vulnerability of this Host.
        :rtype: int
        """
        return self._vulnerability

    @vulnerability.setter
    def vulnerability(self, vulnerability):
        """Sets the vulnerability of this Host.

        漏洞风险

        :param vulnerability: The vulnerability of this Host.
        :type vulnerability: int
        """
        self._vulnerability = vulnerability

    @property
    def baseline(self):
        """Gets the baseline of this Host.

        基线风险

        :return: The baseline of this Host.
        :rtype: int
        """
        return self._baseline

    @baseline.setter
    def baseline(self, baseline):
        """Sets the baseline of this Host.

        基线风险

        :param baseline: The baseline of this Host.
        :type baseline: int
        """
        self._baseline = baseline

    @property
    def intrusion(self):
        """Gets the intrusion of this Host.

        入侵风险

        :return: The intrusion of this Host.
        :rtype: int
        """
        return self._intrusion

    @intrusion.setter
    def intrusion(self, intrusion):
        """Sets the intrusion of this Host.

        入侵风险

        :param intrusion: The intrusion of this Host.
        :type intrusion: int
        """
        self._intrusion = intrusion

    @property
    def asset_value(self):
        """Gets the asset_value of this Host.

        资产重要性，包含如下4种   - important ：重要资产   - common ：一般资产   - test ：测试资产

        :return: The asset_value of this Host.
        :rtype: str
        """
        return self._asset_value

    @asset_value.setter
    def asset_value(self, asset_value):
        """Sets the asset_value of this Host.

        资产重要性，包含如下4种   - important ：重要资产   - common ：一般资产   - test ：测试资产

        :param asset_value: The asset_value of this Host.
        :type asset_value: str
        """
        self._asset_value = asset_value

    @property
    def labels(self):
        """Gets the labels of this Host.

        标签列表

        :return: The labels of this Host.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this Host.

        标签列表

        :param labels: The labels of this Host.
        :type labels: list[str]
        """
        self._labels = labels

    @property
    def agent_create_time(self):
        """Gets the agent_create_time of this Host.

        agent安装时间，采用时间戳，默认毫秒，

        :return: The agent_create_time of this Host.
        :rtype: int
        """
        return self._agent_create_time

    @agent_create_time.setter
    def agent_create_time(self, agent_create_time):
        """Sets the agent_create_time of this Host.

        agent安装时间，采用时间戳，默认毫秒，

        :param agent_create_time: The agent_create_time of this Host.
        :type agent_create_time: int
        """
        self._agent_create_time = agent_create_time

    @property
    def agent_update_time(self):
        """Gets the agent_update_time of this Host.

        agent状态修改时间，采用时间戳，默认毫秒，

        :return: The agent_update_time of this Host.
        :rtype: int
        """
        return self._agent_update_time

    @agent_update_time.setter
    def agent_update_time(self, agent_update_time):
        """Sets the agent_update_time of this Host.

        agent状态修改时间，采用时间戳，默认毫秒，

        :param agent_update_time: The agent_update_time of this Host.
        :type agent_update_time: int
        """
        self._agent_update_time = agent_update_time

    @property
    def agent_version(self):
        """Gets the agent_version of this Host.

        agent版本

        :return: The agent_version of this Host.
        :rtype: str
        """
        return self._agent_version

    @agent_version.setter
    def agent_version(self, agent_version):
        """Sets the agent_version of this Host.

        agent版本

        :param agent_version: The agent_version of this Host.
        :type agent_version: str
        """
        self._agent_version = agent_version

    @property
    def upgrade_status(self):
        """Gets the upgrade_status of this Host.

        升级状态，包含如下4种。   - not_upgrade ：未升级，也就是默认状态，客户还没有给这台机器下发过升级。   - upgrading ：正在升级中。   - upgrade_failed ：升级失败。   - upgrade_succeed ：升级成功。

        :return: The upgrade_status of this Host.
        :rtype: str
        """
        return self._upgrade_status

    @upgrade_status.setter
    def upgrade_status(self, upgrade_status):
        """Sets the upgrade_status of this Host.

        升级状态，包含如下4种。   - not_upgrade ：未升级，也就是默认状态，客户还没有给这台机器下发过升级。   - upgrading ：正在升级中。   - upgrade_failed ：升级失败。   - upgrade_succeed ：升级成功。

        :param upgrade_status: The upgrade_status of this Host.
        :type upgrade_status: str
        """
        self._upgrade_status = upgrade_status

    @property
    def upgrade_result_code(self):
        """Gets the upgrade_result_code of this Host.

        升级失败原因，只有当 upgrade_status 为 upgrade_failed 时才显示，包含如下12种。   - package_unavailable ：升级包解析失败，升级文件有错误。   - network_access_timeout ：下载升级包失败，网络异常。   - agent_offline ：agent离线。   - hostguard_abnormal ：agent工作进程异常。   - insufficient_disk_space ：磁盘空间不足。   - failed_to_replace_file ：替换文件失败。

        :return: The upgrade_result_code of this Host.
        :rtype: str
        """
        return self._upgrade_result_code

    @upgrade_result_code.setter
    def upgrade_result_code(self, upgrade_result_code):
        """Sets the upgrade_result_code of this Host.

        升级失败原因，只有当 upgrade_status 为 upgrade_failed 时才显示，包含如下12种。   - package_unavailable ：升级包解析失败，升级文件有错误。   - network_access_timeout ：下载升级包失败，网络异常。   - agent_offline ：agent离线。   - hostguard_abnormal ：agent工作进程异常。   - insufficient_disk_space ：磁盘空间不足。   - failed_to_replace_file ：替换文件失败。

        :param upgrade_result_code: The upgrade_result_code of this Host.
        :type upgrade_result_code: str
        """
        self._upgrade_result_code = upgrade_result_code

    @property
    def upgradable(self):
        """Gets the upgradable of this Host.

        该服务器agent是否可升级

        :return: The upgradable of this Host.
        :rtype: bool
        """
        return self._upgradable

    @upgradable.setter
    def upgradable(self, upgradable):
        """Sets the upgradable of this Host.

        该服务器agent是否可升级

        :param upgradable: The upgradable of this Host.
        :type upgradable: bool
        """
        self._upgradable = upgradable

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
