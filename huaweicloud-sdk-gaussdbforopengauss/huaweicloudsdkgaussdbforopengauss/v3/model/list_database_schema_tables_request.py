# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDatabaseSchemaTablesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'instance_id': 'str',
        'db_name': 'str',
        'schema_name': 'str',
        'table_name_keyword': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'instance_id': 'instance_id',
        'db_name': 'db_name',
        'schema_name': 'schema_name',
        'table_name_keyword': 'table_name_keyword',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, x_language=None, instance_id=None, db_name=None, schema_name=None, table_name_keyword=None, offset=None, limit=None):
        r"""ListDatabaseSchemaTablesRequest

        The model defined in huaweicloud sdk

        :param x_language: **参数解释**: 语言。 **约束限制**: 不涉及。 **取值范围**: - zh-cn  - en-us  **默认取值**: en-us
        :type x_language: str
        :param instance_id: **参数解释**: 实例ID，此参数是用户创建实例的唯一标识。 **约束限制**: 不涉及。 **取值范围**: 只能由英文字母、数字组成，且长度为36个字符。 **默认取值**: 不涉及。
        :type instance_id: str
        :param db_name: **参数解释**: 数据库名称。 **约束限制**: 不能使用模板库，且是已存在的数据库名称。 模板库包括postgres， template0，template1，templatea，template_pdb，templatem。 **取值范围**: 不涉及。 **默认取值**: 不涉及。 
        :type db_name: str
        :param schema_name: **参数解释**: SCHEMA名称。 **约束限制**: 不能使用public，information_schema，且schema名称必须存在。 **取值范围**: 不涉及。 **默认取值**: 不涉及。 
        :type schema_name: str
        :param table_name_keyword: **参数解释**: 表名关键字。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。 
        :type table_name_keyword: str
        :param offset: **参数解释**: 偏移量，表示从此偏移量开始查询。 **约束限制**: 不涉及。 **取值范围**: [0~2147483647) **默认取值**: 0 
        :type offset: int
        :param limit: **参数解释**: 每页显示的条目数量。 **约束限制**: 不涉及。 **取值范围**: [1, 200] **默认取值**: 10 
        :type limit: int
        """
        
        

        self._x_language = None
        self._instance_id = None
        self._db_name = None
        self._schema_name = None
        self._table_name_keyword = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.instance_id = instance_id
        self.db_name = db_name
        self.schema_name = schema_name
        if table_name_keyword is not None:
            self.table_name_keyword = table_name_keyword
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def x_language(self):
        r"""Gets the x_language of this ListDatabaseSchemaTablesRequest.

        **参数解释**: 语言。 **约束限制**: 不涉及。 **取值范围**: - zh-cn  - en-us  **默认取值**: en-us

        :return: The x_language of this ListDatabaseSchemaTablesRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListDatabaseSchemaTablesRequest.

        **参数解释**: 语言。 **约束限制**: 不涉及。 **取值范围**: - zh-cn  - en-us  **默认取值**: en-us

        :param x_language: The x_language of this ListDatabaseSchemaTablesRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListDatabaseSchemaTablesRequest.

        **参数解释**: 实例ID，此参数是用户创建实例的唯一标识。 **约束限制**: 不涉及。 **取值范围**: 只能由英文字母、数字组成，且长度为36个字符。 **默认取值**: 不涉及。

        :return: The instance_id of this ListDatabaseSchemaTablesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListDatabaseSchemaTablesRequest.

        **参数解释**: 实例ID，此参数是用户创建实例的唯一标识。 **约束限制**: 不涉及。 **取值范围**: 只能由英文字母、数字组成，且长度为36个字符。 **默认取值**: 不涉及。

        :param instance_id: The instance_id of this ListDatabaseSchemaTablesRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def db_name(self):
        r"""Gets the db_name of this ListDatabaseSchemaTablesRequest.

        **参数解释**: 数据库名称。 **约束限制**: 不能使用模板库，且是已存在的数据库名称。 模板库包括postgres， template0，template1，templatea，template_pdb，templatem。 **取值范围**: 不涉及。 **默认取值**: 不涉及。 

        :return: The db_name of this ListDatabaseSchemaTablesRequest.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this ListDatabaseSchemaTablesRequest.

        **参数解释**: 数据库名称。 **约束限制**: 不能使用模板库，且是已存在的数据库名称。 模板库包括postgres， template0，template1，templatea，template_pdb，templatem。 **取值范围**: 不涉及。 **默认取值**: 不涉及。 

        :param db_name: The db_name of this ListDatabaseSchemaTablesRequest.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def schema_name(self):
        r"""Gets the schema_name of this ListDatabaseSchemaTablesRequest.

        **参数解释**: SCHEMA名称。 **约束限制**: 不能使用public，information_schema，且schema名称必须存在。 **取值范围**: 不涉及。 **默认取值**: 不涉及。 

        :return: The schema_name of this ListDatabaseSchemaTablesRequest.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        r"""Sets the schema_name of this ListDatabaseSchemaTablesRequest.

        **参数解释**: SCHEMA名称。 **约束限制**: 不能使用public，information_schema，且schema名称必须存在。 **取值范围**: 不涉及。 **默认取值**: 不涉及。 

        :param schema_name: The schema_name of this ListDatabaseSchemaTablesRequest.
        :type schema_name: str
        """
        self._schema_name = schema_name

    @property
    def table_name_keyword(self):
        r"""Gets the table_name_keyword of this ListDatabaseSchemaTablesRequest.

        **参数解释**: 表名关键字。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。 

        :return: The table_name_keyword of this ListDatabaseSchemaTablesRequest.
        :rtype: str
        """
        return self._table_name_keyword

    @table_name_keyword.setter
    def table_name_keyword(self, table_name_keyword):
        r"""Sets the table_name_keyword of this ListDatabaseSchemaTablesRequest.

        **参数解释**: 表名关键字。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。 

        :param table_name_keyword: The table_name_keyword of this ListDatabaseSchemaTablesRequest.
        :type table_name_keyword: str
        """
        self._table_name_keyword = table_name_keyword

    @property
    def offset(self):
        r"""Gets the offset of this ListDatabaseSchemaTablesRequest.

        **参数解释**: 偏移量，表示从此偏移量开始查询。 **约束限制**: 不涉及。 **取值范围**: [0~2147483647) **默认取值**: 0 

        :return: The offset of this ListDatabaseSchemaTablesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListDatabaseSchemaTablesRequest.

        **参数解释**: 偏移量，表示从此偏移量开始查询。 **约束限制**: 不涉及。 **取值范围**: [0~2147483647) **默认取值**: 0 

        :param offset: The offset of this ListDatabaseSchemaTablesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListDatabaseSchemaTablesRequest.

        **参数解释**: 每页显示的条目数量。 **约束限制**: 不涉及。 **取值范围**: [1, 200] **默认取值**: 10 

        :return: The limit of this ListDatabaseSchemaTablesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListDatabaseSchemaTablesRequest.

        **参数解释**: 每页显示的条目数量。 **约束限制**: 不涉及。 **取值范围**: [1, 200] **默认取值**: 10 

        :param limit: The limit of this ListDatabaseSchemaTablesRequest.
        :type limit: int
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
        if not isinstance(other, ListDatabaseSchemaTablesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
