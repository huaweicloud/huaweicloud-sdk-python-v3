# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReplaySqlNowInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'thread_id': 'int',
        'created_at': 'int',
        'modified_at': 'int',
        'shard_id': 'int',
        'schema_name': 'str',
        'sql_statement': 'str',
        'latency': 'int',
        'execute_latency': 'int',
        'target_type': 'str',
        'target_name': 'str',
        'status': 'str'
    }

    attribute_map = {
        'thread_id': 'thread_id',
        'created_at': 'created_at',
        'modified_at': 'modified_at',
        'shard_id': 'shard_id',
        'schema_name': 'schema_name',
        'sql_statement': 'sql_statement',
        'latency': 'latency',
        'execute_latency': 'execute_latency',
        'target_type': 'target_type',
        'target_name': 'target_name',
        'status': 'status'
    }

    def __init__(self, thread_id=None, created_at=None, modified_at=None, shard_id=None, schema_name=None, sql_statement=None, latency=None, execute_latency=None, target_type=None, target_name=None, status=None):
        r"""ReplaySqlNowInfo

        The model defined in huaweicloud sdk

        :param thread_id: 会话id
        :type thread_id: int
        :param created_at: 创建时间
        :type created_at: int
        :param modified_at: 修改时间
        :type modified_at: int
        :param shard_id: 分片id
        :type shard_id: int
        :param schema_name: schema名称
        :type schema_name: str
        :param sql_statement: sql语句
        :type sql_statement: str
        :param latency: 原始耗时
        :type latency: int
        :param execute_latency: 执行耗时
        :type execute_latency: int
        :param target_type: 目标库类型
        :type target_type: str
        :param target_name: 目标库标识
        :type target_name: str
        :param status: 回放状态。取值： - running：执行中。 - finish：已完成。
        :type status: str
        """
        
        

        self._thread_id = None
        self._created_at = None
        self._modified_at = None
        self._shard_id = None
        self._schema_name = None
        self._sql_statement = None
        self._latency = None
        self._execute_latency = None
        self._target_type = None
        self._target_name = None
        self._status = None
        self.discriminator = None

        self.thread_id = thread_id
        self.created_at = created_at
        self.modified_at = modified_at
        self.shard_id = shard_id
        self.schema_name = schema_name
        self.sql_statement = sql_statement
        self.latency = latency
        self.execute_latency = execute_latency
        self.target_type = target_type
        self.target_name = target_name
        self.status = status

    @property
    def thread_id(self):
        r"""Gets the thread_id of this ReplaySqlNowInfo.

        会话id

        :return: The thread_id of this ReplaySqlNowInfo.
        :rtype: int
        """
        return self._thread_id

    @thread_id.setter
    def thread_id(self, thread_id):
        r"""Sets the thread_id of this ReplaySqlNowInfo.

        会话id

        :param thread_id: The thread_id of this ReplaySqlNowInfo.
        :type thread_id: int
        """
        self._thread_id = thread_id

    @property
    def created_at(self):
        r"""Gets the created_at of this ReplaySqlNowInfo.

        创建时间

        :return: The created_at of this ReplaySqlNowInfo.
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ReplaySqlNowInfo.

        创建时间

        :param created_at: The created_at of this ReplaySqlNowInfo.
        :type created_at: int
        """
        self._created_at = created_at

    @property
    def modified_at(self):
        r"""Gets the modified_at of this ReplaySqlNowInfo.

        修改时间

        :return: The modified_at of this ReplaySqlNowInfo.
        :rtype: int
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        r"""Sets the modified_at of this ReplaySqlNowInfo.

        修改时间

        :param modified_at: The modified_at of this ReplaySqlNowInfo.
        :type modified_at: int
        """
        self._modified_at = modified_at

    @property
    def shard_id(self):
        r"""Gets the shard_id of this ReplaySqlNowInfo.

        分片id

        :return: The shard_id of this ReplaySqlNowInfo.
        :rtype: int
        """
        return self._shard_id

    @shard_id.setter
    def shard_id(self, shard_id):
        r"""Sets the shard_id of this ReplaySqlNowInfo.

        分片id

        :param shard_id: The shard_id of this ReplaySqlNowInfo.
        :type shard_id: int
        """
        self._shard_id = shard_id

    @property
    def schema_name(self):
        r"""Gets the schema_name of this ReplaySqlNowInfo.

        schema名称

        :return: The schema_name of this ReplaySqlNowInfo.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        r"""Sets the schema_name of this ReplaySqlNowInfo.

        schema名称

        :param schema_name: The schema_name of this ReplaySqlNowInfo.
        :type schema_name: str
        """
        self._schema_name = schema_name

    @property
    def sql_statement(self):
        r"""Gets the sql_statement of this ReplaySqlNowInfo.

        sql语句

        :return: The sql_statement of this ReplaySqlNowInfo.
        :rtype: str
        """
        return self._sql_statement

    @sql_statement.setter
    def sql_statement(self, sql_statement):
        r"""Sets the sql_statement of this ReplaySqlNowInfo.

        sql语句

        :param sql_statement: The sql_statement of this ReplaySqlNowInfo.
        :type sql_statement: str
        """
        self._sql_statement = sql_statement

    @property
    def latency(self):
        r"""Gets the latency of this ReplaySqlNowInfo.

        原始耗时

        :return: The latency of this ReplaySqlNowInfo.
        :rtype: int
        """
        return self._latency

    @latency.setter
    def latency(self, latency):
        r"""Sets the latency of this ReplaySqlNowInfo.

        原始耗时

        :param latency: The latency of this ReplaySqlNowInfo.
        :type latency: int
        """
        self._latency = latency

    @property
    def execute_latency(self):
        r"""Gets the execute_latency of this ReplaySqlNowInfo.

        执行耗时

        :return: The execute_latency of this ReplaySqlNowInfo.
        :rtype: int
        """
        return self._execute_latency

    @execute_latency.setter
    def execute_latency(self, execute_latency):
        r"""Sets the execute_latency of this ReplaySqlNowInfo.

        执行耗时

        :param execute_latency: The execute_latency of this ReplaySqlNowInfo.
        :type execute_latency: int
        """
        self._execute_latency = execute_latency

    @property
    def target_type(self):
        r"""Gets the target_type of this ReplaySqlNowInfo.

        目标库类型

        :return: The target_type of this ReplaySqlNowInfo.
        :rtype: str
        """
        return self._target_type

    @target_type.setter
    def target_type(self, target_type):
        r"""Sets the target_type of this ReplaySqlNowInfo.

        目标库类型

        :param target_type: The target_type of this ReplaySqlNowInfo.
        :type target_type: str
        """
        self._target_type = target_type

    @property
    def target_name(self):
        r"""Gets the target_name of this ReplaySqlNowInfo.

        目标库标识

        :return: The target_name of this ReplaySqlNowInfo.
        :rtype: str
        """
        return self._target_name

    @target_name.setter
    def target_name(self, target_name):
        r"""Sets the target_name of this ReplaySqlNowInfo.

        目标库标识

        :param target_name: The target_name of this ReplaySqlNowInfo.
        :type target_name: str
        """
        self._target_name = target_name

    @property
    def status(self):
        r"""Gets the status of this ReplaySqlNowInfo.

        回放状态。取值： - running：执行中。 - finish：已完成。

        :return: The status of this ReplaySqlNowInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ReplaySqlNowInfo.

        回放状态。取值： - running：执行中。 - finish：已完成。

        :param status: The status of this ReplaySqlNowInfo.
        :type status: str
        """
        self._status = status

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ReplaySqlNowInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
