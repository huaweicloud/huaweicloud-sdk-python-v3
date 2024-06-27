# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChSlowLogDetailResponseSlowLogList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_id': 'str',
        'time': 'str',
        'lock_time': 'str',
        'rows_sent': 'int',
        'rows_examined': 'int',
        'database': 'str',
        'users': 'str',
        'query_sample': 'str',
        'type': 'str',
        'client_ip': 'str',
        'start_time': 'str',
        'line_num': 'str',
        'count': 'str'
    }

    attribute_map = {
        'node_id': 'node_id',
        'time': 'time',
        'lock_time': 'lock_time',
        'rows_sent': 'rows_sent',
        'rows_examined': 'rows_examined',
        'database': 'database',
        'users': 'users',
        'query_sample': 'query_sample',
        'type': 'type',
        'client_ip': 'client_ip',
        'start_time': 'start_time',
        'line_num': 'line_num',
        'count': 'count'
    }

    def __init__(self, node_id=None, time=None, lock_time=None, rows_sent=None, rows_examined=None, database=None, users=None, query_sample=None, type=None, client_ip=None, start_time=None, line_num=None, count=None):
        """ChSlowLogDetailResponseSlowLogList

        The model defined in huaweicloud sdk

        :param node_id: ClickHouse实例节点ID。
        :type node_id: str
        :param time: 数据库语句执行时间。
        :type time: str
        :param lock_time: 数据库语句等待锁时间。
        :type lock_time: str
        :param rows_sent: 数据库语句执行结果行数。
        :type rows_sent: int
        :param rows_examined: 数据库语句扫描行数。
        :type rows_examined: int
        :param database: 所属数据库名。
        :type database: str
        :param users: 执行语句账号。
        :type users: str
        :param query_sample: 数据库执行语句。
        :type query_sample: str
        :param type: 数据库语句类型。
        :type type: str
        :param client_ip: IP地址。
        :type client_ip: str
        :param start_time: 数据库语句发生时间。
        :type start_time: str
        :param line_num: 日志单行序列号，第一次查询时不需要此参数，后续分页查询时需要使用，可从上次查询的返回信息中获取。
        :type line_num: str
        :param count: 慢日志数量。
        :type count: str
        """
        
        

        self._node_id = None
        self._time = None
        self._lock_time = None
        self._rows_sent = None
        self._rows_examined = None
        self._database = None
        self._users = None
        self._query_sample = None
        self._type = None
        self._client_ip = None
        self._start_time = None
        self._line_num = None
        self._count = None
        self.discriminator = None

        self.node_id = node_id
        self.time = time
        self.lock_time = lock_time
        self.rows_sent = rows_sent
        self.rows_examined = rows_examined
        self.database = database
        self.users = users
        self.query_sample = query_sample
        self.type = type
        self.client_ip = client_ip
        self.start_time = start_time
        self.line_num = line_num
        self.count = count

    @property
    def node_id(self):
        """Gets the node_id of this ChSlowLogDetailResponseSlowLogList.

        ClickHouse实例节点ID。

        :return: The node_id of this ChSlowLogDetailResponseSlowLogList.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this ChSlowLogDetailResponseSlowLogList.

        ClickHouse实例节点ID。

        :param node_id: The node_id of this ChSlowLogDetailResponseSlowLogList.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def time(self):
        """Gets the time of this ChSlowLogDetailResponseSlowLogList.

        数据库语句执行时间。

        :return: The time of this ChSlowLogDetailResponseSlowLogList.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this ChSlowLogDetailResponseSlowLogList.

        数据库语句执行时间。

        :param time: The time of this ChSlowLogDetailResponseSlowLogList.
        :type time: str
        """
        self._time = time

    @property
    def lock_time(self):
        """Gets the lock_time of this ChSlowLogDetailResponseSlowLogList.

        数据库语句等待锁时间。

        :return: The lock_time of this ChSlowLogDetailResponseSlowLogList.
        :rtype: str
        """
        return self._lock_time

    @lock_time.setter
    def lock_time(self, lock_time):
        """Sets the lock_time of this ChSlowLogDetailResponseSlowLogList.

        数据库语句等待锁时间。

        :param lock_time: The lock_time of this ChSlowLogDetailResponseSlowLogList.
        :type lock_time: str
        """
        self._lock_time = lock_time

    @property
    def rows_sent(self):
        """Gets the rows_sent of this ChSlowLogDetailResponseSlowLogList.

        数据库语句执行结果行数。

        :return: The rows_sent of this ChSlowLogDetailResponseSlowLogList.
        :rtype: int
        """
        return self._rows_sent

    @rows_sent.setter
    def rows_sent(self, rows_sent):
        """Sets the rows_sent of this ChSlowLogDetailResponseSlowLogList.

        数据库语句执行结果行数。

        :param rows_sent: The rows_sent of this ChSlowLogDetailResponseSlowLogList.
        :type rows_sent: int
        """
        self._rows_sent = rows_sent

    @property
    def rows_examined(self):
        """Gets the rows_examined of this ChSlowLogDetailResponseSlowLogList.

        数据库语句扫描行数。

        :return: The rows_examined of this ChSlowLogDetailResponseSlowLogList.
        :rtype: int
        """
        return self._rows_examined

    @rows_examined.setter
    def rows_examined(self, rows_examined):
        """Sets the rows_examined of this ChSlowLogDetailResponseSlowLogList.

        数据库语句扫描行数。

        :param rows_examined: The rows_examined of this ChSlowLogDetailResponseSlowLogList.
        :type rows_examined: int
        """
        self._rows_examined = rows_examined

    @property
    def database(self):
        """Gets the database of this ChSlowLogDetailResponseSlowLogList.

        所属数据库名。

        :return: The database of this ChSlowLogDetailResponseSlowLogList.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        """Sets the database of this ChSlowLogDetailResponseSlowLogList.

        所属数据库名。

        :param database: The database of this ChSlowLogDetailResponseSlowLogList.
        :type database: str
        """
        self._database = database

    @property
    def users(self):
        """Gets the users of this ChSlowLogDetailResponseSlowLogList.

        执行语句账号。

        :return: The users of this ChSlowLogDetailResponseSlowLogList.
        :rtype: str
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this ChSlowLogDetailResponseSlowLogList.

        执行语句账号。

        :param users: The users of this ChSlowLogDetailResponseSlowLogList.
        :type users: str
        """
        self._users = users

    @property
    def query_sample(self):
        """Gets the query_sample of this ChSlowLogDetailResponseSlowLogList.

        数据库执行语句。

        :return: The query_sample of this ChSlowLogDetailResponseSlowLogList.
        :rtype: str
        """
        return self._query_sample

    @query_sample.setter
    def query_sample(self, query_sample):
        """Sets the query_sample of this ChSlowLogDetailResponseSlowLogList.

        数据库执行语句。

        :param query_sample: The query_sample of this ChSlowLogDetailResponseSlowLogList.
        :type query_sample: str
        """
        self._query_sample = query_sample

    @property
    def type(self):
        """Gets the type of this ChSlowLogDetailResponseSlowLogList.

        数据库语句类型。

        :return: The type of this ChSlowLogDetailResponseSlowLogList.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ChSlowLogDetailResponseSlowLogList.

        数据库语句类型。

        :param type: The type of this ChSlowLogDetailResponseSlowLogList.
        :type type: str
        """
        self._type = type

    @property
    def client_ip(self):
        """Gets the client_ip of this ChSlowLogDetailResponseSlowLogList.

        IP地址。

        :return: The client_ip of this ChSlowLogDetailResponseSlowLogList.
        :rtype: str
        """
        return self._client_ip

    @client_ip.setter
    def client_ip(self, client_ip):
        """Sets the client_ip of this ChSlowLogDetailResponseSlowLogList.

        IP地址。

        :param client_ip: The client_ip of this ChSlowLogDetailResponseSlowLogList.
        :type client_ip: str
        """
        self._client_ip = client_ip

    @property
    def start_time(self):
        """Gets the start_time of this ChSlowLogDetailResponseSlowLogList.

        数据库语句发生时间。

        :return: The start_time of this ChSlowLogDetailResponseSlowLogList.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ChSlowLogDetailResponseSlowLogList.

        数据库语句发生时间。

        :param start_time: The start_time of this ChSlowLogDetailResponseSlowLogList.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def line_num(self):
        """Gets the line_num of this ChSlowLogDetailResponseSlowLogList.

        日志单行序列号，第一次查询时不需要此参数，后续分页查询时需要使用，可从上次查询的返回信息中获取。

        :return: The line_num of this ChSlowLogDetailResponseSlowLogList.
        :rtype: str
        """
        return self._line_num

    @line_num.setter
    def line_num(self, line_num):
        """Sets the line_num of this ChSlowLogDetailResponseSlowLogList.

        日志单行序列号，第一次查询时不需要此参数，后续分页查询时需要使用，可从上次查询的返回信息中获取。

        :param line_num: The line_num of this ChSlowLogDetailResponseSlowLogList.
        :type line_num: str
        """
        self._line_num = line_num

    @property
    def count(self):
        """Gets the count of this ChSlowLogDetailResponseSlowLogList.

        慢日志数量。

        :return: The count of this ChSlowLogDetailResponseSlowLogList.
        :rtype: str
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ChSlowLogDetailResponseSlowLogList.

        慢日志数量。

        :param count: The count of this ChSlowLogDetailResponseSlowLogList.
        :type count: str
        """
        self._count = count

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
        if not isinstance(other, ChSlowLogDetailResponseSlowLogList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
