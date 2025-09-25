# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSqlTraceRequest:

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
        'sql_id': 'str',
        'sql_exec_id': 'str',
        'transaction_id': 'str',
        'trace_id': 'str',
        'x_language': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'sql_id': 'sql_id',
        'sql_exec_id': 'sql_exec_id',
        'transaction_id': 'transaction_id',
        'trace_id': 'trace_id',
        'x_language': 'X-Language'
    }

    def __init__(self, instance_id=None, sql_id=None, sql_exec_id=None, transaction_id=None, trace_id=None, x_language=None):
        r"""ListSqlTraceRequest

        The model defined in huaweicloud sdk

        :param instance_id: **参数解释**: 实例ID，此参数是用户创建实例的唯一标识。 **约束限制**: 不涉及。 **取值范围**: 只能由英文字母、数字组成，且长度为36个字符。 **默认取值**: 不涉及。
        :type instance_id: str
        :param sql_id: **参数解释**: 归一化SQL ID，对应内核字段：unique_sql_id。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type sql_id: str
        :param sql_exec_id: **参数解释**: 唯一SQL ID，对应内核字段：debug_query_id。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type sql_exec_id: str
        :param transaction_id: **参数解释**: 事务ID，对应内核字段：transaction_id。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type transaction_id: str
        :param trace_id: **参数解释**: 链路ID，对应内核字段：trace_id。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type trace_id: str
        :param x_language: **参数解释**: 语言。 **约束限制**: 不涉及。 **取值范围**: - zh-cn  - en-us  **默认取值**: en-us
        :type x_language: str
        """
        
        

        self._instance_id = None
        self._sql_id = None
        self._sql_exec_id = None
        self._transaction_id = None
        self._trace_id = None
        self._x_language = None
        self.discriminator = None

        self.instance_id = instance_id
        if sql_id is not None:
            self.sql_id = sql_id
        if sql_exec_id is not None:
            self.sql_exec_id = sql_exec_id
        if transaction_id is not None:
            self.transaction_id = transaction_id
        if trace_id is not None:
            self.trace_id = trace_id
        if x_language is not None:
            self.x_language = x_language

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListSqlTraceRequest.

        **参数解释**: 实例ID，此参数是用户创建实例的唯一标识。 **约束限制**: 不涉及。 **取值范围**: 只能由英文字母、数字组成，且长度为36个字符。 **默认取值**: 不涉及。

        :return: The instance_id of this ListSqlTraceRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListSqlTraceRequest.

        **参数解释**: 实例ID，此参数是用户创建实例的唯一标识。 **约束限制**: 不涉及。 **取值范围**: 只能由英文字母、数字组成，且长度为36个字符。 **默认取值**: 不涉及。

        :param instance_id: The instance_id of this ListSqlTraceRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def sql_id(self):
        r"""Gets the sql_id of this ListSqlTraceRequest.

        **参数解释**: 归一化SQL ID，对应内核字段：unique_sql_id。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The sql_id of this ListSqlTraceRequest.
        :rtype: str
        """
        return self._sql_id

    @sql_id.setter
    def sql_id(self, sql_id):
        r"""Sets the sql_id of this ListSqlTraceRequest.

        **参数解释**: 归一化SQL ID，对应内核字段：unique_sql_id。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param sql_id: The sql_id of this ListSqlTraceRequest.
        :type sql_id: str
        """
        self._sql_id = sql_id

    @property
    def sql_exec_id(self):
        r"""Gets the sql_exec_id of this ListSqlTraceRequest.

        **参数解释**: 唯一SQL ID，对应内核字段：debug_query_id。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The sql_exec_id of this ListSqlTraceRequest.
        :rtype: str
        """
        return self._sql_exec_id

    @sql_exec_id.setter
    def sql_exec_id(self, sql_exec_id):
        r"""Sets the sql_exec_id of this ListSqlTraceRequest.

        **参数解释**: 唯一SQL ID，对应内核字段：debug_query_id。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param sql_exec_id: The sql_exec_id of this ListSqlTraceRequest.
        :type sql_exec_id: str
        """
        self._sql_exec_id = sql_exec_id

    @property
    def transaction_id(self):
        r"""Gets the transaction_id of this ListSqlTraceRequest.

        **参数解释**: 事务ID，对应内核字段：transaction_id。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The transaction_id of this ListSqlTraceRequest.
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        r"""Sets the transaction_id of this ListSqlTraceRequest.

        **参数解释**: 事务ID，对应内核字段：transaction_id。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param transaction_id: The transaction_id of this ListSqlTraceRequest.
        :type transaction_id: str
        """
        self._transaction_id = transaction_id

    @property
    def trace_id(self):
        r"""Gets the trace_id of this ListSqlTraceRequest.

        **参数解释**: 链路ID，对应内核字段：trace_id。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The trace_id of this ListSqlTraceRequest.
        :rtype: str
        """
        return self._trace_id

    @trace_id.setter
    def trace_id(self, trace_id):
        r"""Sets the trace_id of this ListSqlTraceRequest.

        **参数解释**: 链路ID，对应内核字段：trace_id。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param trace_id: The trace_id of this ListSqlTraceRequest.
        :type trace_id: str
        """
        self._trace_id = trace_id

    @property
    def x_language(self):
        r"""Gets the x_language of this ListSqlTraceRequest.

        **参数解释**: 语言。 **约束限制**: 不涉及。 **取值范围**: - zh-cn  - en-us  **默认取值**: en-us

        :return: The x_language of this ListSqlTraceRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListSqlTraceRequest.

        **参数解释**: 语言。 **约束限制**: 不涉及。 **取值范围**: - zh-cn  - en-us  **默认取值**: en-us

        :param x_language: The x_language of this ListSqlTraceRequest.
        :type x_language: str
        """
        self._x_language = x_language

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
        if not isinstance(other, ListSqlTraceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
