# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowKafkaTopicDetailResponseBody:

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
        'create_time': 'int',
        'partitions': 'list[ShowKafkaTopicDetailResponsePartitions]'
    }

    attribute_map = {
        'topic': 'topic',
        'create_time': 'create_time',
        'partitions': 'partitions'
    }

    def __init__(self, topic=None, create_time=None, partitions=None):
        r"""ShowKafkaTopicDetailResponseBody

        The model defined in huaweicloud sdk

        :param topic: **参数解释**： Topic名称。  **取值范围**： 不涉及。
        :type topic: str
        :param create_time: **参数解释**： 创建时间。  **取值范围**： 不涉及。
        :type create_time: int
        :param partitions: **参数解释**： 分区列表。
        :type partitions: list[:class:`huaweicloudsdkkafka.v2.ShowKafkaTopicDetailResponsePartitions`]
        """
        
        

        self._topic = None
        self._create_time = None
        self._partitions = None
        self.discriminator = None

        if topic is not None:
            self.topic = topic
        if create_time is not None:
            self.create_time = create_time
        if partitions is not None:
            self.partitions = partitions

    @property
    def topic(self):
        r"""Gets the topic of this ShowKafkaTopicDetailResponseBody.

        **参数解释**： Topic名称。  **取值范围**： 不涉及。

        :return: The topic of this ShowKafkaTopicDetailResponseBody.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        r"""Sets the topic of this ShowKafkaTopicDetailResponseBody.

        **参数解释**： Topic名称。  **取值范围**： 不涉及。

        :param topic: The topic of this ShowKafkaTopicDetailResponseBody.
        :type topic: str
        """
        self._topic = topic

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowKafkaTopicDetailResponseBody.

        **参数解释**： 创建时间。  **取值范围**： 不涉及。

        :return: The create_time of this ShowKafkaTopicDetailResponseBody.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowKafkaTopicDetailResponseBody.

        **参数解释**： 创建时间。  **取值范围**： 不涉及。

        :param create_time: The create_time of this ShowKafkaTopicDetailResponseBody.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def partitions(self):
        r"""Gets the partitions of this ShowKafkaTopicDetailResponseBody.

        **参数解释**： 分区列表。

        :return: The partitions of this ShowKafkaTopicDetailResponseBody.
        :rtype: list[:class:`huaweicloudsdkkafka.v2.ShowKafkaTopicDetailResponsePartitions`]
        """
        return self._partitions

    @partitions.setter
    def partitions(self, partitions):
        r"""Sets the partitions of this ShowKafkaTopicDetailResponseBody.

        **参数解释**： 分区列表。

        :param partitions: The partitions of this ShowKafkaTopicDetailResponseBody.
        :type partitions: list[:class:`huaweicloudsdkkafka.v2.ShowKafkaTopicDetailResponsePartitions`]
        """
        self._partitions = partitions

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
        if not isinstance(other, ShowKafkaTopicDetailResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
