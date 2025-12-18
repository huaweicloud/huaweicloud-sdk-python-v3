# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NoSqlCreateBackupRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'database_tables': 'list[DatabaseTable]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'database_tables': 'database_tables'
    }

    def __init__(self, name=None, description=None, database_tables=None):
        r"""NoSqlCreateBackupRequestBody

        The model defined in huaweicloud sdk

        :param name: **参数解释：** 手动备份名称。 **约束限制：** 长度为4~64位，必须以字母开头（A~Z或a~z），区分大小写，可以包含字母、数字（0~9）、中划线（-）或者下划线（_），不能包含其他特殊字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type name: str
        :param description: **参数解释：** 手动备份描述。 **约束限制：** 长度不超过256位，且不能包含&gt;!&lt;\&quot;&amp;&#39;&#x3D;特殊字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type description: str
        :param database_tables: **参数解释：** 备份里的库表信息。 **约束限制：** 该参数仅针对GeminiDB Cassandra。 **取值范围：** - 字段为空，表示创建实例级备份。 - 字段非空，表示创建库表级备份。  **默认取值：** 不涉及。
        :type database_tables: list[:class:`huaweicloudsdkgaussdbfornosql.v3.DatabaseTable`]
        """
        
        

        self._name = None
        self._description = None
        self._database_tables = None
        self.discriminator = None

        self.name = name
        self.description = description
        if database_tables is not None:
            self.database_tables = database_tables

    @property
    def name(self):
        r"""Gets the name of this NoSqlCreateBackupRequestBody.

        **参数解释：** 手动备份名称。 **约束限制：** 长度为4~64位，必须以字母开头（A~Z或a~z），区分大小写，可以包含字母、数字（0~9）、中划线（-）或者下划线（_），不能包含其他特殊字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The name of this NoSqlCreateBackupRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this NoSqlCreateBackupRequestBody.

        **参数解释：** 手动备份名称。 **约束限制：** 长度为4~64位，必须以字母开头（A~Z或a~z），区分大小写，可以包含字母、数字（0~9）、中划线（-）或者下划线（_），不能包含其他特殊字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param name: The name of this NoSqlCreateBackupRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this NoSqlCreateBackupRequestBody.

        **参数解释：** 手动备份描述。 **约束限制：** 长度不超过256位，且不能包含>!<\"&'=特殊字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The description of this NoSqlCreateBackupRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this NoSqlCreateBackupRequestBody.

        **参数解释：** 手动备份描述。 **约束限制：** 长度不超过256位，且不能包含>!<\"&'=特殊字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param description: The description of this NoSqlCreateBackupRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def database_tables(self):
        r"""Gets the database_tables of this NoSqlCreateBackupRequestBody.

        **参数解释：** 备份里的库表信息。 **约束限制：** 该参数仅针对GeminiDB Cassandra。 **取值范围：** - 字段为空，表示创建实例级备份。 - 字段非空，表示创建库表级备份。  **默认取值：** 不涉及。

        :return: The database_tables of this NoSqlCreateBackupRequestBody.
        :rtype: list[:class:`huaweicloudsdkgaussdbfornosql.v3.DatabaseTable`]
        """
        return self._database_tables

    @database_tables.setter
    def database_tables(self, database_tables):
        r"""Sets the database_tables of this NoSqlCreateBackupRequestBody.

        **参数解释：** 备份里的库表信息。 **约束限制：** 该参数仅针对GeminiDB Cassandra。 **取值范围：** - 字段为空，表示创建实例级备份。 - 字段非空，表示创建库表级备份。  **默认取值：** 不涉及。

        :param database_tables: The database_tables of this NoSqlCreateBackupRequestBody.
        :type database_tables: list[:class:`huaweicloudsdkgaussdbfornosql.v3.DatabaseTable`]
        """
        self._database_tables = database_tables

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
        if not isinstance(other, NoSqlCreateBackupRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
