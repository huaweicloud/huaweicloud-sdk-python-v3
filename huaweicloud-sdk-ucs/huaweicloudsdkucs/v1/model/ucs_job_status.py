# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UCSJobStatus:

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
        'reason': 'str',
        'start_time': 'datetime',
        'finish_time': 'datetime'
    }

    attribute_map = {
        'status': 'status',
        'reason': 'reason',
        'start_time': 'startTime',
        'finish_time': 'finishTime'
    }

    def __init__(self, status=None, reason=None, start_time=None, finish_time=None):
        r"""UCSJobStatus

        The model defined in huaweicloud sdk

        :param status: Job状态： - Running：运行中 - TimedOut：运行超时 - Succeeded：运行成功 - Failed：运行失败
        :type status: str
        :param reason: 原因
        :type reason: str
        :param start_time: 开始时间
        :type start_time: datetime
        :param finish_time: 结束时间
        :type finish_time: datetime
        """
        
        

        self._status = None
        self._reason = None
        self._start_time = None
        self._finish_time = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if reason is not None:
            self.reason = reason
        if start_time is not None:
            self.start_time = start_time
        if finish_time is not None:
            self.finish_time = finish_time

    @property
    def status(self):
        r"""Gets the status of this UCSJobStatus.

        Job状态： - Running：运行中 - TimedOut：运行超时 - Succeeded：运行成功 - Failed：运行失败

        :return: The status of this UCSJobStatus.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UCSJobStatus.

        Job状态： - Running：运行中 - TimedOut：运行超时 - Succeeded：运行成功 - Failed：运行失败

        :param status: The status of this UCSJobStatus.
        :type status: str
        """
        self._status = status

    @property
    def reason(self):
        r"""Gets the reason of this UCSJobStatus.

        原因

        :return: The reason of this UCSJobStatus.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this UCSJobStatus.

        原因

        :param reason: The reason of this UCSJobStatus.
        :type reason: str
        """
        self._reason = reason

    @property
    def start_time(self):
        r"""Gets the start_time of this UCSJobStatus.

        开始时间

        :return: The start_time of this UCSJobStatus.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this UCSJobStatus.

        开始时间

        :param start_time: The start_time of this UCSJobStatus.
        :type start_time: datetime
        """
        self._start_time = start_time

    @property
    def finish_time(self):
        r"""Gets the finish_time of this UCSJobStatus.

        结束时间

        :return: The finish_time of this UCSJobStatus.
        :rtype: datetime
        """
        return self._finish_time

    @finish_time.setter
    def finish_time(self, finish_time):
        r"""Sets the finish_time of this UCSJobStatus.

        结束时间

        :param finish_time: The finish_time of this UCSJobStatus.
        :type finish_time: datetime
        """
        self._finish_time = finish_time

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
        if not isinstance(other, UCSJobStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
