# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportSecurityCheckReportRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'group_id': 'str',
        'host_id': 'str',
        'check_name': 'str',
        'standard': 'str',
        'scan_result': 'str',
        'severity': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'group_id': 'group_id',
        'host_id': 'host_id',
        'check_name': 'check_name',
        'standard': 'standard',
        'scan_result': 'scan_result',
        'severity': 'severity'
    }

    def __init__(self, enterprise_project_id=None, group_id=None, host_id=None, check_name=None, standard=None, scan_result=None, severity=None):
        r"""ExportSecurityCheckReportRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param group_id: **参数解释**: 服务器组ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 
        :type group_id: str
        :param host_id: **参数解释**: 服务器ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 
        :type host_id: str
        :param check_name: **参数解释** : \&quot;配置检查（基线）的名称，例如SSH、CentOS 7、Windows\&quot;。 **约束限制** : 不涉及 **取值范围** : - cn_standard: 等保合规标准 - hw_standard: 云安全实践标准 **默认取值** : 不涉及 
        :type check_name: str
        :param standard: **参数解释**: 标准类型。 **约束限制**: 不涉及 **取值范围**: - cn_standard : 等保合规标准 - hw_standard : 云安全实践标准 **默认取值**: 不涉及 
        :type standard: str
        :param scan_result: **参数解释**: 检查结果。 **约束限制**: 不涉及 **取值范围**: - pass : 检查通过 - failed : 检查未通过 **默认取值**: 不涉及 
        :type scan_result: str
        :param severity: **参数解释**: 风险级别。 **约束限制**: 不涉及 **取值范围**: - Low : 低危 - Medium : 中危 - High : 高危 **默认取值**: 不涉及 
        :type severity: str
        """
        
        

        self._enterprise_project_id = None
        self._group_id = None
        self._host_id = None
        self._check_name = None
        self._standard = None
        self._scan_result = None
        self._severity = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if group_id is not None:
            self.group_id = group_id
        if host_id is not None:
            self.host_id = host_id
        if check_name is not None:
            self.check_name = check_name
        if standard is not None:
            self.standard = standard
        if scan_result is not None:
            self.scan_result = scan_result
        if severity is not None:
            self.severity = severity

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ExportSecurityCheckReportRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ExportSecurityCheckReportRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ExportSecurityCheckReportRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ExportSecurityCheckReportRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def group_id(self):
        r"""Gets the group_id of this ExportSecurityCheckReportRequest.

        **参数解释**: 服务器组ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :return: The group_id of this ExportSecurityCheckReportRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ExportSecurityCheckReportRequest.

        **参数解释**: 服务器组ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :param group_id: The group_id of this ExportSecurityCheckReportRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def host_id(self):
        r"""Gets the host_id of this ExportSecurityCheckReportRequest.

        **参数解释**: 服务器ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :return: The host_id of this ExportSecurityCheckReportRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ExportSecurityCheckReportRequest.

        **参数解释**: 服务器ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :param host_id: The host_id of this ExportSecurityCheckReportRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def check_name(self):
        r"""Gets the check_name of this ExportSecurityCheckReportRequest.

        **参数解释** : \"配置检查（基线）的名称，例如SSH、CentOS 7、Windows\"。 **约束限制** : 不涉及 **取值范围** : - cn_standard: 等保合规标准 - hw_standard: 云安全实践标准 **默认取值** : 不涉及 

        :return: The check_name of this ExportSecurityCheckReportRequest.
        :rtype: str
        """
        return self._check_name

    @check_name.setter
    def check_name(self, check_name):
        r"""Sets the check_name of this ExportSecurityCheckReportRequest.

        **参数解释** : \"配置检查（基线）的名称，例如SSH、CentOS 7、Windows\"。 **约束限制** : 不涉及 **取值范围** : - cn_standard: 等保合规标准 - hw_standard: 云安全实践标准 **默认取值** : 不涉及 

        :param check_name: The check_name of this ExportSecurityCheckReportRequest.
        :type check_name: str
        """
        self._check_name = check_name

    @property
    def standard(self):
        r"""Gets the standard of this ExportSecurityCheckReportRequest.

        **参数解释**: 标准类型。 **约束限制**: 不涉及 **取值范围**: - cn_standard : 等保合规标准 - hw_standard : 云安全实践标准 **默认取值**: 不涉及 

        :return: The standard of this ExportSecurityCheckReportRequest.
        :rtype: str
        """
        return self._standard

    @standard.setter
    def standard(self, standard):
        r"""Sets the standard of this ExportSecurityCheckReportRequest.

        **参数解释**: 标准类型。 **约束限制**: 不涉及 **取值范围**: - cn_standard : 等保合规标准 - hw_standard : 云安全实践标准 **默认取值**: 不涉及 

        :param standard: The standard of this ExportSecurityCheckReportRequest.
        :type standard: str
        """
        self._standard = standard

    @property
    def scan_result(self):
        r"""Gets the scan_result of this ExportSecurityCheckReportRequest.

        **参数解释**: 检查结果。 **约束限制**: 不涉及 **取值范围**: - pass : 检查通过 - failed : 检查未通过 **默认取值**: 不涉及 

        :return: The scan_result of this ExportSecurityCheckReportRequest.
        :rtype: str
        """
        return self._scan_result

    @scan_result.setter
    def scan_result(self, scan_result):
        r"""Sets the scan_result of this ExportSecurityCheckReportRequest.

        **参数解释**: 检查结果。 **约束限制**: 不涉及 **取值范围**: - pass : 检查通过 - failed : 检查未通过 **默认取值**: 不涉及 

        :param scan_result: The scan_result of this ExportSecurityCheckReportRequest.
        :type scan_result: str
        """
        self._scan_result = scan_result

    @property
    def severity(self):
        r"""Gets the severity of this ExportSecurityCheckReportRequest.

        **参数解释**: 风险级别。 **约束限制**: 不涉及 **取值范围**: - Low : 低危 - Medium : 中危 - High : 高危 **默认取值**: 不涉及 

        :return: The severity of this ExportSecurityCheckReportRequest.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this ExportSecurityCheckReportRequest.

        **参数解释**: 风险级别。 **约束限制**: 不涉及 **取值范围**: - Low : 低危 - Medium : 中危 - High : 高危 **默认取值**: 不涉及 

        :param severity: The severity of this ExportSecurityCheckReportRequest.
        :type severity: str
        """
        self._severity = severity

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
        if not isinstance(other, ExportSecurityCheckReportRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
