# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VulReportRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'asset_value': 'str',
        'group_name': 'str',
        'host_ids': 'list[str]',
        'host_name': 'str',
        'host_ip': 'str',
        'severity_level': 'str',
        'handle_status': 'str',
        'status': 'str'
    }

    attribute_map = {
        'asset_value': 'asset_value',
        'group_name': 'group_name',
        'host_ids': 'host_ids',
        'host_name': 'host_name',
        'host_ip': 'host_ip',
        'severity_level': 'severity_level',
        'handle_status': 'handle_status',
        'status': 'status'
    }

    def __init__(self, asset_value=None, group_name=None, host_ids=None, host_name=None, host_ip=None, severity_level=None, handle_status=None, status=None):
        r"""VulReportRequestBody

        The model defined in huaweicloud sdk

        :param asset_value: **参数解释**: 资产重要性 **约束限制**: 不涉及 **取值范围**: - important：重要资产。 - common：一般资产。 - test：测试资产。  **默认取值**: 不涉及 
        :type asset_value: str
        :param group_name: **参数解释**： 服务器组名称 **约束限制**： 不涉及 **取值范围**： 字符长度1-64位 **默认取值**： 不涉及 
        :type group_name: str
        :param host_ids: **参数解释**： 服务器ID列表 **约束限制**： 不涉及 **取值范围**： 0-100个items **默认取值**： 不涉及 
        :type host_ids: list[str]
        :param host_name: **参数解释**： 主机名称 **约束限制**： 不涉及 **取值范围**： 字符长度1-64位 **默认取值**： 不涉及 
        :type host_name: str
        :param host_ip: **参数解释**： 主机ip **约束限制**： 不涉及 **取值范围**： 字符长度0-128位 **默认取值**： 不涉及 
        :type host_ip: str
        :param severity_level: **参数解释**: 漏洞风险等级 **约束限制**: 不涉及 **取值范围**: - High：高。 - Medium：中等。 - Low：低。 - Security：安全。  **默认取值**: 不涉及 
        :type severity_level: str
        :param handle_status: **参数解释**: 处置状态 **约束限制**: 不涉及 **取值范围**: - unhandled：未处理。 - handled：已处理。  **默认取值**: 不涉及 
        :type handle_status: str
        :param status: **参数解释**: 主机的漏洞状态 **约束限制**: 不涉及 **取值范围**: - vul_status_unfix：未处理。 - vul_status_ignored：已忽略。 - vul_status_verified：验证中。 - vul_status_fixing：修复中。 - vul_status_fixed：已修复。 - vul_status_reboot：修复待重启。 - vul_status_failed：修复失败。 - vul_status_fix_after_reboot：请重启主机再次修复。  **默认取值**: 不涉及 
        :type status: str
        """
        
        

        self._asset_value = None
        self._group_name = None
        self._host_ids = None
        self._host_name = None
        self._host_ip = None
        self._severity_level = None
        self._handle_status = None
        self._status = None
        self.discriminator = None

        if asset_value is not None:
            self.asset_value = asset_value
        if group_name is not None:
            self.group_name = group_name
        if host_ids is not None:
            self.host_ids = host_ids
        if host_name is not None:
            self.host_name = host_name
        if host_ip is not None:
            self.host_ip = host_ip
        if severity_level is not None:
            self.severity_level = severity_level
        self.handle_status = handle_status
        if status is not None:
            self.status = status

    @property
    def asset_value(self):
        r"""Gets the asset_value of this VulReportRequestBody.

        **参数解释**: 资产重要性 **约束限制**: 不涉及 **取值范围**: - important：重要资产。 - common：一般资产。 - test：测试资产。  **默认取值**: 不涉及 

        :return: The asset_value of this VulReportRequestBody.
        :rtype: str
        """
        return self._asset_value

    @asset_value.setter
    def asset_value(self, asset_value):
        r"""Sets the asset_value of this VulReportRequestBody.

        **参数解释**: 资产重要性 **约束限制**: 不涉及 **取值范围**: - important：重要资产。 - common：一般资产。 - test：测试资产。  **默认取值**: 不涉及 

        :param asset_value: The asset_value of this VulReportRequestBody.
        :type asset_value: str
        """
        self._asset_value = asset_value

    @property
    def group_name(self):
        r"""Gets the group_name of this VulReportRequestBody.

        **参数解释**： 服务器组名称 **约束限制**： 不涉及 **取值范围**： 字符长度1-64位 **默认取值**： 不涉及 

        :return: The group_name of this VulReportRequestBody.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this VulReportRequestBody.

        **参数解释**： 服务器组名称 **约束限制**： 不涉及 **取值范围**： 字符长度1-64位 **默认取值**： 不涉及 

        :param group_name: The group_name of this VulReportRequestBody.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def host_ids(self):
        r"""Gets the host_ids of this VulReportRequestBody.

        **参数解释**： 服务器ID列表 **约束限制**： 不涉及 **取值范围**： 0-100个items **默认取值**： 不涉及 

        :return: The host_ids of this VulReportRequestBody.
        :rtype: list[str]
        """
        return self._host_ids

    @host_ids.setter
    def host_ids(self, host_ids):
        r"""Sets the host_ids of this VulReportRequestBody.

        **参数解释**： 服务器ID列表 **约束限制**： 不涉及 **取值范围**： 0-100个items **默认取值**： 不涉及 

        :param host_ids: The host_ids of this VulReportRequestBody.
        :type host_ids: list[str]
        """
        self._host_ids = host_ids

    @property
    def host_name(self):
        r"""Gets the host_name of this VulReportRequestBody.

        **参数解释**： 主机名称 **约束限制**： 不涉及 **取值范围**： 字符长度1-64位 **默认取值**： 不涉及 

        :return: The host_name of this VulReportRequestBody.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this VulReportRequestBody.

        **参数解释**： 主机名称 **约束限制**： 不涉及 **取值范围**： 字符长度1-64位 **默认取值**： 不涉及 

        :param host_name: The host_name of this VulReportRequestBody.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_ip(self):
        r"""Gets the host_ip of this VulReportRequestBody.

        **参数解释**： 主机ip **约束限制**： 不涉及 **取值范围**： 字符长度0-128位 **默认取值**： 不涉及 

        :return: The host_ip of this VulReportRequestBody.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        r"""Sets the host_ip of this VulReportRequestBody.

        **参数解释**： 主机ip **约束限制**： 不涉及 **取值范围**： 字符长度0-128位 **默认取值**： 不涉及 

        :param host_ip: The host_ip of this VulReportRequestBody.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def severity_level(self):
        r"""Gets the severity_level of this VulReportRequestBody.

        **参数解释**: 漏洞风险等级 **约束限制**: 不涉及 **取值范围**: - High：高。 - Medium：中等。 - Low：低。 - Security：安全。  **默认取值**: 不涉及 

        :return: The severity_level of this VulReportRequestBody.
        :rtype: str
        """
        return self._severity_level

    @severity_level.setter
    def severity_level(self, severity_level):
        r"""Sets the severity_level of this VulReportRequestBody.

        **参数解释**: 漏洞风险等级 **约束限制**: 不涉及 **取值范围**: - High：高。 - Medium：中等。 - Low：低。 - Security：安全。  **默认取值**: 不涉及 

        :param severity_level: The severity_level of this VulReportRequestBody.
        :type severity_level: str
        """
        self._severity_level = severity_level

    @property
    def handle_status(self):
        r"""Gets the handle_status of this VulReportRequestBody.

        **参数解释**: 处置状态 **约束限制**: 不涉及 **取值范围**: - unhandled：未处理。 - handled：已处理。  **默认取值**: 不涉及 

        :return: The handle_status of this VulReportRequestBody.
        :rtype: str
        """
        return self._handle_status

    @handle_status.setter
    def handle_status(self, handle_status):
        r"""Sets the handle_status of this VulReportRequestBody.

        **参数解释**: 处置状态 **约束限制**: 不涉及 **取值范围**: - unhandled：未处理。 - handled：已处理。  **默认取值**: 不涉及 

        :param handle_status: The handle_status of this VulReportRequestBody.
        :type handle_status: str
        """
        self._handle_status = handle_status

    @property
    def status(self):
        r"""Gets the status of this VulReportRequestBody.

        **参数解释**: 主机的漏洞状态 **约束限制**: 不涉及 **取值范围**: - vul_status_unfix：未处理。 - vul_status_ignored：已忽略。 - vul_status_verified：验证中。 - vul_status_fixing：修复中。 - vul_status_fixed：已修复。 - vul_status_reboot：修复待重启。 - vul_status_failed：修复失败。 - vul_status_fix_after_reboot：请重启主机再次修复。  **默认取值**: 不涉及 

        :return: The status of this VulReportRequestBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this VulReportRequestBody.

        **参数解释**: 主机的漏洞状态 **约束限制**: 不涉及 **取值范围**: - vul_status_unfix：未处理。 - vul_status_ignored：已忽略。 - vul_status_verified：验证中。 - vul_status_fixing：修复中。 - vul_status_fixed：已修复。 - vul_status_reboot：修复待重启。 - vul_status_failed：修复失败。 - vul_status_fix_after_reboot：请重启主机再次修复。  **默认取值**: 不涉及 

        :param status: The status of this VulReportRequestBody.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, VulReportRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
