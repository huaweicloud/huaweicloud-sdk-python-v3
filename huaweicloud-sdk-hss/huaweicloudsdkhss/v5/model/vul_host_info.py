# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VulHostInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_id': 'str',
        'agent_id': 'str',
        'repair_necessity': 'str',
        'severity_level': 'str',
        'host_name': 'str',
        'host_ip': 'str',
        'cve_num': 'int',
        'cve_id_list': 'list[str]',
        'status': 'str',
        'remark': 'str',
        'repair_cmd': 'str',
        'version': 'str',
        'app_path': 'str',
        'is_affect_business': 'bool',
        'asset_value': 'str',
        'private_ip': 'str',
        'group_name': 'str',
        'group_id': 'str',
        'os_type': 'str',
        'os_name': 'str',
        'os_version': 'str',
        'os_kernel': 'str',
        'host_status': 'str',
        'first_scan_time': 'int',
        'scan_time': 'int',
        'failed_reason': 'str',
        'support_restore': 'bool',
        'backup_name': 'str',
        'agent_status': 'str',
        'disabled_operate_types': 'list[HostVulInfoDisabledOperateTypes]',
        'repair_priority': 'str'
    }

    attribute_map = {
        'host_id': 'host_id',
        'agent_id': 'agent_id',
        'repair_necessity': 'repair_necessity',
        'severity_level': 'severity_level',
        'host_name': 'host_name',
        'host_ip': 'host_ip',
        'cve_num': 'cve_num',
        'cve_id_list': 'cve_id_list',
        'status': 'status',
        'remark': 'remark',
        'repair_cmd': 'repair_cmd',
        'version': 'version',
        'app_path': 'app_path',
        'is_affect_business': 'is_affect_business',
        'asset_value': 'asset_value',
        'private_ip': 'private_ip',
        'group_name': 'group_name',
        'group_id': 'group_id',
        'os_type': 'os_type',
        'os_name': 'os_name',
        'os_version': 'os_version',
        'os_kernel': 'os_kernel',
        'host_status': 'host_status',
        'first_scan_time': 'first_scan_time',
        'scan_time': 'scan_time',
        'failed_reason': 'failed_reason',
        'support_restore': 'support_restore',
        'backup_name': 'backup_name',
        'agent_status': 'agent_status',
        'disabled_operate_types': 'disabled_operate_types',
        'repair_priority': 'repair_priority'
    }

    def __init__(self, host_id=None, agent_id=None, repair_necessity=None, severity_level=None, host_name=None, host_ip=None, cve_num=None, cve_id_list=None, status=None, remark=None, repair_cmd=None, version=None, app_path=None, is_affect_business=None, asset_value=None, private_ip=None, group_name=None, group_id=None, os_type=None, os_name=None, os_version=None, os_kernel=None, host_status=None, first_scan_time=None, scan_time=None, failed_reason=None, support_restore=None, backup_name=None, agent_status=None, disabled_operate_types=None, repair_priority=None):
        r"""VulHostInfo

        The model defined in huaweicloud sdk

        :param host_id: **参数解释**: 受漏洞影响的服务器id **取值范围**: 字符范围1-128位 
        :type host_id: str
        :param agent_id: **参数解释**: 主机对应的agent id **取值范围**: 字符范围1-128位 
        :type agent_id: str
        :param repair_necessity: **参数解释**: 修复紧急度 **取值范围**: - Critical：漏洞cvss评分大于等于9；对应控制台页面的高危 - High：漏洞cvss评分大于等于7，小于9；对应控制台页面的中危 - Medium：漏洞cvss评分大于等于4，小于7；对应控制台页面的中危 - Low：漏洞cvss评分小于4；对应控制台页面的低危 
        :type repair_necessity: str
        :param severity_level: **参数解释**: 危险程度 **取值范围**: - Critical：漏洞cvss评分大于等于9；对应控制台页面的高危 - High：漏洞cvss评分大于等于7，小于9；对应控制台页面的中危 - Medium：漏洞cvss评分大于等于4，小于7；对应控制台页面的中危 - Low：漏洞cvss评分小于4；对应控制台页面的低危 
        :type severity_level: str
        :param host_name: **参数解释**: 受影响主机名称 **取值范围**: 字符范围1-256位 
        :type host_name: str
        :param host_ip: **参数解释**: 受影响主机ip **取值范围**: 字符范围1-256位 
        :type host_ip: str
        :param cve_num: **参数解释**: 漏洞cve总数 **取值范围**: 最小值0，最大值10000 
        :type cve_num: int
        :param cve_id_list: **参数解释**: 漏洞对应的cve id列表 **取值范围**: 最小值1，最大值10000 
        :type cve_id_list: list[str]
        :param status: **参数解释**: 漏洞状态 **取值范围**: - vul_status_unfix：未处理 - vul_status_ignored：已忽略 - vul_status_verified：验证中 - vul_status_fixing：修复中 - vul_status_fixed：修复成功 - vul_status_reboot：修复成功待重启 - vul_status_failed：修复失败 - vul_status_fix_after_reboot：请重启主机再次修复 
        :type status: str
        :param remark: **参数解释**: 处置备注 **取值范围**: 字符长度1-65535位 
        :type remark: str
        :param repair_cmd: **参数解释**: 修复漏洞需要执行的命令行（只有Linux漏洞有该字段） **取值范围**: 字符范围1-256位 
        :type repair_cmd: str
        :param version: **参数解释**: 主机绑定的配额版本 **取值范围**: 字符范围1-128位 
        :type version: str
        :param app_path: **参数解释**: 应用软件的路径（只有应用漏洞有该字段） **取值范围**: 字符范围1-512位 
        :type app_path: str
        :param is_affect_business: **参数解释**: 是否影响业务 **取值范围**: - true  : 影响业务 - false : 不影响业务 
        :type is_affect_business: bool
        :param asset_value: **参数解释**: 资产重要性 **取值范围**: - important : 重要资产 - common    : 一般资产 - test      : 测试资产 
        :type asset_value: str
        :param private_ip: **参数解释**: 服务器私网ip **取值范围**: 字符范围0-128位 
        :type private_ip: str
        :param group_name: **参数解释**: 服务器组名称 **取值范围**: 字符范围0-256位 
        :type group_name: str
        :param group_id: **参数解释**: 服务器组id **取值范围**: 字符范围0-128位 
        :type group_id: str
        :param os_type: **参数解释**: 操作系统类型 **取值范围**: - Linux ：linux系统 - Windows：windows系统 
        :type os_type: str
        :param os_name: **参数解释**: 操作系统名称 **取值范围**: 字符长度1-256位 
        :type os_name: str
        :param os_version: **参数解释**: 操作系统版本 **取值范围**: 字符长度1-255位 
        :type os_version: str
        :param os_kernel: **参数解释**: 操作系统内核 **取值范围**: 字符长度1-64位 
        :type os_kernel: str
        :param host_status: **参数解释**: 主机状态 **取值范围**: - ACTIVE：正在运行。 - SHUTOFF：关机。 - BUILDING：创建中。 - ERROR：故障。 **默认取值**: 不涉及 
        :type host_status: str
        :param first_scan_time: **参数解释**: 首次扫描时间 **取值范围**: 最小值0，最大值9223372036854775807 
        :type first_scan_time: int
        :param scan_time: **参数解释**: 扫描时间，时间戳单位：毫秒 **取值范围**: 最小值0，最大值9223372036854775807 
        :type scan_time: int
        :param failed_reason: **参数解释**: 修复失败原因 **取值范围**: 字符长度1-65535位 
        :type failed_reason: str
        :param support_restore: **参数解释**: 是否可以回滚到修复漏洞时创建的备份 **取值范围**: - true  : 可以回滚 - false : 不可以回滚 
        :type support_restore: bool
        :param backup_name: **参数解释**: 备份名称 **取值范围**: 字符长度1-2048位 
        :type backup_name: str
        :param agent_status: **参数解释**: Agent状态 **取值范围**: - installed：已安装。 - not_installed：未安装。 - online：在线。 - offline：离线。 - install_failed：安装失败。 - installing：安装中。
        :type agent_status: str
        :param disabled_operate_types: **参数解释**: 漏洞在当前主机上不可进行的操作类型列表 **取值范围**: 最小值1，最大值10000 
        :type disabled_operate_types: list[:class:`huaweicloudsdkhss.v5.HostVulInfoDisabledOperateTypes`]
        :param repair_priority: **参数解释**: 修复优先级 **取值范围**: - Critical : 紧急 - High     : 高 - Medium   : 中 - Low      : 低 
        :type repair_priority: str
        """
        
        

        self._host_id = None
        self._agent_id = None
        self._repair_necessity = None
        self._severity_level = None
        self._host_name = None
        self._host_ip = None
        self._cve_num = None
        self._cve_id_list = None
        self._status = None
        self._remark = None
        self._repair_cmd = None
        self._version = None
        self._app_path = None
        self._is_affect_business = None
        self._asset_value = None
        self._private_ip = None
        self._group_name = None
        self._group_id = None
        self._os_type = None
        self._os_name = None
        self._os_version = None
        self._os_kernel = None
        self._host_status = None
        self._first_scan_time = None
        self._scan_time = None
        self._failed_reason = None
        self._support_restore = None
        self._backup_name = None
        self._agent_status = None
        self._disabled_operate_types = None
        self._repair_priority = None
        self.discriminator = None

        if host_id is not None:
            self.host_id = host_id
        if agent_id is not None:
            self.agent_id = agent_id
        if repair_necessity is not None:
            self.repair_necessity = repair_necessity
        if severity_level is not None:
            self.severity_level = severity_level
        if host_name is not None:
            self.host_name = host_name
        if host_ip is not None:
            self.host_ip = host_ip
        if cve_num is not None:
            self.cve_num = cve_num
        if cve_id_list is not None:
            self.cve_id_list = cve_id_list
        if status is not None:
            self.status = status
        if remark is not None:
            self.remark = remark
        if repair_cmd is not None:
            self.repair_cmd = repair_cmd
        if version is not None:
            self.version = version
        if app_path is not None:
            self.app_path = app_path
        if is_affect_business is not None:
            self.is_affect_business = is_affect_business
        if asset_value is not None:
            self.asset_value = asset_value
        if private_ip is not None:
            self.private_ip = private_ip
        if group_name is not None:
            self.group_name = group_name
        if group_id is not None:
            self.group_id = group_id
        if os_type is not None:
            self.os_type = os_type
        if os_name is not None:
            self.os_name = os_name
        if os_version is not None:
            self.os_version = os_version
        if os_kernel is not None:
            self.os_kernel = os_kernel
        if host_status is not None:
            self.host_status = host_status
        if first_scan_time is not None:
            self.first_scan_time = first_scan_time
        if scan_time is not None:
            self.scan_time = scan_time
        if failed_reason is not None:
            self.failed_reason = failed_reason
        if support_restore is not None:
            self.support_restore = support_restore
        if backup_name is not None:
            self.backup_name = backup_name
        if agent_status is not None:
            self.agent_status = agent_status
        if disabled_operate_types is not None:
            self.disabled_operate_types = disabled_operate_types
        if repair_priority is not None:
            self.repair_priority = repair_priority

    @property
    def host_id(self):
        r"""Gets the host_id of this VulHostInfo.

        **参数解释**: 受漏洞影响的服务器id **取值范围**: 字符范围1-128位 

        :return: The host_id of this VulHostInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this VulHostInfo.

        **参数解释**: 受漏洞影响的服务器id **取值范围**: 字符范围1-128位 

        :param host_id: The host_id of this VulHostInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def agent_id(self):
        r"""Gets the agent_id of this VulHostInfo.

        **参数解释**: 主机对应的agent id **取值范围**: 字符范围1-128位 

        :return: The agent_id of this VulHostInfo.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this VulHostInfo.

        **参数解释**: 主机对应的agent id **取值范围**: 字符范围1-128位 

        :param agent_id: The agent_id of this VulHostInfo.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def repair_necessity(self):
        r"""Gets the repair_necessity of this VulHostInfo.

        **参数解释**: 修复紧急度 **取值范围**: - Critical：漏洞cvss评分大于等于9；对应控制台页面的高危 - High：漏洞cvss评分大于等于7，小于9；对应控制台页面的中危 - Medium：漏洞cvss评分大于等于4，小于7；对应控制台页面的中危 - Low：漏洞cvss评分小于4；对应控制台页面的低危 

        :return: The repair_necessity of this VulHostInfo.
        :rtype: str
        """
        return self._repair_necessity

    @repair_necessity.setter
    def repair_necessity(self, repair_necessity):
        r"""Sets the repair_necessity of this VulHostInfo.

        **参数解释**: 修复紧急度 **取值范围**: - Critical：漏洞cvss评分大于等于9；对应控制台页面的高危 - High：漏洞cvss评分大于等于7，小于9；对应控制台页面的中危 - Medium：漏洞cvss评分大于等于4，小于7；对应控制台页面的中危 - Low：漏洞cvss评分小于4；对应控制台页面的低危 

        :param repair_necessity: The repair_necessity of this VulHostInfo.
        :type repair_necessity: str
        """
        self._repair_necessity = repair_necessity

    @property
    def severity_level(self):
        r"""Gets the severity_level of this VulHostInfo.

        **参数解释**: 危险程度 **取值范围**: - Critical：漏洞cvss评分大于等于9；对应控制台页面的高危 - High：漏洞cvss评分大于等于7，小于9；对应控制台页面的中危 - Medium：漏洞cvss评分大于等于4，小于7；对应控制台页面的中危 - Low：漏洞cvss评分小于4；对应控制台页面的低危 

        :return: The severity_level of this VulHostInfo.
        :rtype: str
        """
        return self._severity_level

    @severity_level.setter
    def severity_level(self, severity_level):
        r"""Sets the severity_level of this VulHostInfo.

        **参数解释**: 危险程度 **取值范围**: - Critical：漏洞cvss评分大于等于9；对应控制台页面的高危 - High：漏洞cvss评分大于等于7，小于9；对应控制台页面的中危 - Medium：漏洞cvss评分大于等于4，小于7；对应控制台页面的中危 - Low：漏洞cvss评分小于4；对应控制台页面的低危 

        :param severity_level: The severity_level of this VulHostInfo.
        :type severity_level: str
        """
        self._severity_level = severity_level

    @property
    def host_name(self):
        r"""Gets the host_name of this VulHostInfo.

        **参数解释**: 受影响主机名称 **取值范围**: 字符范围1-256位 

        :return: The host_name of this VulHostInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this VulHostInfo.

        **参数解释**: 受影响主机名称 **取值范围**: 字符范围1-256位 

        :param host_name: The host_name of this VulHostInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_ip(self):
        r"""Gets the host_ip of this VulHostInfo.

        **参数解释**: 受影响主机ip **取值范围**: 字符范围1-256位 

        :return: The host_ip of this VulHostInfo.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        r"""Sets the host_ip of this VulHostInfo.

        **参数解释**: 受影响主机ip **取值范围**: 字符范围1-256位 

        :param host_ip: The host_ip of this VulHostInfo.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def cve_num(self):
        r"""Gets the cve_num of this VulHostInfo.

        **参数解释**: 漏洞cve总数 **取值范围**: 最小值0，最大值10000 

        :return: The cve_num of this VulHostInfo.
        :rtype: int
        """
        return self._cve_num

    @cve_num.setter
    def cve_num(self, cve_num):
        r"""Sets the cve_num of this VulHostInfo.

        **参数解释**: 漏洞cve总数 **取值范围**: 最小值0，最大值10000 

        :param cve_num: The cve_num of this VulHostInfo.
        :type cve_num: int
        """
        self._cve_num = cve_num

    @property
    def cve_id_list(self):
        r"""Gets the cve_id_list of this VulHostInfo.

        **参数解释**: 漏洞对应的cve id列表 **取值范围**: 最小值1，最大值10000 

        :return: The cve_id_list of this VulHostInfo.
        :rtype: list[str]
        """
        return self._cve_id_list

    @cve_id_list.setter
    def cve_id_list(self, cve_id_list):
        r"""Sets the cve_id_list of this VulHostInfo.

        **参数解释**: 漏洞对应的cve id列表 **取值范围**: 最小值1，最大值10000 

        :param cve_id_list: The cve_id_list of this VulHostInfo.
        :type cve_id_list: list[str]
        """
        self._cve_id_list = cve_id_list

    @property
    def status(self):
        r"""Gets the status of this VulHostInfo.

        **参数解释**: 漏洞状态 **取值范围**: - vul_status_unfix：未处理 - vul_status_ignored：已忽略 - vul_status_verified：验证中 - vul_status_fixing：修复中 - vul_status_fixed：修复成功 - vul_status_reboot：修复成功待重启 - vul_status_failed：修复失败 - vul_status_fix_after_reboot：请重启主机再次修复 

        :return: The status of this VulHostInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this VulHostInfo.

        **参数解释**: 漏洞状态 **取值范围**: - vul_status_unfix：未处理 - vul_status_ignored：已忽略 - vul_status_verified：验证中 - vul_status_fixing：修复中 - vul_status_fixed：修复成功 - vul_status_reboot：修复成功待重启 - vul_status_failed：修复失败 - vul_status_fix_after_reboot：请重启主机再次修复 

        :param status: The status of this VulHostInfo.
        :type status: str
        """
        self._status = status

    @property
    def remark(self):
        r"""Gets the remark of this VulHostInfo.

        **参数解释**: 处置备注 **取值范围**: 字符长度1-65535位 

        :return: The remark of this VulHostInfo.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        r"""Sets the remark of this VulHostInfo.

        **参数解释**: 处置备注 **取值范围**: 字符长度1-65535位 

        :param remark: The remark of this VulHostInfo.
        :type remark: str
        """
        self._remark = remark

    @property
    def repair_cmd(self):
        r"""Gets the repair_cmd of this VulHostInfo.

        **参数解释**: 修复漏洞需要执行的命令行（只有Linux漏洞有该字段） **取值范围**: 字符范围1-256位 

        :return: The repair_cmd of this VulHostInfo.
        :rtype: str
        """
        return self._repair_cmd

    @repair_cmd.setter
    def repair_cmd(self, repair_cmd):
        r"""Sets the repair_cmd of this VulHostInfo.

        **参数解释**: 修复漏洞需要执行的命令行（只有Linux漏洞有该字段） **取值范围**: 字符范围1-256位 

        :param repair_cmd: The repair_cmd of this VulHostInfo.
        :type repair_cmd: str
        """
        self._repair_cmd = repair_cmd

    @property
    def version(self):
        r"""Gets the version of this VulHostInfo.

        **参数解释**: 主机绑定的配额版本 **取值范围**: 字符范围1-128位 

        :return: The version of this VulHostInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this VulHostInfo.

        **参数解释**: 主机绑定的配额版本 **取值范围**: 字符范围1-128位 

        :param version: The version of this VulHostInfo.
        :type version: str
        """
        self._version = version

    @property
    def app_path(self):
        r"""Gets the app_path of this VulHostInfo.

        **参数解释**: 应用软件的路径（只有应用漏洞有该字段） **取值范围**: 字符范围1-512位 

        :return: The app_path of this VulHostInfo.
        :rtype: str
        """
        return self._app_path

    @app_path.setter
    def app_path(self, app_path):
        r"""Sets the app_path of this VulHostInfo.

        **参数解释**: 应用软件的路径（只有应用漏洞有该字段） **取值范围**: 字符范围1-512位 

        :param app_path: The app_path of this VulHostInfo.
        :type app_path: str
        """
        self._app_path = app_path

    @property
    def is_affect_business(self):
        r"""Gets the is_affect_business of this VulHostInfo.

        **参数解释**: 是否影响业务 **取值范围**: - true  : 影响业务 - false : 不影响业务 

        :return: The is_affect_business of this VulHostInfo.
        :rtype: bool
        """
        return self._is_affect_business

    @is_affect_business.setter
    def is_affect_business(self, is_affect_business):
        r"""Sets the is_affect_business of this VulHostInfo.

        **参数解释**: 是否影响业务 **取值范围**: - true  : 影响业务 - false : 不影响业务 

        :param is_affect_business: The is_affect_business of this VulHostInfo.
        :type is_affect_business: bool
        """
        self._is_affect_business = is_affect_business

    @property
    def asset_value(self):
        r"""Gets the asset_value of this VulHostInfo.

        **参数解释**: 资产重要性 **取值范围**: - important : 重要资产 - common    : 一般资产 - test      : 测试资产 

        :return: The asset_value of this VulHostInfo.
        :rtype: str
        """
        return self._asset_value

    @asset_value.setter
    def asset_value(self, asset_value):
        r"""Sets the asset_value of this VulHostInfo.

        **参数解释**: 资产重要性 **取值范围**: - important : 重要资产 - common    : 一般资产 - test      : 测试资产 

        :param asset_value: The asset_value of this VulHostInfo.
        :type asset_value: str
        """
        self._asset_value = asset_value

    @property
    def private_ip(self):
        r"""Gets the private_ip of this VulHostInfo.

        **参数解释**: 服务器私网ip **取值范围**: 字符范围0-128位 

        :return: The private_ip of this VulHostInfo.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this VulHostInfo.

        **参数解释**: 服务器私网ip **取值范围**: 字符范围0-128位 

        :param private_ip: The private_ip of this VulHostInfo.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def group_name(self):
        r"""Gets the group_name of this VulHostInfo.

        **参数解释**: 服务器组名称 **取值范围**: 字符范围0-256位 

        :return: The group_name of this VulHostInfo.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this VulHostInfo.

        **参数解释**: 服务器组名称 **取值范围**: 字符范围0-256位 

        :param group_name: The group_name of this VulHostInfo.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def group_id(self):
        r"""Gets the group_id of this VulHostInfo.

        **参数解释**: 服务器组id **取值范围**: 字符范围0-128位 

        :return: The group_id of this VulHostInfo.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this VulHostInfo.

        **参数解释**: 服务器组id **取值范围**: 字符范围0-128位 

        :param group_id: The group_id of this VulHostInfo.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def os_type(self):
        r"""Gets the os_type of this VulHostInfo.

        **参数解释**: 操作系统类型 **取值范围**: - Linux ：linux系统 - Windows：windows系统 

        :return: The os_type of this VulHostInfo.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this VulHostInfo.

        **参数解释**: 操作系统类型 **取值范围**: - Linux ：linux系统 - Windows：windows系统 

        :param os_type: The os_type of this VulHostInfo.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def os_name(self):
        r"""Gets the os_name of this VulHostInfo.

        **参数解释**: 操作系统名称 **取值范围**: 字符长度1-256位 

        :return: The os_name of this VulHostInfo.
        :rtype: str
        """
        return self._os_name

    @os_name.setter
    def os_name(self, os_name):
        r"""Sets the os_name of this VulHostInfo.

        **参数解释**: 操作系统名称 **取值范围**: 字符长度1-256位 

        :param os_name: The os_name of this VulHostInfo.
        :type os_name: str
        """
        self._os_name = os_name

    @property
    def os_version(self):
        r"""Gets the os_version of this VulHostInfo.

        **参数解释**: 操作系统版本 **取值范围**: 字符长度1-255位 

        :return: The os_version of this VulHostInfo.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        r"""Sets the os_version of this VulHostInfo.

        **参数解释**: 操作系统版本 **取值范围**: 字符长度1-255位 

        :param os_version: The os_version of this VulHostInfo.
        :type os_version: str
        """
        self._os_version = os_version

    @property
    def os_kernel(self):
        r"""Gets the os_kernel of this VulHostInfo.

        **参数解释**: 操作系统内核 **取值范围**: 字符长度1-64位 

        :return: The os_kernel of this VulHostInfo.
        :rtype: str
        """
        return self._os_kernel

    @os_kernel.setter
    def os_kernel(self, os_kernel):
        r"""Sets the os_kernel of this VulHostInfo.

        **参数解释**: 操作系统内核 **取值范围**: 字符长度1-64位 

        :param os_kernel: The os_kernel of this VulHostInfo.
        :type os_kernel: str
        """
        self._os_kernel = os_kernel

    @property
    def host_status(self):
        r"""Gets the host_status of this VulHostInfo.

        **参数解释**: 主机状态 **取值范围**: - ACTIVE：正在运行。 - SHUTOFF：关机。 - BUILDING：创建中。 - ERROR：故障。 **默认取值**: 不涉及 

        :return: The host_status of this VulHostInfo.
        :rtype: str
        """
        return self._host_status

    @host_status.setter
    def host_status(self, host_status):
        r"""Sets the host_status of this VulHostInfo.

        **参数解释**: 主机状态 **取值范围**: - ACTIVE：正在运行。 - SHUTOFF：关机。 - BUILDING：创建中。 - ERROR：故障。 **默认取值**: 不涉及 

        :param host_status: The host_status of this VulHostInfo.
        :type host_status: str
        """
        self._host_status = host_status

    @property
    def first_scan_time(self):
        r"""Gets the first_scan_time of this VulHostInfo.

        **参数解释**: 首次扫描时间 **取值范围**: 最小值0，最大值9223372036854775807 

        :return: The first_scan_time of this VulHostInfo.
        :rtype: int
        """
        return self._first_scan_time

    @first_scan_time.setter
    def first_scan_time(self, first_scan_time):
        r"""Sets the first_scan_time of this VulHostInfo.

        **参数解释**: 首次扫描时间 **取值范围**: 最小值0，最大值9223372036854775807 

        :param first_scan_time: The first_scan_time of this VulHostInfo.
        :type first_scan_time: int
        """
        self._first_scan_time = first_scan_time

    @property
    def scan_time(self):
        r"""Gets the scan_time of this VulHostInfo.

        **参数解释**: 扫描时间，时间戳单位：毫秒 **取值范围**: 最小值0，最大值9223372036854775807 

        :return: The scan_time of this VulHostInfo.
        :rtype: int
        """
        return self._scan_time

    @scan_time.setter
    def scan_time(self, scan_time):
        r"""Sets the scan_time of this VulHostInfo.

        **参数解释**: 扫描时间，时间戳单位：毫秒 **取值范围**: 最小值0，最大值9223372036854775807 

        :param scan_time: The scan_time of this VulHostInfo.
        :type scan_time: int
        """
        self._scan_time = scan_time

    @property
    def failed_reason(self):
        r"""Gets the failed_reason of this VulHostInfo.

        **参数解释**: 修复失败原因 **取值范围**: 字符长度1-65535位 

        :return: The failed_reason of this VulHostInfo.
        :rtype: str
        """
        return self._failed_reason

    @failed_reason.setter
    def failed_reason(self, failed_reason):
        r"""Sets the failed_reason of this VulHostInfo.

        **参数解释**: 修复失败原因 **取值范围**: 字符长度1-65535位 

        :param failed_reason: The failed_reason of this VulHostInfo.
        :type failed_reason: str
        """
        self._failed_reason = failed_reason

    @property
    def support_restore(self):
        r"""Gets the support_restore of this VulHostInfo.

        **参数解释**: 是否可以回滚到修复漏洞时创建的备份 **取值范围**: - true  : 可以回滚 - false : 不可以回滚 

        :return: The support_restore of this VulHostInfo.
        :rtype: bool
        """
        return self._support_restore

    @support_restore.setter
    def support_restore(self, support_restore):
        r"""Sets the support_restore of this VulHostInfo.

        **参数解释**: 是否可以回滚到修复漏洞时创建的备份 **取值范围**: - true  : 可以回滚 - false : 不可以回滚 

        :param support_restore: The support_restore of this VulHostInfo.
        :type support_restore: bool
        """
        self._support_restore = support_restore

    @property
    def backup_name(self):
        r"""Gets the backup_name of this VulHostInfo.

        **参数解释**: 备份名称 **取值范围**: 字符长度1-2048位 

        :return: The backup_name of this VulHostInfo.
        :rtype: str
        """
        return self._backup_name

    @backup_name.setter
    def backup_name(self, backup_name):
        r"""Sets the backup_name of this VulHostInfo.

        **参数解释**: 备份名称 **取值范围**: 字符长度1-2048位 

        :param backup_name: The backup_name of this VulHostInfo.
        :type backup_name: str
        """
        self._backup_name = backup_name

    @property
    def agent_status(self):
        r"""Gets the agent_status of this VulHostInfo.

        **参数解释**: Agent状态 **取值范围**: - installed：已安装。 - not_installed：未安装。 - online：在线。 - offline：离线。 - install_failed：安装失败。 - installing：安装中。

        :return: The agent_status of this VulHostInfo.
        :rtype: str
        """
        return self._agent_status

    @agent_status.setter
    def agent_status(self, agent_status):
        r"""Sets the agent_status of this VulHostInfo.

        **参数解释**: Agent状态 **取值范围**: - installed：已安装。 - not_installed：未安装。 - online：在线。 - offline：离线。 - install_failed：安装失败。 - installing：安装中。

        :param agent_status: The agent_status of this VulHostInfo.
        :type agent_status: str
        """
        self._agent_status = agent_status

    @property
    def disabled_operate_types(self):
        r"""Gets the disabled_operate_types of this VulHostInfo.

        **参数解释**: 漏洞在当前主机上不可进行的操作类型列表 **取值范围**: 最小值1，最大值10000 

        :return: The disabled_operate_types of this VulHostInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.HostVulInfoDisabledOperateTypes`]
        """
        return self._disabled_operate_types

    @disabled_operate_types.setter
    def disabled_operate_types(self, disabled_operate_types):
        r"""Sets the disabled_operate_types of this VulHostInfo.

        **参数解释**: 漏洞在当前主机上不可进行的操作类型列表 **取值范围**: 最小值1，最大值10000 

        :param disabled_operate_types: The disabled_operate_types of this VulHostInfo.
        :type disabled_operate_types: list[:class:`huaweicloudsdkhss.v5.HostVulInfoDisabledOperateTypes`]
        """
        self._disabled_operate_types = disabled_operate_types

    @property
    def repair_priority(self):
        r"""Gets the repair_priority of this VulHostInfo.

        **参数解释**: 修复优先级 **取值范围**: - Critical : 紧急 - High     : 高 - Medium   : 中 - Low      : 低 

        :return: The repair_priority of this VulHostInfo.
        :rtype: str
        """
        return self._repair_priority

    @repair_priority.setter
    def repair_priority(self, repair_priority):
        r"""Sets the repair_priority of this VulHostInfo.

        **参数解释**: 修复优先级 **取值范围**: - Critical : 紧急 - High     : 高 - Medium   : 中 - Low      : 低 

        :param repair_priority: The repair_priority of this VulHostInfo.
        :type repair_priority: str
        """
        self._repair_priority = repair_priority

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
        if not isinstance(other, VulHostInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
