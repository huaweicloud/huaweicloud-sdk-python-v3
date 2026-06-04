# coding: utf-8

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
        'table_format': 'str',
        'table_type': 'str',
        'filter': 'str',
        'limit': 'int',
        'marker': 'str',
        'reverse_page': 'bool',
        'deleted': 'bool',
        'include_fields': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'catalog_name': 'catalog_name',
        'database_name': 'database_name',
        'table_name_pattern': 'table_name_pattern',
        'table_format': 'table_format',
        'table_type': 'table_type',
        'filter': 'filter',
        'limit': 'limit',
        'marker': 'marker',
        'reverse_page': 'reverse_page',
        'deleted': 'deleted',
        'include_fields': 'include_fields'
    }

    def __init__(self, instance_id=None, catalog_name=None, database_name=None, table_name_pattern=None, table_format=None, table_type=None, filter=None, limit=None, marker=None, reverse_page=None, deleted=None, include_fields=None):
        r"""ListTablesRequest

        The model defined in huaweicloud sdk

        :param instance_id: LakeFormation实例ID。创建实例时自动生成。例如：2180518f-42b8-4947-b20b-adfc53981a25。
        :type instance_id: str
        :param catalog_name: catalog名称。只能包含字母、数字和下划线，且长度为1~256个字符。
        :type catalog_name: str
        :param database_name: 数据库名称。只能包含中文、字母、数字、下划线、中划线，且长度为1~128个字符。
        :type database_name: str
        :param table_name_pattern: 表名称通配符。只能包含中文、字母、数字和_|*.-特殊字符，且长度为1~256个字符。
        :type table_name_pattern: str
        :param table_format: 表格式。支持HIVE,ICEBERG,LANCE
        :type table_format: str
        :param table_type: 表类型：MANAGED_TABLE-内表、EXTERNAL_TABLE-外表、VIRTUAL_VIEW-视图、MATERIALIZED_VIEW-物化视图、DICTIONARY_TABLE字典表、LAKE_TABLE内表。
        :type table_type: str
        :param filter: 过滤条件字符串，可以按照属性查询表。 支持的属性查找包括： HIVE_FILTER_FIELD_OWNER HIVE_FILTER_FIELD_LAST_ACCESS HIVE_FILTER_FIELD_PARAMS
        :type filter: str
        :param limit: 查询返回条数。默认值为100。最小值为1，最大值为1000。当include_fields只包含name时，最大值可以为5000
        :type limit: int
        :param marker: 查询的起始记录ID。最小长度为0，最大长度为256。
        :type marker: str
        :param reverse_page: 是否倒序查询。
        :type reverse_page: bool
        :param deleted: 是否查询被删除元数据。
        :type deleted: bool
        :param include_fields: 包含字段，非必填，多个字段使用英文逗号分隔，不填时返回全部字段，当前暂只支持name
        :type include_fields: str
        """
        
        

        self._instance_id = None
        self._catalog_name = None
        self._database_name = None
        self._table_name_pattern = None
        self._table_format = None
        self._table_type = None
        self._filter = None
        self._limit = None
        self._marker = None
        self._reverse_page = None
        self._deleted = None
        self._include_fields = None
        self.discriminator = None

        self.instance_id = instance_id
        self.catalog_name = catalog_name
        self.database_name = database_name
        if table_name_pattern is not None:
            self.table_name_pattern = table_name_pattern
        if table_format is not None:
            self.table_format = table_format
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
        if deleted is not None:
            self.deleted = deleted
        if include_fields is not None:
            self.include_fields = include_fields

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListTablesRequest.

        LakeFormation实例ID。创建实例时自动生成。例如：2180518f-42b8-4947-b20b-adfc53981a25。

        :return: The instance_id of this ListTablesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListTablesRequest.

        LakeFormation实例ID。创建实例时自动生成。例如：2180518f-42b8-4947-b20b-adfc53981a25。

        :param instance_id: The instance_id of this ListTablesRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def catalog_name(self):
        r"""Gets the catalog_name of this ListTablesRequest.

        catalog名称。只能包含字母、数字和下划线，且长度为1~256个字符。

        :return: The catalog_name of this ListTablesRequest.
        :rtype: str
        """
        return self._catalog_name

    @catalog_name.setter
    def catalog_name(self, catalog_name):
        r"""Sets the catalog_name of this ListTablesRequest.

        catalog名称。只能包含字母、数字和下划线，且长度为1~256个字符。

        :param catalog_name: The catalog_name of this ListTablesRequest.
        :type catalog_name: str
        """
        self._catalog_name = catalog_name

    @property
    def database_name(self):
        r"""Gets the database_name of this ListTablesRequest.

        数据库名称。只能包含中文、字母、数字、下划线、中划线，且长度为1~128个字符。

        :return: The database_name of this ListTablesRequest.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this ListTablesRequest.

        数据库名称。只能包含中文、字母、数字、下划线、中划线，且长度为1~128个字符。

        :param database_name: The database_name of this ListTablesRequest.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def table_name_pattern(self):
        r"""Gets the table_name_pattern of this ListTablesRequest.

        表名称通配符。只能包含中文、字母、数字和_|*.-特殊字符，且长度为1~256个字符。

        :return: The table_name_pattern of this ListTablesRequest.
        :rtype: str
        """
        return self._table_name_pattern

    @table_name_pattern.setter
    def table_name_pattern(self, table_name_pattern):
        r"""Sets the table_name_pattern of this ListTablesRequest.

        表名称通配符。只能包含中文、字母、数字和_|*.-特殊字符，且长度为1~256个字符。

        :param table_name_pattern: The table_name_pattern of this ListTablesRequest.
        :type table_name_pattern: str
        """
        self._table_name_pattern = table_name_pattern

    @property
    def table_format(self):
        r"""Gets the table_format of this ListTablesRequest.

        表格式。支持HIVE,ICEBERG,LANCE

        :return: The table_format of this ListTablesRequest.
        :rtype: str
        """
        return self._table_format

    @table_format.setter
    def table_format(self, table_format):
        r"""Sets the table_format of this ListTablesRequest.

        表格式。支持HIVE,ICEBERG,LANCE

        :param table_format: The table_format of this ListTablesRequest.
        :type table_format: str
        """
        self._table_format = table_format

    @property
    def table_type(self):
        r"""Gets the table_type of this ListTablesRequest.

        表类型：MANAGED_TABLE-内表、EXTERNAL_TABLE-外表、VIRTUAL_VIEW-视图、MATERIALIZED_VIEW-物化视图、DICTIONARY_TABLE字典表、LAKE_TABLE内表。

        :return: The table_type of this ListTablesRequest.
        :rtype: str
        """
        return self._table_type

    @table_type.setter
    def table_type(self, table_type):
        r"""Sets the table_type of this ListTablesRequest.

        表类型：MANAGED_TABLE-内表、EXTERNAL_TABLE-外表、VIRTUAL_VIEW-视图、MATERIALIZED_VIEW-物化视图、DICTIONARY_TABLE字典表、LAKE_TABLE内表。

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

        查询返回条数。默认值为100。最小值为1，最大值为1000。当include_fields只包含name时，最大值可以为5000

        :return: The limit of this ListTablesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListTablesRequest.

        查询返回条数。默认值为100。最小值为1，最大值为1000。当include_fields只包含name时，最大值可以为5000

        :param limit: The limit of this ListTablesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListTablesRequest.

        查询的起始记录ID。最小长度为0，最大长度为256。

        :return: The marker of this ListTablesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListTablesRequest.

        查询的起始记录ID。最小长度为0，最大长度为256。

        :param marker: The marker of this ListTablesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def reverse_page(self):
        r"""Gets the reverse_page of this ListTablesRequest.

        是否倒序查询。

        :return: The reverse_page of this ListTablesRequest.
        :rtype: bool
        """
        return self._reverse_page

    @reverse_page.setter
    def reverse_page(self, reverse_page):
        r"""Sets the reverse_page of this ListTablesRequest.

        是否倒序查询。

        :param reverse_page: The reverse_page of this ListTablesRequest.
        :type reverse_page: bool
        """
        self._reverse_page = reverse_page

    @property
    def deleted(self):
        r"""Gets the deleted of this ListTablesRequest.

        是否查询被删除元数据。

        :return: The deleted of this ListTablesRequest.
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        r"""Sets the deleted of this ListTablesRequest.

        是否查询被删除元数据。

        :param deleted: The deleted of this ListTablesRequest.
        :type deleted: bool
        """
        self._deleted = deleted

    @property
    def include_fields(self):
        r"""Gets the include_fields of this ListTablesRequest.

        包含字段，非必填，多个字段使用英文逗号分隔，不填时返回全部字段，当前暂只支持name

        :return: The include_fields of this ListTablesRequest.
        :rtype: str
        """
        return self._include_fields

    @include_fields.setter
    def include_fields(self, include_fields):
        r"""Sets the include_fields of this ListTablesRequest.

        包含字段，非必填，多个字段使用英文逗号分隔，不填时返回全部字段，当前暂只支持name

        :param include_fields: The include_fields of this ListTablesRequest.
        :type include_fields: str
        """
        self._include_fields = include_fields

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
        if not isinstance(other, ListTablesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
