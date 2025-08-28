# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VulUrgentResponseInfoDataList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'label_list': 'list[str]',
        'repair_priority': 'str',
        'repair_success_num': 'int',
        'vul_id': 'str',
        'vul_name': 'str',
        'cve_list': 'list[VulUrgentResponseInfoCveList]',
        'is_affected_business': 'bool',
        'host_id': 'str',
        'public_ip': 'str',
        'private_ip': 'str',
        'host_name': 'str',
        'asset_value': 'str',
        'status': 'str',
        'first_scan_time': 'int',
        'scan_time': 'int',
        'disabled_operate_types': 'list[VulUrgentResponseInfoDisabledOperateTypes]'
    }

    attribute_map = {
        'label_list': 'label_list',
        'repair_priority': 'repair_priority',
        'repair_success_num': 'repair_success_num',
        'vul_id': 'vul_id',
        'vul_name': 'vul_name',
        'cve_list': 'cve_list',
        'is_affected_business': 'is_affected_business',
        'host_id': 'host_id',
        'public_ip': 'public_ip',
        'private_ip': 'private_ip',
        'host_name': 'host_name',
        'asset_value': 'asset_value',
        'status': 'status',
        'first_scan_time': 'first_scan_time',
        'scan_time': 'scan_time',
        'disabled_operate_types': 'disabled_operate_types'
    }

    def __init__(self, label_list=None, repair_priority=None, repair_success_num=None, vul_id=None, vul_name=None, cve_list=None, is_affected_business=None, host_id=None, public_ip=None, private_ip=None, host_name=None, asset_value=None, status=None, first_scan_time=None, scan_time=None, disabled_operate_types=None):
        r"""VulUrgentResponseInfoDataList

        The model defined in huaweicloud sdk

        :param label_list: **参数解释**: 漏洞标签列表 **取值范围**: 最小值0，最大值2147483647 
        :type label_list: list[str]
        :param repair_priority: **参数解释**: 修复优先级 **取值范围**: - Critical：紧急。 - High：高。 - Medium：中。 - Low：低。 
        :type repair_priority: str
        :param repair_success_num: **参数解释**: 当前漏洞修复成功次数 **取值范围**: 最小值0，最大值1000000 
        :type repair_success_num: int
        :param vul_id: **参数解释**: 漏洞ID **取值范围**: 字符范围0-64位 
        :type vul_id: str
        :param vul_name: **参数解释**: 漏洞名称 **取值范围**: 字符范围0-256位 
        :type vul_name: str
        :param cve_list: **参数解释**: CVE列表 **取值范围**: 最小值1，最大值10000 
        :type cve_list: list[:class:`huaweicloudsdkhss.v5.VulUrgentResponseInfoCveList`]
        :param is_affected_business: **参数解释**: 是否影响业务 **取值范围**: - true：是。 - false：否。 
        :type is_affected_business: bool
        :param host_id: **参数解释**: 主机ID **取值范围**: 字符长度1-64 
        :type host_id: str
        :param public_ip: **参数解释**: 服务器公网IP **取值范围**: 字符长度0-128 
        :type public_ip: str
        :param private_ip: **参数解释**: 服务器私网IP **取值范围**: 字符长度0-128 
        :type private_ip: str
        :param host_name: **参数解释**: 主机名称 **取值范围**: 字符长度1-128位 
        :type host_name: str
        :param asset_value: **参数解释**: 修复优先级 **取值范围**: - Critical：紧急。 - High：高。 - Medium：中。 - Low：低。 
        :type asset_value: str
        :param status: **参数解释**： 漏洞状态 **取值范围**： 字符长度0-32位 
        :type status: str
        :param first_scan_time: **参数解释**: 首次扫描时间 **取值范围**: 最小值0，最大值9223372036854775807 
        :type first_scan_time: int
        :param scan_time: **参数解释**: 最近扫描时间 **取值范围**: 最小值0，最大值9223372036854775807 
        :type scan_time: int
        :param disabled_operate_types: **参数解释**: 该漏洞不可进行的操作类型列表 **取值范围**: 最小值1，最大值10000 
        :type disabled_operate_types: list[:class:`huaweicloudsdkhss.v5.VulUrgentResponseInfoDisabledOperateTypes`]
        """
        
        

        self._label_list = None
        self._repair_priority = None
        self._repair_success_num = None
        self._vul_id = None
        self._vul_name = None
        self._cve_list = None
        self._is_affected_business = None
        self._host_id = None
        self._public_ip = None
        self._private_ip = None
        self._host_name = None
        self._asset_value = None
        self._status = None
        self._first_scan_time = None
        self._scan_time = None
        self._disabled_operate_types = None
        self.discriminator = None

        if label_list is not None:
            self.label_list = label_list
        if repair_priority is not None:
            self.repair_priority = repair_priority
        if repair_success_num is not None:
            self.repair_success_num = repair_success_num
        if vul_id is not None:
            self.vul_id = vul_id
        if vul_name is not None:
            self.vul_name = vul_name
        if cve_list is not None:
            self.cve_list = cve_list
        if is_affected_business is not None:
            self.is_affected_business = is_affected_business
        if host_id is not None:
            self.host_id = host_id
        if public_ip is not None:
            self.public_ip = public_ip
        if private_ip is not None:
            self.private_ip = private_ip
        if host_name is not None:
            self.host_name = host_name
        if asset_value is not None:
            self.asset_value = asset_value
        if status is not None:
            self.status = status
        if first_scan_time is not None:
            self.first_scan_time = first_scan_time
        if scan_time is not None:
            self.scan_time = scan_time
        if disabled_operate_types is not None:
            self.disabled_operate_types = disabled_operate_types

    @property
    def label_list(self):
        r"""Gets the label_list of this VulUrgentResponseInfoDataList.

        **参数解释**: 漏洞标签列表 **取值范围**: 最小值0，最大值2147483647 

        :return: The label_list of this VulUrgentResponseInfoDataList.
        :rtype: list[str]
        """
        return self._label_list

    @label_list.setter
    def label_list(self, label_list):
        r"""Sets the label_list of this VulUrgentResponseInfoDataList.

        **参数解释**: 漏洞标签列表 **取值范围**: 最小值0，最大值2147483647 

        :param label_list: The label_list of this VulUrgentResponseInfoDataList.
        :type label_list: list[str]
        """
        self._label_list = label_list

    @property
    def repair_priority(self):
        r"""Gets the repair_priority of this VulUrgentResponseInfoDataList.

        **参数解释**: 修复优先级 **取值范围**: - Critical：紧急。 - High：高。 - Medium：中。 - Low：低。 

        :return: The repair_priority of this VulUrgentResponseInfoDataList.
        :rtype: str
        """
        return self._repair_priority

    @repair_priority.setter
    def repair_priority(self, repair_priority):
        r"""Sets the repair_priority of this VulUrgentResponseInfoDataList.

        **参数解释**: 修复优先级 **取值范围**: - Critical：紧急。 - High：高。 - Medium：中。 - Low：低。 

        :param repair_priority: The repair_priority of this VulUrgentResponseInfoDataList.
        :type repair_priority: str
        """
        self._repair_priority = repair_priority

    @property
    def repair_success_num(self):
        r"""Gets the repair_success_num of this VulUrgentResponseInfoDataList.

        **参数解释**: 当前漏洞修复成功次数 **取值范围**: 最小值0，最大值1000000 

        :return: The repair_success_num of this VulUrgentResponseInfoDataList.
        :rtype: int
        """
        return self._repair_success_num

    @repair_success_num.setter
    def repair_success_num(self, repair_success_num):
        r"""Sets the repair_success_num of this VulUrgentResponseInfoDataList.

        **参数解释**: 当前漏洞修复成功次数 **取值范围**: 最小值0，最大值1000000 

        :param repair_success_num: The repair_success_num of this VulUrgentResponseInfoDataList.
        :type repair_success_num: int
        """
        self._repair_success_num = repair_success_num

    @property
    def vul_id(self):
        r"""Gets the vul_id of this VulUrgentResponseInfoDataList.

        **参数解释**: 漏洞ID **取值范围**: 字符范围0-64位 

        :return: The vul_id of this VulUrgentResponseInfoDataList.
        :rtype: str
        """
        return self._vul_id

    @vul_id.setter
    def vul_id(self, vul_id):
        r"""Sets the vul_id of this VulUrgentResponseInfoDataList.

        **参数解释**: 漏洞ID **取值范围**: 字符范围0-64位 

        :param vul_id: The vul_id of this VulUrgentResponseInfoDataList.
        :type vul_id: str
        """
        self._vul_id = vul_id

    @property
    def vul_name(self):
        r"""Gets the vul_name of this VulUrgentResponseInfoDataList.

        **参数解释**: 漏洞名称 **取值范围**: 字符范围0-256位 

        :return: The vul_name of this VulUrgentResponseInfoDataList.
        :rtype: str
        """
        return self._vul_name

    @vul_name.setter
    def vul_name(self, vul_name):
        r"""Sets the vul_name of this VulUrgentResponseInfoDataList.

        **参数解释**: 漏洞名称 **取值范围**: 字符范围0-256位 

        :param vul_name: The vul_name of this VulUrgentResponseInfoDataList.
        :type vul_name: str
        """
        self._vul_name = vul_name

    @property
    def cve_list(self):
        r"""Gets the cve_list of this VulUrgentResponseInfoDataList.

        **参数解释**: CVE列表 **取值范围**: 最小值1，最大值10000 

        :return: The cve_list of this VulUrgentResponseInfoDataList.
        :rtype: list[:class:`huaweicloudsdkhss.v5.VulUrgentResponseInfoCveList`]
        """
        return self._cve_list

    @cve_list.setter
    def cve_list(self, cve_list):
        r"""Sets the cve_list of this VulUrgentResponseInfoDataList.

        **参数解释**: CVE列表 **取值范围**: 最小值1，最大值10000 

        :param cve_list: The cve_list of this VulUrgentResponseInfoDataList.
        :type cve_list: list[:class:`huaweicloudsdkhss.v5.VulUrgentResponseInfoCveList`]
        """
        self._cve_list = cve_list

    @property
    def is_affected_business(self):
        r"""Gets the is_affected_business of this VulUrgentResponseInfoDataList.

        **参数解释**: 是否影响业务 **取值范围**: - true：是。 - false：否。 

        :return: The is_affected_business of this VulUrgentResponseInfoDataList.
        :rtype: bool
        """
        return self._is_affected_business

    @is_affected_business.setter
    def is_affected_business(self, is_affected_business):
        r"""Sets the is_affected_business of this VulUrgentResponseInfoDataList.

        **参数解释**: 是否影响业务 **取值范围**: - true：是。 - false：否。 

        :param is_affected_business: The is_affected_business of this VulUrgentResponseInfoDataList.
        :type is_affected_business: bool
        """
        self._is_affected_business = is_affected_business

    @property
    def host_id(self):
        r"""Gets the host_id of this VulUrgentResponseInfoDataList.

        **参数解释**: 主机ID **取值范围**: 字符长度1-64 

        :return: The host_id of this VulUrgentResponseInfoDataList.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this VulUrgentResponseInfoDataList.

        **参数解释**: 主机ID **取值范围**: 字符长度1-64 

        :param host_id: The host_id of this VulUrgentResponseInfoDataList.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def public_ip(self):
        r"""Gets the public_ip of this VulUrgentResponseInfoDataList.

        **参数解释**: 服务器公网IP **取值范围**: 字符长度0-128 

        :return: The public_ip of this VulUrgentResponseInfoDataList.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this VulUrgentResponseInfoDataList.

        **参数解释**: 服务器公网IP **取值范围**: 字符长度0-128 

        :param public_ip: The public_ip of this VulUrgentResponseInfoDataList.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def private_ip(self):
        r"""Gets the private_ip of this VulUrgentResponseInfoDataList.

        **参数解释**: 服务器私网IP **取值范围**: 字符长度0-128 

        :return: The private_ip of this VulUrgentResponseInfoDataList.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this VulUrgentResponseInfoDataList.

        **参数解释**: 服务器私网IP **取值范围**: 字符长度0-128 

        :param private_ip: The private_ip of this VulUrgentResponseInfoDataList.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def host_name(self):
        r"""Gets the host_name of this VulUrgentResponseInfoDataList.

        **参数解释**: 主机名称 **取值范围**: 字符长度1-128位 

        :return: The host_name of this VulUrgentResponseInfoDataList.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this VulUrgentResponseInfoDataList.

        **参数解释**: 主机名称 **取值范围**: 字符长度1-128位 

        :param host_name: The host_name of this VulUrgentResponseInfoDataList.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def asset_value(self):
        r"""Gets the asset_value of this VulUrgentResponseInfoDataList.

        **参数解释**: 修复优先级 **取值范围**: - Critical：紧急。 - High：高。 - Medium：中。 - Low：低。 

        :return: The asset_value of this VulUrgentResponseInfoDataList.
        :rtype: str
        """
        return self._asset_value

    @asset_value.setter
    def asset_value(self, asset_value):
        r"""Sets the asset_value of this VulUrgentResponseInfoDataList.

        **参数解释**: 修复优先级 **取值范围**: - Critical：紧急。 - High：高。 - Medium：中。 - Low：低。 

        :param asset_value: The asset_value of this VulUrgentResponseInfoDataList.
        :type asset_value: str
        """
        self._asset_value = asset_value

    @property
    def status(self):
        r"""Gets the status of this VulUrgentResponseInfoDataList.

        **参数解释**： 漏洞状态 **取值范围**： 字符长度0-32位 

        :return: The status of this VulUrgentResponseInfoDataList.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this VulUrgentResponseInfoDataList.

        **参数解释**： 漏洞状态 **取值范围**： 字符长度0-32位 

        :param status: The status of this VulUrgentResponseInfoDataList.
        :type status: str
        """
        self._status = status

    @property
    def first_scan_time(self):
        r"""Gets the first_scan_time of this VulUrgentResponseInfoDataList.

        **参数解释**: 首次扫描时间 **取值范围**: 最小值0，最大值9223372036854775807 

        :return: The first_scan_time of this VulUrgentResponseInfoDataList.
        :rtype: int
        """
        return self._first_scan_time

    @first_scan_time.setter
    def first_scan_time(self, first_scan_time):
        r"""Sets the first_scan_time of this VulUrgentResponseInfoDataList.

        **参数解释**: 首次扫描时间 **取值范围**: 最小值0，最大值9223372036854775807 

        :param first_scan_time: The first_scan_time of this VulUrgentResponseInfoDataList.
        :type first_scan_time: int
        """
        self._first_scan_time = first_scan_time

    @property
    def scan_time(self):
        r"""Gets the scan_time of this VulUrgentResponseInfoDataList.

        **参数解释**: 最近扫描时间 **取值范围**: 最小值0，最大值9223372036854775807 

        :return: The scan_time of this VulUrgentResponseInfoDataList.
        :rtype: int
        """
        return self._scan_time

    @scan_time.setter
    def scan_time(self, scan_time):
        r"""Sets the scan_time of this VulUrgentResponseInfoDataList.

        **参数解释**: 最近扫描时间 **取值范围**: 最小值0，最大值9223372036854775807 

        :param scan_time: The scan_time of this VulUrgentResponseInfoDataList.
        :type scan_time: int
        """
        self._scan_time = scan_time

    @property
    def disabled_operate_types(self):
        r"""Gets the disabled_operate_types of this VulUrgentResponseInfoDataList.

        **参数解释**: 该漏洞不可进行的操作类型列表 **取值范围**: 最小值1，最大值10000 

        :return: The disabled_operate_types of this VulUrgentResponseInfoDataList.
        :rtype: list[:class:`huaweicloudsdkhss.v5.VulUrgentResponseInfoDisabledOperateTypes`]
        """
        return self._disabled_operate_types

    @disabled_operate_types.setter
    def disabled_operate_types(self, disabled_operate_types):
        r"""Sets the disabled_operate_types of this VulUrgentResponseInfoDataList.

        **参数解释**: 该漏洞不可进行的操作类型列表 **取值范围**: 最小值1，最大值10000 

        :param disabled_operate_types: The disabled_operate_types of this VulUrgentResponseInfoDataList.
        :type disabled_operate_types: list[:class:`huaweicloudsdkhss.v5.VulUrgentResponseInfoDisabledOperateTypes`]
        """
        self._disabled_operate_types = disabled_operate_types

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
        if not isinstance(other, VulUrgentResponseInfoDataList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
