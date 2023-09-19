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
        """HitCondition

        The model defined in huaweicloud sdk

        :param relation: 条件关系；取值And或者Or
        :type relation: str
        :param priority: 优先级，数值越低优先级越高；取值0-999，默认值为500，为可选值
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
        """Gets the relation of this HitCondition.

        条件关系；取值And或者Or

        :return: The relation of this HitCondition.
        :rtype: str
        """
        return self._relation

    @relation.setter
    def relation(self, relation):
        """Sets the relation of this HitCondition.

        条件关系；取值And或者Or

        :param relation: The relation of this HitCondition.
        :type relation: str
        """
        self._relation = relation

    @property
    def priority(self):
        """Gets the priority of this HitCondition.

        优先级，数值越低优先级越高；取值0-999，默认值为500，为可选值

        :return: The priority of this HitCondition.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this HitCondition.

        优先级，数值越低优先级越高；取值0-999，默认值为500，为可选值

        :param priority: The priority of this HitCondition.
        :type priority: int
        """
        self._priority = priority

    @property
    def tags(self):
        """Gets the tags of this HitCondition.

        匹配关系配置

        :return: The tags of this HitCondition.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.HitConditionTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this HitCondition.

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
