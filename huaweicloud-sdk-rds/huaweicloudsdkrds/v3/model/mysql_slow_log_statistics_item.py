# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MysqlSlowLogStatisticsItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'str',
        'time': 'str',
        'lock_time': 'str',
        'rows_sent': 'int',
        'rows_examined': 'int',
        'database': 'str',
        'users': 'str',
        'query_sample': 'str',
        'client_ip': 'str',
        'type': 'str'
    }

    attribute_map = {
        'count': 'count',
        'time': 'time',
        'lock_time': 'lock_time',
        'rows_sent': 'rows_sent',
        'rows_examined': 'rows_examined',
        'database': 'database',
        'users': 'users',
        'query_sample': 'query_sample',
        'client_ip': 'client_ip',
        'type': 'type'
    }

    def __init__(self, count=None, time=None, lock_time=None, rows_sent=None, rows_examined=None, database=None, users=None, query_sample=None, client_ip=None, type=None):
        """MysqlSlowLogStatisticsItem

        The model defined in huaweicloud sdk

        :param count: 执行次数。
        :type count: str
        :param time: 执行时间。
        :type time: str
        :param lock_time: 等待锁时间。mysql支持
        :type lock_time: str
        :param rows_sent: 结果行数量。mysql支持
        :type rows_sent: int
        :param rows_examined: 扫描的行数量。mysql支持
        :type rows_examined: int
        :param database: 所属数据库。
        :type database: str
        :param users: 帐号。
        :type users: str
        :param query_sample: 执行语法。
        :type query_sample: str
        :param client_ip: IP地址。
        :type client_ip: str
        :param type: 语句类型。
        :type type: str
        """
        
        

        self._count = None
        self._time = None
        self._lock_time = None
        self._rows_sent = None
        self._rows_examined = None
        self._database = None
        self._users = None
        self._query_sample = None
        self._client_ip = None
        self._type = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if time is not None:
            self.time = time
        if lock_time is not None:
            self.lock_time = lock_time
        if rows_sent is not None:
            self.rows_sent = rows_sent
        if rows_examined is not None:
            self.rows_examined = rows_examined
        if database is not None:
            self.database = database
        if users is not None:
            self.users = users
        if query_sample is not None:
            self.query_sample = query_sample
        if client_ip is not None:
            self.client_ip = client_ip
        if type is not None:
            self.type = type

    @property
    def count(self):
        """Gets the count of this MysqlSlowLogStatisticsItem.

        执行次数。

        :return: The count of this MysqlSlowLogStatisticsItem.
        :rtype: str
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this MysqlSlowLogStatisticsItem.

        执行次数。

        :param count: The count of this MysqlSlowLogStatisticsItem.
        :type count: str
        """
        self._count = count

    @property
    def time(self):
        """Gets the time of this MysqlSlowLogStatisticsItem.

        执行时间。

        :return: The time of this MysqlSlowLogStatisticsItem.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this MysqlSlowLogStatisticsItem.

        执行时间。

        :param time: The time of this MysqlSlowLogStatisticsItem.
        :type time: str
        """
        self._time = time

    @property
    def lock_time(self):
        """Gets the lock_time of this MysqlSlowLogStatisticsItem.

        等待锁时间。mysql支持

        :return: The lock_time of this MysqlSlowLogStatisticsItem.
        :rtype: str
        """
        return self._lock_time

    @lock_time.setter
    def lock_time(self, lock_time):
        """Sets the lock_time of this MysqlSlowLogStatisticsItem.

        等待锁时间。mysql支持

        :param lock_time: The lock_time of this MysqlSlowLogStatisticsItem.
        :type lock_time: str
        """
        self._lock_time = lock_time

    @property
    def rows_sent(self):
        """Gets the rows_sent of this MysqlSlowLogStatisticsItem.

        结果行数量。mysql支持

        :return: The rows_sent of this MysqlSlowLogStatisticsItem.
        :rtype: int
        """
        return self._rows_sent

    @rows_sent.setter
    def rows_sent(self, rows_sent):
        """Sets the rows_sent of this MysqlSlowLogStatisticsItem.

        结果行数量。mysql支持

        :param rows_sent: The rows_sent of this MysqlSlowLogStatisticsItem.
        :type rows_sent: int
        """
        self._rows_sent = rows_sent

    @property
    def rows_examined(self):
        """Gets the rows_examined of this MysqlSlowLogStatisticsItem.

        扫描的行数量。mysql支持

        :return: The rows_examined of this MysqlSlowLogStatisticsItem.
        :rtype: int
        """
        return self._rows_examined

    @rows_examined.setter
    def rows_examined(self, rows_examined):
        """Sets the rows_examined of this MysqlSlowLogStatisticsItem.

        扫描的行数量。mysql支持

        :param rows_examined: The rows_examined of this MysqlSlowLogStatisticsItem.
        :type rows_examined: int
        """
        self._rows_examined = rows_examined

    @property
    def database(self):
        """Gets the database of this MysqlSlowLogStatisticsItem.

        所属数据库。

        :return: The database of this MysqlSlowLogStatisticsItem.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        """Sets the database of this MysqlSlowLogStatisticsItem.

        所属数据库。

        :param database: The database of this MysqlSlowLogStatisticsItem.
        :type database: str
        """
        self._database = database

    @property
    def users(self):
        """Gets the users of this MysqlSlowLogStatisticsItem.

        帐号。

        :return: The users of this MysqlSlowLogStatisticsItem.
        :rtype: str
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this MysqlSlowLogStatisticsItem.

        帐号。

        :param users: The users of this MysqlSlowLogStatisticsItem.
        :type users: str
        """
        self._users = users

    @property
    def query_sample(self):
        """Gets the query_sample of this MysqlSlowLogStatisticsItem.

        执行语法。

        :return: The query_sample of this MysqlSlowLogStatisticsItem.
        :rtype: str
        """
        return self._query_sample

    @query_sample.setter
    def query_sample(self, query_sample):
        """Sets the query_sample of this MysqlSlowLogStatisticsItem.

        执行语法。

        :param query_sample: The query_sample of this MysqlSlowLogStatisticsItem.
        :type query_sample: str
        """
        self._query_sample = query_sample

    @property
    def client_ip(self):
        """Gets the client_ip of this MysqlSlowLogStatisticsItem.

        IP地址。

        :return: The client_ip of this MysqlSlowLogStatisticsItem.
        :rtype: str
        """
        return self._client_ip

    @client_ip.setter
    def client_ip(self, client_ip):
        """Sets the client_ip of this MysqlSlowLogStatisticsItem.

        IP地址。

        :param client_ip: The client_ip of this MysqlSlowLogStatisticsItem.
        :type client_ip: str
        """
        self._client_ip = client_ip

    @property
    def type(self):
        """Gets the type of this MysqlSlowLogStatisticsItem.

        语句类型。

        :return: The type of this MysqlSlowLogStatisticsItem.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MysqlSlowLogStatisticsItem.

        语句类型。

        :param type: The type of this MysqlSlowLogStatisticsItem.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, MysqlSlowLogStatisticsItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
