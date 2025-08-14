# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVulnerabilitiesRequest:

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
        'type': 'str',
        'vul_id': 'str',
        'vul_name': 'str',
        'limit': 'int',
        'offset': 'int',
        'repair_priority': 'str',
        'handle_status': 'str',
        'cve_id': 'str',
        'label_list': 'str',
        'status': 'str',
        'asset_value': 'str',
        'group_name': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'type': 'type',
        'vul_id': 'vul_id',
        'vul_name': 'vul_name',
        'limit': 'limit',
        'offset': 'offset',
        'repair_priority': 'repair_priority',
        'handle_status': 'handle_status',
        'cve_id': 'cve_id',
        'label_list': 'label_list',
        'status': 'status',
        'asset_value': 'asset_value',
        'group_name': 'group_name'
    }

    def __init__(self, enterprise_project_id=None, type=None, vul_id=None, vul_name=None, limit=None, offset=None, repair_priority=None, handle_status=None, cve_id=None, label_list=None, status=None, asset_value=None, group_name=None):
        r"""ListVulnerabilitiesRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param type: **参数解释**: 漏洞类型 **约束限制**: 不涉及 **取值范围**:   - linux_vul：linux漏洞   - windows_vul：windows漏洞   - web_cms：Web-CMS漏洞   - app_vul：应用漏洞  **默认取值**: linux_vul，默认查询linux漏洞 
        :type type: str
        :param vul_id: **参数解释**: 漏洞ID **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 
        :type vul_id: str
        :param vul_name: **参数解释**: 漏洞名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 
        :type vul_name: str
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 
        :type offset: int
        :param repair_priority: **参数解释**: 漏洞修复优先级 **约束限制**: 不涉及 **取值范围**: - Critical：紧急 - High：高 - Medium：中 - Low：低  **默认取值**: 不涉及 
        :type repair_priority: str
        :param handle_status: **参数解释**: 漏洞的处置状态 **约束限制**: 不涉及 **取值范围**: - unhandled：未处理 - handled：已处理  **默认取值**: 不涉及 
        :type handle_status: str
        :param cve_id: **参数解释**: 漏洞cve编号 **约束限制**: 不涉及 **取值范围**: 字符长度0-32位 **默认取值**: 不涉及 
        :type cve_id: str
        :param label_list: **参数解释**: 漏洞标签 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 
        :type label_list: str
        :param status: **参数解释**: 漏洞状态 **约束限制**: 不涉及 **取值范围**: - vul_status_unfix：未处理 - vul_status_ignored：已忽略 - vul_status_verified：验证中 - vul_status_fixing：修复中 - vul_status_fixed：修复成功 - vul_status_reboot：修复成功待重启 - vul_status_failed：修复失败 - vul_status_fix_after_reboot：请重启主机再次修复  **默认取值**: 不涉及 
        :type status: str
        :param asset_value: **参数解释**: 存在漏洞主机的资产重要性 **约束限制**: 不涉及 **取值范围**: - important：重要资产 - common：一般资产 - test：测试资产  **默认取值**: 不涉及 
        :type asset_value: str
        :param group_name: **参数解释**: 存在漏洞主机的所属服务器组 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 
        :type group_name: str
        """
        
        

        self._enterprise_project_id = None
        self._type = None
        self._vul_id = None
        self._vul_name = None
        self._limit = None
        self._offset = None
        self._repair_priority = None
        self._handle_status = None
        self._cve_id = None
        self._label_list = None
        self._status = None
        self._asset_value = None
        self._group_name = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if type is not None:
            self.type = type
        if vul_id is not None:
            self.vul_id = vul_id
        if vul_name is not None:
            self.vul_name = vul_name
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if repair_priority is not None:
            self.repair_priority = repair_priority
        if handle_status is not None:
            self.handle_status = handle_status
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

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListVulnerabilitiesRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListVulnerabilitiesRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListVulnerabilitiesRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListVulnerabilitiesRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def type(self):
        r"""Gets the type of this ListVulnerabilitiesRequest.

        **参数解释**: 漏洞类型 **约束限制**: 不涉及 **取值范围**:   - linux_vul：linux漏洞   - windows_vul：windows漏洞   - web_cms：Web-CMS漏洞   - app_vul：应用漏洞  **默认取值**: linux_vul，默认查询linux漏洞 

        :return: The type of this ListVulnerabilitiesRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListVulnerabilitiesRequest.

        **参数解释**: 漏洞类型 **约束限制**: 不涉及 **取值范围**:   - linux_vul：linux漏洞   - windows_vul：windows漏洞   - web_cms：Web-CMS漏洞   - app_vul：应用漏洞  **默认取值**: linux_vul，默认查询linux漏洞 

        :param type: The type of this ListVulnerabilitiesRequest.
        :type type: str
        """
        self._type = type

    @property
    def vul_id(self):
        r"""Gets the vul_id of this ListVulnerabilitiesRequest.

        **参数解释**: 漏洞ID **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :return: The vul_id of this ListVulnerabilitiesRequest.
        :rtype: str
        """
        return self._vul_id

    @vul_id.setter
    def vul_id(self, vul_id):
        r"""Sets the vul_id of this ListVulnerabilitiesRequest.

        **参数解释**: 漏洞ID **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :param vul_id: The vul_id of this ListVulnerabilitiesRequest.
        :type vul_id: str
        """
        self._vul_id = vul_id

    @property
    def vul_name(self):
        r"""Gets the vul_name of this ListVulnerabilitiesRequest.

        **参数解释**: 漏洞名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :return: The vul_name of this ListVulnerabilitiesRequest.
        :rtype: str
        """
        return self._vul_name

    @vul_name.setter
    def vul_name(self, vul_name):
        r"""Sets the vul_name of this ListVulnerabilitiesRequest.

        **参数解释**: 漏洞名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :param vul_name: The vul_name of this ListVulnerabilitiesRequest.
        :type vul_name: str
        """
        self._vul_name = vul_name

    @property
    def limit(self):
        r"""Gets the limit of this ListVulnerabilitiesRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListVulnerabilitiesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListVulnerabilitiesRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListVulnerabilitiesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListVulnerabilitiesRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :return: The offset of this ListVulnerabilitiesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListVulnerabilitiesRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :param offset: The offset of this ListVulnerabilitiesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def repair_priority(self):
        r"""Gets the repair_priority of this ListVulnerabilitiesRequest.

        **参数解释**: 漏洞修复优先级 **约束限制**: 不涉及 **取值范围**: - Critical：紧急 - High：高 - Medium：中 - Low：低  **默认取值**: 不涉及 

        :return: The repair_priority of this ListVulnerabilitiesRequest.
        :rtype: str
        """
        return self._repair_priority

    @repair_priority.setter
    def repair_priority(self, repair_priority):
        r"""Sets the repair_priority of this ListVulnerabilitiesRequest.

        **参数解释**: 漏洞修复优先级 **约束限制**: 不涉及 **取值范围**: - Critical：紧急 - High：高 - Medium：中 - Low：低  **默认取值**: 不涉及 

        :param repair_priority: The repair_priority of this ListVulnerabilitiesRequest.
        :type repair_priority: str
        """
        self._repair_priority = repair_priority

    @property
    def handle_status(self):
        r"""Gets the handle_status of this ListVulnerabilitiesRequest.

        **参数解释**: 漏洞的处置状态 **约束限制**: 不涉及 **取值范围**: - unhandled：未处理 - handled：已处理  **默认取值**: 不涉及 

        :return: The handle_status of this ListVulnerabilitiesRequest.
        :rtype: str
        """
        return self._handle_status

    @handle_status.setter
    def handle_status(self, handle_status):
        r"""Sets the handle_status of this ListVulnerabilitiesRequest.

        **参数解释**: 漏洞的处置状态 **约束限制**: 不涉及 **取值范围**: - unhandled：未处理 - handled：已处理  **默认取值**: 不涉及 

        :param handle_status: The handle_status of this ListVulnerabilitiesRequest.
        :type handle_status: str
        """
        self._handle_status = handle_status

    @property
    def cve_id(self):
        r"""Gets the cve_id of this ListVulnerabilitiesRequest.

        **参数解释**: 漏洞cve编号 **约束限制**: 不涉及 **取值范围**: 字符长度0-32位 **默认取值**: 不涉及 

        :return: The cve_id of this ListVulnerabilitiesRequest.
        :rtype: str
        """
        return self._cve_id

    @cve_id.setter
    def cve_id(self, cve_id):
        r"""Sets the cve_id of this ListVulnerabilitiesRequest.

        **参数解释**: 漏洞cve编号 **约束限制**: 不涉及 **取值范围**: 字符长度0-32位 **默认取值**: 不涉及 

        :param cve_id: The cve_id of this ListVulnerabilitiesRequest.
        :type cve_id: str
        """
        self._cve_id = cve_id

    @property
    def label_list(self):
        r"""Gets the label_list of this ListVulnerabilitiesRequest.

        **参数解释**: 漏洞标签 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :return: The label_list of this ListVulnerabilitiesRequest.
        :rtype: str
        """
        return self._label_list

    @label_list.setter
    def label_list(self, label_list):
        r"""Sets the label_list of this ListVulnerabilitiesRequest.

        **参数解释**: 漏洞标签 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :param label_list: The label_list of this ListVulnerabilitiesRequest.
        :type label_list: str
        """
        self._label_list = label_list

    @property
    def status(self):
        r"""Gets the status of this ListVulnerabilitiesRequest.

        **参数解释**: 漏洞状态 **约束限制**: 不涉及 **取值范围**: - vul_status_unfix：未处理 - vul_status_ignored：已忽略 - vul_status_verified：验证中 - vul_status_fixing：修复中 - vul_status_fixed：修复成功 - vul_status_reboot：修复成功待重启 - vul_status_failed：修复失败 - vul_status_fix_after_reboot：请重启主机再次修复  **默认取值**: 不涉及 

        :return: The status of this ListVulnerabilitiesRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListVulnerabilitiesRequest.

        **参数解释**: 漏洞状态 **约束限制**: 不涉及 **取值范围**: - vul_status_unfix：未处理 - vul_status_ignored：已忽略 - vul_status_verified：验证中 - vul_status_fixing：修复中 - vul_status_fixed：修复成功 - vul_status_reboot：修复成功待重启 - vul_status_failed：修复失败 - vul_status_fix_after_reboot：请重启主机再次修复  **默认取值**: 不涉及 

        :param status: The status of this ListVulnerabilitiesRequest.
        :type status: str
        """
        self._status = status

    @property
    def asset_value(self):
        r"""Gets the asset_value of this ListVulnerabilitiesRequest.

        **参数解释**: 存在漏洞主机的资产重要性 **约束限制**: 不涉及 **取值范围**: - important：重要资产 - common：一般资产 - test：测试资产  **默认取值**: 不涉及 

        :return: The asset_value of this ListVulnerabilitiesRequest.
        :rtype: str
        """
        return self._asset_value

    @asset_value.setter
    def asset_value(self, asset_value):
        r"""Sets the asset_value of this ListVulnerabilitiesRequest.

        **参数解释**: 存在漏洞主机的资产重要性 **约束限制**: 不涉及 **取值范围**: - important：重要资产 - common：一般资产 - test：测试资产  **默认取值**: 不涉及 

        :param asset_value: The asset_value of this ListVulnerabilitiesRequest.
        :type asset_value: str
        """
        self._asset_value = asset_value

    @property
    def group_name(self):
        r"""Gets the group_name of this ListVulnerabilitiesRequest.

        **参数解释**: 存在漏洞主机的所属服务器组 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :return: The group_name of this ListVulnerabilitiesRequest.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this ListVulnerabilitiesRequest.

        **参数解释**: 存在漏洞主机的所属服务器组 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :param group_name: The group_name of this ListVulnerabilitiesRequest.
        :type group_name: str
        """
        self._group_name = group_name

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
        if not isinstance(other, ListVulnerabilitiesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
