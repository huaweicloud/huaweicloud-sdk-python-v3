# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSlowSqlsRequestBody:

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
        'node_ids': 'list[str]',
        'start_time': 'int',
        'end_time': 'int',
        'sql_id': 'str',
        'threshold': 'int',
        'multi_queries': 'list[MultiQueryConditionOption]'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'node_ids': 'node_ids',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'sql_id': 'sql_id',
        'threshold': 'threshold',
        'multi_queries': 'multi_queries'
    }

    def __init__(self, instance_id=None, node_ids=None, start_time=None, end_time=None, sql_id=None, threshold=None, multi_queries=None):
        r"""ListSlowSqlsRequestBody

        The model defined in huaweicloud sdk

        :param instance_id: **参数解释**: 实例ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type instance_id: str
        :param node_ids: **参数解释**: 节点ID列表。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type node_ids: list[str]
        :param start_time: **参数解释** 起始日期。 **约束限制** 13位UNIX时间戳格式，单位是毫秒，时区是UTC。 **取值范围**: 不涉及。 **默认取值**: 不涉及。 
        :type start_time: int
        :param end_time: **参数解释** 结束日期。 **约束限制** 13位UNIX时间戳格式，单位是毫秒，时区是UTC。 **取值范围**: 不涉及。 **默认取值**: 不涉及。 
        :type end_time: int
        :param sql_id: **参数解释**: 慢SQL的sql_id，可按照sql_id过滤查询。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type sql_id: str
        :param threshold: **参数解释**: 阈值。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type threshold: int
        :param multi_queries: **参数解释**: 字符型组合过滤多条件查询列表。 **约束限制**: 不涉及。
        :type multi_queries: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.MultiQueryConditionOption`]
        """
        
        

        self._instance_id = None
        self._node_ids = None
        self._start_time = None
        self._end_time = None
        self._sql_id = None
        self._threshold = None
        self._multi_queries = None
        self.discriminator = None

        self.instance_id = instance_id
        self.node_ids = node_ids
        self.start_time = start_time
        self.end_time = end_time
        if sql_id is not None:
            self.sql_id = sql_id
        self.threshold = threshold
        if multi_queries is not None:
            self.multi_queries = multi_queries

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListSlowSqlsRequestBody.

        **参数解释**: 实例ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The instance_id of this ListSlowSqlsRequestBody.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListSlowSqlsRequestBody.

        **参数解释**: 实例ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param instance_id: The instance_id of this ListSlowSqlsRequestBody.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def node_ids(self):
        r"""Gets the node_ids of this ListSlowSqlsRequestBody.

        **参数解释**: 节点ID列表。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The node_ids of this ListSlowSqlsRequestBody.
        :rtype: list[str]
        """
        return self._node_ids

    @node_ids.setter
    def node_ids(self, node_ids):
        r"""Sets the node_ids of this ListSlowSqlsRequestBody.

        **参数解释**: 节点ID列表。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param node_ids: The node_ids of this ListSlowSqlsRequestBody.
        :type node_ids: list[str]
        """
        self._node_ids = node_ids

    @property
    def start_time(self):
        r"""Gets the start_time of this ListSlowSqlsRequestBody.

        **参数解释** 起始日期。 **约束限制** 13位UNIX时间戳格式，单位是毫秒，时区是UTC。 **取值范围**: 不涉及。 **默认取值**: 不涉及。 

        :return: The start_time of this ListSlowSqlsRequestBody.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListSlowSqlsRequestBody.

        **参数解释** 起始日期。 **约束限制** 13位UNIX时间戳格式，单位是毫秒，时区是UTC。 **取值范围**: 不涉及。 **默认取值**: 不涉及。 

        :param start_time: The start_time of this ListSlowSqlsRequestBody.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListSlowSqlsRequestBody.

        **参数解释** 结束日期。 **约束限制** 13位UNIX时间戳格式，单位是毫秒，时区是UTC。 **取值范围**: 不涉及。 **默认取值**: 不涉及。 

        :return: The end_time of this ListSlowSqlsRequestBody.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListSlowSqlsRequestBody.

        **参数解释** 结束日期。 **约束限制** 13位UNIX时间戳格式，单位是毫秒，时区是UTC。 **取值范围**: 不涉及。 **默认取值**: 不涉及。 

        :param end_time: The end_time of this ListSlowSqlsRequestBody.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def sql_id(self):
        r"""Gets the sql_id of this ListSlowSqlsRequestBody.

        **参数解释**: 慢SQL的sql_id，可按照sql_id过滤查询。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The sql_id of this ListSlowSqlsRequestBody.
        :rtype: str
        """
        return self._sql_id

    @sql_id.setter
    def sql_id(self, sql_id):
        r"""Sets the sql_id of this ListSlowSqlsRequestBody.

        **参数解释**: 慢SQL的sql_id，可按照sql_id过滤查询。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param sql_id: The sql_id of this ListSlowSqlsRequestBody.
        :type sql_id: str
        """
        self._sql_id = sql_id

    @property
    def threshold(self):
        r"""Gets the threshold of this ListSlowSqlsRequestBody.

        **参数解释**: 阈值。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The threshold of this ListSlowSqlsRequestBody.
        :rtype: int
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        r"""Sets the threshold of this ListSlowSqlsRequestBody.

        **参数解释**: 阈值。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param threshold: The threshold of this ListSlowSqlsRequestBody.
        :type threshold: int
        """
        self._threshold = threshold

    @property
    def multi_queries(self):
        r"""Gets the multi_queries of this ListSlowSqlsRequestBody.

        **参数解释**: 字符型组合过滤多条件查询列表。 **约束限制**: 不涉及。

        :return: The multi_queries of this ListSlowSqlsRequestBody.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.MultiQueryConditionOption`]
        """
        return self._multi_queries

    @multi_queries.setter
    def multi_queries(self, multi_queries):
        r"""Sets the multi_queries of this ListSlowSqlsRequestBody.

        **参数解释**: 字符型组合过滤多条件查询列表。 **约束限制**: 不涉及。

        :param multi_queries: The multi_queries of this ListSlowSqlsRequestBody.
        :type multi_queries: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.MultiQueryConditionOption`]
        """
        self._multi_queries = multi_queries

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
        if not isinstance(other, ListSlowSqlsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
