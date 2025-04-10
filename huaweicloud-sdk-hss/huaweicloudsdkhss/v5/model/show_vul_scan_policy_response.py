# coding: utf-8

import six

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
        'status': 'str'
    }

    attribute_map = {
        'scan_period': 'scan_period',
        'scan_vul_types': 'scan_vul_types',
        'scan_range_type': 'scan_range_type',
        'host_ids': 'host_ids',
        'total_host_num': 'total_host_num',
        'status': 'status'
    }

    def __init__(self, scan_period=None, scan_vul_types=None, scan_range_type=None, host_ids=None, total_host_num=None, status=None):
        r"""ShowVulScanPolicyResponse

        The model defined in huaweicloud sdk

        :param scan_period: 扫描周期 - one_day : 每天 - three_day : 每三天 - one_week : 每周
        :type scan_period: str
        :param scan_vul_types: 扫描的漏洞类型列表
        :type scan_vul_types: list[str]
        :param scan_range_type: 扫描主机的范围，包含如下：   -all_host : 扫描全部主机   -specific_host : 扫描指定主机
        :type scan_range_type: str
        :param host_ids: 主机ID列表；当scan_range_type的值为specific_host时表示扫描的主机列表
        :type host_ids: list[str]
        :param total_host_num: 可进行漏洞扫描的主机总数
        :type total_host_num: int
        :param status: 扫描策略状态，包含如下：   -open : 开启   -close : 关闭
        :type status: str
        """
        
        super(ShowVulScanPolicyResponse, self).__init__()

        self._scan_period = None
        self._scan_vul_types = None
        self._scan_range_type = None
        self._host_ids = None
        self._total_host_num = None
        self._status = None
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

    @property
    def scan_period(self):
        r"""Gets the scan_period of this ShowVulScanPolicyResponse.

        扫描周期 - one_day : 每天 - three_day : 每三天 - one_week : 每周

        :return: The scan_period of this ShowVulScanPolicyResponse.
        :rtype: str
        """
        return self._scan_period

    @scan_period.setter
    def scan_period(self, scan_period):
        r"""Sets the scan_period of this ShowVulScanPolicyResponse.

        扫描周期 - one_day : 每天 - three_day : 每三天 - one_week : 每周

        :param scan_period: The scan_period of this ShowVulScanPolicyResponse.
        :type scan_period: str
        """
        self._scan_period = scan_period

    @property
    def scan_vul_types(self):
        r"""Gets the scan_vul_types of this ShowVulScanPolicyResponse.

        扫描的漏洞类型列表

        :return: The scan_vul_types of this ShowVulScanPolicyResponse.
        :rtype: list[str]
        """
        return self._scan_vul_types

    @scan_vul_types.setter
    def scan_vul_types(self, scan_vul_types):
        r"""Sets the scan_vul_types of this ShowVulScanPolicyResponse.

        扫描的漏洞类型列表

        :param scan_vul_types: The scan_vul_types of this ShowVulScanPolicyResponse.
        :type scan_vul_types: list[str]
        """
        self._scan_vul_types = scan_vul_types

    @property
    def scan_range_type(self):
        r"""Gets the scan_range_type of this ShowVulScanPolicyResponse.

        扫描主机的范围，包含如下：   -all_host : 扫描全部主机   -specific_host : 扫描指定主机

        :return: The scan_range_type of this ShowVulScanPolicyResponse.
        :rtype: str
        """
        return self._scan_range_type

    @scan_range_type.setter
    def scan_range_type(self, scan_range_type):
        r"""Sets the scan_range_type of this ShowVulScanPolicyResponse.

        扫描主机的范围，包含如下：   -all_host : 扫描全部主机   -specific_host : 扫描指定主机

        :param scan_range_type: The scan_range_type of this ShowVulScanPolicyResponse.
        :type scan_range_type: str
        """
        self._scan_range_type = scan_range_type

    @property
    def host_ids(self):
        r"""Gets the host_ids of this ShowVulScanPolicyResponse.

        主机ID列表；当scan_range_type的值为specific_host时表示扫描的主机列表

        :return: The host_ids of this ShowVulScanPolicyResponse.
        :rtype: list[str]
        """
        return self._host_ids

    @host_ids.setter
    def host_ids(self, host_ids):
        r"""Sets the host_ids of this ShowVulScanPolicyResponse.

        主机ID列表；当scan_range_type的值为specific_host时表示扫描的主机列表

        :param host_ids: The host_ids of this ShowVulScanPolicyResponse.
        :type host_ids: list[str]
        """
        self._host_ids = host_ids

    @property
    def total_host_num(self):
        r"""Gets the total_host_num of this ShowVulScanPolicyResponse.

        可进行漏洞扫描的主机总数

        :return: The total_host_num of this ShowVulScanPolicyResponse.
        :rtype: int
        """
        return self._total_host_num

    @total_host_num.setter
    def total_host_num(self, total_host_num):
        r"""Sets the total_host_num of this ShowVulScanPolicyResponse.

        可进行漏洞扫描的主机总数

        :param total_host_num: The total_host_num of this ShowVulScanPolicyResponse.
        :type total_host_num: int
        """
        self._total_host_num = total_host_num

    @property
    def status(self):
        r"""Gets the status of this ShowVulScanPolicyResponse.

        扫描策略状态，包含如下：   -open : 开启   -close : 关闭

        :return: The status of this ShowVulScanPolicyResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowVulScanPolicyResponse.

        扫描策略状态，包含如下：   -open : 开启   -close : 关闭

        :param status: The status of this ShowVulScanPolicyResponse.
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
        if not isinstance(other, ShowVulScanPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
