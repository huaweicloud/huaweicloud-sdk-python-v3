# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTracedEventsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_time': 'int',
        'end_time': 'int',
        'event_id': 'str',
        'source_name': 'str',
        'event_type': 'str',
        'subscription_name': 'str',
        'limit': 'str',
        'offset': 'int',
        'channel_id': 'str'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'event_id': 'event_id',
        'source_name': 'source_name',
        'event_type': 'event_type',
        'subscription_name': 'subscription_name',
        'limit': 'limit',
        'offset': 'offset',
        'channel_id': 'channel_id'
    }

    def __init__(self, start_time=None, end_time=None, event_id=None, source_name=None, event_type=None, subscription_name=None, limit=None, offset=None, channel_id=None):
        """ListTracedEventsRequest

        The model defined in huaweicloud sdk

        :param start_time: 查询数据起始时间
        :type start_time: int
        :param end_time: 查询数据结束时间
        :type end_time: int
        :param event_id: 指定查询事件的Id
        :type event_id: str
        :param source_name: 事件源名称
        :type source_name: str
        :param event_type: 指定查询的事件类型，精准匹配
        :type event_type: str
        :param subscription_name: 事件订阅名称
        :type subscription_name: str
        :param limit: 每页显示的条目数量，不能小于0
        :type limit: str
        :param offset: 偏移量，表示从此偏移量开始查询，偏移量不能小于0
        :type offset: int
        :param channel_id: 通道ID
        :type channel_id: str
        """
        
        

        self._start_time = None
        self._end_time = None
        self._event_id = None
        self._source_name = None
        self._event_type = None
        self._subscription_name = None
        self._limit = None
        self._offset = None
        self._channel_id = None
        self.discriminator = None

        self.start_time = start_time
        self.end_time = end_time
        if event_id is not None:
            self.event_id = event_id
        if source_name is not None:
            self.source_name = source_name
        if event_type is not None:
            self.event_type = event_type
        if subscription_name is not None:
            self.subscription_name = subscription_name
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        self.channel_id = channel_id

    @property
    def start_time(self):
        """Gets the start_time of this ListTracedEventsRequest.

        查询数据起始时间

        :return: The start_time of this ListTracedEventsRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListTracedEventsRequest.

        查询数据起始时间

        :param start_time: The start_time of this ListTracedEventsRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListTracedEventsRequest.

        查询数据结束时间

        :return: The end_time of this ListTracedEventsRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListTracedEventsRequest.

        查询数据结束时间

        :param end_time: The end_time of this ListTracedEventsRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def event_id(self):
        """Gets the event_id of this ListTracedEventsRequest.

        指定查询事件的Id

        :return: The event_id of this ListTracedEventsRequest.
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this ListTracedEventsRequest.

        指定查询事件的Id

        :param event_id: The event_id of this ListTracedEventsRequest.
        :type event_id: str
        """
        self._event_id = event_id

    @property
    def source_name(self):
        """Gets the source_name of this ListTracedEventsRequest.

        事件源名称

        :return: The source_name of this ListTracedEventsRequest.
        :rtype: str
        """
        return self._source_name

    @source_name.setter
    def source_name(self, source_name):
        """Sets the source_name of this ListTracedEventsRequest.

        事件源名称

        :param source_name: The source_name of this ListTracedEventsRequest.
        :type source_name: str
        """
        self._source_name = source_name

    @property
    def event_type(self):
        """Gets the event_type of this ListTracedEventsRequest.

        指定查询的事件类型，精准匹配

        :return: The event_type of this ListTracedEventsRequest.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this ListTracedEventsRequest.

        指定查询的事件类型，精准匹配

        :param event_type: The event_type of this ListTracedEventsRequest.
        :type event_type: str
        """
        self._event_type = event_type

    @property
    def subscription_name(self):
        """Gets the subscription_name of this ListTracedEventsRequest.

        事件订阅名称

        :return: The subscription_name of this ListTracedEventsRequest.
        :rtype: str
        """
        return self._subscription_name

    @subscription_name.setter
    def subscription_name(self, subscription_name):
        """Sets the subscription_name of this ListTracedEventsRequest.

        事件订阅名称

        :param subscription_name: The subscription_name of this ListTracedEventsRequest.
        :type subscription_name: str
        """
        self._subscription_name = subscription_name

    @property
    def limit(self):
        """Gets the limit of this ListTracedEventsRequest.

        每页显示的条目数量，不能小于0

        :return: The limit of this ListTracedEventsRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListTracedEventsRequest.

        每页显示的条目数量，不能小于0

        :param limit: The limit of this ListTracedEventsRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListTracedEventsRequest.

        偏移量，表示从此偏移量开始查询，偏移量不能小于0

        :return: The offset of this ListTracedEventsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListTracedEventsRequest.

        偏移量，表示从此偏移量开始查询，偏移量不能小于0

        :param offset: The offset of this ListTracedEventsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def channel_id(self):
        """Gets the channel_id of this ListTracedEventsRequest.

        通道ID

        :return: The channel_id of this ListTracedEventsRequest.
        :rtype: str
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        """Sets the channel_id of this ListTracedEventsRequest.

        通道ID

        :param channel_id: The channel_id of this ListTracedEventsRequest.
        :type channel_id: str
        """
        self._channel_id = channel_id

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
        if not isinstance(other, ListTracedEventsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
