# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SqlJob:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'job_type': 'str',
        'queue_name': 'str',
        'owner': 'str',
        'start_time': 'int',
        'duration': 'int',
        'status': 'str',
        'input_row_count': 'int',
        'bad_row_count': 'int',
        'input_size': 'int',
        'result_count': 'int',
        'database_name': 'str',
        'table_name': 'str',
        'with_column_header': 'bool',
        'detail': 'str',
        'engine_type': 'str',
        'statement': 'str',
        'tags': 'list[Tag]',
        'message': 'str',
        'end_time': 'int',
        'cpu_cost': 'str',
        'output_byte': 'str',
        'result_path': 'str',
        'result_format': 'str',
        'execution_details_path': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'job_type': 'job_type',
        'queue_name': 'queue_name',
        'owner': 'owner',
        'start_time': 'start_time',
        'duration': 'duration',
        'status': 'status',
        'input_row_count': 'input_row_count',
        'bad_row_count': 'bad_row_count',
        'input_size': 'input_size',
        'result_count': 'result_count',
        'database_name': 'database_name',
        'table_name': 'table_name',
        'with_column_header': 'with_column_header',
        'detail': 'detail',
        'engine_type': 'engine_type',
        'statement': 'statement',
        'tags': 'tags',
        'message': 'message',
        'end_time': 'end_time',
        'cpu_cost': 'cpu_cost',
        'output_byte': 'output_byte',
        'result_path': 'result_path',
        'result_format': 'result_format',
        'execution_details_path': 'execution_details_path'
    }

    def __init__(self, job_id=None, job_type=None, queue_name=None, owner=None, start_time=None, duration=None, status=None, input_row_count=None, bad_row_count=None, input_size=None, result_count=None, database_name=None, table_name=None, with_column_header=None, detail=None, engine_type=None, statement=None, tags=None, message=None, end_time=None, cpu_cost=None, output_byte=None, result_path=None, result_format=None, execution_details_path=None):
        r"""SqlJob

        The model defined in huaweicloud sdk

        :param job_id: 参数解释:  作业ID 示例: 6d2146a0-c2d5-41bd-8ca0-ca9694ada992 约束限制:  无 取值范围: 无 默认取值: 无
        :type job_id: str
        :param job_type: 参数解释:  指定查询的作业类型，包含DDL、DCL、IMPORT、EXPORT、QUERY、INSERT、DATA_MIGRATION、UPDATE、DELETE、RESTART_QUEUE、SCALE_QUEUE，若要查询所有类型的作业，则传入ALL。 示例: QUERY 约束限制:  无 取值范围: DDL、DCL、IMPORT、EXPORT、QUERY、INSERT、DATA_MIGRATION、UPDATE、DELETE、RESTART_QUEUE、SCALE_QUEUE、ALL 默认取值: 无
        :type job_type: str
        :param queue_name: 作业提交的对列 示例: ci_sql 约束限制:  无 取值范围: 无 默认取值: 无
        :type queue_name: str
        :param owner: 提交作业的用户 示例: tenant1 约束限制:  无 取值范围: 无 默认取值: 无
        :type owner: str
        :param start_time: 作业开始的时间。是单位为“毫秒”的时间戳 示例: 1502349803729 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无
        :type start_time: int
        :param duration: 作业运行时长，单位毫秒 示例: 30000 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无
        :type duration: int
        :param status: 此作业的当前状态 示例: CANCELLED 约束限制:  无 取值范围: LAUNCHING（提交中） RUNNING（运行中） FINISHED（完成） FAILED（失败） CANCELLED（取消） 默认取值: 无
        :type status: str
        :param input_row_count: Insert作业执行过程中扫描的记录条数 示例: 66 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无
        :type input_row_count: int
        :param bad_row_count: Insert作业执行过程中扫描到的错误记录数 示例: 666 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无
        :type bad_row_count: int
        :param input_size: 作业执行过程中扫描文件的大小 示例: 5 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无
        :type input_size: int
        :param result_count: 当前作业返回的结果总条数或insert作业插入的总条数 示例: 55 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无
        :type result_count: int
        :param database_name: 记录其操作的表所在的数据库名称。类型为Import和Export作业才有“database_name”属性 示例: db2 约束限制:  无 取值范围: 无 默认取值: 无
        :type database_name: str
        :param table_name: 记录其操作的表名称。类型为Import和Export作业才有“table_name”属性 示例: t2 约束限制:  无 取值范围: 无 默认取值: 无
        :type table_name: str
        :param with_column_header: Import类型的作业，记录其导入的数据是否包括列名 示例: true 约束限制:  无 取值范围: true, false 默认取值: 无
        :type with_column_header: bool
        :param detail: SQL查询的相关列信息的Json字符串 示例: {\\\&quot;type\\\&quot;:\\\&quot;struct\\\&quot;,\\\&quot;fields\\\&quot;:[{\\\&quot;name\\\&quot;:\\\&quot;name\\\&quot;,\\\&quot;type\\\&quot;:\\\&quot;string\\\&quot;,\\\&quot;nullable\\\&quot;:true,\\\&quot;metadata\\\&quot;:{}},{\\\&quot;name\\\&quot;:\\\&quot;age\\\&quot;,\\\&quot;type\\\&quot;:\\\&quot;integer\\\&quot;,\\\&quot;nullable\\\&quot;:true,\\\&quot;metadata\\\&quot;:{}}]} 约束限制:  符合Json格式的字符串 取值范围: 无 默认取值: 无
        :type detail: str
        :param engine_type: 引擎类型 示例: spark 约束限制:  无 取值范围: spark, hetuEngine 默认取值: 无
        :type engine_type: str
        :param statement: 作业执行的SQL语句 示例: select * from t_json_002 约束限制:  无 取值范围: 无 默认取值: 无
        :type statement: str
        :param tags: 作业标签
        :type tags: list[:class:`huaweicloudsdkdli.v1.Tag`]
        :param message: 系统提示信息 示例: Navicat Data Modeler enables you to build high-quality conceptual, logical and physical data models for a wide variety of audiences. Navicat 15 has added support for the system-wide dark mode. Creativity is intelligence having fun. The On Startup feature allows you to control what tabs appear when you launch Navicat. In the Objects tab, you can use the List List, Detail Detail and ER Diagram ER Diagram buttons to change the object view. If your Internet Service Provider (ISP) does not provide direct access to its server, Secure Tunneling Protocol (SSH) / HTTP is another solution. A man’s best friends are his ten fingers. Export Wizard allows you to export data from tables, collections, views, or query results to any available formats. Navicat 15 has added support for the system-wide dark mode. Secure Sockets Layer(SSL) is a protocol for transmitting private documents via the Internet. A man’s best friends are his ten fingers. Navicat Monitor is a safe, simple and agentless remote server monitoring tool that is packed with powerful features to make your monitoring effective as possible. The past has no power over the present moment. Such sessions are also susceptible to session hijacking, where a malicious user takes over your session once you have authenticated. A man is not old until regrets take the place of dreams. Secure SHell (SSH) is a program to log in into another computer over a network, execute commands on a remote server, and move files from one machine to another. Secure SHell (SSH) is a program to log in into another computer over a network, execute commands on a remote server, and move files from one machine to another. Champions keep playing until they get it right. All journeys have secret destinations of which the traveler is unaware. Flexible settings enable you to set up a custom key for comparison and synchronization. Navicat authorizes you to make connection to remote servers running on different platforms (i.e. Windows, macOS, Linux and UNIX), and supports PAM and GSSAPI authentication. To successfully establish a new connection to local/remote server - no matter via SSL, SSH or HTTP, set the database login information in the General tab. It can also manage cloud databases such as Amazon Redshift, Amazon RDS, Alibaba Cloud. Features in Navicat are sophisticated enough to provide professional developers for all their specific needs, yet easy to learn for users who are new to database server. After logged in the Navicat Cloud feature, the Navigation pane will be divided into Navicat Cloud and My Connections sections. 约束限制:  无 取值范围: 无 默认取值: 无
        :type message: str
        :param end_time: 作业结束的时间。是单位为“毫秒”的时间戳 示例: 1502349803729 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无
        :type end_time: int
        :param cpu_cost: 作业的CPU累计使用量 示例: 15376 约束限制:  无 取值范围: 无 默认取值: 无
        :type cpu_cost: str
        :param output_byte: 作业的输出字节数 示例: 35 约束限制:  无 取值范围: 无 默认取值: 无
        :type output_byte: str
        :param result_path: 作业结果的存储路径。
        :type result_path: str
        :param result_format: 作业结果的存储格式，当前只支持csv
        :type result_format: str
        :param execution_details_path: 作业执行计划的存储路径。
        :type execution_details_path: str
        """
        
        

        self._job_id = None
        self._job_type = None
        self._queue_name = None
        self._owner = None
        self._start_time = None
        self._duration = None
        self._status = None
        self._input_row_count = None
        self._bad_row_count = None
        self._input_size = None
        self._result_count = None
        self._database_name = None
        self._table_name = None
        self._with_column_header = None
        self._detail = None
        self._engine_type = None
        self._statement = None
        self._tags = None
        self._message = None
        self._end_time = None
        self._cpu_cost = None
        self._output_byte = None
        self._result_path = None
        self._result_format = None
        self._execution_details_path = None
        self.discriminator = None

        self.job_id = job_id
        self.job_type = job_type
        self.queue_name = queue_name
        self.owner = owner
        self.start_time = start_time
        if duration is not None:
            self.duration = duration
        self.status = status
        if input_row_count is not None:
            self.input_row_count = input_row_count
        if bad_row_count is not None:
            self.bad_row_count = bad_row_count
        self.input_size = input_size
        self.result_count = result_count
        if database_name is not None:
            self.database_name = database_name
        if table_name is not None:
            self.table_name = table_name
        if with_column_header is not None:
            self.with_column_header = with_column_header
        self.detail = detail
        if engine_type is not None:
            self.engine_type = engine_type
        self.statement = statement
        if tags is not None:
            self.tags = tags
        if message is not None:
            self.message = message
        if end_time is not None:
            self.end_time = end_time
        if cpu_cost is not None:
            self.cpu_cost = cpu_cost
        if output_byte is not None:
            self.output_byte = output_byte
        if result_path is not None:
            self.result_path = result_path
        if result_format is not None:
            self.result_format = result_format
        if execution_details_path is not None:
            self.execution_details_path = execution_details_path

    @property
    def job_id(self):
        r"""Gets the job_id of this SqlJob.

        参数解释:  作业ID 示例: 6d2146a0-c2d5-41bd-8ca0-ca9694ada992 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The job_id of this SqlJob.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this SqlJob.

        参数解释:  作业ID 示例: 6d2146a0-c2d5-41bd-8ca0-ca9694ada992 约束限制:  无 取值范围: 无 默认取值: 无

        :param job_id: The job_id of this SqlJob.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_type(self):
        r"""Gets the job_type of this SqlJob.

        参数解释:  指定查询的作业类型，包含DDL、DCL、IMPORT、EXPORT、QUERY、INSERT、DATA_MIGRATION、UPDATE、DELETE、RESTART_QUEUE、SCALE_QUEUE，若要查询所有类型的作业，则传入ALL。 示例: QUERY 约束限制:  无 取值范围: DDL、DCL、IMPORT、EXPORT、QUERY、INSERT、DATA_MIGRATION、UPDATE、DELETE、RESTART_QUEUE、SCALE_QUEUE、ALL 默认取值: 无

        :return: The job_type of this SqlJob.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this SqlJob.

        参数解释:  指定查询的作业类型，包含DDL、DCL、IMPORT、EXPORT、QUERY、INSERT、DATA_MIGRATION、UPDATE、DELETE、RESTART_QUEUE、SCALE_QUEUE，若要查询所有类型的作业，则传入ALL。 示例: QUERY 约束限制:  无 取值范围: DDL、DCL、IMPORT、EXPORT、QUERY、INSERT、DATA_MIGRATION、UPDATE、DELETE、RESTART_QUEUE、SCALE_QUEUE、ALL 默认取值: 无

        :param job_type: The job_type of this SqlJob.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def queue_name(self):
        r"""Gets the queue_name of this SqlJob.

        作业提交的对列 示例: ci_sql 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The queue_name of this SqlJob.
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        r"""Sets the queue_name of this SqlJob.

        作业提交的对列 示例: ci_sql 约束限制:  无 取值范围: 无 默认取值: 无

        :param queue_name: The queue_name of this SqlJob.
        :type queue_name: str
        """
        self._queue_name = queue_name

    @property
    def owner(self):
        r"""Gets the owner of this SqlJob.

        提交作业的用户 示例: tenant1 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The owner of this SqlJob.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this SqlJob.

        提交作业的用户 示例: tenant1 约束限制:  无 取值范围: 无 默认取值: 无

        :param owner: The owner of this SqlJob.
        :type owner: str
        """
        self._owner = owner

    @property
    def start_time(self):
        r"""Gets the start_time of this SqlJob.

        作业开始的时间。是单位为“毫秒”的时间戳 示例: 1502349803729 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :return: The start_time of this SqlJob.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this SqlJob.

        作业开始的时间。是单位为“毫秒”的时间戳 示例: 1502349803729 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :param start_time: The start_time of this SqlJob.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def duration(self):
        r"""Gets the duration of this SqlJob.

        作业运行时长，单位毫秒 示例: 30000 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :return: The duration of this SqlJob.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this SqlJob.

        作业运行时长，单位毫秒 示例: 30000 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :param duration: The duration of this SqlJob.
        :type duration: int
        """
        self._duration = duration

    @property
    def status(self):
        r"""Gets the status of this SqlJob.

        此作业的当前状态 示例: CANCELLED 约束限制:  无 取值范围: LAUNCHING（提交中） RUNNING（运行中） FINISHED（完成） FAILED（失败） CANCELLED（取消） 默认取值: 无

        :return: The status of this SqlJob.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SqlJob.

        此作业的当前状态 示例: CANCELLED 约束限制:  无 取值范围: LAUNCHING（提交中） RUNNING（运行中） FINISHED（完成） FAILED（失败） CANCELLED（取消） 默认取值: 无

        :param status: The status of this SqlJob.
        :type status: str
        """
        self._status = status

    @property
    def input_row_count(self):
        r"""Gets the input_row_count of this SqlJob.

        Insert作业执行过程中扫描的记录条数 示例: 66 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :return: The input_row_count of this SqlJob.
        :rtype: int
        """
        return self._input_row_count

    @input_row_count.setter
    def input_row_count(self, input_row_count):
        r"""Sets the input_row_count of this SqlJob.

        Insert作业执行过程中扫描的记录条数 示例: 66 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :param input_row_count: The input_row_count of this SqlJob.
        :type input_row_count: int
        """
        self._input_row_count = input_row_count

    @property
    def bad_row_count(self):
        r"""Gets the bad_row_count of this SqlJob.

        Insert作业执行过程中扫描到的错误记录数 示例: 666 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :return: The bad_row_count of this SqlJob.
        :rtype: int
        """
        return self._bad_row_count

    @bad_row_count.setter
    def bad_row_count(self, bad_row_count):
        r"""Sets the bad_row_count of this SqlJob.

        Insert作业执行过程中扫描到的错误记录数 示例: 666 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :param bad_row_count: The bad_row_count of this SqlJob.
        :type bad_row_count: int
        """
        self._bad_row_count = bad_row_count

    @property
    def input_size(self):
        r"""Gets the input_size of this SqlJob.

        作业执行过程中扫描文件的大小 示例: 5 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :return: The input_size of this SqlJob.
        :rtype: int
        """
        return self._input_size

    @input_size.setter
    def input_size(self, input_size):
        r"""Sets the input_size of this SqlJob.

        作业执行过程中扫描文件的大小 示例: 5 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :param input_size: The input_size of this SqlJob.
        :type input_size: int
        """
        self._input_size = input_size

    @property
    def result_count(self):
        r"""Gets the result_count of this SqlJob.

        当前作业返回的结果总条数或insert作业插入的总条数 示例: 55 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :return: The result_count of this SqlJob.
        :rtype: int
        """
        return self._result_count

    @result_count.setter
    def result_count(self, result_count):
        r"""Sets the result_count of this SqlJob.

        当前作业返回的结果总条数或insert作业插入的总条数 示例: 55 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :param result_count: The result_count of this SqlJob.
        :type result_count: int
        """
        self._result_count = result_count

    @property
    def database_name(self):
        r"""Gets the database_name of this SqlJob.

        记录其操作的表所在的数据库名称。类型为Import和Export作业才有“database_name”属性 示例: db2 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The database_name of this SqlJob.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this SqlJob.

        记录其操作的表所在的数据库名称。类型为Import和Export作业才有“database_name”属性 示例: db2 约束限制:  无 取值范围: 无 默认取值: 无

        :param database_name: The database_name of this SqlJob.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def table_name(self):
        r"""Gets the table_name of this SqlJob.

        记录其操作的表名称。类型为Import和Export作业才有“table_name”属性 示例: t2 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The table_name of this SqlJob.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this SqlJob.

        记录其操作的表名称。类型为Import和Export作业才有“table_name”属性 示例: t2 约束限制:  无 取值范围: 无 默认取值: 无

        :param table_name: The table_name of this SqlJob.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def with_column_header(self):
        r"""Gets the with_column_header of this SqlJob.

        Import类型的作业，记录其导入的数据是否包括列名 示例: true 约束限制:  无 取值范围: true, false 默认取值: 无

        :return: The with_column_header of this SqlJob.
        :rtype: bool
        """
        return self._with_column_header

    @with_column_header.setter
    def with_column_header(self, with_column_header):
        r"""Sets the with_column_header of this SqlJob.

        Import类型的作业，记录其导入的数据是否包括列名 示例: true 约束限制:  无 取值范围: true, false 默认取值: 无

        :param with_column_header: The with_column_header of this SqlJob.
        :type with_column_header: bool
        """
        self._with_column_header = with_column_header

    @property
    def detail(self):
        r"""Gets the detail of this SqlJob.

        SQL查询的相关列信息的Json字符串 示例: {\\\"type\\\":\\\"struct\\\",\\\"fields\\\":[{\\\"name\\\":\\\"name\\\",\\\"type\\\":\\\"string\\\",\\\"nullable\\\":true,\\\"metadata\\\":{}},{\\\"name\\\":\\\"age\\\",\\\"type\\\":\\\"integer\\\",\\\"nullable\\\":true,\\\"metadata\\\":{}}]} 约束限制:  符合Json格式的字符串 取值范围: 无 默认取值: 无

        :return: The detail of this SqlJob.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        r"""Sets the detail of this SqlJob.

        SQL查询的相关列信息的Json字符串 示例: {\\\"type\\\":\\\"struct\\\",\\\"fields\\\":[{\\\"name\\\":\\\"name\\\",\\\"type\\\":\\\"string\\\",\\\"nullable\\\":true,\\\"metadata\\\":{}},{\\\"name\\\":\\\"age\\\",\\\"type\\\":\\\"integer\\\",\\\"nullable\\\":true,\\\"metadata\\\":{}}]} 约束限制:  符合Json格式的字符串 取值范围: 无 默认取值: 无

        :param detail: The detail of this SqlJob.
        :type detail: str
        """
        self._detail = detail

    @property
    def engine_type(self):
        r"""Gets the engine_type of this SqlJob.

        引擎类型 示例: spark 约束限制:  无 取值范围: spark, hetuEngine 默认取值: 无

        :return: The engine_type of this SqlJob.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this SqlJob.

        引擎类型 示例: spark 约束限制:  无 取值范围: spark, hetuEngine 默认取值: 无

        :param engine_type: The engine_type of this SqlJob.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def statement(self):
        r"""Gets the statement of this SqlJob.

        作业执行的SQL语句 示例: select * from t_json_002 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The statement of this SqlJob.
        :rtype: str
        """
        return self._statement

    @statement.setter
    def statement(self, statement):
        r"""Sets the statement of this SqlJob.

        作业执行的SQL语句 示例: select * from t_json_002 约束限制:  无 取值范围: 无 默认取值: 无

        :param statement: The statement of this SqlJob.
        :type statement: str
        """
        self._statement = statement

    @property
    def tags(self):
        r"""Gets the tags of this SqlJob.

        作业标签

        :return: The tags of this SqlJob.
        :rtype: list[:class:`huaweicloudsdkdli.v1.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this SqlJob.

        作业标签

        :param tags: The tags of this SqlJob.
        :type tags: list[:class:`huaweicloudsdkdli.v1.Tag`]
        """
        self._tags = tags

    @property
    def message(self):
        r"""Gets the message of this SqlJob.

        系统提示信息 示例: Navicat Data Modeler enables you to build high-quality conceptual, logical and physical data models for a wide variety of audiences. Navicat 15 has added support for the system-wide dark mode. Creativity is intelligence having fun. The On Startup feature allows you to control what tabs appear when you launch Navicat. In the Objects tab, you can use the List List, Detail Detail and ER Diagram ER Diagram buttons to change the object view. If your Internet Service Provider (ISP) does not provide direct access to its server, Secure Tunneling Protocol (SSH) / HTTP is another solution. A man’s best friends are his ten fingers. Export Wizard allows you to export data from tables, collections, views, or query results to any available formats. Navicat 15 has added support for the system-wide dark mode. Secure Sockets Layer(SSL) is a protocol for transmitting private documents via the Internet. A man’s best friends are his ten fingers. Navicat Monitor is a safe, simple and agentless remote server monitoring tool that is packed with powerful features to make your monitoring effective as possible. The past has no power over the present moment. Such sessions are also susceptible to session hijacking, where a malicious user takes over your session once you have authenticated. A man is not old until regrets take the place of dreams. Secure SHell (SSH) is a program to log in into another computer over a network, execute commands on a remote server, and move files from one machine to another. Secure SHell (SSH) is a program to log in into another computer over a network, execute commands on a remote server, and move files from one machine to another. Champions keep playing until they get it right. All journeys have secret destinations of which the traveler is unaware. Flexible settings enable you to set up a custom key for comparison and synchronization. Navicat authorizes you to make connection to remote servers running on different platforms (i.e. Windows, macOS, Linux and UNIX), and supports PAM and GSSAPI authentication. To successfully establish a new connection to local/remote server - no matter via SSL, SSH or HTTP, set the database login information in the General tab. It can also manage cloud databases such as Amazon Redshift, Amazon RDS, Alibaba Cloud. Features in Navicat are sophisticated enough to provide professional developers for all their specific needs, yet easy to learn for users who are new to database server. After logged in the Navicat Cloud feature, the Navigation pane will be divided into Navicat Cloud and My Connections sections. 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The message of this SqlJob.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this SqlJob.

        系统提示信息 示例: Navicat Data Modeler enables you to build high-quality conceptual, logical and physical data models for a wide variety of audiences. Navicat 15 has added support for the system-wide dark mode. Creativity is intelligence having fun. The On Startup feature allows you to control what tabs appear when you launch Navicat. In the Objects tab, you can use the List List, Detail Detail and ER Diagram ER Diagram buttons to change the object view. If your Internet Service Provider (ISP) does not provide direct access to its server, Secure Tunneling Protocol (SSH) / HTTP is another solution. A man’s best friends are his ten fingers. Export Wizard allows you to export data from tables, collections, views, or query results to any available formats. Navicat 15 has added support for the system-wide dark mode. Secure Sockets Layer(SSL) is a protocol for transmitting private documents via the Internet. A man’s best friends are his ten fingers. Navicat Monitor is a safe, simple and agentless remote server monitoring tool that is packed with powerful features to make your monitoring effective as possible. The past has no power over the present moment. Such sessions are also susceptible to session hijacking, where a malicious user takes over your session once you have authenticated. A man is not old until regrets take the place of dreams. Secure SHell (SSH) is a program to log in into another computer over a network, execute commands on a remote server, and move files from one machine to another. Secure SHell (SSH) is a program to log in into another computer over a network, execute commands on a remote server, and move files from one machine to another. Champions keep playing until they get it right. All journeys have secret destinations of which the traveler is unaware. Flexible settings enable you to set up a custom key for comparison and synchronization. Navicat authorizes you to make connection to remote servers running on different platforms (i.e. Windows, macOS, Linux and UNIX), and supports PAM and GSSAPI authentication. To successfully establish a new connection to local/remote server - no matter via SSL, SSH or HTTP, set the database login information in the General tab. It can also manage cloud databases such as Amazon Redshift, Amazon RDS, Alibaba Cloud. Features in Navicat are sophisticated enough to provide professional developers for all their specific needs, yet easy to learn for users who are new to database server. After logged in the Navicat Cloud feature, the Navigation pane will be divided into Navicat Cloud and My Connections sections. 约束限制:  无 取值范围: 无 默认取值: 无

        :param message: The message of this SqlJob.
        :type message: str
        """
        self._message = message

    @property
    def end_time(self):
        r"""Gets the end_time of this SqlJob.

        作业结束的时间。是单位为“毫秒”的时间戳 示例: 1502349803729 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :return: The end_time of this SqlJob.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this SqlJob.

        作业结束的时间。是单位为“毫秒”的时间戳 示例: 1502349803729 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :param end_time: The end_time of this SqlJob.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def cpu_cost(self):
        r"""Gets the cpu_cost of this SqlJob.

        作业的CPU累计使用量 示例: 15376 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The cpu_cost of this SqlJob.
        :rtype: str
        """
        return self._cpu_cost

    @cpu_cost.setter
    def cpu_cost(self, cpu_cost):
        r"""Sets the cpu_cost of this SqlJob.

        作业的CPU累计使用量 示例: 15376 约束限制:  无 取值范围: 无 默认取值: 无

        :param cpu_cost: The cpu_cost of this SqlJob.
        :type cpu_cost: str
        """
        self._cpu_cost = cpu_cost

    @property
    def output_byte(self):
        r"""Gets the output_byte of this SqlJob.

        作业的输出字节数 示例: 35 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The output_byte of this SqlJob.
        :rtype: str
        """
        return self._output_byte

    @output_byte.setter
    def output_byte(self, output_byte):
        r"""Sets the output_byte of this SqlJob.

        作业的输出字节数 示例: 35 约束限制:  无 取值范围: 无 默认取值: 无

        :param output_byte: The output_byte of this SqlJob.
        :type output_byte: str
        """
        self._output_byte = output_byte

    @property
    def result_path(self):
        r"""Gets the result_path of this SqlJob.

        作业结果的存储路径。

        :return: The result_path of this SqlJob.
        :rtype: str
        """
        return self._result_path

    @result_path.setter
    def result_path(self, result_path):
        r"""Sets the result_path of this SqlJob.

        作业结果的存储路径。

        :param result_path: The result_path of this SqlJob.
        :type result_path: str
        """
        self._result_path = result_path

    @property
    def result_format(self):
        r"""Gets the result_format of this SqlJob.

        作业结果的存储格式，当前只支持csv

        :return: The result_format of this SqlJob.
        :rtype: str
        """
        return self._result_format

    @result_format.setter
    def result_format(self, result_format):
        r"""Sets the result_format of this SqlJob.

        作业结果的存储格式，当前只支持csv

        :param result_format: The result_format of this SqlJob.
        :type result_format: str
        """
        self._result_format = result_format

    @property
    def execution_details_path(self):
        r"""Gets the execution_details_path of this SqlJob.

        作业执行计划的存储路径。

        :return: The execution_details_path of this SqlJob.
        :rtype: str
        """
        return self._execution_details_path

    @execution_details_path.setter
    def execution_details_path(self, execution_details_path):
        r"""Sets the execution_details_path of this SqlJob.

        作业执行计划的存储路径。

        :param execution_details_path: The execution_details_path of this SqlJob.
        :type execution_details_path: str
        """
        self._execution_details_path = execution_details_path

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
        if not isinstance(other, SqlJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
