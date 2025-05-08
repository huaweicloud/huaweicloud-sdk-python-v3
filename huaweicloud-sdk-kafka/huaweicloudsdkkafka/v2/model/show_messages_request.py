# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMessagesRequest:

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
        'start_time': 'str',
        'end_time': 'str',
        'limit': 'int',
        'offset': 'int',
        'partition': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'topic': 'topic',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'limit': 'limit',
        'offset': 'offset',
        'partition': 'partition'
    }

    def __init__(self, instance_id=None, topic=None, start_time=None, end_time=None, limit=None, offset=None, partition=None):
        r"""ShowMessagesRequest

        The model defined in huaweicloud sdk

        :param instance_id: **参数解释**： 实例ID。获取方法如下：登录Kafka控制台，在Kafka实例详情页面查找实例ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type instance_id: str
        :param topic: **参数解释**： Topic名称。 **约束限制**： Topic名称必须以字母开头且只支持大小写字母、中横线、下划线以及数字。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type topic: str
        :param start_time: **参数解释**： 查询起始时间，为Unix时间戳格式。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 0。
        :type start_time: str
        :param end_time: **参数解释**： 查询结束时间，为Unix时间戳格式。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 系统当前时间。
        :type end_time: str
        :param limit: **参数解释**： 单页返回消息数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 10。
        :type limit: int
        :param offset: **参数解释**： 偏移量，表示从此偏移量开始查询。 **约束限制**： 不涉及。 **取值范围**： 大于等于0。 **默认取值**： 不涉及。
        :type offset: int
        :param partition: **参数解释**： 分区编号。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 默认值为-1，若传入值为-1，则查询所有分区。
        :type partition: str
        """
        
        

        self._instance_id = None
        self._topic = None
        self._start_time = None
        self._end_time = None
        self._limit = None
        self._offset = None
        self._partition = None
        self.discriminator = None

        self.instance_id = instance_id
        self.topic = topic
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if partition is not None:
            self.partition = partition

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowMessagesRequest.

        **参数解释**： 实例ID。获取方法如下：登录Kafka控制台，在Kafka实例详情页面查找实例ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The instance_id of this ShowMessagesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowMessagesRequest.

        **参数解释**： 实例ID。获取方法如下：登录Kafka控制台，在Kafka实例详情页面查找实例ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param instance_id: The instance_id of this ShowMessagesRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def topic(self):
        r"""Gets the topic of this ShowMessagesRequest.

        **参数解释**： Topic名称。 **约束限制**： Topic名称必须以字母开头且只支持大小写字母、中横线、下划线以及数字。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The topic of this ShowMessagesRequest.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        r"""Sets the topic of this ShowMessagesRequest.

        **参数解释**： Topic名称。 **约束限制**： Topic名称必须以字母开头且只支持大小写字母、中横线、下划线以及数字。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param topic: The topic of this ShowMessagesRequest.
        :type topic: str
        """
        self._topic = topic

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowMessagesRequest.

        **参数解释**： 查询起始时间，为Unix时间戳格式。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 0。

        :return: The start_time of this ShowMessagesRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowMessagesRequest.

        **参数解释**： 查询起始时间，为Unix时间戳格式。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 0。

        :param start_time: The start_time of this ShowMessagesRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowMessagesRequest.

        **参数解释**： 查询结束时间，为Unix时间戳格式。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 系统当前时间。

        :return: The end_time of this ShowMessagesRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowMessagesRequest.

        **参数解释**： 查询结束时间，为Unix时间戳格式。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 系统当前时间。

        :param end_time: The end_time of this ShowMessagesRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def limit(self):
        r"""Gets the limit of this ShowMessagesRequest.

        **参数解释**： 单页返回消息数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 10。

        :return: The limit of this ShowMessagesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowMessagesRequest.

        **参数解释**： 单页返回消息数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 10。

        :param limit: The limit of this ShowMessagesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ShowMessagesRequest.

        **参数解释**： 偏移量，表示从此偏移量开始查询。 **约束限制**： 不涉及。 **取值范围**： 大于等于0。 **默认取值**： 不涉及。

        :return: The offset of this ShowMessagesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowMessagesRequest.

        **参数解释**： 偏移量，表示从此偏移量开始查询。 **约束限制**： 不涉及。 **取值范围**： 大于等于0。 **默认取值**： 不涉及。

        :param offset: The offset of this ShowMessagesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def partition(self):
        r"""Gets the partition of this ShowMessagesRequest.

        **参数解释**： 分区编号。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 默认值为-1，若传入值为-1，则查询所有分区。

        :return: The partition of this ShowMessagesRequest.
        :rtype: str
        """
        return self._partition

    @partition.setter
    def partition(self, partition):
        r"""Sets the partition of this ShowMessagesRequest.

        **参数解释**： 分区编号。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 默认值为-1，若传入值为-1，则查询所有分区。

        :param partition: The partition of this ShowMessagesRequest.
        :type partition: str
        """
        self._partition = partition

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
        if not isinstance(other, ShowMessagesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
