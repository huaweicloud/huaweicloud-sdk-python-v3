# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SqlFilterRulePattern:

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
        'cur_concurrency': 'int',
        'cur_reject': 'int',
        'create_at': 'int',
        'expire_at': 'int'
    }

    attribute_map = {
        'pattern': 'pattern',
        'max_concurrency': 'max_concurrency',
        'cur_concurrency': 'cur_concurrency',
        'cur_reject': 'cur_reject',
        'create_at': 'create_at',
        'expire_at': 'expire_at'
    }

    def __init__(self, pattern=None, max_concurrency=None, cur_concurrency=None, cur_reject=None, create_at=None, expire_at=None):
        r"""SqlFilterRulePattern

        The model defined in huaweicloud sdk

        :param pattern: **参数解释**：  SQL限流规则。  **取值范围**：  由一个或多个关键字（最多为128个关键字）组成，关键字之间通过\&quot;~\&quot;分隔符分开，如select~from~t1。规则中不能包含‘\\’、中英文逗号、‘~~’，不能以‘~’结尾。
        :type pattern: str
        :param max_concurrency: **参数解释**：  最大并发数。  **取值范围**：  不涉及。
        :type max_concurrency: int
        :param cur_concurrency: **参数解释**：  当前并发数。  **取值范围**：  0 - 4294967296。
        :type cur_concurrency: int
        :param cur_reject: **参数解释**：  当前拦截次数。  **取值范围**：  0 - 4294967296。
        :type cur_reject: int
        :param create_at: **参数解释**：  SQL限流规则创建时间。  **取值范围**：  0 - 9223372036854775807。
        :type create_at: int
        :param expire_at: **参数解释**：  SQL限流规则失效时间。  **取值范围**：  0 - 9223372036854775807。
        :type expire_at: int
        """
        
        

        self._pattern = None
        self._max_concurrency = None
        self._cur_concurrency = None
        self._cur_reject = None
        self._create_at = None
        self._expire_at = None
        self.discriminator = None

        self.pattern = pattern
        self.max_concurrency = max_concurrency
        if cur_concurrency is not None:
            self.cur_concurrency = cur_concurrency
        if cur_reject is not None:
            self.cur_reject = cur_reject
        if create_at is not None:
            self.create_at = create_at
        if expire_at is not None:
            self.expire_at = expire_at

    @property
    def pattern(self):
        r"""Gets the pattern of this SqlFilterRulePattern.

        **参数解释**：  SQL限流规则。  **取值范围**：  由一个或多个关键字（最多为128个关键字）组成，关键字之间通过\"~\"分隔符分开，如select~from~t1。规则中不能包含‘\\’、中英文逗号、‘~~’，不能以‘~’结尾。

        :return: The pattern of this SqlFilterRulePattern.
        :rtype: str
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        r"""Sets the pattern of this SqlFilterRulePattern.

        **参数解释**：  SQL限流规则。  **取值范围**：  由一个或多个关键字（最多为128个关键字）组成，关键字之间通过\"~\"分隔符分开，如select~from~t1。规则中不能包含‘\\’、中英文逗号、‘~~’，不能以‘~’结尾。

        :param pattern: The pattern of this SqlFilterRulePattern.
        :type pattern: str
        """
        self._pattern = pattern

    @property
    def max_concurrency(self):
        r"""Gets the max_concurrency of this SqlFilterRulePattern.

        **参数解释**：  最大并发数。  **取值范围**：  不涉及。

        :return: The max_concurrency of this SqlFilterRulePattern.
        :rtype: int
        """
        return self._max_concurrency

    @max_concurrency.setter
    def max_concurrency(self, max_concurrency):
        r"""Sets the max_concurrency of this SqlFilterRulePattern.

        **参数解释**：  最大并发数。  **取值范围**：  不涉及。

        :param max_concurrency: The max_concurrency of this SqlFilterRulePattern.
        :type max_concurrency: int
        """
        self._max_concurrency = max_concurrency

    @property
    def cur_concurrency(self):
        r"""Gets the cur_concurrency of this SqlFilterRulePattern.

        **参数解释**：  当前并发数。  **取值范围**：  0 - 4294967296。

        :return: The cur_concurrency of this SqlFilterRulePattern.
        :rtype: int
        """
        return self._cur_concurrency

    @cur_concurrency.setter
    def cur_concurrency(self, cur_concurrency):
        r"""Sets the cur_concurrency of this SqlFilterRulePattern.

        **参数解释**：  当前并发数。  **取值范围**：  0 - 4294967296。

        :param cur_concurrency: The cur_concurrency of this SqlFilterRulePattern.
        :type cur_concurrency: int
        """
        self._cur_concurrency = cur_concurrency

    @property
    def cur_reject(self):
        r"""Gets the cur_reject of this SqlFilterRulePattern.

        **参数解释**：  当前拦截次数。  **取值范围**：  0 - 4294967296。

        :return: The cur_reject of this SqlFilterRulePattern.
        :rtype: int
        """
        return self._cur_reject

    @cur_reject.setter
    def cur_reject(self, cur_reject):
        r"""Sets the cur_reject of this SqlFilterRulePattern.

        **参数解释**：  当前拦截次数。  **取值范围**：  0 - 4294967296。

        :param cur_reject: The cur_reject of this SqlFilterRulePattern.
        :type cur_reject: int
        """
        self._cur_reject = cur_reject

    @property
    def create_at(self):
        r"""Gets the create_at of this SqlFilterRulePattern.

        **参数解释**：  SQL限流规则创建时间。  **取值范围**：  0 - 9223372036854775807。

        :return: The create_at of this SqlFilterRulePattern.
        :rtype: int
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this SqlFilterRulePattern.

        **参数解释**：  SQL限流规则创建时间。  **取值范围**：  0 - 9223372036854775807。

        :param create_at: The create_at of this SqlFilterRulePattern.
        :type create_at: int
        """
        self._create_at = create_at

    @property
    def expire_at(self):
        r"""Gets the expire_at of this SqlFilterRulePattern.

        **参数解释**：  SQL限流规则失效时间。  **取值范围**：  0 - 9223372036854775807。

        :return: The expire_at of this SqlFilterRulePattern.
        :rtype: int
        """
        return self._expire_at

    @expire_at.setter
    def expire_at(self, expire_at):
        r"""Sets the expire_at of this SqlFilterRulePattern.

        **参数解释**：  SQL限流规则失效时间。  **取值范围**：  0 - 9223372036854775807。

        :param expire_at: The expire_at of this SqlFilterRulePattern.
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
        if not isinstance(other, SqlFilterRulePattern):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
