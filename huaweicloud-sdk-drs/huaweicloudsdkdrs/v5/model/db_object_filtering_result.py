# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DbObjectFilteringResult:

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
        'is_success': 'bool',
        'message': 'str'
    }

    attribute_map = {
        'db_name': 'db_name',
        'schema_name': 'schema_name',
        'table_name': 'table_name',
        'is_success': 'is_success',
        'message': 'message'
    }

    def __init__(self, db_name=None, schema_name=None, table_name=None, is_success=None, message=None):
        """DbObjectFilteringResult

        The model defined in huaweicloud sdk

        :param db_name: 数据库库名。
        :type db_name: str
        :param schema_name: 数据库Schema名称。
        :type schema_name: str
        :param table_name: 数据库表名称。
        :type table_name: str
        :param is_success: 数据过滤校验结果。
        :type is_success: bool
        :param message: 当数据过滤校验结果是false，返回校验失败的原因。
        :type message: str
        """
        
        

        self._db_name = None
        self._schema_name = None
        self._table_name = None
        self._is_success = None
        self._message = None
        self.discriminator = None

        if db_name is not None:
            self.db_name = db_name
        if schema_name is not None:
            self.schema_name = schema_name
        if table_name is not None:
            self.table_name = table_name
        if is_success is not None:
            self.is_success = is_success
        if message is not None:
            self.message = message

    @property
    def db_name(self):
        """Gets the db_name of this DbObjectFilteringResult.

        数据库库名。

        :return: The db_name of this DbObjectFilteringResult.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """Sets the db_name of this DbObjectFilteringResult.

        数据库库名。

        :param db_name: The db_name of this DbObjectFilteringResult.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def schema_name(self):
        """Gets the schema_name of this DbObjectFilteringResult.

        数据库Schema名称。

        :return: The schema_name of this DbObjectFilteringResult.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        """Sets the schema_name of this DbObjectFilteringResult.

        数据库Schema名称。

        :param schema_name: The schema_name of this DbObjectFilteringResult.
        :type schema_name: str
        """
        self._schema_name = schema_name

    @property
    def table_name(self):
        """Gets the table_name of this DbObjectFilteringResult.

        数据库表名称。

        :return: The table_name of this DbObjectFilteringResult.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this DbObjectFilteringResult.

        数据库表名称。

        :param table_name: The table_name of this DbObjectFilteringResult.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def is_success(self):
        """Gets the is_success of this DbObjectFilteringResult.

        数据过滤校验结果。

        :return: The is_success of this DbObjectFilteringResult.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        """Sets the is_success of this DbObjectFilteringResult.

        数据过滤校验结果。

        :param is_success: The is_success of this DbObjectFilteringResult.
        :type is_success: bool
        """
        self._is_success = is_success

    @property
    def message(self):
        """Gets the message of this DbObjectFilteringResult.

        当数据过滤校验结果是false，返回校验失败的原因。

        :return: The message of this DbObjectFilteringResult.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this DbObjectFilteringResult.

        当数据过滤校验结果是false，返回校验失败的原因。

        :param message: The message of this DbObjectFilteringResult.
        :type message: str
        """
        self._message = message

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
        if not isinstance(other, DbObjectFilteringResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
