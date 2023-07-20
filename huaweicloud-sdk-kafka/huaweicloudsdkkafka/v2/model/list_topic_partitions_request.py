# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTopicPartitionsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'topic': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'topic': 'topic',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, instance_id=None, topic=None, offset=None, limit=None):
        """ListTopicPartitionsRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例id
        :type instance_id: str
        :param topic: 主题
        :type topic: str
        :param offset: 偏移量，表示查询该偏移量后面的记录
        :type offset: int
        :param limit: 查询返回记录的数量限制
        :type limit: int
        """
        
        

        self._instance_id = None
        self._topic = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.instance_id = instance_id
        self.topic = topic
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def instance_id(self):
        """Gets the instance_id of this ListTopicPartitionsRequest.

        实例id

        :return: The instance_id of this ListTopicPartitionsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListTopicPartitionsRequest.

        实例id

        :param instance_id: The instance_id of this ListTopicPartitionsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def topic(self):
        """Gets the topic of this ListTopicPartitionsRequest.

        主题

        :return: The topic of this ListTopicPartitionsRequest.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this ListTopicPartitionsRequest.

        主题

        :param topic: The topic of this ListTopicPartitionsRequest.
        :type topic: str
        """
        self._topic = topic

    @property
    def offset(self):
        """Gets the offset of this ListTopicPartitionsRequest.

        偏移量，表示查询该偏移量后面的记录

        :return: The offset of this ListTopicPartitionsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListTopicPartitionsRequest.

        偏移量，表示查询该偏移量后面的记录

        :param offset: The offset of this ListTopicPartitionsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListTopicPartitionsRequest.

        查询返回记录的数量限制

        :return: The limit of this ListTopicPartitionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListTopicPartitionsRequest.

        查询返回记录的数量限制

        :param limit: The limit of this ListTopicPartitionsRequest.
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
        if not isinstance(other, ListTopicPartitionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
