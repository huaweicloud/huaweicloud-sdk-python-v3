# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkloadInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'allocated': 'WorkloadStatistics',
        'queue': 'WorkloadStatistics',
        'timestamp': 'str',
        'window': 'str'
    }

    attribute_map = {
        'allocated': 'allocated',
        'queue': 'queue',
        'timestamp': 'timestamp',
        'window': 'window'
    }

    def __init__(self, allocated=None, queue=None, timestamp=None, window=None):
        r"""WorkloadInfo

        The model defined in huaweicloud sdk

        :param allocated: 
        :type allocated: :class:`huaweicloudsdkmodelarts.v1.WorkloadStatistics`
        :param queue: 
        :type queue: :class:`huaweicloudsdkmodelarts.v1.WorkloadStatistics`
        :param timestamp: UTC时间，格式yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;。
        :type timestamp: str
        :param window: 统计间隔，1s表示1秒，1m表示一分钟，1h为一小时。
        :type window: str
        """
        
        

        self._allocated = None
        self._queue = None
        self._timestamp = None
        self._window = None
        self.discriminator = None

        if allocated is not None:
            self.allocated = allocated
        if queue is not None:
            self.queue = queue
        if timestamp is not None:
            self.timestamp = timestamp
        if window is not None:
            self.window = window

    @property
    def allocated(self):
        r"""Gets the allocated of this WorkloadInfo.

        :return: The allocated of this WorkloadInfo.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.WorkloadStatistics`
        """
        return self._allocated

    @allocated.setter
    def allocated(self, allocated):
        r"""Sets the allocated of this WorkloadInfo.

        :param allocated: The allocated of this WorkloadInfo.
        :type allocated: :class:`huaweicloudsdkmodelarts.v1.WorkloadStatistics`
        """
        self._allocated = allocated

    @property
    def queue(self):
        r"""Gets the queue of this WorkloadInfo.

        :return: The queue of this WorkloadInfo.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.WorkloadStatistics`
        """
        return self._queue

    @queue.setter
    def queue(self, queue):
        r"""Sets the queue of this WorkloadInfo.

        :param queue: The queue of this WorkloadInfo.
        :type queue: :class:`huaweicloudsdkmodelarts.v1.WorkloadStatistics`
        """
        self._queue = queue

    @property
    def timestamp(self):
        r"""Gets the timestamp of this WorkloadInfo.

        UTC时间，格式yyyy-MM-dd'T'HH:mm:ss'Z'。

        :return: The timestamp of this WorkloadInfo.
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        r"""Sets the timestamp of this WorkloadInfo.

        UTC时间，格式yyyy-MM-dd'T'HH:mm:ss'Z'。

        :param timestamp: The timestamp of this WorkloadInfo.
        :type timestamp: str
        """
        self._timestamp = timestamp

    @property
    def window(self):
        r"""Gets the window of this WorkloadInfo.

        统计间隔，1s表示1秒，1m表示一分钟，1h为一小时。

        :return: The window of this WorkloadInfo.
        :rtype: str
        """
        return self._window

    @window.setter
    def window(self, window):
        r"""Sets the window of this WorkloadInfo.

        统计间隔，1s表示1秒，1m表示一分钟，1h为一小时。

        :param window: The window of this WorkloadInfo.
        :type window: str
        """
        self._window = window

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
        if not isinstance(other, WorkloadInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
