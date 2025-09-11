# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MultiQueryConditionOption:

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
        'condition': 'str',
        'is_fuzzy': 'bool',
        'values': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'condition': 'condition',
        'is_fuzzy': 'is_fuzzy',
        'values': 'values'
    }

    def __init__(self, name=None, condition=None, is_fuzzy=None, values=None):
        r"""MultiQueryConditionOption

        The model defined in huaweicloud sdk

        :param name: **参数解释**： 查询字段名称。 **约束限制**： 只支持字符串\&quot;query\&quot;。 **取值范围**： 由英文字母（大小写）、数字或下划线组成，长度为 1 至 128 个字符。 **默认取值**： 不涉及。
        :type name: str
        :param condition: **参数解释**: 组合条件类型。 **约束限制**: 不涉及。 **取值范围**: 仅限字符串：\&quot;AND\&quot;、\&quot;OR\&quot;。 **默认取值**: 不涉及。
        :type condition: str
        :param is_fuzzy: **参数解释**: 多个过滤检索条件内容集合。 **约束限制**: 只支持为true进行模糊查询。 **取值范围**: - true：模糊查询。 - false：精确匹配。  **默认取值**: true 
        :type is_fuzzy: bool
        :param values: **参数解释**: 多个过滤检索条件内容集合。由 1 至 5 个字符串组成的列表。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type values: list[str]
        """
        
        

        self._name = None
        self._condition = None
        self._is_fuzzy = None
        self._values = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if condition is not None:
            self.condition = condition
        if is_fuzzy is not None:
            self.is_fuzzy = is_fuzzy
        if values is not None:
            self.values = values

    @property
    def name(self):
        r"""Gets the name of this MultiQueryConditionOption.

        **参数解释**： 查询字段名称。 **约束限制**： 只支持字符串\"query\"。 **取值范围**： 由英文字母（大小写）、数字或下划线组成，长度为 1 至 128 个字符。 **默认取值**： 不涉及。

        :return: The name of this MultiQueryConditionOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this MultiQueryConditionOption.

        **参数解释**： 查询字段名称。 **约束限制**： 只支持字符串\"query\"。 **取值范围**： 由英文字母（大小写）、数字或下划线组成，长度为 1 至 128 个字符。 **默认取值**： 不涉及。

        :param name: The name of this MultiQueryConditionOption.
        :type name: str
        """
        self._name = name

    @property
    def condition(self):
        r"""Gets the condition of this MultiQueryConditionOption.

        **参数解释**: 组合条件类型。 **约束限制**: 不涉及。 **取值范围**: 仅限字符串：\"AND\"、\"OR\"。 **默认取值**: 不涉及。

        :return: The condition of this MultiQueryConditionOption.
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        r"""Sets the condition of this MultiQueryConditionOption.

        **参数解释**: 组合条件类型。 **约束限制**: 不涉及。 **取值范围**: 仅限字符串：\"AND\"、\"OR\"。 **默认取值**: 不涉及。

        :param condition: The condition of this MultiQueryConditionOption.
        :type condition: str
        """
        self._condition = condition

    @property
    def is_fuzzy(self):
        r"""Gets the is_fuzzy of this MultiQueryConditionOption.

        **参数解释**: 多个过滤检索条件内容集合。 **约束限制**: 只支持为true进行模糊查询。 **取值范围**: - true：模糊查询。 - false：精确匹配。  **默认取值**: true 

        :return: The is_fuzzy of this MultiQueryConditionOption.
        :rtype: bool
        """
        return self._is_fuzzy

    @is_fuzzy.setter
    def is_fuzzy(self, is_fuzzy):
        r"""Sets the is_fuzzy of this MultiQueryConditionOption.

        **参数解释**: 多个过滤检索条件内容集合。 **约束限制**: 只支持为true进行模糊查询。 **取值范围**: - true：模糊查询。 - false：精确匹配。  **默认取值**: true 

        :param is_fuzzy: The is_fuzzy of this MultiQueryConditionOption.
        :type is_fuzzy: bool
        """
        self._is_fuzzy = is_fuzzy

    @property
    def values(self):
        r"""Gets the values of this MultiQueryConditionOption.

        **参数解释**: 多个过滤检索条件内容集合。由 1 至 5 个字符串组成的列表。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The values of this MultiQueryConditionOption.
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        r"""Sets the values of this MultiQueryConditionOption.

        **参数解释**: 多个过滤检索条件内容集合。由 1 至 5 个字符串组成的列表。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param values: The values of this MultiQueryConditionOption.
        :type values: list[str]
        """
        self._values = values

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
        if not isinstance(other, MultiQueryConditionOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
