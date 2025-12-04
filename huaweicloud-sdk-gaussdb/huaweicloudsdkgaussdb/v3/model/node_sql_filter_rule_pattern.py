# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeSqlFilterRulePattern:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pattern': 'str',
        'max_concurrency': 'int',
        'expire_at': 'int'
    }

    attribute_map = {
        'pattern': 'pattern',
        'max_concurrency': 'max_concurrency',
        'expire_at': 'expire_at'
    }

    def __init__(self, pattern=None, max_concurrency=None, expire_at=None):
        r"""NodeSqlFilterRulePattern

        The model defined in huaweicloud sdk

        :param pattern: SQL限流规则，由一个或多个关键字（最多为128个关键字）组成，关键字之间通过\&quot;~\&quot;分隔符分开，如select~from~t1。规则中不能包含‘\\’、中英文逗号、‘~~’，不能以‘~’结尾。
        :type pattern: str
        :param max_concurrency: 最大并发数。取值范围：非负整数。
        :type max_concurrency: int
        :param expire_at: **参数解释**：  SQL限流失效时间，标准秒级时间戳，永久生效SQL限流规则该字段为null。  **约束限制**：  不涉及。  **取值范围**：  0 - 9223372036854775807。  **默认取值**：  不涉及。
        :type expire_at: int
        """
        
        

        self._pattern = None
        self._max_concurrency = None
        self._expire_at = None
        self.discriminator = None

        self.pattern = pattern
        self.max_concurrency = max_concurrency
        self.expire_at = expire_at

    @property
    def pattern(self):
        r"""Gets the pattern of this NodeSqlFilterRulePattern.

        SQL限流规则，由一个或多个关键字（最多为128个关键字）组成，关键字之间通过\"~\"分隔符分开，如select~from~t1。规则中不能包含‘\\’、中英文逗号、‘~~’，不能以‘~’结尾。

        :return: The pattern of this NodeSqlFilterRulePattern.
        :rtype: str
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        r"""Sets the pattern of this NodeSqlFilterRulePattern.

        SQL限流规则，由一个或多个关键字（最多为128个关键字）组成，关键字之间通过\"~\"分隔符分开，如select~from~t1。规则中不能包含‘\\’、中英文逗号、‘~~’，不能以‘~’结尾。

        :param pattern: The pattern of this NodeSqlFilterRulePattern.
        :type pattern: str
        """
        self._pattern = pattern

    @property
    def max_concurrency(self):
        r"""Gets the max_concurrency of this NodeSqlFilterRulePattern.

        最大并发数。取值范围：非负整数。

        :return: The max_concurrency of this NodeSqlFilterRulePattern.
        :rtype: int
        """
        return self._max_concurrency

    @max_concurrency.setter
    def max_concurrency(self, max_concurrency):
        r"""Sets the max_concurrency of this NodeSqlFilterRulePattern.

        最大并发数。取值范围：非负整数。

        :param max_concurrency: The max_concurrency of this NodeSqlFilterRulePattern.
        :type max_concurrency: int
        """
        self._max_concurrency = max_concurrency

    @property
    def expire_at(self):
        r"""Gets the expire_at of this NodeSqlFilterRulePattern.

        **参数解释**：  SQL限流失效时间，标准秒级时间戳，永久生效SQL限流规则该字段为null。  **约束限制**：  不涉及。  **取值范围**：  0 - 9223372036854775807。  **默认取值**：  不涉及。

        :return: The expire_at of this NodeSqlFilterRulePattern.
        :rtype: int
        """
        return self._expire_at

    @expire_at.setter
    def expire_at(self, expire_at):
        r"""Sets the expire_at of this NodeSqlFilterRulePattern.

        **参数解释**：  SQL限流失效时间，标准秒级时间戳，永久生效SQL限流规则该字段为null。  **约束限制**：  不涉及。  **取值范围**：  0 - 9223372036854775807。  **默认取值**：  不涉及。

        :param expire_at: The expire_at of this NodeSqlFilterRulePattern.
        :type expire_at: int
        """
        self._expire_at = expire_at

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
        if not isinstance(other, NodeSqlFilterRulePattern):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
