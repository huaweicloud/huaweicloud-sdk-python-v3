# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestoreTableListDetail:

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
        'schema_name': 'str',
        'table_name': 'str',
        'new_db_name': 'str',
        'new_schema_name': 'str',
        'new_table_name': 'str'
    }

    attribute_map = {
        'db_name': 'db_name',
        'schema_name': 'schema_name',
        'table_name': 'table_name',
        'new_db_name': 'new_db_name',
        'new_schema_name': 'new_schema_name',
        'new_table_name': 'new_table_name'
    }

    def __init__(self, db_name=None, schema_name=None, table_name=None, new_db_name=None, new_schema_name=None, new_table_name=None):
        """RestoreTableListDetail

        The model defined in huaweicloud sdk

        :param db_name: 库名参数必传
        :type db_name: str
        :param schema_name: schema名  备份恢复到新实例和当前实例：使用DATABASE_TABLE级别恢复参数必传, 使用DATABASE类型恢复参数无效。
        :type schema_name: str
        :param table_name: 表名  备份恢复到新实例和当前实例：使用DATABASE_TABLE级别恢复参数必传, 使用DATABASE类型恢复参数无效。
        :type table_name: str
        :param new_db_name: 新库名  备份恢复到新实例和当前实例：   使用DATABASE级别恢复：需注意目标实例不存在当前一样的库名，否则无法下发。   使用DATABASE_TABLE级别恢复，不填时与源库名一致。
        :type new_db_name: str
        :param new_schema_name: 新schema_name  备份恢复到新实例和当前实例：    使用DATABASE类型恢复参数无效。   使用DATABASE_TABLE级别恢复，不填时与源schema名一致。
        :type new_schema_name: str
        :param new_table_name: 新表名  备份恢复到新实例和当前实例：   使用DATABASE类型恢复参数无效。   使用DATABASE_TABLE级别恢复，需注意目标实例里不存在当前的表名，否则无法下发。
        :type new_table_name: str
        """
        
        

        self._db_name = None
        self._schema_name = None
        self._table_name = None
        self._new_db_name = None
        self._new_schema_name = None
        self._new_table_name = None
        self.discriminator = None

        self.db_name = db_name
        if schema_name is not None:
            self.schema_name = schema_name
        if table_name is not None:
            self.table_name = table_name
        if new_db_name is not None:
            self.new_db_name = new_db_name
        if new_schema_name is not None:
            self.new_schema_name = new_schema_name
        if new_table_name is not None:
            self.new_table_name = new_table_name

    @property
    def db_name(self):
        """Gets the db_name of this RestoreTableListDetail.

        库名参数必传

        :return: The db_name of this RestoreTableListDetail.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """Sets the db_name of this RestoreTableListDetail.

        库名参数必传

        :param db_name: The db_name of this RestoreTableListDetail.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def schema_name(self):
        """Gets the schema_name of this RestoreTableListDetail.

        schema名  备份恢复到新实例和当前实例：使用DATABASE_TABLE级别恢复参数必传, 使用DATABASE类型恢复参数无效。

        :return: The schema_name of this RestoreTableListDetail.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        """Sets the schema_name of this RestoreTableListDetail.

        schema名  备份恢复到新实例和当前实例：使用DATABASE_TABLE级别恢复参数必传, 使用DATABASE类型恢复参数无效。

        :param schema_name: The schema_name of this RestoreTableListDetail.
        :type schema_name: str
        """
        self._schema_name = schema_name

    @property
    def table_name(self):
        """Gets the table_name of this RestoreTableListDetail.

        表名  备份恢复到新实例和当前实例：使用DATABASE_TABLE级别恢复参数必传, 使用DATABASE类型恢复参数无效。

        :return: The table_name of this RestoreTableListDetail.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this RestoreTableListDetail.

        表名  备份恢复到新实例和当前实例：使用DATABASE_TABLE级别恢复参数必传, 使用DATABASE类型恢复参数无效。

        :param table_name: The table_name of this RestoreTableListDetail.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def new_db_name(self):
        """Gets the new_db_name of this RestoreTableListDetail.

        新库名  备份恢复到新实例和当前实例：   使用DATABASE级别恢复：需注意目标实例不存在当前一样的库名，否则无法下发。   使用DATABASE_TABLE级别恢复，不填时与源库名一致。

        :return: The new_db_name of this RestoreTableListDetail.
        :rtype: str
        """
        return self._new_db_name

    @new_db_name.setter
    def new_db_name(self, new_db_name):
        """Sets the new_db_name of this RestoreTableListDetail.

        新库名  备份恢复到新实例和当前实例：   使用DATABASE级别恢复：需注意目标实例不存在当前一样的库名，否则无法下发。   使用DATABASE_TABLE级别恢复，不填时与源库名一致。

        :param new_db_name: The new_db_name of this RestoreTableListDetail.
        :type new_db_name: str
        """
        self._new_db_name = new_db_name

    @property
    def new_schema_name(self):
        """Gets the new_schema_name of this RestoreTableListDetail.

        新schema_name  备份恢复到新实例和当前实例：    使用DATABASE类型恢复参数无效。   使用DATABASE_TABLE级别恢复，不填时与源schema名一致。

        :return: The new_schema_name of this RestoreTableListDetail.
        :rtype: str
        """
        return self._new_schema_name

    @new_schema_name.setter
    def new_schema_name(self, new_schema_name):
        """Sets the new_schema_name of this RestoreTableListDetail.

        新schema_name  备份恢复到新实例和当前实例：    使用DATABASE类型恢复参数无效。   使用DATABASE_TABLE级别恢复，不填时与源schema名一致。

        :param new_schema_name: The new_schema_name of this RestoreTableListDetail.
        :type new_schema_name: str
        """
        self._new_schema_name = new_schema_name

    @property
    def new_table_name(self):
        """Gets the new_table_name of this RestoreTableListDetail.

        新表名  备份恢复到新实例和当前实例：   使用DATABASE类型恢复参数无效。   使用DATABASE_TABLE级别恢复，需注意目标实例里不存在当前的表名，否则无法下发。

        :return: The new_table_name of this RestoreTableListDetail.
        :rtype: str
        """
        return self._new_table_name

    @new_table_name.setter
    def new_table_name(self, new_table_name):
        """Sets the new_table_name of this RestoreTableListDetail.

        新表名  备份恢复到新实例和当前实例：   使用DATABASE类型恢复参数无效。   使用DATABASE_TABLE级别恢复，需注意目标实例里不存在当前的表名，否则无法下发。

        :param new_table_name: The new_table_name of this RestoreTableListDetail.
        :type new_table_name: str
        """
        self._new_table_name = new_table_name

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
        if not isinstance(other, RestoreTableListDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
