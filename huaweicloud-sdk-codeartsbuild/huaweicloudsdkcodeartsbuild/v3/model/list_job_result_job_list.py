# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListJobResultJobList:

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
        'job_name': 'str',
        'job_creator': 'str',
        'user_id': 'str',
        'user_name': 'str',
        'nick_name': 'str',
        'project_id': 'str',
        'project_name': 'str',
        'last_build_time': 'float',
        'health_score': 'int',
        'source_code': 'str',
        'last_build_status': 'str',
        'last_job_running_status': 'str',
        'last_build_user': 'str',
        'last_build_user_id': 'str',
        'is_finished': 'bool',
        'disabled': 'bool',
        'favorite': 'bool',
        'is_modify': 'bool',
        'is_delete': 'bool',
        'is_view': 'bool',
        'is_execute': 'bool',
        'is_copy': 'bool',
        'is_forbidden': 'bool',
        'task_id': 'str',
        'code_branch': 'str',
        'commit_id': 'str',
        'trigger_type': 'str',
        'build_time': 'float',
        'scm_web_url': 'str',
        'scm_type': 'str',
        'repo_id': 'str',
        'commit_detail_url': 'str',
        'build_number': 'str',
        'forbidden_msg': 'str',
        'build_project_id': 'str',
        'build_type': 'str',
        'tag': 'str',
        'project_permission_switch': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'job_name': 'job_name',
        'job_creator': 'job_creator',
        'user_id': 'user_id',
        'user_name': 'user_name',
        'nick_name': 'nick_name',
        'project_id': 'project_id',
        'project_name': 'project_name',
        'last_build_time': 'last_build_time',
        'health_score': 'health_score',
        'source_code': 'source_code',
        'last_build_status': 'last_build_status',
        'last_job_running_status': 'last_job_running_status',
        'last_build_user': 'last_build_user',
        'last_build_user_id': 'last_build_user_id',
        'is_finished': 'is_finished',
        'disabled': 'disabled',
        'favorite': 'favorite',
        'is_modify': 'is_modify',
        'is_delete': 'is_delete',
        'is_view': 'is_view',
        'is_execute': 'is_execute',
        'is_copy': 'is_copy',
        'is_forbidden': 'is_forbidden',
        'task_id': 'task_id',
        'code_branch': 'code_branch',
        'commit_id': 'commit_id',
        'trigger_type': 'trigger_type',
        'build_time': 'build_time',
        'scm_web_url': 'scm_web_url',
        'scm_type': 'scm_type',
        'repo_id': 'repo_id',
        'commit_detail_url': 'commit_detail_url',
        'build_number': 'build_number',
        'forbidden_msg': 'forbidden_msg',
        'build_project_id': 'build_project_id',
        'build_type': 'build_type',
        'tag': 'tag',
        'project_permission_switch': 'project_permission_switch'
    }

    def __init__(self, id=None, job_name=None, job_creator=None, user_id=None, user_name=None, nick_name=None, project_id=None, project_name=None, last_build_time=None, health_score=None, source_code=None, last_build_status=None, last_job_running_status=None, last_build_user=None, last_build_user_id=None, is_finished=None, disabled=None, favorite=None, is_modify=None, is_delete=None, is_view=None, is_execute=None, is_copy=None, is_forbidden=None, task_id=None, code_branch=None, commit_id=None, trigger_type=None, build_time=None, scm_web_url=None, scm_type=None, repo_id=None, commit_detail_url=None, build_number=None, forbidden_msg=None, build_project_id=None, build_type=None, tag=None, project_permission_switch=None):
        r"""ListJobResultJobList

        The model defined in huaweicloud sdk

        :param id: 任务ID
        :type id: str
        :param job_name: 任务名称
        :type job_name: str
        :param job_creator: 任务创建者
        :type job_creator: str
        :param user_id: 用户id
        :type user_id: str
        :param user_name: 用户名
        :type user_name: str
        :param nick_name: 用户昵称
        :type nick_name: str
        :param project_id: 构建任务所在项目的ID
        :type project_id: str
        :param project_name: 构建任务所在项目的名称
        :type project_name: str
        :param last_build_time: 最新执行时间
        :type last_build_time: float
        :param health_score: 健康分值
        :type health_score: int
        :param source_code: 代码来源
        :type source_code: str
        :param last_build_status: 最新构建状态
        :type last_build_status: str
        :param last_job_running_status: 最新运行状态
        :type last_job_running_status: str
        :param last_build_user: 执行用户
        :type last_build_user: str
        :param last_build_user_id: 执行用户ID
        :type last_build_user_id: str
        :param is_finished: 是否已结束
        :type is_finished: bool
        :param disabled: 是否已禁用
        :type disabled: bool
        :param favorite: 是否已收藏
        :type favorite: bool
        :param is_modify: 是否有修改任务权限
        :type is_modify: bool
        :param is_delete: 是否有删除任务权限
        :type is_delete: bool
        :param is_view: 是否有查看任务权限
        :type is_view: bool
        :param is_execute: 是否有执行任务权限
        :type is_execute: bool
        :param is_copy: 是否有复制任务权限
        :type is_copy: bool
        :param is_forbidden: 是否有禁用任务权限
        :type is_forbidden: bool
        :param task_id: 任务记录编号
        :type task_id: str
        :param code_branch: 代码分支
        :type code_branch: str
        :param commit_id: 代码提交ID
        :type commit_id: str
        :param trigger_type: 触发类型
        :type trigger_type: str
        :param build_time: 执行时间
        :type build_time: float
        :param scm_web_url: 代码源地址
        :type scm_web_url: str
        :param scm_type: 仓库类别，Repo、Github等
        :type scm_type: str
        :param repo_id: repo的id
        :type repo_id: str
        :param commit_detail_url: 代码提交记录信息地址（代码源为Repo)
        :type commit_detail_url: str
        :param build_number: 构建编号
        :type build_number: str
        :param forbidden_msg: 禁用消息
        :type forbidden_msg: str
        :param build_project_id: 构建工程ID,唯一对应codeci_job_id
        :type build_project_id: str
        :param build_type: 构建类别
        :type build_type: str
        :param tag: 仓库tag
        :type tag: str
        :param project_permission_switch: 使用项目权限
        :type project_permission_switch: bool
        """
        
        

        self._id = None
        self._job_name = None
        self._job_creator = None
        self._user_id = None
        self._user_name = None
        self._nick_name = None
        self._project_id = None
        self._project_name = None
        self._last_build_time = None
        self._health_score = None
        self._source_code = None
        self._last_build_status = None
        self._last_job_running_status = None
        self._last_build_user = None
        self._last_build_user_id = None
        self._is_finished = None
        self._disabled = None
        self._favorite = None
        self._is_modify = None
        self._is_delete = None
        self._is_view = None
        self._is_execute = None
        self._is_copy = None
        self._is_forbidden = None
        self._task_id = None
        self._code_branch = None
        self._commit_id = None
        self._trigger_type = None
        self._build_time = None
        self._scm_web_url = None
        self._scm_type = None
        self._repo_id = None
        self._commit_detail_url = None
        self._build_number = None
        self._forbidden_msg = None
        self._build_project_id = None
        self._build_type = None
        self._tag = None
        self._project_permission_switch = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if job_name is not None:
            self.job_name = job_name
        if job_creator is not None:
            self.job_creator = job_creator
        if user_id is not None:
            self.user_id = user_id
        if user_name is not None:
            self.user_name = user_name
        if nick_name is not None:
            self.nick_name = nick_name
        if project_id is not None:
            self.project_id = project_id
        if project_name is not None:
            self.project_name = project_name
        if last_build_time is not None:
            self.last_build_time = last_build_time
        if health_score is not None:
            self.health_score = health_score
        if source_code is not None:
            self.source_code = source_code
        if last_build_status is not None:
            self.last_build_status = last_build_status
        if last_job_running_status is not None:
            self.last_job_running_status = last_job_running_status
        if last_build_user is not None:
            self.last_build_user = last_build_user
        if last_build_user_id is not None:
            self.last_build_user_id = last_build_user_id
        if is_finished is not None:
            self.is_finished = is_finished
        if disabled is not None:
            self.disabled = disabled
        if favorite is not None:
            self.favorite = favorite
        if is_modify is not None:
            self.is_modify = is_modify
        if is_delete is not None:
            self.is_delete = is_delete
        if is_view is not None:
            self.is_view = is_view
        if is_execute is not None:
            self.is_execute = is_execute
        if is_copy is not None:
            self.is_copy = is_copy
        if is_forbidden is not None:
            self.is_forbidden = is_forbidden
        if task_id is not None:
            self.task_id = task_id
        if code_branch is not None:
            self.code_branch = code_branch
        if commit_id is not None:
            self.commit_id = commit_id
        if trigger_type is not None:
            self.trigger_type = trigger_type
        if build_time is not None:
            self.build_time = build_time
        if scm_web_url is not None:
            self.scm_web_url = scm_web_url
        if scm_type is not None:
            self.scm_type = scm_type
        if repo_id is not None:
            self.repo_id = repo_id
        if commit_detail_url is not None:
            self.commit_detail_url = commit_detail_url
        if build_number is not None:
            self.build_number = build_number
        if forbidden_msg is not None:
            self.forbidden_msg = forbidden_msg
        if build_project_id is not None:
            self.build_project_id = build_project_id
        if build_type is not None:
            self.build_type = build_type
        if tag is not None:
            self.tag = tag
        if project_permission_switch is not None:
            self.project_permission_switch = project_permission_switch

    @property
    def id(self):
        r"""Gets the id of this ListJobResultJobList.

        任务ID

        :return: The id of this ListJobResultJobList.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListJobResultJobList.

        任务ID

        :param id: The id of this ListJobResultJobList.
        :type id: str
        """
        self._id = id

    @property
    def job_name(self):
        r"""Gets the job_name of this ListJobResultJobList.

        任务名称

        :return: The job_name of this ListJobResultJobList.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        r"""Sets the job_name of this ListJobResultJobList.

        任务名称

        :param job_name: The job_name of this ListJobResultJobList.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def job_creator(self):
        r"""Gets the job_creator of this ListJobResultJobList.

        任务创建者

        :return: The job_creator of this ListJobResultJobList.
        :rtype: str
        """
        return self._job_creator

    @job_creator.setter
    def job_creator(self, job_creator):
        r"""Sets the job_creator of this ListJobResultJobList.

        任务创建者

        :param job_creator: The job_creator of this ListJobResultJobList.
        :type job_creator: str
        """
        self._job_creator = job_creator

    @property
    def user_id(self):
        r"""Gets the user_id of this ListJobResultJobList.

        用户id

        :return: The user_id of this ListJobResultJobList.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this ListJobResultJobList.

        用户id

        :param user_id: The user_id of this ListJobResultJobList.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def user_name(self):
        r"""Gets the user_name of this ListJobResultJobList.

        用户名

        :return: The user_name of this ListJobResultJobList.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ListJobResultJobList.

        用户名

        :param user_name: The user_name of this ListJobResultJobList.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def nick_name(self):
        r"""Gets the nick_name of this ListJobResultJobList.

        用户昵称

        :return: The nick_name of this ListJobResultJobList.
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        r"""Sets the nick_name of this ListJobResultJobList.

        用户昵称

        :param nick_name: The nick_name of this ListJobResultJobList.
        :type nick_name: str
        """
        self._nick_name = nick_name

    @property
    def project_id(self):
        r"""Gets the project_id of this ListJobResultJobList.

        构建任务所在项目的ID

        :return: The project_id of this ListJobResultJobList.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListJobResultJobList.

        构建任务所在项目的ID

        :param project_id: The project_id of this ListJobResultJobList.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def project_name(self):
        r"""Gets the project_name of this ListJobResultJobList.

        构建任务所在项目的名称

        :return: The project_name of this ListJobResultJobList.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        r"""Sets the project_name of this ListJobResultJobList.

        构建任务所在项目的名称

        :param project_name: The project_name of this ListJobResultJobList.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def last_build_time(self):
        r"""Gets the last_build_time of this ListJobResultJobList.

        最新执行时间

        :return: The last_build_time of this ListJobResultJobList.
        :rtype: float
        """
        return self._last_build_time

    @last_build_time.setter
    def last_build_time(self, last_build_time):
        r"""Sets the last_build_time of this ListJobResultJobList.

        最新执行时间

        :param last_build_time: The last_build_time of this ListJobResultJobList.
        :type last_build_time: float
        """
        self._last_build_time = last_build_time

    @property
    def health_score(self):
        r"""Gets the health_score of this ListJobResultJobList.

        健康分值

        :return: The health_score of this ListJobResultJobList.
        :rtype: int
        """
        return self._health_score

    @health_score.setter
    def health_score(self, health_score):
        r"""Sets the health_score of this ListJobResultJobList.

        健康分值

        :param health_score: The health_score of this ListJobResultJobList.
        :type health_score: int
        """
        self._health_score = health_score

    @property
    def source_code(self):
        r"""Gets the source_code of this ListJobResultJobList.

        代码来源

        :return: The source_code of this ListJobResultJobList.
        :rtype: str
        """
        return self._source_code

    @source_code.setter
    def source_code(self, source_code):
        r"""Sets the source_code of this ListJobResultJobList.

        代码来源

        :param source_code: The source_code of this ListJobResultJobList.
        :type source_code: str
        """
        self._source_code = source_code

    @property
    def last_build_status(self):
        r"""Gets the last_build_status of this ListJobResultJobList.

        最新构建状态

        :return: The last_build_status of this ListJobResultJobList.
        :rtype: str
        """
        return self._last_build_status

    @last_build_status.setter
    def last_build_status(self, last_build_status):
        r"""Sets the last_build_status of this ListJobResultJobList.

        最新构建状态

        :param last_build_status: The last_build_status of this ListJobResultJobList.
        :type last_build_status: str
        """
        self._last_build_status = last_build_status

    @property
    def last_job_running_status(self):
        r"""Gets the last_job_running_status of this ListJobResultJobList.

        最新运行状态

        :return: The last_job_running_status of this ListJobResultJobList.
        :rtype: str
        """
        return self._last_job_running_status

    @last_job_running_status.setter
    def last_job_running_status(self, last_job_running_status):
        r"""Sets the last_job_running_status of this ListJobResultJobList.

        最新运行状态

        :param last_job_running_status: The last_job_running_status of this ListJobResultJobList.
        :type last_job_running_status: str
        """
        self._last_job_running_status = last_job_running_status

    @property
    def last_build_user(self):
        r"""Gets the last_build_user of this ListJobResultJobList.

        执行用户

        :return: The last_build_user of this ListJobResultJobList.
        :rtype: str
        """
        return self._last_build_user

    @last_build_user.setter
    def last_build_user(self, last_build_user):
        r"""Sets the last_build_user of this ListJobResultJobList.

        执行用户

        :param last_build_user: The last_build_user of this ListJobResultJobList.
        :type last_build_user: str
        """
        self._last_build_user = last_build_user

    @property
    def last_build_user_id(self):
        r"""Gets the last_build_user_id of this ListJobResultJobList.

        执行用户ID

        :return: The last_build_user_id of this ListJobResultJobList.
        :rtype: str
        """
        return self._last_build_user_id

    @last_build_user_id.setter
    def last_build_user_id(self, last_build_user_id):
        r"""Sets the last_build_user_id of this ListJobResultJobList.

        执行用户ID

        :param last_build_user_id: The last_build_user_id of this ListJobResultJobList.
        :type last_build_user_id: str
        """
        self._last_build_user_id = last_build_user_id

    @property
    def is_finished(self):
        r"""Gets the is_finished of this ListJobResultJobList.

        是否已结束

        :return: The is_finished of this ListJobResultJobList.
        :rtype: bool
        """
        return self._is_finished

    @is_finished.setter
    def is_finished(self, is_finished):
        r"""Sets the is_finished of this ListJobResultJobList.

        是否已结束

        :param is_finished: The is_finished of this ListJobResultJobList.
        :type is_finished: bool
        """
        self._is_finished = is_finished

    @property
    def disabled(self):
        r"""Gets the disabled of this ListJobResultJobList.

        是否已禁用

        :return: The disabled of this ListJobResultJobList.
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        r"""Sets the disabled of this ListJobResultJobList.

        是否已禁用

        :param disabled: The disabled of this ListJobResultJobList.
        :type disabled: bool
        """
        self._disabled = disabled

    @property
    def favorite(self):
        r"""Gets the favorite of this ListJobResultJobList.

        是否已收藏

        :return: The favorite of this ListJobResultJobList.
        :rtype: bool
        """
        return self._favorite

    @favorite.setter
    def favorite(self, favorite):
        r"""Sets the favorite of this ListJobResultJobList.

        是否已收藏

        :param favorite: The favorite of this ListJobResultJobList.
        :type favorite: bool
        """
        self._favorite = favorite

    @property
    def is_modify(self):
        r"""Gets the is_modify of this ListJobResultJobList.

        是否有修改任务权限

        :return: The is_modify of this ListJobResultJobList.
        :rtype: bool
        """
        return self._is_modify

    @is_modify.setter
    def is_modify(self, is_modify):
        r"""Sets the is_modify of this ListJobResultJobList.

        是否有修改任务权限

        :param is_modify: The is_modify of this ListJobResultJobList.
        :type is_modify: bool
        """
        self._is_modify = is_modify

    @property
    def is_delete(self):
        r"""Gets the is_delete of this ListJobResultJobList.

        是否有删除任务权限

        :return: The is_delete of this ListJobResultJobList.
        :rtype: bool
        """
        return self._is_delete

    @is_delete.setter
    def is_delete(self, is_delete):
        r"""Sets the is_delete of this ListJobResultJobList.

        是否有删除任务权限

        :param is_delete: The is_delete of this ListJobResultJobList.
        :type is_delete: bool
        """
        self._is_delete = is_delete

    @property
    def is_view(self):
        r"""Gets the is_view of this ListJobResultJobList.

        是否有查看任务权限

        :return: The is_view of this ListJobResultJobList.
        :rtype: bool
        """
        return self._is_view

    @is_view.setter
    def is_view(self, is_view):
        r"""Sets the is_view of this ListJobResultJobList.

        是否有查看任务权限

        :param is_view: The is_view of this ListJobResultJobList.
        :type is_view: bool
        """
        self._is_view = is_view

    @property
    def is_execute(self):
        r"""Gets the is_execute of this ListJobResultJobList.

        是否有执行任务权限

        :return: The is_execute of this ListJobResultJobList.
        :rtype: bool
        """
        return self._is_execute

    @is_execute.setter
    def is_execute(self, is_execute):
        r"""Sets the is_execute of this ListJobResultJobList.

        是否有执行任务权限

        :param is_execute: The is_execute of this ListJobResultJobList.
        :type is_execute: bool
        """
        self._is_execute = is_execute

    @property
    def is_copy(self):
        r"""Gets the is_copy of this ListJobResultJobList.

        是否有复制任务权限

        :return: The is_copy of this ListJobResultJobList.
        :rtype: bool
        """
        return self._is_copy

    @is_copy.setter
    def is_copy(self, is_copy):
        r"""Sets the is_copy of this ListJobResultJobList.

        是否有复制任务权限

        :param is_copy: The is_copy of this ListJobResultJobList.
        :type is_copy: bool
        """
        self._is_copy = is_copy

    @property
    def is_forbidden(self):
        r"""Gets the is_forbidden of this ListJobResultJobList.

        是否有禁用任务权限

        :return: The is_forbidden of this ListJobResultJobList.
        :rtype: bool
        """
        return self._is_forbidden

    @is_forbidden.setter
    def is_forbidden(self, is_forbidden):
        r"""Sets the is_forbidden of this ListJobResultJobList.

        是否有禁用任务权限

        :param is_forbidden: The is_forbidden of this ListJobResultJobList.
        :type is_forbidden: bool
        """
        self._is_forbidden = is_forbidden

    @property
    def task_id(self):
        r"""Gets the task_id of this ListJobResultJobList.

        任务记录编号

        :return: The task_id of this ListJobResultJobList.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ListJobResultJobList.

        任务记录编号

        :param task_id: The task_id of this ListJobResultJobList.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def code_branch(self):
        r"""Gets the code_branch of this ListJobResultJobList.

        代码分支

        :return: The code_branch of this ListJobResultJobList.
        :rtype: str
        """
        return self._code_branch

    @code_branch.setter
    def code_branch(self, code_branch):
        r"""Sets the code_branch of this ListJobResultJobList.

        代码分支

        :param code_branch: The code_branch of this ListJobResultJobList.
        :type code_branch: str
        """
        self._code_branch = code_branch

    @property
    def commit_id(self):
        r"""Gets the commit_id of this ListJobResultJobList.

        代码提交ID

        :return: The commit_id of this ListJobResultJobList.
        :rtype: str
        """
        return self._commit_id

    @commit_id.setter
    def commit_id(self, commit_id):
        r"""Sets the commit_id of this ListJobResultJobList.

        代码提交ID

        :param commit_id: The commit_id of this ListJobResultJobList.
        :type commit_id: str
        """
        self._commit_id = commit_id

    @property
    def trigger_type(self):
        r"""Gets the trigger_type of this ListJobResultJobList.

        触发类型

        :return: The trigger_type of this ListJobResultJobList.
        :rtype: str
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        r"""Sets the trigger_type of this ListJobResultJobList.

        触发类型

        :param trigger_type: The trigger_type of this ListJobResultJobList.
        :type trigger_type: str
        """
        self._trigger_type = trigger_type

    @property
    def build_time(self):
        r"""Gets the build_time of this ListJobResultJobList.

        执行时间

        :return: The build_time of this ListJobResultJobList.
        :rtype: float
        """
        return self._build_time

    @build_time.setter
    def build_time(self, build_time):
        r"""Sets the build_time of this ListJobResultJobList.

        执行时间

        :param build_time: The build_time of this ListJobResultJobList.
        :type build_time: float
        """
        self._build_time = build_time

    @property
    def scm_web_url(self):
        r"""Gets the scm_web_url of this ListJobResultJobList.

        代码源地址

        :return: The scm_web_url of this ListJobResultJobList.
        :rtype: str
        """
        return self._scm_web_url

    @scm_web_url.setter
    def scm_web_url(self, scm_web_url):
        r"""Sets the scm_web_url of this ListJobResultJobList.

        代码源地址

        :param scm_web_url: The scm_web_url of this ListJobResultJobList.
        :type scm_web_url: str
        """
        self._scm_web_url = scm_web_url

    @property
    def scm_type(self):
        r"""Gets the scm_type of this ListJobResultJobList.

        仓库类别，Repo、Github等

        :return: The scm_type of this ListJobResultJobList.
        :rtype: str
        """
        return self._scm_type

    @scm_type.setter
    def scm_type(self, scm_type):
        r"""Sets the scm_type of this ListJobResultJobList.

        仓库类别，Repo、Github等

        :param scm_type: The scm_type of this ListJobResultJobList.
        :type scm_type: str
        """
        self._scm_type = scm_type

    @property
    def repo_id(self):
        r"""Gets the repo_id of this ListJobResultJobList.

        repo的id

        :return: The repo_id of this ListJobResultJobList.
        :rtype: str
        """
        return self._repo_id

    @repo_id.setter
    def repo_id(self, repo_id):
        r"""Sets the repo_id of this ListJobResultJobList.

        repo的id

        :param repo_id: The repo_id of this ListJobResultJobList.
        :type repo_id: str
        """
        self._repo_id = repo_id

    @property
    def commit_detail_url(self):
        r"""Gets the commit_detail_url of this ListJobResultJobList.

        代码提交记录信息地址（代码源为Repo)

        :return: The commit_detail_url of this ListJobResultJobList.
        :rtype: str
        """
        return self._commit_detail_url

    @commit_detail_url.setter
    def commit_detail_url(self, commit_detail_url):
        r"""Sets the commit_detail_url of this ListJobResultJobList.

        代码提交记录信息地址（代码源为Repo)

        :param commit_detail_url: The commit_detail_url of this ListJobResultJobList.
        :type commit_detail_url: str
        """
        self._commit_detail_url = commit_detail_url

    @property
    def build_number(self):
        r"""Gets the build_number of this ListJobResultJobList.

        构建编号

        :return: The build_number of this ListJobResultJobList.
        :rtype: str
        """
        return self._build_number

    @build_number.setter
    def build_number(self, build_number):
        r"""Sets the build_number of this ListJobResultJobList.

        构建编号

        :param build_number: The build_number of this ListJobResultJobList.
        :type build_number: str
        """
        self._build_number = build_number

    @property
    def forbidden_msg(self):
        r"""Gets the forbidden_msg of this ListJobResultJobList.

        禁用消息

        :return: The forbidden_msg of this ListJobResultJobList.
        :rtype: str
        """
        return self._forbidden_msg

    @forbidden_msg.setter
    def forbidden_msg(self, forbidden_msg):
        r"""Sets the forbidden_msg of this ListJobResultJobList.

        禁用消息

        :param forbidden_msg: The forbidden_msg of this ListJobResultJobList.
        :type forbidden_msg: str
        """
        self._forbidden_msg = forbidden_msg

    @property
    def build_project_id(self):
        r"""Gets the build_project_id of this ListJobResultJobList.

        构建工程ID,唯一对应codeci_job_id

        :return: The build_project_id of this ListJobResultJobList.
        :rtype: str
        """
        return self._build_project_id

    @build_project_id.setter
    def build_project_id(self, build_project_id):
        r"""Sets the build_project_id of this ListJobResultJobList.

        构建工程ID,唯一对应codeci_job_id

        :param build_project_id: The build_project_id of this ListJobResultJobList.
        :type build_project_id: str
        """
        self._build_project_id = build_project_id

    @property
    def build_type(self):
        r"""Gets the build_type of this ListJobResultJobList.

        构建类别

        :return: The build_type of this ListJobResultJobList.
        :rtype: str
        """
        return self._build_type

    @build_type.setter
    def build_type(self, build_type):
        r"""Sets the build_type of this ListJobResultJobList.

        构建类别

        :param build_type: The build_type of this ListJobResultJobList.
        :type build_type: str
        """
        self._build_type = build_type

    @property
    def tag(self):
        r"""Gets the tag of this ListJobResultJobList.

        仓库tag

        :return: The tag of this ListJobResultJobList.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this ListJobResultJobList.

        仓库tag

        :param tag: The tag of this ListJobResultJobList.
        :type tag: str
        """
        self._tag = tag

    @property
    def project_permission_switch(self):
        r"""Gets the project_permission_switch of this ListJobResultJobList.

        使用项目权限

        :return: The project_permission_switch of this ListJobResultJobList.
        :rtype: bool
        """
        return self._project_permission_switch

    @project_permission_switch.setter
    def project_permission_switch(self, project_permission_switch):
        r"""Sets the project_permission_switch of this ListJobResultJobList.

        使用项目权限

        :param project_permission_switch: The project_permission_switch of this ListJobResultJobList.
        :type project_permission_switch: bool
        """
        self._project_permission_switch = project_permission_switch

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
        if not isinstance(other, ListJobResultJobList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
