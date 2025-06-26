# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FineGrainedSnapshotDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'database': 'str',
        'schema_list': 'list[str]',
        'table_list': 'list[str]'
    }

    attribute_map = {
        'database': 'database',
        'schema_list': 'schema_list',
        'table_list': 'table_list'
    }

    def __init__(self, database=None, schema_list=None, table_list=None):
        r"""FineGrainedSnapshotDetail

        The model defined in huaweicloud sdk

        :param database: **参数解释**： 数据库。 **取值范围**： 不涉及。
        :type database: str
        :param schema_list: **参数解释**： 模式列表。 **取值范围**： 不涉及。
        :type schema_list: list[str]
        :param table_list: **参数解释**： 表集合。 **取值范围**： 不涉及。
        :type table_list: list[str]
        """
        
        

        self._database = None
        self._schema_list = None
        self._table_list = None
        self.discriminator = None

        if database is not None:
            self.database = database
        if schema_list is not None:
            self.schema_list = schema_list
        if table_list is not None:
            self.table_list = table_list

    @property
    def database(self):
        r"""Gets the database of this FineGrainedSnapshotDetail.

        **参数解释**： 数据库。 **取值范围**： 不涉及。

        :return: The database of this FineGrainedSnapshotDetail.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        r"""Sets the database of this FineGrainedSnapshotDetail.

        **参数解释**： 数据库。 **取值范围**： 不涉及。

        :param database: The database of this FineGrainedSnapshotDetail.
        :type database: str
        """
        self._database = database

    @property
    def schema_list(self):
        r"""Gets the schema_list of this FineGrainedSnapshotDetail.

        **参数解释**： 模式列表。 **取值范围**： 不涉及。

        :return: The schema_list of this FineGrainedSnapshotDetail.
        :rtype: list[str]
        """
        return self._schema_list

    @schema_list.setter
    def schema_list(self, schema_list):
        r"""Sets the schema_list of this FineGrainedSnapshotDetail.

        **参数解释**： 模式列表。 **取值范围**： 不涉及。

        :param schema_list: The schema_list of this FineGrainedSnapshotDetail.
        :type schema_list: list[str]
        """
        self._schema_list = schema_list

    @property
    def table_list(self):
        r"""Gets the table_list of this FineGrainedSnapshotDetail.

        **参数解释**： 表集合。 **取值范围**： 不涉及。

        :return: The table_list of this FineGrainedSnapshotDetail.
        :rtype: list[str]
        """
        return self._table_list

    @table_list.setter
    def table_list(self, table_list):
        r"""Sets the table_list of this FineGrainedSnapshotDetail.

        **参数解释**： 表集合。 **取值范围**： 不涉及。

        :param table_list: The table_list of this FineGrainedSnapshotDetail.
        :type table_list: list[str]
        """
        self._table_list = table_list

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FineGrainedSnapshotDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
