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
        'resource_id': 'str',
        'resource_name': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'username': 'username',
        'event_type': 'event_type',
        'resource_id': 'resource_id',
        'resource_name': 'resource_name',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, start_time=None, end_time=None, username=None, event_type=None, resource_id=None, resource_name=None, offset=None, limit=None):
        r"""ListUserEventsRequest

        The model defined in huaweicloud sdk

        :param start_time: 查询起始时间，格式为：UTC时间，例如\&quot;1970-01-01T00:00:00Z\&quot;。
        :type start_time: str
        :param end_time: 查询结束时间，格式为：UTC时间，例如\&quot;1970-01-01T00:00:00Z\&quot;。
        :type end_time: str
        :param username: 用户名（精确搜索）。
        :type username: str
        :param event_type: 事件类型，英文逗号隔开。
        :type event_type: str
        :param resource_id: 操作资源ID。
        :type resource_id: str
        :param resource_name: 操作资源名称。
        :type resource_name: str
        :param offset: 用于分页查询，查询的起始记录序号，从0开始。
        :type offset: int
        :param limit: 用于分页查询，返回用户事件数量限制，取值范围0-1000。如果不指定，默认为100。
        :type limit: int
        """
        
        

        self._start_time = None
        self._end_time = None
        self._username = None
        self._event_type = None
        self._resource_id = None
        self._resource_name = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.start_time = start_time
        self.end_time = end_time
        if username is not None:
            self.username = username
        if event_type is not None:
            self.event_type = event_type
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_name is not None:
            self.resource_name = resource_name
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def start_time(self):
        r"""Gets the start_time of this ListUserEventsRequest.

        查询起始时间，格式为：UTC时间，例如\"1970-01-01T00:00:00Z\"。

        :return: The start_time of this ListUserEventsRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListUserEventsRequest.

        查询起始时间，格式为：UTC时间，例如\"1970-01-01T00:00:00Z\"。

        :param start_time: The start_time of this ListUserEventsRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListUserEventsRequest.

        查询结束时间，格式为：UTC时间，例如\"1970-01-01T00:00:00Z\"。

        :return: The end_time of this ListUserEventsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListUserEventsRequest.

        查询结束时间，格式为：UTC时间，例如\"1970-01-01T00:00:00Z\"。

        :param end_time: The end_time of this ListUserEventsRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def username(self):
        r"""Gets the username of this ListUserEventsRequest.

        用户名（精确搜索）。

        :return: The username of this ListUserEventsRequest.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        r"""Sets the username of this ListUserEventsRequest.

        用户名（精确搜索）。

        :param username: The username of this ListUserEventsRequest.
        :type username: str
        """
        self._username = username

    @property
    def event_type(self):
        r"""Gets the event_type of this ListUserEventsRequest.

        事件类型，英文逗号隔开。

        :return: The event_type of this ListUserEventsRequest.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        r"""Sets the event_type of this ListUserEventsRequest.

        事件类型，英文逗号隔开。

        :param event_type: The event_type of this ListUserEventsRequest.
        :type event_type: str
        """
        self._event_type = event_type

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ListUserEventsRequest.

        操作资源ID。

        :return: The resource_id of this ListUserEventsRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ListUserEventsRequest.

        操作资源ID。

        :param resource_id: The resource_id of this ListUserEventsRequest.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        r"""Gets the resource_name of this ListUserEventsRequest.

        操作资源名称。

        :return: The resource_name of this ListUserEventsRequest.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this ListUserEventsRequest.

        操作资源名称。

        :param resource_name: The resource_name of this ListUserEventsRequest.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def offset(self):
        r"""Gets the offset of this ListUserEventsRequest.

        用于分页查询，查询的起始记录序号，从0开始。

        :return: The offset of this ListUserEventsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListUserEventsRequest.

        用于分页查询，查询的起始记录序号，从0开始。

        :param offset: The offset of this ListUserEventsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListUserEventsRequest.

        用于分页查询，返回用户事件数量限制，取值范围0-1000。如果不指定，默认为100。

        :return: The limit of this ListUserEventsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListUserEventsRequest.

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
