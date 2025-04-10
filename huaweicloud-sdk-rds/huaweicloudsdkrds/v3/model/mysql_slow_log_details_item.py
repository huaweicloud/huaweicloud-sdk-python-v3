# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MysqlSlowLogDetailsItem:

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
        'rows_sent': 'str',
        'rows_examined': 'str',
        'database': 'str',
        'users': 'str',
        'query_sample': 'str',
        'type': 'str',
        'start_time': 'str',
        'client_ip': 'str',
        'line_num': 'str'
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
        'type': 'type',
        'start_time': 'start_time',
        'client_ip': 'client_ip',
        'line_num': 'line_num'
    }

    def __init__(self, count=None, time=None, lock_time=None, rows_sent=None, rows_examined=None, database=None, users=None, query_sample=None, type=None, start_time=None, client_ip=None, line_num=None):
        r"""MysqlSlowLogDetailsItem

        The model defined in huaweicloud sdk

        :param count: 执行次数。
        :type count: str
        :param time: 执行时间。
        :type time: str
        :param lock_time: 等待锁时间。mysql支持
        :type lock_time: str
        :param rows_sent: 结果行数量。mysql支持
        :type rows_sent: str
        :param rows_examined: 扫描的行数量。mysql支持
        :type rows_examined: str
        :param database: 所属数据库。
        :type database: str
        :param users: 帐号。
        :type users: str
        :param query_sample: 执行语法。慢日志默认脱敏显示，如需明文显示，请联系客服人员添加白名单。
        :type query_sample: str
        :param type: 语句类型。
        :type type: str
        :param start_time: 发生时间，UTC时间。
        :type start_time: str
        :param client_ip: IP地址。
        :type client_ip: str
        :param line_num: 日志单行序列号。
        :type line_num: str
        """
        
        

        self._count = None
        self._time = None
        self._lock_time = None
        self._rows_sent = None
        self._rows_examined = None
        self._database = None
        self._users = None
        self._query_sample = None
        self._type = None
        self._start_time = None
        self._client_ip = None
        self._line_num = None
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
        if type is not None:
            self.type = type
        if start_time is not None:
            self.start_time = start_time
        if client_ip is not None:
            self.client_ip = client_ip
        if line_num is not None:
            self.line_num = line_num

    @property
    def count(self):
        r"""Gets the count of this MysqlSlowLogDetailsItem.

        执行次数。

        :return: The count of this MysqlSlowLogDetailsItem.
        :rtype: str
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this MysqlSlowLogDetailsItem.

        执行次数。

        :param count: The count of this MysqlSlowLogDetailsItem.
        :type count: str
        """
        self._count = count

    @property
    def time(self):
        r"""Gets the time of this MysqlSlowLogDetailsItem.

        执行时间。

        :return: The time of this MysqlSlowLogDetailsItem.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this MysqlSlowLogDetailsItem.

        执行时间。

        :param time: The time of this MysqlSlowLogDetailsItem.
        :type time: str
        """
        self._time = time

    @property
    def lock_time(self):
        r"""Gets the lock_time of this MysqlSlowLogDetailsItem.

        等待锁时间。mysql支持

        :return: The lock_time of this MysqlSlowLogDetailsItem.
        :rtype: str
        """
        return self._lock_time

    @lock_time.setter
    def lock_time(self, lock_time):
        r"""Sets the lock_time of this MysqlSlowLogDetailsItem.

        等待锁时间。mysql支持

        :param lock_time: The lock_time of this MysqlSlowLogDetailsItem.
        :type lock_time: str
        """
        self._lock_time = lock_time

    @property
    def rows_sent(self):
        r"""Gets the rows_sent of this MysqlSlowLogDetailsItem.

        结果行数量。mysql支持

        :return: The rows_sent of this MysqlSlowLogDetailsItem.
        :rtype: str
        """
        return self._rows_sent

    @rows_sent.setter
    def rows_sent(self, rows_sent):
        r"""Sets the rows_sent of this MysqlSlowLogDetailsItem.

        结果行数量。mysql支持

        :param rows_sent: The rows_sent of this MysqlSlowLogDetailsItem.
        :type rows_sent: str
        """
        self._rows_sent = rows_sent

    @property
    def rows_examined(self):
        r"""Gets the rows_examined of this MysqlSlowLogDetailsItem.

        扫描的行数量。mysql支持

        :return: The rows_examined of this MysqlSlowLogDetailsItem.
        :rtype: str
        """
        return self._rows_examined

    @rows_examined.setter
    def rows_examined(self, rows_examined):
        r"""Sets the rows_examined of this MysqlSlowLogDetailsItem.

        扫描的行数量。mysql支持

        :param rows_examined: The rows_examined of this MysqlSlowLogDetailsItem.
        :type rows_examined: str
        """
        self._rows_examined = rows_examined

    @property
    def database(self):
        r"""Gets the database of this MysqlSlowLogDetailsItem.

        所属数据库。

        :return: The database of this MysqlSlowLogDetailsItem.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        r"""Sets the database of this MysqlSlowLogDetailsItem.

        所属数据库。

        :param database: The database of this MysqlSlowLogDetailsItem.
        :type database: str
        """
        self._database = database

    @property
    def users(self):
        r"""Gets the users of this MysqlSlowLogDetailsItem.

        帐号。

        :return: The users of this MysqlSlowLogDetailsItem.
        :rtype: str
        """
        return self._users

    @users.setter
    def users(self, users):
        r"""Sets the users of this MysqlSlowLogDetailsItem.

        帐号。

        :param users: The users of this MysqlSlowLogDetailsItem.
        :type users: str
        """
        self._users = users

    @property
    def query_sample(self):
        r"""Gets the query_sample of this MysqlSlowLogDetailsItem.

        执行语法。慢日志默认脱敏显示，如需明文显示，请联系客服人员添加白名单。

        :return: The query_sample of this MysqlSlowLogDetailsItem.
        :rtype: str
        """
        return self._query_sample

    @query_sample.setter
    def query_sample(self, query_sample):
        r"""Sets the query_sample of this MysqlSlowLogDetailsItem.

        执行语法。慢日志默认脱敏显示，如需明文显示，请联系客服人员添加白名单。

        :param query_sample: The query_sample of this MysqlSlowLogDetailsItem.
        :type query_sample: str
        """
        self._query_sample = query_sample

    @property
    def type(self):
        r"""Gets the type of this MysqlSlowLogDetailsItem.

        语句类型。

        :return: The type of this MysqlSlowLogDetailsItem.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this MysqlSlowLogDetailsItem.

        语句类型。

        :param type: The type of this MysqlSlowLogDetailsItem.
        :type type: str
        """
        self._type = type

    @property
    def start_time(self):
        r"""Gets the start_time of this MysqlSlowLogDetailsItem.

        发生时间，UTC时间。

        :return: The start_time of this MysqlSlowLogDetailsItem.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this MysqlSlowLogDetailsItem.

        发生时间，UTC时间。

        :param start_time: The start_time of this MysqlSlowLogDetailsItem.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def client_ip(self):
        r"""Gets the client_ip of this MysqlSlowLogDetailsItem.

        IP地址。

        :return: The client_ip of this MysqlSlowLogDetailsItem.
        :rtype: str
        """
        return self._client_ip

    @client_ip.setter
    def client_ip(self, client_ip):
        r"""Sets the client_ip of this MysqlSlowLogDetailsItem.

        IP地址。

        :param client_ip: The client_ip of this MysqlSlowLogDetailsItem.
        :type client_ip: str
        """
        self._client_ip = client_ip

    @property
    def line_num(self):
        r"""Gets the line_num of this MysqlSlowLogDetailsItem.

        日志单行序列号。

        :return: The line_num of this MysqlSlowLogDetailsItem.
        :rtype: str
        """
        return self._line_num

    @line_num.setter
    def line_num(self, line_num):
        r"""Sets the line_num of this MysqlSlowLogDetailsItem.

        日志单行序列号。

        :param line_num: The line_num of this MysqlSlowLogDetailsItem.
        :type line_num: str
        """
        self._line_num = line_num

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
        if not isinstance(other, MysqlSlowLogDetailsItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
