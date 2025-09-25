# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSqlLimitTaskRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_scope': 'str',
        'limit_type': 'str',
        'limit_type_value': 'str',
        'task_name': 'str',
        'rule_name': 'str',
        'offset': 'int',
        'limit': 'int',
        'sql_id': 'str',
        'node_ids': 'list[str]'
    }

    attribute_map = {
        'task_scope': 'task_scope',
        'limit_type': 'limit_type',
        'limit_type_value': 'limit_type_value',
        'task_name': 'task_name',
        'rule_name': 'rule_name',
        'offset': 'offset',
        'limit': 'limit',
        'sql_id': 'sql_id',
        'node_ids': 'node_ids'
    }

    def __init__(self, task_scope=None, limit_type=None, limit_type_value=None, task_name=None, rule_name=None, offset=None, limit=None, sql_id=None, node_ids=None):
        r"""ListSqlLimitTaskRequestBody

        The model defined in huaweicloud sdk

        :param task_scope: **参数解释**: 限流任务范围。 **约束限制**: 不涉及。 **取值范围**: 目前支持SQL、SESSION。 **默认取值**: 不涉及。
        :type task_scope: str
        :param limit_type: **参数解释**: 限流类型。 **约束限制**: 不涉及。 **取值范围**: 支持SQL_ID、SQL_TYPE、SESSION_ACTIVE_MAX_COUNT类型。 **默认取值**: 不涉及。
        :type limit_type: str
        :param limit_type_value: **参数解释**: 限流类型值，支持模糊匹配。 **约束限制**: 不涉及。 **取值范围**: 长度为1~19字符，且只能包含大小写字母、数字和_。 **默认取值**: 不涉及。
        :type limit_type_value: str
        :param task_name: **参数解释**: 限流任务名，支持模糊匹配。 **约束限制**: 不涉及。 **取值范围**: 长度为1~100字符，只能包含大小写字母、数字、-、_和$。 **默认取值**: 不涉及。
        :type task_name: str
        :param rule_name: **参数解释**: 规则名。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type rule_name: str
        :param offset: **参数解释**: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询。 **约束限制**: 不涉及。 **取值范围**: 0 - 10000 **默认取值**: 0（偏移0条数据，表示从第一条数据开始查询）。
        :type offset: int
        :param limit: **参数解释**: 查询记录数。 **约束限制**: 不涉及。 **取值范围**: 不能为负数，最小值为1，最大值为100。 **默认取值**: 10
        :type limit: int
        :param sql_id: **参数解释**: 限流任务SQL_ID。 **约束限制**: 不涉及。 **取值范围**: 1 到 19 位的正整数（首位不为 0）。 **默认取值**: 不涉及。
        :type sql_id: str
        :param node_ids: **参数解释**: 限流任务NodeID列表。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type node_ids: list[str]
        """
        
        

        self._task_scope = None
        self._limit_type = None
        self._limit_type_value = None
        self._task_name = None
        self._rule_name = None
        self._offset = None
        self._limit = None
        self._sql_id = None
        self._node_ids = None
        self.discriminator = None

        if task_scope is not None:
            self.task_scope = task_scope
        if limit_type is not None:
            self.limit_type = limit_type
        if limit_type_value is not None:
            self.limit_type_value = limit_type_value
        if task_name is not None:
            self.task_name = task_name
        if rule_name is not None:
            self.rule_name = rule_name
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if sql_id is not None:
            self.sql_id = sql_id
        if node_ids is not None:
            self.node_ids = node_ids

    @property
    def task_scope(self):
        r"""Gets the task_scope of this ListSqlLimitTaskRequestBody.

        **参数解释**: 限流任务范围。 **约束限制**: 不涉及。 **取值范围**: 目前支持SQL、SESSION。 **默认取值**: 不涉及。

        :return: The task_scope of this ListSqlLimitTaskRequestBody.
        :rtype: str
        """
        return self._task_scope

    @task_scope.setter
    def task_scope(self, task_scope):
        r"""Sets the task_scope of this ListSqlLimitTaskRequestBody.

        **参数解释**: 限流任务范围。 **约束限制**: 不涉及。 **取值范围**: 目前支持SQL、SESSION。 **默认取值**: 不涉及。

        :param task_scope: The task_scope of this ListSqlLimitTaskRequestBody.
        :type task_scope: str
        """
        self._task_scope = task_scope

    @property
    def limit_type(self):
        r"""Gets the limit_type of this ListSqlLimitTaskRequestBody.

        **参数解释**: 限流类型。 **约束限制**: 不涉及。 **取值范围**: 支持SQL_ID、SQL_TYPE、SESSION_ACTIVE_MAX_COUNT类型。 **默认取值**: 不涉及。

        :return: The limit_type of this ListSqlLimitTaskRequestBody.
        :rtype: str
        """
        return self._limit_type

    @limit_type.setter
    def limit_type(self, limit_type):
        r"""Sets the limit_type of this ListSqlLimitTaskRequestBody.

        **参数解释**: 限流类型。 **约束限制**: 不涉及。 **取值范围**: 支持SQL_ID、SQL_TYPE、SESSION_ACTIVE_MAX_COUNT类型。 **默认取值**: 不涉及。

        :param limit_type: The limit_type of this ListSqlLimitTaskRequestBody.
        :type limit_type: str
        """
        self._limit_type = limit_type

    @property
    def limit_type_value(self):
        r"""Gets the limit_type_value of this ListSqlLimitTaskRequestBody.

        **参数解释**: 限流类型值，支持模糊匹配。 **约束限制**: 不涉及。 **取值范围**: 长度为1~19字符，且只能包含大小写字母、数字和_。 **默认取值**: 不涉及。

        :return: The limit_type_value of this ListSqlLimitTaskRequestBody.
        :rtype: str
        """
        return self._limit_type_value

    @limit_type_value.setter
    def limit_type_value(self, limit_type_value):
        r"""Sets the limit_type_value of this ListSqlLimitTaskRequestBody.

        **参数解释**: 限流类型值，支持模糊匹配。 **约束限制**: 不涉及。 **取值范围**: 长度为1~19字符，且只能包含大小写字母、数字和_。 **默认取值**: 不涉及。

        :param limit_type_value: The limit_type_value of this ListSqlLimitTaskRequestBody.
        :type limit_type_value: str
        """
        self._limit_type_value = limit_type_value

    @property
    def task_name(self):
        r"""Gets the task_name of this ListSqlLimitTaskRequestBody.

        **参数解释**: 限流任务名，支持模糊匹配。 **约束限制**: 不涉及。 **取值范围**: 长度为1~100字符，只能包含大小写字母、数字、-、_和$。 **默认取值**: 不涉及。

        :return: The task_name of this ListSqlLimitTaskRequestBody.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this ListSqlLimitTaskRequestBody.

        **参数解释**: 限流任务名，支持模糊匹配。 **约束限制**: 不涉及。 **取值范围**: 长度为1~100字符，只能包含大小写字母、数字、-、_和$。 **默认取值**: 不涉及。

        :param task_name: The task_name of this ListSqlLimitTaskRequestBody.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def rule_name(self):
        r"""Gets the rule_name of this ListSqlLimitTaskRequestBody.

        **参数解释**: 规则名。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The rule_name of this ListSqlLimitTaskRequestBody.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        r"""Sets the rule_name of this ListSqlLimitTaskRequestBody.

        **参数解释**: 规则名。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param rule_name: The rule_name of this ListSqlLimitTaskRequestBody.
        :type rule_name: str
        """
        self._rule_name = rule_name

    @property
    def offset(self):
        r"""Gets the offset of this ListSqlLimitTaskRequestBody.

        **参数解释**: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询。 **约束限制**: 不涉及。 **取值范围**: 0 - 10000 **默认取值**: 0（偏移0条数据，表示从第一条数据开始查询）。

        :return: The offset of this ListSqlLimitTaskRequestBody.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSqlLimitTaskRequestBody.

        **参数解释**: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询。 **约束限制**: 不涉及。 **取值范围**: 0 - 10000 **默认取值**: 0（偏移0条数据，表示从第一条数据开始查询）。

        :param offset: The offset of this ListSqlLimitTaskRequestBody.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListSqlLimitTaskRequestBody.

        **参数解释**: 查询记录数。 **约束限制**: 不涉及。 **取值范围**: 不能为负数，最小值为1，最大值为100。 **默认取值**: 10

        :return: The limit of this ListSqlLimitTaskRequestBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSqlLimitTaskRequestBody.

        **参数解释**: 查询记录数。 **约束限制**: 不涉及。 **取值范围**: 不能为负数，最小值为1，最大值为100。 **默认取值**: 10

        :param limit: The limit of this ListSqlLimitTaskRequestBody.
        :type limit: int
        """
        self._limit = limit

    @property
    def sql_id(self):
        r"""Gets the sql_id of this ListSqlLimitTaskRequestBody.

        **参数解释**: 限流任务SQL_ID。 **约束限制**: 不涉及。 **取值范围**: 1 到 19 位的正整数（首位不为 0）。 **默认取值**: 不涉及。

        :return: The sql_id of this ListSqlLimitTaskRequestBody.
        :rtype: str
        """
        return self._sql_id

    @sql_id.setter
    def sql_id(self, sql_id):
        r"""Sets the sql_id of this ListSqlLimitTaskRequestBody.

        **参数解释**: 限流任务SQL_ID。 **约束限制**: 不涉及。 **取值范围**: 1 到 19 位的正整数（首位不为 0）。 **默认取值**: 不涉及。

        :param sql_id: The sql_id of this ListSqlLimitTaskRequestBody.
        :type sql_id: str
        """
        self._sql_id = sql_id

    @property
    def node_ids(self):
        r"""Gets the node_ids of this ListSqlLimitTaskRequestBody.

        **参数解释**: 限流任务NodeID列表。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The node_ids of this ListSqlLimitTaskRequestBody.
        :rtype: list[str]
        """
        return self._node_ids

    @node_ids.setter
    def node_ids(self, node_ids):
        r"""Sets the node_ids of this ListSqlLimitTaskRequestBody.

        **参数解释**: 限流任务NodeID列表。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param node_ids: The node_ids of this ListSqlLimitTaskRequestBody.
        :type node_ids: list[str]
        """
        self._node_ids = node_ids

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
        if not isinstance(other, ListSqlLimitTaskRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
