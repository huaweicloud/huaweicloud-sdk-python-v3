# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DirtyData:

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
        'error_sql': 'str',
        'error_time': 'str',
        'error_msg': 'str'
    }

    attribute_map = {
        'db_name': 'db_name',
        'schema_name': 'schema_name',
        'table_name': 'table_name',
        'error_sql': 'error_sql',
        'error_time': 'error_time',
        'error_msg': 'error_msg'
    }

    def __init__(self, db_name=None, schema_name=None, table_name=None, error_sql=None, error_time=None, error_msg=None):
        r"""DirtyData

        The model defined in huaweicloud sdk

        :param db_name: 数据库名称。
        :type db_name: str
        :param schema_name: 模式名称。
        :type schema_name: str
        :param table_name: 表名称。
        :type table_name: str
        :param error_sql: 异常SQL。
        :type error_sql: str
        :param error_time: 发生异常时间，UTC时间，例如：2023-06-10T03:01:52Z
        :type error_time: str
        :param error_msg: 异常信息。
        :type error_msg: str
        """
        
        

        self._db_name = None
        self._schema_name = None
        self._table_name = None
        self._error_sql = None
        self._error_time = None
        self._error_msg = None
        self.discriminator = None

        if db_name is not None:
            self.db_name = db_name
        if schema_name is not None:
            self.schema_name = schema_name
        if table_name is not None:
            self.table_name = table_name
        if error_sql is not None:
            self.error_sql = error_sql
        if error_time is not None:
            self.error_time = error_time
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def db_name(self):
        r"""Gets the db_name of this DirtyData.

        数据库名称。

        :return: The db_name of this DirtyData.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this DirtyData.

        数据库名称。

        :param db_name: The db_name of this DirtyData.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def schema_name(self):
        r"""Gets the schema_name of this DirtyData.

        模式名称。

        :return: The schema_name of this DirtyData.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        r"""Sets the schema_name of this DirtyData.

        模式名称。

        :param schema_name: The schema_name of this DirtyData.
        :type schema_name: str
        """
        self._schema_name = schema_name

    @property
    def table_name(self):
        r"""Gets the table_name of this DirtyData.

        表名称。

        :return: The table_name of this DirtyData.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this DirtyData.

        表名称。

        :param table_name: The table_name of this DirtyData.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def error_sql(self):
        r"""Gets the error_sql of this DirtyData.

        异常SQL。

        :return: The error_sql of this DirtyData.
        :rtype: str
        """
        return self._error_sql

    @error_sql.setter
    def error_sql(self, error_sql):
        r"""Sets the error_sql of this DirtyData.

        异常SQL。

        :param error_sql: The error_sql of this DirtyData.
        :type error_sql: str
        """
        self._error_sql = error_sql

    @property
    def error_time(self):
        r"""Gets the error_time of this DirtyData.

        发生异常时间，UTC时间，例如：2023-06-10T03:01:52Z

        :return: The error_time of this DirtyData.
        :rtype: str
        """
        return self._error_time

    @error_time.setter
    def error_time(self, error_time):
        r"""Sets the error_time of this DirtyData.

        发生异常时间，UTC时间，例如：2023-06-10T03:01:52Z

        :param error_time: The error_time of this DirtyData.
        :type error_time: str
        """
        self._error_time = error_time

    @property
    def error_msg(self):
        r"""Gets the error_msg of this DirtyData.

        异常信息。

        :return: The error_msg of this DirtyData.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this DirtyData.

        异常信息。

        :param error_msg: The error_msg of this DirtyData.
        :type error_msg: str
        """
        self._error_msg = error_msg

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
        if not isinstance(other, DirtyData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
