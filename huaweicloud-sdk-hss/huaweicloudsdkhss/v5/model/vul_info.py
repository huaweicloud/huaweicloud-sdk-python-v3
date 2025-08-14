# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VulInfo:

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
        'severity_level': 'str',
        'host_num': 'int',
        'unhandle_host_num': 'int',
        'scan_time': 'int',
        'solution_detail': 'str',
        'url': 'str',
        'description': 'str',
        'type': 'str',
        'host_id_list': 'list[str]',
        'cve_list': 'list[VulInfoCveList]',
        'patch_url': 'str',
        'repair_priority': 'str',
        'hosts_num': 'VulnerabilityHostNumberInfo',
        'repair_success_num': 'int',
        'fixed_num': 'int',
        'ignored_num': 'int',
        'verify_num': 'int',
        'repair_priority_list': 'list[RepairPriorityListInfo]'
    }

    attribute_map = {
        'vul_name': 'vul_name',
        'vul_id': 'vul_id',
        'label_list': 'label_list',
        'repair_necessity': 'repair_necessity',
        'severity_level': 'severity_level',
        'host_num': 'host_num',
        'unhandle_host_num': 'unhandle_host_num',
        'scan_time': 'scan_time',
        'solution_detail': 'solution_detail',
        'url': 'url',
        'description': 'description',
        'type': 'type',
        'host_id_list': 'host_id_list',
        'cve_list': 'cve_list',
        'patch_url': 'patch_url',
        'repair_priority': 'repair_priority',
        'hosts_num': 'hosts_num',
        'repair_success_num': 'repair_success_num',
        'fixed_num': 'fixed_num',
        'ignored_num': 'ignored_num',
        'verify_num': 'verify_num',
        'repair_priority_list': 'repair_priority_list'
    }

    def __init__(self, vul_name=None, vul_id=None, label_list=None, repair_necessity=None, severity_level=None, host_num=None, unhandle_host_num=None, scan_time=None, solution_detail=None, url=None, description=None, type=None, host_id_list=None, cve_list=None, patch_url=None, repair_priority=None, hosts_num=None, repair_success_num=None, fixed_num=None, ignored_num=None, verify_num=None, repair_priority_list=None):
        r"""VulInfo

        The model defined in huaweicloud sdk

        :param vul_name: **参数解释**: 漏洞名称 **取值范围**: 字符长度0-256位 
        :type vul_name: str
        :param vul_id: **参数解释**: 漏洞ID **取值范围**: 字符长度0-64位 
        :type vul_id: str
        :param label_list: **参数解释**: 漏洞标签列表 **取值范围**: 不涉及 
        :type label_list: list[str]
        :param repair_necessity: **参数解释**: 漏洞修复的必要性 **取值范围**: - Critical：漏洞cvss评分大于等于9；对应控制台页面的高危 - High：漏洞cvss评分大于等于7，小于9；对应控制台页面的中危 - Medium：漏洞cvss评分大于等于4，小于7；对应控制台页面的中危 - Low：漏洞cvss评分小于4；对应控制台页面的低危 
        :type repair_necessity: str
        :param severity_level: **参数解释**: 漏洞风险级别 **取值范围**: - Critical：漏洞cvss评分大于等于9；对应控制台页面的高危 - High：漏洞cvss评分大于等于7，小于9；对应控制台页面的中危 - Medium：漏洞cvss评分大于等于4，小于7；对应控制台页面的中危 - Low：漏洞cvss评分小于4；对应控制台页面的低危 
        :type severity_level: str
        :param host_num: **参数解释**: 受影响服务器台数 **取值范围**: 取值0-2147483647 
        :type host_num: int
        :param unhandle_host_num: **参数解释**: 未处理主机台数：除已忽略和已修复的主机数量 **取值范围**: 取值0-2147483647 
        :type unhandle_host_num: int
        :param scan_time: **参数解释**: 最近扫描时间，时间戳单位：毫秒 **取值范围**: 取值0-9223372036854775807 
        :type scan_time: int
        :param solution_detail: **参数解释**: 修复漏洞的指导意见 **取值范围**: 字符长度0-65534位 
        :type solution_detail: str
        :param url: **参数解释**: URL链接 **取值范围**: 字符长度0-2083位 
        :type url: str
        :param description: **参数解释**: 漏洞描述 **取值范围**: 字符长度0-65534位 
        :type description: str
        :param type: **参数解释**: 漏洞类型 **取值范围**: - linux_vul：linux漏洞 - windows_vul：windows漏洞 - web_cms：Web-CMS漏洞 - app_vul：应用漏洞 
        :type type: str
        :param host_id_list: **参数解释**: 可处置该漏洞的主机ID列表 **取值范围**: 不涉及 
        :type host_id_list: list[str]
        :param cve_list: **参数解释**: 漏洞关联的cve信息列表 **取值范围**: 不涉及 
        :type cve_list: list[:class:`huaweicloudsdkhss.v5.VulInfoCveList`]
        :param patch_url: **参数解释**: 补丁地址 **取值范围**: 字符长度0-512位 
        :type patch_url: str
        :param repair_priority: **参数解释**: 修复优先级 **取值范围**: - Critical：紧急 - High：高 - Medium：中 - Low：低 
        :type repair_priority: str
        :param hosts_num: 
        :type hosts_num: :class:`huaweicloudsdkhss.v5.VulnerabilityHostNumberInfo`
        :param repair_success_num: **参数解释**: 修复成功次数 **取值范围**: 取值0-1000000 
        :type repair_success_num: int
        :param fixed_num: **参数解释**: 修复数量 **取值范围**: 取值0-1000000 
        :type fixed_num: int
        :param ignored_num: **参数解释**: 忽略数量 **取值范围**: 取值0-1000000 
        :type ignored_num: int
        :param verify_num: **参数解释**: 验证数量 **取值范围**: 取值0-1000000 
        :type verify_num: int
        :param repair_priority_list: **参数解释**: 修复优先级，每个修复优先级对应的主机数量 **取值范围**: 不涉及 
        :type repair_priority_list: list[:class:`huaweicloudsdkhss.v5.RepairPriorityListInfo`]
        """
        
        

        self._vul_name = None
        self._vul_id = None
        self._label_list = None
        self._repair_necessity = None
        self._severity_level = None
        self._host_num = None
        self._unhandle_host_num = None
        self._scan_time = None
        self._solution_detail = None
        self._url = None
        self._description = None
        self._type = None
        self._host_id_list = None
        self._cve_list = None
        self._patch_url = None
        self._repair_priority = None
        self._hosts_num = None
        self._repair_success_num = None
        self._fixed_num = None
        self._ignored_num = None
        self._verify_num = None
        self._repair_priority_list = None
        self.discriminator = None

        if vul_name is not None:
            self.vul_name = vul_name
        if vul_id is not None:
            self.vul_id = vul_id
        if label_list is not None:
            self.label_list = label_list
        if repair_necessity is not None:
            self.repair_necessity = repair_necessity
        if severity_level is not None:
            self.severity_level = severity_level
        if host_num is not None:
            self.host_num = host_num
        if unhandle_host_num is not None:
            self.unhandle_host_num = unhandle_host_num
        if scan_time is not None:
            self.scan_time = scan_time
        if solution_detail is not None:
            self.solution_detail = solution_detail
        if url is not None:
            self.url = url
        if description is not None:
            self.description = description
        if type is not None:
            self.type = type
        if host_id_list is not None:
            self.host_id_list = host_id_list
        if cve_list is not None:
            self.cve_list = cve_list
        if patch_url is not None:
            self.patch_url = patch_url
        if repair_priority is not None:
            self.repair_priority = repair_priority
        if hosts_num is not None:
            self.hosts_num = hosts_num
        if repair_success_num is not None:
            self.repair_success_num = repair_success_num
        if fixed_num is not None:
            self.fixed_num = fixed_num
        if ignored_num is not None:
            self.ignored_num = ignored_num
        if verify_num is not None:
            self.verify_num = verify_num
        if repair_priority_list is not None:
            self.repair_priority_list = repair_priority_list

    @property
    def vul_name(self):
        r"""Gets the vul_name of this VulInfo.

        **参数解释**: 漏洞名称 **取值范围**: 字符长度0-256位 

        :return: The vul_name of this VulInfo.
        :rtype: str
        """
        return self._vul_name

    @vul_name.setter
    def vul_name(self, vul_name):
        r"""Sets the vul_name of this VulInfo.

        **参数解释**: 漏洞名称 **取值范围**: 字符长度0-256位 

        :param vul_name: The vul_name of this VulInfo.
        :type vul_name: str
        """
        self._vul_name = vul_name

    @property
    def vul_id(self):
        r"""Gets the vul_id of this VulInfo.

        **参数解释**: 漏洞ID **取值范围**: 字符长度0-64位 

        :return: The vul_id of this VulInfo.
        :rtype: str
        """
        return self._vul_id

    @vul_id.setter
    def vul_id(self, vul_id):
        r"""Sets the vul_id of this VulInfo.

        **参数解释**: 漏洞ID **取值范围**: 字符长度0-64位 

        :param vul_id: The vul_id of this VulInfo.
        :type vul_id: str
        """
        self._vul_id = vul_id

    @property
    def label_list(self):
        r"""Gets the label_list of this VulInfo.

        **参数解释**: 漏洞标签列表 **取值范围**: 不涉及 

        :return: The label_list of this VulInfo.
        :rtype: list[str]
        """
        return self._label_list

    @label_list.setter
    def label_list(self, label_list):
        r"""Sets the label_list of this VulInfo.

        **参数解释**: 漏洞标签列表 **取值范围**: 不涉及 

        :param label_list: The label_list of this VulInfo.
        :type label_list: list[str]
        """
        self._label_list = label_list

    @property
    def repair_necessity(self):
        r"""Gets the repair_necessity of this VulInfo.

        **参数解释**: 漏洞修复的必要性 **取值范围**: - Critical：漏洞cvss评分大于等于9；对应控制台页面的高危 - High：漏洞cvss评分大于等于7，小于9；对应控制台页面的中危 - Medium：漏洞cvss评分大于等于4，小于7；对应控制台页面的中危 - Low：漏洞cvss评分小于4；对应控制台页面的低危 

        :return: The repair_necessity of this VulInfo.
        :rtype: str
        """
        return self._repair_necessity

    @repair_necessity.setter
    def repair_necessity(self, repair_necessity):
        r"""Sets the repair_necessity of this VulInfo.

        **参数解释**: 漏洞修复的必要性 **取值范围**: - Critical：漏洞cvss评分大于等于9；对应控制台页面的高危 - High：漏洞cvss评分大于等于7，小于9；对应控制台页面的中危 - Medium：漏洞cvss评分大于等于4，小于7；对应控制台页面的中危 - Low：漏洞cvss评分小于4；对应控制台页面的低危 

        :param repair_necessity: The repair_necessity of this VulInfo.
        :type repair_necessity: str
        """
        self._repair_necessity = repair_necessity

    @property
    def severity_level(self):
        r"""Gets the severity_level of this VulInfo.

        **参数解释**: 漏洞风险级别 **取值范围**: - Critical：漏洞cvss评分大于等于9；对应控制台页面的高危 - High：漏洞cvss评分大于等于7，小于9；对应控制台页面的中危 - Medium：漏洞cvss评分大于等于4，小于7；对应控制台页面的中危 - Low：漏洞cvss评分小于4；对应控制台页面的低危 

        :return: The severity_level of this VulInfo.
        :rtype: str
        """
        return self._severity_level

    @severity_level.setter
    def severity_level(self, severity_level):
        r"""Sets the severity_level of this VulInfo.

        **参数解释**: 漏洞风险级别 **取值范围**: - Critical：漏洞cvss评分大于等于9；对应控制台页面的高危 - High：漏洞cvss评分大于等于7，小于9；对应控制台页面的中危 - Medium：漏洞cvss评分大于等于4，小于7；对应控制台页面的中危 - Low：漏洞cvss评分小于4；对应控制台页面的低危 

        :param severity_level: The severity_level of this VulInfo.
        :type severity_level: str
        """
        self._severity_level = severity_level

    @property
    def host_num(self):
        r"""Gets the host_num of this VulInfo.

        **参数解释**: 受影响服务器台数 **取值范围**: 取值0-2147483647 

        :return: The host_num of this VulInfo.
        :rtype: int
        """
        return self._host_num

    @host_num.setter
    def host_num(self, host_num):
        r"""Sets the host_num of this VulInfo.

        **参数解释**: 受影响服务器台数 **取值范围**: 取值0-2147483647 

        :param host_num: The host_num of this VulInfo.
        :type host_num: int
        """
        self._host_num = host_num

    @property
    def unhandle_host_num(self):
        r"""Gets the unhandle_host_num of this VulInfo.

        **参数解释**: 未处理主机台数：除已忽略和已修复的主机数量 **取值范围**: 取值0-2147483647 

        :return: The unhandle_host_num of this VulInfo.
        :rtype: int
        """
        return self._unhandle_host_num

    @unhandle_host_num.setter
    def unhandle_host_num(self, unhandle_host_num):
        r"""Sets the unhandle_host_num of this VulInfo.

        **参数解释**: 未处理主机台数：除已忽略和已修复的主机数量 **取值范围**: 取值0-2147483647 

        :param unhandle_host_num: The unhandle_host_num of this VulInfo.
        :type unhandle_host_num: int
        """
        self._unhandle_host_num = unhandle_host_num

    @property
    def scan_time(self):
        r"""Gets the scan_time of this VulInfo.

        **参数解释**: 最近扫描时间，时间戳单位：毫秒 **取值范围**: 取值0-9223372036854775807 

        :return: The scan_time of this VulInfo.
        :rtype: int
        """
        return self._scan_time

    @scan_time.setter
    def scan_time(self, scan_time):
        r"""Sets the scan_time of this VulInfo.

        **参数解释**: 最近扫描时间，时间戳单位：毫秒 **取值范围**: 取值0-9223372036854775807 

        :param scan_time: The scan_time of this VulInfo.
        :type scan_time: int
        """
        self._scan_time = scan_time

    @property
    def solution_detail(self):
        r"""Gets the solution_detail of this VulInfo.

        **参数解释**: 修复漏洞的指导意见 **取值范围**: 字符长度0-65534位 

        :return: The solution_detail of this VulInfo.
        :rtype: str
        """
        return self._solution_detail

    @solution_detail.setter
    def solution_detail(self, solution_detail):
        r"""Sets the solution_detail of this VulInfo.

        **参数解释**: 修复漏洞的指导意见 **取值范围**: 字符长度0-65534位 

        :param solution_detail: The solution_detail of this VulInfo.
        :type solution_detail: str
        """
        self._solution_detail = solution_detail

    @property
    def url(self):
        r"""Gets the url of this VulInfo.

        **参数解释**: URL链接 **取值范围**: 字符长度0-2083位 

        :return: The url of this VulInfo.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this VulInfo.

        **参数解释**: URL链接 **取值范围**: 字符长度0-2083位 

        :param url: The url of this VulInfo.
        :type url: str
        """
        self._url = url

    @property
    def description(self):
        r"""Gets the description of this VulInfo.

        **参数解释**: 漏洞描述 **取值范围**: 字符长度0-65534位 

        :return: The description of this VulInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this VulInfo.

        **参数解释**: 漏洞描述 **取值范围**: 字符长度0-65534位 

        :param description: The description of this VulInfo.
        :type description: str
        """
        self._description = description

    @property
    def type(self):
        r"""Gets the type of this VulInfo.

        **参数解释**: 漏洞类型 **取值范围**: - linux_vul：linux漏洞 - windows_vul：windows漏洞 - web_cms：Web-CMS漏洞 - app_vul：应用漏洞 

        :return: The type of this VulInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this VulInfo.

        **参数解释**: 漏洞类型 **取值范围**: - linux_vul：linux漏洞 - windows_vul：windows漏洞 - web_cms：Web-CMS漏洞 - app_vul：应用漏洞 

        :param type: The type of this VulInfo.
        :type type: str
        """
        self._type = type

    @property
    def host_id_list(self):
        r"""Gets the host_id_list of this VulInfo.

        **参数解释**: 可处置该漏洞的主机ID列表 **取值范围**: 不涉及 

        :return: The host_id_list of this VulInfo.
        :rtype: list[str]
        """
        return self._host_id_list

    @host_id_list.setter
    def host_id_list(self, host_id_list):
        r"""Sets the host_id_list of this VulInfo.

        **参数解释**: 可处置该漏洞的主机ID列表 **取值范围**: 不涉及 

        :param host_id_list: The host_id_list of this VulInfo.
        :type host_id_list: list[str]
        """
        self._host_id_list = host_id_list

    @property
    def cve_list(self):
        r"""Gets the cve_list of this VulInfo.

        **参数解释**: 漏洞关联的cve信息列表 **取值范围**: 不涉及 

        :return: The cve_list of this VulInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.VulInfoCveList`]
        """
        return self._cve_list

    @cve_list.setter
    def cve_list(self, cve_list):
        r"""Sets the cve_list of this VulInfo.

        **参数解释**: 漏洞关联的cve信息列表 **取值范围**: 不涉及 

        :param cve_list: The cve_list of this VulInfo.
        :type cve_list: list[:class:`huaweicloudsdkhss.v5.VulInfoCveList`]
        """
        self._cve_list = cve_list

    @property
    def patch_url(self):
        r"""Gets the patch_url of this VulInfo.

        **参数解释**: 补丁地址 **取值范围**: 字符长度0-512位 

        :return: The patch_url of this VulInfo.
        :rtype: str
        """
        return self._patch_url

    @patch_url.setter
    def patch_url(self, patch_url):
        r"""Sets the patch_url of this VulInfo.

        **参数解释**: 补丁地址 **取值范围**: 字符长度0-512位 

        :param patch_url: The patch_url of this VulInfo.
        :type patch_url: str
        """
        self._patch_url = patch_url

    @property
    def repair_priority(self):
        r"""Gets the repair_priority of this VulInfo.

        **参数解释**: 修复优先级 **取值范围**: - Critical：紧急 - High：高 - Medium：中 - Low：低 

        :return: The repair_priority of this VulInfo.
        :rtype: str
        """
        return self._repair_priority

    @repair_priority.setter
    def repair_priority(self, repair_priority):
        r"""Sets the repair_priority of this VulInfo.

        **参数解释**: 修复优先级 **取值范围**: - Critical：紧急 - High：高 - Medium：中 - Low：低 

        :param repair_priority: The repair_priority of this VulInfo.
        :type repair_priority: str
        """
        self._repair_priority = repair_priority

    @property
    def hosts_num(self):
        r"""Gets the hosts_num of this VulInfo.

        :return: The hosts_num of this VulInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.VulnerabilityHostNumberInfo`
        """
        return self._hosts_num

    @hosts_num.setter
    def hosts_num(self, hosts_num):
        r"""Sets the hosts_num of this VulInfo.

        :param hosts_num: The hosts_num of this VulInfo.
        :type hosts_num: :class:`huaweicloudsdkhss.v5.VulnerabilityHostNumberInfo`
        """
        self._hosts_num = hosts_num

    @property
    def repair_success_num(self):
        r"""Gets the repair_success_num of this VulInfo.

        **参数解释**: 修复成功次数 **取值范围**: 取值0-1000000 

        :return: The repair_success_num of this VulInfo.
        :rtype: int
        """
        return self._repair_success_num

    @repair_success_num.setter
    def repair_success_num(self, repair_success_num):
        r"""Sets the repair_success_num of this VulInfo.

        **参数解释**: 修复成功次数 **取值范围**: 取值0-1000000 

        :param repair_success_num: The repair_success_num of this VulInfo.
        :type repair_success_num: int
        """
        self._repair_success_num = repair_success_num

    @property
    def fixed_num(self):
        r"""Gets the fixed_num of this VulInfo.

        **参数解释**: 修复数量 **取值范围**: 取值0-1000000 

        :return: The fixed_num of this VulInfo.
        :rtype: int
        """
        return self._fixed_num

    @fixed_num.setter
    def fixed_num(self, fixed_num):
        r"""Sets the fixed_num of this VulInfo.

        **参数解释**: 修复数量 **取值范围**: 取值0-1000000 

        :param fixed_num: The fixed_num of this VulInfo.
        :type fixed_num: int
        """
        self._fixed_num = fixed_num

    @property
    def ignored_num(self):
        r"""Gets the ignored_num of this VulInfo.

        **参数解释**: 忽略数量 **取值范围**: 取值0-1000000 

        :return: The ignored_num of this VulInfo.
        :rtype: int
        """
        return self._ignored_num

    @ignored_num.setter
    def ignored_num(self, ignored_num):
        r"""Sets the ignored_num of this VulInfo.

        **参数解释**: 忽略数量 **取值范围**: 取值0-1000000 

        :param ignored_num: The ignored_num of this VulInfo.
        :type ignored_num: int
        """
        self._ignored_num = ignored_num

    @property
    def verify_num(self):
        r"""Gets the verify_num of this VulInfo.

        **参数解释**: 验证数量 **取值范围**: 取值0-1000000 

        :return: The verify_num of this VulInfo.
        :rtype: int
        """
        return self._verify_num

    @verify_num.setter
    def verify_num(self, verify_num):
        r"""Sets the verify_num of this VulInfo.

        **参数解释**: 验证数量 **取值范围**: 取值0-1000000 

        :param verify_num: The verify_num of this VulInfo.
        :type verify_num: int
        """
        self._verify_num = verify_num

    @property
    def repair_priority_list(self):
        r"""Gets the repair_priority_list of this VulInfo.

        **参数解释**: 修复优先级，每个修复优先级对应的主机数量 **取值范围**: 不涉及 

        :return: The repair_priority_list of this VulInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.RepairPriorityListInfo`]
        """
        return self._repair_priority_list

    @repair_priority_list.setter
    def repair_priority_list(self, repair_priority_list):
        r"""Sets the repair_priority_list of this VulInfo.

        **参数解释**: 修复优先级，每个修复优先级对应的主机数量 **取值范围**: 不涉及 

        :param repair_priority_list: The repair_priority_list of this VulInfo.
        :type repair_priority_list: list[:class:`huaweicloudsdkhss.v5.RepairPriorityListInfo`]
        """
        self._repair_priority_list = repair_priority_list

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
        if not isinstance(other, VulInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
