# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowVulScanTaskEstimatedTimeResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'queue_time': 'int',
        'run_time': 'int',
        'total_time': 'int'
    }

    attribute_map = {
        'queue_time': 'queue_time',
        'run_time': 'run_time',
        'total_time': 'total_time'
    }

    def __init__(self, queue_time=None, run_time=None, total_time=None):
        r"""ShowVulScanTaskEstimatedTimeResponse

        The model defined in huaweicloud sdk

        :param queue_time: **参数解释**： 执行漏洞扫描需要排队等待的时间，单位为分钟 **约束限制**： 不涉及 **取值范围**： 字符长度1-9223372036854775807 **默认取值**： 不涉及 
        :type queue_time: int
        :param run_time: **参数解释**: 本次任务执行需要的时间，单位为分钟 **约束限制**： 不涉及 **取值范围**： 字符长度1-9223372036854775807 **默认取值**： 不涉及 
        :type run_time: int
        :param total_time: **参数解释**: 从现在到任务结束需要的总时间，单位为分钟 **约束限制**： 不涉及 **取值范围**： 字符长度1-9223372036854775807 **默认取值**： 不涉及 
        :type total_time: int
        """
        
        super().__init__()

        self._queue_time = None
        self._run_time = None
        self._total_time = None
        self.discriminator = None

        if queue_time is not None:
            self.queue_time = queue_time
        if run_time is not None:
            self.run_time = run_time
        if total_time is not None:
            self.total_time = total_time

    @property
    def queue_time(self):
        r"""Gets the queue_time of this ShowVulScanTaskEstimatedTimeResponse.

        **参数解释**： 执行漏洞扫描需要排队等待的时间，单位为分钟 **约束限制**： 不涉及 **取值范围**： 字符长度1-9223372036854775807 **默认取值**： 不涉及 

        :return: The queue_time of this ShowVulScanTaskEstimatedTimeResponse.
        :rtype: int
        """
        return self._queue_time

    @queue_time.setter
    def queue_time(self, queue_time):
        r"""Sets the queue_time of this ShowVulScanTaskEstimatedTimeResponse.

        **参数解释**： 执行漏洞扫描需要排队等待的时间，单位为分钟 **约束限制**： 不涉及 **取值范围**： 字符长度1-9223372036854775807 **默认取值**： 不涉及 

        :param queue_time: The queue_time of this ShowVulScanTaskEstimatedTimeResponse.
        :type queue_time: int
        """
        self._queue_time = queue_time

    @property
    def run_time(self):
        r"""Gets the run_time of this ShowVulScanTaskEstimatedTimeResponse.

        **参数解释**: 本次任务执行需要的时间，单位为分钟 **约束限制**： 不涉及 **取值范围**： 字符长度1-9223372036854775807 **默认取值**： 不涉及 

        :return: The run_time of this ShowVulScanTaskEstimatedTimeResponse.
        :rtype: int
        """
        return self._run_time

    @run_time.setter
    def run_time(self, run_time):
        r"""Sets the run_time of this ShowVulScanTaskEstimatedTimeResponse.

        **参数解释**: 本次任务执行需要的时间，单位为分钟 **约束限制**： 不涉及 **取值范围**： 字符长度1-9223372036854775807 **默认取值**： 不涉及 

        :param run_time: The run_time of this ShowVulScanTaskEstimatedTimeResponse.
        :type run_time: int
        """
        self._run_time = run_time

    @property
    def total_time(self):
        r"""Gets the total_time of this ShowVulScanTaskEstimatedTimeResponse.

        **参数解释**: 从现在到任务结束需要的总时间，单位为分钟 **约束限制**： 不涉及 **取值范围**： 字符长度1-9223372036854775807 **默认取值**： 不涉及 

        :return: The total_time of this ShowVulScanTaskEstimatedTimeResponse.
        :rtype: int
        """
        return self._total_time

    @total_time.setter
    def total_time(self, total_time):
        r"""Sets the total_time of this ShowVulScanTaskEstimatedTimeResponse.

        **参数解释**: 从现在到任务结束需要的总时间，单位为分钟 **约束限制**： 不涉及 **取值范围**： 字符长度1-9223372036854775807 **默认取值**： 不涉及 

        :param total_time: The total_time of this ShowVulScanTaskEstimatedTimeResponse.
        :type total_time: int
        """
        self._total_time = total_time

    def to_dict(self):
        import warnings
        warnings.warn("ShowVulScanTaskEstimatedTimeResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowVulScanTaskEstimatedTimeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
