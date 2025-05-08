# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceConsumerGroupMessageOffsetRequest:

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
        'group': 'str',
        'topic': 'str',
        'partition': 'str',
        'offset': 'str',
        'limit': 'str'
    }

    attribute_map = {
        'engine': 'engine',
        'instance_id': 'instance_id',
        'group': 'group',
        'topic': 'topic',
        'partition': 'partition',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, engine=None, instance_id=None, group=None, topic=None, partition=None, offset=None, limit=None):
        r"""ListInstanceConsumerGroupMessageOffsetRequest

        The model defined in huaweicloud sdk

        :param engine: 消息引擎。
        :type engine: str
        :param instance_id: 实例ID。
        :type instance_id: str
        :param group: 消费组名称。
        :type group: str
        :param topic: topic名称。
        :type topic: str
        :param partition: 分区名称。
        :type partition: str
        :param offset: 偏移值。
        :type offset: str
        :param limit: 最大值。
        :type limit: str
        """
        
        

        self._engine = None
        self._instance_id = None
        self._group = None
        self._topic = None
        self._partition = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.engine = engine
        self.instance_id = instance_id
        self.group = group
        if topic is not None:
            self.topic = topic
        if partition is not None:
            self.partition = partition
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def engine(self):
        r"""Gets the engine of this ListInstanceConsumerGroupMessageOffsetRequest.

        消息引擎。

        :return: The engine of this ListInstanceConsumerGroupMessageOffsetRequest.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        r"""Sets the engine of this ListInstanceConsumerGroupMessageOffsetRequest.

        消息引擎。

        :param engine: The engine of this ListInstanceConsumerGroupMessageOffsetRequest.
        :type engine: str
        """
        self._engine = engine

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListInstanceConsumerGroupMessageOffsetRequest.

        实例ID。

        :return: The instance_id of this ListInstanceConsumerGroupMessageOffsetRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListInstanceConsumerGroupMessageOffsetRequest.

        实例ID。

        :param instance_id: The instance_id of this ListInstanceConsumerGroupMessageOffsetRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def group(self):
        r"""Gets the group of this ListInstanceConsumerGroupMessageOffsetRequest.

        消费组名称。

        :return: The group of this ListInstanceConsumerGroupMessageOffsetRequest.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        r"""Sets the group of this ListInstanceConsumerGroupMessageOffsetRequest.

        消费组名称。

        :param group: The group of this ListInstanceConsumerGroupMessageOffsetRequest.
        :type group: str
        """
        self._group = group

    @property
    def topic(self):
        r"""Gets the topic of this ListInstanceConsumerGroupMessageOffsetRequest.

        topic名称。

        :return: The topic of this ListInstanceConsumerGroupMessageOffsetRequest.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        r"""Sets the topic of this ListInstanceConsumerGroupMessageOffsetRequest.

        topic名称。

        :param topic: The topic of this ListInstanceConsumerGroupMessageOffsetRequest.
        :type topic: str
        """
        self._topic = topic

    @property
    def partition(self):
        r"""Gets the partition of this ListInstanceConsumerGroupMessageOffsetRequest.

        分区名称。

        :return: The partition of this ListInstanceConsumerGroupMessageOffsetRequest.
        :rtype: str
        """
        return self._partition

    @partition.setter
    def partition(self, partition):
        r"""Sets the partition of this ListInstanceConsumerGroupMessageOffsetRequest.

        分区名称。

        :param partition: The partition of this ListInstanceConsumerGroupMessageOffsetRequest.
        :type partition: str
        """
        self._partition = partition

    @property
    def offset(self):
        r"""Gets the offset of this ListInstanceConsumerGroupMessageOffsetRequest.

        偏移值。

        :return: The offset of this ListInstanceConsumerGroupMessageOffsetRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListInstanceConsumerGroupMessageOffsetRequest.

        偏移值。

        :param offset: The offset of this ListInstanceConsumerGroupMessageOffsetRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListInstanceConsumerGroupMessageOffsetRequest.

        最大值。

        :return: The limit of this ListInstanceConsumerGroupMessageOffsetRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListInstanceConsumerGroupMessageOffsetRequest.

        最大值。

        :param limit: The limit of this ListInstanceConsumerGroupMessageOffsetRequest.
        :type limit: str
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
        if not isinstance(other, ListInstanceConsumerGroupMessageOffsetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
