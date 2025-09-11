# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SqlDetailBean:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'audit_result': 'str',
        'client_port': 'int',
        'client_ip': 'str',
        'client_mac': 'str',
        'client_name': 'str',
        'client_os_name': 'str',
        'client_os_user': 'str',
        'client_port_str': 'str',
        'client_tool': 'str',
        'db_port': 'int',
        'db_instance': 'str',
        'db_ip': 'str',
        'db_mac': 'str',
        'db_port_str': 'str',
        'db_service_name': 'str',
        'db_session_id': 'str',
        'db_type': 'str',
        'db_user': 'str',
        'end_time': 'str',
        'execute_time': 'int',
        'field': 'str',
        'id': 'str',
        'level': 'str',
        'lines': 'str',
        'log_result': 'str',
        'object': 'str',
        'object_type': 'str',
        'query_id': 'str',
        'query_type': 'str',
        'response_length': 'int',
        'response_status': 'str',
        'rule_id': 'str',
        'rule_name': 'str',
        'rule_type': 'str',
        'schema': 'str',
        'scope_id': 'str',
        'scope_name': 'str',
        'sql_response': 'str',
        'sql_result': 'str',
        'sql_statement': 'str',
        'start_time': 'str',
        'tcp_session_id': 'str'
    }

    attribute_map = {
        'audit_result': 'audit_result',
        'client_port': 'client_port',
        'client_ip': 'client_ip',
        'client_mac': 'client_mac',
        'client_name': 'client_name',
        'client_os_name': 'client_os_name',
        'client_os_user': 'client_os_user',
        'client_port_str': 'client_port_str',
        'client_tool': 'client_tool',
        'db_port': 'db_port',
        'db_instance': 'db_instance',
        'db_ip': 'db_ip',
        'db_mac': 'db_mac',
        'db_port_str': 'db_port_str',
        'db_service_name': 'db_service_name',
        'db_session_id': 'db_session_id',
        'db_type': 'db_type',
        'db_user': 'db_user',
        'end_time': 'end_time',
        'execute_time': 'execute_time',
        'field': 'field',
        'id': 'id',
        'level': 'level',
        'lines': 'lines',
        'log_result': 'log_result',
        'object': 'object',
        'object_type': 'object_type',
        'query_id': 'query_id',
        'query_type': 'query_type',
        'response_length': 'response_length',
        'response_status': 'response_status',
        'rule_id': 'rule_id',
        'rule_name': 'rule_name',
        'rule_type': 'rule_type',
        'schema': 'schema',
        'scope_id': 'scope_id',
        'scope_name': 'scope_name',
        'sql_response': 'sql_response',
        'sql_result': 'sql_result',
        'sql_statement': 'sql_statement',
        'start_time': 'start_time',
        'tcp_session_id': 'tcp_session_id'
    }

    def __init__(self, audit_result=None, client_port=None, client_ip=None, client_mac=None, client_name=None, client_os_name=None, client_os_user=None, client_port_str=None, client_tool=None, db_port=None, db_instance=None, db_ip=None, db_mac=None, db_port_str=None, db_service_name=None, db_session_id=None, db_type=None, db_user=None, end_time=None, execute_time=None, field=None, id=None, level=None, lines=None, log_result=None, object=None, object_type=None, query_id=None, query_type=None, response_length=None, response_status=None, rule_id=None, rule_name=None, rule_type=None, schema=None, scope_id=None, scope_name=None, sql_response=None, sql_result=None, sql_statement=None, start_time=None, tcp_session_id=None):
        r"""SqlDetailBean

        The model defined in huaweicloud sdk

        :param audit_result: 审计结果
        :type audit_result: str
        :param client_port: 客户端端口
        :type client_port: int
        :param client_ip: 客户端IP
        :type client_ip: str
        :param client_mac: 客户端MAC地址
        :type client_mac: str
        :param client_name: 客户端名称
        :type client_name: str
        :param client_os_name: 客户端系统主机名称
        :type client_os_name: str
        :param client_os_user: 客户端操作系统用户名
        :type client_os_user: str
        :param client_port_str: 客户端端口字符
        :type client_port_str: str
        :param client_tool: 客户端连接工具
        :type client_tool: str
        :param db_port: 数据库端口
        :type db_port: int
        :param db_instance: 数据库实例
        :type db_instance: str
        :param db_ip: 数据库IP
        :type db_ip: str
        :param db_mac: 数据库MAC地址
        :type db_mac: str
        :param db_port_str: 数据库端口字符
        :type db_port_str: str
        :param db_service_name: 数据库服务名称
        :type db_service_name: str
        :param db_session_id: 数据库连接ID
        :type db_session_id: str
        :param db_type: 数据库类型
        :type db_type: str
        :param db_user: 数据库用户
        :type db_user: str
        :param end_time: 请求结束时间
        :type end_time: str
        :param execute_time: 执行时长
        :type execute_time: int
        :param field: 操作对象类型信息
        :type field: str
        :param id: 记录ID
        :type id: str
        :param level: 风险等级   - LOW：低  - MEDIUM：中  - HIGH：高  - NO_RISK：无
        :type level: str
        :param lines: 影响行数
        :type lines: str
        :param log_result: 登入登出结果
        :type log_result: str
        :param object: 操作对象
        :type object: str
        :param object_type: 操作对象类型
        :type object_type: str
        :param query_id: 查询ID
        :type query_id: str
        :param query_type: 操作类型
        :type query_type: str
        :param response_length: 数据长度
        :type response_length: int
        :param response_status: 响应状态
        :type response_status: str
        :param rule_id: 规则ID
        :type rule_id: str
        :param rule_name: 规则名称
        :type rule_name: str
        :param rule_type: 规则类型
        :type rule_type: str
        :param schema: 数据库SCHEMA
        :type schema: str
        :param scope_id: 审计范围ID
        :type scope_id: str
        :param scope_name: 审计范围名称
        :type scope_name: str
        :param sql_response: SQL返回结果
        :type sql_response: str
        :param sql_result: SQL处理结果
        :type sql_result: str
        :param sql_statement: SQL语句内容
        :type sql_statement: str
        :param start_time: 请求开始时间
        :type start_time: str
        :param tcp_session_id: TCP连接ID
        :type tcp_session_id: str
        """
        
        

        self._audit_result = None
        self._client_port = None
        self._client_ip = None
        self._client_mac = None
        self._client_name = None
        self._client_os_name = None
        self._client_os_user = None
        self._client_port_str = None
        self._client_tool = None
        self._db_port = None
        self._db_instance = None
        self._db_ip = None
        self._db_mac = None
        self._db_port_str = None
        self._db_service_name = None
        self._db_session_id = None
        self._db_type = None
        self._db_user = None
        self._end_time = None
        self._execute_time = None
        self._field = None
        self._id = None
        self._level = None
        self._lines = None
        self._log_result = None
        self._object = None
        self._object_type = None
        self._query_id = None
        self._query_type = None
        self._response_length = None
        self._response_status = None
        self._rule_id = None
        self._rule_name = None
        self._rule_type = None
        self._schema = None
        self._scope_id = None
        self._scope_name = None
        self._sql_response = None
        self._sql_result = None
        self._sql_statement = None
        self._start_time = None
        self._tcp_session_id = None
        self.discriminator = None

        if audit_result is not None:
            self.audit_result = audit_result
        if client_port is not None:
            self.client_port = client_port
        if client_ip is not None:
            self.client_ip = client_ip
        if client_mac is not None:
            self.client_mac = client_mac
        if client_name is not None:
            self.client_name = client_name
        if client_os_name is not None:
            self.client_os_name = client_os_name
        if client_os_user is not None:
            self.client_os_user = client_os_user
        if client_port_str is not None:
            self.client_port_str = client_port_str
        if client_tool is not None:
            self.client_tool = client_tool
        if db_port is not None:
            self.db_port = db_port
        if db_instance is not None:
            self.db_instance = db_instance
        if db_ip is not None:
            self.db_ip = db_ip
        if db_mac is not None:
            self.db_mac = db_mac
        if db_port_str is not None:
            self.db_port_str = db_port_str
        if db_service_name is not None:
            self.db_service_name = db_service_name
        if db_session_id is not None:
            self.db_session_id = db_session_id
        if db_type is not None:
            self.db_type = db_type
        if db_user is not None:
            self.db_user = db_user
        if end_time is not None:
            self.end_time = end_time
        if execute_time is not None:
            self.execute_time = execute_time
        if field is not None:
            self.field = field
        if id is not None:
            self.id = id
        if level is not None:
            self.level = level
        if lines is not None:
            self.lines = lines
        if log_result is not None:
            self.log_result = log_result
        if object is not None:
            self.object = object
        if object_type is not None:
            self.object_type = object_type
        if query_id is not None:
            self.query_id = query_id
        if query_type is not None:
            self.query_type = query_type
        if response_length is not None:
            self.response_length = response_length
        if response_status is not None:
            self.response_status = response_status
        if rule_id is not None:
            self.rule_id = rule_id
        if rule_name is not None:
            self.rule_name = rule_name
        if rule_type is not None:
            self.rule_type = rule_type
        if schema is not None:
            self.schema = schema
        if scope_id is not None:
            self.scope_id = scope_id
        if scope_name is not None:
            self.scope_name = scope_name
        if sql_response is not None:
            self.sql_response = sql_response
        if sql_result is not None:
            self.sql_result = sql_result
        if sql_statement is not None:
            self.sql_statement = sql_statement
        if start_time is not None:
            self.start_time = start_time
        if tcp_session_id is not None:
            self.tcp_session_id = tcp_session_id

    @property
    def audit_result(self):
        r"""Gets the audit_result of this SqlDetailBean.

        审计结果

        :return: The audit_result of this SqlDetailBean.
        :rtype: str
        """
        return self._audit_result

    @audit_result.setter
    def audit_result(self, audit_result):
        r"""Sets the audit_result of this SqlDetailBean.

        审计结果

        :param audit_result: The audit_result of this SqlDetailBean.
        :type audit_result: str
        """
        self._audit_result = audit_result

    @property
    def client_port(self):
        r"""Gets the client_port of this SqlDetailBean.

        客户端端口

        :return: The client_port of this SqlDetailBean.
        :rtype: int
        """
        return self._client_port

    @client_port.setter
    def client_port(self, client_port):
        r"""Sets the client_port of this SqlDetailBean.

        客户端端口

        :param client_port: The client_port of this SqlDetailBean.
        :type client_port: int
        """
        self._client_port = client_port

    @property
    def client_ip(self):
        r"""Gets the client_ip of this SqlDetailBean.

        客户端IP

        :return: The client_ip of this SqlDetailBean.
        :rtype: str
        """
        return self._client_ip

    @client_ip.setter
    def client_ip(self, client_ip):
        r"""Sets the client_ip of this SqlDetailBean.

        客户端IP

        :param client_ip: The client_ip of this SqlDetailBean.
        :type client_ip: str
        """
        self._client_ip = client_ip

    @property
    def client_mac(self):
        r"""Gets the client_mac of this SqlDetailBean.

        客户端MAC地址

        :return: The client_mac of this SqlDetailBean.
        :rtype: str
        """
        return self._client_mac

    @client_mac.setter
    def client_mac(self, client_mac):
        r"""Sets the client_mac of this SqlDetailBean.

        客户端MAC地址

        :param client_mac: The client_mac of this SqlDetailBean.
        :type client_mac: str
        """
        self._client_mac = client_mac

    @property
    def client_name(self):
        r"""Gets the client_name of this SqlDetailBean.

        客户端名称

        :return: The client_name of this SqlDetailBean.
        :rtype: str
        """
        return self._client_name

    @client_name.setter
    def client_name(self, client_name):
        r"""Sets the client_name of this SqlDetailBean.

        客户端名称

        :param client_name: The client_name of this SqlDetailBean.
        :type client_name: str
        """
        self._client_name = client_name

    @property
    def client_os_name(self):
        r"""Gets the client_os_name of this SqlDetailBean.

        客户端系统主机名称

        :return: The client_os_name of this SqlDetailBean.
        :rtype: str
        """
        return self._client_os_name

    @client_os_name.setter
    def client_os_name(self, client_os_name):
        r"""Sets the client_os_name of this SqlDetailBean.

        客户端系统主机名称

        :param client_os_name: The client_os_name of this SqlDetailBean.
        :type client_os_name: str
        """
        self._client_os_name = client_os_name

    @property
    def client_os_user(self):
        r"""Gets the client_os_user of this SqlDetailBean.

        客户端操作系统用户名

        :return: The client_os_user of this SqlDetailBean.
        :rtype: str
        """
        return self._client_os_user

    @client_os_user.setter
    def client_os_user(self, client_os_user):
        r"""Sets the client_os_user of this SqlDetailBean.

        客户端操作系统用户名

        :param client_os_user: The client_os_user of this SqlDetailBean.
        :type client_os_user: str
        """
        self._client_os_user = client_os_user

    @property
    def client_port_str(self):
        r"""Gets the client_port_str of this SqlDetailBean.

        客户端端口字符

        :return: The client_port_str of this SqlDetailBean.
        :rtype: str
        """
        return self._client_port_str

    @client_port_str.setter
    def client_port_str(self, client_port_str):
        r"""Sets the client_port_str of this SqlDetailBean.

        客户端端口字符

        :param client_port_str: The client_port_str of this SqlDetailBean.
        :type client_port_str: str
        """
        self._client_port_str = client_port_str

    @property
    def client_tool(self):
        r"""Gets the client_tool of this SqlDetailBean.

        客户端连接工具

        :return: The client_tool of this SqlDetailBean.
        :rtype: str
        """
        return self._client_tool

    @client_tool.setter
    def client_tool(self, client_tool):
        r"""Sets the client_tool of this SqlDetailBean.

        客户端连接工具

        :param client_tool: The client_tool of this SqlDetailBean.
        :type client_tool: str
        """
        self._client_tool = client_tool

    @property
    def db_port(self):
        r"""Gets the db_port of this SqlDetailBean.

        数据库端口

        :return: The db_port of this SqlDetailBean.
        :rtype: int
        """
        return self._db_port

    @db_port.setter
    def db_port(self, db_port):
        r"""Sets the db_port of this SqlDetailBean.

        数据库端口

        :param db_port: The db_port of this SqlDetailBean.
        :type db_port: int
        """
        self._db_port = db_port

    @property
    def db_instance(self):
        r"""Gets the db_instance of this SqlDetailBean.

        数据库实例

        :return: The db_instance of this SqlDetailBean.
        :rtype: str
        """
        return self._db_instance

    @db_instance.setter
    def db_instance(self, db_instance):
        r"""Sets the db_instance of this SqlDetailBean.

        数据库实例

        :param db_instance: The db_instance of this SqlDetailBean.
        :type db_instance: str
        """
        self._db_instance = db_instance

    @property
    def db_ip(self):
        r"""Gets the db_ip of this SqlDetailBean.

        数据库IP

        :return: The db_ip of this SqlDetailBean.
        :rtype: str
        """
        return self._db_ip

    @db_ip.setter
    def db_ip(self, db_ip):
        r"""Sets the db_ip of this SqlDetailBean.

        数据库IP

        :param db_ip: The db_ip of this SqlDetailBean.
        :type db_ip: str
        """
        self._db_ip = db_ip

    @property
    def db_mac(self):
        r"""Gets the db_mac of this SqlDetailBean.

        数据库MAC地址

        :return: The db_mac of this SqlDetailBean.
        :rtype: str
        """
        return self._db_mac

    @db_mac.setter
    def db_mac(self, db_mac):
        r"""Sets the db_mac of this SqlDetailBean.

        数据库MAC地址

        :param db_mac: The db_mac of this SqlDetailBean.
        :type db_mac: str
        """
        self._db_mac = db_mac

    @property
    def db_port_str(self):
        r"""Gets the db_port_str of this SqlDetailBean.

        数据库端口字符

        :return: The db_port_str of this SqlDetailBean.
        :rtype: str
        """
        return self._db_port_str

    @db_port_str.setter
    def db_port_str(self, db_port_str):
        r"""Sets the db_port_str of this SqlDetailBean.

        数据库端口字符

        :param db_port_str: The db_port_str of this SqlDetailBean.
        :type db_port_str: str
        """
        self._db_port_str = db_port_str

    @property
    def db_service_name(self):
        r"""Gets the db_service_name of this SqlDetailBean.

        数据库服务名称

        :return: The db_service_name of this SqlDetailBean.
        :rtype: str
        """
        return self._db_service_name

    @db_service_name.setter
    def db_service_name(self, db_service_name):
        r"""Sets the db_service_name of this SqlDetailBean.

        数据库服务名称

        :param db_service_name: The db_service_name of this SqlDetailBean.
        :type db_service_name: str
        """
        self._db_service_name = db_service_name

    @property
    def db_session_id(self):
        r"""Gets the db_session_id of this SqlDetailBean.

        数据库连接ID

        :return: The db_session_id of this SqlDetailBean.
        :rtype: str
        """
        return self._db_session_id

    @db_session_id.setter
    def db_session_id(self, db_session_id):
        r"""Sets the db_session_id of this SqlDetailBean.

        数据库连接ID

        :param db_session_id: The db_session_id of this SqlDetailBean.
        :type db_session_id: str
        """
        self._db_session_id = db_session_id

    @property
    def db_type(self):
        r"""Gets the db_type of this SqlDetailBean.

        数据库类型

        :return: The db_type of this SqlDetailBean.
        :rtype: str
        """
        return self._db_type

    @db_type.setter
    def db_type(self, db_type):
        r"""Sets the db_type of this SqlDetailBean.

        数据库类型

        :param db_type: The db_type of this SqlDetailBean.
        :type db_type: str
        """
        self._db_type = db_type

    @property
    def db_user(self):
        r"""Gets the db_user of this SqlDetailBean.

        数据库用户

        :return: The db_user of this SqlDetailBean.
        :rtype: str
        """
        return self._db_user

    @db_user.setter
    def db_user(self, db_user):
        r"""Sets the db_user of this SqlDetailBean.

        数据库用户

        :param db_user: The db_user of this SqlDetailBean.
        :type db_user: str
        """
        self._db_user = db_user

    @property
    def end_time(self):
        r"""Gets the end_time of this SqlDetailBean.

        请求结束时间

        :return: The end_time of this SqlDetailBean.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this SqlDetailBean.

        请求结束时间

        :param end_time: The end_time of this SqlDetailBean.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def execute_time(self):
        r"""Gets the execute_time of this SqlDetailBean.

        执行时长

        :return: The execute_time of this SqlDetailBean.
        :rtype: int
        """
        return self._execute_time

    @execute_time.setter
    def execute_time(self, execute_time):
        r"""Sets the execute_time of this SqlDetailBean.

        执行时长

        :param execute_time: The execute_time of this SqlDetailBean.
        :type execute_time: int
        """
        self._execute_time = execute_time

    @property
    def field(self):
        r"""Gets the field of this SqlDetailBean.

        操作对象类型信息

        :return: The field of this SqlDetailBean.
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        r"""Sets the field of this SqlDetailBean.

        操作对象类型信息

        :param field: The field of this SqlDetailBean.
        :type field: str
        """
        self._field = field

    @property
    def id(self):
        r"""Gets the id of this SqlDetailBean.

        记录ID

        :return: The id of this SqlDetailBean.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SqlDetailBean.

        记录ID

        :param id: The id of this SqlDetailBean.
        :type id: str
        """
        self._id = id

    @property
    def level(self):
        r"""Gets the level of this SqlDetailBean.

        风险等级   - LOW：低  - MEDIUM：中  - HIGH：高  - NO_RISK：无

        :return: The level of this SqlDetailBean.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this SqlDetailBean.

        风险等级   - LOW：低  - MEDIUM：中  - HIGH：高  - NO_RISK：无

        :param level: The level of this SqlDetailBean.
        :type level: str
        """
        self._level = level

    @property
    def lines(self):
        r"""Gets the lines of this SqlDetailBean.

        影响行数

        :return: The lines of this SqlDetailBean.
        :rtype: str
        """
        return self._lines

    @lines.setter
    def lines(self, lines):
        r"""Sets the lines of this SqlDetailBean.

        影响行数

        :param lines: The lines of this SqlDetailBean.
        :type lines: str
        """
        self._lines = lines

    @property
    def log_result(self):
        r"""Gets the log_result of this SqlDetailBean.

        登入登出结果

        :return: The log_result of this SqlDetailBean.
        :rtype: str
        """
        return self._log_result

    @log_result.setter
    def log_result(self, log_result):
        r"""Sets the log_result of this SqlDetailBean.

        登入登出结果

        :param log_result: The log_result of this SqlDetailBean.
        :type log_result: str
        """
        self._log_result = log_result

    @property
    def object(self):
        r"""Gets the object of this SqlDetailBean.

        操作对象

        :return: The object of this SqlDetailBean.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        r"""Sets the object of this SqlDetailBean.

        操作对象

        :param object: The object of this SqlDetailBean.
        :type object: str
        """
        self._object = object

    @property
    def object_type(self):
        r"""Gets the object_type of this SqlDetailBean.

        操作对象类型

        :return: The object_type of this SqlDetailBean.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        r"""Sets the object_type of this SqlDetailBean.

        操作对象类型

        :param object_type: The object_type of this SqlDetailBean.
        :type object_type: str
        """
        self._object_type = object_type

    @property
    def query_id(self):
        r"""Gets the query_id of this SqlDetailBean.

        查询ID

        :return: The query_id of this SqlDetailBean.
        :rtype: str
        """
        return self._query_id

    @query_id.setter
    def query_id(self, query_id):
        r"""Sets the query_id of this SqlDetailBean.

        查询ID

        :param query_id: The query_id of this SqlDetailBean.
        :type query_id: str
        """
        self._query_id = query_id

    @property
    def query_type(self):
        r"""Gets the query_type of this SqlDetailBean.

        操作类型

        :return: The query_type of this SqlDetailBean.
        :rtype: str
        """
        return self._query_type

    @query_type.setter
    def query_type(self, query_type):
        r"""Sets the query_type of this SqlDetailBean.

        操作类型

        :param query_type: The query_type of this SqlDetailBean.
        :type query_type: str
        """
        self._query_type = query_type

    @property
    def response_length(self):
        r"""Gets the response_length of this SqlDetailBean.

        数据长度

        :return: The response_length of this SqlDetailBean.
        :rtype: int
        """
        return self._response_length

    @response_length.setter
    def response_length(self, response_length):
        r"""Sets the response_length of this SqlDetailBean.

        数据长度

        :param response_length: The response_length of this SqlDetailBean.
        :type response_length: int
        """
        self._response_length = response_length

    @property
    def response_status(self):
        r"""Gets the response_status of this SqlDetailBean.

        响应状态

        :return: The response_status of this SqlDetailBean.
        :rtype: str
        """
        return self._response_status

    @response_status.setter
    def response_status(self, response_status):
        r"""Sets the response_status of this SqlDetailBean.

        响应状态

        :param response_status: The response_status of this SqlDetailBean.
        :type response_status: str
        """
        self._response_status = response_status

    @property
    def rule_id(self):
        r"""Gets the rule_id of this SqlDetailBean.

        规则ID

        :return: The rule_id of this SqlDetailBean.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        r"""Sets the rule_id of this SqlDetailBean.

        规则ID

        :param rule_id: The rule_id of this SqlDetailBean.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def rule_name(self):
        r"""Gets the rule_name of this SqlDetailBean.

        规则名称

        :return: The rule_name of this SqlDetailBean.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        r"""Sets the rule_name of this SqlDetailBean.

        规则名称

        :param rule_name: The rule_name of this SqlDetailBean.
        :type rule_name: str
        """
        self._rule_name = rule_name

    @property
    def rule_type(self):
        r"""Gets the rule_type of this SqlDetailBean.

        规则类型

        :return: The rule_type of this SqlDetailBean.
        :rtype: str
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        r"""Sets the rule_type of this SqlDetailBean.

        规则类型

        :param rule_type: The rule_type of this SqlDetailBean.
        :type rule_type: str
        """
        self._rule_type = rule_type

    @property
    def schema(self):
        r"""Gets the schema of this SqlDetailBean.

        数据库SCHEMA

        :return: The schema of this SqlDetailBean.
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        r"""Sets the schema of this SqlDetailBean.

        数据库SCHEMA

        :param schema: The schema of this SqlDetailBean.
        :type schema: str
        """
        self._schema = schema

    @property
    def scope_id(self):
        r"""Gets the scope_id of this SqlDetailBean.

        审计范围ID

        :return: The scope_id of this SqlDetailBean.
        :rtype: str
        """
        return self._scope_id

    @scope_id.setter
    def scope_id(self, scope_id):
        r"""Sets the scope_id of this SqlDetailBean.

        审计范围ID

        :param scope_id: The scope_id of this SqlDetailBean.
        :type scope_id: str
        """
        self._scope_id = scope_id

    @property
    def scope_name(self):
        r"""Gets the scope_name of this SqlDetailBean.

        审计范围名称

        :return: The scope_name of this SqlDetailBean.
        :rtype: str
        """
        return self._scope_name

    @scope_name.setter
    def scope_name(self, scope_name):
        r"""Sets the scope_name of this SqlDetailBean.

        审计范围名称

        :param scope_name: The scope_name of this SqlDetailBean.
        :type scope_name: str
        """
        self._scope_name = scope_name

    @property
    def sql_response(self):
        r"""Gets the sql_response of this SqlDetailBean.

        SQL返回结果

        :return: The sql_response of this SqlDetailBean.
        :rtype: str
        """
        return self._sql_response

    @sql_response.setter
    def sql_response(self, sql_response):
        r"""Sets the sql_response of this SqlDetailBean.

        SQL返回结果

        :param sql_response: The sql_response of this SqlDetailBean.
        :type sql_response: str
        """
        self._sql_response = sql_response

    @property
    def sql_result(self):
        r"""Gets the sql_result of this SqlDetailBean.

        SQL处理结果

        :return: The sql_result of this SqlDetailBean.
        :rtype: str
        """
        return self._sql_result

    @sql_result.setter
    def sql_result(self, sql_result):
        r"""Sets the sql_result of this SqlDetailBean.

        SQL处理结果

        :param sql_result: The sql_result of this SqlDetailBean.
        :type sql_result: str
        """
        self._sql_result = sql_result

    @property
    def sql_statement(self):
        r"""Gets the sql_statement of this SqlDetailBean.

        SQL语句内容

        :return: The sql_statement of this SqlDetailBean.
        :rtype: str
        """
        return self._sql_statement

    @sql_statement.setter
    def sql_statement(self, sql_statement):
        r"""Sets the sql_statement of this SqlDetailBean.

        SQL语句内容

        :param sql_statement: The sql_statement of this SqlDetailBean.
        :type sql_statement: str
        """
        self._sql_statement = sql_statement

    @property
    def start_time(self):
        r"""Gets the start_time of this SqlDetailBean.

        请求开始时间

        :return: The start_time of this SqlDetailBean.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this SqlDetailBean.

        请求开始时间

        :param start_time: The start_time of this SqlDetailBean.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def tcp_session_id(self):
        r"""Gets the tcp_session_id of this SqlDetailBean.

        TCP连接ID

        :return: The tcp_session_id of this SqlDetailBean.
        :rtype: str
        """
        return self._tcp_session_id

    @tcp_session_id.setter
    def tcp_session_id(self, tcp_session_id):
        r"""Sets the tcp_session_id of this SqlDetailBean.

        TCP连接ID

        :param tcp_session_id: The tcp_session_id of this SqlDetailBean.
        :type tcp_session_id: str
        """
        self._tcp_session_id = tcp_session_id

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
        if not isinstance(other, SqlDetailBean):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
