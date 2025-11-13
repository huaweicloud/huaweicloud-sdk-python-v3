# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SuccessTable:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'db_name': 'str',
        'table_name': 'str',
        'config_name': 'str',
        'row_number': 'int',
        'full_table_name': 'str',
        'valid': 'bool'
    }

    attribute_map = {
        'db_name': 'db_name',
        'table_name': 'table_name',
        'config_name': 'config_name',
        'row_number': 'row_number',
        'full_table_name': 'full_table_name',
        'valid': 'valid'
    }

    def __init__(self, db_name=None, table_name=None, config_name=None, row_number=None, full_table_name=None, valid=None):
        r"""SuccessTable

        The model defined in huaweicloud sdk

        :param db_name: **参数解释**：  Excel导入成功的数据库名。   **取值范围**：  不涉及。
        :type db_name: str
        :param table_name: **参数解释**：  Excel导入成功的表名。   **取值范围**：  不涉及。
        :type table_name: str
        :param config_name: **参数解释**：  Excel导入成功的表配置。   **取值范围**：  不涉及。
        :type config_name: str
        :param row_number: **参数解释**：  Excel导入成功的行数。   **取值范围**：  不涉及。
        :type row_number: int
        :param full_table_name: **参数解释**：  Excel导入成功的表全名。   **取值范围**：  不涉及。
        :type full_table_name: str
        :param valid: **参数解释**：  Excel信息是否合规。   **取值范围**：  - true：校验结果合规。 - false：校验结果不合规。
        :type valid: bool
        """
        
        

        self._db_name = None
        self._table_name = None
        self._config_name = None
        self._row_number = None
        self._full_table_name = None
        self._valid = None
        self.discriminator = None

        if db_name is not None:
            self.db_name = db_name
        if table_name is not None:
            self.table_name = table_name
        if config_name is not None:
            self.config_name = config_name
        if row_number is not None:
            self.row_number = row_number
        if full_table_name is not None:
            self.full_table_name = full_table_name
        if valid is not None:
            self.valid = valid

    @property
    def db_name(self):
        r"""Gets the db_name of this SuccessTable.

        **参数解释**：  Excel导入成功的数据库名。   **取值范围**：  不涉及。

        :return: The db_name of this SuccessTable.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this SuccessTable.

        **参数解释**：  Excel导入成功的数据库名。   **取值范围**：  不涉及。

        :param db_name: The db_name of this SuccessTable.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def table_name(self):
        r"""Gets the table_name of this SuccessTable.

        **参数解释**：  Excel导入成功的表名。   **取值范围**：  不涉及。

        :return: The table_name of this SuccessTable.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this SuccessTable.

        **参数解释**：  Excel导入成功的表名。   **取值范围**：  不涉及。

        :param table_name: The table_name of this SuccessTable.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def config_name(self):
        r"""Gets the config_name of this SuccessTable.

        **参数解释**：  Excel导入成功的表配置。   **取值范围**：  不涉及。

        :return: The config_name of this SuccessTable.
        :rtype: str
        """
        return self._config_name

    @config_name.setter
    def config_name(self, config_name):
        r"""Sets the config_name of this SuccessTable.

        **参数解释**：  Excel导入成功的表配置。   **取值范围**：  不涉及。

        :param config_name: The config_name of this SuccessTable.
        :type config_name: str
        """
        self._config_name = config_name

    @property
    def row_number(self):
        r"""Gets the row_number of this SuccessTable.

        **参数解释**：  Excel导入成功的行数。   **取值范围**：  不涉及。

        :return: The row_number of this SuccessTable.
        :rtype: int
        """
        return self._row_number

    @row_number.setter
    def row_number(self, row_number):
        r"""Sets the row_number of this SuccessTable.

        **参数解释**：  Excel导入成功的行数。   **取值范围**：  不涉及。

        :param row_number: The row_number of this SuccessTable.
        :type row_number: int
        """
        self._row_number = row_number

    @property
    def full_table_name(self):
        r"""Gets the full_table_name of this SuccessTable.

        **参数解释**：  Excel导入成功的表全名。   **取值范围**：  不涉及。

        :return: The full_table_name of this SuccessTable.
        :rtype: str
        """
        return self._full_table_name

    @full_table_name.setter
    def full_table_name(self, full_table_name):
        r"""Sets the full_table_name of this SuccessTable.

        **参数解释**：  Excel导入成功的表全名。   **取值范围**：  不涉及。

        :param full_table_name: The full_table_name of this SuccessTable.
        :type full_table_name: str
        """
        self._full_table_name = full_table_name

    @property
    def valid(self):
        r"""Gets the valid of this SuccessTable.

        **参数解释**：  Excel信息是否合规。   **取值范围**：  - true：校验结果合规。 - false：校验结果不合规。

        :return: The valid of this SuccessTable.
        :rtype: bool
        """
        return self._valid

    @valid.setter
    def valid(self, valid):
        r"""Sets the valid of this SuccessTable.

        **参数解释**：  Excel信息是否合规。   **取值范围**：  - true：校验结果合规。 - false：校验结果不合规。

        :param valid: The valid of this SuccessTable.
        :type valid: bool
        """
        self._valid = valid

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
        if not isinstance(other, SuccessTable):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
