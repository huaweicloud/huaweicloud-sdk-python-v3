# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowVulScanTaskStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scan_task_count': 'int',
        'running_scan_task_count': 'int',
        'last_scan_task': 'VulScanTaskStatisticsResponseInfoLastScanTask'
    }

    attribute_map = {
        'scan_task_count': 'scan_task_count',
        'running_scan_task_count': 'running_scan_task_count',
        'last_scan_task': 'last_scan_task'
    }

    def __init__(self, scan_task_count=None, running_scan_task_count=None, last_scan_task=None):
        r"""ShowVulScanTaskStatisticsResponse

        The model defined in huaweicloud sdk

        :param scan_task_count: **参数解释**: 漏洞扫描任务总次数 **取值范围**: 最小值0，最大值2147483647 
        :type scan_task_count: int
        :param running_scan_task_count: **参数解释**: 进行中的漏洞扫描任务次数 **取值范围**: 最小值0，最大值2147483647 
        :type running_scan_task_count: int
        :param last_scan_task: 
        :type last_scan_task: :class:`huaweicloudsdkhss.v5.VulScanTaskStatisticsResponseInfoLastScanTask`
        """
        
        super().__init__()

        self._scan_task_count = None
        self._running_scan_task_count = None
        self._last_scan_task = None
        self.discriminator = None

        if scan_task_count is not None:
            self.scan_task_count = scan_task_count
        if running_scan_task_count is not None:
            self.running_scan_task_count = running_scan_task_count
        if last_scan_task is not None:
            self.last_scan_task = last_scan_task

    @property
    def scan_task_count(self):
        r"""Gets the scan_task_count of this ShowVulScanTaskStatisticsResponse.

        **参数解释**: 漏洞扫描任务总次数 **取值范围**: 最小值0，最大值2147483647 

        :return: The scan_task_count of this ShowVulScanTaskStatisticsResponse.
        :rtype: int
        """
        return self._scan_task_count

    @scan_task_count.setter
    def scan_task_count(self, scan_task_count):
        r"""Sets the scan_task_count of this ShowVulScanTaskStatisticsResponse.

        **参数解释**: 漏洞扫描任务总次数 **取值范围**: 最小值0，最大值2147483647 

        :param scan_task_count: The scan_task_count of this ShowVulScanTaskStatisticsResponse.
        :type scan_task_count: int
        """
        self._scan_task_count = scan_task_count

    @property
    def running_scan_task_count(self):
        r"""Gets the running_scan_task_count of this ShowVulScanTaskStatisticsResponse.

        **参数解释**: 进行中的漏洞扫描任务次数 **取值范围**: 最小值0，最大值2147483647 

        :return: The running_scan_task_count of this ShowVulScanTaskStatisticsResponse.
        :rtype: int
        """
        return self._running_scan_task_count

    @running_scan_task_count.setter
    def running_scan_task_count(self, running_scan_task_count):
        r"""Sets the running_scan_task_count of this ShowVulScanTaskStatisticsResponse.

        **参数解释**: 进行中的漏洞扫描任务次数 **取值范围**: 最小值0，最大值2147483647 

        :param running_scan_task_count: The running_scan_task_count of this ShowVulScanTaskStatisticsResponse.
        :type running_scan_task_count: int
        """
        self._running_scan_task_count = running_scan_task_count

    @property
    def last_scan_task(self):
        r"""Gets the last_scan_task of this ShowVulScanTaskStatisticsResponse.

        :return: The last_scan_task of this ShowVulScanTaskStatisticsResponse.
        :rtype: :class:`huaweicloudsdkhss.v5.VulScanTaskStatisticsResponseInfoLastScanTask`
        """
        return self._last_scan_task

    @last_scan_task.setter
    def last_scan_task(self, last_scan_task):
        r"""Sets the last_scan_task of this ShowVulScanTaskStatisticsResponse.

        :param last_scan_task: The last_scan_task of this ShowVulScanTaskStatisticsResponse.
        :type last_scan_task: :class:`huaweicloudsdkhss.v5.VulScanTaskStatisticsResponseInfoLastScanTask`
        """
        self._last_scan_task = last_scan_task

    def to_dict(self):
        import warnings
        warnings.warn("ShowVulScanTaskStatisticsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowVulScanTaskStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
