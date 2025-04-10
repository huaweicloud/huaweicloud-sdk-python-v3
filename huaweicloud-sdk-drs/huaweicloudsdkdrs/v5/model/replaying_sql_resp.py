# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReplayingSqlResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'schema_name': 'str',
        'sql_statement': 'str',
        'latency': 'int',
        'execute_latency': 'int',
        'status': 'str',
        'client': 'str',
        'connection_id': 'str',
        'replay_start_time': 'str'
    }

    attribute_map = {
        'schema_name': 'schema_name',
        'sql_statement': 'sql_statement',
        'latency': 'latency',
        'execute_latency': 'execute_latency',
        'status': 'status',
        'client': 'client',
        'connection_id': 'connection_id',
        'replay_start_time': 'replay_start_time'
    }

    def __init__(self, schema_name=None, sql_statement=None, latency=None, execute_latency=None, status=None, client=None, connection_id=None, replay_start_time=None):
        r"""ReplayingSqlResp

        The model defined in huaweicloud sdk

        :param schema_name: 库名或shema名称
        :type schema_name: str
        :param sql_statement: SQL语句
        :type sql_statement: str
        :param latency: 原始执行耗时
        :type latency: int
        :param execute_latency: 回放执行耗时
        :type execute_latency: int
        :param status: 执行状态
        :type status: str
        :param client: 客户端IP
        :type client: str
        :param connection_id: 连接ID
        :type connection_id: str
        :param replay_start_time: 回放开始时间
        :type replay_start_time: str
        """
        
        

        self._schema_name = None
        self._sql_statement = None
        self._latency = None
        self._execute_latency = None
        self._status = None
        self._client = None
        self._connection_id = None
        self._replay_start_time = None
        self.discriminator = None

        if schema_name is not None:
            self.schema_name = schema_name
        if sql_statement is not None:
            self.sql_statement = sql_statement
        if latency is not None:
            self.latency = latency
        if execute_latency is not None:
            self.execute_latency = execute_latency
        if status is not None:
            self.status = status
        if client is not None:
            self.client = client
        if connection_id is not None:
            self.connection_id = connection_id
        if replay_start_time is not None:
            self.replay_start_time = replay_start_time

    @property
    def schema_name(self):
        r"""Gets the schema_name of this ReplayingSqlResp.

        库名或shema名称

        :return: The schema_name of this ReplayingSqlResp.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        r"""Sets the schema_name of this ReplayingSqlResp.

        库名或shema名称

        :param schema_name: The schema_name of this ReplayingSqlResp.
        :type schema_name: str
        """
        self._schema_name = schema_name

    @property
    def sql_statement(self):
        r"""Gets the sql_statement of this ReplayingSqlResp.

        SQL语句

        :return: The sql_statement of this ReplayingSqlResp.
        :rtype: str
        """
        return self._sql_statement

    @sql_statement.setter
    def sql_statement(self, sql_statement):
        r"""Sets the sql_statement of this ReplayingSqlResp.

        SQL语句

        :param sql_statement: The sql_statement of this ReplayingSqlResp.
        :type sql_statement: str
        """
        self._sql_statement = sql_statement

    @property
    def latency(self):
        r"""Gets the latency of this ReplayingSqlResp.

        原始执行耗时

        :return: The latency of this ReplayingSqlResp.
        :rtype: int
        """
        return self._latency

    @latency.setter
    def latency(self, latency):
        r"""Sets the latency of this ReplayingSqlResp.

        原始执行耗时

        :param latency: The latency of this ReplayingSqlResp.
        :type latency: int
        """
        self._latency = latency

    @property
    def execute_latency(self):
        r"""Gets the execute_latency of this ReplayingSqlResp.

        回放执行耗时

        :return: The execute_latency of this ReplayingSqlResp.
        :rtype: int
        """
        return self._execute_latency

    @execute_latency.setter
    def execute_latency(self, execute_latency):
        r"""Sets the execute_latency of this ReplayingSqlResp.

        回放执行耗时

        :param execute_latency: The execute_latency of this ReplayingSqlResp.
        :type execute_latency: int
        """
        self._execute_latency = execute_latency

    @property
    def status(self):
        r"""Gets the status of this ReplayingSqlResp.

        执行状态

        :return: The status of this ReplayingSqlResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ReplayingSqlResp.

        执行状态

        :param status: The status of this ReplayingSqlResp.
        :type status: str
        """
        self._status = status

    @property
    def client(self):
        r"""Gets the client of this ReplayingSqlResp.

        客户端IP

        :return: The client of this ReplayingSqlResp.
        :rtype: str
        """
        return self._client

    @client.setter
    def client(self, client):
        r"""Sets the client of this ReplayingSqlResp.

        客户端IP

        :param client: The client of this ReplayingSqlResp.
        :type client: str
        """
        self._client = client

    @property
    def connection_id(self):
        r"""Gets the connection_id of this ReplayingSqlResp.

        连接ID

        :return: The connection_id of this ReplayingSqlResp.
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        r"""Sets the connection_id of this ReplayingSqlResp.

        连接ID

        :param connection_id: The connection_id of this ReplayingSqlResp.
        :type connection_id: str
        """
        self._connection_id = connection_id

    @property
    def replay_start_time(self):
        r"""Gets the replay_start_time of this ReplayingSqlResp.

        回放开始时间

        :return: The replay_start_time of this ReplayingSqlResp.
        :rtype: str
        """
        return self._replay_start_time

    @replay_start_time.setter
    def replay_start_time(self, replay_start_time):
        r"""Sets the replay_start_time of this ReplayingSqlResp.

        回放开始时间

        :param replay_start_time: The replay_start_time of this ReplayingSqlResp.
        :type replay_start_time: str
        """
        self._replay_start_time = replay_start_time

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
        if not isinstance(other, ReplayingSqlResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
