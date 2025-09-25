# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTransactionResponseBodyRowsInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sessionid': 'int',
        'pid': 'int',
        'query_id': 'int',
        'datname': 'str',
        'client_addr': 'str',
        'client_port': 'int',
        'usename': 'str',
        'query': 'str',
        'backend_start': 'str',
        'xact_start': 'str',
        'application_name': 'str',
        'state': 'str',
        'state_change': 'str',
        'query_start': 'str',
        'waiting': 'str',
        'unique_sql_id': 'int',
        'top_xid': 'str',
        'current_xid': 'str',
        'exec_time': 'str',
        'xlog_quantity': 'int'
    }

    attribute_map = {
        'sessionid': 'sessionid',
        'pid': 'pid',
        'query_id': 'query_id',
        'datname': 'datname',
        'client_addr': 'client_addr',
        'client_port': 'client_port',
        'usename': 'usename',
        'query': 'query',
        'backend_start': 'backend_start',
        'xact_start': 'xact_start',
        'application_name': 'application_name',
        'state': 'state',
        'state_change': 'state_change',
        'query_start': 'query_start',
        'waiting': 'waiting',
        'unique_sql_id': 'unique_sql_id',
        'top_xid': 'top_xid',
        'current_xid': 'current_xid',
        'exec_time': 'exec_time',
        'xlog_quantity': 'xlog_quantity'
    }

    def __init__(self, sessionid=None, pid=None, query_id=None, datname=None, client_addr=None, client_port=None, usename=None, query=None, backend_start=None, xact_start=None, application_name=None, state=None, state_change=None, query_start=None, waiting=None, unique_sql_id=None, top_xid=None, current_xid=None, exec_time=None, xlog_quantity=None):
        r"""ListTransactionResponseBodyRowsInfo

        The model defined in huaweicloud sdk

        :param sessionid: **参数解释**: 事务ID。 **取值范围**: 不涉及。
        :type sessionid: int
        :param pid: **参数解释**: 线程ID。 **取值范围**: 不涉及。
        :type pid: int
        :param query_id: **参数解释**: SQL查询ID。 **取值范围**: 不涉及。
        :type query_id: int
        :param datname: **参数解释**: 数据库。 **取值范围**: 不涉及。
        :type datname: str
        :param client_addr: **参数解释**: 用户发起事务请求的客户端地址。 **取值范围**: 不涉及。
        :type client_addr: str
        :param client_port: **参数解释**: 用户发起事务请求的客户端端口。 **取值范围**: 不涉及。
        :type client_port: int
        :param usename: **参数解释**: 用户名。 **取值范围**: 不涉及。 **取值范围**: 不涉及。
        :type usename: str
        :param query: **参数解释**: 查询的SQL语句。 **取值范围**: 不涉及。
        :type query: str
        :param backend_start: **参数解释**: 会话开始时间。 **取值范围**: 不涉及。
        :type backend_start: str
        :param xact_start: **参数解释**: 事务开始时间。 **取值范围**: 不涉及。
        :type xact_start: str
        :param application_name: **参数解释**: 应用名称。 **取值范围**: 不涉及。
        :type application_name: str
        :param state: **参数解释**: 事务状态。 **取值范围**: 不涉及。
        :type state: str
        :param state_change: **参数解释**: 事务变更时间。 **取值范围**: 不涉及。
        :type state_change: str
        :param query_start: **参数解释**: 查询开始时间。 **取值范围**: 不涉及。
        :type query_start: str
        :param waiting: **参数解释**: 是否等待。 **取值范围**: 不涉及。
        :type waiting: str
        :param unique_sql_id: **参数解释**: 归一化ID。 **取值范围**: 不涉及。
        :type unique_sql_id: int
        :param top_xid: **参数解释**: 顶层事务ID。
        :type top_xid: str
        :param current_xid: **参数解释**: 当前事务ID。 **取值范围**: 不涉及。
        :type current_xid: str
        :param exec_time: **参数解释**: 事务执行时长。 **取值范围**: 不涉及。
        :type exec_time: str
        :param xlog_quantity: **参数解释**: 事务xlog量。 **取值范围**: 不涉及。
        :type xlog_quantity: int
        """
        
        

        self._sessionid = None
        self._pid = None
        self._query_id = None
        self._datname = None
        self._client_addr = None
        self._client_port = None
        self._usename = None
        self._query = None
        self._backend_start = None
        self._xact_start = None
        self._application_name = None
        self._state = None
        self._state_change = None
        self._query_start = None
        self._waiting = None
        self._unique_sql_id = None
        self._top_xid = None
        self._current_xid = None
        self._exec_time = None
        self._xlog_quantity = None
        self.discriminator = None

        if sessionid is not None:
            self.sessionid = sessionid
        if pid is not None:
            self.pid = pid
        if query_id is not None:
            self.query_id = query_id
        if datname is not None:
            self.datname = datname
        if client_addr is not None:
            self.client_addr = client_addr
        if client_port is not None:
            self.client_port = client_port
        if usename is not None:
            self.usename = usename
        if query is not None:
            self.query = query
        if backend_start is not None:
            self.backend_start = backend_start
        if xact_start is not None:
            self.xact_start = xact_start
        if application_name is not None:
            self.application_name = application_name
        if state is not None:
            self.state = state
        if state_change is not None:
            self.state_change = state_change
        if query_start is not None:
            self.query_start = query_start
        if waiting is not None:
            self.waiting = waiting
        if unique_sql_id is not None:
            self.unique_sql_id = unique_sql_id
        if top_xid is not None:
            self.top_xid = top_xid
        if current_xid is not None:
            self.current_xid = current_xid
        if exec_time is not None:
            self.exec_time = exec_time
        if xlog_quantity is not None:
            self.xlog_quantity = xlog_quantity

    @property
    def sessionid(self):
        r"""Gets the sessionid of this ListTransactionResponseBodyRowsInfo.

        **参数解释**: 事务ID。 **取值范围**: 不涉及。

        :return: The sessionid of this ListTransactionResponseBodyRowsInfo.
        :rtype: int
        """
        return self._sessionid

    @sessionid.setter
    def sessionid(self, sessionid):
        r"""Sets the sessionid of this ListTransactionResponseBodyRowsInfo.

        **参数解释**: 事务ID。 **取值范围**: 不涉及。

        :param sessionid: The sessionid of this ListTransactionResponseBodyRowsInfo.
        :type sessionid: int
        """
        self._sessionid = sessionid

    @property
    def pid(self):
        r"""Gets the pid of this ListTransactionResponseBodyRowsInfo.

        **参数解释**: 线程ID。 **取值范围**: 不涉及。

        :return: The pid of this ListTransactionResponseBodyRowsInfo.
        :rtype: int
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        r"""Sets the pid of this ListTransactionResponseBodyRowsInfo.

        **参数解释**: 线程ID。 **取值范围**: 不涉及。

        :param pid: The pid of this ListTransactionResponseBodyRowsInfo.
        :type pid: int
        """
        self._pid = pid

    @property
    def query_id(self):
        r"""Gets the query_id of this ListTransactionResponseBodyRowsInfo.

        **参数解释**: SQL查询ID。 **取值范围**: 不涉及。

        :return: The query_id of this ListTransactionResponseBodyRowsInfo.
        :rtype: int
        """
        return self._query_id

    @query_id.setter
    def query_id(self, query_id):
        r"""Sets the query_id of this ListTransactionResponseBodyRowsInfo.

        **参数解释**: SQL查询ID。 **取值范围**: 不涉及。

        :param query_id: The query_id of this ListTransactionResponseBodyRowsInfo.
        :type query_id: int
        """
        self._query_id = query_id

    @property
    def datname(self):
        r"""Gets the datname of this ListTransactionResponseBodyRowsInfo.

        **参数解释**: 数据库。 **取值范围**: 不涉及。

        :return: The datname of this ListTransactionResponseBodyRowsInfo.
        :rtype: str
        """
        return self._datname

    @datname.setter
    def datname(self, datname):
        r"""Sets the datname of this ListTransactionResponseBodyRowsInfo.

        **参数解释**: 数据库。 **取值范围**: 不涉及。

        :param datname: The datname of this ListTransactionResponseBodyRowsInfo.
        :type datname: str
        """
        self._datname = datname

    @property
    def client_addr(self):
        r"""Gets the client_addr of this ListTransactionResponseBodyRowsInfo.

        **参数解释**: 用户发起事务请求的客户端地址。 **取值范围**: 不涉及。

        :return: The client_addr of this ListTransactionResponseBodyRowsInfo.
        :rtype: str
        """
        return self._client_addr

    @client_addr.setter
    def client_addr(self, client_addr):
        r"""Sets the client_addr of this ListTransactionResponseBodyRowsInfo.

        **参数解释**: 用户发起事务请求的客户端地址。 **取值范围**: 不涉及。

        :param client_addr: The client_addr of this ListTransactionResponseBodyRowsInfo.
        :type client_addr: str
        """
        self._client_addr = client_addr

    @property
    def client_port(self):
        r"""Gets the client_port of this ListTransactionResponseBodyRowsInfo.

        **参数解释**: 用户发起事务请求的客户端端口。 **取值范围**: 不涉及。

        :return: The client_port of this ListTransactionResponseBodyRowsInfo.
        :rtype: int
        """
        return self._client_port

    @client_port.setter
    def client_port(self, client_port):
        r"""Sets the client_port of this ListTransactionResponseBodyRowsInfo.

        **参数解释**: 用户发起事务请求的客户端端口。 **取值范围**: 不涉及。

        :param client_port: The client_port of this ListTransactionResponseBodyRowsInfo.
        :type client_port: int
        """
        self._client_port = client_port

    @property
    def usename(self):
        r"""Gets the usename of this ListTransactionResponseBodyRowsInfo.

        **参数解释**: 用户名。 **取值范围**: 不涉及。 **取值范围**: 不涉及。

        :return: The usename of this ListTransactionResponseBodyRowsInfo.
        :rtype: str
        """
        return self._usename

    @usename.setter
    def usename(self, usename):
        r"""Sets the usename of this ListTransactionResponseBodyRowsInfo.

        **参数解释**: 用户名。 **取值范围**: 不涉及。 **取值范围**: 不涉及。

        :param usename: The usename of this ListTransactionResponseBodyRowsInfo.
        :type usename: str
        """
        self._usename = usename

    @property
    def query(self):
        r"""Gets the query of this ListTransactionResponseBodyRowsInfo.

        **参数解释**: 查询的SQL语句。 **取值范围**: 不涉及。

        :return: The query of this ListTransactionResponseBodyRowsInfo.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        r"""Sets the query of this ListTransactionResponseBodyRowsInfo.

        **参数解释**: 查询的SQL语句。 **取值范围**: 不涉及。

        :param query: The query of this ListTransactionResponseBodyRowsInfo.
        :type query: str
        """
        self._query = query

    @property
    def backend_start(self):
        r"""Gets the backend_start of this ListTransactionResponseBodyRowsInfo.

        **参数解释**: 会话开始时间。 **取值范围**: 不涉及。

        :return: The backend_start of this ListTransactionResponseBodyRowsInfo.
        :rtype: str
        """
        return self._backend_start

    @backend_start.setter
    def backend_start(self, backend_start):
        r"""Sets the backend_start of this ListTransactionResponseBodyRowsInfo.

        **参数解释**: 会话开始时间。 **取值范围**: 不涉及。

        :param backend_start: The backend_start of this ListTransactionResponseBodyRowsInfo.
        :type backend_start: str
        """
        self._backend_start = backend_start

    @property
    def xact_start(self):
        r"""Gets the xact_start of this ListTransactionResponseBodyRowsInfo.

        **参数解释**: 事务开始时间。 **取值范围**: 不涉及。

        :return: The xact_start of this ListTransactionResponseBodyRowsInfo.
        :rtype: str
        """
        return self._xact_start

    @xact_start.setter
    def xact_start(self, xact_start):
        r"""Sets the xact_start of this ListTransactionResponseBodyRowsInfo.

        **参数解释**: 事务开始时间。 **取值范围**: 不涉及。

        :param xact_start: The xact_start of this ListTransactionResponseBodyRowsInfo.
        :type xact_start: str
        """
        self._xact_start = xact_start

    @property
    def application_name(self):
        r"""Gets the application_name of this ListTransactionResponseBodyRowsInfo.

        **参数解释**: 应用名称。 **取值范围**: 不涉及。

        :return: The application_name of this ListTransactionResponseBodyRowsInfo.
        :rtype: str
        """
        return self._application_name

    @application_name.setter
    def application_name(self, application_name):
        r"""Sets the application_name of this ListTransactionResponseBodyRowsInfo.

        **参数解释**: 应用名称。 **取值范围**: 不涉及。

        :param application_name: The application_name of this ListTransactionResponseBodyRowsInfo.
        :type application_name: str
        """
        self._application_name = application_name

    @property
    def state(self):
        r"""Gets the state of this ListTransactionResponseBodyRowsInfo.

        **参数解释**: 事务状态。 **取值范围**: 不涉及。

        :return: The state of this ListTransactionResponseBodyRowsInfo.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ListTransactionResponseBodyRowsInfo.

        **参数解释**: 事务状态。 **取值范围**: 不涉及。

        :param state: The state of this ListTransactionResponseBodyRowsInfo.
        :type state: str
        """
        self._state = state

    @property
    def state_change(self):
        r"""Gets the state_change of this ListTransactionResponseBodyRowsInfo.

        **参数解释**: 事务变更时间。 **取值范围**: 不涉及。

        :return: The state_change of this ListTransactionResponseBodyRowsInfo.
        :rtype: str
        """
        return self._state_change

    @state_change.setter
    def state_change(self, state_change):
        r"""Sets the state_change of this ListTransactionResponseBodyRowsInfo.

        **参数解释**: 事务变更时间。 **取值范围**: 不涉及。

        :param state_change: The state_change of this ListTransactionResponseBodyRowsInfo.
        :type state_change: str
        """
        self._state_change = state_change

    @property
    def query_start(self):
        r"""Gets the query_start of this ListTransactionResponseBodyRowsInfo.

        **参数解释**: 查询开始时间。 **取值范围**: 不涉及。

        :return: The query_start of this ListTransactionResponseBodyRowsInfo.
        :rtype: str
        """
        return self._query_start

    @query_start.setter
    def query_start(self, query_start):
        r"""Sets the query_start of this ListTransactionResponseBodyRowsInfo.

        **参数解释**: 查询开始时间。 **取值范围**: 不涉及。

        :param query_start: The query_start of this ListTransactionResponseBodyRowsInfo.
        :type query_start: str
        """
        self._query_start = query_start

    @property
    def waiting(self):
        r"""Gets the waiting of this ListTransactionResponseBodyRowsInfo.

        **参数解释**: 是否等待。 **取值范围**: 不涉及。

        :return: The waiting of this ListTransactionResponseBodyRowsInfo.
        :rtype: str
        """
        return self._waiting

    @waiting.setter
    def waiting(self, waiting):
        r"""Sets the waiting of this ListTransactionResponseBodyRowsInfo.

        **参数解释**: 是否等待。 **取值范围**: 不涉及。

        :param waiting: The waiting of this ListTransactionResponseBodyRowsInfo.
        :type waiting: str
        """
        self._waiting = waiting

    @property
    def unique_sql_id(self):
        r"""Gets the unique_sql_id of this ListTransactionResponseBodyRowsInfo.

        **参数解释**: 归一化ID。 **取值范围**: 不涉及。

        :return: The unique_sql_id of this ListTransactionResponseBodyRowsInfo.
        :rtype: int
        """
        return self._unique_sql_id

    @unique_sql_id.setter
    def unique_sql_id(self, unique_sql_id):
        r"""Sets the unique_sql_id of this ListTransactionResponseBodyRowsInfo.

        **参数解释**: 归一化ID。 **取值范围**: 不涉及。

        :param unique_sql_id: The unique_sql_id of this ListTransactionResponseBodyRowsInfo.
        :type unique_sql_id: int
        """
        self._unique_sql_id = unique_sql_id

    @property
    def top_xid(self):
        r"""Gets the top_xid of this ListTransactionResponseBodyRowsInfo.

        **参数解释**: 顶层事务ID。

        :return: The top_xid of this ListTransactionResponseBodyRowsInfo.
        :rtype: str
        """
        return self._top_xid

    @top_xid.setter
    def top_xid(self, top_xid):
        r"""Sets the top_xid of this ListTransactionResponseBodyRowsInfo.

        **参数解释**: 顶层事务ID。

        :param top_xid: The top_xid of this ListTransactionResponseBodyRowsInfo.
        :type top_xid: str
        """
        self._top_xid = top_xid

    @property
    def current_xid(self):
        r"""Gets the current_xid of this ListTransactionResponseBodyRowsInfo.

        **参数解释**: 当前事务ID。 **取值范围**: 不涉及。

        :return: The current_xid of this ListTransactionResponseBodyRowsInfo.
        :rtype: str
        """
        return self._current_xid

    @current_xid.setter
    def current_xid(self, current_xid):
        r"""Sets the current_xid of this ListTransactionResponseBodyRowsInfo.

        **参数解释**: 当前事务ID。 **取值范围**: 不涉及。

        :param current_xid: The current_xid of this ListTransactionResponseBodyRowsInfo.
        :type current_xid: str
        """
        self._current_xid = current_xid

    @property
    def exec_time(self):
        r"""Gets the exec_time of this ListTransactionResponseBodyRowsInfo.

        **参数解释**: 事务执行时长。 **取值范围**: 不涉及。

        :return: The exec_time of this ListTransactionResponseBodyRowsInfo.
        :rtype: str
        """
        return self._exec_time

    @exec_time.setter
    def exec_time(self, exec_time):
        r"""Sets the exec_time of this ListTransactionResponseBodyRowsInfo.

        **参数解释**: 事务执行时长。 **取值范围**: 不涉及。

        :param exec_time: The exec_time of this ListTransactionResponseBodyRowsInfo.
        :type exec_time: str
        """
        self._exec_time = exec_time

    @property
    def xlog_quantity(self):
        r"""Gets the xlog_quantity of this ListTransactionResponseBodyRowsInfo.

        **参数解释**: 事务xlog量。 **取值范围**: 不涉及。

        :return: The xlog_quantity of this ListTransactionResponseBodyRowsInfo.
        :rtype: int
        """
        return self._xlog_quantity

    @xlog_quantity.setter
    def xlog_quantity(self, xlog_quantity):
        r"""Sets the xlog_quantity of this ListTransactionResponseBodyRowsInfo.

        **参数解释**: 事务xlog量。 **取值范围**: 不涉及。

        :param xlog_quantity: The xlog_quantity of this ListTransactionResponseBodyRowsInfo.
        :type xlog_quantity: int
        """
        self._xlog_quantity = xlog_quantity

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
        if not isinstance(other, ListTransactionResponseBodyRowsInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
