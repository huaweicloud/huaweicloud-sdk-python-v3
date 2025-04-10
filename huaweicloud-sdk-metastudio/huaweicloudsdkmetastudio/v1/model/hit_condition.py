# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HitCondition:

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
        'priority': 'int',
        'tags': 'list[HitConditionTag]'
    }

    attribute_map = {
        'relation': 'relation',
        'priority': 'priority',
        'tags': 'tags'
    }

    def __init__(self, relation=None, priority=None, tags=None):
        r"""HitCondition

        The model defined in huaweicloud sdk

        :param relation: **参数解释**： 条件关系。对于多个条件的逻辑运算关系。 **约束限制**： 不涉及。 **取值范围**： * AND：表示多个条件同时满足。 * OR：表示多个条件满足其一即可。 * RESERVED：兜底回复不会去判断其他命中条件。  **默认取值**： 不涉及。
        :type relation: str
        :param priority: **参数解释**： 优先级，数值越低优先级越高；取值0-999，默认值为500，为可选值 **约束限制**： 不涉及
        :type priority: int
        :param tags: 匹配关系配置
        :type tags: list[:class:`huaweicloudsdkmetastudio.v1.HitConditionTag`]
        """
        
        

        self._relation = None
        self._priority = None
        self._tags = None
        self.discriminator = None

        if relation is not None:
            self.relation = relation
        if priority is not None:
            self.priority = priority
        if tags is not None:
            self.tags = tags

    @property
    def relation(self):
        r"""Gets the relation of this HitCondition.

        **参数解释**： 条件关系。对于多个条件的逻辑运算关系。 **约束限制**： 不涉及。 **取值范围**： * AND：表示多个条件同时满足。 * OR：表示多个条件满足其一即可。 * RESERVED：兜底回复不会去判断其他命中条件。  **默认取值**： 不涉及。

        :return: The relation of this HitCondition.
        :rtype: str
        """
        return self._relation

    @relation.setter
    def relation(self, relation):
        r"""Sets the relation of this HitCondition.

        **参数解释**： 条件关系。对于多个条件的逻辑运算关系。 **约束限制**： 不涉及。 **取值范围**： * AND：表示多个条件同时满足。 * OR：表示多个条件满足其一即可。 * RESERVED：兜底回复不会去判断其他命中条件。  **默认取值**： 不涉及。

        :param relation: The relation of this HitCondition.
        :type relation: str
        """
        self._relation = relation

    @property
    def priority(self):
        r"""Gets the priority of this HitCondition.

        **参数解释**： 优先级，数值越低优先级越高；取值0-999，默认值为500，为可选值 **约束限制**： 不涉及

        :return: The priority of this HitCondition.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this HitCondition.

        **参数解释**： 优先级，数值越低优先级越高；取值0-999，默认值为500，为可选值 **约束限制**： 不涉及

        :param priority: The priority of this HitCondition.
        :type priority: int
        """
        self._priority = priority

    @property
    def tags(self):
        r"""Gets the tags of this HitCondition.

        匹配关系配置

        :return: The tags of this HitCondition.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.HitConditionTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this HitCondition.

        匹配关系配置

        :param tags: The tags of this HitCondition.
        :type tags: list[:class:`huaweicloudsdkmetastudio.v1.HitConditionTag`]
        """
        self._tags = tags

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
        if not isinstance(other, HitCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
