# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DatabaseTable:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'database_name': 'str',
        'table_names': 'list[str]'
    }

    attribute_map = {
        'database_name': 'database_name',
        'table_names': 'table_names'
    }

    def __init__(self, database_name=None, table_names=None):
        r"""DatabaseTable

        The model defined in huaweicloud sdk

        :param database_name: **参数解释：** 数据库名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type database_name: str
        :param table_names: **参数解释：** 数据表名称列表。 **约束限制：** 不涉及。 **取值范围：** - table_names为空的时候，表示库级别备份。 - table_names非空的时候，表示表级别备份。  **默认取值：** 不涉及。
        :type table_names: list[str]
        """
        
        

        self._database_name = None
        self._table_names = None
        self.discriminator = None

        self.database_name = database_name
        if table_names is not None:
            self.table_names = table_names

    @property
    def database_name(self):
        r"""Gets the database_name of this DatabaseTable.

        **参数解释：** 数据库名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The database_name of this DatabaseTable.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this DatabaseTable.

        **参数解释：** 数据库名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param database_name: The database_name of this DatabaseTable.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def table_names(self):
        r"""Gets the table_names of this DatabaseTable.

        **参数解释：** 数据表名称列表。 **约束限制：** 不涉及。 **取值范围：** - table_names为空的时候，表示库级别备份。 - table_names非空的时候，表示表级别备份。  **默认取值：** 不涉及。

        :return: The table_names of this DatabaseTable.
        :rtype: list[str]
        """
        return self._table_names

    @table_names.setter
    def table_names(self, table_names):
        r"""Sets the table_names of this DatabaseTable.

        **参数解释：** 数据表名称列表。 **约束限制：** 不涉及。 **取值范围：** - table_names为空的时候，表示库级别备份。 - table_names非空的时候，表示表级别备份。  **默认取值：** 不涉及。

        :param table_names: The table_names of this DatabaseTable.
        :type table_names: list[str]
        """
        self._table_names = table_names

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
        if not isinstance(other, DatabaseTable):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
