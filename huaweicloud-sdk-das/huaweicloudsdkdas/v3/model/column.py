# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Column:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'auto_increment': 'bool',
        'data_type': 'str',
        'db_name': 'str',
        'label': 'str',
        'name': 'str',
        'real_name': 'str',
        'size': 'int',
        'table_name': 'str',
        'schema_name': 'str',
        'readonly': 'bool',
        'is_binary': 'bool',
        'int_data_type': 'int'
    }

    attribute_map = {
        'auto_increment': 'auto_increment',
        'data_type': 'data_type',
        'db_name': 'db_name',
        'label': 'label',
        'name': 'name',
        'real_name': 'real_name',
        'size': 'size',
        'table_name': 'table_name',
        'schema_name': 'schema_name',
        'readonly': 'readonly',
        'is_binary': 'is_binary',
        'int_data_type': 'int_data_type'
    }

    def __init__(self, auto_increment=None, data_type=None, db_name=None, label=None, name=None, real_name=None, size=None, table_name=None, schema_name=None, readonly=None, is_binary=None, int_data_type=None):
        r"""Column

        The model defined in huaweicloud sdk

        :param auto_increment: 是否自增
        :type auto_increment: bool
        :param data_type: 数据类型
        :type data_type: str
        :param db_name: 数据库名称
        :type db_name: str
        :param label: 标签
        :type label: str
        :param name: 名称
        :type name: str
        :param real_name: 实际名称
        :type real_name: str
        :param size: 尺寸大小
        :type size: int
        :param table_name: 表名
        :type table_name: str
        :param schema_name: schema名称
        :type schema_name: str
        :param readonly: 是否只读
        :type readonly: bool
        :param is_binary: 是否二进制
        :type is_binary: bool
        :param int_data_type: 数据类型
        :type int_data_type: int
        """
        
        

        self._auto_increment = None
        self._data_type = None
        self._db_name = None
        self._label = None
        self._name = None
        self._real_name = None
        self._size = None
        self._table_name = None
        self._schema_name = None
        self._readonly = None
        self._is_binary = None
        self._int_data_type = None
        self.discriminator = None

        if auto_increment is not None:
            self.auto_increment = auto_increment
        if data_type is not None:
            self.data_type = data_type
        if db_name is not None:
            self.db_name = db_name
        if label is not None:
            self.label = label
        if name is not None:
            self.name = name
        if real_name is not None:
            self.real_name = real_name
        if size is not None:
            self.size = size
        if table_name is not None:
            self.table_name = table_name
        if schema_name is not None:
            self.schema_name = schema_name
        if readonly is not None:
            self.readonly = readonly
        if is_binary is not None:
            self.is_binary = is_binary
        if int_data_type is not None:
            self.int_data_type = int_data_type

    @property
    def auto_increment(self):
        r"""Gets the auto_increment of this Column.

        是否自增

        :return: The auto_increment of this Column.
        :rtype: bool
        """
        return self._auto_increment

    @auto_increment.setter
    def auto_increment(self, auto_increment):
        r"""Sets the auto_increment of this Column.

        是否自增

        :param auto_increment: The auto_increment of this Column.
        :type auto_increment: bool
        """
        self._auto_increment = auto_increment

    @property
    def data_type(self):
        r"""Gets the data_type of this Column.

        数据类型

        :return: The data_type of this Column.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        r"""Sets the data_type of this Column.

        数据类型

        :param data_type: The data_type of this Column.
        :type data_type: str
        """
        self._data_type = data_type

    @property
    def db_name(self):
        r"""Gets the db_name of this Column.

        数据库名称

        :return: The db_name of this Column.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this Column.

        数据库名称

        :param db_name: The db_name of this Column.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def label(self):
        r"""Gets the label of this Column.

        标签

        :return: The label of this Column.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        r"""Sets the label of this Column.

        标签

        :param label: The label of this Column.
        :type label: str
        """
        self._label = label

    @property
    def name(self):
        r"""Gets the name of this Column.

        名称

        :return: The name of this Column.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Column.

        名称

        :param name: The name of this Column.
        :type name: str
        """
        self._name = name

    @property
    def real_name(self):
        r"""Gets the real_name of this Column.

        实际名称

        :return: The real_name of this Column.
        :rtype: str
        """
        return self._real_name

    @real_name.setter
    def real_name(self, real_name):
        r"""Sets the real_name of this Column.

        实际名称

        :param real_name: The real_name of this Column.
        :type real_name: str
        """
        self._real_name = real_name

    @property
    def size(self):
        r"""Gets the size of this Column.

        尺寸大小

        :return: The size of this Column.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this Column.

        尺寸大小

        :param size: The size of this Column.
        :type size: int
        """
        self._size = size

    @property
    def table_name(self):
        r"""Gets the table_name of this Column.

        表名

        :return: The table_name of this Column.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this Column.

        表名

        :param table_name: The table_name of this Column.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def schema_name(self):
        r"""Gets the schema_name of this Column.

        schema名称

        :return: The schema_name of this Column.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        r"""Sets the schema_name of this Column.

        schema名称

        :param schema_name: The schema_name of this Column.
        :type schema_name: str
        """
        self._schema_name = schema_name

    @property
    def readonly(self):
        r"""Gets the readonly of this Column.

        是否只读

        :return: The readonly of this Column.
        :rtype: bool
        """
        return self._readonly

    @readonly.setter
    def readonly(self, readonly):
        r"""Sets the readonly of this Column.

        是否只读

        :param readonly: The readonly of this Column.
        :type readonly: bool
        """
        self._readonly = readonly

    @property
    def is_binary(self):
        r"""Gets the is_binary of this Column.

        是否二进制

        :return: The is_binary of this Column.
        :rtype: bool
        """
        return self._is_binary

    @is_binary.setter
    def is_binary(self, is_binary):
        r"""Sets the is_binary of this Column.

        是否二进制

        :param is_binary: The is_binary of this Column.
        :type is_binary: bool
        """
        self._is_binary = is_binary

    @property
    def int_data_type(self):
        r"""Gets the int_data_type of this Column.

        数据类型

        :return: The int_data_type of this Column.
        :rtype: int
        """
        return self._int_data_type

    @int_data_type.setter
    def int_data_type(self, int_data_type):
        r"""Sets the int_data_type of this Column.

        数据类型

        :param int_data_type: The int_data_type of this Column.
        :type int_data_type: int
        """
        self._int_data_type = int_data_type

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
        if not isinstance(other, Column):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
