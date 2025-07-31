# coding: utf-8

import six

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
        'severity_level': 'str',
        'host_name': 'str',
        'host_ip': 'str',
        'agent_id': 'str',
        'version': 'str',
        'cve_num': 'int',
        'cve_id_list': 'list[str]',
        'status': 'str',
        'repair_cmd': 'str',
        'app_path': 'str',
        'region_name': 'str',
        'public_ip': 'str',
        'private_ip': 'str',
        'group_id': 'str',
        'group_name': 'str',
        'os_type': 'str',
        'asset_value': 'str',
        'is_affect_business': 'bool',
        'first_scan_time': 'int',
        'scan_time': 'int',
        'support_restore': 'bool',
        'disabled_operate_types': 'list[HostVulInfoDisabledOperateTypes]',
        'repair_priority': 'str'
    }

    attribute_map = {
        'host_id': 'host_id',
        'severity_level': 'severity_level',
        'host_name': 'host_name',
        'host_ip': 'host_ip',
        'agent_id': 'agent_id',
        'version': 'version',
        'cve_num': 'cve_num',
        'cve_id_list': 'cve_id_list',
        'status': 'status',
        'repair_cmd': 'repair_cmd',
        'app_path': 'app_path',
        'region_name': 'region_name',
        'public_ip': 'public_ip',
        'private_ip': 'private_ip',
        'group_id': 'group_id',
        'group_name': 'group_name',
        'os_type': 'os_type',
        'asset_value': 'asset_value',
        'is_affect_business': 'is_affect_business',
        'first_scan_time': 'first_scan_time',
        'scan_time': 'scan_time',
        'support_restore': 'support_restore',
        'disabled_operate_types': 'disabled_operate_types',
        'repair_priority': 'repair_priority'
    }

    def __init__(self, host_id=None, severity_level=None, host_name=None, host_ip=None, agent_id=None, version=None, cve_num=None, cve_id_list=None, status=None, repair_cmd=None, app_path=None, region_name=None, public_ip=None, private_ip=None, group_id=None, group_name=None, os_type=None, asset_value=None, is_affect_business=None, first_scan_time=None, scan_time=None, support_restore=None, disabled_operate_types=None, repair_priority=None):
        r"""VulHostInfo

        The model defined in huaweicloud sdk

        :param host_id: 受漏洞影响的服务器id
        :type host_id: str
        :param severity_level: **参数解释**: 危险程度 **取值范围**: - Critical : 漏洞cvss评分大于等于9；对应控制台页面的高危 - High     : 漏洞cvss评分大于等于7，小于9；对应控制台页面的中危 - Medium   : 漏洞cvss评分大于等于4，小于7；对应控制台页面的中危 - Low      : 漏洞cvss评分小于4；对应控制台页面的低危 
        :type severity_level: str
        :param host_name: **参数解释**: 受影响主机名称 **取值范围**: 字符范围1-256位 
        :type host_name: str
        :param host_ip: **参数解释**: 受影响主机ip **取值范围**: 字符范围1-256位 
        :type host_ip: str
        :param agent_id: **参数解释**: 主机对应的agent id **取值范围**: 字符范围1-128位 
        :type agent_id: str
        :param version: **参数解释**: 主机绑定的配额版本 **取值范围**: 字符范围1-128位 
        :type version: str
        :param cve_num: **参数解释**: 漏洞cve总数 **取值范围**: 最小值0，最大值10000 
        :type cve_num: int
        :param cve_id_list: **参数解释**: 漏洞对应的cve id列表 **取值范围**: 最小值1，最大值10000 
        :type cve_id_list: list[str]
        :param status: **参数解释**: 漏洞状态 **取值范围**: - vul_status_unfix            : 未处理 - vul_status_ignored          : 已忽略 - vul_status_verified         : 验证中 - vul_status_fixing           : 修复中 - vul_status_fixed            : 修复成功 - vul_status_reboot           : 修复成功待重启 - vul_status_failed           : 修复失败 - vul_status_fix_after_reboot : 请重启主机再次修复 
        :type status: str
        :param repair_cmd: **参数解释**: 修复漏洞需要执行的命令行（只有Linux漏洞有该字段） **取值范围**: 字符范围1-256位 
        :type repair_cmd: str
        :param app_path: **参数解释**: 应用软件的路径（只有应用漏洞有该字段） **取值范围**: 字符范围1-512位 
        :type app_path: str
        :param region_name: **参数解释**: 地域 **取值范围**: 字符范围0-128位 
        :type region_name: str
        :param public_ip: **参数解释**: 服务器公网ip **取值范围**: 字符范围0-128位 
        :type public_ip: str
        :param private_ip: **参数解释**: 服务器私网ip **取值范围**: 字符范围0-128位 
        :type private_ip: str
        :param group_id: **参数解释**: 服务器组id **取值范围**: 字符范围0-128位 
        :type group_id: str
        :param group_name: **参数解释**: 服务器组名称 **取值范围**: 字符范围0-256位 
        :type group_name: str
        :param os_type: **参数解释**: 操作系统 **取值范围**: 字符范围0-32位 
        :type os_type: str
        :param asset_value: **参数解释**: 资产重要性 **取值范围**: - important : 重要资产 - common    : 一般资产 - test      : 测试资产 
        :type asset_value: str
        :param is_affect_business: **参数解释**: 是否影响业务 **取值范围**: - true  : 影响业务 - false : 不影响业务 
        :type is_affect_business: bool
        :param first_scan_time: **参数解释**: 首次扫描时间 **取值范围**: 最小值0，最大值9223372036854775807 
        :type first_scan_time: int
        :param scan_time: **参数解释**: 扫描时间，时间戳单位：毫秒 **取值范围**: 最小值0，最大值9223372036854775807 
        :type scan_time: int
        :param support_restore: **参数解释**: 是否可以回滚到修复漏洞时创建的备份 **取值范围**: - true  : 可以回滚 - false : 不可以回滚 
        :type support_restore: bool
        :param disabled_operate_types: **参数解释**: 漏洞在当前主机上不可进行的操作类型列表 **取值范围**: 最小值1，最大值10000 
        :type disabled_operate_types: list[:class:`huaweicloudsdkhss.v5.HostVulInfoDisabledOperateTypes`]
        :param repair_priority: **参数解释**: 修复优先级 **取值范围**: - Critical : 紧急  - High     : 高  - Medium   : 中  - Low      : 低 
        :type repair_priority: str
        """
        
        

        self._host_id = None
        self._severity_level = None
        self._host_name = None
        self._host_ip = None
        self._agent_id = None
        self._version = None
        self._cve_num = None
        self._cve_id_list = None
        self._status = None
        self._repair_cmd = None
        self._app_path = None
        self._region_name = None
        self._public_ip = None
        self._private_ip = None
        self._group_id = None
        self._group_name = None
        self._os_type = None
        self._asset_value = None
        self._is_affect_business = None
        self._first_scan_time = None
        self._scan_time = None
        self._support_restore = None
        self._disabled_operate_types = None
        self._repair_priority = None
        self.discriminator = None

        if host_id is not None:
            self.host_id = host_id
        if severity_level is not None:
            self.severity_level = severity_level
        if host_name is not None:
            self.host_name = host_name
        if host_ip is not None:
            self.host_ip = host_ip
        if agent_id is not None:
            self.agent_id = agent_id
        if version is not None:
            self.version = version
        if cve_num is not None:
            self.cve_num = cve_num
        if cve_id_list is not None:
            self.cve_id_list = cve_id_list
        if status is not None:
            self.status = status
        if repair_cmd is not None:
            self.repair_cmd = repair_cmd
        if app_path is not None:
            self.app_path = app_path
        if region_name is not None:
            self.region_name = region_name
        if public_ip is not None:
            self.public_ip = public_ip
        if private_ip is not None:
            self.private_ip = private_ip
        if group_id is not None:
            self.group_id = group_id
        if group_name is not None:
            self.group_name = group_name
        if os_type is not None:
            self.os_type = os_type
        if asset_value is not None:
            self.asset_value = asset_value
        if is_affect_business is not None:
            self.is_affect_business = is_affect_business
        if first_scan_time is not None:
            self.first_scan_time = first_scan_time
        if scan_time is not None:
            self.scan_time = scan_time
        if support_restore is not None:
            self.support_restore = support_restore
        if disabled_operate_types is not None:
            self.disabled_operate_types = disabled_operate_types
        if repair_priority is not None:
            self.repair_priority = repair_priority

    @property
    def host_id(self):
        r"""Gets the host_id of this VulHostInfo.

        受漏洞影响的服务器id

        :return: The host_id of this VulHostInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this VulHostInfo.

        受漏洞影响的服务器id

        :param host_id: The host_id of this VulHostInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def severity_level(self):
        r"""Gets the severity_level of this VulHostInfo.

        **参数解释**: 危险程度 **取值范围**: - Critical : 漏洞cvss评分大于等于9；对应控制台页面的高危 - High     : 漏洞cvss评分大于等于7，小于9；对应控制台页面的中危 - Medium   : 漏洞cvss评分大于等于4，小于7；对应控制台页面的中危 - Low      : 漏洞cvss评分小于4；对应控制台页面的低危 

        :return: The severity_level of this VulHostInfo.
        :rtype: str
        """
        return self._severity_level

    @severity_level.setter
    def severity_level(self, severity_level):
        r"""Sets the severity_level of this VulHostInfo.

        **参数解释**: 危险程度 **取值范围**: - Critical : 漏洞cvss评分大于等于9；对应控制台页面的高危 - High     : 漏洞cvss评分大于等于7，小于9；对应控制台页面的中危 - Medium   : 漏洞cvss评分大于等于4，小于7；对应控制台页面的中危 - Low      : 漏洞cvss评分小于4；对应控制台页面的低危 

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

        **参数解释**: 漏洞状态 **取值范围**: - vul_status_unfix            : 未处理 - vul_status_ignored          : 已忽略 - vul_status_verified         : 验证中 - vul_status_fixing           : 修复中 - vul_status_fixed            : 修复成功 - vul_status_reboot           : 修复成功待重启 - vul_status_failed           : 修复失败 - vul_status_fix_after_reboot : 请重启主机再次修复 

        :return: The status of this VulHostInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this VulHostInfo.

        **参数解释**: 漏洞状态 **取值范围**: - vul_status_unfix            : 未处理 - vul_status_ignored          : 已忽略 - vul_status_verified         : 验证中 - vul_status_fixing           : 修复中 - vul_status_fixed            : 修复成功 - vul_status_reboot           : 修复成功待重启 - vul_status_failed           : 修复失败 - vul_status_fix_after_reboot : 请重启主机再次修复 

        :param status: The status of this VulHostInfo.
        :type status: str
        """
        self._status = status

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
    def region_name(self):
        r"""Gets the region_name of this VulHostInfo.

        **参数解释**: 地域 **取值范围**: 字符范围0-128位 

        :return: The region_name of this VulHostInfo.
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        r"""Sets the region_name of this VulHostInfo.

        **参数解释**: 地域 **取值范围**: 字符范围0-128位 

        :param region_name: The region_name of this VulHostInfo.
        :type region_name: str
        """
        self._region_name = region_name

    @property
    def public_ip(self):
        r"""Gets the public_ip of this VulHostInfo.

        **参数解释**: 服务器公网ip **取值范围**: 字符范围0-128位 

        :return: The public_ip of this VulHostInfo.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this VulHostInfo.

        **参数解释**: 服务器公网ip **取值范围**: 字符范围0-128位 

        :param public_ip: The public_ip of this VulHostInfo.
        :type public_ip: str
        """
        self._public_ip = public_ip

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
    def os_type(self):
        r"""Gets the os_type of this VulHostInfo.

        **参数解释**: 操作系统 **取值范围**: 字符范围0-32位 

        :return: The os_type of this VulHostInfo.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this VulHostInfo.

        **参数解释**: 操作系统 **取值范围**: 字符范围0-32位 

        :param os_type: The os_type of this VulHostInfo.
        :type os_type: str
        """
        self._os_type = os_type

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

        **参数解释**: 修复优先级 **取值范围**: - Critical : 紧急  - High     : 高  - Medium   : 中  - Low      : 低 

        :return: The repair_priority of this VulHostInfo.
        :rtype: str
        """
        return self._repair_priority

    @repair_priority.setter
    def repair_priority(self, repair_priority):
        r"""Sets the repair_priority of this VulHostInfo.

        **参数解释**: 修复优先级 **取值范围**: - Critical : 紧急  - High     : 高  - Medium   : 中  - Low      : 低 

        :param repair_priority: The repair_priority of this VulHostInfo.
        :type repair_priority: str
        """
        self._repair_priority = repair_priority

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
        if not isinstance(other, VulHostInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
