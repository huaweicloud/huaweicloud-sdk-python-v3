# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMessagesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'engine': 'str',
        'instance_id': 'str',
        'topic': 'str',
        'queue': 'str',
        'limit': 'str',
        'offset': 'str',
        'key': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'msg_id': 'str'
    }

    attribute_map = {
        'engine': 'engine',
        'instance_id': 'instance_id',
        'topic': 'topic',
        'queue': 'queue',
        'limit': 'limit',
        'offset': 'offset',
        'key': 'key',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'msg_id': 'msg_id'
    }

    def __init__(self, engine=None, instance_id=None, topic=None, queue=None, limit=None, offset=None, key=None, start_time=None, end_time=None, msg_id=None):
        r"""ListMessagesRequest

        The model defined in huaweicloud sdk

        :param engine: 消息引擎。
        :type engine: str
        :param instance_id: 实例ID。
        :type instance_id: str
        :param topic: 主题名称。
        :type topic: str
        :param queue: 队列。
        :type queue: str
        :param limit: 查询数量。
        :type limit: str
        :param offset: 偏移量，表示从此偏移量开始查询， offset大于等于0。
        :type offset: str
        :param key: 消息的key。
        :type key: str
        :param start_time: 开始时间（不通过msg_id精确查询消息时，此参数必填）。
        :type start_time: str
        :param end_time: 结束时间（不通过msg_id精确查询消息时，此参数必填）。
        :type end_time: str
        :param msg_id: 消息ID。
        :type msg_id: str
        """
        
        

        self._engine = None
        self._instance_id = None
        self._topic = None
        self._queue = None
        self._limit = None
        self._offset = None
        self._key = None
        self._start_time = None
        self._end_time = None
        self._msg_id = None
        self.discriminator = None

        self.engine = engine
        self.instance_id = instance_id
        self.topic = topic
        if queue is not None:
            self.queue = queue
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if key is not None:
            self.key = key
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if msg_id is not None:
            self.msg_id = msg_id

    @property
    def engine(self):
        r"""Gets the engine of this ListMessagesRequest.

        消息引擎。

        :return: The engine of this ListMessagesRequest.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        r"""Sets the engine of this ListMessagesRequest.

        消息引擎。

        :param engine: The engine of this ListMessagesRequest.
        :type engine: str
        """
        self._engine = engine

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListMessagesRequest.

        实例ID。

        :return: The instance_id of this ListMessagesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListMessagesRequest.

        实例ID。

        :param instance_id: The instance_id of this ListMessagesRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def topic(self):
        r"""Gets the topic of this ListMessagesRequest.

        主题名称。

        :return: The topic of this ListMessagesRequest.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        r"""Sets the topic of this ListMessagesRequest.

        主题名称。

        :param topic: The topic of this ListMessagesRequest.
        :type topic: str
        """
        self._topic = topic

    @property
    def queue(self):
        r"""Gets the queue of this ListMessagesRequest.

        队列。

        :return: The queue of this ListMessagesRequest.
        :rtype: str
        """
        return self._queue

    @queue.setter
    def queue(self, queue):
        r"""Sets the queue of this ListMessagesRequest.

        队列。

        :param queue: The queue of this ListMessagesRequest.
        :type queue: str
        """
        self._queue = queue

    @property
    def limit(self):
        r"""Gets the limit of this ListMessagesRequest.

        查询数量。

        :return: The limit of this ListMessagesRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListMessagesRequest.

        查询数量。

        :param limit: The limit of this ListMessagesRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListMessagesRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0。

        :return: The offset of this ListMessagesRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListMessagesRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0。

        :param offset: The offset of this ListMessagesRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def key(self):
        r"""Gets the key of this ListMessagesRequest.

        消息的key。

        :return: The key of this ListMessagesRequest.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this ListMessagesRequest.

        消息的key。

        :param key: The key of this ListMessagesRequest.
        :type key: str
        """
        self._key = key

    @property
    def start_time(self):
        r"""Gets the start_time of this ListMessagesRequest.

        开始时间（不通过msg_id精确查询消息时，此参数必填）。

        :return: The start_time of this ListMessagesRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListMessagesRequest.

        开始时间（不通过msg_id精确查询消息时，此参数必填）。

        :param start_time: The start_time of this ListMessagesRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListMessagesRequest.

        结束时间（不通过msg_id精确查询消息时，此参数必填）。

        :return: The end_time of this ListMessagesRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListMessagesRequest.

        结束时间（不通过msg_id精确查询消息时，此参数必填）。

        :param end_time: The end_time of this ListMessagesRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def msg_id(self):
        r"""Gets the msg_id of this ListMessagesRequest.

        消息ID。

        :return: The msg_id of this ListMessagesRequest.
        :rtype: str
        """
        return self._msg_id

    @msg_id.setter
    def msg_id(self, msg_id):
        r"""Sets the msg_id of this ListMessagesRequest.

        消息ID。

        :param msg_id: The msg_id of this ListMessagesRequest.
        :type msg_id: str
        """
        self._msg_id = msg_id

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
        if not isinstance(other, ListMessagesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
