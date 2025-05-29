# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BuildRecord:

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
        'status': 'str',
        'status_code': 'int',
        'create_time': 'str',
        'schedule_time': 'str',
        'queued_time': 'str',
        'start_time': 'str',
        'finish_time': 'str',
        'duration': 'int',
        'build_duration': 'int',
        'pending_duration': 'int',
        'project_id': 'str',
        'display_name': 'str',
        'trigger_name': 'str',
        'group_name': 'str',
        'execution_id': 'str',
        'parameters': 'list[BuildRecordParameters]',
        'repository': 'str',
        'branch': 'str',
        'revision': 'str',
        'build_yml_path': 'str',
        'build_yml_url': 'str',
        'daily_build_number': 'str',
        'build_record_type': 'BuildRecordBuildRecordType',
        'trigger_type': 'str',
        'scm_type': 'str',
        'scm_web_url': 'str',
        'user_id': 'str',
        'build_no': 'str',
        'daily_build_no': 'str',
        'dev_cloud_build_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'status_code': 'status_code',
        'create_time': 'create_time',
        'schedule_time': 'schedule_time',
        'queued_time': 'queued_time',
        'start_time': 'start_time',
        'finish_time': 'finish_time',
        'duration': 'duration',
        'build_duration': 'build_duration',
        'pending_duration': 'pending_duration',
        'project_id': 'project_id',
        'display_name': 'display_name',
        'trigger_name': 'trigger_name',
        'group_name': 'group_name',
        'execution_id': 'execution_id',
        'parameters': 'parameters',
        'repository': 'repository',
        'branch': 'branch',
        'revision': 'revision',
        'build_yml_path': 'build_yml_path',
        'build_yml_url': 'build_yml_url',
        'daily_build_number': 'daily_build_number',
        'build_record_type': 'build_record_type',
        'trigger_type': 'trigger_type',
        'scm_type': 'scm_type',
        'scm_web_url': 'scm_web_url',
        'user_id': 'user_id',
        'build_no': 'build_no',
        'daily_build_no': 'daily_build_no',
        'dev_cloud_build_type': 'dev_cloud_build_type'
    }

    def __init__(self, id=None, status=None, status_code=None, create_time=None, schedule_time=None, queued_time=None, start_time=None, finish_time=None, duration=None, build_duration=None, pending_duration=None, project_id=None, display_name=None, trigger_name=None, group_name=None, execution_id=None, parameters=None, repository=None, branch=None, revision=None, build_yml_path=None, build_yml_url=None, daily_build_number=None, build_record_type=None, trigger_type=None, scm_type=None, scm_web_url=None, user_id=None, build_no=None, daily_build_no=None, dev_cloud_build_type=None):
        r"""BuildRecord

        The model defined in huaweicloud sdk

        :param id: 唯一标识
        :type id: str
        :param status: 状态
        :type status: str
        :param status_code: 状态码
        :type status_code: int
        :param create_time: 创建时间
        :type create_time: str
        :param schedule_time: 等待时间
        :type schedule_time: str
        :param queued_time: 排队时间
        :type queued_time: str
        :param start_time: 开始时间
        :type start_time: str
        :param finish_time: 完成时间
        :type finish_time: str
        :param duration: 持续时间
        :type duration: int
        :param build_duration: 构建时间
        :type build_duration: int
        :param pending_duration: 等待时间
        :type pending_duration: int
        :param project_id: 工程ID
        :type project_id: str
        :param display_name: 子任务名称
        :type display_name: str
        :param trigger_name: 触发者名称
        :type trigger_name: str
        :param group_name: 分组名
        :type group_name: str
        :param execution_id: 八爪鱼任务ID
        :type execution_id: str
        :param parameters: 构建执行参数列表
        :type parameters: list[:class:`huaweicloudsdkcodeartsbuild.v3.BuildRecordParameters`]
        :param repository: 仓库地址
        :type repository: str
        :param branch: 分支名
        :type branch: str
        :param revision: commitId
        :type revision: str
        :param build_yml_path: yaml路径
        :type build_yml_path: str
        :param build_yml_url: yaml地址
        :type build_yml_url: str
        :param daily_build_number: 构建每日编号
        :type daily_build_number: str
        :param build_record_type: 
        :type build_record_type: :class:`huaweicloudsdkcodeartsbuild.v3.BuildRecordBuildRecordType`
        :param trigger_type: 触发类型
        :type trigger_type: str
        :param scm_type: 代码源类型
        :type scm_type: str
        :param scm_web_url: 代码源地址
        :type scm_web_url: str
        :param user_id: 用户id
        :type user_id: str
        :param build_no: 构建编码
        :type build_no: str
        :param daily_build_no: 构建每日编号
        :type daily_build_no: str
        :param dev_cloud_build_type: 构建类型
        :type dev_cloud_build_type: str
        """
        
        

        self._id = None
        self._status = None
        self._status_code = None
        self._create_time = None
        self._schedule_time = None
        self._queued_time = None
        self._start_time = None
        self._finish_time = None
        self._duration = None
        self._build_duration = None
        self._pending_duration = None
        self._project_id = None
        self._display_name = None
        self._trigger_name = None
        self._group_name = None
        self._execution_id = None
        self._parameters = None
        self._repository = None
        self._branch = None
        self._revision = None
        self._build_yml_path = None
        self._build_yml_url = None
        self._daily_build_number = None
        self._build_record_type = None
        self._trigger_type = None
        self._scm_type = None
        self._scm_web_url = None
        self._user_id = None
        self._build_no = None
        self._daily_build_no = None
        self._dev_cloud_build_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if status_code is not None:
            self.status_code = status_code
        if create_time is not None:
            self.create_time = create_time
        if schedule_time is not None:
            self.schedule_time = schedule_time
        if queued_time is not None:
            self.queued_time = queued_time
        if start_time is not None:
            self.start_time = start_time
        if finish_time is not None:
            self.finish_time = finish_time
        if duration is not None:
            self.duration = duration
        if build_duration is not None:
            self.build_duration = build_duration
        if pending_duration is not None:
            self.pending_duration = pending_duration
        if project_id is not None:
            self.project_id = project_id
        if display_name is not None:
            self.display_name = display_name
        if trigger_name is not None:
            self.trigger_name = trigger_name
        if group_name is not None:
            self.group_name = group_name
        if execution_id is not None:
            self.execution_id = execution_id
        if parameters is not None:
            self.parameters = parameters
        if repository is not None:
            self.repository = repository
        if branch is not None:
            self.branch = branch
        if revision is not None:
            self.revision = revision
        if build_yml_path is not None:
            self.build_yml_path = build_yml_path
        if build_yml_url is not None:
            self.build_yml_url = build_yml_url
        if daily_build_number is not None:
            self.daily_build_number = daily_build_number
        if build_record_type is not None:
            self.build_record_type = build_record_type
        if trigger_type is not None:
            self.trigger_type = trigger_type
        if scm_type is not None:
            self.scm_type = scm_type
        if scm_web_url is not None:
            self.scm_web_url = scm_web_url
        if user_id is not None:
            self.user_id = user_id
        if build_no is not None:
            self.build_no = build_no
        if daily_build_no is not None:
            self.daily_build_no = daily_build_no
        if dev_cloud_build_type is not None:
            self.dev_cloud_build_type = dev_cloud_build_type

    @property
    def id(self):
        r"""Gets the id of this BuildRecord.

        唯一标识

        :return: The id of this BuildRecord.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BuildRecord.

        唯一标识

        :param id: The id of this BuildRecord.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        r"""Gets the status of this BuildRecord.

        状态

        :return: The status of this BuildRecord.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this BuildRecord.

        状态

        :param status: The status of this BuildRecord.
        :type status: str
        """
        self._status = status

    @property
    def status_code(self):
        r"""Gets the status_code of this BuildRecord.

        状态码

        :return: The status_code of this BuildRecord.
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        r"""Sets the status_code of this BuildRecord.

        状态码

        :param status_code: The status_code of this BuildRecord.
        :type status_code: int
        """
        self._status_code = status_code

    @property
    def create_time(self):
        r"""Gets the create_time of this BuildRecord.

        创建时间

        :return: The create_time of this BuildRecord.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this BuildRecord.

        创建时间

        :param create_time: The create_time of this BuildRecord.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def schedule_time(self):
        r"""Gets the schedule_time of this BuildRecord.

        等待时间

        :return: The schedule_time of this BuildRecord.
        :rtype: str
        """
        return self._schedule_time

    @schedule_time.setter
    def schedule_time(self, schedule_time):
        r"""Sets the schedule_time of this BuildRecord.

        等待时间

        :param schedule_time: The schedule_time of this BuildRecord.
        :type schedule_time: str
        """
        self._schedule_time = schedule_time

    @property
    def queued_time(self):
        r"""Gets the queued_time of this BuildRecord.

        排队时间

        :return: The queued_time of this BuildRecord.
        :rtype: str
        """
        return self._queued_time

    @queued_time.setter
    def queued_time(self, queued_time):
        r"""Sets the queued_time of this BuildRecord.

        排队时间

        :param queued_time: The queued_time of this BuildRecord.
        :type queued_time: str
        """
        self._queued_time = queued_time

    @property
    def start_time(self):
        r"""Gets the start_time of this BuildRecord.

        开始时间

        :return: The start_time of this BuildRecord.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this BuildRecord.

        开始时间

        :param start_time: The start_time of this BuildRecord.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def finish_time(self):
        r"""Gets the finish_time of this BuildRecord.

        完成时间

        :return: The finish_time of this BuildRecord.
        :rtype: str
        """
        return self._finish_time

    @finish_time.setter
    def finish_time(self, finish_time):
        r"""Sets the finish_time of this BuildRecord.

        完成时间

        :param finish_time: The finish_time of this BuildRecord.
        :type finish_time: str
        """
        self._finish_time = finish_time

    @property
    def duration(self):
        r"""Gets the duration of this BuildRecord.

        持续时间

        :return: The duration of this BuildRecord.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this BuildRecord.

        持续时间

        :param duration: The duration of this BuildRecord.
        :type duration: int
        """
        self._duration = duration

    @property
    def build_duration(self):
        r"""Gets the build_duration of this BuildRecord.

        构建时间

        :return: The build_duration of this BuildRecord.
        :rtype: int
        """
        return self._build_duration

    @build_duration.setter
    def build_duration(self, build_duration):
        r"""Sets the build_duration of this BuildRecord.

        构建时间

        :param build_duration: The build_duration of this BuildRecord.
        :type build_duration: int
        """
        self._build_duration = build_duration

    @property
    def pending_duration(self):
        r"""Gets the pending_duration of this BuildRecord.

        等待时间

        :return: The pending_duration of this BuildRecord.
        :rtype: int
        """
        return self._pending_duration

    @pending_duration.setter
    def pending_duration(self, pending_duration):
        r"""Sets the pending_duration of this BuildRecord.

        等待时间

        :param pending_duration: The pending_duration of this BuildRecord.
        :type pending_duration: int
        """
        self._pending_duration = pending_duration

    @property
    def project_id(self):
        r"""Gets the project_id of this BuildRecord.

        工程ID

        :return: The project_id of this BuildRecord.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this BuildRecord.

        工程ID

        :param project_id: The project_id of this BuildRecord.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def display_name(self):
        r"""Gets the display_name of this BuildRecord.

        子任务名称

        :return: The display_name of this BuildRecord.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this BuildRecord.

        子任务名称

        :param display_name: The display_name of this BuildRecord.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def trigger_name(self):
        r"""Gets the trigger_name of this BuildRecord.

        触发者名称

        :return: The trigger_name of this BuildRecord.
        :rtype: str
        """
        return self._trigger_name

    @trigger_name.setter
    def trigger_name(self, trigger_name):
        r"""Sets the trigger_name of this BuildRecord.

        触发者名称

        :param trigger_name: The trigger_name of this BuildRecord.
        :type trigger_name: str
        """
        self._trigger_name = trigger_name

    @property
    def group_name(self):
        r"""Gets the group_name of this BuildRecord.

        分组名

        :return: The group_name of this BuildRecord.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this BuildRecord.

        分组名

        :param group_name: The group_name of this BuildRecord.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def execution_id(self):
        r"""Gets the execution_id of this BuildRecord.

        八爪鱼任务ID

        :return: The execution_id of this BuildRecord.
        :rtype: str
        """
        return self._execution_id

    @execution_id.setter
    def execution_id(self, execution_id):
        r"""Sets the execution_id of this BuildRecord.

        八爪鱼任务ID

        :param execution_id: The execution_id of this BuildRecord.
        :type execution_id: str
        """
        self._execution_id = execution_id

    @property
    def parameters(self):
        r"""Gets the parameters of this BuildRecord.

        构建执行参数列表

        :return: The parameters of this BuildRecord.
        :rtype: list[:class:`huaweicloudsdkcodeartsbuild.v3.BuildRecordParameters`]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        r"""Sets the parameters of this BuildRecord.

        构建执行参数列表

        :param parameters: The parameters of this BuildRecord.
        :type parameters: list[:class:`huaweicloudsdkcodeartsbuild.v3.BuildRecordParameters`]
        """
        self._parameters = parameters

    @property
    def repository(self):
        r"""Gets the repository of this BuildRecord.

        仓库地址

        :return: The repository of this BuildRecord.
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        r"""Sets the repository of this BuildRecord.

        仓库地址

        :param repository: The repository of this BuildRecord.
        :type repository: str
        """
        self._repository = repository

    @property
    def branch(self):
        r"""Gets the branch of this BuildRecord.

        分支名

        :return: The branch of this BuildRecord.
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        r"""Sets the branch of this BuildRecord.

        分支名

        :param branch: The branch of this BuildRecord.
        :type branch: str
        """
        self._branch = branch

    @property
    def revision(self):
        r"""Gets the revision of this BuildRecord.

        commitId

        :return: The revision of this BuildRecord.
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        r"""Sets the revision of this BuildRecord.

        commitId

        :param revision: The revision of this BuildRecord.
        :type revision: str
        """
        self._revision = revision

    @property
    def build_yml_path(self):
        r"""Gets the build_yml_path of this BuildRecord.

        yaml路径

        :return: The build_yml_path of this BuildRecord.
        :rtype: str
        """
        return self._build_yml_path

    @build_yml_path.setter
    def build_yml_path(self, build_yml_path):
        r"""Sets the build_yml_path of this BuildRecord.

        yaml路径

        :param build_yml_path: The build_yml_path of this BuildRecord.
        :type build_yml_path: str
        """
        self._build_yml_path = build_yml_path

    @property
    def build_yml_url(self):
        r"""Gets the build_yml_url of this BuildRecord.

        yaml地址

        :return: The build_yml_url of this BuildRecord.
        :rtype: str
        """
        return self._build_yml_url

    @build_yml_url.setter
    def build_yml_url(self, build_yml_url):
        r"""Sets the build_yml_url of this BuildRecord.

        yaml地址

        :param build_yml_url: The build_yml_url of this BuildRecord.
        :type build_yml_url: str
        """
        self._build_yml_url = build_yml_url

    @property
    def daily_build_number(self):
        r"""Gets the daily_build_number of this BuildRecord.

        构建每日编号

        :return: The daily_build_number of this BuildRecord.
        :rtype: str
        """
        return self._daily_build_number

    @daily_build_number.setter
    def daily_build_number(self, daily_build_number):
        r"""Sets the daily_build_number of this BuildRecord.

        构建每日编号

        :param daily_build_number: The daily_build_number of this BuildRecord.
        :type daily_build_number: str
        """
        self._daily_build_number = daily_build_number

    @property
    def build_record_type(self):
        r"""Gets the build_record_type of this BuildRecord.

        :return: The build_record_type of this BuildRecord.
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.BuildRecordBuildRecordType`
        """
        return self._build_record_type

    @build_record_type.setter
    def build_record_type(self, build_record_type):
        r"""Sets the build_record_type of this BuildRecord.

        :param build_record_type: The build_record_type of this BuildRecord.
        :type build_record_type: :class:`huaweicloudsdkcodeartsbuild.v3.BuildRecordBuildRecordType`
        """
        self._build_record_type = build_record_type

    @property
    def trigger_type(self):
        r"""Gets the trigger_type of this BuildRecord.

        触发类型

        :return: The trigger_type of this BuildRecord.
        :rtype: str
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        r"""Sets the trigger_type of this BuildRecord.

        触发类型

        :param trigger_type: The trigger_type of this BuildRecord.
        :type trigger_type: str
        """
        self._trigger_type = trigger_type

    @property
    def scm_type(self):
        r"""Gets the scm_type of this BuildRecord.

        代码源类型

        :return: The scm_type of this BuildRecord.
        :rtype: str
        """
        return self._scm_type

    @scm_type.setter
    def scm_type(self, scm_type):
        r"""Sets the scm_type of this BuildRecord.

        代码源类型

        :param scm_type: The scm_type of this BuildRecord.
        :type scm_type: str
        """
        self._scm_type = scm_type

    @property
    def scm_web_url(self):
        r"""Gets the scm_web_url of this BuildRecord.

        代码源地址

        :return: The scm_web_url of this BuildRecord.
        :rtype: str
        """
        return self._scm_web_url

    @scm_web_url.setter
    def scm_web_url(self, scm_web_url):
        r"""Sets the scm_web_url of this BuildRecord.

        代码源地址

        :param scm_web_url: The scm_web_url of this BuildRecord.
        :type scm_web_url: str
        """
        self._scm_web_url = scm_web_url

    @property
    def user_id(self):
        r"""Gets the user_id of this BuildRecord.

        用户id

        :return: The user_id of this BuildRecord.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this BuildRecord.

        用户id

        :param user_id: The user_id of this BuildRecord.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def build_no(self):
        r"""Gets the build_no of this BuildRecord.

        构建编码

        :return: The build_no of this BuildRecord.
        :rtype: str
        """
        return self._build_no

    @build_no.setter
    def build_no(self, build_no):
        r"""Sets the build_no of this BuildRecord.

        构建编码

        :param build_no: The build_no of this BuildRecord.
        :type build_no: str
        """
        self._build_no = build_no

    @property
    def daily_build_no(self):
        r"""Gets the daily_build_no of this BuildRecord.

        构建每日编号

        :return: The daily_build_no of this BuildRecord.
        :rtype: str
        """
        return self._daily_build_no

    @daily_build_no.setter
    def daily_build_no(self, daily_build_no):
        r"""Sets the daily_build_no of this BuildRecord.

        构建每日编号

        :param daily_build_no: The daily_build_no of this BuildRecord.
        :type daily_build_no: str
        """
        self._daily_build_no = daily_build_no

    @property
    def dev_cloud_build_type(self):
        r"""Gets the dev_cloud_build_type of this BuildRecord.

        构建类型

        :return: The dev_cloud_build_type of this BuildRecord.
        :rtype: str
        """
        return self._dev_cloud_build_type

    @dev_cloud_build_type.setter
    def dev_cloud_build_type(self, dev_cloud_build_type):
        r"""Sets the dev_cloud_build_type of this BuildRecord.

        构建类型

        :param dev_cloud_build_type: The dev_cloud_build_type of this BuildRecord.
        :type dev_cloud_build_type: str
        """
        self._dev_cloud_build_type = dev_cloud_build_type

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
        if not isinstance(other, BuildRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
