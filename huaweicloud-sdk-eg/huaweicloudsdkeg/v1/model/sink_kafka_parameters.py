# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SinkKafkaParameters:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'topic': 'str',
        'key_transform': 'list[TransForm]',
        'connection_id': 'str'
    }

    attribute_map = {
        'topic': 'topic',
        'key_transform': 'keyTransform',
        'connection_id': 'connectionId'
    }

    def __init__(self, topic=None, key_transform=None, connection_id=None):
        r"""SinkKafkaParameters

        The model defined in huaweicloud sdk

        :param topic: topic名称
        :type topic: str
        :param key_transform: key的转换规则
        :type key_transform: list[:class:`huaweicloudsdkeg.v1.TransForm`]
        :param connection_id: 目标连接id
        :type connection_id: str
        """
        
        

        self._topic = None
        self._key_transform = None
        self._connection_id = None
        self.discriminator = None

        self.topic = topic
        if key_transform is not None:
            self.key_transform = key_transform
        self.connection_id = connection_id

    @property
    def topic(self):
        r"""Gets the topic of this SinkKafkaParameters.

        topic名称

        :return: The topic of this SinkKafkaParameters.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        r"""Sets the topic of this SinkKafkaParameters.

        topic名称

        :param topic: The topic of this SinkKafkaParameters.
        :type topic: str
        """
        self._topic = topic

    @property
    def key_transform(self):
        r"""Gets the key_transform of this SinkKafkaParameters.

        key的转换规则

        :return: The key_transform of this SinkKafkaParameters.
        :rtype: list[:class:`huaweicloudsdkeg.v1.TransForm`]
        """
        return self._key_transform

    @key_transform.setter
    def key_transform(self, key_transform):
        r"""Sets the key_transform of this SinkKafkaParameters.

        key的转换规则

        :param key_transform: The key_transform of this SinkKafkaParameters.
        :type key_transform: list[:class:`huaweicloudsdkeg.v1.TransForm`]
        """
        self._key_transform = key_transform

    @property
    def connection_id(self):
        r"""Gets the connection_id of this SinkKafkaParameters.

        目标连接id

        :return: The connection_id of this SinkKafkaParameters.
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        r"""Sets the connection_id of this SinkKafkaParameters.

        目标连接id

        :param connection_id: The connection_id of this SinkKafkaParameters.
        :type connection_id: str
        """
        self._connection_id = connection_id

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
        if not isinstance(other, SinkKafkaParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
