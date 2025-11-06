# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UrgentVulInfo:

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
        'hosts_num': 'VulnerabilityHostNumberInfo',
        'scan_time': 'int',
        'publish_time': 'int',
        'solution_detail': 'str',
        'description': 'str',
        'scan_status': 'str',
        'severity_level': 'str',
        'scanning_host_num': 'int',
        'success_host_num': 'int',
        'failed_host_num': 'int'
    }

    attribute_map = {
        'vul_name': 'vul_name',
        'vul_id': 'vul_id',
        'label_list': 'label_list',
        'hosts_num': 'hosts_num',
        'scan_time': 'scan_time',
        'publish_time': 'publish_time',
        'solution_detail': 'solution_detail',
        'description': 'description',
        'scan_status': 'scan_status',
        'severity_level': 'severity_level',
        'scanning_host_num': 'scanning_host_num',
        'success_host_num': 'success_host_num',
        'failed_host_num': 'failed_host_num'
    }

    def __init__(self, vul_name=None, vul_id=None, label_list=None, hosts_num=None, scan_time=None, publish_time=None, solution_detail=None, description=None, scan_status=None, severity_level=None, scanning_host_num=None, success_host_num=None, failed_host_num=None):
        r"""UrgentVulInfo

        The model defined in huaweicloud sdk

        :param vul_name: **参数解释**： 漏洞名称 **取值范围**： 字符长度0-256位 
        :type vul_name: str
        :param vul_id: **参数解释**： 漏洞ID **取值范围**： 字符长度0-64位 
        :type vul_id: str
        :param label_list: **参数解释**： 漏洞标签 **取值范围**: 最小值0，最大值2147483647 
        :type label_list: list[str]
        :param hosts_num: 
        :type hosts_num: :class:`huaweicloudsdkhss.v5.VulnerabilityHostNumberInfo`
        :param scan_time: **参数解释**： 最近扫描时间 **取值范围**： 字符长度0-9223372036854775807 
        :type scan_time: int
        :param publish_time: **参数解释**： 漏洞披露时间 **取值范围**： 字符长度0-9223372036854775807 
        :type publish_time: int
        :param solution_detail: **参数解释**： 解决方案 **取值范围**： 字符长度0-65534位 
        :type solution_detail: str
        :param description: **参数解释**： 漏洞描述 **取值范围**： 字符长度0-64位 
        :type description: str
        :param scan_status: **参数解释**： 漏洞扫描状态 **约束限制**: 不涉及 **取值范围**： - never_scan : 未扫描 - scanning : 扫描中 - finished : 扫描完成  **默认取值**: 不涉及 
        :type scan_status: str
        :param severity_level: **参数解释**： 危险程度 **约束限制**: 不涉及 **取值范围**： - Critical：漏洞cvss评分大于等于9；对应控制台页面的高危 - High：漏洞cvss评分大于等于7，小于9；对应控制台页面的中危 - Medium：漏洞cvss评分大于等于4，小于7；对应控制台页面的中危 - Low：漏洞cvss评分小于4；对应控制台页面的低危  **默认取值**: 不涉及 
        :type severity_level: str
        :param scanning_host_num: **参数解释**： 处于扫描中状态的主机数量 **取值范围**： 字符长度0-2147483647 
        :type scanning_host_num: int
        :param success_host_num: **参数解释**： 已扫描成功的主机数量 **取值范围**： 字符长度0-2147483647 
        :type success_host_num: int
        :param failed_host_num: **参数解释**： 已扫描失败的主机数量 **取值范围**： 字符长度0-2147483647 
        :type failed_host_num: int
        """
        
        

        self._vul_name = None
        self._vul_id = None
        self._label_list = None
        self._hosts_num = None
        self._scan_time = None
        self._publish_time = None
        self._solution_detail = None
        self._description = None
        self._scan_status = None
        self._severity_level = None
        self._scanning_host_num = None
        self._success_host_num = None
        self._failed_host_num = None
        self.discriminator = None

        if vul_name is not None:
            self.vul_name = vul_name
        if vul_id is not None:
            self.vul_id = vul_id
        if label_list is not None:
            self.label_list = label_list
        if hosts_num is not None:
            self.hosts_num = hosts_num
        if scan_time is not None:
            self.scan_time = scan_time
        if publish_time is not None:
            self.publish_time = publish_time
        if solution_detail is not None:
            self.solution_detail = solution_detail
        if description is not None:
            self.description = description
        if scan_status is not None:
            self.scan_status = scan_status
        if severity_level is not None:
            self.severity_level = severity_level
        if scanning_host_num is not None:
            self.scanning_host_num = scanning_host_num
        if success_host_num is not None:
            self.success_host_num = success_host_num
        if failed_host_num is not None:
            self.failed_host_num = failed_host_num

    @property
    def vul_name(self):
        r"""Gets the vul_name of this UrgentVulInfo.

        **参数解释**： 漏洞名称 **取值范围**： 字符长度0-256位 

        :return: The vul_name of this UrgentVulInfo.
        :rtype: str
        """
        return self._vul_name

    @vul_name.setter
    def vul_name(self, vul_name):
        r"""Sets the vul_name of this UrgentVulInfo.

        **参数解释**： 漏洞名称 **取值范围**： 字符长度0-256位 

        :param vul_name: The vul_name of this UrgentVulInfo.
        :type vul_name: str
        """
        self._vul_name = vul_name

    @property
    def vul_id(self):
        r"""Gets the vul_id of this UrgentVulInfo.

        **参数解释**： 漏洞ID **取值范围**： 字符长度0-64位 

        :return: The vul_id of this UrgentVulInfo.
        :rtype: str
        """
        return self._vul_id

    @vul_id.setter
    def vul_id(self, vul_id):
        r"""Sets the vul_id of this UrgentVulInfo.

        **参数解释**： 漏洞ID **取值范围**： 字符长度0-64位 

        :param vul_id: The vul_id of this UrgentVulInfo.
        :type vul_id: str
        """
        self._vul_id = vul_id

    @property
    def label_list(self):
        r"""Gets the label_list of this UrgentVulInfo.

        **参数解释**： 漏洞标签 **取值范围**: 最小值0，最大值2147483647 

        :return: The label_list of this UrgentVulInfo.
        :rtype: list[str]
        """
        return self._label_list

    @label_list.setter
    def label_list(self, label_list):
        r"""Sets the label_list of this UrgentVulInfo.

        **参数解释**： 漏洞标签 **取值范围**: 最小值0，最大值2147483647 

        :param label_list: The label_list of this UrgentVulInfo.
        :type label_list: list[str]
        """
        self._label_list = label_list

    @property
    def hosts_num(self):
        r"""Gets the hosts_num of this UrgentVulInfo.

        :return: The hosts_num of this UrgentVulInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.VulnerabilityHostNumberInfo`
        """
        return self._hosts_num

    @hosts_num.setter
    def hosts_num(self, hosts_num):
        r"""Sets the hosts_num of this UrgentVulInfo.

        :param hosts_num: The hosts_num of this UrgentVulInfo.
        :type hosts_num: :class:`huaweicloudsdkhss.v5.VulnerabilityHostNumberInfo`
        """
        self._hosts_num = hosts_num

    @property
    def scan_time(self):
        r"""Gets the scan_time of this UrgentVulInfo.

        **参数解释**： 最近扫描时间 **取值范围**： 字符长度0-9223372036854775807 

        :return: The scan_time of this UrgentVulInfo.
        :rtype: int
        """
        return self._scan_time

    @scan_time.setter
    def scan_time(self, scan_time):
        r"""Sets the scan_time of this UrgentVulInfo.

        **参数解释**： 最近扫描时间 **取值范围**： 字符长度0-9223372036854775807 

        :param scan_time: The scan_time of this UrgentVulInfo.
        :type scan_time: int
        """
        self._scan_time = scan_time

    @property
    def publish_time(self):
        r"""Gets the publish_time of this UrgentVulInfo.

        **参数解释**： 漏洞披露时间 **取值范围**： 字符长度0-9223372036854775807 

        :return: The publish_time of this UrgentVulInfo.
        :rtype: int
        """
        return self._publish_time

    @publish_time.setter
    def publish_time(self, publish_time):
        r"""Sets the publish_time of this UrgentVulInfo.

        **参数解释**： 漏洞披露时间 **取值范围**： 字符长度0-9223372036854775807 

        :param publish_time: The publish_time of this UrgentVulInfo.
        :type publish_time: int
        """
        self._publish_time = publish_time

    @property
    def solution_detail(self):
        r"""Gets the solution_detail of this UrgentVulInfo.

        **参数解释**： 解决方案 **取值范围**： 字符长度0-65534位 

        :return: The solution_detail of this UrgentVulInfo.
        :rtype: str
        """
        return self._solution_detail

    @solution_detail.setter
    def solution_detail(self, solution_detail):
        r"""Sets the solution_detail of this UrgentVulInfo.

        **参数解释**： 解决方案 **取值范围**： 字符长度0-65534位 

        :param solution_detail: The solution_detail of this UrgentVulInfo.
        :type solution_detail: str
        """
        self._solution_detail = solution_detail

    @property
    def description(self):
        r"""Gets the description of this UrgentVulInfo.

        **参数解释**： 漏洞描述 **取值范围**： 字符长度0-64位 

        :return: The description of this UrgentVulInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UrgentVulInfo.

        **参数解释**： 漏洞描述 **取值范围**： 字符长度0-64位 

        :param description: The description of this UrgentVulInfo.
        :type description: str
        """
        self._description = description

    @property
    def scan_status(self):
        r"""Gets the scan_status of this UrgentVulInfo.

        **参数解释**： 漏洞扫描状态 **约束限制**: 不涉及 **取值范围**： - never_scan : 未扫描 - scanning : 扫描中 - finished : 扫描完成  **默认取值**: 不涉及 

        :return: The scan_status of this UrgentVulInfo.
        :rtype: str
        """
        return self._scan_status

    @scan_status.setter
    def scan_status(self, scan_status):
        r"""Sets the scan_status of this UrgentVulInfo.

        **参数解释**： 漏洞扫描状态 **约束限制**: 不涉及 **取值范围**： - never_scan : 未扫描 - scanning : 扫描中 - finished : 扫描完成  **默认取值**: 不涉及 

        :param scan_status: The scan_status of this UrgentVulInfo.
        :type scan_status: str
        """
        self._scan_status = scan_status

    @property
    def severity_level(self):
        r"""Gets the severity_level of this UrgentVulInfo.

        **参数解释**： 危险程度 **约束限制**: 不涉及 **取值范围**： - Critical：漏洞cvss评分大于等于9；对应控制台页面的高危 - High：漏洞cvss评分大于等于7，小于9；对应控制台页面的中危 - Medium：漏洞cvss评分大于等于4，小于7；对应控制台页面的中危 - Low：漏洞cvss评分小于4；对应控制台页面的低危  **默认取值**: 不涉及 

        :return: The severity_level of this UrgentVulInfo.
        :rtype: str
        """
        return self._severity_level

    @severity_level.setter
    def severity_level(self, severity_level):
        r"""Sets the severity_level of this UrgentVulInfo.

        **参数解释**： 危险程度 **约束限制**: 不涉及 **取值范围**： - Critical：漏洞cvss评分大于等于9；对应控制台页面的高危 - High：漏洞cvss评分大于等于7，小于9；对应控制台页面的中危 - Medium：漏洞cvss评分大于等于4，小于7；对应控制台页面的中危 - Low：漏洞cvss评分小于4；对应控制台页面的低危  **默认取值**: 不涉及 

        :param severity_level: The severity_level of this UrgentVulInfo.
        :type severity_level: str
        """
        self._severity_level = severity_level

    @property
    def scanning_host_num(self):
        r"""Gets the scanning_host_num of this UrgentVulInfo.

        **参数解释**： 处于扫描中状态的主机数量 **取值范围**： 字符长度0-2147483647 

        :return: The scanning_host_num of this UrgentVulInfo.
        :rtype: int
        """
        return self._scanning_host_num

    @scanning_host_num.setter
    def scanning_host_num(self, scanning_host_num):
        r"""Sets the scanning_host_num of this UrgentVulInfo.

        **参数解释**： 处于扫描中状态的主机数量 **取值范围**： 字符长度0-2147483647 

        :param scanning_host_num: The scanning_host_num of this UrgentVulInfo.
        :type scanning_host_num: int
        """
        self._scanning_host_num = scanning_host_num

    @property
    def success_host_num(self):
        r"""Gets the success_host_num of this UrgentVulInfo.

        **参数解释**： 已扫描成功的主机数量 **取值范围**： 字符长度0-2147483647 

        :return: The success_host_num of this UrgentVulInfo.
        :rtype: int
        """
        return self._success_host_num

    @success_host_num.setter
    def success_host_num(self, success_host_num):
        r"""Sets the success_host_num of this UrgentVulInfo.

        **参数解释**： 已扫描成功的主机数量 **取值范围**： 字符长度0-2147483647 

        :param success_host_num: The success_host_num of this UrgentVulInfo.
        :type success_host_num: int
        """
        self._success_host_num = success_host_num

    @property
    def failed_host_num(self):
        r"""Gets the failed_host_num of this UrgentVulInfo.

        **参数解释**： 已扫描失败的主机数量 **取值范围**： 字符长度0-2147483647 

        :return: The failed_host_num of this UrgentVulInfo.
        :rtype: int
        """
        return self._failed_host_num

    @failed_host_num.setter
    def failed_host_num(self, failed_host_num):
        r"""Sets the failed_host_num of this UrgentVulInfo.

        **参数解释**： 已扫描失败的主机数量 **取值范围**： 字符长度0-2147483647 

        :param failed_host_num: The failed_host_num of this UrgentVulInfo.
        :type failed_host_num: int
        """
        self._failed_host_num = failed_host_num

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
        if not isinstance(other, UrgentVulInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
