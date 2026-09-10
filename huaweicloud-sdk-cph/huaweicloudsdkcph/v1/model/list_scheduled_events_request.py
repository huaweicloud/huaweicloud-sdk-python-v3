# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListScheduledEventsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'marker': 'str',
        'event_id': 'str',
        'server_id': 'str',
        'publish_since': 'str',
        'publish_until': 'str',
        'state': 'list[str]',
        'type': 'list[str]'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'event_id': 'event_id',
        'server_id': 'server_id',
        'publish_since': 'publish_since',
        'publish_until': 'publish_until',
        'state': 'state',
        'type': 'type'
    }

    def __init__(self, limit=None, marker=None, event_id=None, server_id=None, publish_since=None, publish_until=None, state=None, type=None):
        r"""ListScheduledEventsRequest

        The model defined in huaweicloud sdk

        :param limit: 每页返回的事件个数。取值范围：1~100（默认值为10）
        :type limit: int
        :param marker: 分页标记。从marker指定的下一条数据开始查询。
        :type marker: str
        :param event_id: 计划事件id。
        :type event_id: str
        :param server_id: 云手机服务器的唯一标识。
        :type server_id: str
        :param publish_since: 事件发布开始时间，按照时间范围过滤。
        :type publish_since: str
        :param publish_until: 事件发布结束时间，按照时间范围过滤。
        :type publish_until: str
        :param state: 计划事件状态。支持多值查询过滤。 取值范围： inquiring: 待授权、 scheduled：待执行、 executing：执行中、 completed：执行成功、 failed：执行失败、 canceled：取消
        :type state: list[str]
        :param type: 计划事件类型。支持多值查询过滤。取值范围： localdisk-recovery：本地盘换盘、 system-maintenance：系统维护
        :type type: list[str]
        """
        
        

        self._limit = None
        self._marker = None
        self._event_id = None
        self._server_id = None
        self._publish_since = None
        self._publish_until = None
        self._state = None
        self._type = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if event_id is not None:
            self.event_id = event_id
        if server_id is not None:
            self.server_id = server_id
        if publish_since is not None:
            self.publish_since = publish_since
        if publish_until is not None:
            self.publish_until = publish_until
        if state is not None:
            self.state = state
        if type is not None:
            self.type = type

    @property
    def limit(self):
        r"""Gets the limit of this ListScheduledEventsRequest.

        每页返回的事件个数。取值范围：1~100（默认值为10）

        :return: The limit of this ListScheduledEventsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListScheduledEventsRequest.

        每页返回的事件个数。取值范围：1~100（默认值为10）

        :param limit: The limit of this ListScheduledEventsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListScheduledEventsRequest.

        分页标记。从marker指定的下一条数据开始查询。

        :return: The marker of this ListScheduledEventsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListScheduledEventsRequest.

        分页标记。从marker指定的下一条数据开始查询。

        :param marker: The marker of this ListScheduledEventsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def event_id(self):
        r"""Gets the event_id of this ListScheduledEventsRequest.

        计划事件id。

        :return: The event_id of this ListScheduledEventsRequest.
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        r"""Sets the event_id of this ListScheduledEventsRequest.

        计划事件id。

        :param event_id: The event_id of this ListScheduledEventsRequest.
        :type event_id: str
        """
        self._event_id = event_id

    @property
    def server_id(self):
        r"""Gets the server_id of this ListScheduledEventsRequest.

        云手机服务器的唯一标识。

        :return: The server_id of this ListScheduledEventsRequest.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        r"""Sets the server_id of this ListScheduledEventsRequest.

        云手机服务器的唯一标识。

        :param server_id: The server_id of this ListScheduledEventsRequest.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def publish_since(self):
        r"""Gets the publish_since of this ListScheduledEventsRequest.

        事件发布开始时间，按照时间范围过滤。

        :return: The publish_since of this ListScheduledEventsRequest.
        :rtype: str
        """
        return self._publish_since

    @publish_since.setter
    def publish_since(self, publish_since):
        r"""Sets the publish_since of this ListScheduledEventsRequest.

        事件发布开始时间，按照时间范围过滤。

        :param publish_since: The publish_since of this ListScheduledEventsRequest.
        :type publish_since: str
        """
        self._publish_since = publish_since

    @property
    def publish_until(self):
        r"""Gets the publish_until of this ListScheduledEventsRequest.

        事件发布结束时间，按照时间范围过滤。

        :return: The publish_until of this ListScheduledEventsRequest.
        :rtype: str
        """
        return self._publish_until

    @publish_until.setter
    def publish_until(self, publish_until):
        r"""Sets the publish_until of this ListScheduledEventsRequest.

        事件发布结束时间，按照时间范围过滤。

        :param publish_until: The publish_until of this ListScheduledEventsRequest.
        :type publish_until: str
        """
        self._publish_until = publish_until

    @property
    def state(self):
        r"""Gets the state of this ListScheduledEventsRequest.

        计划事件状态。支持多值查询过滤。 取值范围： inquiring: 待授权、 scheduled：待执行、 executing：执行中、 completed：执行成功、 failed：执行失败、 canceled：取消

        :return: The state of this ListScheduledEventsRequest.
        :rtype: list[str]
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ListScheduledEventsRequest.

        计划事件状态。支持多值查询过滤。 取值范围： inquiring: 待授权、 scheduled：待执行、 executing：执行中、 completed：执行成功、 failed：执行失败、 canceled：取消

        :param state: The state of this ListScheduledEventsRequest.
        :type state: list[str]
        """
        self._state = state

    @property
    def type(self):
        r"""Gets the type of this ListScheduledEventsRequest.

        计划事件类型。支持多值查询过滤。取值范围： localdisk-recovery：本地盘换盘、 system-maintenance：系统维护

        :return: The type of this ListScheduledEventsRequest.
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListScheduledEventsRequest.

        计划事件类型。支持多值查询过滤。取值范围： localdisk-recovery：本地盘换盘、 system-maintenance：系统维护

        :param type: The type of this ListScheduledEventsRequest.
        :type type: list[str]
        """
        self._type = type

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
        if not isinstance(other, ListScheduledEventsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
