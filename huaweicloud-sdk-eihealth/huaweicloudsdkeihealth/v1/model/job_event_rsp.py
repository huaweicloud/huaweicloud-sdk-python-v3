# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobEventRsp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action_name': 'str',
        'count': 'int',
        'first_timestamp': 'str',
        'last_timestamp': 'str',
        'message': 'str',
        'reason': 'str',
        'type': 'str'
    }

    attribute_map = {
        'action_name': 'action_name',
        'count': 'count',
        'first_timestamp': 'first_timestamp',
        'last_timestamp': 'last_timestamp',
        'message': 'message',
        'reason': 'reason',
        'type': 'type'
    }

    def __init__(self, action_name=None, count=None, first_timestamp=None, last_timestamp=None, message=None, reason=None, type=None):
        r"""JobEventRsp

        The model defined in huaweicloud sdk

        :param action_name: 执行动作名称
        :type action_name: str
        :param count: 作业启动事件发生次数
        :type count: int
        :param first_timestamp: 作业启动事件首次上报时间
        :type first_timestamp: str
        :param last_timestamp: 作业启动事件末次上报时间
        :type last_timestamp: str
        :param message: 作业启动事件详细信息
        :type message: str
        :param reason: 作业启动事件状态
        :type reason: str
        :param type: 作业启动事件类型
        :type type: str
        """
        
        

        self._action_name = None
        self._count = None
        self._first_timestamp = None
        self._last_timestamp = None
        self._message = None
        self._reason = None
        self._type = None
        self.discriminator = None

        if action_name is not None:
            self.action_name = action_name
        if count is not None:
            self.count = count
        if first_timestamp is not None:
            self.first_timestamp = first_timestamp
        if last_timestamp is not None:
            self.last_timestamp = last_timestamp
        if message is not None:
            self.message = message
        if reason is not None:
            self.reason = reason
        if type is not None:
            self.type = type

    @property
    def action_name(self):
        r"""Gets the action_name of this JobEventRsp.

        执行动作名称

        :return: The action_name of this JobEventRsp.
        :rtype: str
        """
        return self._action_name

    @action_name.setter
    def action_name(self, action_name):
        r"""Sets the action_name of this JobEventRsp.

        执行动作名称

        :param action_name: The action_name of this JobEventRsp.
        :type action_name: str
        """
        self._action_name = action_name

    @property
    def count(self):
        r"""Gets the count of this JobEventRsp.

        作业启动事件发生次数

        :return: The count of this JobEventRsp.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this JobEventRsp.

        作业启动事件发生次数

        :param count: The count of this JobEventRsp.
        :type count: int
        """
        self._count = count

    @property
    def first_timestamp(self):
        r"""Gets the first_timestamp of this JobEventRsp.

        作业启动事件首次上报时间

        :return: The first_timestamp of this JobEventRsp.
        :rtype: str
        """
        return self._first_timestamp

    @first_timestamp.setter
    def first_timestamp(self, first_timestamp):
        r"""Sets the first_timestamp of this JobEventRsp.

        作业启动事件首次上报时间

        :param first_timestamp: The first_timestamp of this JobEventRsp.
        :type first_timestamp: str
        """
        self._first_timestamp = first_timestamp

    @property
    def last_timestamp(self):
        r"""Gets the last_timestamp of this JobEventRsp.

        作业启动事件末次上报时间

        :return: The last_timestamp of this JobEventRsp.
        :rtype: str
        """
        return self._last_timestamp

    @last_timestamp.setter
    def last_timestamp(self, last_timestamp):
        r"""Sets the last_timestamp of this JobEventRsp.

        作业启动事件末次上报时间

        :param last_timestamp: The last_timestamp of this JobEventRsp.
        :type last_timestamp: str
        """
        self._last_timestamp = last_timestamp

    @property
    def message(self):
        r"""Gets the message of this JobEventRsp.

        作业启动事件详细信息

        :return: The message of this JobEventRsp.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this JobEventRsp.

        作业启动事件详细信息

        :param message: The message of this JobEventRsp.
        :type message: str
        """
        self._message = message

    @property
    def reason(self):
        r"""Gets the reason of this JobEventRsp.

        作业启动事件状态

        :return: The reason of this JobEventRsp.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this JobEventRsp.

        作业启动事件状态

        :param reason: The reason of this JobEventRsp.
        :type reason: str
        """
        self._reason = reason

    @property
    def type(self):
        r"""Gets the type of this JobEventRsp.

        作业启动事件类型

        :return: The type of this JobEventRsp.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this JobEventRsp.

        作业启动事件类型

        :param type: The type of this JobEventRsp.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, JobEventRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
