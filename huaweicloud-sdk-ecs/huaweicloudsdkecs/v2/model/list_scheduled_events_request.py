# coding: utf-8

import six

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
        'marker': 'str',
        'id': 'str',
        'instance_id': 'list[str]',
        'type': 'list[str]',
        'state': 'list[str]',
        'publish_since': 'str',
        'publish_until': 'str',
        'limit': 'int'
    }

    attribute_map = {
        'marker': 'marker',
        'id': 'id',
        'instance_id': 'instance_id',
        'type': 'type',
        'state': 'state',
        'publish_since': 'publish_since',
        'publish_until': 'publish_until',
        'limit': 'limit'
    }

    def __init__(self, marker=None, id=None, instance_id=None, type=None, state=None, publish_since=None, publish_until=None, limit=None):
        r"""ListScheduledEventsRequest

        The model defined in huaweicloud sdk

        :param marker: 从marker指定的事件的下一条数据开始查询。
        :type marker: str
        :param id: 事件ID
        :type id: str
        :param instance_id: 实例ID
        :type instance_id: list[str]
        :param type: 事件类型
        :type type: list[str]
        :param state: 事件状态
        :type state: list[str]
        :param publish_since: 事件发布开始时间
        :type publish_since: str
        :param publish_until: 事件发布截至时间
        :type publish_until: str
        :param limit: 每页显示的条目数量
        :type limit: int
        """
        
        

        self._marker = None
        self._id = None
        self._instance_id = None
        self._type = None
        self._state = None
        self._publish_since = None
        self._publish_until = None
        self._limit = None
        self.discriminator = None

        if marker is not None:
            self.marker = marker
        if id is not None:
            self.id = id
        if instance_id is not None:
            self.instance_id = instance_id
        if type is not None:
            self.type = type
        if state is not None:
            self.state = state
        if publish_since is not None:
            self.publish_since = publish_since
        if publish_until is not None:
            self.publish_until = publish_until
        if limit is not None:
            self.limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListScheduledEventsRequest.

        从marker指定的事件的下一条数据开始查询。

        :return: The marker of this ListScheduledEventsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListScheduledEventsRequest.

        从marker指定的事件的下一条数据开始查询。

        :param marker: The marker of this ListScheduledEventsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def id(self):
        r"""Gets the id of this ListScheduledEventsRequest.

        事件ID

        :return: The id of this ListScheduledEventsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListScheduledEventsRequest.

        事件ID

        :param id: The id of this ListScheduledEventsRequest.
        :type id: str
        """
        self._id = id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListScheduledEventsRequest.

        实例ID

        :return: The instance_id of this ListScheduledEventsRequest.
        :rtype: list[str]
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListScheduledEventsRequest.

        实例ID

        :param instance_id: The instance_id of this ListScheduledEventsRequest.
        :type instance_id: list[str]
        """
        self._instance_id = instance_id

    @property
    def type(self):
        r"""Gets the type of this ListScheduledEventsRequest.

        事件类型

        :return: The type of this ListScheduledEventsRequest.
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListScheduledEventsRequest.

        事件类型

        :param type: The type of this ListScheduledEventsRequest.
        :type type: list[str]
        """
        self._type = type

    @property
    def state(self):
        r"""Gets the state of this ListScheduledEventsRequest.

        事件状态

        :return: The state of this ListScheduledEventsRequest.
        :rtype: list[str]
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ListScheduledEventsRequest.

        事件状态

        :param state: The state of this ListScheduledEventsRequest.
        :type state: list[str]
        """
        self._state = state

    @property
    def publish_since(self):
        r"""Gets the publish_since of this ListScheduledEventsRequest.

        事件发布开始时间

        :return: The publish_since of this ListScheduledEventsRequest.
        :rtype: str
        """
        return self._publish_since

    @publish_since.setter
    def publish_since(self, publish_since):
        r"""Sets the publish_since of this ListScheduledEventsRequest.

        事件发布开始时间

        :param publish_since: The publish_since of this ListScheduledEventsRequest.
        :type publish_since: str
        """
        self._publish_since = publish_since

    @property
    def publish_until(self):
        r"""Gets the publish_until of this ListScheduledEventsRequest.

        事件发布截至时间

        :return: The publish_until of this ListScheduledEventsRequest.
        :rtype: str
        """
        return self._publish_until

    @publish_until.setter
    def publish_until(self, publish_until):
        r"""Sets the publish_until of this ListScheduledEventsRequest.

        事件发布截至时间

        :param publish_until: The publish_until of this ListScheduledEventsRequest.
        :type publish_until: str
        """
        self._publish_until = publish_until

    @property
    def limit(self):
        r"""Gets the limit of this ListScheduledEventsRequest.

        每页显示的条目数量

        :return: The limit of this ListScheduledEventsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListScheduledEventsRequest.

        每页显示的条目数量

        :param limit: The limit of this ListScheduledEventsRequest.
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
        if not isinstance(other, ListScheduledEventsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
