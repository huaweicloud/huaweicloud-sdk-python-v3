# coding: utf-8

import pprint
import re

import six





class EventInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'event_name': 'str',
        'event_type': 'str',
        'event_count': 'str',
        'latest_occur_time': 'str',
        'latest_event_source': 'str'
    }

    attribute_map = {
        'event_name': 'event_name',
        'event_type': 'event_type',
        'event_count': 'event_count',
        'latest_occur_time': 'latest_occur_time',
        'latest_event_source': 'latest_event_source'
    }

    def __init__(self, event_name=None, event_type=None, event_count=None, latest_occur_time=None, latest_event_source=None):
        """EventInfo - a model defined in huaweicloud sdk"""
        
        

        self._event_name = None
        self._event_type = None
        self._event_count = None
        self._latest_occur_time = None
        self._latest_event_source = None
        self.discriminator = None

        if event_name is not None:
            self.event_name = event_name
        if event_type is not None:
            self.event_type = event_type
        if event_count is not None:
            self.event_count = event_count
        if latest_occur_time is not None:
            self.latest_occur_time = latest_occur_time
        if latest_event_source is not None:
            self.latest_event_source = latest_event_source

    @property
    def event_name(self):
        """Gets the event_name of this EventInfo.

        事件名称。

        :return: The event_name of this EventInfo.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """Sets the event_name of this EventInfo.

        事件名称。

        :param event_name: The event_name of this EventInfo.
        :type: str
        """
        self._event_name = event_name

    @property
    def event_type(self):
        """Gets the event_type of this EventInfo.

        事件类型。

        :return: The event_type of this EventInfo.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this EventInfo.

        事件类型。

        :param event_type: The event_type of this EventInfo.
        :type: str
        """
        self._event_type = event_type

    @property
    def event_count(self):
        """Gets the event_count of this EventInfo.

        选择查询的时间范围内，此事件发生的数量。

        :return: The event_count of this EventInfo.
        :rtype: str
        """
        return self._event_count

    @event_count.setter
    def event_count(self, event_count):
        """Sets the event_count of this EventInfo.

        选择查询的时间范围内，此事件发生的数量。

        :param event_count: The event_count of this EventInfo.
        :type: str
        """
        self._event_count = event_count

    @property
    def latest_occur_time(self):
        """Gets the latest_occur_time of this EventInfo.

        此事件最近一次发生的时间。

        :return: The latest_occur_time of this EventInfo.
        :rtype: str
        """
        return self._latest_occur_time

    @latest_occur_time.setter
    def latest_occur_time(self, latest_occur_time):
        """Sets the latest_occur_time of this EventInfo.

        此事件最近一次发生的时间。

        :param latest_occur_time: The latest_occur_time of this EventInfo.
        :type: str
        """
        self._latest_occur_time = latest_occur_time

    @property
    def latest_event_source(self):
        """Gets the latest_event_source of this EventInfo.

        事件来源，如果是系统事件则值为各服务的命名空间，各服务的命名空间可查看：“[服务命名空间](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”；如果是自定义事件，则为用户自定义上报定义。

        :return: The latest_event_source of this EventInfo.
        :rtype: str
        """
        return self._latest_event_source

    @latest_event_source.setter
    def latest_event_source(self, latest_event_source):
        """Sets the latest_event_source of this EventInfo.

        事件来源，如果是系统事件则值为各服务的命名空间，各服务的命名空间可查看：“[服务命名空间](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”；如果是自定义事件，则为用户自定义上报定义。

        :param latest_event_source: The latest_event_source of this EventInfo.
        :type: str
        """
        self._latest_event_source = latest_event_source

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EventInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
