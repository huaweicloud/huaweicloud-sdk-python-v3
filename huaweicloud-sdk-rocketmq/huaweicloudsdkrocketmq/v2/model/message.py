# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Message:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'msg_id': 'str',
        'instance_id': 'str',
        'topic': 'str',
        'store_timestamp': 'float',
        'born_timestamp': 'float',
        'reconsume_times': 'str',
        'body': 'str',
        'body_crc': 'float',
        'store_size': 'float',
        'property_list': 'list[MessagePropertyList]',
        'born_host': 'str',
        'store_host': 'str',
        'queue_id': 'str',
        'queue_offset': 'str'
    }

    attribute_map = {
        'msg_id': 'msg_id',
        'instance_id': 'instance_id',
        'topic': 'topic',
        'store_timestamp': 'store_timestamp',
        'born_timestamp': 'born_timestamp',
        'reconsume_times': 'reconsume_times',
        'body': 'body',
        'body_crc': 'body_crc',
        'store_size': 'store_size',
        'property_list': 'property_list',
        'born_host': 'born_host',
        'store_host': 'store_host',
        'queue_id': 'queue_id',
        'queue_offset': 'queue_offset'
    }

    def __init__(self, msg_id=None, instance_id=None, topic=None, store_timestamp=None, born_timestamp=None, reconsume_times=None, body=None, body_crc=None, store_size=None, property_list=None, born_host=None, store_host=None, queue_id=None, queue_offset=None):
        """Message

        The model defined in huaweicloud sdk

        :param msg_id: 消息ID。
        :type msg_id: str
        :param instance_id: 实例ID。
        :type instance_id: str
        :param topic: 主题名称。
        :type topic: str
        :param store_timestamp: 存储消息的时间。
        :type store_timestamp: float
        :param born_timestamp: 产生消息的时间。
        :type born_timestamp: float
        :param reconsume_times: 重试次数。
        :type reconsume_times: str
        :param body: 消息体。
        :type body: str
        :param body_crc: 消息体校验和。
        :type body_crc: float
        :param store_size: 存储大小。
        :type store_size: float
        :param property_list: 消息属性列表。
        :type property_list: list[:class:`huaweicloudsdkrocketmq.v2.MessagePropertyList`]
        :param born_host: 产生消息的主机IP。
        :type born_host: str
        :param store_host: 存储消息的主机IP。
        :type store_host: str
        :param queue_id: 队列ID。
        :type queue_id: str
        :param queue_offset: 在队列中的偏移量。
        :type queue_offset: str
        """
        
        

        self._msg_id = None
        self._instance_id = None
        self._topic = None
        self._store_timestamp = None
        self._born_timestamp = None
        self._reconsume_times = None
        self._body = None
        self._body_crc = None
        self._store_size = None
        self._property_list = None
        self._born_host = None
        self._store_host = None
        self._queue_id = None
        self._queue_offset = None
        self.discriminator = None

        if msg_id is not None:
            self.msg_id = msg_id
        if instance_id is not None:
            self.instance_id = instance_id
        if topic is not None:
            self.topic = topic
        if store_timestamp is not None:
            self.store_timestamp = store_timestamp
        if born_timestamp is not None:
            self.born_timestamp = born_timestamp
        if reconsume_times is not None:
            self.reconsume_times = reconsume_times
        if body is not None:
            self.body = body
        if body_crc is not None:
            self.body_crc = body_crc
        if store_size is not None:
            self.store_size = store_size
        if property_list is not None:
            self.property_list = property_list
        if born_host is not None:
            self.born_host = born_host
        if store_host is not None:
            self.store_host = store_host
        if queue_id is not None:
            self.queue_id = queue_id
        if queue_offset is not None:
            self.queue_offset = queue_offset

    @property
    def msg_id(self):
        """Gets the msg_id of this Message.

        消息ID。

        :return: The msg_id of this Message.
        :rtype: str
        """
        return self._msg_id

    @msg_id.setter
    def msg_id(self, msg_id):
        """Sets the msg_id of this Message.

        消息ID。

        :param msg_id: The msg_id of this Message.
        :type msg_id: str
        """
        self._msg_id = msg_id

    @property
    def instance_id(self):
        """Gets the instance_id of this Message.

        实例ID。

        :return: The instance_id of this Message.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this Message.

        实例ID。

        :param instance_id: The instance_id of this Message.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def topic(self):
        """Gets the topic of this Message.

        主题名称。

        :return: The topic of this Message.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this Message.

        主题名称。

        :param topic: The topic of this Message.
        :type topic: str
        """
        self._topic = topic

    @property
    def store_timestamp(self):
        """Gets the store_timestamp of this Message.

        存储消息的时间。

        :return: The store_timestamp of this Message.
        :rtype: float
        """
        return self._store_timestamp

    @store_timestamp.setter
    def store_timestamp(self, store_timestamp):
        """Sets the store_timestamp of this Message.

        存储消息的时间。

        :param store_timestamp: The store_timestamp of this Message.
        :type store_timestamp: float
        """
        self._store_timestamp = store_timestamp

    @property
    def born_timestamp(self):
        """Gets the born_timestamp of this Message.

        产生消息的时间。

        :return: The born_timestamp of this Message.
        :rtype: float
        """
        return self._born_timestamp

    @born_timestamp.setter
    def born_timestamp(self, born_timestamp):
        """Sets the born_timestamp of this Message.

        产生消息的时间。

        :param born_timestamp: The born_timestamp of this Message.
        :type born_timestamp: float
        """
        self._born_timestamp = born_timestamp

    @property
    def reconsume_times(self):
        """Gets the reconsume_times of this Message.

        重试次数。

        :return: The reconsume_times of this Message.
        :rtype: str
        """
        return self._reconsume_times

    @reconsume_times.setter
    def reconsume_times(self, reconsume_times):
        """Sets the reconsume_times of this Message.

        重试次数。

        :param reconsume_times: The reconsume_times of this Message.
        :type reconsume_times: str
        """
        self._reconsume_times = reconsume_times

    @property
    def body(self):
        """Gets the body of this Message.

        消息体。

        :return: The body of this Message.
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this Message.

        消息体。

        :param body: The body of this Message.
        :type body: str
        """
        self._body = body

    @property
    def body_crc(self):
        """Gets the body_crc of this Message.

        消息体校验和。

        :return: The body_crc of this Message.
        :rtype: float
        """
        return self._body_crc

    @body_crc.setter
    def body_crc(self, body_crc):
        """Sets the body_crc of this Message.

        消息体校验和。

        :param body_crc: The body_crc of this Message.
        :type body_crc: float
        """
        self._body_crc = body_crc

    @property
    def store_size(self):
        """Gets the store_size of this Message.

        存储大小。

        :return: The store_size of this Message.
        :rtype: float
        """
        return self._store_size

    @store_size.setter
    def store_size(self, store_size):
        """Sets the store_size of this Message.

        存储大小。

        :param store_size: The store_size of this Message.
        :type store_size: float
        """
        self._store_size = store_size

    @property
    def property_list(self):
        """Gets the property_list of this Message.

        消息属性列表。

        :return: The property_list of this Message.
        :rtype: list[:class:`huaweicloudsdkrocketmq.v2.MessagePropertyList`]
        """
        return self._property_list

    @property_list.setter
    def property_list(self, property_list):
        """Sets the property_list of this Message.

        消息属性列表。

        :param property_list: The property_list of this Message.
        :type property_list: list[:class:`huaweicloudsdkrocketmq.v2.MessagePropertyList`]
        """
        self._property_list = property_list

    @property
    def born_host(self):
        """Gets the born_host of this Message.

        产生消息的主机IP。

        :return: The born_host of this Message.
        :rtype: str
        """
        return self._born_host

    @born_host.setter
    def born_host(self, born_host):
        """Sets the born_host of this Message.

        产生消息的主机IP。

        :param born_host: The born_host of this Message.
        :type born_host: str
        """
        self._born_host = born_host

    @property
    def store_host(self):
        """Gets the store_host of this Message.

        存储消息的主机IP。

        :return: The store_host of this Message.
        :rtype: str
        """
        return self._store_host

    @store_host.setter
    def store_host(self, store_host):
        """Sets the store_host of this Message.

        存储消息的主机IP。

        :param store_host: The store_host of this Message.
        :type store_host: str
        """
        self._store_host = store_host

    @property
    def queue_id(self):
        """Gets the queue_id of this Message.

        队列ID。

        :return: The queue_id of this Message.
        :rtype: str
        """
        return self._queue_id

    @queue_id.setter
    def queue_id(self, queue_id):
        """Sets the queue_id of this Message.

        队列ID。

        :param queue_id: The queue_id of this Message.
        :type queue_id: str
        """
        self._queue_id = queue_id

    @property
    def queue_offset(self):
        """Gets the queue_offset of this Message.

        在队列中的偏移量。

        :return: The queue_offset of this Message.
        :rtype: str
        """
        return self._queue_offset

    @queue_offset.setter
    def queue_offset(self, queue_offset):
        """Sets the queue_offset of this Message.

        在队列中的偏移量。

        :param queue_offset: The queue_offset of this Message.
        :type queue_offset: str
        """
        self._queue_offset = queue_offset

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
        if not isinstance(other, Message):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
