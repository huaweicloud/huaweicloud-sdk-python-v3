# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TableColumnForIsapPipe:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'column_name': 'str',
        'column_data_type': 'str',
        'column_data_type_setting': 'str',
        'column_type': 'str',
        'column_type_setting': 'str',
        'default_value': 'str',
        'nullable': 'bool',
        'array': 'bool',
        'depth': 'int',
        'parent_name': 'str',
        'own_name': 'str'
    }

    attribute_map = {
        'column_name': 'column_name',
        'column_data_type': 'column_data_type',
        'column_data_type_setting': 'column_data_type_setting',
        'column_type': 'column_type',
        'column_type_setting': 'column_type_setting',
        'default_value': 'default_value',
        'nullable': 'nullable',
        'array': 'array',
        'depth': 'depth',
        'parent_name': 'parent_name',
        'own_name': 'own_name'
    }

    def __init__(self, column_name=None, column_data_type=None, column_data_type_setting=None, column_type=None, column_type_setting=None, default_value=None, nullable=None, array=None, depth=None, parent_name=None, own_name=None):
        r"""TableColumnForIsapPipe

        The model defined in huaweicloud sdk

        :param column_name: 表列名称
        :type column_name: str
        :param column_data_type: **参数解释**: 列字段数据类型 - ROW 行类型 - MAP_STRING 字符串映射类型 - MAP_DECIMAL 小数映射类型 - TINYINT 微整型 - SMALLINT 小整型 - INT 整型 - BIGINT 长整型 - DECIMAL 精确小数类型 - FLOAT 单精度浮点数 - DOUBLE 双精度浮点数 - CHAR 定长字符串 - VARCHAR 不定长字符串 - STRING 字符串类型 - KEYWORD 关键字类型 - BOOLEAN 布尔类型 - DATE 日期类型 - TIME 时间类型 - TIMESTAMP 时间戳类型 - TIMESTAMP_LTZ 本地时间戳类型  **约束限制** 不涉及  **取值范围**: - ROW - MAP_STRING - MAP_DECIMAL - TINYINT - SMALLINT - INT - BIGINT - DECIMAL - FLOAT - DOUBLE - CHAR - VARCHAR - STRING - KEYWORD - BOOLEAN - DATE - TIME - TIMESTAMP - TIMESTAMP_LTZ  **默认值** 不涉及    
        :type column_data_type: str
        :param column_data_type_setting: 列数据类型设置
        :type column_data_type_setting: str
        :param column_type: **参数解释**: 列字段类型 - PHYSICAL 物理字段 - METADATA 元数据字段 - VIRTUAL_METADATA 虚拟元数据字段 - COMPUTED 计算字段  **约束限制** 不涉及  **取值范围**: - PHYSICAL - METADATA - VIRTUAL_METADATA - COMPUTED  **默认值** 不涉及   
        :type column_type: str
        :param column_type_setting: 列类型设置
        :type column_type_setting: str
        :param default_value: 列默认值
        :type default_value: str
        :param nullable: 列是否可为空
        :type nullable: bool
        :param array: 是否为数组
        :type array: bool
        :param depth: 列深度
        :type depth: int
        :param parent_name: 列名称
        :type parent_name: str
        :param own_name: 列名称
        :type own_name: str
        """
        
        

        self._column_name = None
        self._column_data_type = None
        self._column_data_type_setting = None
        self._column_type = None
        self._column_type_setting = None
        self._default_value = None
        self._nullable = None
        self._array = None
        self._depth = None
        self._parent_name = None
        self._own_name = None
        self.discriminator = None

        self.column_name = column_name
        self.column_data_type = column_data_type
        if column_data_type_setting is not None:
            self.column_data_type_setting = column_data_type_setting
        if column_type is not None:
            self.column_type = column_type
        if column_type_setting is not None:
            self.column_type_setting = column_type_setting
        if default_value is not None:
            self.default_value = default_value
        if nullable is not None:
            self.nullable = nullable
        if array is not None:
            self.array = array
        if depth is not None:
            self.depth = depth
        if parent_name is not None:
            self.parent_name = parent_name
        if own_name is not None:
            self.own_name = own_name

    @property
    def column_name(self):
        r"""Gets the column_name of this TableColumnForIsapPipe.

        表列名称

        :return: The column_name of this TableColumnForIsapPipe.
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        r"""Sets the column_name of this TableColumnForIsapPipe.

        表列名称

        :param column_name: The column_name of this TableColumnForIsapPipe.
        :type column_name: str
        """
        self._column_name = column_name

    @property
    def column_data_type(self):
        r"""Gets the column_data_type of this TableColumnForIsapPipe.

        **参数解释**: 列字段数据类型 - ROW 行类型 - MAP_STRING 字符串映射类型 - MAP_DECIMAL 小数映射类型 - TINYINT 微整型 - SMALLINT 小整型 - INT 整型 - BIGINT 长整型 - DECIMAL 精确小数类型 - FLOAT 单精度浮点数 - DOUBLE 双精度浮点数 - CHAR 定长字符串 - VARCHAR 不定长字符串 - STRING 字符串类型 - KEYWORD 关键字类型 - BOOLEAN 布尔类型 - DATE 日期类型 - TIME 时间类型 - TIMESTAMP 时间戳类型 - TIMESTAMP_LTZ 本地时间戳类型  **约束限制** 不涉及  **取值范围**: - ROW - MAP_STRING - MAP_DECIMAL - TINYINT - SMALLINT - INT - BIGINT - DECIMAL - FLOAT - DOUBLE - CHAR - VARCHAR - STRING - KEYWORD - BOOLEAN - DATE - TIME - TIMESTAMP - TIMESTAMP_LTZ  **默认值** 不涉及    

        :return: The column_data_type of this TableColumnForIsapPipe.
        :rtype: str
        """
        return self._column_data_type

    @column_data_type.setter
    def column_data_type(self, column_data_type):
        r"""Sets the column_data_type of this TableColumnForIsapPipe.

        **参数解释**: 列字段数据类型 - ROW 行类型 - MAP_STRING 字符串映射类型 - MAP_DECIMAL 小数映射类型 - TINYINT 微整型 - SMALLINT 小整型 - INT 整型 - BIGINT 长整型 - DECIMAL 精确小数类型 - FLOAT 单精度浮点数 - DOUBLE 双精度浮点数 - CHAR 定长字符串 - VARCHAR 不定长字符串 - STRING 字符串类型 - KEYWORD 关键字类型 - BOOLEAN 布尔类型 - DATE 日期类型 - TIME 时间类型 - TIMESTAMP 时间戳类型 - TIMESTAMP_LTZ 本地时间戳类型  **约束限制** 不涉及  **取值范围**: - ROW - MAP_STRING - MAP_DECIMAL - TINYINT - SMALLINT - INT - BIGINT - DECIMAL - FLOAT - DOUBLE - CHAR - VARCHAR - STRING - KEYWORD - BOOLEAN - DATE - TIME - TIMESTAMP - TIMESTAMP_LTZ  **默认值** 不涉及    

        :param column_data_type: The column_data_type of this TableColumnForIsapPipe.
        :type column_data_type: str
        """
        self._column_data_type = column_data_type

    @property
    def column_data_type_setting(self):
        r"""Gets the column_data_type_setting of this TableColumnForIsapPipe.

        列数据类型设置

        :return: The column_data_type_setting of this TableColumnForIsapPipe.
        :rtype: str
        """
        return self._column_data_type_setting

    @column_data_type_setting.setter
    def column_data_type_setting(self, column_data_type_setting):
        r"""Sets the column_data_type_setting of this TableColumnForIsapPipe.

        列数据类型设置

        :param column_data_type_setting: The column_data_type_setting of this TableColumnForIsapPipe.
        :type column_data_type_setting: str
        """
        self._column_data_type_setting = column_data_type_setting

    @property
    def column_type(self):
        r"""Gets the column_type of this TableColumnForIsapPipe.

        **参数解释**: 列字段类型 - PHYSICAL 物理字段 - METADATA 元数据字段 - VIRTUAL_METADATA 虚拟元数据字段 - COMPUTED 计算字段  **约束限制** 不涉及  **取值范围**: - PHYSICAL - METADATA - VIRTUAL_METADATA - COMPUTED  **默认值** 不涉及   

        :return: The column_type of this TableColumnForIsapPipe.
        :rtype: str
        """
        return self._column_type

    @column_type.setter
    def column_type(self, column_type):
        r"""Sets the column_type of this TableColumnForIsapPipe.

        **参数解释**: 列字段类型 - PHYSICAL 物理字段 - METADATA 元数据字段 - VIRTUAL_METADATA 虚拟元数据字段 - COMPUTED 计算字段  **约束限制** 不涉及  **取值范围**: - PHYSICAL - METADATA - VIRTUAL_METADATA - COMPUTED  **默认值** 不涉及   

        :param column_type: The column_type of this TableColumnForIsapPipe.
        :type column_type: str
        """
        self._column_type = column_type

    @property
    def column_type_setting(self):
        r"""Gets the column_type_setting of this TableColumnForIsapPipe.

        列类型设置

        :return: The column_type_setting of this TableColumnForIsapPipe.
        :rtype: str
        """
        return self._column_type_setting

    @column_type_setting.setter
    def column_type_setting(self, column_type_setting):
        r"""Sets the column_type_setting of this TableColumnForIsapPipe.

        列类型设置

        :param column_type_setting: The column_type_setting of this TableColumnForIsapPipe.
        :type column_type_setting: str
        """
        self._column_type_setting = column_type_setting

    @property
    def default_value(self):
        r"""Gets the default_value of this TableColumnForIsapPipe.

        列默认值

        :return: The default_value of this TableColumnForIsapPipe.
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        r"""Sets the default_value of this TableColumnForIsapPipe.

        列默认值

        :param default_value: The default_value of this TableColumnForIsapPipe.
        :type default_value: str
        """
        self._default_value = default_value

    @property
    def nullable(self):
        r"""Gets the nullable of this TableColumnForIsapPipe.

        列是否可为空

        :return: The nullable of this TableColumnForIsapPipe.
        :rtype: bool
        """
        return self._nullable

    @nullable.setter
    def nullable(self, nullable):
        r"""Sets the nullable of this TableColumnForIsapPipe.

        列是否可为空

        :param nullable: The nullable of this TableColumnForIsapPipe.
        :type nullable: bool
        """
        self._nullable = nullable

    @property
    def array(self):
        r"""Gets the array of this TableColumnForIsapPipe.

        是否为数组

        :return: The array of this TableColumnForIsapPipe.
        :rtype: bool
        """
        return self._array

    @array.setter
    def array(self, array):
        r"""Sets the array of this TableColumnForIsapPipe.

        是否为数组

        :param array: The array of this TableColumnForIsapPipe.
        :type array: bool
        """
        self._array = array

    @property
    def depth(self):
        r"""Gets the depth of this TableColumnForIsapPipe.

        列深度

        :return: The depth of this TableColumnForIsapPipe.
        :rtype: int
        """
        return self._depth

    @depth.setter
    def depth(self, depth):
        r"""Sets the depth of this TableColumnForIsapPipe.

        列深度

        :param depth: The depth of this TableColumnForIsapPipe.
        :type depth: int
        """
        self._depth = depth

    @property
    def parent_name(self):
        r"""Gets the parent_name of this TableColumnForIsapPipe.

        列名称

        :return: The parent_name of this TableColumnForIsapPipe.
        :rtype: str
        """
        return self._parent_name

    @parent_name.setter
    def parent_name(self, parent_name):
        r"""Sets the parent_name of this TableColumnForIsapPipe.

        列名称

        :param parent_name: The parent_name of this TableColumnForIsapPipe.
        :type parent_name: str
        """
        self._parent_name = parent_name

    @property
    def own_name(self):
        r"""Gets the own_name of this TableColumnForIsapPipe.

        列名称

        :return: The own_name of this TableColumnForIsapPipe.
        :rtype: str
        """
        return self._own_name

    @own_name.setter
    def own_name(self, own_name):
        r"""Sets the own_name of this TableColumnForIsapPipe.

        列名称

        :param own_name: The own_name of this TableColumnForIsapPipe.
        :type own_name: str
        """
        self._own_name = own_name

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
        if not isinstance(other, TableColumnForIsapPipe):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
