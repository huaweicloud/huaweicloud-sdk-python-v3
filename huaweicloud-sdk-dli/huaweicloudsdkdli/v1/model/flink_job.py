# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlinkJob:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'int',
        'name': 'str',
        'desc': 'str',
        'user_name': 'str',
        'job_type': 'str',
        'status': 'str',
        'status_desc': 'str',
        'create_time': 'int',
        'start_time': 'int',
        'duration': 'int',
        'root_id': 'int',
        'user_id': 'str',
        'project_id': 'str',
        'sql_body': 'str',
        'run_mode': 'str',
        'main_class': 'str',
        'entrypoint_args': 'str',
        'execution_graph': 'str',
        'update_time': 'int',
        'graph_editor_enabled': 'bool',
        'has_savepoint': 'bool',
        'queue_name': 'str',
        'edge_group_ids': 'list[str]',
        'restart_times': 'int',
        'savepoint_path': 'str',
        'job_config': 'FlinkJobConfig'
    }

    attribute_map = {
        'job_id': 'job_id',
        'name': 'name',
        'desc': 'desc',
        'user_name': 'user_name',
        'job_type': 'job_type',
        'status': 'status',
        'status_desc': 'status_desc',
        'create_time': 'create_time',
        'start_time': 'start_time',
        'duration': 'duration',
        'root_id': 'root_id',
        'user_id': 'user_id',
        'project_id': 'project_id',
        'sql_body': 'sql_body',
        'run_mode': 'run_mode',
        'main_class': 'main_class',
        'entrypoint_args': 'entrypoint_args',
        'execution_graph': 'execution_graph',
        'update_time': 'update_time',
        'graph_editor_enabled': 'graph_editor_enabled',
        'has_savepoint': 'has_savepoint',
        'queue_name': 'queue_name',
        'edge_group_ids': 'edge_group_ids',
        'restart_times': 'restart_times',
        'savepoint_path': 'savepoint_path',
        'job_config': 'job_config'
    }

    def __init__(self, job_id=None, name=None, desc=None, user_name=None, job_type=None, status=None, status_desc=None, create_time=None, start_time=None, duration=None, root_id=None, user_id=None, project_id=None, sql_body=None, run_mode=None, main_class=None, entrypoint_args=None, execution_graph=None, update_time=None, graph_editor_enabled=None, has_savepoint=None, queue_name=None, edge_group_ids=None, restart_times=None, savepoint_path=None, job_config=None):
        r"""FlinkJob

        The model defined in huaweicloud sdk

        :param job_id: 参数解释:  作业ID 示例: 50320 约束限制:  无 取值范围: 无 默认取值: 无
        :type job_id: int
        :param name: 参数解释:  作业名称 示例: test 约束限制:  长度在[0,57]范围内的字符串 取值范围: 无 默认取值: 无
        :type name: str
        :param desc: 参数解释:  作业描述 示例: 作业描述 约束限制:  长度在[0,2048]范围内的字符串 取值范围: 无 默认取值: 无
        :type desc: str
        :param user_name: 参数解释:  用户名称 示例: testuser 约束限制:  长度在[1,128]范围内的字符串 取值范围: 无 默认取值: 无
        :type user_name: str
        :param job_type: 参数解释:  作业类型 示例: flink_jar_job 约束限制:  无 取值范围: flink_sql_job（flink sql作业） flink_opensource_sql_job（flink opensource sql作业） flink_sql_edge_job（flink sql边缘作业） flink_jar_job（flink自定义作业） 默认取值: 无
        :type job_type: str
        :param status: 参数解释:  作业状态 示例: job_running 约束限制:  无 取值范围: job_init（草稿） job_submitting（提交中） job_submit_fail（提交失败） job_running（运行中） job_running_exception（运行异常） job_downloading（下载中） job_idle（空闲） job_canceling（停止中） job_cancel_success（已停止） job_cancel_fail（停止失败） job_savepointing（保存点创建中） job_arrearage_stopped（因欠费被停止） job_arrearage_recovering（欠费作业恢复中） job_finish（已完成） 默认取值: 无
        :type status: str
        :param status_desc: 参数解释:  用户名称 示例: 作业状态描述 约束限制:  无 取值范围: 无 默认取值: 无
        :type status_desc: str
        :param create_time: 参数解释:  作业创建时间 示例: 1516952770835 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无
        :type create_time: int
        :param start_time: 参数解释:  作业开始时间 示例: 1516952710740 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无
        :type start_time: int
        :param duration: 参数解释:  作业运行时长，单位ms，当“show_detail”为“false”时独有 示例: 30000 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无
        :type duration: int
        :param root_id: 参数解释:  父作业ID，“show_detail”为“false”时独有 示例: -1 约束限制:  无 取值范围: 无 默认取值: 无
        :type root_id: int
        :param user_id: 参数解释:  作业所属用户标识，“show_detail”为“true”时独有 示例: ac4eaa303639409c8ab099d55eb1538e 约束限制:  无 取值范围: 无 默认取值: 无
        :type user_id: str
        :param project_id: 参数解释:  作业所属用户标识，“show_detail”为“true”时独有 示例: 48cc2c48765f481480c7db940d6409d1 约束限制:  无 取值范围: 无 默认取值: 无
        :type project_id: str
        :param sql_body: 参数解释:  Stream SQL语句，“show_detail”为“false”时独有 示例: select * from source_table 约束限制:  无 取值范围: 无 默认取值: 无
        :type sql_body: str
        :param run_mode: 参数解释:  作业运行模式，show_detail为true时独有 示例: shared_cluster 约束限制:  无 取值范围: shared_cluster（共享） exclusive_cluster（独享） edge_node（边缘节点） 默认取值: 无
        :type run_mode: str
        :param main_class: 参数解释:  jar包主类，“show_detail”为“false”时独有 示例: org.apache.spark.examples.streaming.JavaQueueStream 约束限制:  无 取值范围: 无 默认取值: 无
        :type main_class: str
        :param entrypoint_args: 参数解释:  jar包作业运行参数，多个参数之间用空格分隔。show_detail为true时独有的 示例: custom.dir&#x3D;/usr custom.prefix&#x3D;dli 约束限制:  无 取值范围: 无 默认取值: 无
        :type entrypoint_args: str
        :param execution_graph: 参数解释:  作业执行计划，“show_detail”为“false”时独有 约束限制:  无 取值范围: 无 默认取值: 无
        :type execution_graph: str
        :param update_time: 参数解释:  作业更新时间，“show_detail”为“false”时独有 示例: 1516952770835 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无
        :type update_time: int
        :param graph_editor_enabled: 参数解释:  作业的流图是否可编辑。“true”表示作业的流图可以编辑，“false”表示作业的流图不可以编辑 示例: false 约束限制:  无 取值范围: true,false 默认取值: 无
        :type graph_editor_enabled: bool
        :param has_savepoint: 参数解释:  作业是否有保存点。“true”表示作业有保存点，“false”表示作业没有保存点 示例: false 约束限制:  无 取值范围: true,false 默认取值: 无
        :type has_savepoint: bool
        :param queue_name: 参数解释:  队列名称 示例: flink_17_queue 约束限制:  无 取值范围: 无 默认取值: 无
        :type queue_name: str
        :param edge_group_ids: 参数解释:  边缘计算组ID列表 示例: 62de1e1c-066e-48a8-a79d-f461a31b2ee1,2eb00f85-99f2-4144-bcb7-d39ff47f9002 约束限制:  无 取值范围: 无 默认取值: 无
        :type edge_group_ids: list[str]
        :param restart_times: 参数解释:  重启次数 示例: 0 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无
        :type restart_times: int
        :param savepoint_path: 参数解释:  保存点路径 示例: obs://cwk/savepoint/ 约束限制:  无 取值范围: 无 默认取值: 无
        :type savepoint_path: str
        :param job_config: 
        :type job_config: :class:`huaweicloudsdkdli.v1.FlinkJobConfig`
        """
        
        

        self._job_id = None
        self._name = None
        self._desc = None
        self._user_name = None
        self._job_type = None
        self._status = None
        self._status_desc = None
        self._create_time = None
        self._start_time = None
        self._duration = None
        self._root_id = None
        self._user_id = None
        self._project_id = None
        self._sql_body = None
        self._run_mode = None
        self._main_class = None
        self._entrypoint_args = None
        self._execution_graph = None
        self._update_time = None
        self._graph_editor_enabled = None
        self._has_savepoint = None
        self._queue_name = None
        self._edge_group_ids = None
        self._restart_times = None
        self._savepoint_path = None
        self._job_config = None
        self.discriminator = None

        self.job_id = job_id
        if name is not None:
            self.name = name
        if desc is not None:
            self.desc = desc
        if user_name is not None:
            self.user_name = user_name
        if job_type is not None:
            self.job_type = job_type
        if status is not None:
            self.status = status
        if status_desc is not None:
            self.status_desc = status_desc
        self.create_time = create_time
        if start_time is not None:
            self.start_time = start_time
        if duration is not None:
            self.duration = duration
        if root_id is not None:
            self.root_id = root_id
        if user_id is not None:
            self.user_id = user_id
        if project_id is not None:
            self.project_id = project_id
        if sql_body is not None:
            self.sql_body = sql_body
        if run_mode is not None:
            self.run_mode = run_mode
        if main_class is not None:
            self.main_class = main_class
        if entrypoint_args is not None:
            self.entrypoint_args = entrypoint_args
        if execution_graph is not None:
            self.execution_graph = execution_graph
        if update_time is not None:
            self.update_time = update_time
        if graph_editor_enabled is not None:
            self.graph_editor_enabled = graph_editor_enabled
        if has_savepoint is not None:
            self.has_savepoint = has_savepoint
        if queue_name is not None:
            self.queue_name = queue_name
        if edge_group_ids is not None:
            self.edge_group_ids = edge_group_ids
        if restart_times is not None:
            self.restart_times = restart_times
        if savepoint_path is not None:
            self.savepoint_path = savepoint_path
        if job_config is not None:
            self.job_config = job_config

    @property
    def job_id(self):
        r"""Gets the job_id of this FlinkJob.

        参数解释:  作业ID 示例: 50320 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The job_id of this FlinkJob.
        :rtype: int
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this FlinkJob.

        参数解释:  作业ID 示例: 50320 约束限制:  无 取值范围: 无 默认取值: 无

        :param job_id: The job_id of this FlinkJob.
        :type job_id: int
        """
        self._job_id = job_id

    @property
    def name(self):
        r"""Gets the name of this FlinkJob.

        参数解释:  作业名称 示例: test 约束限制:  长度在[0,57]范围内的字符串 取值范围: 无 默认取值: 无

        :return: The name of this FlinkJob.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this FlinkJob.

        参数解释:  作业名称 示例: test 约束限制:  长度在[0,57]范围内的字符串 取值范围: 无 默认取值: 无

        :param name: The name of this FlinkJob.
        :type name: str
        """
        self._name = name

    @property
    def desc(self):
        r"""Gets the desc of this FlinkJob.

        参数解释:  作业描述 示例: 作业描述 约束限制:  长度在[0,2048]范围内的字符串 取值范围: 无 默认取值: 无

        :return: The desc of this FlinkJob.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        r"""Sets the desc of this FlinkJob.

        参数解释:  作业描述 示例: 作业描述 约束限制:  长度在[0,2048]范围内的字符串 取值范围: 无 默认取值: 无

        :param desc: The desc of this FlinkJob.
        :type desc: str
        """
        self._desc = desc

    @property
    def user_name(self):
        r"""Gets the user_name of this FlinkJob.

        参数解释:  用户名称 示例: testuser 约束限制:  长度在[1,128]范围内的字符串 取值范围: 无 默认取值: 无

        :return: The user_name of this FlinkJob.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this FlinkJob.

        参数解释:  用户名称 示例: testuser 约束限制:  长度在[1,128]范围内的字符串 取值范围: 无 默认取值: 无

        :param user_name: The user_name of this FlinkJob.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def job_type(self):
        r"""Gets the job_type of this FlinkJob.

        参数解释:  作业类型 示例: flink_jar_job 约束限制:  无 取值范围: flink_sql_job（flink sql作业） flink_opensource_sql_job（flink opensource sql作业） flink_sql_edge_job（flink sql边缘作业） flink_jar_job（flink自定义作业） 默认取值: 无

        :return: The job_type of this FlinkJob.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this FlinkJob.

        参数解释:  作业类型 示例: flink_jar_job 约束限制:  无 取值范围: flink_sql_job（flink sql作业） flink_opensource_sql_job（flink opensource sql作业） flink_sql_edge_job（flink sql边缘作业） flink_jar_job（flink自定义作业） 默认取值: 无

        :param job_type: The job_type of this FlinkJob.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def status(self):
        r"""Gets the status of this FlinkJob.

        参数解释:  作业状态 示例: job_running 约束限制:  无 取值范围: job_init（草稿） job_submitting（提交中） job_submit_fail（提交失败） job_running（运行中） job_running_exception（运行异常） job_downloading（下载中） job_idle（空闲） job_canceling（停止中） job_cancel_success（已停止） job_cancel_fail（停止失败） job_savepointing（保存点创建中） job_arrearage_stopped（因欠费被停止） job_arrearage_recovering（欠费作业恢复中） job_finish（已完成） 默认取值: 无

        :return: The status of this FlinkJob.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this FlinkJob.

        参数解释:  作业状态 示例: job_running 约束限制:  无 取值范围: job_init（草稿） job_submitting（提交中） job_submit_fail（提交失败） job_running（运行中） job_running_exception（运行异常） job_downloading（下载中） job_idle（空闲） job_canceling（停止中） job_cancel_success（已停止） job_cancel_fail（停止失败） job_savepointing（保存点创建中） job_arrearage_stopped（因欠费被停止） job_arrearage_recovering（欠费作业恢复中） job_finish（已完成） 默认取值: 无

        :param status: The status of this FlinkJob.
        :type status: str
        """
        self._status = status

    @property
    def status_desc(self):
        r"""Gets the status_desc of this FlinkJob.

        参数解释:  用户名称 示例: 作业状态描述 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The status_desc of this FlinkJob.
        :rtype: str
        """
        return self._status_desc

    @status_desc.setter
    def status_desc(self, status_desc):
        r"""Sets the status_desc of this FlinkJob.

        参数解释:  用户名称 示例: 作业状态描述 约束限制:  无 取值范围: 无 默认取值: 无

        :param status_desc: The status_desc of this FlinkJob.
        :type status_desc: str
        """
        self._status_desc = status_desc

    @property
    def create_time(self):
        r"""Gets the create_time of this FlinkJob.

        参数解释:  作业创建时间 示例: 1516952770835 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :return: The create_time of this FlinkJob.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this FlinkJob.

        参数解释:  作业创建时间 示例: 1516952770835 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :param create_time: The create_time of this FlinkJob.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def start_time(self):
        r"""Gets the start_time of this FlinkJob.

        参数解释:  作业开始时间 示例: 1516952710740 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :return: The start_time of this FlinkJob.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this FlinkJob.

        参数解释:  作业开始时间 示例: 1516952710740 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :param start_time: The start_time of this FlinkJob.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def duration(self):
        r"""Gets the duration of this FlinkJob.

        参数解释:  作业运行时长，单位ms，当“show_detail”为“false”时独有 示例: 30000 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :return: The duration of this FlinkJob.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this FlinkJob.

        参数解释:  作业运行时长，单位ms，当“show_detail”为“false”时独有 示例: 30000 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :param duration: The duration of this FlinkJob.
        :type duration: int
        """
        self._duration = duration

    @property
    def root_id(self):
        r"""Gets the root_id of this FlinkJob.

        参数解释:  父作业ID，“show_detail”为“false”时独有 示例: -1 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The root_id of this FlinkJob.
        :rtype: int
        """
        return self._root_id

    @root_id.setter
    def root_id(self, root_id):
        r"""Sets the root_id of this FlinkJob.

        参数解释:  父作业ID，“show_detail”为“false”时独有 示例: -1 约束限制:  无 取值范围: 无 默认取值: 无

        :param root_id: The root_id of this FlinkJob.
        :type root_id: int
        """
        self._root_id = root_id

    @property
    def user_id(self):
        r"""Gets the user_id of this FlinkJob.

        参数解释:  作业所属用户标识，“show_detail”为“true”时独有 示例: ac4eaa303639409c8ab099d55eb1538e 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The user_id of this FlinkJob.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this FlinkJob.

        参数解释:  作业所属用户标识，“show_detail”为“true”时独有 示例: ac4eaa303639409c8ab099d55eb1538e 约束限制:  无 取值范围: 无 默认取值: 无

        :param user_id: The user_id of this FlinkJob.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def project_id(self):
        r"""Gets the project_id of this FlinkJob.

        参数解释:  作业所属用户标识，“show_detail”为“true”时独有 示例: 48cc2c48765f481480c7db940d6409d1 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The project_id of this FlinkJob.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this FlinkJob.

        参数解释:  作业所属用户标识，“show_detail”为“true”时独有 示例: 48cc2c48765f481480c7db940d6409d1 约束限制:  无 取值范围: 无 默认取值: 无

        :param project_id: The project_id of this FlinkJob.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def sql_body(self):
        r"""Gets the sql_body of this FlinkJob.

        参数解释:  Stream SQL语句，“show_detail”为“false”时独有 示例: select * from source_table 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The sql_body of this FlinkJob.
        :rtype: str
        """
        return self._sql_body

    @sql_body.setter
    def sql_body(self, sql_body):
        r"""Sets the sql_body of this FlinkJob.

        参数解释:  Stream SQL语句，“show_detail”为“false”时独有 示例: select * from source_table 约束限制:  无 取值范围: 无 默认取值: 无

        :param sql_body: The sql_body of this FlinkJob.
        :type sql_body: str
        """
        self._sql_body = sql_body

    @property
    def run_mode(self):
        r"""Gets the run_mode of this FlinkJob.

        参数解释:  作业运行模式，show_detail为true时独有 示例: shared_cluster 约束限制:  无 取值范围: shared_cluster（共享） exclusive_cluster（独享） edge_node（边缘节点） 默认取值: 无

        :return: The run_mode of this FlinkJob.
        :rtype: str
        """
        return self._run_mode

    @run_mode.setter
    def run_mode(self, run_mode):
        r"""Sets the run_mode of this FlinkJob.

        参数解释:  作业运行模式，show_detail为true时独有 示例: shared_cluster 约束限制:  无 取值范围: shared_cluster（共享） exclusive_cluster（独享） edge_node（边缘节点） 默认取值: 无

        :param run_mode: The run_mode of this FlinkJob.
        :type run_mode: str
        """
        self._run_mode = run_mode

    @property
    def main_class(self):
        r"""Gets the main_class of this FlinkJob.

        参数解释:  jar包主类，“show_detail”为“false”时独有 示例: org.apache.spark.examples.streaming.JavaQueueStream 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The main_class of this FlinkJob.
        :rtype: str
        """
        return self._main_class

    @main_class.setter
    def main_class(self, main_class):
        r"""Sets the main_class of this FlinkJob.

        参数解释:  jar包主类，“show_detail”为“false”时独有 示例: org.apache.spark.examples.streaming.JavaQueueStream 约束限制:  无 取值范围: 无 默认取值: 无

        :param main_class: The main_class of this FlinkJob.
        :type main_class: str
        """
        self._main_class = main_class

    @property
    def entrypoint_args(self):
        r"""Gets the entrypoint_args of this FlinkJob.

        参数解释:  jar包作业运行参数，多个参数之间用空格分隔。show_detail为true时独有的 示例: custom.dir=/usr custom.prefix=dli 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The entrypoint_args of this FlinkJob.
        :rtype: str
        """
        return self._entrypoint_args

    @entrypoint_args.setter
    def entrypoint_args(self, entrypoint_args):
        r"""Sets the entrypoint_args of this FlinkJob.

        参数解释:  jar包作业运行参数，多个参数之间用空格分隔。show_detail为true时独有的 示例: custom.dir=/usr custom.prefix=dli 约束限制:  无 取值范围: 无 默认取值: 无

        :param entrypoint_args: The entrypoint_args of this FlinkJob.
        :type entrypoint_args: str
        """
        self._entrypoint_args = entrypoint_args

    @property
    def execution_graph(self):
        r"""Gets the execution_graph of this FlinkJob.

        参数解释:  作业执行计划，“show_detail”为“false”时独有 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The execution_graph of this FlinkJob.
        :rtype: str
        """
        return self._execution_graph

    @execution_graph.setter
    def execution_graph(self, execution_graph):
        r"""Sets the execution_graph of this FlinkJob.

        参数解释:  作业执行计划，“show_detail”为“false”时独有 约束限制:  无 取值范围: 无 默认取值: 无

        :param execution_graph: The execution_graph of this FlinkJob.
        :type execution_graph: str
        """
        self._execution_graph = execution_graph

    @property
    def update_time(self):
        r"""Gets the update_time of this FlinkJob.

        参数解释:  作业更新时间，“show_detail”为“false”时独有 示例: 1516952770835 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :return: The update_time of this FlinkJob.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this FlinkJob.

        参数解释:  作业更新时间，“show_detail”为“false”时独有 示例: 1516952770835 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :param update_time: The update_time of this FlinkJob.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def graph_editor_enabled(self):
        r"""Gets the graph_editor_enabled of this FlinkJob.

        参数解释:  作业的流图是否可编辑。“true”表示作业的流图可以编辑，“false”表示作业的流图不可以编辑 示例: false 约束限制:  无 取值范围: true,false 默认取值: 无

        :return: The graph_editor_enabled of this FlinkJob.
        :rtype: bool
        """
        return self._graph_editor_enabled

    @graph_editor_enabled.setter
    def graph_editor_enabled(self, graph_editor_enabled):
        r"""Sets the graph_editor_enabled of this FlinkJob.

        参数解释:  作业的流图是否可编辑。“true”表示作业的流图可以编辑，“false”表示作业的流图不可以编辑 示例: false 约束限制:  无 取值范围: true,false 默认取值: 无

        :param graph_editor_enabled: The graph_editor_enabled of this FlinkJob.
        :type graph_editor_enabled: bool
        """
        self._graph_editor_enabled = graph_editor_enabled

    @property
    def has_savepoint(self):
        r"""Gets the has_savepoint of this FlinkJob.

        参数解释:  作业是否有保存点。“true”表示作业有保存点，“false”表示作业没有保存点 示例: false 约束限制:  无 取值范围: true,false 默认取值: 无

        :return: The has_savepoint of this FlinkJob.
        :rtype: bool
        """
        return self._has_savepoint

    @has_savepoint.setter
    def has_savepoint(self, has_savepoint):
        r"""Sets the has_savepoint of this FlinkJob.

        参数解释:  作业是否有保存点。“true”表示作业有保存点，“false”表示作业没有保存点 示例: false 约束限制:  无 取值范围: true,false 默认取值: 无

        :param has_savepoint: The has_savepoint of this FlinkJob.
        :type has_savepoint: bool
        """
        self._has_savepoint = has_savepoint

    @property
    def queue_name(self):
        r"""Gets the queue_name of this FlinkJob.

        参数解释:  队列名称 示例: flink_17_queue 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The queue_name of this FlinkJob.
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        r"""Sets the queue_name of this FlinkJob.

        参数解释:  队列名称 示例: flink_17_queue 约束限制:  无 取值范围: 无 默认取值: 无

        :param queue_name: The queue_name of this FlinkJob.
        :type queue_name: str
        """
        self._queue_name = queue_name

    @property
    def edge_group_ids(self):
        r"""Gets the edge_group_ids of this FlinkJob.

        参数解释:  边缘计算组ID列表 示例: 62de1e1c-066e-48a8-a79d-f461a31b2ee1,2eb00f85-99f2-4144-bcb7-d39ff47f9002 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The edge_group_ids of this FlinkJob.
        :rtype: list[str]
        """
        return self._edge_group_ids

    @edge_group_ids.setter
    def edge_group_ids(self, edge_group_ids):
        r"""Sets the edge_group_ids of this FlinkJob.

        参数解释:  边缘计算组ID列表 示例: 62de1e1c-066e-48a8-a79d-f461a31b2ee1,2eb00f85-99f2-4144-bcb7-d39ff47f9002 约束限制:  无 取值范围: 无 默认取值: 无

        :param edge_group_ids: The edge_group_ids of this FlinkJob.
        :type edge_group_ids: list[str]
        """
        self._edge_group_ids = edge_group_ids

    @property
    def restart_times(self):
        r"""Gets the restart_times of this FlinkJob.

        参数解释:  重启次数 示例: 0 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :return: The restart_times of this FlinkJob.
        :rtype: int
        """
        return self._restart_times

    @restart_times.setter
    def restart_times(self, restart_times):
        r"""Sets the restart_times of this FlinkJob.

        参数解释:  重启次数 示例: 0 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :param restart_times: The restart_times of this FlinkJob.
        :type restart_times: int
        """
        self._restart_times = restart_times

    @property
    def savepoint_path(self):
        r"""Gets the savepoint_path of this FlinkJob.

        参数解释:  保存点路径 示例: obs://cwk/savepoint/ 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The savepoint_path of this FlinkJob.
        :rtype: str
        """
        return self._savepoint_path

    @savepoint_path.setter
    def savepoint_path(self, savepoint_path):
        r"""Sets the savepoint_path of this FlinkJob.

        参数解释:  保存点路径 示例: obs://cwk/savepoint/ 约束限制:  无 取值范围: 无 默认取值: 无

        :param savepoint_path: The savepoint_path of this FlinkJob.
        :type savepoint_path: str
        """
        self._savepoint_path = savepoint_path

    @property
    def job_config(self):
        r"""Gets the job_config of this FlinkJob.

        :return: The job_config of this FlinkJob.
        :rtype: :class:`huaweicloudsdkdli.v1.FlinkJobConfig`
        """
        return self._job_config

    @job_config.setter
    def job_config(self, job_config):
        r"""Sets the job_config of this FlinkJob.

        :param job_config: The job_config of this FlinkJob.
        :type job_config: :class:`huaweicloudsdkdli.v1.FlinkJobConfig`
        """
        self._job_config = job_config

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
        if not isinstance(other, FlinkJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
