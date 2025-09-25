# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeExecutionInfoResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'component_id': 'str',
        'node_id': 'str',
        'transaction_id': 'str',
        'sql_id': 'str',
        'sql_exec_id': 'str',
        'db_name': 'str',
        'schema_name': 'str',
        'start_time': 'str',
        'finish_time': 'str',
        'all_time': 'int',
        'user_name': 'str',
        'client_addr': 'str',
        'client_port': 'int',
        'trace_id': 'str',
        'application_name': 'str',
        'session_id': 'str',
        'is_slow_sql': 'bool',
        'execution_time_details': 'ExecutionTimeDetailsInfo'
    }

    attribute_map = {
        'component_id': 'component_id',
        'node_id': 'node_id',
        'transaction_id': 'transaction_id',
        'sql_id': 'sql_id',
        'sql_exec_id': 'sql_exec_id',
        'db_name': 'db_name',
        'schema_name': 'schema_name',
        'start_time': 'start_time',
        'finish_time': 'finish_time',
        'all_time': 'all_time',
        'user_name': 'user_name',
        'client_addr': 'client_addr',
        'client_port': 'client_port',
        'trace_id': 'trace_id',
        'application_name': 'application_name',
        'session_id': 'session_id',
        'is_slow_sql': 'is_slow_sql',
        'execution_time_details': 'execution_time_details'
    }

    def __init__(self, component_id=None, node_id=None, transaction_id=None, sql_id=None, sql_exec_id=None, db_name=None, schema_name=None, start_time=None, finish_time=None, all_time=None, user_name=None, client_addr=None, client_port=None, trace_id=None, application_name=None, session_id=None, is_slow_sql=None, execution_time_details=None):
        r"""NodeExecutionInfoResult

        The model defined in huaweicloud sdk

        :param component_id: **参数解释**: 组件ID。 **取值范围**: 不涉及。
        :type component_id: str
        :param node_id: **参数解释**: 节点ID。 **取值范围**: 不涉及。
        :type node_id: str
        :param transaction_id: **参数解释**: 事务ID。 **取值范围**: 不涉及。
        :type transaction_id: str
        :param sql_id: **参数解释**: 归一化SQL ID。 **取值范围**: 不涉及。
        :type sql_id: str
        :param sql_exec_id: **参数解释**: 唯一SQL ID。 **取值范围**: 不涉及。
        :type sql_exec_id: str
        :param db_name: **参数解释**: 数据库名称。 **取值范围**: 不涉及。
        :type db_name: str
        :param schema_name: **参数解释**: schema名称。 **取值范围**: 不涉及。
        :type schema_name: str
        :param start_time: **参数解释**: 语句启动的时间，格式为“yyyy-mm-ddThh:mm: ssssssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。 **取值范围**: 不涉及。
        :type start_time: str
        :param finish_time: **参数解释**: 语句结束的时间，格式为“yyyy-mm-ddThh:mm: ssssssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。 **取值范围**: 不涉及。
        :type finish_time: str
        :param all_time: **参数解释**: 执行总耗时（单位：微秒）。 **取值范围**: 不涉及。
        :type all_time: int
        :param user_name: **参数解释**: 用户名。 **取值范围**: 不涉及。
        :type user_name: str
        :param client_addr: **参数解释**: 用户发起的请求的客户端地址。 **取值范围**: 不涉及。
        :type client_addr: str
        :param client_port: **参数解释**: 用户发起的请求的客户端端口。 **取值范围**: 不涉及。
        :type client_port: int
        :param trace_id: **参数解释**: 驱动传入的trace id，与应用的一次请求相关联。 **取值范围**: 不涉及。
        :type trace_id: str
        :param application_name: **参数解释**: 用户发起的请求的应用程序名称。 **取值范围**: 不涉及。
        :type application_name: str
        :param session_id: **参数解释**: 用户session id。 **取值范围**: 不涉及。
        :type session_id: str
        :param is_slow_sql: **参数解释**: 该SQL是否为slow SQL。 **取值范围**: 不涉及。
        :type is_slow_sql: bool
        :param execution_time_details: 
        :type execution_time_details: :class:`huaweicloudsdkgaussdbforopengauss.v3.ExecutionTimeDetailsInfo`
        """
        
        

        self._component_id = None
        self._node_id = None
        self._transaction_id = None
        self._sql_id = None
        self._sql_exec_id = None
        self._db_name = None
        self._schema_name = None
        self._start_time = None
        self._finish_time = None
        self._all_time = None
        self._user_name = None
        self._client_addr = None
        self._client_port = None
        self._trace_id = None
        self._application_name = None
        self._session_id = None
        self._is_slow_sql = None
        self._execution_time_details = None
        self.discriminator = None

        self.component_id = component_id
        self.node_id = node_id
        self.transaction_id = transaction_id
        self.sql_id = sql_id
        self.sql_exec_id = sql_exec_id
        self.db_name = db_name
        self.schema_name = schema_name
        self.start_time = start_time
        self.finish_time = finish_time
        self.all_time = all_time
        self.user_name = user_name
        self.client_addr = client_addr
        self.client_port = client_port
        self.trace_id = trace_id
        self.application_name = application_name
        self.session_id = session_id
        if is_slow_sql is not None:
            self.is_slow_sql = is_slow_sql
        self.execution_time_details = execution_time_details

    @property
    def component_id(self):
        r"""Gets the component_id of this NodeExecutionInfoResult.

        **参数解释**: 组件ID。 **取值范围**: 不涉及。

        :return: The component_id of this NodeExecutionInfoResult.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        r"""Sets the component_id of this NodeExecutionInfoResult.

        **参数解释**: 组件ID。 **取值范围**: 不涉及。

        :param component_id: The component_id of this NodeExecutionInfoResult.
        :type component_id: str
        """
        self._component_id = component_id

    @property
    def node_id(self):
        r"""Gets the node_id of this NodeExecutionInfoResult.

        **参数解释**: 节点ID。 **取值范围**: 不涉及。

        :return: The node_id of this NodeExecutionInfoResult.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this NodeExecutionInfoResult.

        **参数解释**: 节点ID。 **取值范围**: 不涉及。

        :param node_id: The node_id of this NodeExecutionInfoResult.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def transaction_id(self):
        r"""Gets the transaction_id of this NodeExecutionInfoResult.

        **参数解释**: 事务ID。 **取值范围**: 不涉及。

        :return: The transaction_id of this NodeExecutionInfoResult.
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        r"""Sets the transaction_id of this NodeExecutionInfoResult.

        **参数解释**: 事务ID。 **取值范围**: 不涉及。

        :param transaction_id: The transaction_id of this NodeExecutionInfoResult.
        :type transaction_id: str
        """
        self._transaction_id = transaction_id

    @property
    def sql_id(self):
        r"""Gets the sql_id of this NodeExecutionInfoResult.

        **参数解释**: 归一化SQL ID。 **取值范围**: 不涉及。

        :return: The sql_id of this NodeExecutionInfoResult.
        :rtype: str
        """
        return self._sql_id

    @sql_id.setter
    def sql_id(self, sql_id):
        r"""Sets the sql_id of this NodeExecutionInfoResult.

        **参数解释**: 归一化SQL ID。 **取值范围**: 不涉及。

        :param sql_id: The sql_id of this NodeExecutionInfoResult.
        :type sql_id: str
        """
        self._sql_id = sql_id

    @property
    def sql_exec_id(self):
        r"""Gets the sql_exec_id of this NodeExecutionInfoResult.

        **参数解释**: 唯一SQL ID。 **取值范围**: 不涉及。

        :return: The sql_exec_id of this NodeExecutionInfoResult.
        :rtype: str
        """
        return self._sql_exec_id

    @sql_exec_id.setter
    def sql_exec_id(self, sql_exec_id):
        r"""Sets the sql_exec_id of this NodeExecutionInfoResult.

        **参数解释**: 唯一SQL ID。 **取值范围**: 不涉及。

        :param sql_exec_id: The sql_exec_id of this NodeExecutionInfoResult.
        :type sql_exec_id: str
        """
        self._sql_exec_id = sql_exec_id

    @property
    def db_name(self):
        r"""Gets the db_name of this NodeExecutionInfoResult.

        **参数解释**: 数据库名称。 **取值范围**: 不涉及。

        :return: The db_name of this NodeExecutionInfoResult.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this NodeExecutionInfoResult.

        **参数解释**: 数据库名称。 **取值范围**: 不涉及。

        :param db_name: The db_name of this NodeExecutionInfoResult.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def schema_name(self):
        r"""Gets the schema_name of this NodeExecutionInfoResult.

        **参数解释**: schema名称。 **取值范围**: 不涉及。

        :return: The schema_name of this NodeExecutionInfoResult.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        r"""Sets the schema_name of this NodeExecutionInfoResult.

        **参数解释**: schema名称。 **取值范围**: 不涉及。

        :param schema_name: The schema_name of this NodeExecutionInfoResult.
        :type schema_name: str
        """
        self._schema_name = schema_name

    @property
    def start_time(self):
        r"""Gets the start_time of this NodeExecutionInfoResult.

        **参数解释**: 语句启动的时间，格式为“yyyy-mm-ddThh:mm: ssssssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。 **取值范围**: 不涉及。

        :return: The start_time of this NodeExecutionInfoResult.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this NodeExecutionInfoResult.

        **参数解释**: 语句启动的时间，格式为“yyyy-mm-ddThh:mm: ssssssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。 **取值范围**: 不涉及。

        :param start_time: The start_time of this NodeExecutionInfoResult.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def finish_time(self):
        r"""Gets the finish_time of this NodeExecutionInfoResult.

        **参数解释**: 语句结束的时间，格式为“yyyy-mm-ddThh:mm: ssssssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。 **取值范围**: 不涉及。

        :return: The finish_time of this NodeExecutionInfoResult.
        :rtype: str
        """
        return self._finish_time

    @finish_time.setter
    def finish_time(self, finish_time):
        r"""Sets the finish_time of this NodeExecutionInfoResult.

        **参数解释**: 语句结束的时间，格式为“yyyy-mm-ddThh:mm: ssssssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。 **取值范围**: 不涉及。

        :param finish_time: The finish_time of this NodeExecutionInfoResult.
        :type finish_time: str
        """
        self._finish_time = finish_time

    @property
    def all_time(self):
        r"""Gets the all_time of this NodeExecutionInfoResult.

        **参数解释**: 执行总耗时（单位：微秒）。 **取值范围**: 不涉及。

        :return: The all_time of this NodeExecutionInfoResult.
        :rtype: int
        """
        return self._all_time

    @all_time.setter
    def all_time(self, all_time):
        r"""Sets the all_time of this NodeExecutionInfoResult.

        **参数解释**: 执行总耗时（单位：微秒）。 **取值范围**: 不涉及。

        :param all_time: The all_time of this NodeExecutionInfoResult.
        :type all_time: int
        """
        self._all_time = all_time

    @property
    def user_name(self):
        r"""Gets the user_name of this NodeExecutionInfoResult.

        **参数解释**: 用户名。 **取值范围**: 不涉及。

        :return: The user_name of this NodeExecutionInfoResult.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this NodeExecutionInfoResult.

        **参数解释**: 用户名。 **取值范围**: 不涉及。

        :param user_name: The user_name of this NodeExecutionInfoResult.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def client_addr(self):
        r"""Gets the client_addr of this NodeExecutionInfoResult.

        **参数解释**: 用户发起的请求的客户端地址。 **取值范围**: 不涉及。

        :return: The client_addr of this NodeExecutionInfoResult.
        :rtype: str
        """
        return self._client_addr

    @client_addr.setter
    def client_addr(self, client_addr):
        r"""Sets the client_addr of this NodeExecutionInfoResult.

        **参数解释**: 用户发起的请求的客户端地址。 **取值范围**: 不涉及。

        :param client_addr: The client_addr of this NodeExecutionInfoResult.
        :type client_addr: str
        """
        self._client_addr = client_addr

    @property
    def client_port(self):
        r"""Gets the client_port of this NodeExecutionInfoResult.

        **参数解释**: 用户发起的请求的客户端端口。 **取值范围**: 不涉及。

        :return: The client_port of this NodeExecutionInfoResult.
        :rtype: int
        """
        return self._client_port

    @client_port.setter
    def client_port(self, client_port):
        r"""Sets the client_port of this NodeExecutionInfoResult.

        **参数解释**: 用户发起的请求的客户端端口。 **取值范围**: 不涉及。

        :param client_port: The client_port of this NodeExecutionInfoResult.
        :type client_port: int
        """
        self._client_port = client_port

    @property
    def trace_id(self):
        r"""Gets the trace_id of this NodeExecutionInfoResult.

        **参数解释**: 驱动传入的trace id，与应用的一次请求相关联。 **取值范围**: 不涉及。

        :return: The trace_id of this NodeExecutionInfoResult.
        :rtype: str
        """
        return self._trace_id

    @trace_id.setter
    def trace_id(self, trace_id):
        r"""Sets the trace_id of this NodeExecutionInfoResult.

        **参数解释**: 驱动传入的trace id，与应用的一次请求相关联。 **取值范围**: 不涉及。

        :param trace_id: The trace_id of this NodeExecutionInfoResult.
        :type trace_id: str
        """
        self._trace_id = trace_id

    @property
    def application_name(self):
        r"""Gets the application_name of this NodeExecutionInfoResult.

        **参数解释**: 用户发起的请求的应用程序名称。 **取值范围**: 不涉及。

        :return: The application_name of this NodeExecutionInfoResult.
        :rtype: str
        """
        return self._application_name

    @application_name.setter
    def application_name(self, application_name):
        r"""Sets the application_name of this NodeExecutionInfoResult.

        **参数解释**: 用户发起的请求的应用程序名称。 **取值范围**: 不涉及。

        :param application_name: The application_name of this NodeExecutionInfoResult.
        :type application_name: str
        """
        self._application_name = application_name

    @property
    def session_id(self):
        r"""Gets the session_id of this NodeExecutionInfoResult.

        **参数解释**: 用户session id。 **取值范围**: 不涉及。

        :return: The session_id of this NodeExecutionInfoResult.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        r"""Sets the session_id of this NodeExecutionInfoResult.

        **参数解释**: 用户session id。 **取值范围**: 不涉及。

        :param session_id: The session_id of this NodeExecutionInfoResult.
        :type session_id: str
        """
        self._session_id = session_id

    @property
    def is_slow_sql(self):
        r"""Gets the is_slow_sql of this NodeExecutionInfoResult.

        **参数解释**: 该SQL是否为slow SQL。 **取值范围**: 不涉及。

        :return: The is_slow_sql of this NodeExecutionInfoResult.
        :rtype: bool
        """
        return self._is_slow_sql

    @is_slow_sql.setter
    def is_slow_sql(self, is_slow_sql):
        r"""Sets the is_slow_sql of this NodeExecutionInfoResult.

        **参数解释**: 该SQL是否为slow SQL。 **取值范围**: 不涉及。

        :param is_slow_sql: The is_slow_sql of this NodeExecutionInfoResult.
        :type is_slow_sql: bool
        """
        self._is_slow_sql = is_slow_sql

    @property
    def execution_time_details(self):
        r"""Gets the execution_time_details of this NodeExecutionInfoResult.

        :return: The execution_time_details of this NodeExecutionInfoResult.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ExecutionTimeDetailsInfo`
        """
        return self._execution_time_details

    @execution_time_details.setter
    def execution_time_details(self, execution_time_details):
        r"""Sets the execution_time_details of this NodeExecutionInfoResult.

        :param execution_time_details: The execution_time_details of this NodeExecutionInfoResult.
        :type execution_time_details: :class:`huaweicloudsdkgaussdbforopengauss.v3.ExecutionTimeDetailsInfo`
        """
        self._execution_time_details = execution_time_details

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
        if not isinstance(other, NodeExecutionInfoResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
