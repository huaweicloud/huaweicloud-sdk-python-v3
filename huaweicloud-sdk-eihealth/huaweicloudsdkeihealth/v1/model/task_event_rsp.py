# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskEventRsp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'count': 'int',
        'reason': 'str',
        'message': 'str',
        'first_timestamp': 'str',
        'last_timestamp': 'str'
    }

    attribute_map = {
        'type': 'type',
        'count': 'count',
        'reason': 'reason',
        'message': 'message',
        'first_timestamp': 'first_timestamp',
        'last_timestamp': 'last_timestamp'
    }

    def __init__(self, type=None, count=None, reason=None, message=None, first_timestamp=None, last_timestamp=None):
        """TaskEventRsp

        The model defined in huaweicloud sdk

        :param type: 任务启动事件类型
        :type type: str
        :param count: 任务启动事件发生次数
        :type count: int
        :param reason: 任务启动事件状态
        :type reason: str
        :param message: 任务启动事件详细信息
        :type message: str
        :param first_timestamp: 任务启动事件首次上报时间
        :type first_timestamp: str
        :param last_timestamp: 任务启动事件末次上报时间
        :type last_timestamp: str
        """
        
        

        self._type = None
        self._count = None
        self._reason = None
        self._message = None
        self._first_timestamp = None
        self._last_timestamp = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if count is not None:
            self.count = count
        if reason is not None:
            self.reason = reason
        if message is not None:
            self.message = message
        if first_timestamp is not None:
            self.first_timestamp = first_timestamp
        if last_timestamp is not None:
            self.last_timestamp = last_timestamp

    @property
    def type(self):
        """Gets the type of this TaskEventRsp.

        任务启动事件类型

        :return: The type of this TaskEventRsp.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TaskEventRsp.

        任务启动事件类型

        :param type: The type of this TaskEventRsp.
        :type type: str
        """
        self._type = type

    @property
    def count(self):
        """Gets the count of this TaskEventRsp.

        任务启动事件发生次数

        :return: The count of this TaskEventRsp.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this TaskEventRsp.

        任务启动事件发生次数

        :param count: The count of this TaskEventRsp.
        :type count: int
        """
        self._count = count

    @property
    def reason(self):
        """Gets the reason of this TaskEventRsp.

        任务启动事件状态

        :return: The reason of this TaskEventRsp.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this TaskEventRsp.

        任务启动事件状态

        :param reason: The reason of this TaskEventRsp.
        :type reason: str
        """
        self._reason = reason

    @property
    def message(self):
        """Gets the message of this TaskEventRsp.

        任务启动事件详细信息

        :return: The message of this TaskEventRsp.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this TaskEventRsp.

        任务启动事件详细信息

        :param message: The message of this TaskEventRsp.
        :type message: str
        """
        self._message = message

    @property
    def first_timestamp(self):
        """Gets the first_timestamp of this TaskEventRsp.

        任务启动事件首次上报时间

        :return: The first_timestamp of this TaskEventRsp.
        :rtype: str
        """
        return self._first_timestamp

    @first_timestamp.setter
    def first_timestamp(self, first_timestamp):
        """Sets the first_timestamp of this TaskEventRsp.

        任务启动事件首次上报时间

        :param first_timestamp: The first_timestamp of this TaskEventRsp.
        :type first_timestamp: str
        """
        self._first_timestamp = first_timestamp

    @property
    def last_timestamp(self):
        """Gets the last_timestamp of this TaskEventRsp.

        任务启动事件末次上报时间

        :return: The last_timestamp of this TaskEventRsp.
        :rtype: str
        """
        return self._last_timestamp

    @last_timestamp.setter
    def last_timestamp(self, last_timestamp):
        """Sets the last_timestamp of this TaskEventRsp.

        任务启动事件末次上报时间

        :param last_timestamp: The last_timestamp of this TaskEventRsp.
        :type last_timestamp: str
        """
        self._last_timestamp = last_timestamp

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
        if not isinstance(other, TaskEventRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
