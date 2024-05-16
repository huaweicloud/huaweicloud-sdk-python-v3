# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SlowSqlStatistics:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'execute_count': 'int',
        'avg_execute_time': 'float',
        'max_execute_time': 'float',
        'avg_lock_wait_time': 'float',
        'max_lock_wait_time': 'float',
        'avg_rows_sent': 'float',
        'max_rows_sent': 'float',
        'avg_rows_examined': 'float',
        'max_rows_examined': 'float',
        'avg_key_examined': 'float',
        'max_key_examined': 'float',
        'node_id': 'str',
        'node_name': 'str',
        'sql_type': 'str',
        'db_name': 'str',
        'collection': 'str',
        'user': 'str',
        'client': 'str'
    }

    attribute_map = {
        'execute_count': 'execute_count',
        'avg_execute_time': 'avg_execute_time',
        'max_execute_time': 'max_execute_time',
        'avg_lock_wait_time': 'avg_lock_wait_time',
        'max_lock_wait_time': 'max_lock_wait_time',
        'avg_rows_sent': 'avg_rows_sent',
        'max_rows_sent': 'max_rows_sent',
        'avg_rows_examined': 'avg_rows_examined',
        'max_rows_examined': 'max_rows_examined',
        'avg_key_examined': 'avg_key_examined',
        'max_key_examined': 'max_key_examined',
        'node_id': 'node_id',
        'node_name': 'node_name',
        'sql_type': 'sql_type',
        'db_name': 'db_name',
        'collection': 'collection',
        'user': 'user',
        'client': 'client'
    }

    def __init__(self, execute_count=None, avg_execute_time=None, max_execute_time=None, avg_lock_wait_time=None, max_lock_wait_time=None, avg_rows_sent=None, max_rows_sent=None, avg_rows_examined=None, max_rows_examined=None, avg_key_examined=None, max_key_examined=None, node_id=None, node_name=None, sql_type=None, db_name=None, collection=None, user=None, client=None):
        """SlowSqlStatistics

        The model defined in huaweicloud sdk

        :param execute_count: 执行次数。
        :type execute_count: int
        :param avg_execute_time: 平均执行耗时(s)。
        :type avg_execute_time: float
        :param max_execute_time: 最大执行耗时(s)。
        :type max_execute_time: float
        :param avg_lock_wait_time: 平均锁等待时间(s)。
        :type avg_lock_wait_time: float
        :param max_lock_wait_time: 最大锁等待时间(s)。
        :type max_lock_wait_time: float
        :param avg_rows_sent: 平均返回文档数。
        :type avg_rows_sent: float
        :param max_rows_sent: 最大返回文档数。
        :type max_rows_sent: float
        :param avg_rows_examined: 平均扫描文档数。
        :type avg_rows_examined: float
        :param max_rows_examined: 最大扫描文档数。
        :type max_rows_examined: float
        :param avg_key_examined: 平均扫描索引数。
        :type avg_key_examined: float
        :param max_key_examined: 最大扫描索引数。
        :type max_key_examined: float
        :param node_id: 节点ID，按node_id统计时赋值。
        :type node_id: str
        :param node_name: 节点名称，按node_id统计时赋值。
        :type node_name: str
        :param sql_type: 语句类型，按sql_type统计时赋值。
        :type sql_type: str
        :param db_name: 库名，按db_name、collection统计时赋值。
        :type db_name: str
        :param collection: 数据库表，按collection统计时赋值。
        :type collection: str
        :param user: 用户名，按user统计时赋值。
        :type user: str
        :param client: 客户端，按client统计时赋值。
        :type client: str
        """
        
        

        self._execute_count = None
        self._avg_execute_time = None
        self._max_execute_time = None
        self._avg_lock_wait_time = None
        self._max_lock_wait_time = None
        self._avg_rows_sent = None
        self._max_rows_sent = None
        self._avg_rows_examined = None
        self._max_rows_examined = None
        self._avg_key_examined = None
        self._max_key_examined = None
        self._node_id = None
        self._node_name = None
        self._sql_type = None
        self._db_name = None
        self._collection = None
        self._user = None
        self._client = None
        self.discriminator = None

        self.execute_count = execute_count
        self.avg_execute_time = avg_execute_time
        self.max_execute_time = max_execute_time
        self.avg_lock_wait_time = avg_lock_wait_time
        self.max_lock_wait_time = max_lock_wait_time
        self.avg_rows_sent = avg_rows_sent
        self.max_rows_sent = max_rows_sent
        self.avg_rows_examined = avg_rows_examined
        self.max_rows_examined = max_rows_examined
        self.avg_key_examined = avg_key_examined
        self.max_key_examined = max_key_examined
        if node_id is not None:
            self.node_id = node_id
        if node_name is not None:
            self.node_name = node_name
        if sql_type is not None:
            self.sql_type = sql_type
        if db_name is not None:
            self.db_name = db_name
        if collection is not None:
            self.collection = collection
        if user is not None:
            self.user = user
        if client is not None:
            self.client = client

    @property
    def execute_count(self):
        """Gets the execute_count of this SlowSqlStatistics.

        执行次数。

        :return: The execute_count of this SlowSqlStatistics.
        :rtype: int
        """
        return self._execute_count

    @execute_count.setter
    def execute_count(self, execute_count):
        """Sets the execute_count of this SlowSqlStatistics.

        执行次数。

        :param execute_count: The execute_count of this SlowSqlStatistics.
        :type execute_count: int
        """
        self._execute_count = execute_count

    @property
    def avg_execute_time(self):
        """Gets the avg_execute_time of this SlowSqlStatistics.

        平均执行耗时(s)。

        :return: The avg_execute_time of this SlowSqlStatistics.
        :rtype: float
        """
        return self._avg_execute_time

    @avg_execute_time.setter
    def avg_execute_time(self, avg_execute_time):
        """Sets the avg_execute_time of this SlowSqlStatistics.

        平均执行耗时(s)。

        :param avg_execute_time: The avg_execute_time of this SlowSqlStatistics.
        :type avg_execute_time: float
        """
        self._avg_execute_time = avg_execute_time

    @property
    def max_execute_time(self):
        """Gets the max_execute_time of this SlowSqlStatistics.

        最大执行耗时(s)。

        :return: The max_execute_time of this SlowSqlStatistics.
        :rtype: float
        """
        return self._max_execute_time

    @max_execute_time.setter
    def max_execute_time(self, max_execute_time):
        """Sets the max_execute_time of this SlowSqlStatistics.

        最大执行耗时(s)。

        :param max_execute_time: The max_execute_time of this SlowSqlStatistics.
        :type max_execute_time: float
        """
        self._max_execute_time = max_execute_time

    @property
    def avg_lock_wait_time(self):
        """Gets the avg_lock_wait_time of this SlowSqlStatistics.

        平均锁等待时间(s)。

        :return: The avg_lock_wait_time of this SlowSqlStatistics.
        :rtype: float
        """
        return self._avg_lock_wait_time

    @avg_lock_wait_time.setter
    def avg_lock_wait_time(self, avg_lock_wait_time):
        """Sets the avg_lock_wait_time of this SlowSqlStatistics.

        平均锁等待时间(s)。

        :param avg_lock_wait_time: The avg_lock_wait_time of this SlowSqlStatistics.
        :type avg_lock_wait_time: float
        """
        self._avg_lock_wait_time = avg_lock_wait_time

    @property
    def max_lock_wait_time(self):
        """Gets the max_lock_wait_time of this SlowSqlStatistics.

        最大锁等待时间(s)。

        :return: The max_lock_wait_time of this SlowSqlStatistics.
        :rtype: float
        """
        return self._max_lock_wait_time

    @max_lock_wait_time.setter
    def max_lock_wait_time(self, max_lock_wait_time):
        """Sets the max_lock_wait_time of this SlowSqlStatistics.

        最大锁等待时间(s)。

        :param max_lock_wait_time: The max_lock_wait_time of this SlowSqlStatistics.
        :type max_lock_wait_time: float
        """
        self._max_lock_wait_time = max_lock_wait_time

    @property
    def avg_rows_sent(self):
        """Gets the avg_rows_sent of this SlowSqlStatistics.

        平均返回文档数。

        :return: The avg_rows_sent of this SlowSqlStatistics.
        :rtype: float
        """
        return self._avg_rows_sent

    @avg_rows_sent.setter
    def avg_rows_sent(self, avg_rows_sent):
        """Sets the avg_rows_sent of this SlowSqlStatistics.

        平均返回文档数。

        :param avg_rows_sent: The avg_rows_sent of this SlowSqlStatistics.
        :type avg_rows_sent: float
        """
        self._avg_rows_sent = avg_rows_sent

    @property
    def max_rows_sent(self):
        """Gets the max_rows_sent of this SlowSqlStatistics.

        最大返回文档数。

        :return: The max_rows_sent of this SlowSqlStatistics.
        :rtype: float
        """
        return self._max_rows_sent

    @max_rows_sent.setter
    def max_rows_sent(self, max_rows_sent):
        """Sets the max_rows_sent of this SlowSqlStatistics.

        最大返回文档数。

        :param max_rows_sent: The max_rows_sent of this SlowSqlStatistics.
        :type max_rows_sent: float
        """
        self._max_rows_sent = max_rows_sent

    @property
    def avg_rows_examined(self):
        """Gets the avg_rows_examined of this SlowSqlStatistics.

        平均扫描文档数。

        :return: The avg_rows_examined of this SlowSqlStatistics.
        :rtype: float
        """
        return self._avg_rows_examined

    @avg_rows_examined.setter
    def avg_rows_examined(self, avg_rows_examined):
        """Sets the avg_rows_examined of this SlowSqlStatistics.

        平均扫描文档数。

        :param avg_rows_examined: The avg_rows_examined of this SlowSqlStatistics.
        :type avg_rows_examined: float
        """
        self._avg_rows_examined = avg_rows_examined

    @property
    def max_rows_examined(self):
        """Gets the max_rows_examined of this SlowSqlStatistics.

        最大扫描文档数。

        :return: The max_rows_examined of this SlowSqlStatistics.
        :rtype: float
        """
        return self._max_rows_examined

    @max_rows_examined.setter
    def max_rows_examined(self, max_rows_examined):
        """Sets the max_rows_examined of this SlowSqlStatistics.

        最大扫描文档数。

        :param max_rows_examined: The max_rows_examined of this SlowSqlStatistics.
        :type max_rows_examined: float
        """
        self._max_rows_examined = max_rows_examined

    @property
    def avg_key_examined(self):
        """Gets the avg_key_examined of this SlowSqlStatistics.

        平均扫描索引数。

        :return: The avg_key_examined of this SlowSqlStatistics.
        :rtype: float
        """
        return self._avg_key_examined

    @avg_key_examined.setter
    def avg_key_examined(self, avg_key_examined):
        """Sets the avg_key_examined of this SlowSqlStatistics.

        平均扫描索引数。

        :param avg_key_examined: The avg_key_examined of this SlowSqlStatistics.
        :type avg_key_examined: float
        """
        self._avg_key_examined = avg_key_examined

    @property
    def max_key_examined(self):
        """Gets the max_key_examined of this SlowSqlStatistics.

        最大扫描索引数。

        :return: The max_key_examined of this SlowSqlStatistics.
        :rtype: float
        """
        return self._max_key_examined

    @max_key_examined.setter
    def max_key_examined(self, max_key_examined):
        """Sets the max_key_examined of this SlowSqlStatistics.

        最大扫描索引数。

        :param max_key_examined: The max_key_examined of this SlowSqlStatistics.
        :type max_key_examined: float
        """
        self._max_key_examined = max_key_examined

    @property
    def node_id(self):
        """Gets the node_id of this SlowSqlStatistics.

        节点ID，按node_id统计时赋值。

        :return: The node_id of this SlowSqlStatistics.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this SlowSqlStatistics.

        节点ID，按node_id统计时赋值。

        :param node_id: The node_id of this SlowSqlStatistics.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def node_name(self):
        """Gets the node_name of this SlowSqlStatistics.

        节点名称，按node_id统计时赋值。

        :return: The node_name of this SlowSqlStatistics.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        """Sets the node_name of this SlowSqlStatistics.

        节点名称，按node_id统计时赋值。

        :param node_name: The node_name of this SlowSqlStatistics.
        :type node_name: str
        """
        self._node_name = node_name

    @property
    def sql_type(self):
        """Gets the sql_type of this SlowSqlStatistics.

        语句类型，按sql_type统计时赋值。

        :return: The sql_type of this SlowSqlStatistics.
        :rtype: str
        """
        return self._sql_type

    @sql_type.setter
    def sql_type(self, sql_type):
        """Sets the sql_type of this SlowSqlStatistics.

        语句类型，按sql_type统计时赋值。

        :param sql_type: The sql_type of this SlowSqlStatistics.
        :type sql_type: str
        """
        self._sql_type = sql_type

    @property
    def db_name(self):
        """Gets the db_name of this SlowSqlStatistics.

        库名，按db_name、collection统计时赋值。

        :return: The db_name of this SlowSqlStatistics.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """Sets the db_name of this SlowSqlStatistics.

        库名，按db_name、collection统计时赋值。

        :param db_name: The db_name of this SlowSqlStatistics.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def collection(self):
        """Gets the collection of this SlowSqlStatistics.

        数据库表，按collection统计时赋值。

        :return: The collection of this SlowSqlStatistics.
        :rtype: str
        """
        return self._collection

    @collection.setter
    def collection(self, collection):
        """Sets the collection of this SlowSqlStatistics.

        数据库表，按collection统计时赋值。

        :param collection: The collection of this SlowSqlStatistics.
        :type collection: str
        """
        self._collection = collection

    @property
    def user(self):
        """Gets the user of this SlowSqlStatistics.

        用户名，按user统计时赋值。

        :return: The user of this SlowSqlStatistics.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this SlowSqlStatistics.

        用户名，按user统计时赋值。

        :param user: The user of this SlowSqlStatistics.
        :type user: str
        """
        self._user = user

    @property
    def client(self):
        """Gets the client of this SlowSqlStatistics.

        客户端，按client统计时赋值。

        :return: The client of this SlowSqlStatistics.
        :rtype: str
        """
        return self._client

    @client.setter
    def client(self, client):
        """Sets the client of this SlowSqlStatistics.

        客户端，按client统计时赋值。

        :param client: The client of this SlowSqlStatistics.
        :type client: str
        """
        self._client = client

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
        if not isinstance(other, SlowSqlStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
