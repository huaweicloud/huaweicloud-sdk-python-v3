# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowVulReportDataResponseInfoVulnerabilities:

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
        'scan_time': 'int',
        'type': 'str',
        'cve_list': 'list[ShowVulReportDataResponseInfoCveList]',
        'repair_priority': 'str',
        'host_num': 'int',
        'host_id_list': 'list[str]'
    }

    attribute_map = {
        'vul_name': 'vul_name',
        'scan_time': 'scan_time',
        'type': 'type',
        'cve_list': 'cve_list',
        'repair_priority': 'repair_priority',
        'host_num': 'host_num',
        'host_id_list': 'host_id_list'
    }

    def __init__(self, vul_name=None, scan_time=None, type=None, cve_list=None, repair_priority=None, host_num=None, host_id_list=None):
        r"""ShowVulReportDataResponseInfoVulnerabilities

        The model defined in huaweicloud sdk

        :param vul_name: **参数解释**： 漏洞名称 **取值范围**： 字符长度0-256位 
        :type vul_name: str
        :param scan_time: **参数解释**： 最近扫描时间 **取值范围**： 最小值0，最大值9223372036854775807 
        :type scan_time: int
        :param type: **参数解释**： 漏洞类型 **取值范围**： - linux_vul：linux漏洞。 - windows_vul：windows漏洞。 - web_cms：Web-CMS漏洞。 - app_vul：应用漏洞。 
        :type type: str
        :param cve_list: CVE列表
        :type cve_list: list[:class:`huaweicloudsdkhss.v5.ShowVulReportDataResponseInfoCveList`]
        :param repair_priority: **参数解释**： 修复优先级 **取值范围**： - Critical：紧急。 - High：高。 - Medium：中。 - Low：低。 
        :type repair_priority: str
        :param host_num: **参数解释**： 影响主机数量 **取值范围**： 最小值0，最大值20000 
        :type host_num: int
        :param host_id_list: **参数解释**: 主机ID列表(数组长度跟host_num对不上时，主机数量以host_num为准) **取值范围**: 最小值0，最大值20000 
        :type host_id_list: list[str]
        """
        
        

        self._vul_name = None
        self._scan_time = None
        self._type = None
        self._cve_list = None
        self._repair_priority = None
        self._host_num = None
        self._host_id_list = None
        self.discriminator = None

        if vul_name is not None:
            self.vul_name = vul_name
        if scan_time is not None:
            self.scan_time = scan_time
        if type is not None:
            self.type = type
        if cve_list is not None:
            self.cve_list = cve_list
        if repair_priority is not None:
            self.repair_priority = repair_priority
        if host_num is not None:
            self.host_num = host_num
        if host_id_list is not None:
            self.host_id_list = host_id_list

    @property
    def vul_name(self):
        r"""Gets the vul_name of this ShowVulReportDataResponseInfoVulnerabilities.

        **参数解释**： 漏洞名称 **取值范围**： 字符长度0-256位 

        :return: The vul_name of this ShowVulReportDataResponseInfoVulnerabilities.
        :rtype: str
        """
        return self._vul_name

    @vul_name.setter
    def vul_name(self, vul_name):
        r"""Sets the vul_name of this ShowVulReportDataResponseInfoVulnerabilities.

        **参数解释**： 漏洞名称 **取值范围**： 字符长度0-256位 

        :param vul_name: The vul_name of this ShowVulReportDataResponseInfoVulnerabilities.
        :type vul_name: str
        """
        self._vul_name = vul_name

    @property
    def scan_time(self):
        r"""Gets the scan_time of this ShowVulReportDataResponseInfoVulnerabilities.

        **参数解释**： 最近扫描时间 **取值范围**： 最小值0，最大值9223372036854775807 

        :return: The scan_time of this ShowVulReportDataResponseInfoVulnerabilities.
        :rtype: int
        """
        return self._scan_time

    @scan_time.setter
    def scan_time(self, scan_time):
        r"""Sets the scan_time of this ShowVulReportDataResponseInfoVulnerabilities.

        **参数解释**： 最近扫描时间 **取值范围**： 最小值0，最大值9223372036854775807 

        :param scan_time: The scan_time of this ShowVulReportDataResponseInfoVulnerabilities.
        :type scan_time: int
        """
        self._scan_time = scan_time

    @property
    def type(self):
        r"""Gets the type of this ShowVulReportDataResponseInfoVulnerabilities.

        **参数解释**： 漏洞类型 **取值范围**： - linux_vul：linux漏洞。 - windows_vul：windows漏洞。 - web_cms：Web-CMS漏洞。 - app_vul：应用漏洞。 

        :return: The type of this ShowVulReportDataResponseInfoVulnerabilities.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowVulReportDataResponseInfoVulnerabilities.

        **参数解释**： 漏洞类型 **取值范围**： - linux_vul：linux漏洞。 - windows_vul：windows漏洞。 - web_cms：Web-CMS漏洞。 - app_vul：应用漏洞。 

        :param type: The type of this ShowVulReportDataResponseInfoVulnerabilities.
        :type type: str
        """
        self._type = type

    @property
    def cve_list(self):
        r"""Gets the cve_list of this ShowVulReportDataResponseInfoVulnerabilities.

        CVE列表

        :return: The cve_list of this ShowVulReportDataResponseInfoVulnerabilities.
        :rtype: list[:class:`huaweicloudsdkhss.v5.ShowVulReportDataResponseInfoCveList`]
        """
        return self._cve_list

    @cve_list.setter
    def cve_list(self, cve_list):
        r"""Sets the cve_list of this ShowVulReportDataResponseInfoVulnerabilities.

        CVE列表

        :param cve_list: The cve_list of this ShowVulReportDataResponseInfoVulnerabilities.
        :type cve_list: list[:class:`huaweicloudsdkhss.v5.ShowVulReportDataResponseInfoCveList`]
        """
        self._cve_list = cve_list

    @property
    def repair_priority(self):
        r"""Gets the repair_priority of this ShowVulReportDataResponseInfoVulnerabilities.

        **参数解释**： 修复优先级 **取值范围**： - Critical：紧急。 - High：高。 - Medium：中。 - Low：低。 

        :return: The repair_priority of this ShowVulReportDataResponseInfoVulnerabilities.
        :rtype: str
        """
        return self._repair_priority

    @repair_priority.setter
    def repair_priority(self, repair_priority):
        r"""Sets the repair_priority of this ShowVulReportDataResponseInfoVulnerabilities.

        **参数解释**： 修复优先级 **取值范围**： - Critical：紧急。 - High：高。 - Medium：中。 - Low：低。 

        :param repair_priority: The repair_priority of this ShowVulReportDataResponseInfoVulnerabilities.
        :type repair_priority: str
        """
        self._repair_priority = repair_priority

    @property
    def host_num(self):
        r"""Gets the host_num of this ShowVulReportDataResponseInfoVulnerabilities.

        **参数解释**： 影响主机数量 **取值范围**： 最小值0，最大值20000 

        :return: The host_num of this ShowVulReportDataResponseInfoVulnerabilities.
        :rtype: int
        """
        return self._host_num

    @host_num.setter
    def host_num(self, host_num):
        r"""Sets the host_num of this ShowVulReportDataResponseInfoVulnerabilities.

        **参数解释**： 影响主机数量 **取值范围**： 最小值0，最大值20000 

        :param host_num: The host_num of this ShowVulReportDataResponseInfoVulnerabilities.
        :type host_num: int
        """
        self._host_num = host_num

    @property
    def host_id_list(self):
        r"""Gets the host_id_list of this ShowVulReportDataResponseInfoVulnerabilities.

        **参数解释**: 主机ID列表(数组长度跟host_num对不上时，主机数量以host_num为准) **取值范围**: 最小值0，最大值20000 

        :return: The host_id_list of this ShowVulReportDataResponseInfoVulnerabilities.
        :rtype: list[str]
        """
        return self._host_id_list

    @host_id_list.setter
    def host_id_list(self, host_id_list):
        r"""Sets the host_id_list of this ShowVulReportDataResponseInfoVulnerabilities.

        **参数解释**: 主机ID列表(数组长度跟host_num对不上时，主机数量以host_num为准) **取值范围**: 最小值0，最大值20000 

        :param host_id_list: The host_id_list of this ShowVulReportDataResponseInfoVulnerabilities.
        :type host_id_list: list[str]
        """
        self._host_id_list = host_id_list

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
        if not isinstance(other, ShowVulReportDataResponseInfoVulnerabilities):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
