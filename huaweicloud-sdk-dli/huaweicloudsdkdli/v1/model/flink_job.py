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
        """FlinkJob

        The model defined in huaweicloud sdk

        :param job_id: 作业ID。
        :type job_id: int
        :param name: 作业名称。长度限制：0-57个字符。
        :type name: str
        :param desc: 作业描述。长度限制：0-2048个字符。
        :type desc: str
        :param user_name: 用户名，当“show_detail”为“false”时独有。
        :type user_name: str
        :param job_type: 作业类型。
        :type job_type: str
        :param status: 作业状态。
        :type status: str
        :param status_desc: 作业状态描述。
        :type status_desc: str
        :param create_time: 作业创建时间。
        :type create_time: int
        :param start_time: 作业开始时间。
        :type start_time: int
        :param duration: 作业运行时长, 单位ms，当“show_detail”为“false”时独有。
        :type duration: int
        :param root_id: 父作业ID，“show_detail”为“false”时独有。
        :type root_id: int
        :param user_id: 作业所属用户标识，“show_detail”为“true”时独有。
        :type user_id: str
        :param project_id: 作业所属项目标识，“show_detail”为“true”时独有。
        :type project_id: str
        :param sql_body: Stream SQL语句，“show_detail”为“false”时独有。
        :type sql_body: str
        :param run_mode: 作业运行模式： shared_cluster：共享。 exclusive_cluster：独享。 edge_node：边缘节点。 show_detail为true时独有.
        :type run_mode: str
        :param main_class: jar包主类，“show_detail”为“false”时独有。
        :type main_class: str
        :param entrypoint_args: jar包作业运行参数，多个参数之间用空格分隔。show_detail为true时独有的。
        :type entrypoint_args: str
        :param execution_graph: 作业执行计划，“show_detail”为“false”时独有。
        :type execution_graph: str
        :param update_time: 作业更新时间，“show_detail”为“false”时独有。
        :type update_time: int
        :param graph_editor_enabled: 作业的流图是否可编辑。“true”表示作业的流图可以编辑，“false”表示作业的流图不可以编辑。
        :type graph_editor_enabled: bool
        :param has_savepoint: 作业是否有保存点。“true”表示作业有保存点，“false”表示作业没有保存点。
        :type has_savepoint: bool
        :param queue_name: 队列名字。
        :type queue_name: str
        :param edge_group_ids: 边缘计算组ID列表。
        :type edge_group_ids: list[str]
        :param restart_times: 重启次数。
        :type restart_times: int
        :param savepoint_path: 保存点路径。
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
        """Gets the job_id of this FlinkJob.

        作业ID。

        :return: The job_id of this FlinkJob.
        :rtype: int
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this FlinkJob.

        作业ID。

        :param job_id: The job_id of this FlinkJob.
        :type job_id: int
        """
        self._job_id = job_id

    @property
    def name(self):
        """Gets the name of this FlinkJob.

        作业名称。长度限制：0-57个字符。

        :return: The name of this FlinkJob.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FlinkJob.

        作业名称。长度限制：0-57个字符。

        :param name: The name of this FlinkJob.
        :type name: str
        """
        self._name = name

    @property
    def desc(self):
        """Gets the desc of this FlinkJob.

        作业描述。长度限制：0-2048个字符。

        :return: The desc of this FlinkJob.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this FlinkJob.

        作业描述。长度限制：0-2048个字符。

        :param desc: The desc of this FlinkJob.
        :type desc: str
        """
        self._desc = desc

    @property
    def user_name(self):
        """Gets the user_name of this FlinkJob.

        用户名，当“show_detail”为“false”时独有。

        :return: The user_name of this FlinkJob.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this FlinkJob.

        用户名，当“show_detail”为“false”时独有。

        :param user_name: The user_name of this FlinkJob.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def job_type(self):
        """Gets the job_type of this FlinkJob.

        作业类型。

        :return: The job_type of this FlinkJob.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this FlinkJob.

        作业类型。

        :param job_type: The job_type of this FlinkJob.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def status(self):
        """Gets the status of this FlinkJob.

        作业状态。

        :return: The status of this FlinkJob.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this FlinkJob.

        作业状态。

        :param status: The status of this FlinkJob.
        :type status: str
        """
        self._status = status

    @property
    def status_desc(self):
        """Gets the status_desc of this FlinkJob.

        作业状态描述。

        :return: The status_desc of this FlinkJob.
        :rtype: str
        """
        return self._status_desc

    @status_desc.setter
    def status_desc(self, status_desc):
        """Sets the status_desc of this FlinkJob.

        作业状态描述。

        :param status_desc: The status_desc of this FlinkJob.
        :type status_desc: str
        """
        self._status_desc = status_desc

    @property
    def create_time(self):
        """Gets the create_time of this FlinkJob.

        作业创建时间。

        :return: The create_time of this FlinkJob.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this FlinkJob.

        作业创建时间。

        :param create_time: The create_time of this FlinkJob.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def start_time(self):
        """Gets the start_time of this FlinkJob.

        作业开始时间。

        :return: The start_time of this FlinkJob.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this FlinkJob.

        作业开始时间。

        :param start_time: The start_time of this FlinkJob.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def duration(self):
        """Gets the duration of this FlinkJob.

        作业运行时长, 单位ms，当“show_detail”为“false”时独有。

        :return: The duration of this FlinkJob.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this FlinkJob.

        作业运行时长, 单位ms，当“show_detail”为“false”时独有。

        :param duration: The duration of this FlinkJob.
        :type duration: int
        """
        self._duration = duration

    @property
    def root_id(self):
        """Gets the root_id of this FlinkJob.

        父作业ID，“show_detail”为“false”时独有。

        :return: The root_id of this FlinkJob.
        :rtype: int
        """
        return self._root_id

    @root_id.setter
    def root_id(self, root_id):
        """Sets the root_id of this FlinkJob.

        父作业ID，“show_detail”为“false”时独有。

        :param root_id: The root_id of this FlinkJob.
        :type root_id: int
        """
        self._root_id = root_id

    @property
    def user_id(self):
        """Gets the user_id of this FlinkJob.

        作业所属用户标识，“show_detail”为“true”时独有。

        :return: The user_id of this FlinkJob.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this FlinkJob.

        作业所属用户标识，“show_detail”为“true”时独有。

        :param user_id: The user_id of this FlinkJob.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def project_id(self):
        """Gets the project_id of this FlinkJob.

        作业所属项目标识，“show_detail”为“true”时独有。

        :return: The project_id of this FlinkJob.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this FlinkJob.

        作业所属项目标识，“show_detail”为“true”时独有。

        :param project_id: The project_id of this FlinkJob.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def sql_body(self):
        """Gets the sql_body of this FlinkJob.

        Stream SQL语句，“show_detail”为“false”时独有。

        :return: The sql_body of this FlinkJob.
        :rtype: str
        """
        return self._sql_body

    @sql_body.setter
    def sql_body(self, sql_body):
        """Sets the sql_body of this FlinkJob.

        Stream SQL语句，“show_detail”为“false”时独有。

        :param sql_body: The sql_body of this FlinkJob.
        :type sql_body: str
        """
        self._sql_body = sql_body

    @property
    def run_mode(self):
        """Gets the run_mode of this FlinkJob.

        作业运行模式： shared_cluster：共享。 exclusive_cluster：独享。 edge_node：边缘节点。 show_detail为true时独有.

        :return: The run_mode of this FlinkJob.
        :rtype: str
        """
        return self._run_mode

    @run_mode.setter
    def run_mode(self, run_mode):
        """Sets the run_mode of this FlinkJob.

        作业运行模式： shared_cluster：共享。 exclusive_cluster：独享。 edge_node：边缘节点。 show_detail为true时独有.

        :param run_mode: The run_mode of this FlinkJob.
        :type run_mode: str
        """
        self._run_mode = run_mode

    @property
    def main_class(self):
        """Gets the main_class of this FlinkJob.

        jar包主类，“show_detail”为“false”时独有。

        :return: The main_class of this FlinkJob.
        :rtype: str
        """
        return self._main_class

    @main_class.setter
    def main_class(self, main_class):
        """Sets the main_class of this FlinkJob.

        jar包主类，“show_detail”为“false”时独有。

        :param main_class: The main_class of this FlinkJob.
        :type main_class: str
        """
        self._main_class = main_class

    @property
    def entrypoint_args(self):
        """Gets the entrypoint_args of this FlinkJob.

        jar包作业运行参数，多个参数之间用空格分隔。show_detail为true时独有的。

        :return: The entrypoint_args of this FlinkJob.
        :rtype: str
        """
        return self._entrypoint_args

    @entrypoint_args.setter
    def entrypoint_args(self, entrypoint_args):
        """Sets the entrypoint_args of this FlinkJob.

        jar包作业运行参数，多个参数之间用空格分隔。show_detail为true时独有的。

        :param entrypoint_args: The entrypoint_args of this FlinkJob.
        :type entrypoint_args: str
        """
        self._entrypoint_args = entrypoint_args

    @property
    def execution_graph(self):
        """Gets the execution_graph of this FlinkJob.

        作业执行计划，“show_detail”为“false”时独有。

        :return: The execution_graph of this FlinkJob.
        :rtype: str
        """
        return self._execution_graph

    @execution_graph.setter
    def execution_graph(self, execution_graph):
        """Sets the execution_graph of this FlinkJob.

        作业执行计划，“show_detail”为“false”时独有。

        :param execution_graph: The execution_graph of this FlinkJob.
        :type execution_graph: str
        """
        self._execution_graph = execution_graph

    @property
    def update_time(self):
        """Gets the update_time of this FlinkJob.

        作业更新时间，“show_detail”为“false”时独有。

        :return: The update_time of this FlinkJob.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this FlinkJob.

        作业更新时间，“show_detail”为“false”时独有。

        :param update_time: The update_time of this FlinkJob.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def graph_editor_enabled(self):
        """Gets the graph_editor_enabled of this FlinkJob.

        作业的流图是否可编辑。“true”表示作业的流图可以编辑，“false”表示作业的流图不可以编辑。

        :return: The graph_editor_enabled of this FlinkJob.
        :rtype: bool
        """
        return self._graph_editor_enabled

    @graph_editor_enabled.setter
    def graph_editor_enabled(self, graph_editor_enabled):
        """Sets the graph_editor_enabled of this FlinkJob.

        作业的流图是否可编辑。“true”表示作业的流图可以编辑，“false”表示作业的流图不可以编辑。

        :param graph_editor_enabled: The graph_editor_enabled of this FlinkJob.
        :type graph_editor_enabled: bool
        """
        self._graph_editor_enabled = graph_editor_enabled

    @property
    def has_savepoint(self):
        """Gets the has_savepoint of this FlinkJob.

        作业是否有保存点。“true”表示作业有保存点，“false”表示作业没有保存点。

        :return: The has_savepoint of this FlinkJob.
        :rtype: bool
        """
        return self._has_savepoint

    @has_savepoint.setter
    def has_savepoint(self, has_savepoint):
        """Sets the has_savepoint of this FlinkJob.

        作业是否有保存点。“true”表示作业有保存点，“false”表示作业没有保存点。

        :param has_savepoint: The has_savepoint of this FlinkJob.
        :type has_savepoint: bool
        """
        self._has_savepoint = has_savepoint

    @property
    def queue_name(self):
        """Gets the queue_name of this FlinkJob.

        队列名字。

        :return: The queue_name of this FlinkJob.
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        """Sets the queue_name of this FlinkJob.

        队列名字。

        :param queue_name: The queue_name of this FlinkJob.
        :type queue_name: str
        """
        self._queue_name = queue_name

    @property
    def edge_group_ids(self):
        """Gets the edge_group_ids of this FlinkJob.

        边缘计算组ID列表。

        :return: The edge_group_ids of this FlinkJob.
        :rtype: list[str]
        """
        return self._edge_group_ids

    @edge_group_ids.setter
    def edge_group_ids(self, edge_group_ids):
        """Sets the edge_group_ids of this FlinkJob.

        边缘计算组ID列表。

        :param edge_group_ids: The edge_group_ids of this FlinkJob.
        :type edge_group_ids: list[str]
        """
        self._edge_group_ids = edge_group_ids

    @property
    def restart_times(self):
        """Gets the restart_times of this FlinkJob.

        重启次数。

        :return: The restart_times of this FlinkJob.
        :rtype: int
        """
        return self._restart_times

    @restart_times.setter
    def restart_times(self, restart_times):
        """Sets the restart_times of this FlinkJob.

        重启次数。

        :param restart_times: The restart_times of this FlinkJob.
        :type restart_times: int
        """
        self._restart_times = restart_times

    @property
    def savepoint_path(self):
        """Gets the savepoint_path of this FlinkJob.

        保存点路径。

        :return: The savepoint_path of this FlinkJob.
        :rtype: str
        """
        return self._savepoint_path

    @savepoint_path.setter
    def savepoint_path(self, savepoint_path):
        """Sets the savepoint_path of this FlinkJob.

        保存点路径。

        :param savepoint_path: The savepoint_path of this FlinkJob.
        :type savepoint_path: str
        """
        self._savepoint_path = savepoint_path

    @property
    def job_config(self):
        """Gets the job_config of this FlinkJob.

        :return: The job_config of this FlinkJob.
        :rtype: :class:`huaweicloudsdkdli.v1.FlinkJobConfig`
        """
        return self._job_config

    @job_config.setter
    def job_config(self, job_config):
        """Sets the job_config of this FlinkJob.

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
