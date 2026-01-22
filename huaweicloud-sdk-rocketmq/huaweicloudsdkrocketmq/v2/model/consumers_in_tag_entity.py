# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConsumersInTagEntity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'consumers': 'list[str]',
        'tag_name': 'str'
    }

    attribute_map = {
        'consumers': 'consumers',
        'tag_name': 'tag_name'
    }

    def __init__(self, consumers=None, tag_name=None):
        r"""ConsumersInTagEntity

        The model defined in huaweicloud sdk

        :param consumers: **参数解释**： 消费者列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type consumers: list[str]
        :param tag_name: **参数解释**： 标签名。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type tag_name: str
        """
        
        

        self._consumers = None
        self._tag_name = None
        self.discriminator = None

        if consumers is not None:
            self.consumers = consumers
        if tag_name is not None:
            self.tag_name = tag_name

    @property
    def consumers(self):
        r"""Gets the consumers of this ConsumersInTagEntity.

        **参数解释**： 消费者列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The consumers of this ConsumersInTagEntity.
        :rtype: list[str]
        """
        return self._consumers

    @consumers.setter
    def consumers(self, consumers):
        r"""Sets the consumers of this ConsumersInTagEntity.

        **参数解释**： 消费者列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param consumers: The consumers of this ConsumersInTagEntity.
        :type consumers: list[str]
        """
        self._consumers = consumers

    @property
    def tag_name(self):
        r"""Gets the tag_name of this ConsumersInTagEntity.

        **参数解释**： 标签名。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The tag_name of this ConsumersInTagEntity.
        :rtype: str
        """
        return self._tag_name

    @tag_name.setter
    def tag_name(self, tag_name):
        r"""Sets the tag_name of this ConsumersInTagEntity.

        **参数解释**： 标签名。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param tag_name: The tag_name of this ConsumersInTagEntity.
        :type tag_name: str
        """
        self._tag_name = tag_name

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
        if not isinstance(other, ConsumersInTagEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
