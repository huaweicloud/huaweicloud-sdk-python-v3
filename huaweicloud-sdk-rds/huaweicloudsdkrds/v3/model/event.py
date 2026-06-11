# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Event:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sample_time': 'str',
        'count': 'int',
        'session_status': 'str',
        'wait_event_type': 'str',
        'wait_event_name': 'str'
    }

    attribute_map = {
        'sample_time': 'sample_time',
        'count': 'count',
        'session_status': 'session_status',
        'wait_event_type': 'wait_event_type',
        'wait_event_name': 'wait_event_name'
    }

    def __init__(self, sample_time=None, count=None, session_status=None, wait_event_type=None, wait_event_name=None):
        r"""Event

        The model defined in huaweicloud sdk

        :param sample_time: 采样时间
        :type sample_time: str
        :param count: 个数
        :type count: int
        :param session_status: 会话状态
        :type session_status: str
        :param wait_event_type: 等待事件类型
        :type wait_event_type: str
        :param wait_event_name: 等待事件名称
        :type wait_event_name: str
        """
        
        

        self._sample_time = None
        self._count = None
        self._session_status = None
        self._wait_event_type = None
        self._wait_event_name = None
        self.discriminator = None

        if sample_time is not None:
            self.sample_time = sample_time
        if count is not None:
            self.count = count
        if session_status is not None:
            self.session_status = session_status
        if wait_event_type is not None:
            self.wait_event_type = wait_event_type
        if wait_event_name is not None:
            self.wait_event_name = wait_event_name

    @property
    def sample_time(self):
        r"""Gets the sample_time of this Event.

        采样时间

        :return: The sample_time of this Event.
        :rtype: str
        """
        return self._sample_time

    @sample_time.setter
    def sample_time(self, sample_time):
        r"""Sets the sample_time of this Event.

        采样时间

        :param sample_time: The sample_time of this Event.
        :type sample_time: str
        """
        self._sample_time = sample_time

    @property
    def count(self):
        r"""Gets the count of this Event.

        个数

        :return: The count of this Event.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this Event.

        个数

        :param count: The count of this Event.
        :type count: int
        """
        self._count = count

    @property
    def session_status(self):
        r"""Gets the session_status of this Event.

        会话状态

        :return: The session_status of this Event.
        :rtype: str
        """
        return self._session_status

    @session_status.setter
    def session_status(self, session_status):
        r"""Sets the session_status of this Event.

        会话状态

        :param session_status: The session_status of this Event.
        :type session_status: str
        """
        self._session_status = session_status

    @property
    def wait_event_type(self):
        r"""Gets the wait_event_type of this Event.

        等待事件类型

        :return: The wait_event_type of this Event.
        :rtype: str
        """
        return self._wait_event_type

    @wait_event_type.setter
    def wait_event_type(self, wait_event_type):
        r"""Sets the wait_event_type of this Event.

        等待事件类型

        :param wait_event_type: The wait_event_type of this Event.
        :type wait_event_type: str
        """
        self._wait_event_type = wait_event_type

    @property
    def wait_event_name(self):
        r"""Gets the wait_event_name of this Event.

        等待事件名称

        :return: The wait_event_name of this Event.
        :rtype: str
        """
        return self._wait_event_name

    @wait_event_name.setter
    def wait_event_name(self, wait_event_name):
        r"""Sets the wait_event_name of this Event.

        等待事件名称

        :param wait_event_name: The wait_event_name of this Event.
        :type wait_event_name: str
        """
        self._wait_event_name = wait_event_name

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
        if not isinstance(other, Event):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
