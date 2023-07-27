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
        'verify_num': 'int'
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
        'verify_num': 'verify_num'
    }

    def __init__(self, vul_name=None, vul_id=None, label_list=None, repair_necessity=None, severity_level=None, host_num=None, unhandle_host_num=None, scan_time=None, solution_detail=None, url=None, description=None, type=None, host_id_list=None, cve_list=None, patch_url=None, repair_priority=None, hosts_num=None, repair_success_num=None, fixed_num=None, ignored_num=None, verify_num=None):
        """VulInfo

        The model defined in huaweicloud sdk

        :param vul_name: 漏洞名称
        :type vul_name: str
        :param vul_id: 漏洞ID
        :type vul_id: str
        :param label_list: 漏洞标签
        :type label_list: list[str]
        :param repair_necessity: 修复必要性
        :type repair_necessity: str
        :param severity_level: 漏洞级别
        :type severity_level: str
        :param host_num: 受影响服务器台数
        :type host_num: int
        :param unhandle_host_num: 未处理服务器台数
        :type unhandle_host_num: int
        :param scan_time: 最近扫描时间
        :type scan_time: int
        :param solution_detail: 解决方案
        :type solution_detail: str
        :param url: URL链接
        :type url: str
        :param description: 漏洞描述
        :type description: str
        :param type: 漏洞类型，包含如下：   -linux_vul : linux漏洞   -windows_vul : windows漏洞   -web_cms : Web-CMS漏洞   -app_vul : 应用漏洞
        :type type: str
        :param host_id_list: 主机列表
        :type host_id_list: list[str]
        :param cve_list: CVE列表
        :type cve_list: list[:class:`huaweicloudsdkhss.v5.VulInfoCveList`]
        :param patch_url: 补丁地址
        :type patch_url: str
        :param repair_priority: 修复优先级 Critical 紧急 High 高 Medium 中 Low 低
        :type repair_priority: str
        :param hosts_num: 
        :type hosts_num: :class:`huaweicloudsdkhss.v5.VulnerabilityHostNumberInfo`
        :param repair_success_num: 修复成功次数
        :type repair_success_num: int
        :param fixed_num: 修复数量
        :type fixed_num: int
        :param ignored_num: 忽略数量
        :type ignored_num: int
        :param verify_num: 验证数量
        :type verify_num: int
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

    @property
    def vul_name(self):
        """Gets the vul_name of this VulInfo.

        漏洞名称

        :return: The vul_name of this VulInfo.
        :rtype: str
        """
        return self._vul_name

    @vul_name.setter
    def vul_name(self, vul_name):
        """Sets the vul_name of this VulInfo.

        漏洞名称

        :param vul_name: The vul_name of this VulInfo.
        :type vul_name: str
        """
        self._vul_name = vul_name

    @property
    def vul_id(self):
        """Gets the vul_id of this VulInfo.

        漏洞ID

        :return: The vul_id of this VulInfo.
        :rtype: str
        """
        return self._vul_id

    @vul_id.setter
    def vul_id(self, vul_id):
        """Sets the vul_id of this VulInfo.

        漏洞ID

        :param vul_id: The vul_id of this VulInfo.
        :type vul_id: str
        """
        self._vul_id = vul_id

    @property
    def label_list(self):
        """Gets the label_list of this VulInfo.

        漏洞标签

        :return: The label_list of this VulInfo.
        :rtype: list[str]
        """
        return self._label_list

    @label_list.setter
    def label_list(self, label_list):
        """Sets the label_list of this VulInfo.

        漏洞标签

        :param label_list: The label_list of this VulInfo.
        :type label_list: list[str]
        """
        self._label_list = label_list

    @property
    def repair_necessity(self):
        """Gets the repair_necessity of this VulInfo.

        修复必要性

        :return: The repair_necessity of this VulInfo.
        :rtype: str
        """
        return self._repair_necessity

    @repair_necessity.setter
    def repair_necessity(self, repair_necessity):
        """Sets the repair_necessity of this VulInfo.

        修复必要性

        :param repair_necessity: The repair_necessity of this VulInfo.
        :type repair_necessity: str
        """
        self._repair_necessity = repair_necessity

    @property
    def severity_level(self):
        """Gets the severity_level of this VulInfo.

        漏洞级别

        :return: The severity_level of this VulInfo.
        :rtype: str
        """
        return self._severity_level

    @severity_level.setter
    def severity_level(self, severity_level):
        """Sets the severity_level of this VulInfo.

        漏洞级别

        :param severity_level: The severity_level of this VulInfo.
        :type severity_level: str
        """
        self._severity_level = severity_level

    @property
    def host_num(self):
        """Gets the host_num of this VulInfo.

        受影响服务器台数

        :return: The host_num of this VulInfo.
        :rtype: int
        """
        return self._host_num

    @host_num.setter
    def host_num(self, host_num):
        """Sets the host_num of this VulInfo.

        受影响服务器台数

        :param host_num: The host_num of this VulInfo.
        :type host_num: int
        """
        self._host_num = host_num

    @property
    def unhandle_host_num(self):
        """Gets the unhandle_host_num of this VulInfo.

        未处理服务器台数

        :return: The unhandle_host_num of this VulInfo.
        :rtype: int
        """
        return self._unhandle_host_num

    @unhandle_host_num.setter
    def unhandle_host_num(self, unhandle_host_num):
        """Sets the unhandle_host_num of this VulInfo.

        未处理服务器台数

        :param unhandle_host_num: The unhandle_host_num of this VulInfo.
        :type unhandle_host_num: int
        """
        self._unhandle_host_num = unhandle_host_num

    @property
    def scan_time(self):
        """Gets the scan_time of this VulInfo.

        最近扫描时间

        :return: The scan_time of this VulInfo.
        :rtype: int
        """
        return self._scan_time

    @scan_time.setter
    def scan_time(self, scan_time):
        """Sets the scan_time of this VulInfo.

        最近扫描时间

        :param scan_time: The scan_time of this VulInfo.
        :type scan_time: int
        """
        self._scan_time = scan_time

    @property
    def solution_detail(self):
        """Gets the solution_detail of this VulInfo.

        解决方案

        :return: The solution_detail of this VulInfo.
        :rtype: str
        """
        return self._solution_detail

    @solution_detail.setter
    def solution_detail(self, solution_detail):
        """Sets the solution_detail of this VulInfo.

        解决方案

        :param solution_detail: The solution_detail of this VulInfo.
        :type solution_detail: str
        """
        self._solution_detail = solution_detail

    @property
    def url(self):
        """Gets the url of this VulInfo.

        URL链接

        :return: The url of this VulInfo.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this VulInfo.

        URL链接

        :param url: The url of this VulInfo.
        :type url: str
        """
        self._url = url

    @property
    def description(self):
        """Gets the description of this VulInfo.

        漏洞描述

        :return: The description of this VulInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VulInfo.

        漏洞描述

        :param description: The description of this VulInfo.
        :type description: str
        """
        self._description = description

    @property
    def type(self):
        """Gets the type of this VulInfo.

        漏洞类型，包含如下：   -linux_vul : linux漏洞   -windows_vul : windows漏洞   -web_cms : Web-CMS漏洞   -app_vul : 应用漏洞

        :return: The type of this VulInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VulInfo.

        漏洞类型，包含如下：   -linux_vul : linux漏洞   -windows_vul : windows漏洞   -web_cms : Web-CMS漏洞   -app_vul : 应用漏洞

        :param type: The type of this VulInfo.
        :type type: str
        """
        self._type = type

    @property
    def host_id_list(self):
        """Gets the host_id_list of this VulInfo.

        主机列表

        :return: The host_id_list of this VulInfo.
        :rtype: list[str]
        """
        return self._host_id_list

    @host_id_list.setter
    def host_id_list(self, host_id_list):
        """Sets the host_id_list of this VulInfo.

        主机列表

        :param host_id_list: The host_id_list of this VulInfo.
        :type host_id_list: list[str]
        """
        self._host_id_list = host_id_list

    @property
    def cve_list(self):
        """Gets the cve_list of this VulInfo.

        CVE列表

        :return: The cve_list of this VulInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.VulInfoCveList`]
        """
        return self._cve_list

    @cve_list.setter
    def cve_list(self, cve_list):
        """Sets the cve_list of this VulInfo.

        CVE列表

        :param cve_list: The cve_list of this VulInfo.
        :type cve_list: list[:class:`huaweicloudsdkhss.v5.VulInfoCveList`]
        """
        self._cve_list = cve_list

    @property
    def patch_url(self):
        """Gets the patch_url of this VulInfo.

        补丁地址

        :return: The patch_url of this VulInfo.
        :rtype: str
        """
        return self._patch_url

    @patch_url.setter
    def patch_url(self, patch_url):
        """Sets the patch_url of this VulInfo.

        补丁地址

        :param patch_url: The patch_url of this VulInfo.
        :type patch_url: str
        """
        self._patch_url = patch_url

    @property
    def repair_priority(self):
        """Gets the repair_priority of this VulInfo.

        修复优先级 Critical 紧急 High 高 Medium 中 Low 低

        :return: The repair_priority of this VulInfo.
        :rtype: str
        """
        return self._repair_priority

    @repair_priority.setter
    def repair_priority(self, repair_priority):
        """Sets the repair_priority of this VulInfo.

        修复优先级 Critical 紧急 High 高 Medium 中 Low 低

        :param repair_priority: The repair_priority of this VulInfo.
        :type repair_priority: str
        """
        self._repair_priority = repair_priority

    @property
    def hosts_num(self):
        """Gets the hosts_num of this VulInfo.

        :return: The hosts_num of this VulInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.VulnerabilityHostNumberInfo`
        """
        return self._hosts_num

    @hosts_num.setter
    def hosts_num(self, hosts_num):
        """Sets the hosts_num of this VulInfo.

        :param hosts_num: The hosts_num of this VulInfo.
        :type hosts_num: :class:`huaweicloudsdkhss.v5.VulnerabilityHostNumberInfo`
        """
        self._hosts_num = hosts_num

    @property
    def repair_success_num(self):
        """Gets the repair_success_num of this VulInfo.

        修复成功次数

        :return: The repair_success_num of this VulInfo.
        :rtype: int
        """
        return self._repair_success_num

    @repair_success_num.setter
    def repair_success_num(self, repair_success_num):
        """Sets the repair_success_num of this VulInfo.

        修复成功次数

        :param repair_success_num: The repair_success_num of this VulInfo.
        :type repair_success_num: int
        """
        self._repair_success_num = repair_success_num

    @property
    def fixed_num(self):
        """Gets the fixed_num of this VulInfo.

        修复数量

        :return: The fixed_num of this VulInfo.
        :rtype: int
        """
        return self._fixed_num

    @fixed_num.setter
    def fixed_num(self, fixed_num):
        """Sets the fixed_num of this VulInfo.

        修复数量

        :param fixed_num: The fixed_num of this VulInfo.
        :type fixed_num: int
        """
        self._fixed_num = fixed_num

    @property
    def ignored_num(self):
        """Gets the ignored_num of this VulInfo.

        忽略数量

        :return: The ignored_num of this VulInfo.
        :rtype: int
        """
        return self._ignored_num

    @ignored_num.setter
    def ignored_num(self, ignored_num):
        """Sets the ignored_num of this VulInfo.

        忽略数量

        :param ignored_num: The ignored_num of this VulInfo.
        :type ignored_num: int
        """
        self._ignored_num = ignored_num

    @property
    def verify_num(self):
        """Gets the verify_num of this VulInfo.

        验证数量

        :return: The verify_num of this VulInfo.
        :rtype: int
        """
        return self._verify_num

    @verify_num.setter
    def verify_num(self, verify_num):
        """Sets the verify_num of this VulInfo.

        验证数量

        :param verify_num: The verify_num of this VulInfo.
        :type verify_num: int
        """
        self._verify_num = verify_num

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
