# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListUserEventsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_time': 'str',
        'end_time': 'str',
        'username': 'str',
        'event_type': 'str',
        'event_trace_id': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'username': 'username',
        'event_type': 'event_type',
        'event_trace_id': 'event_trace_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, start_time=None, end_time=None, username=None, event_type=None, event_trace_id=None, offset=None, limit=None):
        """ListUserEventsRequest

        The model defined in huaweicloud sdk

        :param start_time: 查询起始时间(0时区)
        :type start_time: str
        :param end_time: 查询结束时间(0时区)
        :type end_time: str
        :param username: 用户名（精确搜索）
        :type username: str
        :param event_type: 事件类型
        :type event_type: str
        :param event_trace_id: 事件之间的关联id
        :type event_trace_id: str
        :param offset: 用于分页查询，查询的起始记录序号，从0开始
        :type offset: int
        :param limit: 用于分页查询，返回用户事件数量限制，取值范围0-1000。如果不指定，默认为100。
        :type limit: int
        """
        
        

        self._start_time = None
        self._end_time = None
        self._username = None
        self._event_type = None
        self._event_trace_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if username is not None:
            self.username = username
        if event_type is not None:
            self.event_type = event_type
        if event_trace_id is not None:
            self.event_trace_id = event_trace_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def start_time(self):
        """Gets the start_time of this ListUserEventsRequest.

        查询起始时间(0时区)

        :return: The start_time of this ListUserEventsRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListUserEventsRequest.

        查询起始时间(0时区)

        :param start_time: The start_time of this ListUserEventsRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListUserEventsRequest.

        查询结束时间(0时区)

        :return: The end_time of this ListUserEventsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListUserEventsRequest.

        查询结束时间(0时区)

        :param end_time: The end_time of this ListUserEventsRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def username(self):
        """Gets the username of this ListUserEventsRequest.

        用户名（精确搜索）

        :return: The username of this ListUserEventsRequest.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this ListUserEventsRequest.

        用户名（精确搜索）

        :param username: The username of this ListUserEventsRequest.
        :type username: str
        """
        self._username = username

    @property
    def event_type(self):
        """Gets the event_type of this ListUserEventsRequest.

        事件类型

        :return: The event_type of this ListUserEventsRequest.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this ListUserEventsRequest.

        事件类型

        :param event_type: The event_type of this ListUserEventsRequest.
        :type event_type: str
        """
        self._event_type = event_type

    @property
    def event_trace_id(self):
        """Gets the event_trace_id of this ListUserEventsRequest.

        事件之间的关联id

        :return: The event_trace_id of this ListUserEventsRequest.
        :rtype: str
        """
        return self._event_trace_id

    @event_trace_id.setter
    def event_trace_id(self, event_trace_id):
        """Sets the event_trace_id of this ListUserEventsRequest.

        事件之间的关联id

        :param event_trace_id: The event_trace_id of this ListUserEventsRequest.
        :type event_trace_id: str
        """
        self._event_trace_id = event_trace_id

    @property
    def offset(self):
        """Gets the offset of this ListUserEventsRequest.

        用于分页查询，查询的起始记录序号，从0开始

        :return: The offset of this ListUserEventsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListUserEventsRequest.

        用于分页查询，查询的起始记录序号，从0开始

        :param offset: The offset of this ListUserEventsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListUserEventsRequest.

        用于分页查询，返回用户事件数量限制，取值范围0-1000。如果不指定，默认为100。

        :return: The limit of this ListUserEventsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListUserEventsRequest.

        用于分页查询，返回用户事件数量限制，取值范围0-1000。如果不指定，默认为100。

        :param limit: The limit of this ListUserEventsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListUserEventsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
