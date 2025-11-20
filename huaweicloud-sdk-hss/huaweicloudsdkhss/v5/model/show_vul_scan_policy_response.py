# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowVulScanPolicyResponse(SdkResponse):

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
        'scan_vul_types': 'list[str]',
        'scan_range_type': 'str',
        'host_ids': 'list[str]',
        'total_host_num': 'int',
        'status': 'str',
        'time': 'VulScanPolicyResponseInfoTime'
    }

    attribute_map = {
        'scan_period': 'scan_period',
        'scan_vul_types': 'scan_vul_types',
        'scan_range_type': 'scan_range_type',
        'host_ids': 'host_ids',
        'total_host_num': 'total_host_num',
        'status': 'status',
        'time': 'time'
    }

    def __init__(self, scan_period=None, scan_vul_types=None, scan_range_type=None, host_ids=None, total_host_num=None, status=None, time=None):
        r"""ShowVulScanPolicyResponse

        The model defined in huaweicloud sdk

        :param scan_period: **参数解释**: 扫描周期 **取值范围**: - one_day：每天 - three_day：每三天 - one_week：每周 - one_month：每月 
        :type scan_period: str
        :param scan_vul_types: **参数解释**: \&quot;扫描的漏洞类型列表\&quot; **取值范围**: 最小值0，最大值5 
        :type scan_vul_types: list[str]
        :param scan_range_type: **参数解释**: 扫描主机的范围 **取值范围**: - all_host：扫描全部主机 - specific_host：扫描指定主机 
        :type scan_range_type: str
        :param host_ids: **参数解释**: 主机ID列表；当scan_range_type的值为specific_host时表示扫描的主机列表 **取值范围**: 最小值0，最大值20000 
        :type host_ids: list[str]
        :param total_host_num: **参数解释**: 可进行漏洞扫描的主机总数 **取值范围**: 最小值0，最大值20000 
        :type total_host_num: int
        :param status: **参数解释**: 扫描策略状态 **取值范围**: - open : 开启 - close : 关闭 
        :type status: str
        :param time: 
        :type time: :class:`huaweicloudsdkhss.v5.VulScanPolicyResponseInfoTime`
        """
        
        super().__init__()

        self._scan_period = None
        self._scan_vul_types = None
        self._scan_range_type = None
        self._host_ids = None
        self._total_host_num = None
        self._status = None
        self._time = None
        self.discriminator = None

        if scan_period is not None:
            self.scan_period = scan_period
        if scan_vul_types is not None:
            self.scan_vul_types = scan_vul_types
        if scan_range_type is not None:
            self.scan_range_type = scan_range_type
        if host_ids is not None:
            self.host_ids = host_ids
        if total_host_num is not None:
            self.total_host_num = total_host_num
        if status is not None:
            self.status = status
        if time is not None:
            self.time = time

    @property
    def scan_period(self):
        r"""Gets the scan_period of this ShowVulScanPolicyResponse.

        **参数解释**: 扫描周期 **取值范围**: - one_day：每天 - three_day：每三天 - one_week：每周 - one_month：每月 

        :return: The scan_period of this ShowVulScanPolicyResponse.
        :rtype: str
        """
        return self._scan_period

    @scan_period.setter
    def scan_period(self, scan_period):
        r"""Sets the scan_period of this ShowVulScanPolicyResponse.

        **参数解释**: 扫描周期 **取值范围**: - one_day：每天 - three_day：每三天 - one_week：每周 - one_month：每月 

        :param scan_period: The scan_period of this ShowVulScanPolicyResponse.
        :type scan_period: str
        """
        self._scan_period = scan_period

    @property
    def scan_vul_types(self):
        r"""Gets the scan_vul_types of this ShowVulScanPolicyResponse.

        **参数解释**: \"扫描的漏洞类型列表\" **取值范围**: 最小值0，最大值5 

        :return: The scan_vul_types of this ShowVulScanPolicyResponse.
        :rtype: list[str]
        """
        return self._scan_vul_types

    @scan_vul_types.setter
    def scan_vul_types(self, scan_vul_types):
        r"""Sets the scan_vul_types of this ShowVulScanPolicyResponse.

        **参数解释**: \"扫描的漏洞类型列表\" **取值范围**: 最小值0，最大值5 

        :param scan_vul_types: The scan_vul_types of this ShowVulScanPolicyResponse.
        :type scan_vul_types: list[str]
        """
        self._scan_vul_types = scan_vul_types

    @property
    def scan_range_type(self):
        r"""Gets the scan_range_type of this ShowVulScanPolicyResponse.

        **参数解释**: 扫描主机的范围 **取值范围**: - all_host：扫描全部主机 - specific_host：扫描指定主机 

        :return: The scan_range_type of this ShowVulScanPolicyResponse.
        :rtype: str
        """
        return self._scan_range_type

    @scan_range_type.setter
    def scan_range_type(self, scan_range_type):
        r"""Sets the scan_range_type of this ShowVulScanPolicyResponse.

        **参数解释**: 扫描主机的范围 **取值范围**: - all_host：扫描全部主机 - specific_host：扫描指定主机 

        :param scan_range_type: The scan_range_type of this ShowVulScanPolicyResponse.
        :type scan_range_type: str
        """
        self._scan_range_type = scan_range_type

    @property
    def host_ids(self):
        r"""Gets the host_ids of this ShowVulScanPolicyResponse.

        **参数解释**: 主机ID列表；当scan_range_type的值为specific_host时表示扫描的主机列表 **取值范围**: 最小值0，最大值20000 

        :return: The host_ids of this ShowVulScanPolicyResponse.
        :rtype: list[str]
        """
        return self._host_ids

    @host_ids.setter
    def host_ids(self, host_ids):
        r"""Sets the host_ids of this ShowVulScanPolicyResponse.

        **参数解释**: 主机ID列表；当scan_range_type的值为specific_host时表示扫描的主机列表 **取值范围**: 最小值0，最大值20000 

        :param host_ids: The host_ids of this ShowVulScanPolicyResponse.
        :type host_ids: list[str]
        """
        self._host_ids = host_ids

    @property
    def total_host_num(self):
        r"""Gets the total_host_num of this ShowVulScanPolicyResponse.

        **参数解释**: 可进行漏洞扫描的主机总数 **取值范围**: 最小值0，最大值20000 

        :return: The total_host_num of this ShowVulScanPolicyResponse.
        :rtype: int
        """
        return self._total_host_num

    @total_host_num.setter
    def total_host_num(self, total_host_num):
        r"""Sets the total_host_num of this ShowVulScanPolicyResponse.

        **参数解释**: 可进行漏洞扫描的主机总数 **取值范围**: 最小值0，最大值20000 

        :param total_host_num: The total_host_num of this ShowVulScanPolicyResponse.
        :type total_host_num: int
        """
        self._total_host_num = total_host_num

    @property
    def status(self):
        r"""Gets the status of this ShowVulScanPolicyResponse.

        **参数解释**: 扫描策略状态 **取值范围**: - open : 开启 - close : 关闭 

        :return: The status of this ShowVulScanPolicyResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowVulScanPolicyResponse.

        **参数解释**: 扫描策略状态 **取值范围**: - open : 开启 - close : 关闭 

        :param status: The status of this ShowVulScanPolicyResponse.
        :type status: str
        """
        self._status = status

    @property
    def time(self):
        r"""Gets the time of this ShowVulScanPolicyResponse.

        :return: The time of this ShowVulScanPolicyResponse.
        :rtype: :class:`huaweicloudsdkhss.v5.VulScanPolicyResponseInfoTime`
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this ShowVulScanPolicyResponse.

        :param time: The time of this ShowVulScanPolicyResponse.
        :type time: :class:`huaweicloudsdkhss.v5.VulScanPolicyResponseInfoTime`
        """
        self._time = time

    def to_dict(self):
        import warnings
        warnings.warn("ShowVulScanPolicyResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowVulScanPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
