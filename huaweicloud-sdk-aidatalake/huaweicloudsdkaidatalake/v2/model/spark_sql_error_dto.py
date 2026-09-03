# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SparkSqlErrorDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'message': 'str',
        'sql_state': 'str',
        'error_class': 'str',
        'line': 'int',
        'start_position': 'int'
    }

    attribute_map = {
        'message': 'message',
        'sql_state': 'sql_state',
        'error_class': 'error_class',
        'line': 'line',
        'start_position': 'start_position'
    }

    def __init__(self, message=None, sql_state=None, error_class=None, line=None, start_position=None):
        r"""SparkSqlErrorDto

        The model defined in huaweicloud sdk

        :param message: **参数解释**：SparkSql错误描述，用于说明错误的具体原因。 **取值范围**：长度为1~1024个字符，例如：表不存在。 
        :type message: str
        :param sql_state: **参数解释**：SparkSql错误码，用于标识错误的类型。 **取值范围**：采用标准SQL错误码格式，例如：42P01。 
        :type sql_state: str
        :param error_class: **参数解释**：SparkSql错误类型，用于标识错误的分类。 **取值范围**：长度为1~128个字符，例如：SCHEMA_ALREADY_EXISTS。 
        :type error_class: str
        :param line: **参数解释**：报错行号，用于定位SQL语句中的错误位置。 **取值范围**：大于0的整数，例如：2。 
        :type line: int
        :param start_position: **参数解释**：报错起始位置，用于定位SQL语句中错误的起始字符位置。 **取值范围**：大于0的整数，例如：2。 
        :type start_position: int
        """
        
        

        self._message = None
        self._sql_state = None
        self._error_class = None
        self._line = None
        self._start_position = None
        self.discriminator = None

        if message is not None:
            self.message = message
        if sql_state is not None:
            self.sql_state = sql_state
        if error_class is not None:
            self.error_class = error_class
        if line is not None:
            self.line = line
        if start_position is not None:
            self.start_position = start_position

    @property
    def message(self):
        r"""Gets the message of this SparkSqlErrorDto.

        **参数解释**：SparkSql错误描述，用于说明错误的具体原因。 **取值范围**：长度为1~1024个字符，例如：表不存在。 

        :return: The message of this SparkSqlErrorDto.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this SparkSqlErrorDto.

        **参数解释**：SparkSql错误描述，用于说明错误的具体原因。 **取值范围**：长度为1~1024个字符，例如：表不存在。 

        :param message: The message of this SparkSqlErrorDto.
        :type message: str
        """
        self._message = message

    @property
    def sql_state(self):
        r"""Gets the sql_state of this SparkSqlErrorDto.

        **参数解释**：SparkSql错误码，用于标识错误的类型。 **取值范围**：采用标准SQL错误码格式，例如：42P01。 

        :return: The sql_state of this SparkSqlErrorDto.
        :rtype: str
        """
        return self._sql_state

    @sql_state.setter
    def sql_state(self, sql_state):
        r"""Sets the sql_state of this SparkSqlErrorDto.

        **参数解释**：SparkSql错误码，用于标识错误的类型。 **取值范围**：采用标准SQL错误码格式，例如：42P01。 

        :param sql_state: The sql_state of this SparkSqlErrorDto.
        :type sql_state: str
        """
        self._sql_state = sql_state

    @property
    def error_class(self):
        r"""Gets the error_class of this SparkSqlErrorDto.

        **参数解释**：SparkSql错误类型，用于标识错误的分类。 **取值范围**：长度为1~128个字符，例如：SCHEMA_ALREADY_EXISTS。 

        :return: The error_class of this SparkSqlErrorDto.
        :rtype: str
        """
        return self._error_class

    @error_class.setter
    def error_class(self, error_class):
        r"""Sets the error_class of this SparkSqlErrorDto.

        **参数解释**：SparkSql错误类型，用于标识错误的分类。 **取值范围**：长度为1~128个字符，例如：SCHEMA_ALREADY_EXISTS。 

        :param error_class: The error_class of this SparkSqlErrorDto.
        :type error_class: str
        """
        self._error_class = error_class

    @property
    def line(self):
        r"""Gets the line of this SparkSqlErrorDto.

        **参数解释**：报错行号，用于定位SQL语句中的错误位置。 **取值范围**：大于0的整数，例如：2。 

        :return: The line of this SparkSqlErrorDto.
        :rtype: int
        """
        return self._line

    @line.setter
    def line(self, line):
        r"""Sets the line of this SparkSqlErrorDto.

        **参数解释**：报错行号，用于定位SQL语句中的错误位置。 **取值范围**：大于0的整数，例如：2。 

        :param line: The line of this SparkSqlErrorDto.
        :type line: int
        """
        self._line = line

    @property
    def start_position(self):
        r"""Gets the start_position of this SparkSqlErrorDto.

        **参数解释**：报错起始位置，用于定位SQL语句中错误的起始字符位置。 **取值范围**：大于0的整数，例如：2。 

        :return: The start_position of this SparkSqlErrorDto.
        :rtype: int
        """
        return self._start_position

    @start_position.setter
    def start_position(self, start_position):
        r"""Sets the start_position of this SparkSqlErrorDto.

        **参数解释**：报错起始位置，用于定位SQL语句中错误的起始字符位置。 **取值范围**：大于0的整数，例如：2。 

        :param start_position: The start_position of this SparkSqlErrorDto.
        :type start_position: int
        """
        self._start_position = start_position

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
        if not isinstance(other, SparkSqlErrorDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
