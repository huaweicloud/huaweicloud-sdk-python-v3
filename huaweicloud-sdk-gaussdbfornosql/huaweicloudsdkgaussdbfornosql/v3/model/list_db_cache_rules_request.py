# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDbCacheRulesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dbcache_mapping_id': 'str',
        'rule_id': 'str',
        'rule_name': 'str',
        'source_db_schema': 'str',
        'source_db_table': 'str',
        'offset': 'str',
        'limit': 'str'
    }

    attribute_map = {
        'dbcache_mapping_id': 'dbcache_mapping_id',
        'rule_id': 'rule_id',
        'rule_name': 'rule_name',
        'source_db_schema': 'source_db_schema',
        'source_db_table': 'source_db_table',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, dbcache_mapping_id=None, rule_id=None, rule_name=None, source_db_schema=None, source_db_table=None, offset=None, limit=None):
        r"""ListDbCacheRulesRequest

        The model defined in huaweicloud sdk

        :param dbcache_mapping_id: 内存加速映射ID。
        :type dbcache_mapping_id: str
        :param rule_id: 内存加速规则ID。
        :type rule_id: str
        :param rule_name: 内存加速规则名称。名称以“*”起始，表示按照“*”后面的值模糊匹配，否则，按照实际填写的名称精确匹配查询。
        :type rule_name: str
        :param source_db_schema: 源端数据库名。名称以“*”起始，表示按照“*”后面的值模糊匹配，否则，按照实际填写的名称精确匹配查询。
        :type source_db_schema: str
        :param source_db_table: 源端数据表名。名称以“*”起始，表示按照“*”后面的值模糊匹配，否则，按照实际填写的名称精确匹配查询。
        :type source_db_table: str
        :param offset: 索引位置，偏移量。 从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询）。 取值必须为数字，不能为负数。
        :type offset: str
        :param limit: 查询个数上限值。取值范围：1~100。不传该参数时，默认查询前100条信息。
        :type limit: str
        """
        
        

        self._dbcache_mapping_id = None
        self._rule_id = None
        self._rule_name = None
        self._source_db_schema = None
        self._source_db_table = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.dbcache_mapping_id = dbcache_mapping_id
        if rule_id is not None:
            self.rule_id = rule_id
        if rule_name is not None:
            self.rule_name = rule_name
        if source_db_schema is not None:
            self.source_db_schema = source_db_schema
        if source_db_table is not None:
            self.source_db_table = source_db_table
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def dbcache_mapping_id(self):
        r"""Gets the dbcache_mapping_id of this ListDbCacheRulesRequest.

        内存加速映射ID。

        :return: The dbcache_mapping_id of this ListDbCacheRulesRequest.
        :rtype: str
        """
        return self._dbcache_mapping_id

    @dbcache_mapping_id.setter
    def dbcache_mapping_id(self, dbcache_mapping_id):
        r"""Sets the dbcache_mapping_id of this ListDbCacheRulesRequest.

        内存加速映射ID。

        :param dbcache_mapping_id: The dbcache_mapping_id of this ListDbCacheRulesRequest.
        :type dbcache_mapping_id: str
        """
        self._dbcache_mapping_id = dbcache_mapping_id

    @property
    def rule_id(self):
        r"""Gets the rule_id of this ListDbCacheRulesRequest.

        内存加速规则ID。

        :return: The rule_id of this ListDbCacheRulesRequest.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        r"""Sets the rule_id of this ListDbCacheRulesRequest.

        内存加速规则ID。

        :param rule_id: The rule_id of this ListDbCacheRulesRequest.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def rule_name(self):
        r"""Gets the rule_name of this ListDbCacheRulesRequest.

        内存加速规则名称。名称以“*”起始，表示按照“*”后面的值模糊匹配，否则，按照实际填写的名称精确匹配查询。

        :return: The rule_name of this ListDbCacheRulesRequest.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        r"""Sets the rule_name of this ListDbCacheRulesRequest.

        内存加速规则名称。名称以“*”起始，表示按照“*”后面的值模糊匹配，否则，按照实际填写的名称精确匹配查询。

        :param rule_name: The rule_name of this ListDbCacheRulesRequest.
        :type rule_name: str
        """
        self._rule_name = rule_name

    @property
    def source_db_schema(self):
        r"""Gets the source_db_schema of this ListDbCacheRulesRequest.

        源端数据库名。名称以“*”起始，表示按照“*”后面的值模糊匹配，否则，按照实际填写的名称精确匹配查询。

        :return: The source_db_schema of this ListDbCacheRulesRequest.
        :rtype: str
        """
        return self._source_db_schema

    @source_db_schema.setter
    def source_db_schema(self, source_db_schema):
        r"""Sets the source_db_schema of this ListDbCacheRulesRequest.

        源端数据库名。名称以“*”起始，表示按照“*”后面的值模糊匹配，否则，按照实际填写的名称精确匹配查询。

        :param source_db_schema: The source_db_schema of this ListDbCacheRulesRequest.
        :type source_db_schema: str
        """
        self._source_db_schema = source_db_schema

    @property
    def source_db_table(self):
        r"""Gets the source_db_table of this ListDbCacheRulesRequest.

        源端数据表名。名称以“*”起始，表示按照“*”后面的值模糊匹配，否则，按照实际填写的名称精确匹配查询。

        :return: The source_db_table of this ListDbCacheRulesRequest.
        :rtype: str
        """
        return self._source_db_table

    @source_db_table.setter
    def source_db_table(self, source_db_table):
        r"""Sets the source_db_table of this ListDbCacheRulesRequest.

        源端数据表名。名称以“*”起始，表示按照“*”后面的值模糊匹配，否则，按照实际填写的名称精确匹配查询。

        :param source_db_table: The source_db_table of this ListDbCacheRulesRequest.
        :type source_db_table: str
        """
        self._source_db_table = source_db_table

    @property
    def offset(self):
        r"""Gets the offset of this ListDbCacheRulesRequest.

        索引位置，偏移量。 从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询）。 取值必须为数字，不能为负数。

        :return: The offset of this ListDbCacheRulesRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListDbCacheRulesRequest.

        索引位置，偏移量。 从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询）。 取值必须为数字，不能为负数。

        :param offset: The offset of this ListDbCacheRulesRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListDbCacheRulesRequest.

        查询个数上限值。取值范围：1~100。不传该参数时，默认查询前100条信息。

        :return: The limit of this ListDbCacheRulesRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListDbCacheRulesRequest.

        查询个数上限值。取值范围：1~100。不传该参数时，默认查询前100条信息。

        :param limit: The limit of this ListDbCacheRulesRequest.
        :type limit: str
        """
        self._limit = limit

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
        if not isinstance(other, ListDbCacheRulesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
