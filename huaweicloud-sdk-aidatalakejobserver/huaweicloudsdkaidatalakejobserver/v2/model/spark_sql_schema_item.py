# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SparkSqlSchemaItem:

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
        'column_type': 'str'
    }

    attribute_map = {
        'column_name': 'column_name',
        'column_type': 'column_type'
    }

    def __init__(self, column_name=None, column_type=None):
        r"""SparkSqlSchemaItem

        The model defined in huaweicloud sdk

        :param column_name: **参数解释**：列名，用于标识结果数据中的列名称。 **取值范围**：长度为1~128个字符，例如：col1。
        :type column_name: str
        :param column_type: **参数解释**：列类型，用于标识结果数据中的列数据类型。 **取值范围**：支持的数据类型，例如：STRING、INT等。
        :type column_type: str
        """
        
        

        self._column_name = None
        self._column_type = None
        self.discriminator = None

        if column_name is not None:
            self.column_name = column_name
        if column_type is not None:
            self.column_type = column_type

    @property
    def column_name(self):
        r"""Gets the column_name of this SparkSqlSchemaItem.

        **参数解释**：列名，用于标识结果数据中的列名称。 **取值范围**：长度为1~128个字符，例如：col1。

        :return: The column_name of this SparkSqlSchemaItem.
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        r"""Sets the column_name of this SparkSqlSchemaItem.

        **参数解释**：列名，用于标识结果数据中的列名称。 **取值范围**：长度为1~128个字符，例如：col1。

        :param column_name: The column_name of this SparkSqlSchemaItem.
        :type column_name: str
        """
        self._column_name = column_name

    @property
    def column_type(self):
        r"""Gets the column_type of this SparkSqlSchemaItem.

        **参数解释**：列类型，用于标识结果数据中的列数据类型。 **取值范围**：支持的数据类型，例如：STRING、INT等。

        :return: The column_type of this SparkSqlSchemaItem.
        :rtype: str
        """
        return self._column_type

    @column_type.setter
    def column_type(self, column_type):
        r"""Sets the column_type of this SparkSqlSchemaItem.

        **参数解释**：列类型，用于标识结果数据中的列数据类型。 **取值范围**：支持的数据类型，例如：STRING、INT等。

        :param column_type: The column_type of this SparkSqlSchemaItem.
        :type column_type: str
        """
        self._column_type = column_type

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
        if not isinstance(other, SparkSqlSchemaItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
