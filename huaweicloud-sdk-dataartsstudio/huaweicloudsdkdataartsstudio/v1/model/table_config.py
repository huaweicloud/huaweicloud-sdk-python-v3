# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TableConfig:

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
        'schema': 'str',
        'table': 'str',
        'is_exist': 'bool'
    }

    attribute_map = {
        'database': 'database',
        'schema': 'schema',
        'table': 'table',
        'is_exist': 'is_exist'
    }

    def __init__(self, database=None, schema=None, table=None, is_exist=None):
        r"""TableConfig

        The model defined in huaweicloud sdk

        :param database: 数据库名称。
        :type database: str
        :param schema: schema名称。
        :type schema: str
        :param table: 表名称。
        :type table: str
        :param is_exist: 是否存在。
        :type is_exist: bool
        """
        
        

        self._database = None
        self._schema = None
        self._table = None
        self._is_exist = None
        self.discriminator = None

        if database is not None:
            self.database = database
        if schema is not None:
            self.schema = schema
        if table is not None:
            self.table = table
        if is_exist is not None:
            self.is_exist = is_exist

    @property
    def database(self):
        r"""Gets the database of this TableConfig.

        数据库名称。

        :return: The database of this TableConfig.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        r"""Sets the database of this TableConfig.

        数据库名称。

        :param database: The database of this TableConfig.
        :type database: str
        """
        self._database = database

    @property
    def schema(self):
        r"""Gets the schema of this TableConfig.

        schema名称。

        :return: The schema of this TableConfig.
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        r"""Sets the schema of this TableConfig.

        schema名称。

        :param schema: The schema of this TableConfig.
        :type schema: str
        """
        self._schema = schema

    @property
    def table(self):
        r"""Gets the table of this TableConfig.

        表名称。

        :return: The table of this TableConfig.
        :rtype: str
        """
        return self._table

    @table.setter
    def table(self, table):
        r"""Sets the table of this TableConfig.

        表名称。

        :param table: The table of this TableConfig.
        :type table: str
        """
        self._table = table

    @property
    def is_exist(self):
        r"""Gets the is_exist of this TableConfig.

        是否存在。

        :return: The is_exist of this TableConfig.
        :rtype: bool
        """
        return self._is_exist

    @is_exist.setter
    def is_exist(self, is_exist):
        r"""Sets the is_exist of this TableConfig.

        是否存在。

        :param is_exist: The is_exist of this TableConfig.
        :type is_exist: bool
        """
        self._is_exist = is_exist

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
        if not isinstance(other, TableConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
