# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataFilterObjectResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'batch_id': 'int',
        'id': 'str',
        'parent_id': 'str',
        'object_name': 'str',
        'object_alias_name': 'str',
        'object_type': 'str',
        'db_name': 'str',
        'schema_name': 'str',
        'table_name': 'str',
        'is_data_filter': 'str',
        'data_filter_type': 'str',
        'filter_condition': 'str',
        'is_synchronized': 'bool'
    }

    attribute_map = {
        'batch_id': 'batch_id',
        'id': 'id',
        'parent_id': 'parent_id',
        'object_name': 'object_name',
        'object_alias_name': 'object_alias_name',
        'object_type': 'object_type',
        'db_name': 'db_name',
        'schema_name': 'schema_name',
        'table_name': 'table_name',
        'is_data_filter': 'is_data_filter',
        'data_filter_type': 'data_filter_type',
        'filter_condition': 'filter_condition',
        'is_synchronized': 'is_synchronized'
    }

    def __init__(self, batch_id=None, id=None, parent_id=None, object_name=None, object_alias_name=None, object_type=None, db_name=None, schema_name=None, table_name=None, is_data_filter=None, data_filter_type=None, filter_condition=None, is_synchronized=None):
        r"""DataFilterObjectResp

        The model defined in huaweicloud sdk

        :param batch_id: 数据过滤对象信息批次ID，与父级DataFilterRuleResp的batch_id关联，用于追溯对象归属的批次
        :type batch_id: int
        :param id: 数据过滤对象的唯一标识符，由对象层级结构（库名、表名、对象类型等）组合生成
        :type id: str
        :param parent_id: 父级过滤对象的标识符，用于表示对象之间的层级归属关系（如列归属于表、表归属于库）。
        :type parent_id: str
        :param object_name: 数据过滤对象的名称，按object_type不同可为库名、表名或列名。
        :type object_name: str
        :param object_alias_name: 数据过滤对象的映射名称（别名），在目标端数据库对象名与源端不一致时使用。
        :type object_alias_name: str
        :param object_type: 数据过滤对象的层级类型，标识当前过滤规则粒度级别。
        :type object_type: str
        :param db_name: 数据过滤对象所属的数据库名称。
        :type db_name: str
        :param schema_name: 数据过滤对象所属的schema名。
        :type schema_name: str
        :param table_name: 数据过滤对象所属的表名。
        :type table_name: str
        :param is_data_filter: 标记该对象是否启用数据过滤。
        :type is_data_filter: str
        :param data_filter_type: 数据过滤的类型，标识使用的过滤策略。
        :type data_filter_type: str
        :param filter_condition: 数据过滤条件
        :type filter_condition: str
        :param is_synchronized: 数据过滤条件是否已同步
        :type is_synchronized: bool
        """
        
        

        self._batch_id = None
        self._id = None
        self._parent_id = None
        self._object_name = None
        self._object_alias_name = None
        self._object_type = None
        self._db_name = None
        self._schema_name = None
        self._table_name = None
        self._is_data_filter = None
        self._data_filter_type = None
        self._filter_condition = None
        self._is_synchronized = None
        self.discriminator = None

        if batch_id is not None:
            self.batch_id = batch_id
        if id is not None:
            self.id = id
        if parent_id is not None:
            self.parent_id = parent_id
        if object_name is not None:
            self.object_name = object_name
        if object_alias_name is not None:
            self.object_alias_name = object_alias_name
        if object_type is not None:
            self.object_type = object_type
        if db_name is not None:
            self.db_name = db_name
        if schema_name is not None:
            self.schema_name = schema_name
        if table_name is not None:
            self.table_name = table_name
        if is_data_filter is not None:
            self.is_data_filter = is_data_filter
        if data_filter_type is not None:
            self.data_filter_type = data_filter_type
        if filter_condition is not None:
            self.filter_condition = filter_condition
        if is_synchronized is not None:
            self.is_synchronized = is_synchronized

    @property
    def batch_id(self):
        r"""Gets the batch_id of this DataFilterObjectResp.

        数据过滤对象信息批次ID，与父级DataFilterRuleResp的batch_id关联，用于追溯对象归属的批次

        :return: The batch_id of this DataFilterObjectResp.
        :rtype: int
        """
        return self._batch_id

    @batch_id.setter
    def batch_id(self, batch_id):
        r"""Sets the batch_id of this DataFilterObjectResp.

        数据过滤对象信息批次ID，与父级DataFilterRuleResp的batch_id关联，用于追溯对象归属的批次

        :param batch_id: The batch_id of this DataFilterObjectResp.
        :type batch_id: int
        """
        self._batch_id = batch_id

    @property
    def id(self):
        r"""Gets the id of this DataFilterObjectResp.

        数据过滤对象的唯一标识符，由对象层级结构（库名、表名、对象类型等）组合生成

        :return: The id of this DataFilterObjectResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DataFilterObjectResp.

        数据过滤对象的唯一标识符，由对象层级结构（库名、表名、对象类型等）组合生成

        :param id: The id of this DataFilterObjectResp.
        :type id: str
        """
        self._id = id

    @property
    def parent_id(self):
        r"""Gets the parent_id of this DataFilterObjectResp.

        父级过滤对象的标识符，用于表示对象之间的层级归属关系（如列归属于表、表归属于库）。

        :return: The parent_id of this DataFilterObjectResp.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this DataFilterObjectResp.

        父级过滤对象的标识符，用于表示对象之间的层级归属关系（如列归属于表、表归属于库）。

        :param parent_id: The parent_id of this DataFilterObjectResp.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def object_name(self):
        r"""Gets the object_name of this DataFilterObjectResp.

        数据过滤对象的名称，按object_type不同可为库名、表名或列名。

        :return: The object_name of this DataFilterObjectResp.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        r"""Sets the object_name of this DataFilterObjectResp.

        数据过滤对象的名称，按object_type不同可为库名、表名或列名。

        :param object_name: The object_name of this DataFilterObjectResp.
        :type object_name: str
        """
        self._object_name = object_name

    @property
    def object_alias_name(self):
        r"""Gets the object_alias_name of this DataFilterObjectResp.

        数据过滤对象的映射名称（别名），在目标端数据库对象名与源端不一致时使用。

        :return: The object_alias_name of this DataFilterObjectResp.
        :rtype: str
        """
        return self._object_alias_name

    @object_alias_name.setter
    def object_alias_name(self, object_alias_name):
        r"""Sets the object_alias_name of this DataFilterObjectResp.

        数据过滤对象的映射名称（别名），在目标端数据库对象名与源端不一致时使用。

        :param object_alias_name: The object_alias_name of this DataFilterObjectResp.
        :type object_alias_name: str
        """
        self._object_alias_name = object_alias_name

    @property
    def object_type(self):
        r"""Gets the object_type of this DataFilterObjectResp.

        数据过滤对象的层级类型，标识当前过滤规则粒度级别。

        :return: The object_type of this DataFilterObjectResp.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        r"""Sets the object_type of this DataFilterObjectResp.

        数据过滤对象的层级类型，标识当前过滤规则粒度级别。

        :param object_type: The object_type of this DataFilterObjectResp.
        :type object_type: str
        """
        self._object_type = object_type

    @property
    def db_name(self):
        r"""Gets the db_name of this DataFilterObjectResp.

        数据过滤对象所属的数据库名称。

        :return: The db_name of this DataFilterObjectResp.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this DataFilterObjectResp.

        数据过滤对象所属的数据库名称。

        :param db_name: The db_name of this DataFilterObjectResp.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def schema_name(self):
        r"""Gets the schema_name of this DataFilterObjectResp.

        数据过滤对象所属的schema名。

        :return: The schema_name of this DataFilterObjectResp.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        r"""Sets the schema_name of this DataFilterObjectResp.

        数据过滤对象所属的schema名。

        :param schema_name: The schema_name of this DataFilterObjectResp.
        :type schema_name: str
        """
        self._schema_name = schema_name

    @property
    def table_name(self):
        r"""Gets the table_name of this DataFilterObjectResp.

        数据过滤对象所属的表名。

        :return: The table_name of this DataFilterObjectResp.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this DataFilterObjectResp.

        数据过滤对象所属的表名。

        :param table_name: The table_name of this DataFilterObjectResp.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def is_data_filter(self):
        r"""Gets the is_data_filter of this DataFilterObjectResp.

        标记该对象是否启用数据过滤。

        :return: The is_data_filter of this DataFilterObjectResp.
        :rtype: str
        """
        return self._is_data_filter

    @is_data_filter.setter
    def is_data_filter(self, is_data_filter):
        r"""Sets the is_data_filter of this DataFilterObjectResp.

        标记该对象是否启用数据过滤。

        :param is_data_filter: The is_data_filter of this DataFilterObjectResp.
        :type is_data_filter: str
        """
        self._is_data_filter = is_data_filter

    @property
    def data_filter_type(self):
        r"""Gets the data_filter_type of this DataFilterObjectResp.

        数据过滤的类型，标识使用的过滤策略。

        :return: The data_filter_type of this DataFilterObjectResp.
        :rtype: str
        """
        return self._data_filter_type

    @data_filter_type.setter
    def data_filter_type(self, data_filter_type):
        r"""Sets the data_filter_type of this DataFilterObjectResp.

        数据过滤的类型，标识使用的过滤策略。

        :param data_filter_type: The data_filter_type of this DataFilterObjectResp.
        :type data_filter_type: str
        """
        self._data_filter_type = data_filter_type

    @property
    def filter_condition(self):
        r"""Gets the filter_condition of this DataFilterObjectResp.

        数据过滤条件

        :return: The filter_condition of this DataFilterObjectResp.
        :rtype: str
        """
        return self._filter_condition

    @filter_condition.setter
    def filter_condition(self, filter_condition):
        r"""Sets the filter_condition of this DataFilterObjectResp.

        数据过滤条件

        :param filter_condition: The filter_condition of this DataFilterObjectResp.
        :type filter_condition: str
        """
        self._filter_condition = filter_condition

    @property
    def is_synchronized(self):
        r"""Gets the is_synchronized of this DataFilterObjectResp.

        数据过滤条件是否已同步

        :return: The is_synchronized of this DataFilterObjectResp.
        :rtype: bool
        """
        return self._is_synchronized

    @is_synchronized.setter
    def is_synchronized(self, is_synchronized):
        r"""Sets the is_synchronized of this DataFilterObjectResp.

        数据过滤条件是否已同步

        :param is_synchronized: The is_synchronized of this DataFilterObjectResp.
        :type is_synchronized: bool
        """
        self._is_synchronized = is_synchronized

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
        if not isinstance(other, DataFilterObjectResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
