# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpdatePublicRecordsetsFilter:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'relation': 'str',
        'conditions': 'list[BatchUpdatePublicRecordsetsConditionvalue]'
    }

    attribute_map = {
        'relation': 'relation',
        'conditions': 'conditions'
    }

    def __init__(self, relation=None, conditions=None):
        r"""BatchUpdatePublicRecordsetsFilter

        The model defined in huaweicloud sdk

        :param relation: **参数解释：** 过滤条件之间的关系。 **约束限制：** 不涉及。 **取值范围：** - OR：或 - AND：与  **默认取值：** 不涉及。
        :type relation: str
        :param conditions: **参数解释：** 条件列表。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type conditions: list[:class:`huaweicloudsdkdns.v2.BatchUpdatePublicRecordsetsConditionvalue`]
        """
        
        

        self._relation = None
        self._conditions = None
        self.discriminator = None

        self.relation = relation
        self.conditions = conditions

    @property
    def relation(self):
        r"""Gets the relation of this BatchUpdatePublicRecordsetsFilter.

        **参数解释：** 过滤条件之间的关系。 **约束限制：** 不涉及。 **取值范围：** - OR：或 - AND：与  **默认取值：** 不涉及。

        :return: The relation of this BatchUpdatePublicRecordsetsFilter.
        :rtype: str
        """
        return self._relation

    @relation.setter
    def relation(self, relation):
        r"""Sets the relation of this BatchUpdatePublicRecordsetsFilter.

        **参数解释：** 过滤条件之间的关系。 **约束限制：** 不涉及。 **取值范围：** - OR：或 - AND：与  **默认取值：** 不涉及。

        :param relation: The relation of this BatchUpdatePublicRecordsetsFilter.
        :type relation: str
        """
        self._relation = relation

    @property
    def conditions(self):
        r"""Gets the conditions of this BatchUpdatePublicRecordsetsFilter.

        **参数解释：** 条件列表。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The conditions of this BatchUpdatePublicRecordsetsFilter.
        :rtype: list[:class:`huaweicloudsdkdns.v2.BatchUpdatePublicRecordsetsConditionvalue`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        r"""Sets the conditions of this BatchUpdatePublicRecordsetsFilter.

        **参数解释：** 条件列表。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param conditions: The conditions of this BatchUpdatePublicRecordsetsFilter.
        :type conditions: list[:class:`huaweicloudsdkdns.v2.BatchUpdatePublicRecordsetsConditionvalue`]
        """
        self._conditions = conditions

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
        if not isinstance(other, BatchUpdatePublicRecordsetsFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
