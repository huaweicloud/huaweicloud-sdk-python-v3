# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHandleVulsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
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
        'handle_circle': 'str',
        'repair_priority': 'str'
    }

    attribute_map = {
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
        'handle_circle': 'handle_circle',
        'repair_priority': 'repair_priority'
    }

    def __init__(self, limit=None, offset=None, vul_name=None, cve_id=None, label_list=None, status=None, asset_value=None, group_name=None, host_name=None, host_ip=None, type=None, handle_circle=None, repair_priority=None):
        r"""ListHandleVulsRequest

        The model defined in huaweicloud sdk

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
        :param status: **参数解释**： 漏洞状态 **约束限制**： 不涉及 **取值范围**： - vul_status_ignored: 已忽略。 - vul_status_fixed: 修复成功。  **默认取值**： 不涉及 
        :type status: str
        :param asset_value: **参数解释**： 资产重要性 **约束限制**: 不涉及 **取值范围**: - important：重要资产。 - common：一般资产。 - test：测试资产。  **默认取值**: 不涉及 
        :type asset_value: str
        :param group_name: **参数解释**: 服务器组名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 
        :type group_name: str
        :param host_name: **参数解释**: 主机名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 
        :type host_name: str
        :param host_ip: **参数解释**: 主机ip **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 
        :type host_ip: str
        :param type: **参数解释**: 漏洞类型 **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 
        :type type: str
        :param handle_circle: **参数解释**： 处理周期 **约束限制**: 不涉及 **取值范围**: - today：今日处理。 - all：累计处理。  **默认取值**: 不涉及 
        :type handle_circle: str
        :param repair_priority: **参数解释**： 修复优先级 **约束限制**: 不涉及 **取值范围**: - Critical：紧急。 - High：高。 - Medium：中。 - Low：低。  **默认取值**: 不涉及 
        :type repair_priority: str
        """
        
        

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
        self._handle_circle = None
        self._repair_priority = None
        self.discriminator = None

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
        if handle_circle is not None:
            self.handle_circle = handle_circle
        if repair_priority is not None:
            self.repair_priority = repair_priority

    @property
    def limit(self):
        r"""Gets the limit of this ListHandleVulsRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListHandleVulsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListHandleVulsRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListHandleVulsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListHandleVulsRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :return: The offset of this ListHandleVulsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListHandleVulsRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :param offset: The offset of this ListHandleVulsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def vul_name(self):
        r"""Gets the vul_name of this ListHandleVulsRequest.

        **参数解释**: 漏洞名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :return: The vul_name of this ListHandleVulsRequest.
        :rtype: str
        """
        return self._vul_name

    @vul_name.setter
    def vul_name(self, vul_name):
        r"""Sets the vul_name of this ListHandleVulsRequest.

        **参数解释**: 漏洞名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :param vul_name: The vul_name of this ListHandleVulsRequest.
        :type vul_name: str
        """
        self._vul_name = vul_name

    @property
    def cve_id(self):
        r"""Gets the cve_id of this ListHandleVulsRequest.

        **参数解释**: 漏洞cve编号 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The cve_id of this ListHandleVulsRequest.
        :rtype: str
        """
        return self._cve_id

    @cve_id.setter
    def cve_id(self, cve_id):
        r"""Sets the cve_id of this ListHandleVulsRequest.

        **参数解释**: 漏洞cve编号 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param cve_id: The cve_id of this ListHandleVulsRequest.
        :type cve_id: str
        """
        self._cve_id = cve_id

    @property
    def label_list(self):
        r"""Gets the label_list of this ListHandleVulsRequest.

        **参数解释**: 漏洞标签 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :return: The label_list of this ListHandleVulsRequest.
        :rtype: str
        """
        return self._label_list

    @label_list.setter
    def label_list(self, label_list):
        r"""Sets the label_list of this ListHandleVulsRequest.

        **参数解释**: 漏洞标签 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :param label_list: The label_list of this ListHandleVulsRequest.
        :type label_list: str
        """
        self._label_list = label_list

    @property
    def status(self):
        r"""Gets the status of this ListHandleVulsRequest.

        **参数解释**： 漏洞状态 **约束限制**： 不涉及 **取值范围**： - vul_status_ignored: 已忽略。 - vul_status_fixed: 修复成功。  **默认取值**： 不涉及 

        :return: The status of this ListHandleVulsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListHandleVulsRequest.

        **参数解释**： 漏洞状态 **约束限制**： 不涉及 **取值范围**： - vul_status_ignored: 已忽略。 - vul_status_fixed: 修复成功。  **默认取值**： 不涉及 

        :param status: The status of this ListHandleVulsRequest.
        :type status: str
        """
        self._status = status

    @property
    def asset_value(self):
        r"""Gets the asset_value of this ListHandleVulsRequest.

        **参数解释**： 资产重要性 **约束限制**: 不涉及 **取值范围**: - important：重要资产。 - common：一般资产。 - test：测试资产。  **默认取值**: 不涉及 

        :return: The asset_value of this ListHandleVulsRequest.
        :rtype: str
        """
        return self._asset_value

    @asset_value.setter
    def asset_value(self, asset_value):
        r"""Sets the asset_value of this ListHandleVulsRequest.

        **参数解释**： 资产重要性 **约束限制**: 不涉及 **取值范围**: - important：重要资产。 - common：一般资产。 - test：测试资产。  **默认取值**: 不涉及 

        :param asset_value: The asset_value of this ListHandleVulsRequest.
        :type asset_value: str
        """
        self._asset_value = asset_value

    @property
    def group_name(self):
        r"""Gets the group_name of this ListHandleVulsRequest.

        **参数解释**: 服务器组名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The group_name of this ListHandleVulsRequest.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this ListHandleVulsRequest.

        **参数解释**: 服务器组名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param group_name: The group_name of this ListHandleVulsRequest.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def host_name(self):
        r"""Gets the host_name of this ListHandleVulsRequest.

        **参数解释**: 主机名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The host_name of this ListHandleVulsRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ListHandleVulsRequest.

        **参数解释**: 主机名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param host_name: The host_name of this ListHandleVulsRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_ip(self):
        r"""Gets the host_ip of this ListHandleVulsRequest.

        **参数解释**: 主机ip **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :return: The host_ip of this ListHandleVulsRequest.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        r"""Sets the host_ip of this ListHandleVulsRequest.

        **参数解释**: 主机ip **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :param host_ip: The host_ip of this ListHandleVulsRequest.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def type(self):
        r"""Gets the type of this ListHandleVulsRequest.

        **参数解释**: 漏洞类型 **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :return: The type of this ListHandleVulsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListHandleVulsRequest.

        **参数解释**: 漏洞类型 **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :param type: The type of this ListHandleVulsRequest.
        :type type: str
        """
        self._type = type

    @property
    def handle_circle(self):
        r"""Gets the handle_circle of this ListHandleVulsRequest.

        **参数解释**： 处理周期 **约束限制**: 不涉及 **取值范围**: - today：今日处理。 - all：累计处理。  **默认取值**: 不涉及 

        :return: The handle_circle of this ListHandleVulsRequest.
        :rtype: str
        """
        return self._handle_circle

    @handle_circle.setter
    def handle_circle(self, handle_circle):
        r"""Sets the handle_circle of this ListHandleVulsRequest.

        **参数解释**： 处理周期 **约束限制**: 不涉及 **取值范围**: - today：今日处理。 - all：累计处理。  **默认取值**: 不涉及 

        :param handle_circle: The handle_circle of this ListHandleVulsRequest.
        :type handle_circle: str
        """
        self._handle_circle = handle_circle

    @property
    def repair_priority(self):
        r"""Gets the repair_priority of this ListHandleVulsRequest.

        **参数解释**： 修复优先级 **约束限制**: 不涉及 **取值范围**: - Critical：紧急。 - High：高。 - Medium：中。 - Low：低。  **默认取值**: 不涉及 

        :return: The repair_priority of this ListHandleVulsRequest.
        :rtype: str
        """
        return self._repair_priority

    @repair_priority.setter
    def repair_priority(self, repair_priority):
        r"""Sets the repair_priority of this ListHandleVulsRequest.

        **参数解释**： 修复优先级 **约束限制**: 不涉及 **取值范围**: - Critical：紧急。 - High：高。 - Medium：中。 - Low：低。  **默认取值**: 不涉及 

        :param repair_priority: The repair_priority of this ListHandleVulsRequest.
        :type repair_priority: str
        """
        self._repair_priority = repair_priority

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
        if not isinstance(other, ListHandleVulsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
