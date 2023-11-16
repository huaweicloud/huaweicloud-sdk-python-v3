# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecordInfoResult:

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
        'build_project_id': 'str',
        'build_record_id': 'str',
        'parent_record_id': 'str',
        'devcloud_project_id': 'str',
        'codeci_job_id': 'str',
        'user_id': 'str',
        'build_no': 'int',
        'daily_build_num': 'str',
        'execution_id': 'str',
        'repo_name': 'str',
        'repo_id': 'str',
        'branch': 'str',
        'tag': 'str',
        'commit': 'str',
        'commit_message': 'str',
        'commit_create_time': 'str',
        'trigger_type': 'str',
        'build_type': 'str',
        'status': 'str',
        'domain_id': 'str',
        'create_time': 'str',
        'schedule_time': 'str',
        'queued_time': 'str',
        'start_time': 'str',
        'runnable_time': 'str',
        'finish_time': 'str',
        'duration': 'float',
        'record_status': 'str',
        'use_private_slave': 'int',
        'region': 'str',
        'err_msg': 'str',
        'build_config_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'build_project_id': 'build_project_id',
        'build_record_id': 'build_record_id',
        'parent_record_id': 'parent_record_id',
        'devcloud_project_id': 'devcloud_project_id',
        'codeci_job_id': 'codeci_job_id',
        'user_id': 'user_id',
        'build_no': 'build_no',
        'daily_build_num': 'daily_build_num',
        'execution_id': 'execution_id',
        'repo_name': 'repo_name',
        'repo_id': 'repo_id',
        'branch': 'branch',
        'tag': 'tag',
        'commit': 'commit',
        'commit_message': 'commit_message',
        'commit_create_time': 'commit_create_time',
        'trigger_type': 'trigger_type',
        'build_type': 'build_type',
        'status': 'status',
        'domain_id': 'domain_id',
        'create_time': 'create_time',
        'schedule_time': 'schedule_time',
        'queued_time': 'queued_time',
        'start_time': 'start_time',
        'runnable_time': 'runnable_time',
        'finish_time': 'finish_time',
        'duration': 'duration',
        'record_status': 'record_status',
        'use_private_slave': 'use_private_slave',
        'region': 'region',
        'err_msg': 'err_msg',
        'build_config_type': 'build_config_type'
    }

    def __init__(self, id=None, build_project_id=None, build_record_id=None, parent_record_id=None, devcloud_project_id=None, codeci_job_id=None, user_id=None, build_no=None, daily_build_num=None, execution_id=None, repo_name=None, repo_id=None, branch=None, tag=None, commit=None, commit_message=None, commit_create_time=None, trigger_type=None, build_type=None, status=None, domain_id=None, create_time=None, schedule_time=None, queued_time=None, start_time=None, runnable_time=None, finish_time=None, duration=None, record_status=None, use_private_slave=None, region=None, err_msg=None, build_config_type=None):
        """RecordInfoResult

        The model defined in huaweicloud sdk

        :param id: id
        :type id: str
        :param build_project_id: 构建工程ID,唯一对应codeci_job_id
        :type build_project_id: str
        :param build_record_id: 构建记录ID
        :type build_record_id: str
        :param parent_record_id: 父构建记录ID
        :type parent_record_id: str
        :param devcloud_project_id: 项目ID
        :type devcloud_project_id: str
        :param codeci_job_id: codeci任务ID,唯一对应build_project_id
        :type codeci_job_id: str
        :param user_id: 用户ID
        :type user_id: str
        :param build_no: 构建编号
        :type build_no: int
        :param daily_build_num: 每日构建编号，每日从1开始
        :type daily_build_num: str
        :param execution_id: 八爪鱼任务ID
        :type execution_id: str
        :param repo_name: 仓库名称
        :type repo_name: str
        :param repo_id: 仓库id
        :type repo_id: str
        :param branch: 仓库分支
        :type branch: str
        :param tag: 仓库tag
        :type tag: str
        :param commit: 仓库commit ID
        :type commit: str
        :param commit_message: 仓库commit提交信息
        :type commit_message: str
        :param commit_create_time: commit创建时间
        :type commit_create_time: str
        :param trigger_type: 触发类型
        :type trigger_type: str
        :param build_type: 构建类型
        :type build_type: str
        :param status: 构建状态
        :type status: str
        :param domain_id: 租户ID
        :type domain_id: str
        :param create_time: 任务创建时间
        :type create_time: str
        :param schedule_time: 构建下发耗时
        :type schedule_time: str
        :param queued_time: 构建排队耗时
        :type queued_time: str
        :param start_time: 开始构建时间
        :type start_time: str
        :param runnable_time: 八爪鱼真正开始构建时间
        :type runnable_time: str
        :param finish_time: 构建结束时间
        :type finish_time: str
        :param duration: 构建时长
        :type duration: float
        :param record_status: record状态
        :type record_status: str
        :param use_private_slave: 是否使用自定义执行机
        :type use_private_slave: int
        :param region: 租户所在region
        :type region: str
        :param err_msg: 错误信息
        :type err_msg: str
        :param build_config_type: 构建配置类型，YAML或ACTION
        :type build_config_type: str
        """
        
        

        self._id = None
        self._build_project_id = None
        self._build_record_id = None
        self._parent_record_id = None
        self._devcloud_project_id = None
        self._codeci_job_id = None
        self._user_id = None
        self._build_no = None
        self._daily_build_num = None
        self._execution_id = None
        self._repo_name = None
        self._repo_id = None
        self._branch = None
        self._tag = None
        self._commit = None
        self._commit_message = None
        self._commit_create_time = None
        self._trigger_type = None
        self._build_type = None
        self._status = None
        self._domain_id = None
        self._create_time = None
        self._schedule_time = None
        self._queued_time = None
        self._start_time = None
        self._runnable_time = None
        self._finish_time = None
        self._duration = None
        self._record_status = None
        self._use_private_slave = None
        self._region = None
        self._err_msg = None
        self._build_config_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if build_project_id is not None:
            self.build_project_id = build_project_id
        if build_record_id is not None:
            self.build_record_id = build_record_id
        if parent_record_id is not None:
            self.parent_record_id = parent_record_id
        if devcloud_project_id is not None:
            self.devcloud_project_id = devcloud_project_id
        if codeci_job_id is not None:
            self.codeci_job_id = codeci_job_id
        if user_id is not None:
            self.user_id = user_id
        if build_no is not None:
            self.build_no = build_no
        if daily_build_num is not None:
            self.daily_build_num = daily_build_num
        if execution_id is not None:
            self.execution_id = execution_id
        if repo_name is not None:
            self.repo_name = repo_name
        if repo_id is not None:
            self.repo_id = repo_id
        if branch is not None:
            self.branch = branch
        if tag is not None:
            self.tag = tag
        if commit is not None:
            self.commit = commit
        if commit_message is not None:
            self.commit_message = commit_message
        if commit_create_time is not None:
            self.commit_create_time = commit_create_time
        if trigger_type is not None:
            self.trigger_type = trigger_type
        if build_type is not None:
            self.build_type = build_type
        if status is not None:
            self.status = status
        if domain_id is not None:
            self.domain_id = domain_id
        if create_time is not None:
            self.create_time = create_time
        if schedule_time is not None:
            self.schedule_time = schedule_time
        if queued_time is not None:
            self.queued_time = queued_time
        if start_time is not None:
            self.start_time = start_time
        if runnable_time is not None:
            self.runnable_time = runnable_time
        if finish_time is not None:
            self.finish_time = finish_time
        if duration is not None:
            self.duration = duration
        if record_status is not None:
            self.record_status = record_status
        if use_private_slave is not None:
            self.use_private_slave = use_private_slave
        if region is not None:
            self.region = region
        if err_msg is not None:
            self.err_msg = err_msg
        if build_config_type is not None:
            self.build_config_type = build_config_type

    @property
    def id(self):
        """Gets the id of this RecordInfoResult.

        id

        :return: The id of this RecordInfoResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RecordInfoResult.

        id

        :param id: The id of this RecordInfoResult.
        :type id: str
        """
        self._id = id

    @property
    def build_project_id(self):
        """Gets the build_project_id of this RecordInfoResult.

        构建工程ID,唯一对应codeci_job_id

        :return: The build_project_id of this RecordInfoResult.
        :rtype: str
        """
        return self._build_project_id

    @build_project_id.setter
    def build_project_id(self, build_project_id):
        """Sets the build_project_id of this RecordInfoResult.

        构建工程ID,唯一对应codeci_job_id

        :param build_project_id: The build_project_id of this RecordInfoResult.
        :type build_project_id: str
        """
        self._build_project_id = build_project_id

    @property
    def build_record_id(self):
        """Gets the build_record_id of this RecordInfoResult.

        构建记录ID

        :return: The build_record_id of this RecordInfoResult.
        :rtype: str
        """
        return self._build_record_id

    @build_record_id.setter
    def build_record_id(self, build_record_id):
        """Sets the build_record_id of this RecordInfoResult.

        构建记录ID

        :param build_record_id: The build_record_id of this RecordInfoResult.
        :type build_record_id: str
        """
        self._build_record_id = build_record_id

    @property
    def parent_record_id(self):
        """Gets the parent_record_id of this RecordInfoResult.

        父构建记录ID

        :return: The parent_record_id of this RecordInfoResult.
        :rtype: str
        """
        return self._parent_record_id

    @parent_record_id.setter
    def parent_record_id(self, parent_record_id):
        """Sets the parent_record_id of this RecordInfoResult.

        父构建记录ID

        :param parent_record_id: The parent_record_id of this RecordInfoResult.
        :type parent_record_id: str
        """
        self._parent_record_id = parent_record_id

    @property
    def devcloud_project_id(self):
        """Gets the devcloud_project_id of this RecordInfoResult.

        项目ID

        :return: The devcloud_project_id of this RecordInfoResult.
        :rtype: str
        """
        return self._devcloud_project_id

    @devcloud_project_id.setter
    def devcloud_project_id(self, devcloud_project_id):
        """Sets the devcloud_project_id of this RecordInfoResult.

        项目ID

        :param devcloud_project_id: The devcloud_project_id of this RecordInfoResult.
        :type devcloud_project_id: str
        """
        self._devcloud_project_id = devcloud_project_id

    @property
    def codeci_job_id(self):
        """Gets the codeci_job_id of this RecordInfoResult.

        codeci任务ID,唯一对应build_project_id

        :return: The codeci_job_id of this RecordInfoResult.
        :rtype: str
        """
        return self._codeci_job_id

    @codeci_job_id.setter
    def codeci_job_id(self, codeci_job_id):
        """Sets the codeci_job_id of this RecordInfoResult.

        codeci任务ID,唯一对应build_project_id

        :param codeci_job_id: The codeci_job_id of this RecordInfoResult.
        :type codeci_job_id: str
        """
        self._codeci_job_id = codeci_job_id

    @property
    def user_id(self):
        """Gets the user_id of this RecordInfoResult.

        用户ID

        :return: The user_id of this RecordInfoResult.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this RecordInfoResult.

        用户ID

        :param user_id: The user_id of this RecordInfoResult.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def build_no(self):
        """Gets the build_no of this RecordInfoResult.

        构建编号

        :return: The build_no of this RecordInfoResult.
        :rtype: int
        """
        return self._build_no

    @build_no.setter
    def build_no(self, build_no):
        """Sets the build_no of this RecordInfoResult.

        构建编号

        :param build_no: The build_no of this RecordInfoResult.
        :type build_no: int
        """
        self._build_no = build_no

    @property
    def daily_build_num(self):
        """Gets the daily_build_num of this RecordInfoResult.

        每日构建编号，每日从1开始

        :return: The daily_build_num of this RecordInfoResult.
        :rtype: str
        """
        return self._daily_build_num

    @daily_build_num.setter
    def daily_build_num(self, daily_build_num):
        """Sets the daily_build_num of this RecordInfoResult.

        每日构建编号，每日从1开始

        :param daily_build_num: The daily_build_num of this RecordInfoResult.
        :type daily_build_num: str
        """
        self._daily_build_num = daily_build_num

    @property
    def execution_id(self):
        """Gets the execution_id of this RecordInfoResult.

        八爪鱼任务ID

        :return: The execution_id of this RecordInfoResult.
        :rtype: str
        """
        return self._execution_id

    @execution_id.setter
    def execution_id(self, execution_id):
        """Sets the execution_id of this RecordInfoResult.

        八爪鱼任务ID

        :param execution_id: The execution_id of this RecordInfoResult.
        :type execution_id: str
        """
        self._execution_id = execution_id

    @property
    def repo_name(self):
        """Gets the repo_name of this RecordInfoResult.

        仓库名称

        :return: The repo_name of this RecordInfoResult.
        :rtype: str
        """
        return self._repo_name

    @repo_name.setter
    def repo_name(self, repo_name):
        """Sets the repo_name of this RecordInfoResult.

        仓库名称

        :param repo_name: The repo_name of this RecordInfoResult.
        :type repo_name: str
        """
        self._repo_name = repo_name

    @property
    def repo_id(self):
        """Gets the repo_id of this RecordInfoResult.

        仓库id

        :return: The repo_id of this RecordInfoResult.
        :rtype: str
        """
        return self._repo_id

    @repo_id.setter
    def repo_id(self, repo_id):
        """Sets the repo_id of this RecordInfoResult.

        仓库id

        :param repo_id: The repo_id of this RecordInfoResult.
        :type repo_id: str
        """
        self._repo_id = repo_id

    @property
    def branch(self):
        """Gets the branch of this RecordInfoResult.

        仓库分支

        :return: The branch of this RecordInfoResult.
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        """Sets the branch of this RecordInfoResult.

        仓库分支

        :param branch: The branch of this RecordInfoResult.
        :type branch: str
        """
        self._branch = branch

    @property
    def tag(self):
        """Gets the tag of this RecordInfoResult.

        仓库tag

        :return: The tag of this RecordInfoResult.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this RecordInfoResult.

        仓库tag

        :param tag: The tag of this RecordInfoResult.
        :type tag: str
        """
        self._tag = tag

    @property
    def commit(self):
        """Gets the commit of this RecordInfoResult.

        仓库commit ID

        :return: The commit of this RecordInfoResult.
        :rtype: str
        """
        return self._commit

    @commit.setter
    def commit(self, commit):
        """Sets the commit of this RecordInfoResult.

        仓库commit ID

        :param commit: The commit of this RecordInfoResult.
        :type commit: str
        """
        self._commit = commit

    @property
    def commit_message(self):
        """Gets the commit_message of this RecordInfoResult.

        仓库commit提交信息

        :return: The commit_message of this RecordInfoResult.
        :rtype: str
        """
        return self._commit_message

    @commit_message.setter
    def commit_message(self, commit_message):
        """Sets the commit_message of this RecordInfoResult.

        仓库commit提交信息

        :param commit_message: The commit_message of this RecordInfoResult.
        :type commit_message: str
        """
        self._commit_message = commit_message

    @property
    def commit_create_time(self):
        """Gets the commit_create_time of this RecordInfoResult.

        commit创建时间

        :return: The commit_create_time of this RecordInfoResult.
        :rtype: str
        """
        return self._commit_create_time

    @commit_create_time.setter
    def commit_create_time(self, commit_create_time):
        """Sets the commit_create_time of this RecordInfoResult.

        commit创建时间

        :param commit_create_time: The commit_create_time of this RecordInfoResult.
        :type commit_create_time: str
        """
        self._commit_create_time = commit_create_time

    @property
    def trigger_type(self):
        """Gets the trigger_type of this RecordInfoResult.

        触发类型

        :return: The trigger_type of this RecordInfoResult.
        :rtype: str
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        """Sets the trigger_type of this RecordInfoResult.

        触发类型

        :param trigger_type: The trigger_type of this RecordInfoResult.
        :type trigger_type: str
        """
        self._trigger_type = trigger_type

    @property
    def build_type(self):
        """Gets the build_type of this RecordInfoResult.

        构建类型

        :return: The build_type of this RecordInfoResult.
        :rtype: str
        """
        return self._build_type

    @build_type.setter
    def build_type(self, build_type):
        """Sets the build_type of this RecordInfoResult.

        构建类型

        :param build_type: The build_type of this RecordInfoResult.
        :type build_type: str
        """
        self._build_type = build_type

    @property
    def status(self):
        """Gets the status of this RecordInfoResult.

        构建状态

        :return: The status of this RecordInfoResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this RecordInfoResult.

        构建状态

        :param status: The status of this RecordInfoResult.
        :type status: str
        """
        self._status = status

    @property
    def domain_id(self):
        """Gets the domain_id of this RecordInfoResult.

        租户ID

        :return: The domain_id of this RecordInfoResult.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this RecordInfoResult.

        租户ID

        :param domain_id: The domain_id of this RecordInfoResult.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def create_time(self):
        """Gets the create_time of this RecordInfoResult.

        任务创建时间

        :return: The create_time of this RecordInfoResult.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this RecordInfoResult.

        任务创建时间

        :param create_time: The create_time of this RecordInfoResult.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def schedule_time(self):
        """Gets the schedule_time of this RecordInfoResult.

        构建下发耗时

        :return: The schedule_time of this RecordInfoResult.
        :rtype: str
        """
        return self._schedule_time

    @schedule_time.setter
    def schedule_time(self, schedule_time):
        """Sets the schedule_time of this RecordInfoResult.

        构建下发耗时

        :param schedule_time: The schedule_time of this RecordInfoResult.
        :type schedule_time: str
        """
        self._schedule_time = schedule_time

    @property
    def queued_time(self):
        """Gets the queued_time of this RecordInfoResult.

        构建排队耗时

        :return: The queued_time of this RecordInfoResult.
        :rtype: str
        """
        return self._queued_time

    @queued_time.setter
    def queued_time(self, queued_time):
        """Sets the queued_time of this RecordInfoResult.

        构建排队耗时

        :param queued_time: The queued_time of this RecordInfoResult.
        :type queued_time: str
        """
        self._queued_time = queued_time

    @property
    def start_time(self):
        """Gets the start_time of this RecordInfoResult.

        开始构建时间

        :return: The start_time of this RecordInfoResult.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this RecordInfoResult.

        开始构建时间

        :param start_time: The start_time of this RecordInfoResult.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def runnable_time(self):
        """Gets the runnable_time of this RecordInfoResult.

        八爪鱼真正开始构建时间

        :return: The runnable_time of this RecordInfoResult.
        :rtype: str
        """
        return self._runnable_time

    @runnable_time.setter
    def runnable_time(self, runnable_time):
        """Sets the runnable_time of this RecordInfoResult.

        八爪鱼真正开始构建时间

        :param runnable_time: The runnable_time of this RecordInfoResult.
        :type runnable_time: str
        """
        self._runnable_time = runnable_time

    @property
    def finish_time(self):
        """Gets the finish_time of this RecordInfoResult.

        构建结束时间

        :return: The finish_time of this RecordInfoResult.
        :rtype: str
        """
        return self._finish_time

    @finish_time.setter
    def finish_time(self, finish_time):
        """Sets the finish_time of this RecordInfoResult.

        构建结束时间

        :param finish_time: The finish_time of this RecordInfoResult.
        :type finish_time: str
        """
        self._finish_time = finish_time

    @property
    def duration(self):
        """Gets the duration of this RecordInfoResult.

        构建时长

        :return: The duration of this RecordInfoResult.
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this RecordInfoResult.

        构建时长

        :param duration: The duration of this RecordInfoResult.
        :type duration: float
        """
        self._duration = duration

    @property
    def record_status(self):
        """Gets the record_status of this RecordInfoResult.

        record状态

        :return: The record_status of this RecordInfoResult.
        :rtype: str
        """
        return self._record_status

    @record_status.setter
    def record_status(self, record_status):
        """Sets the record_status of this RecordInfoResult.

        record状态

        :param record_status: The record_status of this RecordInfoResult.
        :type record_status: str
        """
        self._record_status = record_status

    @property
    def use_private_slave(self):
        """Gets the use_private_slave of this RecordInfoResult.

        是否使用自定义执行机

        :return: The use_private_slave of this RecordInfoResult.
        :rtype: int
        """
        return self._use_private_slave

    @use_private_slave.setter
    def use_private_slave(self, use_private_slave):
        """Sets the use_private_slave of this RecordInfoResult.

        是否使用自定义执行机

        :param use_private_slave: The use_private_slave of this RecordInfoResult.
        :type use_private_slave: int
        """
        self._use_private_slave = use_private_slave

    @property
    def region(self):
        """Gets the region of this RecordInfoResult.

        租户所在region

        :return: The region of this RecordInfoResult.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this RecordInfoResult.

        租户所在region

        :param region: The region of this RecordInfoResult.
        :type region: str
        """
        self._region = region

    @property
    def err_msg(self):
        """Gets the err_msg of this RecordInfoResult.

        错误信息

        :return: The err_msg of this RecordInfoResult.
        :rtype: str
        """
        return self._err_msg

    @err_msg.setter
    def err_msg(self, err_msg):
        """Sets the err_msg of this RecordInfoResult.

        错误信息

        :param err_msg: The err_msg of this RecordInfoResult.
        :type err_msg: str
        """
        self._err_msg = err_msg

    @property
    def build_config_type(self):
        """Gets the build_config_type of this RecordInfoResult.

        构建配置类型，YAML或ACTION

        :return: The build_config_type of this RecordInfoResult.
        :rtype: str
        """
        return self._build_config_type

    @build_config_type.setter
    def build_config_type(self, build_config_type):
        """Sets the build_config_type of this RecordInfoResult.

        构建配置类型，YAML或ACTION

        :param build_config_type: The build_config_type of this RecordInfoResult.
        :type build_config_type: str
        """
        self._build_config_type = build_config_type

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
        if not isinstance(other, RecordInfoResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
