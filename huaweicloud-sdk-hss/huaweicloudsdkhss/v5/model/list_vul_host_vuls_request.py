# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVulHostVulsRequest:

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
        'limit': 'int',
        'offset': 'int',
        'vul_name': 'str',
        'cve_id': 'str',
        'label_list': 'str',
        'status': 'str',
        'asset_value': 'str',
        'group_name': 'str',
        'host_name': 'str',
        'host_ip': 'str',
        'type': 'str',
        'repair_type': 'str',
        'severity_level': 'str',
        'repair_priority': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'limit': 'limit',
        'offset': 'offset',
        'vul_name': 'vul_name',
        'cve_id': 'cve_id',
        'label_list': 'label_list',
        'status': 'status',
        'asset_value': 'asset_value',
        'group_name': 'group_name',
        'host_name': 'host_name',
        'host_ip': 'host_ip',
        'type': 'type',
        'repair_type': 'repair_type',
        'severity_level': 'severity_level',
        'repair_priority': 'repair_priority'
    }

    def __init__(self, enterprise_project_id=None, limit=None, offset=None, vul_name=None, cve_id=None, label_list=None, status=None, asset_value=None, group_name=None, host_name=None, host_ip=None, type=None, repair_type=None, severity_level=None, repair_priority=None):
        r"""ListVulHostVulsRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 
        :type offset: int
        :param vul_name: **参数解释**: 漏洞名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 
        :type vul_name: str
        :param cve_id: **参数解释**: 漏洞cve编号 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 
        :type cve_id: str
        :param label_list: **参数解释**: 漏洞标签 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 
        :type label_list: str
        :param status: **参数解释**: 漏洞状态 **约束限制**: 不涉及 **取值范围**: - vul_status_unfix：未处理 - vul_status_ignored：已忽略 - vul_status_verified：验证中 - vul_status_fixing：修复中 - vul_status_fixed：修复成功 - vul_status_reboot：修复成功待重启 - vul_status_failed：修复失败 - vul_status_fix_after_reboot：请重启主机再次修复  **默认取值**: 不涉及 
        :type status: str
        :param asset_value: **参数解释**: 主机的资产重要性 **约束限制**: 不涉及 **取值范围**: - important：重要资产 - common：一般资产 - test：测试资产  **默认取值**: 不涉及 
        :type asset_value: str
        :param group_name: **参数解释**: 主机的所属服务器组 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 
        :type group_name: str
        :param host_name: **参数解释**: 主机名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 
        :type host_name: str
        :param host_ip: **参数解释**: 主机ip **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 
        :type host_ip: str
        :param type: **参数解释**: 查询的漏洞类型 **约束限制**: 不涉及 **取值范围**: - linux_vul：linux漏洞 - windows_vul：windows漏洞 - web_cms：Web-CMS漏洞 - app_vul：应用漏洞 - urgent_vul：应急漏洞  **默认取值**: 不涉及 
        :type type: str
        :param repair_type: **参数解释**: 查询漏洞的修复紧急程度类型 **约束限制**: 不涉及 **取值范围**: - need_urgent_repair：需要紧急修复的漏洞 - unrepair：未完成修复的漏洞  **默认取值**: 不涉及 
        :type repair_type: str
        :param severity_level: **参数解释**: 漏洞风险等级 **约束限制**: 不涉及 **取值范围**: - Critical: 紧急 - High: 高 - Medium: 中 - Low: 低  **默认取值**: 不涉及 
        :type severity_level: str
        :param repair_priority: **参数解释**: 漏洞修复优先级 **约束限制**: 不涉及 **取值范围**: - Critical：紧急 - High：高 - Medium：中 - Low：低 **默认取值**: 不涉及 
        :type repair_priority: str
        """
        
        

        self._enterprise_project_id = None
        self._limit = None
        self._offset = None
        self._vul_name = None
        self._cve_id = None
        self._label_list = None
        self._status = None
        self._asset_value = None
        self._group_name = None
        self._host_name = None
        self._host_ip = None
        self._type = None
        self._repair_type = None
        self._severity_level = None
        self._repair_priority = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if vul_name is not None:
            self.vul_name = vul_name
        if cve_id is not None:
            self.cve_id = cve_id
        if label_list is not None:
            self.label_list = label_list
        if status is not None:
            self.status = status
        if asset_value is not None:
            self.asset_value = asset_value
        if group_name is not None:
            self.group_name = group_name
        if host_name is not None:
            self.host_name = host_name
        if host_ip is not None:
            self.host_ip = host_ip
        if type is not None:
            self.type = type
        if repair_type is not None:
            self.repair_type = repair_type
        if severity_level is not None:
            self.severity_level = severity_level
        if repair_priority is not None:
            self.repair_priority = repair_priority

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListVulHostVulsRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListVulHostVulsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListVulHostVulsRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListVulHostVulsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def limit(self):
        r"""Gets the limit of this ListVulHostVulsRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListVulHostVulsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListVulHostVulsRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListVulHostVulsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListVulHostVulsRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :return: The offset of this ListVulHostVulsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListVulHostVulsRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :param offset: The offset of this ListVulHostVulsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def vul_name(self):
        r"""Gets the vul_name of this ListVulHostVulsRequest.

        **参数解释**: 漏洞名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :return: The vul_name of this ListVulHostVulsRequest.
        :rtype: str
        """
        return self._vul_name

    @vul_name.setter
    def vul_name(self, vul_name):
        r"""Sets the vul_name of this ListVulHostVulsRequest.

        **参数解释**: 漏洞名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :param vul_name: The vul_name of this ListVulHostVulsRequest.
        :type vul_name: str
        """
        self._vul_name = vul_name

    @property
    def cve_id(self):
        r"""Gets the cve_id of this ListVulHostVulsRequest.

        **参数解释**: 漏洞cve编号 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The cve_id of this ListVulHostVulsRequest.
        :rtype: str
        """
        return self._cve_id

    @cve_id.setter
    def cve_id(self, cve_id):
        r"""Sets the cve_id of this ListVulHostVulsRequest.

        **参数解释**: 漏洞cve编号 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param cve_id: The cve_id of this ListVulHostVulsRequest.
        :type cve_id: str
        """
        self._cve_id = cve_id

    @property
    def label_list(self):
        r"""Gets the label_list of this ListVulHostVulsRequest.

        **参数解释**: 漏洞标签 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :return: The label_list of this ListVulHostVulsRequest.
        :rtype: str
        """
        return self._label_list

    @label_list.setter
    def label_list(self, label_list):
        r"""Sets the label_list of this ListVulHostVulsRequest.

        **参数解释**: 漏洞标签 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :param label_list: The label_list of this ListVulHostVulsRequest.
        :type label_list: str
        """
        self._label_list = label_list

    @property
    def status(self):
        r"""Gets the status of this ListVulHostVulsRequest.

        **参数解释**: 漏洞状态 **约束限制**: 不涉及 **取值范围**: - vul_status_unfix：未处理 - vul_status_ignored：已忽略 - vul_status_verified：验证中 - vul_status_fixing：修复中 - vul_status_fixed：修复成功 - vul_status_reboot：修复成功待重启 - vul_status_failed：修复失败 - vul_status_fix_after_reboot：请重启主机再次修复  **默认取值**: 不涉及 

        :return: The status of this ListVulHostVulsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListVulHostVulsRequest.

        **参数解释**: 漏洞状态 **约束限制**: 不涉及 **取值范围**: - vul_status_unfix：未处理 - vul_status_ignored：已忽略 - vul_status_verified：验证中 - vul_status_fixing：修复中 - vul_status_fixed：修复成功 - vul_status_reboot：修复成功待重启 - vul_status_failed：修复失败 - vul_status_fix_after_reboot：请重启主机再次修复  **默认取值**: 不涉及 

        :param status: The status of this ListVulHostVulsRequest.
        :type status: str
        """
        self._status = status

    @property
    def asset_value(self):
        r"""Gets the asset_value of this ListVulHostVulsRequest.

        **参数解释**: 主机的资产重要性 **约束限制**: 不涉及 **取值范围**: - important：重要资产 - common：一般资产 - test：测试资产  **默认取值**: 不涉及 

        :return: The asset_value of this ListVulHostVulsRequest.
        :rtype: str
        """
        return self._asset_value

    @asset_value.setter
    def asset_value(self, asset_value):
        r"""Sets the asset_value of this ListVulHostVulsRequest.

        **参数解释**: 主机的资产重要性 **约束限制**: 不涉及 **取值范围**: - important：重要资产 - common：一般资产 - test：测试资产  **默认取值**: 不涉及 

        :param asset_value: The asset_value of this ListVulHostVulsRequest.
        :type asset_value: str
        """
        self._asset_value = asset_value

    @property
    def group_name(self):
        r"""Gets the group_name of this ListVulHostVulsRequest.

        **参数解释**: 主机的所属服务器组 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The group_name of this ListVulHostVulsRequest.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this ListVulHostVulsRequest.

        **参数解释**: 主机的所属服务器组 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param group_name: The group_name of this ListVulHostVulsRequest.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def host_name(self):
        r"""Gets the host_name of this ListVulHostVulsRequest.

        **参数解释**: 主机名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The host_name of this ListVulHostVulsRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ListVulHostVulsRequest.

        **参数解释**: 主机名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param host_name: The host_name of this ListVulHostVulsRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_ip(self):
        r"""Gets the host_ip of this ListVulHostVulsRequest.

        **参数解释**: 主机ip **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :return: The host_ip of this ListVulHostVulsRequest.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        r"""Sets the host_ip of this ListVulHostVulsRequest.

        **参数解释**: 主机ip **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :param host_ip: The host_ip of this ListVulHostVulsRequest.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def type(self):
        r"""Gets the type of this ListVulHostVulsRequest.

        **参数解释**: 查询的漏洞类型 **约束限制**: 不涉及 **取值范围**: - linux_vul：linux漏洞 - windows_vul：windows漏洞 - web_cms：Web-CMS漏洞 - app_vul：应用漏洞 - urgent_vul：应急漏洞  **默认取值**: 不涉及 

        :return: The type of this ListVulHostVulsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListVulHostVulsRequest.

        **参数解释**: 查询的漏洞类型 **约束限制**: 不涉及 **取值范围**: - linux_vul：linux漏洞 - windows_vul：windows漏洞 - web_cms：Web-CMS漏洞 - app_vul：应用漏洞 - urgent_vul：应急漏洞  **默认取值**: 不涉及 

        :param type: The type of this ListVulHostVulsRequest.
        :type type: str
        """
        self._type = type

    @property
    def repair_type(self):
        r"""Gets the repair_type of this ListVulHostVulsRequest.

        **参数解释**: 查询漏洞的修复紧急程度类型 **约束限制**: 不涉及 **取值范围**: - need_urgent_repair：需要紧急修复的漏洞 - unrepair：未完成修复的漏洞  **默认取值**: 不涉及 

        :return: The repair_type of this ListVulHostVulsRequest.
        :rtype: str
        """
        return self._repair_type

    @repair_type.setter
    def repair_type(self, repair_type):
        r"""Sets the repair_type of this ListVulHostVulsRequest.

        **参数解释**: 查询漏洞的修复紧急程度类型 **约束限制**: 不涉及 **取值范围**: - need_urgent_repair：需要紧急修复的漏洞 - unrepair：未完成修复的漏洞  **默认取值**: 不涉及 

        :param repair_type: The repair_type of this ListVulHostVulsRequest.
        :type repair_type: str
        """
        self._repair_type = repair_type

    @property
    def severity_level(self):
        r"""Gets the severity_level of this ListVulHostVulsRequest.

        **参数解释**: 漏洞风险等级 **约束限制**: 不涉及 **取值范围**: - Critical: 紧急 - High: 高 - Medium: 中 - Low: 低  **默认取值**: 不涉及 

        :return: The severity_level of this ListVulHostVulsRequest.
        :rtype: str
        """
        return self._severity_level

    @severity_level.setter
    def severity_level(self, severity_level):
        r"""Sets the severity_level of this ListVulHostVulsRequest.

        **参数解释**: 漏洞风险等级 **约束限制**: 不涉及 **取值范围**: - Critical: 紧急 - High: 高 - Medium: 中 - Low: 低  **默认取值**: 不涉及 

        :param severity_level: The severity_level of this ListVulHostVulsRequest.
        :type severity_level: str
        """
        self._severity_level = severity_level

    @property
    def repair_priority(self):
        r"""Gets the repair_priority of this ListVulHostVulsRequest.

        **参数解释**: 漏洞修复优先级 **约束限制**: 不涉及 **取值范围**: - Critical：紧急 - High：高 - Medium：中 - Low：低 **默认取值**: 不涉及 

        :return: The repair_priority of this ListVulHostVulsRequest.
        :rtype: str
        """
        return self._repair_priority

    @repair_priority.setter
    def repair_priority(self, repair_priority):
        r"""Sets the repair_priority of this ListVulHostVulsRequest.

        **参数解释**: 漏洞修复优先级 **约束限制**: 不涉及 **取值范围**: - Critical：紧急 - High：高 - Medium：中 - Low：低 **默认取值**: 不涉及 

        :param repair_priority: The repair_priority of this ListVulHostVulsRequest.
        :type repair_priority: str
        """
        self._repair_priority = repair_priority

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
        if not isinstance(other, ListVulHostVulsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
