# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJobInfoResult:

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
        'project_id': 'str',
        'project_permission_switch': 'bool',
        'build_time': 'str',
        'charge_time': 'str',
        'create_time': 'int',
        'disabled': 'bool',
        'favorite': 'bool',
        'source_code': 'str',
        'running_status': 'str',
        'new_build': 'bool',
        'job_name': 'str',
        'is_copy': 'bool',
        'is_delete': 'bool',
        'is_execute': 'bool',
        'is_forbidden': 'bool',
        'is_manager': 'bool',
        'is_modify': 'bool',
        'is_view': 'bool',
        'last_build_status': 'str',
        'last_build_time': 'int',
        'health_score': 'int'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'project_id',
        'project_permission_switch': 'project_permission_switch',
        'build_time': 'build_time',
        'charge_time': 'charge_time',
        'create_time': 'create_time',
        'disabled': 'disabled',
        'favorite': 'favorite',
        'source_code': 'source_code',
        'running_status': 'running_status',
        'new_build': 'new_build',
        'job_name': 'job_name',
        'is_copy': 'is_copy',
        'is_delete': 'is_delete',
        'is_execute': 'is_execute',
        'is_forbidden': 'is_forbidden',
        'is_manager': 'is_manager',
        'is_modify': 'is_modify',
        'is_view': 'is_view',
        'last_build_status': 'last_build_status',
        'last_build_time': 'last_build_time',
        'health_score': 'health_score'
    }

    def __init__(self, id=None, project_id=None, project_permission_switch=None, build_time=None, charge_time=None, create_time=None, disabled=None, favorite=None, source_code=None, running_status=None, new_build=None, job_name=None, is_copy=None, is_delete=None, is_execute=None, is_forbidden=None, is_manager=None, is_modify=None, is_view=None, last_build_status=None, last_build_time=None, health_score=None):
        r"""ShowJobInfoResult

        The model defined in huaweicloud sdk

        :param id: 构建任务ID
        :type id: str
        :param project_id: 构建工程ID,唯一对应codeci_job_id
        :type project_id: str
        :param project_permission_switch: 使用项目权限
        :type project_permission_switch: bool
        :param build_time: 执行时间
        :type build_time: str
        :param charge_time: 收费时间
        :type charge_time: str
        :param create_time: 任务创建时间
        :type create_time: int
        :param disabled: 是否已禁用
        :type disabled: bool
        :param favorite: 是否已收藏
        :type favorite: bool
        :param source_code: 代码来源
        :type source_code: str
        :param running_status: 运行状态
        :type running_status: str
        :param new_build: 重新运行
        :type new_build: bool
        :param job_name: 任务名称
        :type job_name: str
        :param is_copy: 是否有复制任务权限
        :type is_copy: bool
        :param is_delete: 是否有删除任务权限
        :type is_delete: bool
        :param is_execute: 是否有执行任务权限
        :type is_execute: bool
        :param is_forbidden: 是否有禁用任务权限
        :type is_forbidden: bool
        :param is_manager: 是否有管理任务权限
        :type is_manager: bool
        :param is_modify: 是否有修改任务权限
        :type is_modify: bool
        :param is_view: 是否有查看任务权限
        :type is_view: bool
        :param last_build_status: 最终构建状态
        :type last_build_status: str
        :param last_build_time: 最后构建时间
        :type last_build_time: int
        :param health_score: 健康度
        :type health_score: int
        """
        
        

        self._id = None
        self._project_id = None
        self._project_permission_switch = None
        self._build_time = None
        self._charge_time = None
        self._create_time = None
        self._disabled = None
        self._favorite = None
        self._source_code = None
        self._running_status = None
        self._new_build = None
        self._job_name = None
        self._is_copy = None
        self._is_delete = None
        self._is_execute = None
        self._is_forbidden = None
        self._is_manager = None
        self._is_modify = None
        self._is_view = None
        self._last_build_status = None
        self._last_build_time = None
        self._health_score = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if project_id is not None:
            self.project_id = project_id
        if project_permission_switch is not None:
            self.project_permission_switch = project_permission_switch
        if build_time is not None:
            self.build_time = build_time
        if charge_time is not None:
            self.charge_time = charge_time
        if create_time is not None:
            self.create_time = create_time
        if disabled is not None:
            self.disabled = disabled
        if favorite is not None:
            self.favorite = favorite
        if source_code is not None:
            self.source_code = source_code
        if running_status is not None:
            self.running_status = running_status
        if new_build is not None:
            self.new_build = new_build
        if job_name is not None:
            self.job_name = job_name
        if is_copy is not None:
            self.is_copy = is_copy
        if is_delete is not None:
            self.is_delete = is_delete
        if is_execute is not None:
            self.is_execute = is_execute
        if is_forbidden is not None:
            self.is_forbidden = is_forbidden
        if is_manager is not None:
            self.is_manager = is_manager
        if is_modify is not None:
            self.is_modify = is_modify
        if is_view is not None:
            self.is_view = is_view
        if last_build_status is not None:
            self.last_build_status = last_build_status
        if last_build_time is not None:
            self.last_build_time = last_build_time
        if health_score is not None:
            self.health_score = health_score

    @property
    def id(self):
        r"""Gets the id of this ShowJobInfoResult.

        构建任务ID

        :return: The id of this ShowJobInfoResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowJobInfoResult.

        构建任务ID

        :param id: The id of this ShowJobInfoResult.
        :type id: str
        """
        self._id = id

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowJobInfoResult.

        构建工程ID,唯一对应codeci_job_id

        :return: The project_id of this ShowJobInfoResult.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowJobInfoResult.

        构建工程ID,唯一对应codeci_job_id

        :param project_id: The project_id of this ShowJobInfoResult.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def project_permission_switch(self):
        r"""Gets the project_permission_switch of this ShowJobInfoResult.

        使用项目权限

        :return: The project_permission_switch of this ShowJobInfoResult.
        :rtype: bool
        """
        return self._project_permission_switch

    @project_permission_switch.setter
    def project_permission_switch(self, project_permission_switch):
        r"""Sets the project_permission_switch of this ShowJobInfoResult.

        使用项目权限

        :param project_permission_switch: The project_permission_switch of this ShowJobInfoResult.
        :type project_permission_switch: bool
        """
        self._project_permission_switch = project_permission_switch

    @property
    def build_time(self):
        r"""Gets the build_time of this ShowJobInfoResult.

        执行时间

        :return: The build_time of this ShowJobInfoResult.
        :rtype: str
        """
        return self._build_time

    @build_time.setter
    def build_time(self, build_time):
        r"""Sets the build_time of this ShowJobInfoResult.

        执行时间

        :param build_time: The build_time of this ShowJobInfoResult.
        :type build_time: str
        """
        self._build_time = build_time

    @property
    def charge_time(self):
        r"""Gets the charge_time of this ShowJobInfoResult.

        收费时间

        :return: The charge_time of this ShowJobInfoResult.
        :rtype: str
        """
        return self._charge_time

    @charge_time.setter
    def charge_time(self, charge_time):
        r"""Sets the charge_time of this ShowJobInfoResult.

        收费时间

        :param charge_time: The charge_time of this ShowJobInfoResult.
        :type charge_time: str
        """
        self._charge_time = charge_time

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowJobInfoResult.

        任务创建时间

        :return: The create_time of this ShowJobInfoResult.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowJobInfoResult.

        任务创建时间

        :param create_time: The create_time of this ShowJobInfoResult.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def disabled(self):
        r"""Gets the disabled of this ShowJobInfoResult.

        是否已禁用

        :return: The disabled of this ShowJobInfoResult.
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        r"""Sets the disabled of this ShowJobInfoResult.

        是否已禁用

        :param disabled: The disabled of this ShowJobInfoResult.
        :type disabled: bool
        """
        self._disabled = disabled

    @property
    def favorite(self):
        r"""Gets the favorite of this ShowJobInfoResult.

        是否已收藏

        :return: The favorite of this ShowJobInfoResult.
        :rtype: bool
        """
        return self._favorite

    @favorite.setter
    def favorite(self, favorite):
        r"""Sets the favorite of this ShowJobInfoResult.

        是否已收藏

        :param favorite: The favorite of this ShowJobInfoResult.
        :type favorite: bool
        """
        self._favorite = favorite

    @property
    def source_code(self):
        r"""Gets the source_code of this ShowJobInfoResult.

        代码来源

        :return: The source_code of this ShowJobInfoResult.
        :rtype: str
        """
        return self._source_code

    @source_code.setter
    def source_code(self, source_code):
        r"""Sets the source_code of this ShowJobInfoResult.

        代码来源

        :param source_code: The source_code of this ShowJobInfoResult.
        :type source_code: str
        """
        self._source_code = source_code

    @property
    def running_status(self):
        r"""Gets the running_status of this ShowJobInfoResult.

        运行状态

        :return: The running_status of this ShowJobInfoResult.
        :rtype: str
        """
        return self._running_status

    @running_status.setter
    def running_status(self, running_status):
        r"""Sets the running_status of this ShowJobInfoResult.

        运行状态

        :param running_status: The running_status of this ShowJobInfoResult.
        :type running_status: str
        """
        self._running_status = running_status

    @property
    def new_build(self):
        r"""Gets the new_build of this ShowJobInfoResult.

        重新运行

        :return: The new_build of this ShowJobInfoResult.
        :rtype: bool
        """
        return self._new_build

    @new_build.setter
    def new_build(self, new_build):
        r"""Sets the new_build of this ShowJobInfoResult.

        重新运行

        :param new_build: The new_build of this ShowJobInfoResult.
        :type new_build: bool
        """
        self._new_build = new_build

    @property
    def job_name(self):
        r"""Gets the job_name of this ShowJobInfoResult.

        任务名称

        :return: The job_name of this ShowJobInfoResult.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        r"""Sets the job_name of this ShowJobInfoResult.

        任务名称

        :param job_name: The job_name of this ShowJobInfoResult.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def is_copy(self):
        r"""Gets the is_copy of this ShowJobInfoResult.

        是否有复制任务权限

        :return: The is_copy of this ShowJobInfoResult.
        :rtype: bool
        """
        return self._is_copy

    @is_copy.setter
    def is_copy(self, is_copy):
        r"""Sets the is_copy of this ShowJobInfoResult.

        是否有复制任务权限

        :param is_copy: The is_copy of this ShowJobInfoResult.
        :type is_copy: bool
        """
        self._is_copy = is_copy

    @property
    def is_delete(self):
        r"""Gets the is_delete of this ShowJobInfoResult.

        是否有删除任务权限

        :return: The is_delete of this ShowJobInfoResult.
        :rtype: bool
        """
        return self._is_delete

    @is_delete.setter
    def is_delete(self, is_delete):
        r"""Sets the is_delete of this ShowJobInfoResult.

        是否有删除任务权限

        :param is_delete: The is_delete of this ShowJobInfoResult.
        :type is_delete: bool
        """
        self._is_delete = is_delete

    @property
    def is_execute(self):
        r"""Gets the is_execute of this ShowJobInfoResult.

        是否有执行任务权限

        :return: The is_execute of this ShowJobInfoResult.
        :rtype: bool
        """
        return self._is_execute

    @is_execute.setter
    def is_execute(self, is_execute):
        r"""Sets the is_execute of this ShowJobInfoResult.

        是否有执行任务权限

        :param is_execute: The is_execute of this ShowJobInfoResult.
        :type is_execute: bool
        """
        self._is_execute = is_execute

    @property
    def is_forbidden(self):
        r"""Gets the is_forbidden of this ShowJobInfoResult.

        是否有禁用任务权限

        :return: The is_forbidden of this ShowJobInfoResult.
        :rtype: bool
        """
        return self._is_forbidden

    @is_forbidden.setter
    def is_forbidden(self, is_forbidden):
        r"""Sets the is_forbidden of this ShowJobInfoResult.

        是否有禁用任务权限

        :param is_forbidden: The is_forbidden of this ShowJobInfoResult.
        :type is_forbidden: bool
        """
        self._is_forbidden = is_forbidden

    @property
    def is_manager(self):
        r"""Gets the is_manager of this ShowJobInfoResult.

        是否有管理任务权限

        :return: The is_manager of this ShowJobInfoResult.
        :rtype: bool
        """
        return self._is_manager

    @is_manager.setter
    def is_manager(self, is_manager):
        r"""Sets the is_manager of this ShowJobInfoResult.

        是否有管理任务权限

        :param is_manager: The is_manager of this ShowJobInfoResult.
        :type is_manager: bool
        """
        self._is_manager = is_manager

    @property
    def is_modify(self):
        r"""Gets the is_modify of this ShowJobInfoResult.

        是否有修改任务权限

        :return: The is_modify of this ShowJobInfoResult.
        :rtype: bool
        """
        return self._is_modify

    @is_modify.setter
    def is_modify(self, is_modify):
        r"""Sets the is_modify of this ShowJobInfoResult.

        是否有修改任务权限

        :param is_modify: The is_modify of this ShowJobInfoResult.
        :type is_modify: bool
        """
        self._is_modify = is_modify

    @property
    def is_view(self):
        r"""Gets the is_view of this ShowJobInfoResult.

        是否有查看任务权限

        :return: The is_view of this ShowJobInfoResult.
        :rtype: bool
        """
        return self._is_view

    @is_view.setter
    def is_view(self, is_view):
        r"""Sets the is_view of this ShowJobInfoResult.

        是否有查看任务权限

        :param is_view: The is_view of this ShowJobInfoResult.
        :type is_view: bool
        """
        self._is_view = is_view

    @property
    def last_build_status(self):
        r"""Gets the last_build_status of this ShowJobInfoResult.

        最终构建状态

        :return: The last_build_status of this ShowJobInfoResult.
        :rtype: str
        """
        return self._last_build_status

    @last_build_status.setter
    def last_build_status(self, last_build_status):
        r"""Sets the last_build_status of this ShowJobInfoResult.

        最终构建状态

        :param last_build_status: The last_build_status of this ShowJobInfoResult.
        :type last_build_status: str
        """
        self._last_build_status = last_build_status

    @property
    def last_build_time(self):
        r"""Gets the last_build_time of this ShowJobInfoResult.

        最后构建时间

        :return: The last_build_time of this ShowJobInfoResult.
        :rtype: int
        """
        return self._last_build_time

    @last_build_time.setter
    def last_build_time(self, last_build_time):
        r"""Sets the last_build_time of this ShowJobInfoResult.

        最后构建时间

        :param last_build_time: The last_build_time of this ShowJobInfoResult.
        :type last_build_time: int
        """
        self._last_build_time = last_build_time

    @property
    def health_score(self):
        r"""Gets the health_score of this ShowJobInfoResult.

        健康度

        :return: The health_score of this ShowJobInfoResult.
        :rtype: int
        """
        return self._health_score

    @health_score.setter
    def health_score(self, health_score):
        r"""Sets the health_score of this ShowJobInfoResult.

        健康度

        :param health_score: The health_score of this ShowJobInfoResult.
        :type health_score: int
        """
        self._health_score = health_score

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
        if not isinstance(other, ShowJobInfoResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
