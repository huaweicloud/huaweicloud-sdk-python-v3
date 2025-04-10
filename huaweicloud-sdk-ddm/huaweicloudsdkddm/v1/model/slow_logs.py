# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SlowLogs:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'users': 'str',
        'database': 'str',
        'query_sample': 'str',
        'log_time': 'str',
        'time': 'str',
        'shards': 'str',
        'node_id': 'str',
        'rows_examined': 'str',
        'host': 'str'
    }

    attribute_map = {
        'users': 'users',
        'database': 'database',
        'query_sample': 'query_sample',
        'log_time': 'log_time',
        'time': 'time',
        'shards': 'shards',
        'node_id': 'node_id',
        'rows_examined': 'rows_examined',
        'host': 'host'
    }

    def __init__(self, users=None, database=None, query_sample=None, log_time=None, time=None, shards=None, node_id=None, rows_examined=None, host=None):
        r"""SlowLogs

        The model defined in huaweicloud sdk

        :param users: 执行慢sql的DDM账号名称。
        :type users: str
        :param database: 慢sql所属逻辑库的名称。
        :type database: str
        :param query_sample: 慢sql执行语法。
        :type query_sample: str
        :param log_time: DDM慢sql开始执行时间。
        :type log_time: str
        :param time: 慢sql的执行时长，精确到毫秒。
        :type time: str
        :param shards: 逻辑库物理分片名称。
        :type shards: str
        :param node_id: 节点ID。
        :type node_id: str
        :param rows_examined: 慢sql影响行数。
        :type rows_examined: str
        :param host: 客户端ip，该IP地址可能涉及个人数据，建议用户依据实际IP地址的敏感性做查询后脱敏处理。
        :type host: str
        """
        
        

        self._users = None
        self._database = None
        self._query_sample = None
        self._log_time = None
        self._time = None
        self._shards = None
        self._node_id = None
        self._rows_examined = None
        self._host = None
        self.discriminator = None

        if users is not None:
            self.users = users
        if database is not None:
            self.database = database
        if query_sample is not None:
            self.query_sample = query_sample
        if log_time is not None:
            self.log_time = log_time
        if time is not None:
            self.time = time
        if shards is not None:
            self.shards = shards
        if node_id is not None:
            self.node_id = node_id
        if rows_examined is not None:
            self.rows_examined = rows_examined
        if host is not None:
            self.host = host

    @property
    def users(self):
        r"""Gets the users of this SlowLogs.

        执行慢sql的DDM账号名称。

        :return: The users of this SlowLogs.
        :rtype: str
        """
        return self._users

    @users.setter
    def users(self, users):
        r"""Sets the users of this SlowLogs.

        执行慢sql的DDM账号名称。

        :param users: The users of this SlowLogs.
        :type users: str
        """
        self._users = users

    @property
    def database(self):
        r"""Gets the database of this SlowLogs.

        慢sql所属逻辑库的名称。

        :return: The database of this SlowLogs.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        r"""Sets the database of this SlowLogs.

        慢sql所属逻辑库的名称。

        :param database: The database of this SlowLogs.
        :type database: str
        """
        self._database = database

    @property
    def query_sample(self):
        r"""Gets the query_sample of this SlowLogs.

        慢sql执行语法。

        :return: The query_sample of this SlowLogs.
        :rtype: str
        """
        return self._query_sample

    @query_sample.setter
    def query_sample(self, query_sample):
        r"""Sets the query_sample of this SlowLogs.

        慢sql执行语法。

        :param query_sample: The query_sample of this SlowLogs.
        :type query_sample: str
        """
        self._query_sample = query_sample

    @property
    def log_time(self):
        r"""Gets the log_time of this SlowLogs.

        DDM慢sql开始执行时间。

        :return: The log_time of this SlowLogs.
        :rtype: str
        """
        return self._log_time

    @log_time.setter
    def log_time(self, log_time):
        r"""Sets the log_time of this SlowLogs.

        DDM慢sql开始执行时间。

        :param log_time: The log_time of this SlowLogs.
        :type log_time: str
        """
        self._log_time = log_time

    @property
    def time(self):
        r"""Gets the time of this SlowLogs.

        慢sql的执行时长，精确到毫秒。

        :return: The time of this SlowLogs.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this SlowLogs.

        慢sql的执行时长，精确到毫秒。

        :param time: The time of this SlowLogs.
        :type time: str
        """
        self._time = time

    @property
    def shards(self):
        r"""Gets the shards of this SlowLogs.

        逻辑库物理分片名称。

        :return: The shards of this SlowLogs.
        :rtype: str
        """
        return self._shards

    @shards.setter
    def shards(self, shards):
        r"""Sets the shards of this SlowLogs.

        逻辑库物理分片名称。

        :param shards: The shards of this SlowLogs.
        :type shards: str
        """
        self._shards = shards

    @property
    def node_id(self):
        r"""Gets the node_id of this SlowLogs.

        节点ID。

        :return: The node_id of this SlowLogs.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this SlowLogs.

        节点ID。

        :param node_id: The node_id of this SlowLogs.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def rows_examined(self):
        r"""Gets the rows_examined of this SlowLogs.

        慢sql影响行数。

        :return: The rows_examined of this SlowLogs.
        :rtype: str
        """
        return self._rows_examined

    @rows_examined.setter
    def rows_examined(self, rows_examined):
        r"""Sets the rows_examined of this SlowLogs.

        慢sql影响行数。

        :param rows_examined: The rows_examined of this SlowLogs.
        :type rows_examined: str
        """
        self._rows_examined = rows_examined

    @property
    def host(self):
        r"""Gets the host of this SlowLogs.

        客户端ip，该IP地址可能涉及个人数据，建议用户依据实际IP地址的敏感性做查询后脱敏处理。

        :return: The host of this SlowLogs.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        r"""Sets the host of this SlowLogs.

        客户端ip，该IP地址可能涉及个人数据，建议用户依据实际IP地址的敏感性做查询后脱敏处理。

        :param host: The host of this SlowLogs.
        :type host: str
        """
        self._host = host

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
        if not isinstance(other, SlowLogs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
