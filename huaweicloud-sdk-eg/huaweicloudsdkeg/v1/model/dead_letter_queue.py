# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeadLetterQueue:

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
        'instance_id': 'str',
        'connection_id': 'str',
        'topic': 'str'
    }

    attribute_map = {
        'type': 'type',
        'instance_id': 'instance_id',
        'connection_id': 'connection_id',
        'topic': 'topic'
    }

    def __init__(self, type=None, instance_id=None, connection_id=None, topic=None):
        r"""DeadLetterQueue

        The model defined in huaweicloud sdk

        :param type: 队列类型
        :type type: str
        :param instance_id: 实例id
        :type instance_id: str
        :param connection_id: 目标连接id
        :type connection_id: str
        :param topic: 主题
        :type topic: str
        """
        
        

        self._type = None
        self._instance_id = None
        self._connection_id = None
        self._topic = None
        self.discriminator = None

        self.type = type
        self.instance_id = instance_id
        self.connection_id = connection_id
        self.topic = topic

    @property
    def type(self):
        r"""Gets the type of this DeadLetterQueue.

        队列类型

        :return: The type of this DeadLetterQueue.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this DeadLetterQueue.

        队列类型

        :param type: The type of this DeadLetterQueue.
        :type type: str
        """
        self._type = type

    @property
    def instance_id(self):
        r"""Gets the instance_id of this DeadLetterQueue.

        实例id

        :return: The instance_id of this DeadLetterQueue.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this DeadLetterQueue.

        实例id

        :param instance_id: The instance_id of this DeadLetterQueue.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def connection_id(self):
        r"""Gets the connection_id of this DeadLetterQueue.

        目标连接id

        :return: The connection_id of this DeadLetterQueue.
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        r"""Sets the connection_id of this DeadLetterQueue.

        目标连接id

        :param connection_id: The connection_id of this DeadLetterQueue.
        :type connection_id: str
        """
        self._connection_id = connection_id

    @property
    def topic(self):
        r"""Gets the topic of this DeadLetterQueue.

        主题

        :return: The topic of this DeadLetterQueue.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        r"""Sets the topic of this DeadLetterQueue.

        主题

        :param topic: The topic of this DeadLetterQueue.
        :type topic: str
        """
        self._topic = topic

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
        if not isinstance(other, DeadLetterQueue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
