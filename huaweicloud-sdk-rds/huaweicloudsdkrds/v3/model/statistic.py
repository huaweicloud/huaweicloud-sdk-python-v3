# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Statistic:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_name': 'str',
        'database': 'str',
        'query_id': 'int',
        'calls': 'int',
        'query': 'str',
        'rows': 'int',
        'can_use': 'float'
    }

    attribute_map = {
        'user_name': 'user_name',
        'database': 'database',
        'query_id': 'query_id',
        'calls': 'calls',
        'query': 'query',
        'rows': 'rows',
        'can_use': 'can_use'
    }

    def __init__(self, user_name=None, database=None, query_id=None, calls=None, query=None, rows=None, can_use=None):
        r"""Statistic

        The model defined in huaweicloud sdk

        :param user_name: 用户名称
        :type user_name: str
        :param database: 数据库名称
        :type database: str
        :param query_id: 由SQL的语法解析树计算出的内部哈希码。
        :type query_id: int
        :param calls: 调用次数
        :type calls: int
        :param query: SQL语句的文本形式。
        :type query: str
        :param rows: 扫描行数
        :type rows: int
        :param can_use: 是否可以执行sql限流
        :type can_use: float
        """
        
        

        self._user_name = None
        self._database = None
        self._query_id = None
        self._calls = None
        self._query = None
        self._rows = None
        self._can_use = None
        self.discriminator = None

        if user_name is not None:
            self.user_name = user_name
        if database is not None:
            self.database = database
        if query_id is not None:
            self.query_id = query_id
        if calls is not None:
            self.calls = calls
        if query is not None:
            self.query = query
        if rows is not None:
            self.rows = rows
        if can_use is not None:
            self.can_use = can_use

    @property
    def user_name(self):
        r"""Gets the user_name of this Statistic.

        用户名称

        :return: The user_name of this Statistic.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this Statistic.

        用户名称

        :param user_name: The user_name of this Statistic.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def database(self):
        r"""Gets the database of this Statistic.

        数据库名称

        :return: The database of this Statistic.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        r"""Sets the database of this Statistic.

        数据库名称

        :param database: The database of this Statistic.
        :type database: str
        """
        self._database = database

    @property
    def query_id(self):
        r"""Gets the query_id of this Statistic.

        由SQL的语法解析树计算出的内部哈希码。

        :return: The query_id of this Statistic.
        :rtype: int
        """
        return self._query_id

    @query_id.setter
    def query_id(self, query_id):
        r"""Sets the query_id of this Statistic.

        由SQL的语法解析树计算出的内部哈希码。

        :param query_id: The query_id of this Statistic.
        :type query_id: int
        """
        self._query_id = query_id

    @property
    def calls(self):
        r"""Gets the calls of this Statistic.

        调用次数

        :return: The calls of this Statistic.
        :rtype: int
        """
        return self._calls

    @calls.setter
    def calls(self, calls):
        r"""Sets the calls of this Statistic.

        调用次数

        :param calls: The calls of this Statistic.
        :type calls: int
        """
        self._calls = calls

    @property
    def query(self):
        r"""Gets the query of this Statistic.

        SQL语句的文本形式。

        :return: The query of this Statistic.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        r"""Sets the query of this Statistic.

        SQL语句的文本形式。

        :param query: The query of this Statistic.
        :type query: str
        """
        self._query = query

    @property
    def rows(self):
        r"""Gets the rows of this Statistic.

        扫描行数

        :return: The rows of this Statistic.
        :rtype: int
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        r"""Sets the rows of this Statistic.

        扫描行数

        :param rows: The rows of this Statistic.
        :type rows: int
        """
        self._rows = rows

    @property
    def can_use(self):
        r"""Gets the can_use of this Statistic.

        是否可以执行sql限流

        :return: The can_use of this Statistic.
        :rtype: float
        """
        return self._can_use

    @can_use.setter
    def can_use(self, can_use):
        r"""Sets the can_use of this Statistic.

        是否可以执行sql限流

        :param can_use: The can_use of this Statistic.
        :type can_use: float
        """
        self._can_use = can_use

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
        if not isinstance(other, Statistic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
