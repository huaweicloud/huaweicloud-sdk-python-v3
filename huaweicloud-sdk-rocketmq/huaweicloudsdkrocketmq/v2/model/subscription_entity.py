# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubscriptionEntity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'topic_name': 'str',
        'consumers_in_tags': 'list[ConsumersInTagEntity]'
    }

    attribute_map = {
        'topic_name': 'topic_name',
        'consumers_in_tags': 'consumers_in_tags'
    }

    def __init__(self, topic_name=None, consumers_in_tags=None):
        r"""SubscriptionEntity

        The model defined in huaweicloud sdk

        :param topic_name: **参数解释**： Topic名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type topic_name: str
        :param consumers_in_tags: **参数解释**： 消费者标签列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type consumers_in_tags: list[:class:`huaweicloudsdkrocketmq.v2.ConsumersInTagEntity`]
        """
        
        

        self._topic_name = None
        self._consumers_in_tags = None
        self.discriminator = None

        if topic_name is not None:
            self.topic_name = topic_name
        if consumers_in_tags is not None:
            self.consumers_in_tags = consumers_in_tags

    @property
    def topic_name(self):
        r"""Gets the topic_name of this SubscriptionEntity.

        **参数解释**： Topic名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The topic_name of this SubscriptionEntity.
        :rtype: str
        """
        return self._topic_name

    @topic_name.setter
    def topic_name(self, topic_name):
        r"""Sets the topic_name of this SubscriptionEntity.

        **参数解释**： Topic名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param topic_name: The topic_name of this SubscriptionEntity.
        :type topic_name: str
        """
        self._topic_name = topic_name

    @property
    def consumers_in_tags(self):
        r"""Gets the consumers_in_tags of this SubscriptionEntity.

        **参数解释**： 消费者标签列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The consumers_in_tags of this SubscriptionEntity.
        :rtype: list[:class:`huaweicloudsdkrocketmq.v2.ConsumersInTagEntity`]
        """
        return self._consumers_in_tags

    @consumers_in_tags.setter
    def consumers_in_tags(self, consumers_in_tags):
        r"""Sets the consumers_in_tags of this SubscriptionEntity.

        **参数解释**： 消费者标签列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param consumers_in_tags: The consumers_in_tags of this SubscriptionEntity.
        :type consumers_in_tags: list[:class:`huaweicloudsdkrocketmq.v2.ConsumersInTagEntity`]
        """
        self._consumers_in_tags = consumers_in_tags

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
        if not isinstance(other, SubscriptionEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
