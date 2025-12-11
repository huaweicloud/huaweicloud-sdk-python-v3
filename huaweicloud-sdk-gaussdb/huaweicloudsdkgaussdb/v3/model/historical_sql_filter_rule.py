# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HistoricalSqlFilterRule:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'node_id': 'str',
        'pattern': 'str',
        'sql_type': 'str',
        'max_concurrency': 'int',
        'create_at': 'int',
        'expire_at': 'int',
        'delete_at': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'node_id': 'node_id',
        'pattern': 'pattern',
        'sql_type': 'sql_type',
        'max_concurrency': 'max_concurrency',
        'create_at': 'create_at',
        'expire_at': 'expire_at',
        'delete_at': 'delete_at'
    }

    def __init__(self, instance_id=None, node_id=None, pattern=None, sql_type=None, max_concurrency=None, create_at=None, expire_at=None, delete_at=None):
        r"""HistoricalSqlFilterRule

        The model defined in huaweicloud sdk

        :param instance_id: **参数解释**：  实例ID，此参数是实例的唯一标识。  **取值范围**：  只能由英文字母、数字组成，后缀为in07，长度为36个字符。  **默认取值**：  不涉及。
        :type instance_id: str
        :param node_id: **参数解释**：  节点ID。  **取值范围**：  与入参中的节点ID一致。  **默认取值**：  不涉及。
        :type node_id: str
        :param pattern: **参数解释**：  SQL限流规则。  **取值范围**：  由一个或多个关键字（最多为128个关键字）组成，关键字之间通过\&quot;~\&quot;分隔符分开，如select~from~t1。规则中不能包含‘\\’、中英文逗号、‘~~’，不能以‘~’结尾。  **默认取值**：  不涉及
        :type pattern: str
        :param sql_type: **参数解释**：  SQL限流类型。  **取值范围**：  - SELECT：查询语句。 - UPDATE：更新语句。 - DELETE：删除语句。 - INSERT：插入语句。  **默认取值**：  不涉及。
        :type sql_type: str
        :param max_concurrency: **参数解释**：  最大并发数。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type max_concurrency: int
        :param create_at: **参数解释**：  SQL限流规则创建时间。  **取值范围**：  0 - 9223372036854775807。  **默认取值**：  不涉及
        :type create_at: int
        :param expire_at: **参数解释**：  SQL限流规则失效时间。  **取值范围**：  0 - 9223372036854775807。  **默认取值**：  不涉及
        :type expire_at: int
        :param delete_at: **参数解释**：  SQL限流规则删除时间。  **取值范围**：  0 - 9223372036854775807。  **默认取值**：  不涉及
        :type delete_at: int
        """
        
        

        self._instance_id = None
        self._node_id = None
        self._pattern = None
        self._sql_type = None
        self._max_concurrency = None
        self._create_at = None
        self._expire_at = None
        self._delete_at = None
        self.discriminator = None

        self.instance_id = instance_id
        self.node_id = node_id
        self.pattern = pattern
        self.sql_type = sql_type
        self.max_concurrency = max_concurrency
        self.create_at = create_at
        self.expire_at = expire_at
        self.delete_at = delete_at

    @property
    def instance_id(self):
        r"""Gets the instance_id of this HistoricalSqlFilterRule.

        **参数解释**：  实例ID，此参数是实例的唯一标识。  **取值范围**：  只能由英文字母、数字组成，后缀为in07，长度为36个字符。  **默认取值**：  不涉及。

        :return: The instance_id of this HistoricalSqlFilterRule.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this HistoricalSqlFilterRule.

        **参数解释**：  实例ID，此参数是实例的唯一标识。  **取值范围**：  只能由英文字母、数字组成，后缀为in07，长度为36个字符。  **默认取值**：  不涉及。

        :param instance_id: The instance_id of this HistoricalSqlFilterRule.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def node_id(self):
        r"""Gets the node_id of this HistoricalSqlFilterRule.

        **参数解释**：  节点ID。  **取值范围**：  与入参中的节点ID一致。  **默认取值**：  不涉及。

        :return: The node_id of this HistoricalSqlFilterRule.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this HistoricalSqlFilterRule.

        **参数解释**：  节点ID。  **取值范围**：  与入参中的节点ID一致。  **默认取值**：  不涉及。

        :param node_id: The node_id of this HistoricalSqlFilterRule.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def pattern(self):
        r"""Gets the pattern of this HistoricalSqlFilterRule.

        **参数解释**：  SQL限流规则。  **取值范围**：  由一个或多个关键字（最多为128个关键字）组成，关键字之间通过\"~\"分隔符分开，如select~from~t1。规则中不能包含‘\\’、中英文逗号、‘~~’，不能以‘~’结尾。  **默认取值**：  不涉及

        :return: The pattern of this HistoricalSqlFilterRule.
        :rtype: str
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        r"""Sets the pattern of this HistoricalSqlFilterRule.

        **参数解释**：  SQL限流规则。  **取值范围**：  由一个或多个关键字（最多为128个关键字）组成，关键字之间通过\"~\"分隔符分开，如select~from~t1。规则中不能包含‘\\’、中英文逗号、‘~~’，不能以‘~’结尾。  **默认取值**：  不涉及

        :param pattern: The pattern of this HistoricalSqlFilterRule.
        :type pattern: str
        """
        self._pattern = pattern

    @property
    def sql_type(self):
        r"""Gets the sql_type of this HistoricalSqlFilterRule.

        **参数解释**：  SQL限流类型。  **取值范围**：  - SELECT：查询语句。 - UPDATE：更新语句。 - DELETE：删除语句。 - INSERT：插入语句。  **默认取值**：  不涉及。

        :return: The sql_type of this HistoricalSqlFilterRule.
        :rtype: str
        """
        return self._sql_type

    @sql_type.setter
    def sql_type(self, sql_type):
        r"""Sets the sql_type of this HistoricalSqlFilterRule.

        **参数解释**：  SQL限流类型。  **取值范围**：  - SELECT：查询语句。 - UPDATE：更新语句。 - DELETE：删除语句。 - INSERT：插入语句。  **默认取值**：  不涉及。

        :param sql_type: The sql_type of this HistoricalSqlFilterRule.
        :type sql_type: str
        """
        self._sql_type = sql_type

    @property
    def max_concurrency(self):
        r"""Gets the max_concurrency of this HistoricalSqlFilterRule.

        **参数解释**：  最大并发数。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The max_concurrency of this HistoricalSqlFilterRule.
        :rtype: int
        """
        return self._max_concurrency

    @max_concurrency.setter
    def max_concurrency(self, max_concurrency):
        r"""Sets the max_concurrency of this HistoricalSqlFilterRule.

        **参数解释**：  最大并发数。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param max_concurrency: The max_concurrency of this HistoricalSqlFilterRule.
        :type max_concurrency: int
        """
        self._max_concurrency = max_concurrency

    @property
    def create_at(self):
        r"""Gets the create_at of this HistoricalSqlFilterRule.

        **参数解释**：  SQL限流规则创建时间。  **取值范围**：  0 - 9223372036854775807。  **默认取值**：  不涉及

        :return: The create_at of this HistoricalSqlFilterRule.
        :rtype: int
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this HistoricalSqlFilterRule.

        **参数解释**：  SQL限流规则创建时间。  **取值范围**：  0 - 9223372036854775807。  **默认取值**：  不涉及

        :param create_at: The create_at of this HistoricalSqlFilterRule.
        :type create_at: int
        """
        self._create_at = create_at

    @property
    def expire_at(self):
        r"""Gets the expire_at of this HistoricalSqlFilterRule.

        **参数解释**：  SQL限流规则失效时间。  **取值范围**：  0 - 9223372036854775807。  **默认取值**：  不涉及

        :return: The expire_at of this HistoricalSqlFilterRule.
        :rtype: int
        """
        return self._expire_at

    @expire_at.setter
    def expire_at(self, expire_at):
        r"""Sets the expire_at of this HistoricalSqlFilterRule.

        **参数解释**：  SQL限流规则失效时间。  **取值范围**：  0 - 9223372036854775807。  **默认取值**：  不涉及

        :param expire_at: The expire_at of this HistoricalSqlFilterRule.
        :type expire_at: int
        """
        self._expire_at = expire_at

    @property
    def delete_at(self):
        r"""Gets the delete_at of this HistoricalSqlFilterRule.

        **参数解释**：  SQL限流规则删除时间。  **取值范围**：  0 - 9223372036854775807。  **默认取值**：  不涉及

        :return: The delete_at of this HistoricalSqlFilterRule.
        :rtype: int
        """
        return self._delete_at

    @delete_at.setter
    def delete_at(self, delete_at):
        r"""Sets the delete_at of this HistoricalSqlFilterRule.

        **参数解释**：  SQL限流规则删除时间。  **取值范围**：  0 - 9223372036854775807。  **默认取值**：  不涉及

        :param delete_at: The delete_at of this HistoricalSqlFilterRule.
        :type delete_at: int
        """
        self._delete_at = delete_at

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
        if not isinstance(other, HistoricalSqlFilterRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
