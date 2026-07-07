# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAnalysisSessionResultRespTopStateDuration:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'session_id': 'str',
        'user': 'str',
        'host': 'str',
        'database_name': 'str',
        'execution_status': 'str',
        'command': 'str',
        'sql_statement': 'str',
        'state_duration': 'str',
        'transaction_duration': 'str',
        'transaction_id': 'str',
        'transaction_lock_wait_time': 'str',
        'transaction_status': 'str',
        'rows_locked_by_transactions': 'str',
        'tables_locked_by_transactions': 'str',
        'rows_updated_by_transactions': 'str'
    }

    attribute_map = {
        'session_id': 'session_id',
        'user': 'user',
        'host': 'host',
        'database_name': 'database_name',
        'execution_status': 'execution_status',
        'command': 'command',
        'sql_statement': 'sql_statement',
        'state_duration': 'state_duration',
        'transaction_duration': 'transaction_duration',
        'transaction_id': 'transaction_id',
        'transaction_lock_wait_time': 'transaction_lock_wait_time',
        'transaction_status': 'transaction_status',
        'rows_locked_by_transactions': 'rows_locked_by_transactions',
        'tables_locked_by_transactions': 'tables_locked_by_transactions',
        'rows_updated_by_transactions': 'rows_updated_by_transactions'
    }

    def __init__(self, session_id=None, user=None, host=None, database_name=None, execution_status=None, command=None, sql_statement=None, state_duration=None, transaction_duration=None, transaction_id=None, transaction_lock_wait_time=None, transaction_status=None, rows_locked_by_transactions=None, tables_locked_by_transactions=None, rows_updated_by_transactions=None):
        r"""ShowAnalysisSessionResultRespTopStateDuration

        The model defined in huaweicloud sdk

        :param session_id: 会话ID
        :type session_id: str
        :param user: 用户名
        :type user: str
        :param host: 主机IP
        :type host: str
        :param database_name: 数据库名
        :type database_name: str
        :param execution_status: 执行状态
        :type execution_status: str
        :param command: 命令类型
        :type command: str
        :param sql_statement: SQL语句
        :type sql_statement: str
        :param state_duration: 状态持续时间（秒）
        :type state_duration: str
        :param transaction_duration: 事务持续时间（秒）
        :type transaction_duration: str
        :param transaction_id: 事务ID
        :type transaction_id: str
        :param transaction_lock_wait_time: 事务锁等待时长（秒）
        :type transaction_lock_wait_time: str
        :param transaction_status: 事务状态
        :type transaction_status: str
        :param rows_locked_by_transactions: 事务锁定行数
        :type rows_locked_by_transactions: str
        :param tables_locked_by_transactions: 事务锁定表数量
        :type tables_locked_by_transactions: str
        :param rows_updated_by_transactions: 事务更新行数
        :type rows_updated_by_transactions: str
        """
        
        

        self._session_id = None
        self._user = None
        self._host = None
        self._database_name = None
        self._execution_status = None
        self._command = None
        self._sql_statement = None
        self._state_duration = None
        self._transaction_duration = None
        self._transaction_id = None
        self._transaction_lock_wait_time = None
        self._transaction_status = None
        self._rows_locked_by_transactions = None
        self._tables_locked_by_transactions = None
        self._rows_updated_by_transactions = None
        self.discriminator = None

        self.session_id = session_id
        self.user = user
        self.host = host
        self.database_name = database_name
        self.execution_status = execution_status
        self.command = command
        self.sql_statement = sql_statement
        self.state_duration = state_duration
        self.transaction_duration = transaction_duration
        self.transaction_id = transaction_id
        self.transaction_lock_wait_time = transaction_lock_wait_time
        self.transaction_status = transaction_status
        self.rows_locked_by_transactions = rows_locked_by_transactions
        self.tables_locked_by_transactions = tables_locked_by_transactions
        self.rows_updated_by_transactions = rows_updated_by_transactions

    @property
    def session_id(self):
        r"""Gets the session_id of this ShowAnalysisSessionResultRespTopStateDuration.

        会话ID

        :return: The session_id of this ShowAnalysisSessionResultRespTopStateDuration.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        r"""Sets the session_id of this ShowAnalysisSessionResultRespTopStateDuration.

        会话ID

        :param session_id: The session_id of this ShowAnalysisSessionResultRespTopStateDuration.
        :type session_id: str
        """
        self._session_id = session_id

    @property
    def user(self):
        r"""Gets the user of this ShowAnalysisSessionResultRespTopStateDuration.

        用户名

        :return: The user of this ShowAnalysisSessionResultRespTopStateDuration.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this ShowAnalysisSessionResultRespTopStateDuration.

        用户名

        :param user: The user of this ShowAnalysisSessionResultRespTopStateDuration.
        :type user: str
        """
        self._user = user

    @property
    def host(self):
        r"""Gets the host of this ShowAnalysisSessionResultRespTopStateDuration.

        主机IP

        :return: The host of this ShowAnalysisSessionResultRespTopStateDuration.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        r"""Sets the host of this ShowAnalysisSessionResultRespTopStateDuration.

        主机IP

        :param host: The host of this ShowAnalysisSessionResultRespTopStateDuration.
        :type host: str
        """
        self._host = host

    @property
    def database_name(self):
        r"""Gets the database_name of this ShowAnalysisSessionResultRespTopStateDuration.

        数据库名

        :return: The database_name of this ShowAnalysisSessionResultRespTopStateDuration.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this ShowAnalysisSessionResultRespTopStateDuration.

        数据库名

        :param database_name: The database_name of this ShowAnalysisSessionResultRespTopStateDuration.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def execution_status(self):
        r"""Gets the execution_status of this ShowAnalysisSessionResultRespTopStateDuration.

        执行状态

        :return: The execution_status of this ShowAnalysisSessionResultRespTopStateDuration.
        :rtype: str
        """
        return self._execution_status

    @execution_status.setter
    def execution_status(self, execution_status):
        r"""Sets the execution_status of this ShowAnalysisSessionResultRespTopStateDuration.

        执行状态

        :param execution_status: The execution_status of this ShowAnalysisSessionResultRespTopStateDuration.
        :type execution_status: str
        """
        self._execution_status = execution_status

    @property
    def command(self):
        r"""Gets the command of this ShowAnalysisSessionResultRespTopStateDuration.

        命令类型

        :return: The command of this ShowAnalysisSessionResultRespTopStateDuration.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        r"""Sets the command of this ShowAnalysisSessionResultRespTopStateDuration.

        命令类型

        :param command: The command of this ShowAnalysisSessionResultRespTopStateDuration.
        :type command: str
        """
        self._command = command

    @property
    def sql_statement(self):
        r"""Gets the sql_statement of this ShowAnalysisSessionResultRespTopStateDuration.

        SQL语句

        :return: The sql_statement of this ShowAnalysisSessionResultRespTopStateDuration.
        :rtype: str
        """
        return self._sql_statement

    @sql_statement.setter
    def sql_statement(self, sql_statement):
        r"""Sets the sql_statement of this ShowAnalysisSessionResultRespTopStateDuration.

        SQL语句

        :param sql_statement: The sql_statement of this ShowAnalysisSessionResultRespTopStateDuration.
        :type sql_statement: str
        """
        self._sql_statement = sql_statement

    @property
    def state_duration(self):
        r"""Gets the state_duration of this ShowAnalysisSessionResultRespTopStateDuration.

        状态持续时间（秒）

        :return: The state_duration of this ShowAnalysisSessionResultRespTopStateDuration.
        :rtype: str
        """
        return self._state_duration

    @state_duration.setter
    def state_duration(self, state_duration):
        r"""Sets the state_duration of this ShowAnalysisSessionResultRespTopStateDuration.

        状态持续时间（秒）

        :param state_duration: The state_duration of this ShowAnalysisSessionResultRespTopStateDuration.
        :type state_duration: str
        """
        self._state_duration = state_duration

    @property
    def transaction_duration(self):
        r"""Gets the transaction_duration of this ShowAnalysisSessionResultRespTopStateDuration.

        事务持续时间（秒）

        :return: The transaction_duration of this ShowAnalysisSessionResultRespTopStateDuration.
        :rtype: str
        """
        return self._transaction_duration

    @transaction_duration.setter
    def transaction_duration(self, transaction_duration):
        r"""Sets the transaction_duration of this ShowAnalysisSessionResultRespTopStateDuration.

        事务持续时间（秒）

        :param transaction_duration: The transaction_duration of this ShowAnalysisSessionResultRespTopStateDuration.
        :type transaction_duration: str
        """
        self._transaction_duration = transaction_duration

    @property
    def transaction_id(self):
        r"""Gets the transaction_id of this ShowAnalysisSessionResultRespTopStateDuration.

        事务ID

        :return: The transaction_id of this ShowAnalysisSessionResultRespTopStateDuration.
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        r"""Sets the transaction_id of this ShowAnalysisSessionResultRespTopStateDuration.

        事务ID

        :param transaction_id: The transaction_id of this ShowAnalysisSessionResultRespTopStateDuration.
        :type transaction_id: str
        """
        self._transaction_id = transaction_id

    @property
    def transaction_lock_wait_time(self):
        r"""Gets the transaction_lock_wait_time of this ShowAnalysisSessionResultRespTopStateDuration.

        事务锁等待时长（秒）

        :return: The transaction_lock_wait_time of this ShowAnalysisSessionResultRespTopStateDuration.
        :rtype: str
        """
        return self._transaction_lock_wait_time

    @transaction_lock_wait_time.setter
    def transaction_lock_wait_time(self, transaction_lock_wait_time):
        r"""Sets the transaction_lock_wait_time of this ShowAnalysisSessionResultRespTopStateDuration.

        事务锁等待时长（秒）

        :param transaction_lock_wait_time: The transaction_lock_wait_time of this ShowAnalysisSessionResultRespTopStateDuration.
        :type transaction_lock_wait_time: str
        """
        self._transaction_lock_wait_time = transaction_lock_wait_time

    @property
    def transaction_status(self):
        r"""Gets the transaction_status of this ShowAnalysisSessionResultRespTopStateDuration.

        事务状态

        :return: The transaction_status of this ShowAnalysisSessionResultRespTopStateDuration.
        :rtype: str
        """
        return self._transaction_status

    @transaction_status.setter
    def transaction_status(self, transaction_status):
        r"""Sets the transaction_status of this ShowAnalysisSessionResultRespTopStateDuration.

        事务状态

        :param transaction_status: The transaction_status of this ShowAnalysisSessionResultRespTopStateDuration.
        :type transaction_status: str
        """
        self._transaction_status = transaction_status

    @property
    def rows_locked_by_transactions(self):
        r"""Gets the rows_locked_by_transactions of this ShowAnalysisSessionResultRespTopStateDuration.

        事务锁定行数

        :return: The rows_locked_by_transactions of this ShowAnalysisSessionResultRespTopStateDuration.
        :rtype: str
        """
        return self._rows_locked_by_transactions

    @rows_locked_by_transactions.setter
    def rows_locked_by_transactions(self, rows_locked_by_transactions):
        r"""Sets the rows_locked_by_transactions of this ShowAnalysisSessionResultRespTopStateDuration.

        事务锁定行数

        :param rows_locked_by_transactions: The rows_locked_by_transactions of this ShowAnalysisSessionResultRespTopStateDuration.
        :type rows_locked_by_transactions: str
        """
        self._rows_locked_by_transactions = rows_locked_by_transactions

    @property
    def tables_locked_by_transactions(self):
        r"""Gets the tables_locked_by_transactions of this ShowAnalysisSessionResultRespTopStateDuration.

        事务锁定表数量

        :return: The tables_locked_by_transactions of this ShowAnalysisSessionResultRespTopStateDuration.
        :rtype: str
        """
        return self._tables_locked_by_transactions

    @tables_locked_by_transactions.setter
    def tables_locked_by_transactions(self, tables_locked_by_transactions):
        r"""Sets the tables_locked_by_transactions of this ShowAnalysisSessionResultRespTopStateDuration.

        事务锁定表数量

        :param tables_locked_by_transactions: The tables_locked_by_transactions of this ShowAnalysisSessionResultRespTopStateDuration.
        :type tables_locked_by_transactions: str
        """
        self._tables_locked_by_transactions = tables_locked_by_transactions

    @property
    def rows_updated_by_transactions(self):
        r"""Gets the rows_updated_by_transactions of this ShowAnalysisSessionResultRespTopStateDuration.

        事务更新行数

        :return: The rows_updated_by_transactions of this ShowAnalysisSessionResultRespTopStateDuration.
        :rtype: str
        """
        return self._rows_updated_by_transactions

    @rows_updated_by_transactions.setter
    def rows_updated_by_transactions(self, rows_updated_by_transactions):
        r"""Sets the rows_updated_by_transactions of this ShowAnalysisSessionResultRespTopStateDuration.

        事务更新行数

        :param rows_updated_by_transactions: The rows_updated_by_transactions of this ShowAnalysisSessionResultRespTopStateDuration.
        :type rows_updated_by_transactions: str
        """
        self._rows_updated_by_transactions = rows_updated_by_transactions

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
        if not isinstance(other, ShowAnalysisSessionResultRespTopStateDuration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
