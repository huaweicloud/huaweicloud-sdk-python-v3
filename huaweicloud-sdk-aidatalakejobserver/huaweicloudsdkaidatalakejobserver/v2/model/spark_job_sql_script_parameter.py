# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SparkJobSqlScriptParameter:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'value': 'str',
        'value_type': 'SparkSqlParameterValueType'
    }

    attribute_map = {
        'key': 'key',
        'value': 'value',
        'value_type': 'value_type'
    }

    def __init__(self, key=None, value=None, value_type=None):
        r"""SparkJobSqlScriptParameter

        The model defined in huaweicloud sdk

        :param key: **参数解释**：占位符的键，用于标识SQL脚本中的参数名称。 **取值范围**：长度为1~128个字符。 
        :type key: str
        :param value: **参数解释**：占位符的值，用于传递给SQL脚本的实际参数值。不同类型的数据格式如下： - STRING：字符串，例如：“xxx”。 - DECIMAL：定点数，例如：“12.1”。 - INTEGER：整数，例如：“13”。 - DATE：日期时间戳，例如：“1779188276372”。 - TIMESTAMP：时间戳，例如：“1779188276372”。 **取值范围**：长度为1~512个字符。 
        :type value: str
        :param value_type: 
        :type value_type: :class:`huaweicloudsdkaidatalakejobserver.v2.SparkSqlParameterValueType`
        """
        
        

        self._key = None
        self._value = None
        self._value_type = None
        self.discriminator = None

        self.key = key
        self.value = value
        if value_type is not None:
            self.value_type = value_type

    @property
    def key(self):
        r"""Gets the key of this SparkJobSqlScriptParameter.

        **参数解释**：占位符的键，用于标识SQL脚本中的参数名称。 **取值范围**：长度为1~128个字符。 

        :return: The key of this SparkJobSqlScriptParameter.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this SparkJobSqlScriptParameter.

        **参数解释**：占位符的键，用于标识SQL脚本中的参数名称。 **取值范围**：长度为1~128个字符。 

        :param key: The key of this SparkJobSqlScriptParameter.
        :type key: str
        """
        self._key = key

    @property
    def value(self):
        r"""Gets the value of this SparkJobSqlScriptParameter.

        **参数解释**：占位符的值，用于传递给SQL脚本的实际参数值。不同类型的数据格式如下： - STRING：字符串，例如：“xxx”。 - DECIMAL：定点数，例如：“12.1”。 - INTEGER：整数，例如：“13”。 - DATE：日期时间戳，例如：“1779188276372”。 - TIMESTAMP：时间戳，例如：“1779188276372”。 **取值范围**：长度为1~512个字符。 

        :return: The value of this SparkJobSqlScriptParameter.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this SparkJobSqlScriptParameter.

        **参数解释**：占位符的值，用于传递给SQL脚本的实际参数值。不同类型的数据格式如下： - STRING：字符串，例如：“xxx”。 - DECIMAL：定点数，例如：“12.1”。 - INTEGER：整数，例如：“13”。 - DATE：日期时间戳，例如：“1779188276372”。 - TIMESTAMP：时间戳，例如：“1779188276372”。 **取值范围**：长度为1~512个字符。 

        :param value: The value of this SparkJobSqlScriptParameter.
        :type value: str
        """
        self._value = value

    @property
    def value_type(self):
        r"""Gets the value_type of this SparkJobSqlScriptParameter.

        :return: The value_type of this SparkJobSqlScriptParameter.
        :rtype: :class:`huaweicloudsdkaidatalakejobserver.v2.SparkSqlParameterValueType`
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        r"""Sets the value_type of this SparkJobSqlScriptParameter.

        :param value_type: The value_type of this SparkJobSqlScriptParameter.
        :type value_type: :class:`huaweicloudsdkaidatalakejobserver.v2.SparkSqlParameterValueType`
        """
        self._value_type = value_type

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
        if not isinstance(other, SparkJobSqlScriptParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
