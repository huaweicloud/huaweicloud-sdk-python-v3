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
        'support_restore': 'bool'
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
        'support_restore': 'support_restore'
    }

    def __init__(self, vul_name=None, vul_id=None, label_list=None, repair_necessity=None, scan_time=None, type=None, app_list=None, severity_level=None, solution_detail=None, url=None, description=None, repair_cmd=None, status=None, repair_success_num=None, cve_list=None, is_affect_business=None, first_scan_time=None, app_name=None, app_version=None, app_path=None, version=None, support_restore=None):
        """HostVulInfo

        The model defined in huaweicloud sdk

        :param vul_name: 漏洞名称
        :type vul_name: str
        :param vul_id: 漏洞ID
        :type vul_id: str
        :param label_list: 漏洞标签列表
        :type label_list: list[str]
        :param repair_necessity: 修复紧急度，包括如下：   - immediate_repair : 尽快修复   - delay_repair : 延后修复   - not_needed_repair : 暂可不修复
        :type repair_necessity: str
        :param scan_time: 最近扫描时间
        :type scan_time: int
        :param type: 漏洞类型，包含如下：   -linux_vul : linux漏洞   -windows_vul : windows漏洞   -web_cms : Web-CMS漏洞   -app_vul : 应用漏洞
        :type type: str
        :param app_list: 服务器上受该漏洞影响的软件列表
        :type app_list: list[:class:`huaweicloudsdkhss.v5.HostVulInfoAppList`]
        :param severity_level: 危险程度   - Critical : 漏洞cvss评分大于等于9；对应控制台页面的高危   - High : 漏洞cvss评分大于等于7，小于9；对应控制台页面的中危   - Medium : 漏洞cvss评分大于等于4，小于7；对应控制台页面的中危   - Low : 漏洞cvss评分小于4；对应控制台页面的低危
        :type severity_level: str
        :param solution_detail: 解决方案
        :type solution_detail: str
        :param url: URL链接
        :type url: str
        :param description: 漏洞描述
        :type description: str
        :param repair_cmd: 修复命令行
        :type repair_cmd: str
        :param status: 漏洞状态   - vul_status_unfix : 未处理   - vul_status_ignored : 已忽略   - vul_status_verified : 验证中   - vul_status_fixing : 修复中   - vul_status_fixed : 修复成功   - vul_status_reboot : 修复成功待重启   - vul_status_failed : 修复失败   - vul_status_fix_after_reboot : 请重启主机再次修复
        :type status: str
        :param repair_success_num: HSS全网修复该漏洞的次数
        :type repair_success_num: int
        :param cve_list: CVE列表
        :type cve_list: list[:class:`huaweicloudsdkhss.v5.HostVulInfoCveList`]
        :param is_affect_business: 是否影响业务
        :type is_affect_business: bool
        :param first_scan_time: 首次扫描时间
        :type first_scan_time: int
        :param app_name: 软件名称
        :type app_name: str
        :param app_version: 软件版本
        :type app_version: str
        :param app_path: 软件路径
        :type app_path: str
        :param version: 主机配额
        :type version: str
        :param support_restore: 是否可以回滚到修复漏洞时创建的备份
        :type support_restore: bool
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

    @property
    def vul_name(self):
        """Gets the vul_name of this HostVulInfo.

        漏洞名称

        :return: The vul_name of this HostVulInfo.
        :rtype: str
        """
        return self._vul_name

    @vul_name.setter
    def vul_name(self, vul_name):
        """Sets the vul_name of this HostVulInfo.

        漏洞名称

        :param vul_name: The vul_name of this HostVulInfo.
        :type vul_name: str
        """
        self._vul_name = vul_name

    @property
    def vul_id(self):
        """Gets the vul_id of this HostVulInfo.

        漏洞ID

        :return: The vul_id of this HostVulInfo.
        :rtype: str
        """
        return self._vul_id

    @vul_id.setter
    def vul_id(self, vul_id):
        """Sets the vul_id of this HostVulInfo.

        漏洞ID

        :param vul_id: The vul_id of this HostVulInfo.
        :type vul_id: str
        """
        self._vul_id = vul_id

    @property
    def label_list(self):
        """Gets the label_list of this HostVulInfo.

        漏洞标签列表

        :return: The label_list of this HostVulInfo.
        :rtype: list[str]
        """
        return self._label_list

    @label_list.setter
    def label_list(self, label_list):
        """Sets the label_list of this HostVulInfo.

        漏洞标签列表

        :param label_list: The label_list of this HostVulInfo.
        :type label_list: list[str]
        """
        self._label_list = label_list

    @property
    def repair_necessity(self):
        """Gets the repair_necessity of this HostVulInfo.

        修复紧急度，包括如下：   - immediate_repair : 尽快修复   - delay_repair : 延后修复   - not_needed_repair : 暂可不修复

        :return: The repair_necessity of this HostVulInfo.
        :rtype: str
        """
        return self._repair_necessity

    @repair_necessity.setter
    def repair_necessity(self, repair_necessity):
        """Sets the repair_necessity of this HostVulInfo.

        修复紧急度，包括如下：   - immediate_repair : 尽快修复   - delay_repair : 延后修复   - not_needed_repair : 暂可不修复

        :param repair_necessity: The repair_necessity of this HostVulInfo.
        :type repair_necessity: str
        """
        self._repair_necessity = repair_necessity

    @property
    def scan_time(self):
        """Gets the scan_time of this HostVulInfo.

        最近扫描时间

        :return: The scan_time of this HostVulInfo.
        :rtype: int
        """
        return self._scan_time

    @scan_time.setter
    def scan_time(self, scan_time):
        """Sets the scan_time of this HostVulInfo.

        最近扫描时间

        :param scan_time: The scan_time of this HostVulInfo.
        :type scan_time: int
        """
        self._scan_time = scan_time

    @property
    def type(self):
        """Gets the type of this HostVulInfo.

        漏洞类型，包含如下：   -linux_vul : linux漏洞   -windows_vul : windows漏洞   -web_cms : Web-CMS漏洞   -app_vul : 应用漏洞

        :return: The type of this HostVulInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this HostVulInfo.

        漏洞类型，包含如下：   -linux_vul : linux漏洞   -windows_vul : windows漏洞   -web_cms : Web-CMS漏洞   -app_vul : 应用漏洞

        :param type: The type of this HostVulInfo.
        :type type: str
        """
        self._type = type

    @property
    def app_list(self):
        """Gets the app_list of this HostVulInfo.

        服务器上受该漏洞影响的软件列表

        :return: The app_list of this HostVulInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.HostVulInfoAppList`]
        """
        return self._app_list

    @app_list.setter
    def app_list(self, app_list):
        """Sets the app_list of this HostVulInfo.

        服务器上受该漏洞影响的软件列表

        :param app_list: The app_list of this HostVulInfo.
        :type app_list: list[:class:`huaweicloudsdkhss.v5.HostVulInfoAppList`]
        """
        self._app_list = app_list

    @property
    def severity_level(self):
        """Gets the severity_level of this HostVulInfo.

        危险程度   - Critical : 漏洞cvss评分大于等于9；对应控制台页面的高危   - High : 漏洞cvss评分大于等于7，小于9；对应控制台页面的中危   - Medium : 漏洞cvss评分大于等于4，小于7；对应控制台页面的中危   - Low : 漏洞cvss评分小于4；对应控制台页面的低危

        :return: The severity_level of this HostVulInfo.
        :rtype: str
        """
        return self._severity_level

    @severity_level.setter
    def severity_level(self, severity_level):
        """Sets the severity_level of this HostVulInfo.

        危险程度   - Critical : 漏洞cvss评分大于等于9；对应控制台页面的高危   - High : 漏洞cvss评分大于等于7，小于9；对应控制台页面的中危   - Medium : 漏洞cvss评分大于等于4，小于7；对应控制台页面的中危   - Low : 漏洞cvss评分小于4；对应控制台页面的低危

        :param severity_level: The severity_level of this HostVulInfo.
        :type severity_level: str
        """
        self._severity_level = severity_level

    @property
    def solution_detail(self):
        """Gets the solution_detail of this HostVulInfo.

        解决方案

        :return: The solution_detail of this HostVulInfo.
        :rtype: str
        """
        return self._solution_detail

    @solution_detail.setter
    def solution_detail(self, solution_detail):
        """Sets the solution_detail of this HostVulInfo.

        解决方案

        :param solution_detail: The solution_detail of this HostVulInfo.
        :type solution_detail: str
        """
        self._solution_detail = solution_detail

    @property
    def url(self):
        """Gets the url of this HostVulInfo.

        URL链接

        :return: The url of this HostVulInfo.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this HostVulInfo.

        URL链接

        :param url: The url of this HostVulInfo.
        :type url: str
        """
        self._url = url

    @property
    def description(self):
        """Gets the description of this HostVulInfo.

        漏洞描述

        :return: The description of this HostVulInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this HostVulInfo.

        漏洞描述

        :param description: The description of this HostVulInfo.
        :type description: str
        """
        self._description = description

    @property
    def repair_cmd(self):
        """Gets the repair_cmd of this HostVulInfo.

        修复命令行

        :return: The repair_cmd of this HostVulInfo.
        :rtype: str
        """
        return self._repair_cmd

    @repair_cmd.setter
    def repair_cmd(self, repair_cmd):
        """Sets the repair_cmd of this HostVulInfo.

        修复命令行

        :param repair_cmd: The repair_cmd of this HostVulInfo.
        :type repair_cmd: str
        """
        self._repair_cmd = repair_cmd

    @property
    def status(self):
        """Gets the status of this HostVulInfo.

        漏洞状态   - vul_status_unfix : 未处理   - vul_status_ignored : 已忽略   - vul_status_verified : 验证中   - vul_status_fixing : 修复中   - vul_status_fixed : 修复成功   - vul_status_reboot : 修复成功待重启   - vul_status_failed : 修复失败   - vul_status_fix_after_reboot : 请重启主机再次修复

        :return: The status of this HostVulInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this HostVulInfo.

        漏洞状态   - vul_status_unfix : 未处理   - vul_status_ignored : 已忽略   - vul_status_verified : 验证中   - vul_status_fixing : 修复中   - vul_status_fixed : 修复成功   - vul_status_reboot : 修复成功待重启   - vul_status_failed : 修复失败   - vul_status_fix_after_reboot : 请重启主机再次修复

        :param status: The status of this HostVulInfo.
        :type status: str
        """
        self._status = status

    @property
    def repair_success_num(self):
        """Gets the repair_success_num of this HostVulInfo.

        HSS全网修复该漏洞的次数

        :return: The repair_success_num of this HostVulInfo.
        :rtype: int
        """
        return self._repair_success_num

    @repair_success_num.setter
    def repair_success_num(self, repair_success_num):
        """Sets the repair_success_num of this HostVulInfo.

        HSS全网修复该漏洞的次数

        :param repair_success_num: The repair_success_num of this HostVulInfo.
        :type repair_success_num: int
        """
        self._repair_success_num = repair_success_num

    @property
    def cve_list(self):
        """Gets the cve_list of this HostVulInfo.

        CVE列表

        :return: The cve_list of this HostVulInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.HostVulInfoCveList`]
        """
        return self._cve_list

    @cve_list.setter
    def cve_list(self, cve_list):
        """Sets the cve_list of this HostVulInfo.

        CVE列表

        :param cve_list: The cve_list of this HostVulInfo.
        :type cve_list: list[:class:`huaweicloudsdkhss.v5.HostVulInfoCveList`]
        """
        self._cve_list = cve_list

    @property
    def is_affect_business(self):
        """Gets the is_affect_business of this HostVulInfo.

        是否影响业务

        :return: The is_affect_business of this HostVulInfo.
        :rtype: bool
        """
        return self._is_affect_business

    @is_affect_business.setter
    def is_affect_business(self, is_affect_business):
        """Sets the is_affect_business of this HostVulInfo.

        是否影响业务

        :param is_affect_business: The is_affect_business of this HostVulInfo.
        :type is_affect_business: bool
        """
        self._is_affect_business = is_affect_business

    @property
    def first_scan_time(self):
        """Gets the first_scan_time of this HostVulInfo.

        首次扫描时间

        :return: The first_scan_time of this HostVulInfo.
        :rtype: int
        """
        return self._first_scan_time

    @first_scan_time.setter
    def first_scan_time(self, first_scan_time):
        """Sets the first_scan_time of this HostVulInfo.

        首次扫描时间

        :param first_scan_time: The first_scan_time of this HostVulInfo.
        :type first_scan_time: int
        """
        self._first_scan_time = first_scan_time

    @property
    def app_name(self):
        """Gets the app_name of this HostVulInfo.

        软件名称

        :return: The app_name of this HostVulInfo.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this HostVulInfo.

        软件名称

        :param app_name: The app_name of this HostVulInfo.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def app_version(self):
        """Gets the app_version of this HostVulInfo.

        软件版本

        :return: The app_version of this HostVulInfo.
        :rtype: str
        """
        return self._app_version

    @app_version.setter
    def app_version(self, app_version):
        """Sets the app_version of this HostVulInfo.

        软件版本

        :param app_version: The app_version of this HostVulInfo.
        :type app_version: str
        """
        self._app_version = app_version

    @property
    def app_path(self):
        """Gets the app_path of this HostVulInfo.

        软件路径

        :return: The app_path of this HostVulInfo.
        :rtype: str
        """
        return self._app_path

    @app_path.setter
    def app_path(self, app_path):
        """Sets the app_path of this HostVulInfo.

        软件路径

        :param app_path: The app_path of this HostVulInfo.
        :type app_path: str
        """
        self._app_path = app_path

    @property
    def version(self):
        """Gets the version of this HostVulInfo.

        主机配额

        :return: The version of this HostVulInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this HostVulInfo.

        主机配额

        :param version: The version of this HostVulInfo.
        :type version: str
        """
        self._version = version

    @property
    def support_restore(self):
        """Gets the support_restore of this HostVulInfo.

        是否可以回滚到修复漏洞时创建的备份

        :return: The support_restore of this HostVulInfo.
        :rtype: bool
        """
        return self._support_restore

    @support_restore.setter
    def support_restore(self, support_restore):
        """Sets the support_restore of this HostVulInfo.

        是否可以回滚到修复漏洞时创建的备份

        :param support_restore: The support_restore of this HostVulInfo.
        :type support_restore: bool
        """
        self._support_restore = support_restore

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
