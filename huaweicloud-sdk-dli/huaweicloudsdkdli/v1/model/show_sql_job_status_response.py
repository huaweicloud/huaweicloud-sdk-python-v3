# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSqlJobStatusResponse(SdkResponse):

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
        'detail': 'str',
        'user_conf': 'str',
        'result_path': 'str',
        'execution_details_path': 'str',
        'result_format': 'str',
        'statement': 'str',
        'is_success': 'bool',
        'message': 'str',
        'job_mode': 'str',
        'tags': 'list[Tag]'
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
        'detail': 'detail',
        'user_conf': 'user_conf',
        'result_path': 'result_path',
        'execution_details_path': 'execution_details_path',
        'result_format': 'result_format',
        'statement': 'statement',
        'is_success': 'is_success',
        'message': 'message',
        'job_mode': 'job_mode',
        'tags': 'tags'
    }

    def __init__(self, job_id=None, job_type=None, queue_name=None, owner=None, start_time=None, duration=None, status=None, input_row_count=None, bad_row_count=None, input_size=None, result_count=None, database_name=None, table_name=None, detail=None, user_conf=None, result_path=None, execution_details_path=None, result_format=None, statement=None, is_success=None, message=None, job_mode=None, tags=None):
        r"""ShowSqlJobStatusResponse

        The model defined in huaweicloud sdk

        :param job_id: 参数解释:  作业ID 示例: 6d2146a0-c2d5-41bd-8ca0-ca9694ada992 约束限制:  无 取值范围: 任意字符串 默认取值: 无
        :type job_id: str
        :param job_type: 参数解释:  作业类型 示例: 指定查询的作业类型，包含DDL、DCL、IMPORT、EXPORT、QUERY、INSERT、DATA_MIGRATION、UPDATE、DELETE、RESTART_QUEUE、SCALE_QUEUE，若要查询所有类型的作业，则传入ALL。 约束限制:  无 取值范围: DDL、DCL、IMPORT、EXPORT、QUERY、INSERT、DATA_MIGRATION、UPDATE、DELETE、RESTART_QUEUE、SCALE_QUEUE、ALL 默认取值: 无
        :type job_type: str
        :param queue_name: 参数解释:  作业提交的队列 示例: dli_sql 约束限制:  无 取值范围: 无 默认取值: 无
        :type queue_name: str
        :param owner: 参数解释:  提交作业的用户 示例: ei_dlics_d00352431 约束限制:  无 取值范围: 无 默认取值: 无
        :type owner: str
        :param start_time: 参数解释:  作业开始的时间。是单位为“毫秒”的时间戳 示例: 1502349803729 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无
        :type start_time: int
        :param duration: 参数解释:  作业运行时长，单位毫秒 示例: 1000 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无
        :type duration: int
        :param status: 参数解释:  此作业的当前状态 示例: CANCELLED 约束限制:  无 取值范围: LAUNCHING（提交） RUNNING（运行中） FINISH（完成） FAILED（失败） CANCELLED（取消） 默认取值: 无
        :type status: str
        :param input_row_count: 参数解释:  Insert作业执行过程中扫描的记录条数 示例: 66 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无
        :type input_row_count: int
        :param bad_row_count: 参数解释:  Insert作业执行过程中扫描到的错误记录数 示例: 666 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无
        :type bad_row_count: int
        :param input_size: 参数解释:  作业执行过程中扫描文件的大小 示例: 5 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无
        :type input_size: int
        :param result_count: 参数解释:  当前作业返回的结果总条数或insert作业插入的总条数 示例: 55 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无
        :type result_count: int
        :param database_name: 参数解释:  记录其操作的表所在的数据库名称。类型为Import和Export作业才有“database_name”属性 示例: db2 约束限制:  无 取值范围: 无 默认取值: 无
        :type database_name: str
        :param table_name: 参数解释:  记录其操作的表名称。类型为Import和Export作业才有“table_name”属性 示例: t2 约束限制:  无 取值范围: 无 默认取值: 无
        :type table_name: str
        :param detail: 参数解释:  SQL查询的相关列信息的Json字符串 示例: {\\\&quot;type\\\&quot;:\\\&quot;struct\\\&quot;,\\\&quot;fields\\\&quot;:[{\\\&quot;name\\\&quot;:\\\&quot;name\\\&quot;,\\\&quot;type\\\&quot;:\\\&quot;string\\\&quot;,\\\&quot;nullable\\\&quot;:true,\\\&quot;metadata\\\&quot;:{}},{\\\&quot;name\\\&quot;:\\\&quot;age\\\&quot;,\\\&quot;type\\\&quot;:\\\&quot;integer\\\&quot;,\\\&quot;nullable\\\&quot;:true,\\\&quot;metadata\\\&quot;:{}}]} 约束限制:  符合JSON格式 取值范围: 无 默认取值: 无
        :type detail: str
        :param user_conf: 参数解释:  SQL配置参数信息Json字符串 示例: {\\\&quot;type\\\&quot;:\\\&quot;struct\\\&quot;,\\\&quot;fields\\\&quot;:[{\\\&quot;name\\\&quot;:\\\&quot;name\\\&quot;,\\\&quot;type\\\&quot;:\\\&quot;string\\\&quot;,\\\&quot;nullable\\\&quot;:true,\\\&quot;metadata\\\&quot;:{}},{\\\&quot;name\\\&quot;:\\\&quot;age\\\&quot;,\\\&quot;type\\\&quot;:\\\&quot;integer\\\&quot;,\\\&quot;nullable\\\&quot;:true,\\\&quot;metadata\\\&quot;:{}}]} 约束限制:  符合JSON格式 取值范围: 无 默认取值: 无
        :type user_conf: str
        :param result_path: 参数解释:  查询结果OBS路径 示例: obs://bucketName/jobs/result/011c99a26ae84a1bb963a75e7637d3fd/2023/11/10/229b23ad-5033-40ed-ad70-fda900f2f04e 约束限制:  符合OBS路径格式，obs://* 取值范围: 无 默认取值: 无
        :type result_path: str
        :param execution_details_path: 参数解释:  查询作业执行计划OBS路径 示例: obs://bucketName/jobs/execution_details/011c99a26ae84a1bb963a75e7637d3fd/2023/11/10/229b23ad-5033-40ed-ad70-fda900f2f04e 约束限制:  符合OBS路径格式，obs://* 取值范围: 无 默认取值: 无
        :type execution_details_path: str
        :param result_format: 参数解释:  查询结果格式 示例: csv 约束限制:  无 取值范围: csv 默认取值: 无
        :type result_format: str
        :param statement: 参数解释:  作业执行的SQL语句 示例: select * from t_json_002 约束限制:  符合SQL格式 取值范围: 无 默认取值: 无
        :type statement: str
        :param is_success: 参数解释:  执行请求是否成功。true表示请求执行成功 示例: true 约束限制:  无 取值范围: true、false 默认取值: 无
        :type is_success: bool
        :param message: 参数解释:  系统提示信息，执行成功时，信息可能为空 示例: success 约束限制:  无 取值范围: 无 默认取值: 无
        :type message: str
        :param job_mode: 参数解释:  作业执行方式 示例: async 约束限制:  无 取值范围: async（同步） sync（异步） 默认取值: 无
        :type job_mode: str
        :param tags: 作业标签
        :type tags: list[:class:`huaweicloudsdkdli.v1.Tag`]
        """
        
        super(ShowSqlJobStatusResponse, self).__init__()

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
        self._detail = None
        self._user_conf = None
        self._result_path = None
        self._execution_details_path = None
        self._result_format = None
        self._statement = None
        self._is_success = None
        self._message = None
        self._job_mode = None
        self._tags = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if job_type is not None:
            self.job_type = job_type
        if queue_name is not None:
            self.queue_name = queue_name
        if owner is not None:
            self.owner = owner
        if start_time is not None:
            self.start_time = start_time
        if duration is not None:
            self.duration = duration
        if status is not None:
            self.status = status
        if input_row_count is not None:
            self.input_row_count = input_row_count
        if bad_row_count is not None:
            self.bad_row_count = bad_row_count
        if input_size is not None:
            self.input_size = input_size
        if result_count is not None:
            self.result_count = result_count
        if database_name is not None:
            self.database_name = database_name
        if table_name is not None:
            self.table_name = table_name
        if detail is not None:
            self.detail = detail
        if user_conf is not None:
            self.user_conf = user_conf
        if result_path is not None:
            self.result_path = result_path
        if execution_details_path is not None:
            self.execution_details_path = execution_details_path
        if result_format is not None:
            self.result_format = result_format
        if statement is not None:
            self.statement = statement
        if is_success is not None:
            self.is_success = is_success
        if message is not None:
            self.message = message
        if job_mode is not None:
            self.job_mode = job_mode
        if tags is not None:
            self.tags = tags

    @property
    def job_id(self):
        r"""Gets the job_id of this ShowSqlJobStatusResponse.

        参数解释:  作业ID 示例: 6d2146a0-c2d5-41bd-8ca0-ca9694ada992 约束限制:  无 取值范围: 任意字符串 默认取值: 无

        :return: The job_id of this ShowSqlJobStatusResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ShowSqlJobStatusResponse.

        参数解释:  作业ID 示例: 6d2146a0-c2d5-41bd-8ca0-ca9694ada992 约束限制:  无 取值范围: 任意字符串 默认取值: 无

        :param job_id: The job_id of this ShowSqlJobStatusResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_type(self):
        r"""Gets the job_type of this ShowSqlJobStatusResponse.

        参数解释:  作业类型 示例: 指定查询的作业类型，包含DDL、DCL、IMPORT、EXPORT、QUERY、INSERT、DATA_MIGRATION、UPDATE、DELETE、RESTART_QUEUE、SCALE_QUEUE，若要查询所有类型的作业，则传入ALL。 约束限制:  无 取值范围: DDL、DCL、IMPORT、EXPORT、QUERY、INSERT、DATA_MIGRATION、UPDATE、DELETE、RESTART_QUEUE、SCALE_QUEUE、ALL 默认取值: 无

        :return: The job_type of this ShowSqlJobStatusResponse.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this ShowSqlJobStatusResponse.

        参数解释:  作业类型 示例: 指定查询的作业类型，包含DDL、DCL、IMPORT、EXPORT、QUERY、INSERT、DATA_MIGRATION、UPDATE、DELETE、RESTART_QUEUE、SCALE_QUEUE，若要查询所有类型的作业，则传入ALL。 约束限制:  无 取值范围: DDL、DCL、IMPORT、EXPORT、QUERY、INSERT、DATA_MIGRATION、UPDATE、DELETE、RESTART_QUEUE、SCALE_QUEUE、ALL 默认取值: 无

        :param job_type: The job_type of this ShowSqlJobStatusResponse.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def queue_name(self):
        r"""Gets the queue_name of this ShowSqlJobStatusResponse.

        参数解释:  作业提交的队列 示例: dli_sql 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The queue_name of this ShowSqlJobStatusResponse.
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        r"""Sets the queue_name of this ShowSqlJobStatusResponse.

        参数解释:  作业提交的队列 示例: dli_sql 约束限制:  无 取值范围: 无 默认取值: 无

        :param queue_name: The queue_name of this ShowSqlJobStatusResponse.
        :type queue_name: str
        """
        self._queue_name = queue_name

    @property
    def owner(self):
        r"""Gets the owner of this ShowSqlJobStatusResponse.

        参数解释:  提交作业的用户 示例: ei_dlics_d00352431 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The owner of this ShowSqlJobStatusResponse.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this ShowSqlJobStatusResponse.

        参数解释:  提交作业的用户 示例: ei_dlics_d00352431 约束限制:  无 取值范围: 无 默认取值: 无

        :param owner: The owner of this ShowSqlJobStatusResponse.
        :type owner: str
        """
        self._owner = owner

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowSqlJobStatusResponse.

        参数解释:  作业开始的时间。是单位为“毫秒”的时间戳 示例: 1502349803729 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :return: The start_time of this ShowSqlJobStatusResponse.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowSqlJobStatusResponse.

        参数解释:  作业开始的时间。是单位为“毫秒”的时间戳 示例: 1502349803729 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :param start_time: The start_time of this ShowSqlJobStatusResponse.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def duration(self):
        r"""Gets the duration of this ShowSqlJobStatusResponse.

        参数解释:  作业运行时长，单位毫秒 示例: 1000 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :return: The duration of this ShowSqlJobStatusResponse.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this ShowSqlJobStatusResponse.

        参数解释:  作业运行时长，单位毫秒 示例: 1000 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :param duration: The duration of this ShowSqlJobStatusResponse.
        :type duration: int
        """
        self._duration = duration

    @property
    def status(self):
        r"""Gets the status of this ShowSqlJobStatusResponse.

        参数解释:  此作业的当前状态 示例: CANCELLED 约束限制:  无 取值范围: LAUNCHING（提交） RUNNING（运行中） FINISH（完成） FAILED（失败） CANCELLED（取消） 默认取值: 无

        :return: The status of this ShowSqlJobStatusResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowSqlJobStatusResponse.

        参数解释:  此作业的当前状态 示例: CANCELLED 约束限制:  无 取值范围: LAUNCHING（提交） RUNNING（运行中） FINISH（完成） FAILED（失败） CANCELLED（取消） 默认取值: 无

        :param status: The status of this ShowSqlJobStatusResponse.
        :type status: str
        """
        self._status = status

    @property
    def input_row_count(self):
        r"""Gets the input_row_count of this ShowSqlJobStatusResponse.

        参数解释:  Insert作业执行过程中扫描的记录条数 示例: 66 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :return: The input_row_count of this ShowSqlJobStatusResponse.
        :rtype: int
        """
        return self._input_row_count

    @input_row_count.setter
    def input_row_count(self, input_row_count):
        r"""Sets the input_row_count of this ShowSqlJobStatusResponse.

        参数解释:  Insert作业执行过程中扫描的记录条数 示例: 66 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :param input_row_count: The input_row_count of this ShowSqlJobStatusResponse.
        :type input_row_count: int
        """
        self._input_row_count = input_row_count

    @property
    def bad_row_count(self):
        r"""Gets the bad_row_count of this ShowSqlJobStatusResponse.

        参数解释:  Insert作业执行过程中扫描到的错误记录数 示例: 666 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :return: The bad_row_count of this ShowSqlJobStatusResponse.
        :rtype: int
        """
        return self._bad_row_count

    @bad_row_count.setter
    def bad_row_count(self, bad_row_count):
        r"""Sets the bad_row_count of this ShowSqlJobStatusResponse.

        参数解释:  Insert作业执行过程中扫描到的错误记录数 示例: 666 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :param bad_row_count: The bad_row_count of this ShowSqlJobStatusResponse.
        :type bad_row_count: int
        """
        self._bad_row_count = bad_row_count

    @property
    def input_size(self):
        r"""Gets the input_size of this ShowSqlJobStatusResponse.

        参数解释:  作业执行过程中扫描文件的大小 示例: 5 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :return: The input_size of this ShowSqlJobStatusResponse.
        :rtype: int
        """
        return self._input_size

    @input_size.setter
    def input_size(self, input_size):
        r"""Sets the input_size of this ShowSqlJobStatusResponse.

        参数解释:  作业执行过程中扫描文件的大小 示例: 5 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :param input_size: The input_size of this ShowSqlJobStatusResponse.
        :type input_size: int
        """
        self._input_size = input_size

    @property
    def result_count(self):
        r"""Gets the result_count of this ShowSqlJobStatusResponse.

        参数解释:  当前作业返回的结果总条数或insert作业插入的总条数 示例: 55 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :return: The result_count of this ShowSqlJobStatusResponse.
        :rtype: int
        """
        return self._result_count

    @result_count.setter
    def result_count(self, result_count):
        r"""Sets the result_count of this ShowSqlJobStatusResponse.

        参数解释:  当前作业返回的结果总条数或insert作业插入的总条数 示例: 55 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :param result_count: The result_count of this ShowSqlJobStatusResponse.
        :type result_count: int
        """
        self._result_count = result_count

    @property
    def database_name(self):
        r"""Gets the database_name of this ShowSqlJobStatusResponse.

        参数解释:  记录其操作的表所在的数据库名称。类型为Import和Export作业才有“database_name”属性 示例: db2 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The database_name of this ShowSqlJobStatusResponse.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this ShowSqlJobStatusResponse.

        参数解释:  记录其操作的表所在的数据库名称。类型为Import和Export作业才有“database_name”属性 示例: db2 约束限制:  无 取值范围: 无 默认取值: 无

        :param database_name: The database_name of this ShowSqlJobStatusResponse.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def table_name(self):
        r"""Gets the table_name of this ShowSqlJobStatusResponse.

        参数解释:  记录其操作的表名称。类型为Import和Export作业才有“table_name”属性 示例: t2 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The table_name of this ShowSqlJobStatusResponse.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this ShowSqlJobStatusResponse.

        参数解释:  记录其操作的表名称。类型为Import和Export作业才有“table_name”属性 示例: t2 约束限制:  无 取值范围: 无 默认取值: 无

        :param table_name: The table_name of this ShowSqlJobStatusResponse.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def detail(self):
        r"""Gets the detail of this ShowSqlJobStatusResponse.

        参数解释:  SQL查询的相关列信息的Json字符串 示例: {\\\"type\\\":\\\"struct\\\",\\\"fields\\\":[{\\\"name\\\":\\\"name\\\",\\\"type\\\":\\\"string\\\",\\\"nullable\\\":true,\\\"metadata\\\":{}},{\\\"name\\\":\\\"age\\\",\\\"type\\\":\\\"integer\\\",\\\"nullable\\\":true,\\\"metadata\\\":{}}]} 约束限制:  符合JSON格式 取值范围: 无 默认取值: 无

        :return: The detail of this ShowSqlJobStatusResponse.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        r"""Sets the detail of this ShowSqlJobStatusResponse.

        参数解释:  SQL查询的相关列信息的Json字符串 示例: {\\\"type\\\":\\\"struct\\\",\\\"fields\\\":[{\\\"name\\\":\\\"name\\\",\\\"type\\\":\\\"string\\\",\\\"nullable\\\":true,\\\"metadata\\\":{}},{\\\"name\\\":\\\"age\\\",\\\"type\\\":\\\"integer\\\",\\\"nullable\\\":true,\\\"metadata\\\":{}}]} 约束限制:  符合JSON格式 取值范围: 无 默认取值: 无

        :param detail: The detail of this ShowSqlJobStatusResponse.
        :type detail: str
        """
        self._detail = detail

    @property
    def user_conf(self):
        r"""Gets the user_conf of this ShowSqlJobStatusResponse.

        参数解释:  SQL配置参数信息Json字符串 示例: {\\\"type\\\":\\\"struct\\\",\\\"fields\\\":[{\\\"name\\\":\\\"name\\\",\\\"type\\\":\\\"string\\\",\\\"nullable\\\":true,\\\"metadata\\\":{}},{\\\"name\\\":\\\"age\\\",\\\"type\\\":\\\"integer\\\",\\\"nullable\\\":true,\\\"metadata\\\":{}}]} 约束限制:  符合JSON格式 取值范围: 无 默认取值: 无

        :return: The user_conf of this ShowSqlJobStatusResponse.
        :rtype: str
        """
        return self._user_conf

    @user_conf.setter
    def user_conf(self, user_conf):
        r"""Sets the user_conf of this ShowSqlJobStatusResponse.

        参数解释:  SQL配置参数信息Json字符串 示例: {\\\"type\\\":\\\"struct\\\",\\\"fields\\\":[{\\\"name\\\":\\\"name\\\",\\\"type\\\":\\\"string\\\",\\\"nullable\\\":true,\\\"metadata\\\":{}},{\\\"name\\\":\\\"age\\\",\\\"type\\\":\\\"integer\\\",\\\"nullable\\\":true,\\\"metadata\\\":{}}]} 约束限制:  符合JSON格式 取值范围: 无 默认取值: 无

        :param user_conf: The user_conf of this ShowSqlJobStatusResponse.
        :type user_conf: str
        """
        self._user_conf = user_conf

    @property
    def result_path(self):
        r"""Gets the result_path of this ShowSqlJobStatusResponse.

        参数解释:  查询结果OBS路径 示例: obs://bucketName/jobs/result/011c99a26ae84a1bb963a75e7637d3fd/2023/11/10/229b23ad-5033-40ed-ad70-fda900f2f04e 约束限制:  符合OBS路径格式，obs://* 取值范围: 无 默认取值: 无

        :return: The result_path of this ShowSqlJobStatusResponse.
        :rtype: str
        """
        return self._result_path

    @result_path.setter
    def result_path(self, result_path):
        r"""Sets the result_path of this ShowSqlJobStatusResponse.

        参数解释:  查询结果OBS路径 示例: obs://bucketName/jobs/result/011c99a26ae84a1bb963a75e7637d3fd/2023/11/10/229b23ad-5033-40ed-ad70-fda900f2f04e 约束限制:  符合OBS路径格式，obs://* 取值范围: 无 默认取值: 无

        :param result_path: The result_path of this ShowSqlJobStatusResponse.
        :type result_path: str
        """
        self._result_path = result_path

    @property
    def execution_details_path(self):
        r"""Gets the execution_details_path of this ShowSqlJobStatusResponse.

        参数解释:  查询作业执行计划OBS路径 示例: obs://bucketName/jobs/execution_details/011c99a26ae84a1bb963a75e7637d3fd/2023/11/10/229b23ad-5033-40ed-ad70-fda900f2f04e 约束限制:  符合OBS路径格式，obs://* 取值范围: 无 默认取值: 无

        :return: The execution_details_path of this ShowSqlJobStatusResponse.
        :rtype: str
        """
        return self._execution_details_path

    @execution_details_path.setter
    def execution_details_path(self, execution_details_path):
        r"""Sets the execution_details_path of this ShowSqlJobStatusResponse.

        参数解释:  查询作业执行计划OBS路径 示例: obs://bucketName/jobs/execution_details/011c99a26ae84a1bb963a75e7637d3fd/2023/11/10/229b23ad-5033-40ed-ad70-fda900f2f04e 约束限制:  符合OBS路径格式，obs://* 取值范围: 无 默认取值: 无

        :param execution_details_path: The execution_details_path of this ShowSqlJobStatusResponse.
        :type execution_details_path: str
        """
        self._execution_details_path = execution_details_path

    @property
    def result_format(self):
        r"""Gets the result_format of this ShowSqlJobStatusResponse.

        参数解释:  查询结果格式 示例: csv 约束限制:  无 取值范围: csv 默认取值: 无

        :return: The result_format of this ShowSqlJobStatusResponse.
        :rtype: str
        """
        return self._result_format

    @result_format.setter
    def result_format(self, result_format):
        r"""Sets the result_format of this ShowSqlJobStatusResponse.

        参数解释:  查询结果格式 示例: csv 约束限制:  无 取值范围: csv 默认取值: 无

        :param result_format: The result_format of this ShowSqlJobStatusResponse.
        :type result_format: str
        """
        self._result_format = result_format

    @property
    def statement(self):
        r"""Gets the statement of this ShowSqlJobStatusResponse.

        参数解释:  作业执行的SQL语句 示例: select * from t_json_002 约束限制:  符合SQL格式 取值范围: 无 默认取值: 无

        :return: The statement of this ShowSqlJobStatusResponse.
        :rtype: str
        """
        return self._statement

    @statement.setter
    def statement(self, statement):
        r"""Sets the statement of this ShowSqlJobStatusResponse.

        参数解释:  作业执行的SQL语句 示例: select * from t_json_002 约束限制:  符合SQL格式 取值范围: 无 默认取值: 无

        :param statement: The statement of this ShowSqlJobStatusResponse.
        :type statement: str
        """
        self._statement = statement

    @property
    def is_success(self):
        r"""Gets the is_success of this ShowSqlJobStatusResponse.

        参数解释:  执行请求是否成功。true表示请求执行成功 示例: true 约束限制:  无 取值范围: true、false 默认取值: 无

        :return: The is_success of this ShowSqlJobStatusResponse.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        r"""Sets the is_success of this ShowSqlJobStatusResponse.

        参数解释:  执行请求是否成功。true表示请求执行成功 示例: true 约束限制:  无 取值范围: true、false 默认取值: 无

        :param is_success: The is_success of this ShowSqlJobStatusResponse.
        :type is_success: bool
        """
        self._is_success = is_success

    @property
    def message(self):
        r"""Gets the message of this ShowSqlJobStatusResponse.

        参数解释:  系统提示信息，执行成功时，信息可能为空 示例: success 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The message of this ShowSqlJobStatusResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ShowSqlJobStatusResponse.

        参数解释:  系统提示信息，执行成功时，信息可能为空 示例: success 约束限制:  无 取值范围: 无 默认取值: 无

        :param message: The message of this ShowSqlJobStatusResponse.
        :type message: str
        """
        self._message = message

    @property
    def job_mode(self):
        r"""Gets the job_mode of this ShowSqlJobStatusResponse.

        参数解释:  作业执行方式 示例: async 约束限制:  无 取值范围: async（同步） sync（异步） 默认取值: 无

        :return: The job_mode of this ShowSqlJobStatusResponse.
        :rtype: str
        """
        return self._job_mode

    @job_mode.setter
    def job_mode(self, job_mode):
        r"""Sets the job_mode of this ShowSqlJobStatusResponse.

        参数解释:  作业执行方式 示例: async 约束限制:  无 取值范围: async（同步） sync（异步） 默认取值: 无

        :param job_mode: The job_mode of this ShowSqlJobStatusResponse.
        :type job_mode: str
        """
        self._job_mode = job_mode

    @property
    def tags(self):
        r"""Gets the tags of this ShowSqlJobStatusResponse.

        作业标签

        :return: The tags of this ShowSqlJobStatusResponse.
        :rtype: list[:class:`huaweicloudsdkdli.v1.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ShowSqlJobStatusResponse.

        作业标签

        :param tags: The tags of this ShowSqlJobStatusResponse.
        :type tags: list[:class:`huaweicloudsdkdli.v1.Tag`]
        """
        self._tags = tags

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
        if not isinstance(other, ShowSqlJobStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
