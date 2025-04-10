# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSlowLogStatisticsItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'client_ip': 'str',
        'count': 'str',
        'database': 'str',
        'lock_time': 'str',
        'node_id': 'str',
        'query_sample': 'str',
        'rows_examined': 'int',
        'rows_sent': 'int',
        'time': 'str',
        'type': 'str',
        'users': 'str'
    }

    attribute_map = {
        'client_ip': 'client_ip',
        'count': 'count',
        'database': 'database',
        'lock_time': 'lock_time',
        'node_id': 'node_id',
        'query_sample': 'query_sample',
        'rows_examined': 'rows_examined',
        'rows_sent': 'rows_sent',
        'time': 'time',
        'type': 'type',
        'users': 'users'
    }

    def __init__(self, client_ip=None, count=None, database=None, lock_time=None, node_id=None, query_sample=None, rows_examined=None, rows_sent=None, time=None, type=None, users=None):
        r"""ShowSlowLogStatisticsItem

        The model defined in huaweicloud sdk

        :param client_ip: IP地址。
        :type client_ip: str
        :param count: 执行次数。
        :type count: str
        :param database: 所属数据库。
        :type database: str
        :param lock_time: 平均等待锁时间。
        :type lock_time: str
        :param node_id: 节点ID。
        :type node_id: str
        :param query_sample: 执行语法。
        :type query_sample: str
        :param rows_examined: 平均扫描的行数量。
        :type rows_examined: int
        :param rows_sent: 平均结果行统计数量。
        :type rows_sent: int
        :param time: 平均执行时间。
        :type time: str
        :param type: 语句类型。
        :type type: str
        :param users: 账号。
        :type users: str
        """
        
        

        self._client_ip = None
        self._count = None
        self._database = None
        self._lock_time = None
        self._node_id = None
        self._query_sample = None
        self._rows_examined = None
        self._rows_sent = None
        self._time = None
        self._type = None
        self._users = None
        self.discriminator = None

        if client_ip is not None:
            self.client_ip = client_ip
        if count is not None:
            self.count = count
        if database is not None:
            self.database = database
        if lock_time is not None:
            self.lock_time = lock_time
        if node_id is not None:
            self.node_id = node_id
        if query_sample is not None:
            self.query_sample = query_sample
        if rows_examined is not None:
            self.rows_examined = rows_examined
        if rows_sent is not None:
            self.rows_sent = rows_sent
        if time is not None:
            self.time = time
        if type is not None:
            self.type = type
        if users is not None:
            self.users = users

    @property
    def client_ip(self):
        r"""Gets the client_ip of this ShowSlowLogStatisticsItem.

        IP地址。

        :return: The client_ip of this ShowSlowLogStatisticsItem.
        :rtype: str
        """
        return self._client_ip

    @client_ip.setter
    def client_ip(self, client_ip):
        r"""Sets the client_ip of this ShowSlowLogStatisticsItem.

        IP地址。

        :param client_ip: The client_ip of this ShowSlowLogStatisticsItem.
        :type client_ip: str
        """
        self._client_ip = client_ip

    @property
    def count(self):
        r"""Gets the count of this ShowSlowLogStatisticsItem.

        执行次数。

        :return: The count of this ShowSlowLogStatisticsItem.
        :rtype: str
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ShowSlowLogStatisticsItem.

        执行次数。

        :param count: The count of this ShowSlowLogStatisticsItem.
        :type count: str
        """
        self._count = count

    @property
    def database(self):
        r"""Gets the database of this ShowSlowLogStatisticsItem.

        所属数据库。

        :return: The database of this ShowSlowLogStatisticsItem.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        r"""Sets the database of this ShowSlowLogStatisticsItem.

        所属数据库。

        :param database: The database of this ShowSlowLogStatisticsItem.
        :type database: str
        """
        self._database = database

    @property
    def lock_time(self):
        r"""Gets the lock_time of this ShowSlowLogStatisticsItem.

        平均等待锁时间。

        :return: The lock_time of this ShowSlowLogStatisticsItem.
        :rtype: str
        """
        return self._lock_time

    @lock_time.setter
    def lock_time(self, lock_time):
        r"""Sets the lock_time of this ShowSlowLogStatisticsItem.

        平均等待锁时间。

        :param lock_time: The lock_time of this ShowSlowLogStatisticsItem.
        :type lock_time: str
        """
        self._lock_time = lock_time

    @property
    def node_id(self):
        r"""Gets the node_id of this ShowSlowLogStatisticsItem.

        节点ID。

        :return: The node_id of this ShowSlowLogStatisticsItem.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this ShowSlowLogStatisticsItem.

        节点ID。

        :param node_id: The node_id of this ShowSlowLogStatisticsItem.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def query_sample(self):
        r"""Gets the query_sample of this ShowSlowLogStatisticsItem.

        执行语法。

        :return: The query_sample of this ShowSlowLogStatisticsItem.
        :rtype: str
        """
        return self._query_sample

    @query_sample.setter
    def query_sample(self, query_sample):
        r"""Sets the query_sample of this ShowSlowLogStatisticsItem.

        执行语法。

        :param query_sample: The query_sample of this ShowSlowLogStatisticsItem.
        :type query_sample: str
        """
        self._query_sample = query_sample

    @property
    def rows_examined(self):
        r"""Gets the rows_examined of this ShowSlowLogStatisticsItem.

        平均扫描的行数量。

        :return: The rows_examined of this ShowSlowLogStatisticsItem.
        :rtype: int
        """
        return self._rows_examined

    @rows_examined.setter
    def rows_examined(self, rows_examined):
        r"""Sets the rows_examined of this ShowSlowLogStatisticsItem.

        平均扫描的行数量。

        :param rows_examined: The rows_examined of this ShowSlowLogStatisticsItem.
        :type rows_examined: int
        """
        self._rows_examined = rows_examined

    @property
    def rows_sent(self):
        r"""Gets the rows_sent of this ShowSlowLogStatisticsItem.

        平均结果行统计数量。

        :return: The rows_sent of this ShowSlowLogStatisticsItem.
        :rtype: int
        """
        return self._rows_sent

    @rows_sent.setter
    def rows_sent(self, rows_sent):
        r"""Sets the rows_sent of this ShowSlowLogStatisticsItem.

        平均结果行统计数量。

        :param rows_sent: The rows_sent of this ShowSlowLogStatisticsItem.
        :type rows_sent: int
        """
        self._rows_sent = rows_sent

    @property
    def time(self):
        r"""Gets the time of this ShowSlowLogStatisticsItem.

        平均执行时间。

        :return: The time of this ShowSlowLogStatisticsItem.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this ShowSlowLogStatisticsItem.

        平均执行时间。

        :param time: The time of this ShowSlowLogStatisticsItem.
        :type time: str
        """
        self._time = time

    @property
    def type(self):
        r"""Gets the type of this ShowSlowLogStatisticsItem.

        语句类型。

        :return: The type of this ShowSlowLogStatisticsItem.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowSlowLogStatisticsItem.

        语句类型。

        :param type: The type of this ShowSlowLogStatisticsItem.
        :type type: str
        """
        self._type = type

    @property
    def users(self):
        r"""Gets the users of this ShowSlowLogStatisticsItem.

        账号。

        :return: The users of this ShowSlowLogStatisticsItem.
        :rtype: str
        """
        return self._users

    @users.setter
    def users(self, users):
        r"""Sets the users of this ShowSlowLogStatisticsItem.

        账号。

        :param users: The users of this ShowSlowLogStatisticsItem.
        :type users: str
        """
        self._users = users

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
        if not isinstance(other, ShowSlowLogStatisticsItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
