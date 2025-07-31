# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HostVulInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vul_name': 'str',
        'vul_id': 'str',
        'label_list': 'list[str]',
        'repair_necessity': 'str',
        'scan_time': 'int',
        'type': 'str',
        'app_list': 'list[HostVulInfoAppList]',
        'severity_level': 'str',
        'solution_detail': 'str',
        'url': 'str',
        'description': 'str',
        'repair_cmd': 'str',
        'status': 'str',
        'repair_success_num': 'int',
        'cve_list': 'list[HostVulInfoCveList]',
        'is_affect_business': 'bool',
        'first_scan_time': 'int',
        'app_name': 'str',
        'app_version': 'str',
        'app_path': 'str',
        'version': 'str',
        'support_restore': 'bool',
        'disabled_operate_types': 'list[HostVulInfoDisabledOperateTypes]',
        'repair_priority': 'str'
    }

    attribute_map = {
        'vul_name': 'vul_name',
        'vul_id': 'vul_id',
        'label_list': 'label_list',
        'repair_necessity': 'repair_necessity',
        'scan_time': 'scan_time',
        'type': 'type',
        'app_list': 'app_list',
        'severity_level': 'severity_level',
        'solution_detail': 'solution_detail',
        'url': 'url',
        'description': 'description',
        'repair_cmd': 'repair_cmd',
        'status': 'status',
        'repair_success_num': 'repair_success_num',
        'cve_list': 'cve_list',
        'is_affect_business': 'is_affect_business',
        'first_scan_time': 'first_scan_time',
        'app_name': 'app_name',
        'app_version': 'app_version',
        'app_path': 'app_path',
        'version': 'version',
        'support_restore': 'support_restore',
        'disabled_operate_types': 'disabled_operate_types',
        'repair_priority': 'repair_priority'
    }

    def __init__(self, vul_name=None, vul_id=None, label_list=None, repair_necessity=None, scan_time=None, type=None, app_list=None, severity_level=None, solution_detail=None, url=None, description=None, repair_cmd=None, status=None, repair_success_num=None, cve_list=None, is_affect_business=None, first_scan_time=None, app_name=None, app_version=None, app_path=None, version=None, support_restore=None, disabled_operate_types=None, repair_priority=None):
        r"""HostVulInfo

        The model defined in huaweicloud sdk

        :param vul_name: **参数解释**: 漏洞名称 **取值范围**: 字符范围0-256位 
        :type vul_name: str
        :param vul_id: **参数解释**: 漏洞ID **取值范围**: 字符范围0-64位 
        :type vul_id: str
        :param label_list: **参数解释**: 漏洞标签列表 **取值范围**: 最小值0，最大值2147483647 
        :type label_list: list[str]
        :param repair_necessity: **参数解释**: 修复紧急度 **取值范围**: - immediate_repair  : 尽快修复 - delay_repair      : 延后修复 - not_needed_repair : 暂可不修复 
        :type repair_necessity: str
        :param scan_time: **参数解释**: 最近扫描时间 **取值范围**: 最小值0，最大值9223372036854775807 
        :type scan_time: int
        :param type: **参数解释**: 漏洞类型 **取值范围**: - linux_vul   : linux漏洞 - windows_vul : windows漏洞 - web_cms     : Web-CMS漏洞 - app_vul     : 应用漏洞 - urgent_vul  : 应急漏洞 
        :type type: str
        :param app_list: **参数解释**: 服务器上受该漏洞影响的软件列表 **取值范围**: 最小值0，最大值2147483647 
        :type app_list: list[:class:`huaweicloudsdkhss.v5.HostVulInfoAppList`]
        :param severity_level: **参数解释**: 危险程度 **取值范围**: - Critical : 漏洞cvss评分大于等于9；对应控制台页面的高危 - High     : 漏洞cvss评分大于等于7，小于9；对应控制台页面的中危 - Medium   : 漏洞cvss评分大于等于4，小于7；对应控制台页面的中危 - Low      : 漏洞cvss评分小于4；对应控制台页面的低危 
        :type severity_level: str
        :param solution_detail: **参数解释**: 解决方案 **取值范围**: 字符范围0-65534位 
        :type solution_detail: str
        :param url: **参数解释**: URL链接 **取值范围**: 字符范围0-2083位 
        :type url: str
        :param description: **参数解释**: 漏洞描述 **取值范围**: 字符范围0-65534位 
        :type description: str
        :param repair_cmd: **参数解释**: 修复命令行 **取值范围**: 字符范围1-256位 
        :type repair_cmd: str
        :param status: **参数解释**: 漏洞状态 **取值范围**: - vul_status_unfix            : 未处理 - vul_status_ignored          : 已忽略 - vul_status_verified         : 验证中 - vul_status_fixing           : 修复中 - vul_status_fixed            : 修复成功 - vul_status_reboot           : 修复成功待重启 - vul_status_failed           : 修复失败 - vul_status_fix_after_reboot : 请重启主机再次修复 
        :type status: str
        :param repair_success_num: **参数解释**: HSS全网修复该漏洞的次数 **取值范围**: 最小值0，最大值1000000 
        :type repair_success_num: int
        :param cve_list: **参数解释**: CVE列表 **取值范围**: 最小值1，最大值10000 
        :type cve_list: list[:class:`huaweicloudsdkhss.v5.HostVulInfoCveList`]
        :param is_affect_business: **参数解释**: 是否影响业务 **取值范围**: - true  : 影响业务 - false : 不影响业务 
        :type is_affect_business: bool
        :param first_scan_time: **参数解释**: 首次扫描时间 **取值范围**: 最小值0，最大值9223372036854775807 
        :type first_scan_time: int
        :param app_name: **参数解释**: 软件名称 **取值范围**: 字符长度0-256位 
        :type app_name: str
        :param app_version: **参数解释**: 软件版本 **取值范围**: 字符长度0-256位 
        :type app_version: str
        :param app_path: **参数解释**: 软件路径 **取值范围**: 字符长度0-512位 
        :type app_path: str
        :param version: **参数解释**: 主机配额 **取值范围**: 字符长度0-128位 
        :type version: str
        :param support_restore: **参数解释**: 是否可以回滚到修复漏洞时创建的备份 **取值范围**: - true  : 可以回滚 - false : 不可以回滚 
        :type support_restore: bool
        :param disabled_operate_types: **参数解释**: 该漏洞不可进行的操作类型列表 **取值范围**: 最小值1，最大值10000 
        :type disabled_operate_types: list[:class:`huaweicloudsdkhss.v5.HostVulInfoDisabledOperateTypes`]
        :param repair_priority: **参数解释**: 修复优先级 **取值范围**: - Critical : 紧急  - High     : 高  - Medium   : 中  - Low      : 低 
        :type repair_priority: str
        """
        
        

        self._vul_name = None
        self._vul_id = None
        self._label_list = None
        self._repair_necessity = None
        self._scan_time = None
        self._type = None
        self._app_list = None
        self._severity_level = None
        self._solution_detail = None
        self._url = None
        self._description = None
        self._repair_cmd = None
        self._status = None
        self._repair_success_num = None
        self._cve_list = None
        self._is_affect_business = None
        self._first_scan_time = None
        self._app_name = None
        self._app_version = None
        self._app_path = None
        self._version = None
        self._support_restore = None
        self._disabled_operate_types = None
        self._repair_priority = None
        self.discriminator = None

        if vul_name is not None:
            self.vul_name = vul_name
        if vul_id is not None:
            self.vul_id = vul_id
        if label_list is not None:
            self.label_list = label_list
        if repair_necessity is not None:
            self.repair_necessity = repair_necessity
        if scan_time is not None:
            self.scan_time = scan_time
        if type is not None:
            self.type = type
        if app_list is not None:
            self.app_list = app_list
        if severity_level is not None:
            self.severity_level = severity_level
        if solution_detail is not None:
            self.solution_detail = solution_detail
        if url is not None:
            self.url = url
        if description is not None:
            self.description = description
        if repair_cmd is not None:
            self.repair_cmd = repair_cmd
        if status is not None:
            self.status = status
        if repair_success_num is not None:
            self.repair_success_num = repair_success_num
        if cve_list is not None:
            self.cve_list = cve_list
        if is_affect_business is not None:
            self.is_affect_business = is_affect_business
        if first_scan_time is not None:
            self.first_scan_time = first_scan_time
        if app_name is not None:
            self.app_name = app_name
        if app_version is not None:
            self.app_version = app_version
        if app_path is not None:
            self.app_path = app_path
        if version is not None:
            self.version = version
        if support_restore is not None:
            self.support_restore = support_restore
        if disabled_operate_types is not None:
            self.disabled_operate_types = disabled_operate_types
        if repair_priority is not None:
            self.repair_priority = repair_priority

    @property
    def vul_name(self):
        r"""Gets the vul_name of this HostVulInfo.

        **参数解释**: 漏洞名称 **取值范围**: 字符范围0-256位 

        :return: The vul_name of this HostVulInfo.
        :rtype: str
        """
        return self._vul_name

    @vul_name.setter
    def vul_name(self, vul_name):
        r"""Sets the vul_name of this HostVulInfo.

        **参数解释**: 漏洞名称 **取值范围**: 字符范围0-256位 

        :param vul_name: The vul_name of this HostVulInfo.
        :type vul_name: str
        """
        self._vul_name = vul_name

    @property
    def vul_id(self):
        r"""Gets the vul_id of this HostVulInfo.

        **参数解释**: 漏洞ID **取值范围**: 字符范围0-64位 

        :return: The vul_id of this HostVulInfo.
        :rtype: str
        """
        return self._vul_id

    @vul_id.setter
    def vul_id(self, vul_id):
        r"""Sets the vul_id of this HostVulInfo.

        **参数解释**: 漏洞ID **取值范围**: 字符范围0-64位 

        :param vul_id: The vul_id of this HostVulInfo.
        :type vul_id: str
        """
        self._vul_id = vul_id

    @property
    def label_list(self):
        r"""Gets the label_list of this HostVulInfo.

        **参数解释**: 漏洞标签列表 **取值范围**: 最小值0，最大值2147483647 

        :return: The label_list of this HostVulInfo.
        :rtype: list[str]
        """
        return self._label_list

    @label_list.setter
    def label_list(self, label_list):
        r"""Sets the label_list of this HostVulInfo.

        **参数解释**: 漏洞标签列表 **取值范围**: 最小值0，最大值2147483647 

        :param label_list: The label_list of this HostVulInfo.
        :type label_list: list[str]
        """
        self._label_list = label_list

    @property
    def repair_necessity(self):
        r"""Gets the repair_necessity of this HostVulInfo.

        **参数解释**: 修复紧急度 **取值范围**: - immediate_repair  : 尽快修复 - delay_repair      : 延后修复 - not_needed_repair : 暂可不修复 

        :return: The repair_necessity of this HostVulInfo.
        :rtype: str
        """
        return self._repair_necessity

    @repair_necessity.setter
    def repair_necessity(self, repair_necessity):
        r"""Sets the repair_necessity of this HostVulInfo.

        **参数解释**: 修复紧急度 **取值范围**: - immediate_repair  : 尽快修复 - delay_repair      : 延后修复 - not_needed_repair : 暂可不修复 

        :param repair_necessity: The repair_necessity of this HostVulInfo.
        :type repair_necessity: str
        """
        self._repair_necessity = repair_necessity

    @property
    def scan_time(self):
        r"""Gets the scan_time of this HostVulInfo.

        **参数解释**: 最近扫描时间 **取值范围**: 最小值0，最大值9223372036854775807 

        :return: The scan_time of this HostVulInfo.
        :rtype: int
        """
        return self._scan_time

    @scan_time.setter
    def scan_time(self, scan_time):
        r"""Sets the scan_time of this HostVulInfo.

        **参数解释**: 最近扫描时间 **取值范围**: 最小值0，最大值9223372036854775807 

        :param scan_time: The scan_time of this HostVulInfo.
        :type scan_time: int
        """
        self._scan_time = scan_time

    @property
    def type(self):
        r"""Gets the type of this HostVulInfo.

        **参数解释**: 漏洞类型 **取值范围**: - linux_vul   : linux漏洞 - windows_vul : windows漏洞 - web_cms     : Web-CMS漏洞 - app_vul     : 应用漏洞 - urgent_vul  : 应急漏洞 

        :return: The type of this HostVulInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this HostVulInfo.

        **参数解释**: 漏洞类型 **取值范围**: - linux_vul   : linux漏洞 - windows_vul : windows漏洞 - web_cms     : Web-CMS漏洞 - app_vul     : 应用漏洞 - urgent_vul  : 应急漏洞 

        :param type: The type of this HostVulInfo.
        :type type: str
        """
        self._type = type

    @property
    def app_list(self):
        r"""Gets the app_list of this HostVulInfo.

        **参数解释**: 服务器上受该漏洞影响的软件列表 **取值范围**: 最小值0，最大值2147483647 

        :return: The app_list of this HostVulInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.HostVulInfoAppList`]
        """
        return self._app_list

    @app_list.setter
    def app_list(self, app_list):
        r"""Sets the app_list of this HostVulInfo.

        **参数解释**: 服务器上受该漏洞影响的软件列表 **取值范围**: 最小值0，最大值2147483647 

        :param app_list: The app_list of this HostVulInfo.
        :type app_list: list[:class:`huaweicloudsdkhss.v5.HostVulInfoAppList`]
        """
        self._app_list = app_list

    @property
    def severity_level(self):
        r"""Gets the severity_level of this HostVulInfo.

        **参数解释**: 危险程度 **取值范围**: - Critical : 漏洞cvss评分大于等于9；对应控制台页面的高危 - High     : 漏洞cvss评分大于等于7，小于9；对应控制台页面的中危 - Medium   : 漏洞cvss评分大于等于4，小于7；对应控制台页面的中危 - Low      : 漏洞cvss评分小于4；对应控制台页面的低危 

        :return: The severity_level of this HostVulInfo.
        :rtype: str
        """
        return self._severity_level

    @severity_level.setter
    def severity_level(self, severity_level):
        r"""Sets the severity_level of this HostVulInfo.

        **参数解释**: 危险程度 **取值范围**: - Critical : 漏洞cvss评分大于等于9；对应控制台页面的高危 - High     : 漏洞cvss评分大于等于7，小于9；对应控制台页面的中危 - Medium   : 漏洞cvss评分大于等于4，小于7；对应控制台页面的中危 - Low      : 漏洞cvss评分小于4；对应控制台页面的低危 

        :param severity_level: The severity_level of this HostVulInfo.
        :type severity_level: str
        """
        self._severity_level = severity_level

    @property
    def solution_detail(self):
        r"""Gets the solution_detail of this HostVulInfo.

        **参数解释**: 解决方案 **取值范围**: 字符范围0-65534位 

        :return: The solution_detail of this HostVulInfo.
        :rtype: str
        """
        return self._solution_detail

    @solution_detail.setter
    def solution_detail(self, solution_detail):
        r"""Sets the solution_detail of this HostVulInfo.

        **参数解释**: 解决方案 **取值范围**: 字符范围0-65534位 

        :param solution_detail: The solution_detail of this HostVulInfo.
        :type solution_detail: str
        """
        self._solution_detail = solution_detail

    @property
    def url(self):
        r"""Gets the url of this HostVulInfo.

        **参数解释**: URL链接 **取值范围**: 字符范围0-2083位 

        :return: The url of this HostVulInfo.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this HostVulInfo.

        **参数解释**: URL链接 **取值范围**: 字符范围0-2083位 

        :param url: The url of this HostVulInfo.
        :type url: str
        """
        self._url = url

    @property
    def description(self):
        r"""Gets the description of this HostVulInfo.

        **参数解释**: 漏洞描述 **取值范围**: 字符范围0-65534位 

        :return: The description of this HostVulInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this HostVulInfo.

        **参数解释**: 漏洞描述 **取值范围**: 字符范围0-65534位 

        :param description: The description of this HostVulInfo.
        :type description: str
        """
        self._description = description

    @property
    def repair_cmd(self):
        r"""Gets the repair_cmd of this HostVulInfo.

        **参数解释**: 修复命令行 **取值范围**: 字符范围1-256位 

        :return: The repair_cmd of this HostVulInfo.
        :rtype: str
        """
        return self._repair_cmd

    @repair_cmd.setter
    def repair_cmd(self, repair_cmd):
        r"""Sets the repair_cmd of this HostVulInfo.

        **参数解释**: 修复命令行 **取值范围**: 字符范围1-256位 

        :param repair_cmd: The repair_cmd of this HostVulInfo.
        :type repair_cmd: str
        """
        self._repair_cmd = repair_cmd

    @property
    def status(self):
        r"""Gets the status of this HostVulInfo.

        **参数解释**: 漏洞状态 **取值范围**: - vul_status_unfix            : 未处理 - vul_status_ignored          : 已忽略 - vul_status_verified         : 验证中 - vul_status_fixing           : 修复中 - vul_status_fixed            : 修复成功 - vul_status_reboot           : 修复成功待重启 - vul_status_failed           : 修复失败 - vul_status_fix_after_reboot : 请重启主机再次修复 

        :return: The status of this HostVulInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this HostVulInfo.

        **参数解释**: 漏洞状态 **取值范围**: - vul_status_unfix            : 未处理 - vul_status_ignored          : 已忽略 - vul_status_verified         : 验证中 - vul_status_fixing           : 修复中 - vul_status_fixed            : 修复成功 - vul_status_reboot           : 修复成功待重启 - vul_status_failed           : 修复失败 - vul_status_fix_after_reboot : 请重启主机再次修复 

        :param status: The status of this HostVulInfo.
        :type status: str
        """
        self._status = status

    @property
    def repair_success_num(self):
        r"""Gets the repair_success_num of this HostVulInfo.

        **参数解释**: HSS全网修复该漏洞的次数 **取值范围**: 最小值0，最大值1000000 

        :return: The repair_success_num of this HostVulInfo.
        :rtype: int
        """
        return self._repair_success_num

    @repair_success_num.setter
    def repair_success_num(self, repair_success_num):
        r"""Sets the repair_success_num of this HostVulInfo.

        **参数解释**: HSS全网修复该漏洞的次数 **取值范围**: 最小值0，最大值1000000 

        :param repair_success_num: The repair_success_num of this HostVulInfo.
        :type repair_success_num: int
        """
        self._repair_success_num = repair_success_num

    @property
    def cve_list(self):
        r"""Gets the cve_list of this HostVulInfo.

        **参数解释**: CVE列表 **取值范围**: 最小值1，最大值10000 

        :return: The cve_list of this HostVulInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.HostVulInfoCveList`]
        """
        return self._cve_list

    @cve_list.setter
    def cve_list(self, cve_list):
        r"""Sets the cve_list of this HostVulInfo.

        **参数解释**: CVE列表 **取值范围**: 最小值1，最大值10000 

        :param cve_list: The cve_list of this HostVulInfo.
        :type cve_list: list[:class:`huaweicloudsdkhss.v5.HostVulInfoCveList`]
        """
        self._cve_list = cve_list

    @property
    def is_affect_business(self):
        r"""Gets the is_affect_business of this HostVulInfo.

        **参数解释**: 是否影响业务 **取值范围**: - true  : 影响业务 - false : 不影响业务 

        :return: The is_affect_business of this HostVulInfo.
        :rtype: bool
        """
        return self._is_affect_business

    @is_affect_business.setter
    def is_affect_business(self, is_affect_business):
        r"""Sets the is_affect_business of this HostVulInfo.

        **参数解释**: 是否影响业务 **取值范围**: - true  : 影响业务 - false : 不影响业务 

        :param is_affect_business: The is_affect_business of this HostVulInfo.
        :type is_affect_business: bool
        """
        self._is_affect_business = is_affect_business

    @property
    def first_scan_time(self):
        r"""Gets the first_scan_time of this HostVulInfo.

        **参数解释**: 首次扫描时间 **取值范围**: 最小值0，最大值9223372036854775807 

        :return: The first_scan_time of this HostVulInfo.
        :rtype: int
        """
        return self._first_scan_time

    @first_scan_time.setter
    def first_scan_time(self, first_scan_time):
        r"""Sets the first_scan_time of this HostVulInfo.

        **参数解释**: 首次扫描时间 **取值范围**: 最小值0，最大值9223372036854775807 

        :param first_scan_time: The first_scan_time of this HostVulInfo.
        :type first_scan_time: int
        """
        self._first_scan_time = first_scan_time

    @property
    def app_name(self):
        r"""Gets the app_name of this HostVulInfo.

        **参数解释**: 软件名称 **取值范围**: 字符长度0-256位 

        :return: The app_name of this HostVulInfo.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this HostVulInfo.

        **参数解释**: 软件名称 **取值范围**: 字符长度0-256位 

        :param app_name: The app_name of this HostVulInfo.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def app_version(self):
        r"""Gets the app_version of this HostVulInfo.

        **参数解释**: 软件版本 **取值范围**: 字符长度0-256位 

        :return: The app_version of this HostVulInfo.
        :rtype: str
        """
        return self._app_version

    @app_version.setter
    def app_version(self, app_version):
        r"""Sets the app_version of this HostVulInfo.

        **参数解释**: 软件版本 **取值范围**: 字符长度0-256位 

        :param app_version: The app_version of this HostVulInfo.
        :type app_version: str
        """
        self._app_version = app_version

    @property
    def app_path(self):
        r"""Gets the app_path of this HostVulInfo.

        **参数解释**: 软件路径 **取值范围**: 字符长度0-512位 

        :return: The app_path of this HostVulInfo.
        :rtype: str
        """
        return self._app_path

    @app_path.setter
    def app_path(self, app_path):
        r"""Sets the app_path of this HostVulInfo.

        **参数解释**: 软件路径 **取值范围**: 字符长度0-512位 

        :param app_path: The app_path of this HostVulInfo.
        :type app_path: str
        """
        self._app_path = app_path

    @property
    def version(self):
        r"""Gets the version of this HostVulInfo.

        **参数解释**: 主机配额 **取值范围**: 字符长度0-128位 

        :return: The version of this HostVulInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this HostVulInfo.

        **参数解释**: 主机配额 **取值范围**: 字符长度0-128位 

        :param version: The version of this HostVulInfo.
        :type version: str
        """
        self._version = version

    @property
    def support_restore(self):
        r"""Gets the support_restore of this HostVulInfo.

        **参数解释**: 是否可以回滚到修复漏洞时创建的备份 **取值范围**: - true  : 可以回滚 - false : 不可以回滚 

        :return: The support_restore of this HostVulInfo.
        :rtype: bool
        """
        return self._support_restore

    @support_restore.setter
    def support_restore(self, support_restore):
        r"""Sets the support_restore of this HostVulInfo.

        **参数解释**: 是否可以回滚到修复漏洞时创建的备份 **取值范围**: - true  : 可以回滚 - false : 不可以回滚 

        :param support_restore: The support_restore of this HostVulInfo.
        :type support_restore: bool
        """
        self._support_restore = support_restore

    @property
    def disabled_operate_types(self):
        r"""Gets the disabled_operate_types of this HostVulInfo.

        **参数解释**: 该漏洞不可进行的操作类型列表 **取值范围**: 最小值1，最大值10000 

        :return: The disabled_operate_types of this HostVulInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.HostVulInfoDisabledOperateTypes`]
        """
        return self._disabled_operate_types

    @disabled_operate_types.setter
    def disabled_operate_types(self, disabled_operate_types):
        r"""Sets the disabled_operate_types of this HostVulInfo.

        **参数解释**: 该漏洞不可进行的操作类型列表 **取值范围**: 最小值1，最大值10000 

        :param disabled_operate_types: The disabled_operate_types of this HostVulInfo.
        :type disabled_operate_types: list[:class:`huaweicloudsdkhss.v5.HostVulInfoDisabledOperateTypes`]
        """
        self._disabled_operate_types = disabled_operate_types

    @property
    def repair_priority(self):
        r"""Gets the repair_priority of this HostVulInfo.

        **参数解释**: 修复优先级 **取值范围**: - Critical : 紧急  - High     : 高  - Medium   : 中  - Low      : 低 

        :return: The repair_priority of this HostVulInfo.
        :rtype: str
        """
        return self._repair_priority

    @repair_priority.setter
    def repair_priority(self, repair_priority):
        r"""Sets the repair_priority of this HostVulInfo.

        **参数解释**: 修复优先级 **取值范围**: - Critical : 紧急  - High     : 高  - Medium   : 中  - Low      : 低 

        :param repair_priority: The repair_priority of this HostVulInfo.
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
        if not isinstance(other, HostVulInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
