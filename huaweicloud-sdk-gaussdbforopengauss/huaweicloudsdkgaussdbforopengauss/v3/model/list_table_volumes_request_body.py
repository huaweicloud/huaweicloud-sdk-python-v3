# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTableVolumesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'database_name': 'str',
        'schema_names': 'list[str]',
        'table_name': 'str',
        'user_name': 'str',
        'sort_key': 'str',
        'sort_order': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'database_name': 'database_name',
        'schema_names': 'schema_names',
        'table_name': 'table_name',
        'user_name': 'user_name',
        'sort_key': 'sort_key',
        'sort_order': 'sort_order',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, database_name=None, schema_names=None, table_name=None, user_name=None, sort_key=None, sort_order=None, limit=None, offset=None):
        r"""ListTableVolumesRequestBody

        The model defined in huaweicloud sdk

        :param database_name: **参数解释**: 数据库名称。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。 
        :type database_name: str
        :param schema_names: **参数解释**: schema名称。 **约束限制**: 不涉及。 
        :type schema_names: list[str]
        :param table_name: **参数解释**: 表名称。。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。 
        :type table_name: str
        :param user_name: **参数解释**: 表所属用户名称。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。 
        :type user_name: str
        :param sort_key: **参数解释**: 排序字段。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。 
        :type sort_key: str
        :param sort_order: **参数解释**: 排序方法。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。 
        :type sort_order: str
        :param limit: **参数解释**: 查询记录数 **约束限制**: 必须为数字，不能为负数。 **取值范围**: 1 - 100 **默认取值**: 10 
        :type limit: int
        :param offset: **参数解释**: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询。 **约束限制**: 必须为数字，不能为负数。 **取值范围**: 0 - 10000 **默认取值**: 0 
        :type offset: int
        """
        
        

        self._database_name = None
        self._schema_names = None
        self._table_name = None
        self._user_name = None
        self._sort_key = None
        self._sort_order = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.database_name = database_name
        self.schema_names = schema_names
        if table_name is not None:
            self.table_name = table_name
        if user_name is not None:
            self.user_name = user_name
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_order is not None:
            self.sort_order = sort_order
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def database_name(self):
        r"""Gets the database_name of this ListTableVolumesRequestBody.

        **参数解释**: 数据库名称。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。 

        :return: The database_name of this ListTableVolumesRequestBody.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this ListTableVolumesRequestBody.

        **参数解释**: 数据库名称。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。 

        :param database_name: The database_name of this ListTableVolumesRequestBody.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def schema_names(self):
        r"""Gets the schema_names of this ListTableVolumesRequestBody.

        **参数解释**: schema名称。 **约束限制**: 不涉及。 

        :return: The schema_names of this ListTableVolumesRequestBody.
        :rtype: list[str]
        """
        return self._schema_names

    @schema_names.setter
    def schema_names(self, schema_names):
        r"""Sets the schema_names of this ListTableVolumesRequestBody.

        **参数解释**: schema名称。 **约束限制**: 不涉及。 

        :param schema_names: The schema_names of this ListTableVolumesRequestBody.
        :type schema_names: list[str]
        """
        self._schema_names = schema_names

    @property
    def table_name(self):
        r"""Gets the table_name of this ListTableVolumesRequestBody.

        **参数解释**: 表名称。。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。 

        :return: The table_name of this ListTableVolumesRequestBody.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this ListTableVolumesRequestBody.

        **参数解释**: 表名称。。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。 

        :param table_name: The table_name of this ListTableVolumesRequestBody.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def user_name(self):
        r"""Gets the user_name of this ListTableVolumesRequestBody.

        **参数解释**: 表所属用户名称。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。 

        :return: The user_name of this ListTableVolumesRequestBody.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ListTableVolumesRequestBody.

        **参数解释**: 表所属用户名称。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。 

        :param user_name: The user_name of this ListTableVolumesRequestBody.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListTableVolumesRequestBody.

        **参数解释**: 排序字段。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。 

        :return: The sort_key of this ListTableVolumesRequestBody.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListTableVolumesRequestBody.

        **参数解释**: 排序字段。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。 

        :param sort_key: The sort_key of this ListTableVolumesRequestBody.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_order(self):
        r"""Gets the sort_order of this ListTableVolumesRequestBody.

        **参数解释**: 排序方法。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。 

        :return: The sort_order of this ListTableVolumesRequestBody.
        :rtype: str
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        r"""Sets the sort_order of this ListTableVolumesRequestBody.

        **参数解释**: 排序方法。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。 

        :param sort_order: The sort_order of this ListTableVolumesRequestBody.
        :type sort_order: str
        """
        self._sort_order = sort_order

    @property
    def limit(self):
        r"""Gets the limit of this ListTableVolumesRequestBody.

        **参数解释**: 查询记录数 **约束限制**: 必须为数字，不能为负数。 **取值范围**: 1 - 100 **默认取值**: 10 

        :return: The limit of this ListTableVolumesRequestBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListTableVolumesRequestBody.

        **参数解释**: 查询记录数 **约束限制**: 必须为数字，不能为负数。 **取值范围**: 1 - 100 **默认取值**: 10 

        :param limit: The limit of this ListTableVolumesRequestBody.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListTableVolumesRequestBody.

        **参数解释**: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询。 **约束限制**: 必须为数字，不能为负数。 **取值范围**: 0 - 10000 **默认取值**: 0 

        :return: The offset of this ListTableVolumesRequestBody.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListTableVolumesRequestBody.

        **参数解释**: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询。 **约束限制**: 必须为数字，不能为负数。 **取值范围**: 0 - 10000 **默认取值**: 0 

        :param offset: The offset of this ListTableVolumesRequestBody.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListTableVolumesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
