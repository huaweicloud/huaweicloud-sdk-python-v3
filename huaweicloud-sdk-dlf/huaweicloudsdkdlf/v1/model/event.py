# coding: utf-8

import six

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
        'event_type': 'str',
        'channel': 'str',
        'fail_policy': 'str',
        'concurrent': 'int',
        'read_policy': 'str'
    }

    attribute_map = {
        'event_type': 'eventType',
        'channel': 'channel',
        'fail_policy': 'failPolicy',
        'concurrent': 'concurrent',
        'read_policy': 'readPolicy'
    }

    def __init__(self, event_type=None, channel=None, fail_policy=None, concurrent=None, read_policy=None):
        r"""Event

        The model defined in huaweicloud sdk

        :param event_type: 事件类型
        :type event_type: str
        :param channel: DIS通道名称
        :type channel: str
        :param fail_policy: 执行失败处理策略
        :type fail_policy: str
        :param concurrent: 调度并发数
        :type concurrent: int
        :param read_policy: 读取策略
        :type read_policy: str
        """
        
        

        self._event_type = None
        self._channel = None
        self._fail_policy = None
        self._concurrent = None
        self._read_policy = None
        self.discriminator = None

        if event_type is not None:
            self.event_type = event_type
        if channel is not None:
            self.channel = channel
        if fail_policy is not None:
            self.fail_policy = fail_policy
        if concurrent is not None:
            self.concurrent = concurrent
        if read_policy is not None:
            self.read_policy = read_policy

    @property
    def event_type(self):
        r"""Gets the event_type of this Event.

        事件类型

        :return: The event_type of this Event.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        r"""Sets the event_type of this Event.

        事件类型

        :param event_type: The event_type of this Event.
        :type event_type: str
        """
        self._event_type = event_type

    @property
    def channel(self):
        r"""Gets the channel of this Event.

        DIS通道名称

        :return: The channel of this Event.
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        r"""Sets the channel of this Event.

        DIS通道名称

        :param channel: The channel of this Event.
        :type channel: str
        """
        self._channel = channel

    @property
    def fail_policy(self):
        r"""Gets the fail_policy of this Event.

        执行失败处理策略

        :return: The fail_policy of this Event.
        :rtype: str
        """
        return self._fail_policy

    @fail_policy.setter
    def fail_policy(self, fail_policy):
        r"""Sets the fail_policy of this Event.

        执行失败处理策略

        :param fail_policy: The fail_policy of this Event.
        :type fail_policy: str
        """
        self._fail_policy = fail_policy

    @property
    def concurrent(self):
        r"""Gets the concurrent of this Event.

        调度并发数

        :return: The concurrent of this Event.
        :rtype: int
        """
        return self._concurrent

    @concurrent.setter
    def concurrent(self, concurrent):
        r"""Sets the concurrent of this Event.

        调度并发数

        :param concurrent: The concurrent of this Event.
        :type concurrent: int
        """
        self._concurrent = concurrent

    @property
    def read_policy(self):
        r"""Gets the read_policy of this Event.

        读取策略

        :return: The read_policy of this Event.
        :rtype: str
        """
        return self._read_policy

    @read_policy.setter
    def read_policy(self, read_policy):
        r"""Sets the read_policy of this Event.

        读取策略

        :param read_policy: The read_policy of this Event.
        :type read_policy: str
        """
        self._read_policy = read_policy

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
        if not isinstance(other, Event):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
