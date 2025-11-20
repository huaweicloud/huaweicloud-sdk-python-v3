# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeVulScanPolicyRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scan_period': 'str',
        'scan_range_type': 'str',
        'host_ids': 'list[str]',
        'scan_vul_types': 'list[str]',
        'status': 'str',
        'time': 'ChangeVulScanPolicyRequestInfoTime'
    }

    attribute_map = {
        'scan_period': 'scan_period',
        'scan_range_type': 'scan_range_type',
        'host_ids': 'host_ids',
        'scan_vul_types': 'scan_vul_types',
        'status': 'status',
        'time': 'time'
    }

    def __init__(self, scan_period=None, scan_range_type=None, host_ids=None, scan_vul_types=None, status=None, time=None):
        r"""ChangeVulScanPolicyRequestInfo

        The model defined in huaweicloud sdk

        :param scan_period: **参数解释**: 扫描周期 **约束限制**: 不涉及 **取值范围**: - one_day：每天 - three_day：每三天 - one_week：每周 - one_month：每月 **默认取值**: 不涉及 
        :type scan_period: str
        :param scan_range_type: **参数解释**: 扫描主机的范围 **约束限制**: 不涉及 **取值范围**: - all_host：扫描全部主机 - specific_host：扫描指定主机 **默认取值**: 不涉及 
        :type scan_range_type: str
        :param host_ids: **参数解释**: 主机ID列表； **约束限制**: 当scan_range_type的值为specific_host时 表示扫描的主机列表 必填 **取值范围**: 最小值0，最大值20000 **默认取值**: 不涉及 
        :type host_ids: list[str]
        :param scan_vul_types: **参数解释**: \&quot;扫描的漏洞类型列表\&quot; **约束限制**: 不涉及 **取值范围**: 最小值0，最大值5 **默认取值**: 不涉及 
        :type scan_vul_types: list[str]
        :param status: **参数解释**: 扫描策略状态 **约束限制**: 不涉及 **取值范围**: - open : 开启 - close : 关闭  **默认取值** : 不涉及 
        :type status: str
        :param time: 
        :type time: :class:`huaweicloudsdkhss.v5.ChangeVulScanPolicyRequestInfoTime`
        """
        
        

        self._scan_period = None
        self._scan_range_type = None
        self._host_ids = None
        self._scan_vul_types = None
        self._status = None
        self._time = None
        self.discriminator = None

        self.scan_period = scan_period
        self.scan_range_type = scan_range_type
        if host_ids is not None:
            self.host_ids = host_ids
        if scan_vul_types is not None:
            self.scan_vul_types = scan_vul_types
        self.status = status
        if time is not None:
            self.time = time

    @property
    def scan_period(self):
        r"""Gets the scan_period of this ChangeVulScanPolicyRequestInfo.

        **参数解释**: 扫描周期 **约束限制**: 不涉及 **取值范围**: - one_day：每天 - three_day：每三天 - one_week：每周 - one_month：每月 **默认取值**: 不涉及 

        :return: The scan_period of this ChangeVulScanPolicyRequestInfo.
        :rtype: str
        """
        return self._scan_period

    @scan_period.setter
    def scan_period(self, scan_period):
        r"""Sets the scan_period of this ChangeVulScanPolicyRequestInfo.

        **参数解释**: 扫描周期 **约束限制**: 不涉及 **取值范围**: - one_day：每天 - three_day：每三天 - one_week：每周 - one_month：每月 **默认取值**: 不涉及 

        :param scan_period: The scan_period of this ChangeVulScanPolicyRequestInfo.
        :type scan_period: str
        """
        self._scan_period = scan_period

    @property
    def scan_range_type(self):
        r"""Gets the scan_range_type of this ChangeVulScanPolicyRequestInfo.

        **参数解释**: 扫描主机的范围 **约束限制**: 不涉及 **取值范围**: - all_host：扫描全部主机 - specific_host：扫描指定主机 **默认取值**: 不涉及 

        :return: The scan_range_type of this ChangeVulScanPolicyRequestInfo.
        :rtype: str
        """
        return self._scan_range_type

    @scan_range_type.setter
    def scan_range_type(self, scan_range_type):
        r"""Sets the scan_range_type of this ChangeVulScanPolicyRequestInfo.

        **参数解释**: 扫描主机的范围 **约束限制**: 不涉及 **取值范围**: - all_host：扫描全部主机 - specific_host：扫描指定主机 **默认取值**: 不涉及 

        :param scan_range_type: The scan_range_type of this ChangeVulScanPolicyRequestInfo.
        :type scan_range_type: str
        """
        self._scan_range_type = scan_range_type

    @property
    def host_ids(self):
        r"""Gets the host_ids of this ChangeVulScanPolicyRequestInfo.

        **参数解释**: 主机ID列表； **约束限制**: 当scan_range_type的值为specific_host时 表示扫描的主机列表 必填 **取值范围**: 最小值0，最大值20000 **默认取值**: 不涉及 

        :return: The host_ids of this ChangeVulScanPolicyRequestInfo.
        :rtype: list[str]
        """
        return self._host_ids

    @host_ids.setter
    def host_ids(self, host_ids):
        r"""Sets the host_ids of this ChangeVulScanPolicyRequestInfo.

        **参数解释**: 主机ID列表； **约束限制**: 当scan_range_type的值为specific_host时 表示扫描的主机列表 必填 **取值范围**: 最小值0，最大值20000 **默认取值**: 不涉及 

        :param host_ids: The host_ids of this ChangeVulScanPolicyRequestInfo.
        :type host_ids: list[str]
        """
        self._host_ids = host_ids

    @property
    def scan_vul_types(self):
        r"""Gets the scan_vul_types of this ChangeVulScanPolicyRequestInfo.

        **参数解释**: \"扫描的漏洞类型列表\" **约束限制**: 不涉及 **取值范围**: 最小值0，最大值5 **默认取值**: 不涉及 

        :return: The scan_vul_types of this ChangeVulScanPolicyRequestInfo.
        :rtype: list[str]
        """
        return self._scan_vul_types

    @scan_vul_types.setter
    def scan_vul_types(self, scan_vul_types):
        r"""Sets the scan_vul_types of this ChangeVulScanPolicyRequestInfo.

        **参数解释**: \"扫描的漏洞类型列表\" **约束限制**: 不涉及 **取值范围**: 最小值0，最大值5 **默认取值**: 不涉及 

        :param scan_vul_types: The scan_vul_types of this ChangeVulScanPolicyRequestInfo.
        :type scan_vul_types: list[str]
        """
        self._scan_vul_types = scan_vul_types

    @property
    def status(self):
        r"""Gets the status of this ChangeVulScanPolicyRequestInfo.

        **参数解释**: 扫描策略状态 **约束限制**: 不涉及 **取值范围**: - open : 开启 - close : 关闭  **默认取值** : 不涉及 

        :return: The status of this ChangeVulScanPolicyRequestInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ChangeVulScanPolicyRequestInfo.

        **参数解释**: 扫描策略状态 **约束限制**: 不涉及 **取值范围**: - open : 开启 - close : 关闭  **默认取值** : 不涉及 

        :param status: The status of this ChangeVulScanPolicyRequestInfo.
        :type status: str
        """
        self._status = status

    @property
    def time(self):
        r"""Gets the time of this ChangeVulScanPolicyRequestInfo.

        :return: The time of this ChangeVulScanPolicyRequestInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.ChangeVulScanPolicyRequestInfoTime`
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this ChangeVulScanPolicyRequestInfo.

        :param time: The time of this ChangeVulScanPolicyRequestInfo.
        :type time: :class:`huaweicloudsdkhss.v5.ChangeVulScanPolicyRequestInfoTime`
        """
        self._time = time

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
        if not isinstance(other, ChangeVulScanPolicyRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
