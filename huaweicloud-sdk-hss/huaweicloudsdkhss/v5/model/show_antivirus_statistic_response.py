# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAntivirusStatisticResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_malware_num': 'int',
        'malware_host_num': 'int',
        'total_task_num': 'int',
        'scanning_task_num': 'int',
        'latest_scan_time': 'int',
        'scan_type': 'str'
    }

    attribute_map = {
        'total_malware_num': 'total_malware_num',
        'malware_host_num': 'malware_host_num',
        'total_task_num': 'total_task_num',
        'scanning_task_num': 'scanning_task_num',
        'latest_scan_time': 'latest_scan_time',
        'scan_type': 'scan_type'
    }

    def __init__(self, total_malware_num=None, malware_host_num=None, total_task_num=None, scanning_task_num=None, latest_scan_time=None, scan_type=None):
        r"""ShowAntivirusStatisticResponse

        The model defined in huaweicloud sdk

        :param total_malware_num: 病毒总数
        :type total_malware_num: int
        :param malware_host_num: **参数解释**: 影响主机数量 **取值范围**: 最小值0，最大值2147483647 
        :type malware_host_num: int
        :param total_task_num: 累计扫描任务数
        :type total_task_num: int
        :param scanning_task_num: 运行中任务数
        :type scanning_task_num: int
        :param latest_scan_time: 启动时间，毫秒
        :type latest_scan_time: int
        :param scan_type: 任务类型，包含如下:   - quick ：快速扫描   - full : 全盘扫描   - custom : 自定义扫描
        :type scan_type: str
        """
        
        super(ShowAntivirusStatisticResponse, self).__init__()

        self._total_malware_num = None
        self._malware_host_num = None
        self._total_task_num = None
        self._scanning_task_num = None
        self._latest_scan_time = None
        self._scan_type = None
        self.discriminator = None

        if total_malware_num is not None:
            self.total_malware_num = total_malware_num
        if malware_host_num is not None:
            self.malware_host_num = malware_host_num
        if total_task_num is not None:
            self.total_task_num = total_task_num
        if scanning_task_num is not None:
            self.scanning_task_num = scanning_task_num
        if latest_scan_time is not None:
            self.latest_scan_time = latest_scan_time
        if scan_type is not None:
            self.scan_type = scan_type

    @property
    def total_malware_num(self):
        r"""Gets the total_malware_num of this ShowAntivirusStatisticResponse.

        病毒总数

        :return: The total_malware_num of this ShowAntivirusStatisticResponse.
        :rtype: int
        """
        return self._total_malware_num

    @total_malware_num.setter
    def total_malware_num(self, total_malware_num):
        r"""Sets the total_malware_num of this ShowAntivirusStatisticResponse.

        病毒总数

        :param total_malware_num: The total_malware_num of this ShowAntivirusStatisticResponse.
        :type total_malware_num: int
        """
        self._total_malware_num = total_malware_num

    @property
    def malware_host_num(self):
        r"""Gets the malware_host_num of this ShowAntivirusStatisticResponse.

        **参数解释**: 影响主机数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The malware_host_num of this ShowAntivirusStatisticResponse.
        :rtype: int
        """
        return self._malware_host_num

    @malware_host_num.setter
    def malware_host_num(self, malware_host_num):
        r"""Sets the malware_host_num of this ShowAntivirusStatisticResponse.

        **参数解释**: 影响主机数量 **取值范围**: 最小值0，最大值2147483647 

        :param malware_host_num: The malware_host_num of this ShowAntivirusStatisticResponse.
        :type malware_host_num: int
        """
        self._malware_host_num = malware_host_num

    @property
    def total_task_num(self):
        r"""Gets the total_task_num of this ShowAntivirusStatisticResponse.

        累计扫描任务数

        :return: The total_task_num of this ShowAntivirusStatisticResponse.
        :rtype: int
        """
        return self._total_task_num

    @total_task_num.setter
    def total_task_num(self, total_task_num):
        r"""Sets the total_task_num of this ShowAntivirusStatisticResponse.

        累计扫描任务数

        :param total_task_num: The total_task_num of this ShowAntivirusStatisticResponse.
        :type total_task_num: int
        """
        self._total_task_num = total_task_num

    @property
    def scanning_task_num(self):
        r"""Gets the scanning_task_num of this ShowAntivirusStatisticResponse.

        运行中任务数

        :return: The scanning_task_num of this ShowAntivirusStatisticResponse.
        :rtype: int
        """
        return self._scanning_task_num

    @scanning_task_num.setter
    def scanning_task_num(self, scanning_task_num):
        r"""Sets the scanning_task_num of this ShowAntivirusStatisticResponse.

        运行中任务数

        :param scanning_task_num: The scanning_task_num of this ShowAntivirusStatisticResponse.
        :type scanning_task_num: int
        """
        self._scanning_task_num = scanning_task_num

    @property
    def latest_scan_time(self):
        r"""Gets the latest_scan_time of this ShowAntivirusStatisticResponse.

        启动时间，毫秒

        :return: The latest_scan_time of this ShowAntivirusStatisticResponse.
        :rtype: int
        """
        return self._latest_scan_time

    @latest_scan_time.setter
    def latest_scan_time(self, latest_scan_time):
        r"""Sets the latest_scan_time of this ShowAntivirusStatisticResponse.

        启动时间，毫秒

        :param latest_scan_time: The latest_scan_time of this ShowAntivirusStatisticResponse.
        :type latest_scan_time: int
        """
        self._latest_scan_time = latest_scan_time

    @property
    def scan_type(self):
        r"""Gets the scan_type of this ShowAntivirusStatisticResponse.

        任务类型，包含如下:   - quick ：快速扫描   - full : 全盘扫描   - custom : 自定义扫描

        :return: The scan_type of this ShowAntivirusStatisticResponse.
        :rtype: str
        """
        return self._scan_type

    @scan_type.setter
    def scan_type(self, scan_type):
        r"""Sets the scan_type of this ShowAntivirusStatisticResponse.

        任务类型，包含如下:   - quick ：快速扫描   - full : 全盘扫描   - custom : 自定义扫描

        :param scan_type: The scan_type of this ShowAntivirusStatisticResponse.
        :type scan_type: str
        """
        self._scan_type = scan_type

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
        if not isinstance(other, ShowAntivirusStatisticResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
