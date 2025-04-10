# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTablesRequest:

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
        'catalog_name': 'str',
        'database_name': 'str',
        'table_name_pattern': 'str',
        'table_type': 'str',
        'filter': 'str',
        'limit': 'int',
        'marker': 'str',
        'reverse_page': 'bool'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'catalog_name': 'catalog_name',
        'database_name': 'database_name',
        'table_name_pattern': 'table_name_pattern',
        'table_type': 'table_type',
        'filter': 'filter',
        'limit': 'limit',
        'marker': 'marker',
        'reverse_page': 'reverse_page'
    }

    def __init__(self, instance_id=None, catalog_name=None, database_name=None, table_name_pattern=None, table_type=None, filter=None, limit=None, marker=None, reverse_page=None):
        r"""ListTablesRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param catalog_name: catalog名字
        :type catalog_name: str
        :param database_name: 数据库名字
        :type database_name: str
        :param table_name_pattern: 表名字通配符
        :type table_name_pattern: str
        :param table_type: table_type
        :type table_type: str
        :param filter: 过滤条件字符串，可以按照属性查询表。 支持的属性查找包括： HIVE_FILTER_FIELD_OWNER HIVE_FILTER_FIELD_LAST_ACCESS HIVE_FILTER_FIELD_PARAMS
        :type filter: str
        :param limit: 返回的条目数量
        :type limit: int
        :param marker: 查询的起始记录ID
        :type marker: str
        :param reverse_page: 是否查询上一页
        :type reverse_page: bool
        """
        
        

        self._instance_id = None
        self._catalog_name = None
        self._database_name = None
        self._table_name_pattern = None
        self._table_type = None
        self._filter = None
        self._limit = None
        self._marker = None
        self._reverse_page = None
        self.discriminator = None

        self.instance_id = instance_id
        self.catalog_name = catalog_name
        self.database_name = database_name
        if table_name_pattern is not None:
            self.table_name_pattern = table_name_pattern
        if table_type is not None:
            self.table_type = table_type
        if filter is not None:
            self.filter = filter
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if reverse_page is not None:
            self.reverse_page = reverse_page

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListTablesRequest.

        实例ID

        :return: The instance_id of this ListTablesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListTablesRequest.

        实例ID

        :param instance_id: The instance_id of this ListTablesRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def catalog_name(self):
        r"""Gets the catalog_name of this ListTablesRequest.

        catalog名字

        :return: The catalog_name of this ListTablesRequest.
        :rtype: str
        """
        return self._catalog_name

    @catalog_name.setter
    def catalog_name(self, catalog_name):
        r"""Sets the catalog_name of this ListTablesRequest.

        catalog名字

        :param catalog_name: The catalog_name of this ListTablesRequest.
        :type catalog_name: str
        """
        self._catalog_name = catalog_name

    @property
    def database_name(self):
        r"""Gets the database_name of this ListTablesRequest.

        数据库名字

        :return: The database_name of this ListTablesRequest.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this ListTablesRequest.

        数据库名字

        :param database_name: The database_name of this ListTablesRequest.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def table_name_pattern(self):
        r"""Gets the table_name_pattern of this ListTablesRequest.

        表名字通配符

        :return: The table_name_pattern of this ListTablesRequest.
        :rtype: str
        """
        return self._table_name_pattern

    @table_name_pattern.setter
    def table_name_pattern(self, table_name_pattern):
        r"""Sets the table_name_pattern of this ListTablesRequest.

        表名字通配符

        :param table_name_pattern: The table_name_pattern of this ListTablesRequest.
        :type table_name_pattern: str
        """
        self._table_name_pattern = table_name_pattern

    @property
    def table_type(self):
        r"""Gets the table_type of this ListTablesRequest.

        table_type

        :return: The table_type of this ListTablesRequest.
        :rtype: str
        """
        return self._table_type

    @table_type.setter
    def table_type(self, table_type):
        r"""Sets the table_type of this ListTablesRequest.

        table_type

        :param table_type: The table_type of this ListTablesRequest.
        :type table_type: str
        """
        self._table_type = table_type

    @property
    def filter(self):
        r"""Gets the filter of this ListTablesRequest.

        过滤条件字符串，可以按照属性查询表。 支持的属性查找包括： HIVE_FILTER_FIELD_OWNER HIVE_FILTER_FIELD_LAST_ACCESS HIVE_FILTER_FIELD_PARAMS

        :return: The filter of this ListTablesRequest.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        r"""Sets the filter of this ListTablesRequest.

        过滤条件字符串，可以按照属性查询表。 支持的属性查找包括： HIVE_FILTER_FIELD_OWNER HIVE_FILTER_FIELD_LAST_ACCESS HIVE_FILTER_FIELD_PARAMS

        :param filter: The filter of this ListTablesRequest.
        :type filter: str
        """
        self._filter = filter

    @property
    def limit(self):
        r"""Gets the limit of this ListTablesRequest.

        返回的条目数量

        :return: The limit of this ListTablesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListTablesRequest.

        返回的条目数量

        :param limit: The limit of this ListTablesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListTablesRequest.

        查询的起始记录ID

        :return: The marker of this ListTablesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListTablesRequest.

        查询的起始记录ID

        :param marker: The marker of this ListTablesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def reverse_page(self):
        r"""Gets the reverse_page of this ListTablesRequest.

        是否查询上一页

        :return: The reverse_page of this ListTablesRequest.
        :rtype: bool
        """
        return self._reverse_page

    @reverse_page.setter
    def reverse_page(self, reverse_page):
        r"""Sets the reverse_page of this ListTablesRequest.

        是否查询上一页

        :param reverse_page: The reverse_page of this ListTablesRequest.
        :type reverse_page: bool
        """
        self._reverse_page = reverse_page

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
        if not isinstance(other, ListTablesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
