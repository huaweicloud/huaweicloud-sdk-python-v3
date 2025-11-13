# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CollectSubscriptionMonitorResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'latency': 'int',
        'last_dist_sync': 'str',
        'agent_not_running': 'int',
        'pending_cmd_count': 'int',
        'estimated_process_time': 'int'
    }

    attribute_map = {
        'status': 'status',
        'latency': 'latency',
        'last_dist_sync': 'last_dist_sync',
        'agent_not_running': 'agent_not_running',
        'pending_cmd_count': 'pending_cmd_count',
        'estimated_process_time': 'estimated_process_time'
    }

    def __init__(self, status=None, latency=None, last_dist_sync=None, agent_not_running=None, pending_cmd_count=None, estimated_process_time=None):
        r"""CollectSubscriptionMonitorResponse

        The model defined in huaweicloud sdk

        :param status: 订阅关联的快照代理的运行状态。取值如下:  started:已启动。 succeeded:成功。 in_progress:正在运行。 idle:空闲。 retrying:重试中。 failed:失败。
        :type status: str
        :param latency: 数据更改的最长延迟时间（以秒为单位）。
        :type latency: int
        :param last_dist_sync: 上一次分发代理运行时间。格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type last_dist_sync: str
        :param agent_not_running: 代理未运行的时长（以小时为单位）。
        :type agent_not_running: int
        :param pending_cmd_count: 订阅未执行的命令数。
        :type pending_cmd_count: int
        :param estimated_process_time: 预计执行完未执行的命令数所需时间（以秒为单位）。
        :type estimated_process_time: int
        """
        
        super().__init__()

        self._status = None
        self._latency = None
        self._last_dist_sync = None
        self._agent_not_running = None
        self._pending_cmd_count = None
        self._estimated_process_time = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if latency is not None:
            self.latency = latency
        if last_dist_sync is not None:
            self.last_dist_sync = last_dist_sync
        if agent_not_running is not None:
            self.agent_not_running = agent_not_running
        if pending_cmd_count is not None:
            self.pending_cmd_count = pending_cmd_count
        if estimated_process_time is not None:
            self.estimated_process_time = estimated_process_time

    @property
    def status(self):
        r"""Gets the status of this CollectSubscriptionMonitorResponse.

        订阅关联的快照代理的运行状态。取值如下:  started:已启动。 succeeded:成功。 in_progress:正在运行。 idle:空闲。 retrying:重试中。 failed:失败。

        :return: The status of this CollectSubscriptionMonitorResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CollectSubscriptionMonitorResponse.

        订阅关联的快照代理的运行状态。取值如下:  started:已启动。 succeeded:成功。 in_progress:正在运行。 idle:空闲。 retrying:重试中。 failed:失败。

        :param status: The status of this CollectSubscriptionMonitorResponse.
        :type status: str
        """
        self._status = status

    @property
    def latency(self):
        r"""Gets the latency of this CollectSubscriptionMonitorResponse.

        数据更改的最长延迟时间（以秒为单位）。

        :return: The latency of this CollectSubscriptionMonitorResponse.
        :rtype: int
        """
        return self._latency

    @latency.setter
    def latency(self, latency):
        r"""Sets the latency of this CollectSubscriptionMonitorResponse.

        数据更改的最长延迟时间（以秒为单位）。

        :param latency: The latency of this CollectSubscriptionMonitorResponse.
        :type latency: int
        """
        self._latency = latency

    @property
    def last_dist_sync(self):
        r"""Gets the last_dist_sync of this CollectSubscriptionMonitorResponse.

        上一次分发代理运行时间。格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The last_dist_sync of this CollectSubscriptionMonitorResponse.
        :rtype: str
        """
        return self._last_dist_sync

    @last_dist_sync.setter
    def last_dist_sync(self, last_dist_sync):
        r"""Sets the last_dist_sync of this CollectSubscriptionMonitorResponse.

        上一次分发代理运行时间。格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param last_dist_sync: The last_dist_sync of this CollectSubscriptionMonitorResponse.
        :type last_dist_sync: str
        """
        self._last_dist_sync = last_dist_sync

    @property
    def agent_not_running(self):
        r"""Gets the agent_not_running of this CollectSubscriptionMonitorResponse.

        代理未运行的时长（以小时为单位）。

        :return: The agent_not_running of this CollectSubscriptionMonitorResponse.
        :rtype: int
        """
        return self._agent_not_running

    @agent_not_running.setter
    def agent_not_running(self, agent_not_running):
        r"""Sets the agent_not_running of this CollectSubscriptionMonitorResponse.

        代理未运行的时长（以小时为单位）。

        :param agent_not_running: The agent_not_running of this CollectSubscriptionMonitorResponse.
        :type agent_not_running: int
        """
        self._agent_not_running = agent_not_running

    @property
    def pending_cmd_count(self):
        r"""Gets the pending_cmd_count of this CollectSubscriptionMonitorResponse.

        订阅未执行的命令数。

        :return: The pending_cmd_count of this CollectSubscriptionMonitorResponse.
        :rtype: int
        """
        return self._pending_cmd_count

    @pending_cmd_count.setter
    def pending_cmd_count(self, pending_cmd_count):
        r"""Sets the pending_cmd_count of this CollectSubscriptionMonitorResponse.

        订阅未执行的命令数。

        :param pending_cmd_count: The pending_cmd_count of this CollectSubscriptionMonitorResponse.
        :type pending_cmd_count: int
        """
        self._pending_cmd_count = pending_cmd_count

    @property
    def estimated_process_time(self):
        r"""Gets the estimated_process_time of this CollectSubscriptionMonitorResponse.

        预计执行完未执行的命令数所需时间（以秒为单位）。

        :return: The estimated_process_time of this CollectSubscriptionMonitorResponse.
        :rtype: int
        """
        return self._estimated_process_time

    @estimated_process_time.setter
    def estimated_process_time(self, estimated_process_time):
        r"""Sets the estimated_process_time of this CollectSubscriptionMonitorResponse.

        预计执行完未执行的命令数所需时间（以秒为单位）。

        :param estimated_process_time: The estimated_process_time of this CollectSubscriptionMonitorResponse.
        :type estimated_process_time: int
        """
        self._estimated_process_time = estimated_process_time

    def to_dict(self):
        import warnings
        warnings.warn("CollectSubscriptionMonitorResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, CollectSubscriptionMonitorResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
