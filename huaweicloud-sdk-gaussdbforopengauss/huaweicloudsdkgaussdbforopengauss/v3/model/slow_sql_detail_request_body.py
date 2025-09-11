# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SlowSqlDetailRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_time': 'int',
        'end_time': 'int',
        'instance_id': 'str',
        'multi_queries': 'list[MultiQueryConditionOption]',
        'sql_id': 'str',
        'node_ids': 'list[str]'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'instance_id': 'instance_id',
        'multi_queries': 'multi_queries',
        'sql_id': 'sql_id',
        'node_ids': 'node_ids'
    }

    def __init__(self, start_time=None, end_time=None, instance_id=None, multi_queries=None, sql_id=None, node_ids=None):
        r"""SlowSqlDetailRequestBody

        The model defined in huaweicloud sdk

        :param start_time: **参数解释**: 起始日期。 **约束限制**: 格式:13位UNIX时间戳格式，单位是毫秒，时区是UTC。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type start_time: int
        :param end_time: **参数解释**: 结束日期。 **约束限制**: 格式:13位UNIX时间戳格式，单位是毫秒，时区是UTC。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type end_time: int
        :param instance_id: **参数解释**: 实例ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type instance_id: str
        :param multi_queries: **参数解释**: 字符型组合过滤多条件查询列表。 **约束限制**: 不涉及。
        :type multi_queries: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.MultiQueryConditionOption`]
        :param sql_id: **参数解释**: 慢SQL的SQL ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type sql_id: str
        :param node_ids: **参数解释**: 节点ID数组。 **约束限制**: 不涉及。
        :type node_ids: list[str]
        """
        
        

        self._start_time = None
        self._end_time = None
        self._instance_id = None
        self._multi_queries = None
        self._sql_id = None
        self._node_ids = None
        self.discriminator = None

        self.start_time = start_time
        self.end_time = end_time
        self.instance_id = instance_id
        if multi_queries is not None:
            self.multi_queries = multi_queries
        self.sql_id = sql_id
        self.node_ids = node_ids

    @property
    def start_time(self):
        r"""Gets the start_time of this SlowSqlDetailRequestBody.

        **参数解释**: 起始日期。 **约束限制**: 格式:13位UNIX时间戳格式，单位是毫秒，时区是UTC。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The start_time of this SlowSqlDetailRequestBody.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this SlowSqlDetailRequestBody.

        **参数解释**: 起始日期。 **约束限制**: 格式:13位UNIX时间戳格式，单位是毫秒，时区是UTC。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param start_time: The start_time of this SlowSqlDetailRequestBody.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this SlowSqlDetailRequestBody.

        **参数解释**: 结束日期。 **约束限制**: 格式:13位UNIX时间戳格式，单位是毫秒，时区是UTC。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The end_time of this SlowSqlDetailRequestBody.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this SlowSqlDetailRequestBody.

        **参数解释**: 结束日期。 **约束限制**: 格式:13位UNIX时间戳格式，单位是毫秒，时区是UTC。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param end_time: The end_time of this SlowSqlDetailRequestBody.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def instance_id(self):
        r"""Gets the instance_id of this SlowSqlDetailRequestBody.

        **参数解释**: 实例ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The instance_id of this SlowSqlDetailRequestBody.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this SlowSqlDetailRequestBody.

        **参数解释**: 实例ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param instance_id: The instance_id of this SlowSqlDetailRequestBody.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def multi_queries(self):
        r"""Gets the multi_queries of this SlowSqlDetailRequestBody.

        **参数解释**: 字符型组合过滤多条件查询列表。 **约束限制**: 不涉及。

        :return: The multi_queries of this SlowSqlDetailRequestBody.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.MultiQueryConditionOption`]
        """
        return self._multi_queries

    @multi_queries.setter
    def multi_queries(self, multi_queries):
        r"""Sets the multi_queries of this SlowSqlDetailRequestBody.

        **参数解释**: 字符型组合过滤多条件查询列表。 **约束限制**: 不涉及。

        :param multi_queries: The multi_queries of this SlowSqlDetailRequestBody.
        :type multi_queries: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.MultiQueryConditionOption`]
        """
        self._multi_queries = multi_queries

    @property
    def sql_id(self):
        r"""Gets the sql_id of this SlowSqlDetailRequestBody.

        **参数解释**: 慢SQL的SQL ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The sql_id of this SlowSqlDetailRequestBody.
        :rtype: str
        """
        return self._sql_id

    @sql_id.setter
    def sql_id(self, sql_id):
        r"""Sets the sql_id of this SlowSqlDetailRequestBody.

        **参数解释**: 慢SQL的SQL ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param sql_id: The sql_id of this SlowSqlDetailRequestBody.
        :type sql_id: str
        """
        self._sql_id = sql_id

    @property
    def node_ids(self):
        r"""Gets the node_ids of this SlowSqlDetailRequestBody.

        **参数解释**: 节点ID数组。 **约束限制**: 不涉及。

        :return: The node_ids of this SlowSqlDetailRequestBody.
        :rtype: list[str]
        """
        return self._node_ids

    @node_ids.setter
    def node_ids(self, node_ids):
        r"""Sets the node_ids of this SlowSqlDetailRequestBody.

        **参数解释**: 节点ID数组。 **约束限制**: 不涉及。

        :param node_ids: The node_ids of this SlowSqlDetailRequestBody.
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
        if not isinstance(other, SlowSqlDetailRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
