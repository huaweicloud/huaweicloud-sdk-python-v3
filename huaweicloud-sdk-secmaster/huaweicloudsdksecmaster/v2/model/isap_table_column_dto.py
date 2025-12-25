# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IsapTableColumnDto:

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
        'column_type': 'str',
        'column_type_setting': 'str',
        'column_data_type': 'str',
        'column_data_type_setting': 'str',
        'nullable': 'bool',
        'array': 'bool',
        'column_display_setting': 'ColumnDisplaySetting',
        'column_sequence_number': 'int'
    }

    attribute_map = {
        'column_name': 'column_name',
        'column_type': 'column_type',
        'column_type_setting': 'column_type_setting',
        'column_data_type': 'column_data_type',
        'column_data_type_setting': 'column_data_type_setting',
        'nullable': 'nullable',
        'array': 'array',
        'column_display_setting': 'column_display_setting',
        'column_sequence_number': 'column_sequence_number'
    }

    def __init__(self, column_name=None, column_type=None, column_type_setting=None, column_data_type=None, column_data_type_setting=None, nullable=None, array=None, column_display_setting=None, column_sequence_number=None):
        r"""IsapTableColumnDto

        The model defined in huaweicloud sdk

        :param column_name: 表格列名称
        :type column_name: str
        :param column_type: **参数解释**: 列字段类型 - PHYSICAL 物理字段 - METADATA 元数据字段 - VIRTUAL_METADATA 虚拟元数据字段 - COMPUTED 计算字段  **约束限制** 不涉及  **取值范围**: - PHYSICAL - METADATA - VIRTUAL_METADATA - COMPUTED  **默认值** 不涉及    
        :type column_type: str
        :param column_type_setting: 表格列类型设置
        :type column_type_setting: str
        :param column_data_type: **参数解释**: 列字段数据类型 - ROW 行类型 - MAP_STRING 字符串映射类型 - MAP_DECIMAL 小数映射类型 - TINYINT 微整型 - SMALLINT 小整型 - INT 整型 - BIGINT 长整型 - DECIMAL 精确小数类型 - FLOAT 单精度浮点数 - DOUBLE 双精度浮点数 - CHAR 定长字符串 - VARCHAR 不定长字符串 - STRING 字符串类型 - KEYWORD 关键字类型 - BOOLEAN 布尔类型 - DATE 日期类型 - TIME 时间类型 - TIMESTAMP 时间戳类型 - TIMESTAMP_LTZ 本地时间戳类型  **约束限制** 不涉及  **取值范围**: - ROW - MAP_STRING - MAP_DECIMAL - TINYINT - SMALLINT - INT - BIGINT - DECIMAL - FLOAT - DOUBLE - CHAR - VARCHAR - STRING - KEYWORD - BOOLEAN - DATE - TIME - TIMESTAMP - TIMESTAMP_LTZ  **默认值** 不涉及    
        :type column_data_type: str
        :param column_data_type_setting: 表格列数据类型设置
        :type column_data_type_setting: str
        :param nullable: 是否为空
        :type nullable: bool
        :param array: 是否为数组
        :type array: bool
        :param column_display_setting: 
        :type column_display_setting: :class:`huaweicloudsdksecmaster.v2.ColumnDisplaySetting`
        :param column_sequence_number: 列序号
        :type column_sequence_number: int
        """
        
        

        self._column_name = None
        self._column_type = None
        self._column_type_setting = None
        self._column_data_type = None
        self._column_data_type_setting = None
        self._nullable = None
        self._array = None
        self._column_display_setting = None
        self._column_sequence_number = None
        self.discriminator = None

        if column_name is not None:
            self.column_name = column_name
        if column_type is not None:
            self.column_type = column_type
        if column_type_setting is not None:
            self.column_type_setting = column_type_setting
        if column_data_type is not None:
            self.column_data_type = column_data_type
        if column_data_type_setting is not None:
            self.column_data_type_setting = column_data_type_setting
        if nullable is not None:
            self.nullable = nullable
        if array is not None:
            self.array = array
        if column_display_setting is not None:
            self.column_display_setting = column_display_setting
        if column_sequence_number is not None:
            self.column_sequence_number = column_sequence_number

    @property
    def column_name(self):
        r"""Gets the column_name of this IsapTableColumnDto.

        表格列名称

        :return: The column_name of this IsapTableColumnDto.
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        r"""Sets the column_name of this IsapTableColumnDto.

        表格列名称

        :param column_name: The column_name of this IsapTableColumnDto.
        :type column_name: str
        """
        self._column_name = column_name

    @property
    def column_type(self):
        r"""Gets the column_type of this IsapTableColumnDto.

        **参数解释**: 列字段类型 - PHYSICAL 物理字段 - METADATA 元数据字段 - VIRTUAL_METADATA 虚拟元数据字段 - COMPUTED 计算字段  **约束限制** 不涉及  **取值范围**: - PHYSICAL - METADATA - VIRTUAL_METADATA - COMPUTED  **默认值** 不涉及    

        :return: The column_type of this IsapTableColumnDto.
        :rtype: str
        """
        return self._column_type

    @column_type.setter
    def column_type(self, column_type):
        r"""Sets the column_type of this IsapTableColumnDto.

        **参数解释**: 列字段类型 - PHYSICAL 物理字段 - METADATA 元数据字段 - VIRTUAL_METADATA 虚拟元数据字段 - COMPUTED 计算字段  **约束限制** 不涉及  **取值范围**: - PHYSICAL - METADATA - VIRTUAL_METADATA - COMPUTED  **默认值** 不涉及    

        :param column_type: The column_type of this IsapTableColumnDto.
        :type column_type: str
        """
        self._column_type = column_type

    @property
    def column_type_setting(self):
        r"""Gets the column_type_setting of this IsapTableColumnDto.

        表格列类型设置

        :return: The column_type_setting of this IsapTableColumnDto.
        :rtype: str
        """
        return self._column_type_setting

    @column_type_setting.setter
    def column_type_setting(self, column_type_setting):
        r"""Sets the column_type_setting of this IsapTableColumnDto.

        表格列类型设置

        :param column_type_setting: The column_type_setting of this IsapTableColumnDto.
        :type column_type_setting: str
        """
        self._column_type_setting = column_type_setting

    @property
    def column_data_type(self):
        r"""Gets the column_data_type of this IsapTableColumnDto.

        **参数解释**: 列字段数据类型 - ROW 行类型 - MAP_STRING 字符串映射类型 - MAP_DECIMAL 小数映射类型 - TINYINT 微整型 - SMALLINT 小整型 - INT 整型 - BIGINT 长整型 - DECIMAL 精确小数类型 - FLOAT 单精度浮点数 - DOUBLE 双精度浮点数 - CHAR 定长字符串 - VARCHAR 不定长字符串 - STRING 字符串类型 - KEYWORD 关键字类型 - BOOLEAN 布尔类型 - DATE 日期类型 - TIME 时间类型 - TIMESTAMP 时间戳类型 - TIMESTAMP_LTZ 本地时间戳类型  **约束限制** 不涉及  **取值范围**: - ROW - MAP_STRING - MAP_DECIMAL - TINYINT - SMALLINT - INT - BIGINT - DECIMAL - FLOAT - DOUBLE - CHAR - VARCHAR - STRING - KEYWORD - BOOLEAN - DATE - TIME - TIMESTAMP - TIMESTAMP_LTZ  **默认值** 不涉及    

        :return: The column_data_type of this IsapTableColumnDto.
        :rtype: str
        """
        return self._column_data_type

    @column_data_type.setter
    def column_data_type(self, column_data_type):
        r"""Sets the column_data_type of this IsapTableColumnDto.

        **参数解释**: 列字段数据类型 - ROW 行类型 - MAP_STRING 字符串映射类型 - MAP_DECIMAL 小数映射类型 - TINYINT 微整型 - SMALLINT 小整型 - INT 整型 - BIGINT 长整型 - DECIMAL 精确小数类型 - FLOAT 单精度浮点数 - DOUBLE 双精度浮点数 - CHAR 定长字符串 - VARCHAR 不定长字符串 - STRING 字符串类型 - KEYWORD 关键字类型 - BOOLEAN 布尔类型 - DATE 日期类型 - TIME 时间类型 - TIMESTAMP 时间戳类型 - TIMESTAMP_LTZ 本地时间戳类型  **约束限制** 不涉及  **取值范围**: - ROW - MAP_STRING - MAP_DECIMAL - TINYINT - SMALLINT - INT - BIGINT - DECIMAL - FLOAT - DOUBLE - CHAR - VARCHAR - STRING - KEYWORD - BOOLEAN - DATE - TIME - TIMESTAMP - TIMESTAMP_LTZ  **默认值** 不涉及    

        :param column_data_type: The column_data_type of this IsapTableColumnDto.
        :type column_data_type: str
        """
        self._column_data_type = column_data_type

    @property
    def column_data_type_setting(self):
        r"""Gets the column_data_type_setting of this IsapTableColumnDto.

        表格列数据类型设置

        :return: The column_data_type_setting of this IsapTableColumnDto.
        :rtype: str
        """
        return self._column_data_type_setting

    @column_data_type_setting.setter
    def column_data_type_setting(self, column_data_type_setting):
        r"""Sets the column_data_type_setting of this IsapTableColumnDto.

        表格列数据类型设置

        :param column_data_type_setting: The column_data_type_setting of this IsapTableColumnDto.
        :type column_data_type_setting: str
        """
        self._column_data_type_setting = column_data_type_setting

    @property
    def nullable(self):
        r"""Gets the nullable of this IsapTableColumnDto.

        是否为空

        :return: The nullable of this IsapTableColumnDto.
        :rtype: bool
        """
        return self._nullable

    @nullable.setter
    def nullable(self, nullable):
        r"""Sets the nullable of this IsapTableColumnDto.

        是否为空

        :param nullable: The nullable of this IsapTableColumnDto.
        :type nullable: bool
        """
        self._nullable = nullable

    @property
    def array(self):
        r"""Gets the array of this IsapTableColumnDto.

        是否为数组

        :return: The array of this IsapTableColumnDto.
        :rtype: bool
        """
        return self._array

    @array.setter
    def array(self, array):
        r"""Sets the array of this IsapTableColumnDto.

        是否为数组

        :param array: The array of this IsapTableColumnDto.
        :type array: bool
        """
        self._array = array

    @property
    def column_display_setting(self):
        r"""Gets the column_display_setting of this IsapTableColumnDto.

        :return: The column_display_setting of this IsapTableColumnDto.
        :rtype: :class:`huaweicloudsdksecmaster.v2.ColumnDisplaySetting`
        """
        return self._column_display_setting

    @column_display_setting.setter
    def column_display_setting(self, column_display_setting):
        r"""Sets the column_display_setting of this IsapTableColumnDto.

        :param column_display_setting: The column_display_setting of this IsapTableColumnDto.
        :type column_display_setting: :class:`huaweicloudsdksecmaster.v2.ColumnDisplaySetting`
        """
        self._column_display_setting = column_display_setting

    @property
    def column_sequence_number(self):
        r"""Gets the column_sequence_number of this IsapTableColumnDto.

        列序号

        :return: The column_sequence_number of this IsapTableColumnDto.
        :rtype: int
        """
        return self._column_sequence_number

    @column_sequence_number.setter
    def column_sequence_number(self, column_sequence_number):
        r"""Sets the column_sequence_number of this IsapTableColumnDto.

        列序号

        :param column_sequence_number: The column_sequence_number of this IsapTableColumnDto.
        :type column_sequence_number: int
        """
        self._column_sequence_number = column_sequence_number

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
        if not isinstance(other, IsapTableColumnDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
