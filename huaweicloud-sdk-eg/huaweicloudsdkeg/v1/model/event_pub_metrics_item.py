# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventPubMetricsItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'event_size': 'int',
        'timestamp': 'int',
        'num': 'int',
        'success_num': 'int',
        'process_time': 'int',
        'invoke_time': 'int'
    }

    attribute_map = {
        'event_size': 'event_size',
        'timestamp': 'timestamp',
        'num': 'num',
        'success_num': 'success_num',
        'process_time': 'process_time',
        'invoke_time': 'invoke_time'
    }

    def __init__(self, event_size=None, timestamp=None, num=None, success_num=None, process_time=None, invoke_time=None):
        """EventPubMetricsItem

        The model defined in huaweicloud sdk

        :param event_size: 事件大小
        :type event_size: int
        :param timestamp: 时间戳
        :type timestamp: int
        :param num: 调用数
        :type num: int
        :param success_num: 调用成功数
        :type success_num: int
        :param process_time: 处理时间
        :type process_time: int
        :param invoke_time: 调用时间
        :type invoke_time: int
        """
        
        

        self._event_size = None
        self._timestamp = None
        self._num = None
        self._success_num = None
        self._process_time = None
        self._invoke_time = None
        self.discriminator = None

        if event_size is not None:
            self.event_size = event_size
        if timestamp is not None:
            self.timestamp = timestamp
        if num is not None:
            self.num = num
        if success_num is not None:
            self.success_num = success_num
        if process_time is not None:
            self.process_time = process_time
        if invoke_time is not None:
            self.invoke_time = invoke_time

    @property
    def event_size(self):
        """Gets the event_size of this EventPubMetricsItem.

        事件大小

        :return: The event_size of this EventPubMetricsItem.
        :rtype: int
        """
        return self._event_size

    @event_size.setter
    def event_size(self, event_size):
        """Sets the event_size of this EventPubMetricsItem.

        事件大小

        :param event_size: The event_size of this EventPubMetricsItem.
        :type event_size: int
        """
        self._event_size = event_size

    @property
    def timestamp(self):
        """Gets the timestamp of this EventPubMetricsItem.

        时间戳

        :return: The timestamp of this EventPubMetricsItem.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this EventPubMetricsItem.

        时间戳

        :param timestamp: The timestamp of this EventPubMetricsItem.
        :type timestamp: int
        """
        self._timestamp = timestamp

    @property
    def num(self):
        """Gets the num of this EventPubMetricsItem.

        调用数

        :return: The num of this EventPubMetricsItem.
        :rtype: int
        """
        return self._num

    @num.setter
    def num(self, num):
        """Sets the num of this EventPubMetricsItem.

        调用数

        :param num: The num of this EventPubMetricsItem.
        :type num: int
        """
        self._num = num

    @property
    def success_num(self):
        """Gets the success_num of this EventPubMetricsItem.

        调用成功数

        :return: The success_num of this EventPubMetricsItem.
        :rtype: int
        """
        return self._success_num

    @success_num.setter
    def success_num(self, success_num):
        """Sets the success_num of this EventPubMetricsItem.

        调用成功数

        :param success_num: The success_num of this EventPubMetricsItem.
        :type success_num: int
        """
        self._success_num = success_num

    @property
    def process_time(self):
        """Gets the process_time of this EventPubMetricsItem.

        处理时间

        :return: The process_time of this EventPubMetricsItem.
        :rtype: int
        """
        return self._process_time

    @process_time.setter
    def process_time(self, process_time):
        """Sets the process_time of this EventPubMetricsItem.

        处理时间

        :param process_time: The process_time of this EventPubMetricsItem.
        :type process_time: int
        """
        self._process_time = process_time

    @property
    def invoke_time(self):
        """Gets the invoke_time of this EventPubMetricsItem.

        调用时间

        :return: The invoke_time of this EventPubMetricsItem.
        :rtype: int
        """
        return self._invoke_time

    @invoke_time.setter
    def invoke_time(self, invoke_time):
        """Sets the invoke_time of this EventPubMetricsItem.

        调用时间

        :param invoke_time: The invoke_time of this EventPubMetricsItem.
        :type invoke_time: int
        """
        self._invoke_time = invoke_time

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
        if not isinstance(other, EventPubMetricsItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
