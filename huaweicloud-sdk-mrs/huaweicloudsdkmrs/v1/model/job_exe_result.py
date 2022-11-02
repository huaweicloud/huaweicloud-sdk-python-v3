# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobExeResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'create_at': 'int',
        'update_at': 'int',
        'tenant_id': 'str',
        'job_id': 'str',
        'job_name': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'cluster_id': 'str',
        'group_id': 'str',
        'jar_path': 'str',
        'input': 'str',
        'output': 'str',
        'job_log': 'str',
        'job_type': 'int',
        'file_action': 'str',
        'arguments': 'str',
        'hql': 'str',
        'job_state': 'int',
        'job_final_status': 'int',
        'hive_script_path': 'str',
        'create_by': 'str',
        'finished_step': 'int',
        'job_main_id': 'str',
        'job_step_id': 'str',
        'postpone_at': 'int',
        'step_name': 'str',
        'step_num': 'int',
        'task_num': 'int',
        'update_by': 'str',
        'spend_time': 'float',
        'step_seq': 'int',
        'progress': 'str'
    }

    attribute_map = {
        'id': 'id',
        'create_at': 'create_at',
        'update_at': 'update_at',
        'tenant_id': 'tenant_id',
        'job_id': 'job_id',
        'job_name': 'job_name',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'cluster_id': 'cluster_id',
        'group_id': 'group_id',
        'jar_path': 'jar_path',
        'input': 'input',
        'output': 'output',
        'job_log': 'job_log',
        'job_type': 'job_type',
        'file_action': 'file_action',
        'arguments': 'arguments',
        'hql': 'hql',
        'job_state': 'job_state',
        'job_final_status': 'job_final_status',
        'hive_script_path': 'hive_script_path',
        'create_by': 'create_by',
        'finished_step': 'finished_step',
        'job_main_id': 'job_main_id',
        'job_step_id': 'job_step_id',
        'postpone_at': 'postpone_at',
        'step_name': 'step_name',
        'step_num': 'step_num',
        'task_num': 'task_num',
        'update_by': 'update_by',
        'spend_time': 'spend_time',
        'step_seq': 'step_seq',
        'progress': 'progress'
    }

    def __init__(self, id=None, create_at=None, update_at=None, tenant_id=None, job_id=None, job_name=None, start_time=None, end_time=None, cluster_id=None, group_id=None, jar_path=None, input=None, output=None, job_log=None, job_type=None, file_action=None, arguments=None, hql=None, job_state=None, job_final_status=None, hive_script_path=None, create_by=None, finished_step=None, job_main_id=None, job_step_id=None, postpone_at=None, step_name=None, step_num=None, task_num=None, update_by=None, spend_time=None, step_seq=None, progress=None):
        """JobExeResult

        The model defined in huaweicloud sdk

        :param id: 作业ID。
        :type id: str
        :param create_at: 作业创建时间，十三位时间戳。
        :type create_at: int
        :param update_at: 作业更新时间，十三位时间戳。  
        :type update_at: int
        :param tenant_id: 项目编号。获取方法，请参见[获取项目ID](https://support.huaweicloud.com/api-mrs/mrs_02_0011.html)。
        :type tenant_id: str
        :param job_id: 作业ID。
        :type job_id: str
        :param job_name: 作业名称。
        :type job_name: str
        :param start_time: 作业执行开始时间，十三位时间戳。
        :type start_time: int
        :param end_time: 作业执行结束时间，十三位时间戳。
        :type end_time: int
        :param cluster_id: 作业所属集群ID。
        :type cluster_id: str
        :param group_id: 作业执行组ID
        :type group_id: str
        :param jar_path: 执行程序jar包或sql文件地址。
        :type jar_path: str
        :param input: 数据输入地址。
        :type input: str
        :param output: 数据输出地址。
        :type output: str
        :param job_log: 作业日志存储地址
        :type job_log: str
        :param job_type: 作业类型码。  - 1：MapReduce - 2：Spark - 3：Hive Script - 4：HiveSQL（当前不支持） - 5：DistCp - 6：Spark Script - 7：Spark SQL（该接口当前不支持）
        :type job_type: int
        :param file_action: 导入导出数据。
        :type file_action: str
        :param arguments: 程序执行的关键参数，该参数由用户程序内的函数指定，MRS只负责参数的传入。该参数可为空。
        :type arguments: str
        :param hql: HQL脚本语句。
        :type hql: str
        :param job_state: 作业状态编码：  - 1：Terminated表示已终止的作业状态 - 2：Running表示运行中的作业状态 - 3：Completed表示已完成的作业状态 - 4：Abnormal表示异常的作业状态
        :type job_state: int
        :param job_final_status: 作业最终状态码。  - 0：未完成 - 1：执行错误，终止执行 - 2：执行完成并且成功 - 3：已取消
        :type job_final_status: int
        :param hive_script_path: Hive脚本地址。
        :type hive_script_path: str
        :param create_by: 创建作业的用户ID。
        :type create_by: str
        :param finished_step: 当前已完成的步骤数。
        :type finished_step: int
        :param job_main_id: 作业主ID。
        :type job_main_id: str
        :param job_step_id: 作业步骤ID。
        :type job_step_id: str
        :param postpone_at: 延迟时间，十三位时间戳。
        :type postpone_at: int
        :param step_name: 作业步骤名。
        :type step_name: str
        :param step_num: 步骤数量。
        :type step_num: int
        :param task_num: 任务数量。
        :type task_num: int
        :param update_by: 更新作业的用户ID。
        :type update_by: str
        :param spend_time: 作业执行持续时间，单位：秒。
        :type spend_time: float
        :param step_seq: 步骤序列号。
        :type step_seq: int
        :param progress: 作业执行进度。
        :type progress: str
        """
        
        

        self._id = None
        self._create_at = None
        self._update_at = None
        self._tenant_id = None
        self._job_id = None
        self._job_name = None
        self._start_time = None
        self._end_time = None
        self._cluster_id = None
        self._group_id = None
        self._jar_path = None
        self._input = None
        self._output = None
        self._job_log = None
        self._job_type = None
        self._file_action = None
        self._arguments = None
        self._hql = None
        self._job_state = None
        self._job_final_status = None
        self._hive_script_path = None
        self._create_by = None
        self._finished_step = None
        self._job_main_id = None
        self._job_step_id = None
        self._postpone_at = None
        self._step_name = None
        self._step_num = None
        self._task_num = None
        self._update_by = None
        self._spend_time = None
        self._step_seq = None
        self._progress = None
        self.discriminator = None

        self.id = id
        self.create_at = create_at
        self.update_at = update_at
        self.tenant_id = tenant_id
        self.job_id = job_id
        self.job_name = job_name
        self.start_time = start_time
        self.end_time = end_time
        self.cluster_id = cluster_id
        self.group_id = group_id
        self.jar_path = jar_path
        self.input = input
        if output is not None:
            self.output = output
        self.job_log = job_log
        self.job_type = job_type
        self.file_action = file_action
        self.arguments = arguments
        self.hql = hql
        self.job_state = job_state
        self.job_final_status = job_final_status
        self.hive_script_path = hive_script_path
        self.create_by = create_by
        self.finished_step = finished_step
        self.job_main_id = job_main_id
        self.job_step_id = job_step_id
        self.postpone_at = postpone_at
        self.step_name = step_name
        self.step_num = step_num
        self.task_num = task_num
        self.update_by = update_by
        self.spend_time = spend_time
        self.step_seq = step_seq
        self.progress = progress

    @property
    def id(self):
        """Gets the id of this JobExeResult.

        作业ID。

        :return: The id of this JobExeResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this JobExeResult.

        作业ID。

        :param id: The id of this JobExeResult.
        :type id: str
        """
        self._id = id

    @property
    def create_at(self):
        """Gets the create_at of this JobExeResult.

        作业创建时间，十三位时间戳。

        :return: The create_at of this JobExeResult.
        :rtype: int
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        """Sets the create_at of this JobExeResult.

        作业创建时间，十三位时间戳。

        :param create_at: The create_at of this JobExeResult.
        :type create_at: int
        """
        self._create_at = create_at

    @property
    def update_at(self):
        """Gets the update_at of this JobExeResult.

        作业更新时间，十三位时间戳。  

        :return: The update_at of this JobExeResult.
        :rtype: int
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        """Sets the update_at of this JobExeResult.

        作业更新时间，十三位时间戳。  

        :param update_at: The update_at of this JobExeResult.
        :type update_at: int
        """
        self._update_at = update_at

    @property
    def tenant_id(self):
        """Gets the tenant_id of this JobExeResult.

        项目编号。获取方法，请参见[获取项目ID](https://support.huaweicloud.com/api-mrs/mrs_02_0011.html)。

        :return: The tenant_id of this JobExeResult.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this JobExeResult.

        项目编号。获取方法，请参见[获取项目ID](https://support.huaweicloud.com/api-mrs/mrs_02_0011.html)。

        :param tenant_id: The tenant_id of this JobExeResult.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def job_id(self):
        """Gets the job_id of this JobExeResult.

        作业ID。

        :return: The job_id of this JobExeResult.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this JobExeResult.

        作业ID。

        :param job_id: The job_id of this JobExeResult.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_name(self):
        """Gets the job_name of this JobExeResult.

        作业名称。

        :return: The job_name of this JobExeResult.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this JobExeResult.

        作业名称。

        :param job_name: The job_name of this JobExeResult.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def start_time(self):
        """Gets the start_time of this JobExeResult.

        作业执行开始时间，十三位时间戳。

        :return: The start_time of this JobExeResult.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this JobExeResult.

        作业执行开始时间，十三位时间戳。

        :param start_time: The start_time of this JobExeResult.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this JobExeResult.

        作业执行结束时间，十三位时间戳。

        :return: The end_time of this JobExeResult.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this JobExeResult.

        作业执行结束时间，十三位时间戳。

        :param end_time: The end_time of this JobExeResult.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def cluster_id(self):
        """Gets the cluster_id of this JobExeResult.

        作业所属集群ID。

        :return: The cluster_id of this JobExeResult.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this JobExeResult.

        作业所属集群ID。

        :param cluster_id: The cluster_id of this JobExeResult.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def group_id(self):
        """Gets the group_id of this JobExeResult.

        作业执行组ID

        :return: The group_id of this JobExeResult.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this JobExeResult.

        作业执行组ID

        :param group_id: The group_id of this JobExeResult.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def jar_path(self):
        """Gets the jar_path of this JobExeResult.

        执行程序jar包或sql文件地址。

        :return: The jar_path of this JobExeResult.
        :rtype: str
        """
        return self._jar_path

    @jar_path.setter
    def jar_path(self, jar_path):
        """Sets the jar_path of this JobExeResult.

        执行程序jar包或sql文件地址。

        :param jar_path: The jar_path of this JobExeResult.
        :type jar_path: str
        """
        self._jar_path = jar_path

    @property
    def input(self):
        """Gets the input of this JobExeResult.

        数据输入地址。

        :return: The input of this JobExeResult.
        :rtype: str
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this JobExeResult.

        数据输入地址。

        :param input: The input of this JobExeResult.
        :type input: str
        """
        self._input = input

    @property
    def output(self):
        """Gets the output of this JobExeResult.

        数据输出地址。

        :return: The output of this JobExeResult.
        :rtype: str
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this JobExeResult.

        数据输出地址。

        :param output: The output of this JobExeResult.
        :type output: str
        """
        self._output = output

    @property
    def job_log(self):
        """Gets the job_log of this JobExeResult.

        作业日志存储地址

        :return: The job_log of this JobExeResult.
        :rtype: str
        """
        return self._job_log

    @job_log.setter
    def job_log(self, job_log):
        """Sets the job_log of this JobExeResult.

        作业日志存储地址

        :param job_log: The job_log of this JobExeResult.
        :type job_log: str
        """
        self._job_log = job_log

    @property
    def job_type(self):
        """Gets the job_type of this JobExeResult.

        作业类型码。  - 1：MapReduce - 2：Spark - 3：Hive Script - 4：HiveSQL（当前不支持） - 5：DistCp - 6：Spark Script - 7：Spark SQL（该接口当前不支持）

        :return: The job_type of this JobExeResult.
        :rtype: int
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this JobExeResult.

        作业类型码。  - 1：MapReduce - 2：Spark - 3：Hive Script - 4：HiveSQL（当前不支持） - 5：DistCp - 6：Spark Script - 7：Spark SQL（该接口当前不支持）

        :param job_type: The job_type of this JobExeResult.
        :type job_type: int
        """
        self._job_type = job_type

    @property
    def file_action(self):
        """Gets the file_action of this JobExeResult.

        导入导出数据。

        :return: The file_action of this JobExeResult.
        :rtype: str
        """
        return self._file_action

    @file_action.setter
    def file_action(self, file_action):
        """Sets the file_action of this JobExeResult.

        导入导出数据。

        :param file_action: The file_action of this JobExeResult.
        :type file_action: str
        """
        self._file_action = file_action

    @property
    def arguments(self):
        """Gets the arguments of this JobExeResult.

        程序执行的关键参数，该参数由用户程序内的函数指定，MRS只负责参数的传入。该参数可为空。

        :return: The arguments of this JobExeResult.
        :rtype: str
        """
        return self._arguments

    @arguments.setter
    def arguments(self, arguments):
        """Sets the arguments of this JobExeResult.

        程序执行的关键参数，该参数由用户程序内的函数指定，MRS只负责参数的传入。该参数可为空。

        :param arguments: The arguments of this JobExeResult.
        :type arguments: str
        """
        self._arguments = arguments

    @property
    def hql(self):
        """Gets the hql of this JobExeResult.

        HQL脚本语句。

        :return: The hql of this JobExeResult.
        :rtype: str
        """
        return self._hql

    @hql.setter
    def hql(self, hql):
        """Sets the hql of this JobExeResult.

        HQL脚本语句。

        :param hql: The hql of this JobExeResult.
        :type hql: str
        """
        self._hql = hql

    @property
    def job_state(self):
        """Gets the job_state of this JobExeResult.

        作业状态编码：  - 1：Terminated表示已终止的作业状态 - 2：Running表示运行中的作业状态 - 3：Completed表示已完成的作业状态 - 4：Abnormal表示异常的作业状态

        :return: The job_state of this JobExeResult.
        :rtype: int
        """
        return self._job_state

    @job_state.setter
    def job_state(self, job_state):
        """Sets the job_state of this JobExeResult.

        作业状态编码：  - 1：Terminated表示已终止的作业状态 - 2：Running表示运行中的作业状态 - 3：Completed表示已完成的作业状态 - 4：Abnormal表示异常的作业状态

        :param job_state: The job_state of this JobExeResult.
        :type job_state: int
        """
        self._job_state = job_state

    @property
    def job_final_status(self):
        """Gets the job_final_status of this JobExeResult.

        作业最终状态码。  - 0：未完成 - 1：执行错误，终止执行 - 2：执行完成并且成功 - 3：已取消

        :return: The job_final_status of this JobExeResult.
        :rtype: int
        """
        return self._job_final_status

    @job_final_status.setter
    def job_final_status(self, job_final_status):
        """Sets the job_final_status of this JobExeResult.

        作业最终状态码。  - 0：未完成 - 1：执行错误，终止执行 - 2：执行完成并且成功 - 3：已取消

        :param job_final_status: The job_final_status of this JobExeResult.
        :type job_final_status: int
        """
        self._job_final_status = job_final_status

    @property
    def hive_script_path(self):
        """Gets the hive_script_path of this JobExeResult.

        Hive脚本地址。

        :return: The hive_script_path of this JobExeResult.
        :rtype: str
        """
        return self._hive_script_path

    @hive_script_path.setter
    def hive_script_path(self, hive_script_path):
        """Sets the hive_script_path of this JobExeResult.

        Hive脚本地址。

        :param hive_script_path: The hive_script_path of this JobExeResult.
        :type hive_script_path: str
        """
        self._hive_script_path = hive_script_path

    @property
    def create_by(self):
        """Gets the create_by of this JobExeResult.

        创建作业的用户ID。

        :return: The create_by of this JobExeResult.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        """Sets the create_by of this JobExeResult.

        创建作业的用户ID。

        :param create_by: The create_by of this JobExeResult.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def finished_step(self):
        """Gets the finished_step of this JobExeResult.

        当前已完成的步骤数。

        :return: The finished_step of this JobExeResult.
        :rtype: int
        """
        return self._finished_step

    @finished_step.setter
    def finished_step(self, finished_step):
        """Sets the finished_step of this JobExeResult.

        当前已完成的步骤数。

        :param finished_step: The finished_step of this JobExeResult.
        :type finished_step: int
        """
        self._finished_step = finished_step

    @property
    def job_main_id(self):
        """Gets the job_main_id of this JobExeResult.

        作业主ID。

        :return: The job_main_id of this JobExeResult.
        :rtype: str
        """
        return self._job_main_id

    @job_main_id.setter
    def job_main_id(self, job_main_id):
        """Sets the job_main_id of this JobExeResult.

        作业主ID。

        :param job_main_id: The job_main_id of this JobExeResult.
        :type job_main_id: str
        """
        self._job_main_id = job_main_id

    @property
    def job_step_id(self):
        """Gets the job_step_id of this JobExeResult.

        作业步骤ID。

        :return: The job_step_id of this JobExeResult.
        :rtype: str
        """
        return self._job_step_id

    @job_step_id.setter
    def job_step_id(self, job_step_id):
        """Sets the job_step_id of this JobExeResult.

        作业步骤ID。

        :param job_step_id: The job_step_id of this JobExeResult.
        :type job_step_id: str
        """
        self._job_step_id = job_step_id

    @property
    def postpone_at(self):
        """Gets the postpone_at of this JobExeResult.

        延迟时间，十三位时间戳。

        :return: The postpone_at of this JobExeResult.
        :rtype: int
        """
        return self._postpone_at

    @postpone_at.setter
    def postpone_at(self, postpone_at):
        """Sets the postpone_at of this JobExeResult.

        延迟时间，十三位时间戳。

        :param postpone_at: The postpone_at of this JobExeResult.
        :type postpone_at: int
        """
        self._postpone_at = postpone_at

    @property
    def step_name(self):
        """Gets the step_name of this JobExeResult.

        作业步骤名。

        :return: The step_name of this JobExeResult.
        :rtype: str
        """
        return self._step_name

    @step_name.setter
    def step_name(self, step_name):
        """Sets the step_name of this JobExeResult.

        作业步骤名。

        :param step_name: The step_name of this JobExeResult.
        :type step_name: str
        """
        self._step_name = step_name

    @property
    def step_num(self):
        """Gets the step_num of this JobExeResult.

        步骤数量。

        :return: The step_num of this JobExeResult.
        :rtype: int
        """
        return self._step_num

    @step_num.setter
    def step_num(self, step_num):
        """Sets the step_num of this JobExeResult.

        步骤数量。

        :param step_num: The step_num of this JobExeResult.
        :type step_num: int
        """
        self._step_num = step_num

    @property
    def task_num(self):
        """Gets the task_num of this JobExeResult.

        任务数量。

        :return: The task_num of this JobExeResult.
        :rtype: int
        """
        return self._task_num

    @task_num.setter
    def task_num(self, task_num):
        """Sets the task_num of this JobExeResult.

        任务数量。

        :param task_num: The task_num of this JobExeResult.
        :type task_num: int
        """
        self._task_num = task_num

    @property
    def update_by(self):
        """Gets the update_by of this JobExeResult.

        更新作业的用户ID。

        :return: The update_by of this JobExeResult.
        :rtype: str
        """
        return self._update_by

    @update_by.setter
    def update_by(self, update_by):
        """Sets the update_by of this JobExeResult.

        更新作业的用户ID。

        :param update_by: The update_by of this JobExeResult.
        :type update_by: str
        """
        self._update_by = update_by

    @property
    def spend_time(self):
        """Gets the spend_time of this JobExeResult.

        作业执行持续时间，单位：秒。

        :return: The spend_time of this JobExeResult.
        :rtype: float
        """
        return self._spend_time

    @spend_time.setter
    def spend_time(self, spend_time):
        """Sets the spend_time of this JobExeResult.

        作业执行持续时间，单位：秒。

        :param spend_time: The spend_time of this JobExeResult.
        :type spend_time: float
        """
        self._spend_time = spend_time

    @property
    def step_seq(self):
        """Gets the step_seq of this JobExeResult.

        步骤序列号。

        :return: The step_seq of this JobExeResult.
        :rtype: int
        """
        return self._step_seq

    @step_seq.setter
    def step_seq(self, step_seq):
        """Sets the step_seq of this JobExeResult.

        步骤序列号。

        :param step_seq: The step_seq of this JobExeResult.
        :type step_seq: int
        """
        self._step_seq = step_seq

    @property
    def progress(self):
        """Gets the progress of this JobExeResult.

        作业执行进度。

        :return: The progress of this JobExeResult.
        :rtype: str
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this JobExeResult.

        作业执行进度。

        :param progress: The progress of this JobExeResult.
        :type progress: str
        """
        self._progress = progress

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
        if not isinstance(other, JobExeResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
