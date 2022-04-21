# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SlowLog:

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
        'client_ip': 'str'
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
        'client_ip': 'client_ip'
    }

    def __init__(self, count=None, time=None, lock_time=None, rows_sent=None, rows_examined=None, database=None, users=None, query_sample=None, type=None, start_time=None, client_ip=None):
        """SlowLog

        The model defined in huaweicloud sdk

        :param count: 执行次数。
        :type count: str
        :param time: 平均执行时间。
        :type time: str
        :param lock_time: 平均等待锁时间。
        :type lock_time: str
        :param rows_sent: 平均结果行数量。
        :type rows_sent: str
        :param rows_examined: 平均扫描的行数量。
        :type rows_examined: str
        :param database: 所属数据库。
        :type database: str
        :param users: 帐号。
        :type users: str
        :param query_sample: 执行语法。
        :type query_sample: str
        :param type: 语句类型。
        :type type: str
        :param start_time: 发生时间，UTC时间。
        :type start_time: str
        :param client_ip: IP地址。
        :type client_ip: str
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
        self.discriminator = None

        self.count = count
        self.time = time
        self.lock_time = lock_time
        self.rows_sent = rows_sent
        self.rows_examined = rows_examined
        self.database = database
        self.users = users
        self.query_sample = query_sample
        self.type = type
        self.start_time = start_time
        self.client_ip = client_ip

    @property
    def count(self):
        """Gets the count of this SlowLog.

        执行次数。

        :return: The count of this SlowLog.
        :rtype: str
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this SlowLog.

        执行次数。

        :param count: The count of this SlowLog.
        :type count: str
        """
        self._count = count

    @property
    def time(self):
        """Gets the time of this SlowLog.

        平均执行时间。

        :return: The time of this SlowLog.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this SlowLog.

        平均执行时间。

        :param time: The time of this SlowLog.
        :type time: str
        """
        self._time = time

    @property
    def lock_time(self):
        """Gets the lock_time of this SlowLog.

        平均等待锁时间。

        :return: The lock_time of this SlowLog.
        :rtype: str
        """
        return self._lock_time

    @lock_time.setter
    def lock_time(self, lock_time):
        """Sets the lock_time of this SlowLog.

        平均等待锁时间。

        :param lock_time: The lock_time of this SlowLog.
        :type lock_time: str
        """
        self._lock_time = lock_time

    @property
    def rows_sent(self):
        """Gets the rows_sent of this SlowLog.

        平均结果行数量。

        :return: The rows_sent of this SlowLog.
        :rtype: str
        """
        return self._rows_sent

    @rows_sent.setter
    def rows_sent(self, rows_sent):
        """Sets the rows_sent of this SlowLog.

        平均结果行数量。

        :param rows_sent: The rows_sent of this SlowLog.
        :type rows_sent: str
        """
        self._rows_sent = rows_sent

    @property
    def rows_examined(self):
        """Gets the rows_examined of this SlowLog.

        平均扫描的行数量。

        :return: The rows_examined of this SlowLog.
        :rtype: str
        """
        return self._rows_examined

    @rows_examined.setter
    def rows_examined(self, rows_examined):
        """Sets the rows_examined of this SlowLog.

        平均扫描的行数量。

        :param rows_examined: The rows_examined of this SlowLog.
        :type rows_examined: str
        """
        self._rows_examined = rows_examined

    @property
    def database(self):
        """Gets the database of this SlowLog.

        所属数据库。

        :return: The database of this SlowLog.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        """Sets the database of this SlowLog.

        所属数据库。

        :param database: The database of this SlowLog.
        :type database: str
        """
        self._database = database

    @property
    def users(self):
        """Gets the users of this SlowLog.

        帐号。

        :return: The users of this SlowLog.
        :rtype: str
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this SlowLog.

        帐号。

        :param users: The users of this SlowLog.
        :type users: str
        """
        self._users = users

    @property
    def query_sample(self):
        """Gets the query_sample of this SlowLog.

        执行语法。

        :return: The query_sample of this SlowLog.
        :rtype: str
        """
        return self._query_sample

    @query_sample.setter
    def query_sample(self, query_sample):
        """Sets the query_sample of this SlowLog.

        执行语法。

        :param query_sample: The query_sample of this SlowLog.
        :type query_sample: str
        """
        self._query_sample = query_sample

    @property
    def type(self):
        """Gets the type of this SlowLog.

        语句类型。

        :return: The type of this SlowLog.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SlowLog.

        语句类型。

        :param type: The type of this SlowLog.
        :type type: str
        """
        self._type = type

    @property
    def start_time(self):
        """Gets the start_time of this SlowLog.

        发生时间，UTC时间。

        :return: The start_time of this SlowLog.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this SlowLog.

        发生时间，UTC时间。

        :param start_time: The start_time of this SlowLog.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def client_ip(self):
        """Gets the client_ip of this SlowLog.

        IP地址。

        :return: The client_ip of this SlowLog.
        :rtype: str
        """
        return self._client_ip

    @client_ip.setter
    def client_ip(self, client_ip):
        """Sets the client_ip of this SlowLog.

        IP地址。

        :param client_ip: The client_ip of this SlowLog.
        :type client_ip: str
        """
        self._client_ip = client_ip

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
        if not isinstance(other, SlowLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
