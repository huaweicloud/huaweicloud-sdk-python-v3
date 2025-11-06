# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SessionTopSqlStatisticInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_name': 'str',
        'unique_sql_id': 'str',
        'query': 'str',
        'count': 'int'
    }

    attribute_map = {
        'node_name': 'node_name',
        'unique_sql_id': 'unique_sql_id',
        'query': 'query',
        'count': 'count'
    }

    def __init__(self, node_name=None, unique_sql_id=None, query=None, count=None):
        r"""SessionTopSqlStatisticInfo

        The model defined in huaweicloud sdk

        :param node_name: **参数解释**: 节点名称。 **取值范围**: 不涉及。 
        :type node_name: str
        :param unique_sql_id: **参数解释**: 归一化SQL ID。 **取值范围**: 不涉及。 
        :type unique_sql_id: str
        :param query: **参数解释**: 查询语句。 **取值范围**: 不涉及。 
        :type query: str
        :param count: **参数解释**: SQL执行数量。 **取值范围**: 大于等于0。 
        :type count: int
        """
        
        

        self._node_name = None
        self._unique_sql_id = None
        self._query = None
        self._count = None
        self.discriminator = None

        if node_name is not None:
            self.node_name = node_name
        if unique_sql_id is not None:
            self.unique_sql_id = unique_sql_id
        if query is not None:
            self.query = query
        if count is not None:
            self.count = count

    @property
    def node_name(self):
        r"""Gets the node_name of this SessionTopSqlStatisticInfo.

        **参数解释**: 节点名称。 **取值范围**: 不涉及。 

        :return: The node_name of this SessionTopSqlStatisticInfo.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        r"""Sets the node_name of this SessionTopSqlStatisticInfo.

        **参数解释**: 节点名称。 **取值范围**: 不涉及。 

        :param node_name: The node_name of this SessionTopSqlStatisticInfo.
        :type node_name: str
        """
        self._node_name = node_name

    @property
    def unique_sql_id(self):
        r"""Gets the unique_sql_id of this SessionTopSqlStatisticInfo.

        **参数解释**: 归一化SQL ID。 **取值范围**: 不涉及。 

        :return: The unique_sql_id of this SessionTopSqlStatisticInfo.
        :rtype: str
        """
        return self._unique_sql_id

    @unique_sql_id.setter
    def unique_sql_id(self, unique_sql_id):
        r"""Sets the unique_sql_id of this SessionTopSqlStatisticInfo.

        **参数解释**: 归一化SQL ID。 **取值范围**: 不涉及。 

        :param unique_sql_id: The unique_sql_id of this SessionTopSqlStatisticInfo.
        :type unique_sql_id: str
        """
        self._unique_sql_id = unique_sql_id

    @property
    def query(self):
        r"""Gets the query of this SessionTopSqlStatisticInfo.

        **参数解释**: 查询语句。 **取值范围**: 不涉及。 

        :return: The query of this SessionTopSqlStatisticInfo.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        r"""Sets the query of this SessionTopSqlStatisticInfo.

        **参数解释**: 查询语句。 **取值范围**: 不涉及。 

        :param query: The query of this SessionTopSqlStatisticInfo.
        :type query: str
        """
        self._query = query

    @property
    def count(self):
        r"""Gets the count of this SessionTopSqlStatisticInfo.

        **参数解释**: SQL执行数量。 **取值范围**: 大于等于0。 

        :return: The count of this SessionTopSqlStatisticInfo.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this SessionTopSqlStatisticInfo.

        **参数解释**: SQL执行数量。 **取值范围**: 大于等于0。 

        :param count: The count of this SessionTopSqlStatisticInfo.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, SessionTopSqlStatisticInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
