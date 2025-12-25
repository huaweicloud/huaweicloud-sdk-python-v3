# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SchemaColumns:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'array': 'bool',
        'column_data_type': 'str',
        'column_data_type_setting': 'str',
        'column_name': 'str',
        'column_sequence_number': 'int',
        'column_type': 'str',
        'column_type_setting': 'str',
        'depth': 'int',
        'nullable': 'bool',
        'own_name': 'str',
        'parent_name': 'str'
    }

    attribute_map = {
        'array': 'array',
        'column_data_type': 'column_data_type',
        'column_data_type_setting': 'column_data_type_setting',
        'column_name': 'column_name',
        'column_sequence_number': 'column_sequence_number',
        'column_type': 'column_type',
        'column_type_setting': 'column_type_setting',
        'depth': 'depth',
        'nullable': 'nullable',
        'own_name': 'own_name',
        'parent_name': 'parent_name'
    }

    def __init__(self, array=None, column_data_type=None, column_data_type_setting=None, column_name=None, column_sequence_number=None, column_type=None, column_type_setting=None, depth=None, nullable=None, own_name=None, parent_name=None):
        r"""SchemaColumns

        The model defined in huaweicloud sdk

        :param array: 是否为数组
        :type array: bool
        :param column_data_type: 列数据类型，例如 TIMESTAMP 或 INT
        :type column_data_type: str
        :param column_data_type_setting: 数据类型设置
        :type column_data_type_setting: str
        :param column_name: 列名称
        :type column_name: str
        :param column_sequence_number: 列顺序号
        :type column_sequence_number: int
        :param column_type: 列类型，例如 PHYSICAL
        :type column_type: str
        :param column_type_setting: 列类型设置
        :type column_type_setting: str
        :param depth: 深度
        :type depth: int
        :param nullable: 是否允许为空
        :type nullable: bool
        :param own_name: 自有名称
        :type own_name: str
        :param parent_name: 父名称
        :type parent_name: str
        """
        
        

        self._array = None
        self._column_data_type = None
        self._column_data_type_setting = None
        self._column_name = None
        self._column_sequence_number = None
        self._column_type = None
        self._column_type_setting = None
        self._depth = None
        self._nullable = None
        self._own_name = None
        self._parent_name = None
        self.discriminator = None

        if array is not None:
            self.array = array
        if column_data_type is not None:
            self.column_data_type = column_data_type
        if column_data_type_setting is not None:
            self.column_data_type_setting = column_data_type_setting
        if column_name is not None:
            self.column_name = column_name
        if column_sequence_number is not None:
            self.column_sequence_number = column_sequence_number
        if column_type is not None:
            self.column_type = column_type
        if column_type_setting is not None:
            self.column_type_setting = column_type_setting
        if depth is not None:
            self.depth = depth
        if nullable is not None:
            self.nullable = nullable
        if own_name is not None:
            self.own_name = own_name
        if parent_name is not None:
            self.parent_name = parent_name

    @property
    def array(self):
        r"""Gets the array of this SchemaColumns.

        是否为数组

        :return: The array of this SchemaColumns.
        :rtype: bool
        """
        return self._array

    @array.setter
    def array(self, array):
        r"""Sets the array of this SchemaColumns.

        是否为数组

        :param array: The array of this SchemaColumns.
        :type array: bool
        """
        self._array = array

    @property
    def column_data_type(self):
        r"""Gets the column_data_type of this SchemaColumns.

        列数据类型，例如 TIMESTAMP 或 INT

        :return: The column_data_type of this SchemaColumns.
        :rtype: str
        """
        return self._column_data_type

    @column_data_type.setter
    def column_data_type(self, column_data_type):
        r"""Sets the column_data_type of this SchemaColumns.

        列数据类型，例如 TIMESTAMP 或 INT

        :param column_data_type: The column_data_type of this SchemaColumns.
        :type column_data_type: str
        """
        self._column_data_type = column_data_type

    @property
    def column_data_type_setting(self):
        r"""Gets the column_data_type_setting of this SchemaColumns.

        数据类型设置

        :return: The column_data_type_setting of this SchemaColumns.
        :rtype: str
        """
        return self._column_data_type_setting

    @column_data_type_setting.setter
    def column_data_type_setting(self, column_data_type_setting):
        r"""Sets the column_data_type_setting of this SchemaColumns.

        数据类型设置

        :param column_data_type_setting: The column_data_type_setting of this SchemaColumns.
        :type column_data_type_setting: str
        """
        self._column_data_type_setting = column_data_type_setting

    @property
    def column_name(self):
        r"""Gets the column_name of this SchemaColumns.

        列名称

        :return: The column_name of this SchemaColumns.
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        r"""Sets the column_name of this SchemaColumns.

        列名称

        :param column_name: The column_name of this SchemaColumns.
        :type column_name: str
        """
        self._column_name = column_name

    @property
    def column_sequence_number(self):
        r"""Gets the column_sequence_number of this SchemaColumns.

        列顺序号

        :return: The column_sequence_number of this SchemaColumns.
        :rtype: int
        """
        return self._column_sequence_number

    @column_sequence_number.setter
    def column_sequence_number(self, column_sequence_number):
        r"""Sets the column_sequence_number of this SchemaColumns.

        列顺序号

        :param column_sequence_number: The column_sequence_number of this SchemaColumns.
        :type column_sequence_number: int
        """
        self._column_sequence_number = column_sequence_number

    @property
    def column_type(self):
        r"""Gets the column_type of this SchemaColumns.

        列类型，例如 PHYSICAL

        :return: The column_type of this SchemaColumns.
        :rtype: str
        """
        return self._column_type

    @column_type.setter
    def column_type(self, column_type):
        r"""Sets the column_type of this SchemaColumns.

        列类型，例如 PHYSICAL

        :param column_type: The column_type of this SchemaColumns.
        :type column_type: str
        """
        self._column_type = column_type

    @property
    def column_type_setting(self):
        r"""Gets the column_type_setting of this SchemaColumns.

        列类型设置

        :return: The column_type_setting of this SchemaColumns.
        :rtype: str
        """
        return self._column_type_setting

    @column_type_setting.setter
    def column_type_setting(self, column_type_setting):
        r"""Sets the column_type_setting of this SchemaColumns.

        列类型设置

        :param column_type_setting: The column_type_setting of this SchemaColumns.
        :type column_type_setting: str
        """
        self._column_type_setting = column_type_setting

    @property
    def depth(self):
        r"""Gets the depth of this SchemaColumns.

        深度

        :return: The depth of this SchemaColumns.
        :rtype: int
        """
        return self._depth

    @depth.setter
    def depth(self, depth):
        r"""Sets the depth of this SchemaColumns.

        深度

        :param depth: The depth of this SchemaColumns.
        :type depth: int
        """
        self._depth = depth

    @property
    def nullable(self):
        r"""Gets the nullable of this SchemaColumns.

        是否允许为空

        :return: The nullable of this SchemaColumns.
        :rtype: bool
        """
        return self._nullable

    @nullable.setter
    def nullable(self, nullable):
        r"""Sets the nullable of this SchemaColumns.

        是否允许为空

        :param nullable: The nullable of this SchemaColumns.
        :type nullable: bool
        """
        self._nullable = nullable

    @property
    def own_name(self):
        r"""Gets the own_name of this SchemaColumns.

        自有名称

        :return: The own_name of this SchemaColumns.
        :rtype: str
        """
        return self._own_name

    @own_name.setter
    def own_name(self, own_name):
        r"""Sets the own_name of this SchemaColumns.

        自有名称

        :param own_name: The own_name of this SchemaColumns.
        :type own_name: str
        """
        self._own_name = own_name

    @property
    def parent_name(self):
        r"""Gets the parent_name of this SchemaColumns.

        父名称

        :return: The parent_name of this SchemaColumns.
        :rtype: str
        """
        return self._parent_name

    @parent_name.setter
    def parent_name(self, parent_name):
        r"""Sets the parent_name of this SchemaColumns.

        父名称

        :param parent_name: The parent_name of this SchemaColumns.
        :type parent_name: str
        """
        self._parent_name = parent_name

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
        if not isinstance(other, SchemaColumns):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
