# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ErrorTable:

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
        'database_name': 'str',
        'table_name': 'str',
        'row_number': 'int',
        'full_description': 'str'
    }

    attribute_map = {
        'message': 'message',
        'database_name': 'database_name',
        'table_name': 'table_name',
        'row_number': 'row_number',
        'full_description': 'full_description'
    }

    def __init__(self, message=None, database_name=None, table_name=None, row_number=None, full_description=None):
        r"""ErrorTable

        The model defined in huaweicloud sdk

        :param message: **参数解释**：  Excel导入失败的对象信息。  **取值范围**：  不涉及。
        :type message: str
        :param database_name: **参数解释**：  Excel导入失败的数据库名。   **取值范围**：  不涉及。
        :type database_name: str
        :param table_name: **参数解释**：  Excel导入失败的表名。   **取值范围**：  不涉及。
        :type table_name: str
        :param row_number: **参数解释**：  Excel导入失败的行。  **取值范围**：  不涉及。
        :type row_number: int
        :param full_description: **参数解释**：  Excel导入失败的错误信息描述。  **取值范围**：  不涉及。
        :type full_description: str
        """
        
        

        self._message = None
        self._database_name = None
        self._table_name = None
        self._row_number = None
        self._full_description = None
        self.discriminator = None

        if message is not None:
            self.message = message
        if database_name is not None:
            self.database_name = database_name
        if table_name is not None:
            self.table_name = table_name
        if row_number is not None:
            self.row_number = row_number
        if full_description is not None:
            self.full_description = full_description

    @property
    def message(self):
        r"""Gets the message of this ErrorTable.

        **参数解释**：  Excel导入失败的对象信息。  **取值范围**：  不涉及。

        :return: The message of this ErrorTable.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ErrorTable.

        **参数解释**：  Excel导入失败的对象信息。  **取值范围**：  不涉及。

        :param message: The message of this ErrorTable.
        :type message: str
        """
        self._message = message

    @property
    def database_name(self):
        r"""Gets the database_name of this ErrorTable.

        **参数解释**：  Excel导入失败的数据库名。   **取值范围**：  不涉及。

        :return: The database_name of this ErrorTable.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this ErrorTable.

        **参数解释**：  Excel导入失败的数据库名。   **取值范围**：  不涉及。

        :param database_name: The database_name of this ErrorTable.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def table_name(self):
        r"""Gets the table_name of this ErrorTable.

        **参数解释**：  Excel导入失败的表名。   **取值范围**：  不涉及。

        :return: The table_name of this ErrorTable.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this ErrorTable.

        **参数解释**：  Excel导入失败的表名。   **取值范围**：  不涉及。

        :param table_name: The table_name of this ErrorTable.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def row_number(self):
        r"""Gets the row_number of this ErrorTable.

        **参数解释**：  Excel导入失败的行。  **取值范围**：  不涉及。

        :return: The row_number of this ErrorTable.
        :rtype: int
        """
        return self._row_number

    @row_number.setter
    def row_number(self, row_number):
        r"""Sets the row_number of this ErrorTable.

        **参数解释**：  Excel导入失败的行。  **取值范围**：  不涉及。

        :param row_number: The row_number of this ErrorTable.
        :type row_number: int
        """
        self._row_number = row_number

    @property
    def full_description(self):
        r"""Gets the full_description of this ErrorTable.

        **参数解释**：  Excel导入失败的错误信息描述。  **取值范围**：  不涉及。

        :return: The full_description of this ErrorTable.
        :rtype: str
        """
        return self._full_description

    @full_description.setter
    def full_description(self, full_description):
        r"""Sets the full_description of this ErrorTable.

        **参数解释**：  Excel导入失败的错误信息描述。  **取值范围**：  不涉及。

        :param full_description: The full_description of this ErrorTable.
        :type full_description: str
        """
        self._full_description = full_description

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
        if not isinstance(other, ErrorTable):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
