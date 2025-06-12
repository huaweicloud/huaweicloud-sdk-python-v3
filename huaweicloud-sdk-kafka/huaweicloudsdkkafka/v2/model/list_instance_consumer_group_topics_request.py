# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceConsumerGroupTopicsRequest:

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
        'offset': 'int',
        'limit': 'int',
        'sort_key': 'str',
        'sort_dir': 'str',
        'topic': 'str'
    }

    attribute_map = {
        'engine': 'engine',
        'instance_id': 'instance_id',
        'group': 'group',
        'offset': 'offset',
        'limit': 'limit',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'topic': 'topic'
    }

    def __init__(self, engine=None, instance_id=None, group=None, offset=None, limit=None, sort_key=None, sort_dir=None, topic=None):
        r"""ListInstanceConsumerGroupTopicsRequest

        The model defined in huaweicloud sdk

        :param engine: 引擎。
        :type engine: str
        :param instance_id: 实例ID。
        :type instance_id: str
        :param group: 消费组ID。
        :type group: str
        :param offset: 偏移量，表示从此偏移量开始查询， offset大于等于0。
        :type offset: int
        :param limit: 当次查询返回的最大Topic个数，默认值为10，取值范围为1~50。
        :type limit: int
        :param sort_key: 排序规则： - topic：按Topic名称排序。 - partition：按分区数排序。 - messages：按消息数量排序，默认方式。
        :type sort_key: str
        :param sort_dir: 排序方式。 - asc：升序。 - desc：降序，默认方式。
        :type sort_dir: str
        :param topic: Topic名称。
        :type topic: str
        """
        
        

        self._engine = None
        self._instance_id = None
        self._group = None
        self._offset = None
        self._limit = None
        self._sort_key = None
        self._sort_dir = None
        self._topic = None
        self.discriminator = None

        self.engine = engine
        self.instance_id = instance_id
        self.group = group
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if topic is not None:
            self.topic = topic

    @property
    def engine(self):
        r"""Gets the engine of this ListInstanceConsumerGroupTopicsRequest.

        引擎。

        :return: The engine of this ListInstanceConsumerGroupTopicsRequest.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        r"""Sets the engine of this ListInstanceConsumerGroupTopicsRequest.

        引擎。

        :param engine: The engine of this ListInstanceConsumerGroupTopicsRequest.
        :type engine: str
        """
        self._engine = engine

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListInstanceConsumerGroupTopicsRequest.

        实例ID。

        :return: The instance_id of this ListInstanceConsumerGroupTopicsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListInstanceConsumerGroupTopicsRequest.

        实例ID。

        :param instance_id: The instance_id of this ListInstanceConsumerGroupTopicsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def group(self):
        r"""Gets the group of this ListInstanceConsumerGroupTopicsRequest.

        消费组ID。

        :return: The group of this ListInstanceConsumerGroupTopicsRequest.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        r"""Sets the group of this ListInstanceConsumerGroupTopicsRequest.

        消费组ID。

        :param group: The group of this ListInstanceConsumerGroupTopicsRequest.
        :type group: str
        """
        self._group = group

    @property
    def offset(self):
        r"""Gets the offset of this ListInstanceConsumerGroupTopicsRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0。

        :return: The offset of this ListInstanceConsumerGroupTopicsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListInstanceConsumerGroupTopicsRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0。

        :param offset: The offset of this ListInstanceConsumerGroupTopicsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListInstanceConsumerGroupTopicsRequest.

        当次查询返回的最大Topic个数，默认值为10，取值范围为1~50。

        :return: The limit of this ListInstanceConsumerGroupTopicsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListInstanceConsumerGroupTopicsRequest.

        当次查询返回的最大Topic个数，默认值为10，取值范围为1~50。

        :param limit: The limit of this ListInstanceConsumerGroupTopicsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListInstanceConsumerGroupTopicsRequest.

        排序规则： - topic：按Topic名称排序。 - partition：按分区数排序。 - messages：按消息数量排序，默认方式。

        :return: The sort_key of this ListInstanceConsumerGroupTopicsRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListInstanceConsumerGroupTopicsRequest.

        排序规则： - topic：按Topic名称排序。 - partition：按分区数排序。 - messages：按消息数量排序，默认方式。

        :param sort_key: The sort_key of this ListInstanceConsumerGroupTopicsRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListInstanceConsumerGroupTopicsRequest.

        排序方式。 - asc：升序。 - desc：降序，默认方式。

        :return: The sort_dir of this ListInstanceConsumerGroupTopicsRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListInstanceConsumerGroupTopicsRequest.

        排序方式。 - asc：升序。 - desc：降序，默认方式。

        :param sort_dir: The sort_dir of this ListInstanceConsumerGroupTopicsRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def topic(self):
        r"""Gets the topic of this ListInstanceConsumerGroupTopicsRequest.

        Topic名称。

        :return: The topic of this ListInstanceConsumerGroupTopicsRequest.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        r"""Sets the topic of this ListInstanceConsumerGroupTopicsRequest.

        Topic名称。

        :param topic: The topic of this ListInstanceConsumerGroupTopicsRequest.
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
        if not isinstance(other, ListInstanceConsumerGroupTopicsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
