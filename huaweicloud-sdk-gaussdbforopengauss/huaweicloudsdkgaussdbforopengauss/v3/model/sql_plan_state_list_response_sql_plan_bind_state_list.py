# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SqlPlanStateListResponseSqlPlanBindStateList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'outline': 'str',
        'cost': 'str',
        'status': 'str',
        'sql_hash': 'str',
        'plan_id': 'str'
    }

    attribute_map = {
        'outline': 'outline',
        'cost': 'cost',
        'status': 'status',
        'sql_hash': 'sql_hash',
        'plan_id': 'plan_id'
    }

    def __init__(self, outline=None, cost=None, status=None, sql_hash=None, plan_id=None):
        r"""SqlPlanStateListResponseSqlPlanBindStateList

        The model defined in huaweicloud sdk

        :param outline: **参数解释**: 当前计划的概览。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type outline: str
        :param cost: **参数解释**: SQL执行计划的开销。 **取值范围**: 不涉及。
        :type cost: str
        :param status: **参数解释**: 绑定状态。 **取值范围**: - bind：绑定。 - drop：解绑。
        :type status: str
        :param sql_hash: **参数解释**: SQL文本的哈希值。 **取值范围**: 不涉及。
        :type sql_hash: str
        :param plan_id: **参数解释**: SQL执行计划ID。 **取值范围**: 不涉及。
        :type plan_id: str
        """
        
        

        self._outline = None
        self._cost = None
        self._status = None
        self._sql_hash = None
        self._plan_id = None
        self.discriminator = None

        if outline is not None:
            self.outline = outline
        if cost is not None:
            self.cost = cost
        if status is not None:
            self.status = status
        if sql_hash is not None:
            self.sql_hash = sql_hash
        if plan_id is not None:
            self.plan_id = plan_id

    @property
    def outline(self):
        r"""Gets the outline of this SqlPlanStateListResponseSqlPlanBindStateList.

        **参数解释**: 当前计划的概览。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The outline of this SqlPlanStateListResponseSqlPlanBindStateList.
        :rtype: str
        """
        return self._outline

    @outline.setter
    def outline(self, outline):
        r"""Sets the outline of this SqlPlanStateListResponseSqlPlanBindStateList.

        **参数解释**: 当前计划的概览。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param outline: The outline of this SqlPlanStateListResponseSqlPlanBindStateList.
        :type outline: str
        """
        self._outline = outline

    @property
    def cost(self):
        r"""Gets the cost of this SqlPlanStateListResponseSqlPlanBindStateList.

        **参数解释**: SQL执行计划的开销。 **取值范围**: 不涉及。

        :return: The cost of this SqlPlanStateListResponseSqlPlanBindStateList.
        :rtype: str
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        r"""Sets the cost of this SqlPlanStateListResponseSqlPlanBindStateList.

        **参数解释**: SQL执行计划的开销。 **取值范围**: 不涉及。

        :param cost: The cost of this SqlPlanStateListResponseSqlPlanBindStateList.
        :type cost: str
        """
        self._cost = cost

    @property
    def status(self):
        r"""Gets the status of this SqlPlanStateListResponseSqlPlanBindStateList.

        **参数解释**: 绑定状态。 **取值范围**: - bind：绑定。 - drop：解绑。

        :return: The status of this SqlPlanStateListResponseSqlPlanBindStateList.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SqlPlanStateListResponseSqlPlanBindStateList.

        **参数解释**: 绑定状态。 **取值范围**: - bind：绑定。 - drop：解绑。

        :param status: The status of this SqlPlanStateListResponseSqlPlanBindStateList.
        :type status: str
        """
        self._status = status

    @property
    def sql_hash(self):
        r"""Gets the sql_hash of this SqlPlanStateListResponseSqlPlanBindStateList.

        **参数解释**: SQL文本的哈希值。 **取值范围**: 不涉及。

        :return: The sql_hash of this SqlPlanStateListResponseSqlPlanBindStateList.
        :rtype: str
        """
        return self._sql_hash

    @sql_hash.setter
    def sql_hash(self, sql_hash):
        r"""Sets the sql_hash of this SqlPlanStateListResponseSqlPlanBindStateList.

        **参数解释**: SQL文本的哈希值。 **取值范围**: 不涉及。

        :param sql_hash: The sql_hash of this SqlPlanStateListResponseSqlPlanBindStateList.
        :type sql_hash: str
        """
        self._sql_hash = sql_hash

    @property
    def plan_id(self):
        r"""Gets the plan_id of this SqlPlanStateListResponseSqlPlanBindStateList.

        **参数解释**: SQL执行计划ID。 **取值范围**: 不涉及。

        :return: The plan_id of this SqlPlanStateListResponseSqlPlanBindStateList.
        :rtype: str
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        r"""Sets the plan_id of this SqlPlanStateListResponseSqlPlanBindStateList.

        **参数解释**: SQL执行计划ID。 **取值范围**: 不涉及。

        :param plan_id: The plan_id of this SqlPlanStateListResponseSqlPlanBindStateList.
        :type plan_id: str
        """
        self._plan_id = plan_id

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
        if not isinstance(other, SqlPlanStateListResponseSqlPlanBindStateList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
