# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AuditSqlResponseSqlOperatedObjInfo:

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
        'object_type': 'str',
        'schema_name': 'str',
        'sql_type': 'str',
        'sys_name': 'str',
        'table_name': 'str'
    }

    attribute_map = {
        'column_name': 'column_name',
        'object_type': 'object_type',
        'schema_name': 'schema_name',
        'sql_type': 'sql_type',
        'sys_name': 'sys_name',
        'table_name': 'table_name'
    }

    def __init__(self, column_name=None, object_type=None, schema_name=None, sql_type=None, sys_name=None, table_name=None):
        r"""AuditSqlResponseSqlOperatedObjInfo

        The model defined in huaweicloud sdk

        :param column_name: 列名
        :type column_name: str
        :param object_type: 操作对象类型
        :type object_type: str
        :param schema_name: schema名称
        :type schema_name: str
        :param sql_type: sql类型
        :type sql_type: str
        :param sys_name: 系统名称
        :type sys_name: str
        :param table_name: 表名
        :type table_name: str
        """
        
        

        self._column_name = None
        self._object_type = None
        self._schema_name = None
        self._sql_type = None
        self._sys_name = None
        self._table_name = None
        self.discriminator = None

        if column_name is not None:
            self.column_name = column_name
        if object_type is not None:
            self.object_type = object_type
        if schema_name is not None:
            self.schema_name = schema_name
        if sql_type is not None:
            self.sql_type = sql_type
        if sys_name is not None:
            self.sys_name = sys_name
        if table_name is not None:
            self.table_name = table_name

    @property
    def column_name(self):
        r"""Gets the column_name of this AuditSqlResponseSqlOperatedObjInfo.

        列名

        :return: The column_name of this AuditSqlResponseSqlOperatedObjInfo.
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        r"""Sets the column_name of this AuditSqlResponseSqlOperatedObjInfo.

        列名

        :param column_name: The column_name of this AuditSqlResponseSqlOperatedObjInfo.
        :type column_name: str
        """
        self._column_name = column_name

    @property
    def object_type(self):
        r"""Gets the object_type of this AuditSqlResponseSqlOperatedObjInfo.

        操作对象类型

        :return: The object_type of this AuditSqlResponseSqlOperatedObjInfo.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        r"""Sets the object_type of this AuditSqlResponseSqlOperatedObjInfo.

        操作对象类型

        :param object_type: The object_type of this AuditSqlResponseSqlOperatedObjInfo.
        :type object_type: str
        """
        self._object_type = object_type

    @property
    def schema_name(self):
        r"""Gets the schema_name of this AuditSqlResponseSqlOperatedObjInfo.

        schema名称

        :return: The schema_name of this AuditSqlResponseSqlOperatedObjInfo.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        r"""Sets the schema_name of this AuditSqlResponseSqlOperatedObjInfo.

        schema名称

        :param schema_name: The schema_name of this AuditSqlResponseSqlOperatedObjInfo.
        :type schema_name: str
        """
        self._schema_name = schema_name

    @property
    def sql_type(self):
        r"""Gets the sql_type of this AuditSqlResponseSqlOperatedObjInfo.

        sql类型

        :return: The sql_type of this AuditSqlResponseSqlOperatedObjInfo.
        :rtype: str
        """
        return self._sql_type

    @sql_type.setter
    def sql_type(self, sql_type):
        r"""Sets the sql_type of this AuditSqlResponseSqlOperatedObjInfo.

        sql类型

        :param sql_type: The sql_type of this AuditSqlResponseSqlOperatedObjInfo.
        :type sql_type: str
        """
        self._sql_type = sql_type

    @property
    def sys_name(self):
        r"""Gets the sys_name of this AuditSqlResponseSqlOperatedObjInfo.

        系统名称

        :return: The sys_name of this AuditSqlResponseSqlOperatedObjInfo.
        :rtype: str
        """
        return self._sys_name

    @sys_name.setter
    def sys_name(self, sys_name):
        r"""Sets the sys_name of this AuditSqlResponseSqlOperatedObjInfo.

        系统名称

        :param sys_name: The sys_name of this AuditSqlResponseSqlOperatedObjInfo.
        :type sys_name: str
        """
        self._sys_name = sys_name

    @property
    def table_name(self):
        r"""Gets the table_name of this AuditSqlResponseSqlOperatedObjInfo.

        表名

        :return: The table_name of this AuditSqlResponseSqlOperatedObjInfo.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this AuditSqlResponseSqlOperatedObjInfo.

        表名

        :param table_name: The table_name of this AuditSqlResponseSqlOperatedObjInfo.
        :type table_name: str
        """
        self._table_name = table_name

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
        if not isinstance(other, AuditSqlResponseSqlOperatedObjInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
