# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCeshierarchyRespGroups:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'topics': 'list[ShowCeshierarchyRespTopics]'
    }

    attribute_map = {
        'name': 'name',
        'topics': 'topics'
    }

    def __init__(self, name=None, topics=None):
        r"""ShowCeshierarchyRespGroups

        The model defined in huaweicloud sdk

        :param name: **参数解释**： 消费组名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type name: str
        :param topics: **参数解释**： 订阅Topic信息。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type topics: list[:class:`huaweicloudsdkrocketmq.v2.ShowCeshierarchyRespTopics`]
        """
        
        

        self._name = None
        self._topics = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if topics is not None:
            self.topics = topics

    @property
    def name(self):
        r"""Gets the name of this ShowCeshierarchyRespGroups.

        **参数解释**： 消费组名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The name of this ShowCeshierarchyRespGroups.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowCeshierarchyRespGroups.

        **参数解释**： 消费组名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param name: The name of this ShowCeshierarchyRespGroups.
        :type name: str
        """
        self._name = name

    @property
    def topics(self):
        r"""Gets the topics of this ShowCeshierarchyRespGroups.

        **参数解释**： 订阅Topic信息。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The topics of this ShowCeshierarchyRespGroups.
        :rtype: list[:class:`huaweicloudsdkrocketmq.v2.ShowCeshierarchyRespTopics`]
        """
        return self._topics

    @topics.setter
    def topics(self, topics):
        r"""Sets the topics of this ShowCeshierarchyRespGroups.

        **参数解释**： 订阅Topic信息。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param topics: The topics of this ShowCeshierarchyRespGroups.
        :type topics: list[:class:`huaweicloudsdkrocketmq.v2.ShowCeshierarchyRespTopics`]
        """
        self._topics = topics

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
        if not isinstance(other, ShowCeshierarchyRespGroups):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
