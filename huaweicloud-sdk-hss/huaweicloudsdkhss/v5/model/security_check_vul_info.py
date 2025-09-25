# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityCheckVulInfo:

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
        'repair_necessity': 'str',
        'scan_time': 'int',
        'type': 'str',
        'repair_cmd': 'str',
        'severity_level': 'str'
    }

    attribute_map = {
        'vul_name': 'vul_name',
        'vul_id': 'vul_id',
        'repair_necessity': 'repair_necessity',
        'scan_time': 'scan_time',
        'type': 'type',
        'repair_cmd': 'repair_cmd',
        'severity_level': 'severity_level'
    }

    def __init__(self, vul_name=None, vul_id=None, repair_necessity=None, scan_time=None, type=None, repair_cmd=None, severity_level=None):
        r"""SecurityCheckVulInfo

        The model defined in huaweicloud sdk

        :param vul_name: **参数解释**： 漏洞名称 **取值范围**： 不涉及 
        :type vul_name: str
        :param vul_id: **参数解释**： 漏洞ID **取值范围**： 不涉及 
        :type vul_id: str
        :param repair_necessity: **参数解释**： 修复紧急度 **取值范围**： 不涉及 
        :type repair_necessity: str
        :param scan_time: **参数解释**： 最近扫描时间 **取值范围**： 不涉及 
        :type scan_time: int
        :param type: **参数解释**： 漏洞类型 **取值范围**： 不涉及 
        :type type: str
        :param repair_cmd: **参数解释**： 修复命令行 **取值范围**： 不涉及 
        :type repair_cmd: str
        :param severity_level: **参数解释**: 漏洞风险级别 **取值范围**: - Critical：漏洞cvss评分大于等于9；对应控制台页面的高危 - High：漏洞cvss评分大于等于7，小于9；对应控制台页面的中危 - Medium：漏洞cvss评分大于等于4，小于7；对应控制台页面的中危 - Low：漏洞cvss评分小于4；对应控制台页面的低危 
        :type severity_level: str
        """
        
        

        self._vul_name = None
        self._vul_id = None
        self._repair_necessity = None
        self._scan_time = None
        self._type = None
        self._repair_cmd = None
        self._severity_level = None
        self.discriminator = None

        if vul_name is not None:
            self.vul_name = vul_name
        if vul_id is not None:
            self.vul_id = vul_id
        if repair_necessity is not None:
            self.repair_necessity = repair_necessity
        if scan_time is not None:
            self.scan_time = scan_time
        if type is not None:
            self.type = type
        if repair_cmd is not None:
            self.repair_cmd = repair_cmd
        if severity_level is not None:
            self.severity_level = severity_level

    @property
    def vul_name(self):
        r"""Gets the vul_name of this SecurityCheckVulInfo.

        **参数解释**： 漏洞名称 **取值范围**： 不涉及 

        :return: The vul_name of this SecurityCheckVulInfo.
        :rtype: str
        """
        return self._vul_name

    @vul_name.setter
    def vul_name(self, vul_name):
        r"""Sets the vul_name of this SecurityCheckVulInfo.

        **参数解释**： 漏洞名称 **取值范围**： 不涉及 

        :param vul_name: The vul_name of this SecurityCheckVulInfo.
        :type vul_name: str
        """
        self._vul_name = vul_name

    @property
    def vul_id(self):
        r"""Gets the vul_id of this SecurityCheckVulInfo.

        **参数解释**： 漏洞ID **取值范围**： 不涉及 

        :return: The vul_id of this SecurityCheckVulInfo.
        :rtype: str
        """
        return self._vul_id

    @vul_id.setter
    def vul_id(self, vul_id):
        r"""Sets the vul_id of this SecurityCheckVulInfo.

        **参数解释**： 漏洞ID **取值范围**： 不涉及 

        :param vul_id: The vul_id of this SecurityCheckVulInfo.
        :type vul_id: str
        """
        self._vul_id = vul_id

    @property
    def repair_necessity(self):
        r"""Gets the repair_necessity of this SecurityCheckVulInfo.

        **参数解释**： 修复紧急度 **取值范围**： 不涉及 

        :return: The repair_necessity of this SecurityCheckVulInfo.
        :rtype: str
        """
        return self._repair_necessity

    @repair_necessity.setter
    def repair_necessity(self, repair_necessity):
        r"""Sets the repair_necessity of this SecurityCheckVulInfo.

        **参数解释**： 修复紧急度 **取值范围**： 不涉及 

        :param repair_necessity: The repair_necessity of this SecurityCheckVulInfo.
        :type repair_necessity: str
        """
        self._repair_necessity = repair_necessity

    @property
    def scan_time(self):
        r"""Gets the scan_time of this SecurityCheckVulInfo.

        **参数解释**： 最近扫描时间 **取值范围**： 不涉及 

        :return: The scan_time of this SecurityCheckVulInfo.
        :rtype: int
        """
        return self._scan_time

    @scan_time.setter
    def scan_time(self, scan_time):
        r"""Sets the scan_time of this SecurityCheckVulInfo.

        **参数解释**： 最近扫描时间 **取值范围**： 不涉及 

        :param scan_time: The scan_time of this SecurityCheckVulInfo.
        :type scan_time: int
        """
        self._scan_time = scan_time

    @property
    def type(self):
        r"""Gets the type of this SecurityCheckVulInfo.

        **参数解释**： 漏洞类型 **取值范围**： 不涉及 

        :return: The type of this SecurityCheckVulInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this SecurityCheckVulInfo.

        **参数解释**： 漏洞类型 **取值范围**： 不涉及 

        :param type: The type of this SecurityCheckVulInfo.
        :type type: str
        """
        self._type = type

    @property
    def repair_cmd(self):
        r"""Gets the repair_cmd of this SecurityCheckVulInfo.

        **参数解释**： 修复命令行 **取值范围**： 不涉及 

        :return: The repair_cmd of this SecurityCheckVulInfo.
        :rtype: str
        """
        return self._repair_cmd

    @repair_cmd.setter
    def repair_cmd(self, repair_cmd):
        r"""Sets the repair_cmd of this SecurityCheckVulInfo.

        **参数解释**： 修复命令行 **取值范围**： 不涉及 

        :param repair_cmd: The repair_cmd of this SecurityCheckVulInfo.
        :type repair_cmd: str
        """
        self._repair_cmd = repair_cmd

    @property
    def severity_level(self):
        r"""Gets the severity_level of this SecurityCheckVulInfo.

        **参数解释**: 漏洞风险级别 **取值范围**: - Critical：漏洞cvss评分大于等于9；对应控制台页面的高危 - High：漏洞cvss评分大于等于7，小于9；对应控制台页面的中危 - Medium：漏洞cvss评分大于等于4，小于7；对应控制台页面的中危 - Low：漏洞cvss评分小于4；对应控制台页面的低危 

        :return: The severity_level of this SecurityCheckVulInfo.
        :rtype: str
        """
        return self._severity_level

    @severity_level.setter
    def severity_level(self, severity_level):
        r"""Sets the severity_level of this SecurityCheckVulInfo.

        **参数解释**: 漏洞风险级别 **取值范围**: - Critical：漏洞cvss评分大于等于9；对应控制台页面的高危 - High：漏洞cvss评分大于等于7，小于9；对应控制台页面的中危 - Medium：漏洞cvss评分大于等于4，小于7；对应控制台页面的中危 - Low：漏洞cvss评分小于4；对应控制台页面的低危 

        :param severity_level: The severity_level of this SecurityCheckVulInfo.
        :type severity_level: str
        """
        self._severity_level = severity_level

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
        if not isinstance(other, SecurityCheckVulInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
