# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppExecutionInfo:

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
        'name': 'str',
        'duration': 'str',
        'is_disable': 'bool',
        'project_id': 'str',
        'project_name': 'str',
        'is_care': 'bool',
        'can_modify': 'bool',
        'can_delete': 'bool',
        'can_view': 'bool',
        'can_execute': 'bool',
        'can_copy': 'bool',
        'can_manage': 'bool',
        'can_create_env': 'bool',
        'can_disable': 'bool',
        'deploy_system': 'str',
        'create_user_id': 'str',
        'create_tenant_id': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'execution_time': 'str',
        'end_time': 'str',
        'execution_state': 'str',
        'release_id': 'int',
        'executor_id': 'str',
        'executor_nick_name': 'str',
        'arrange_infos': 'list[TaskBaseResponseBody]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'duration': 'duration',
        'is_disable': 'is_disable',
        'project_id': 'project_id',
        'project_name': 'project_name',
        'is_care': 'is_care',
        'can_modify': 'can_modify',
        'can_delete': 'can_delete',
        'can_view': 'can_view',
        'can_execute': 'can_execute',
        'can_copy': 'can_copy',
        'can_manage': 'can_manage',
        'can_create_env': 'can_create_env',
        'can_disable': 'can_disable',
        'deploy_system': 'deploy_system',
        'create_user_id': 'create_user_id',
        'create_tenant_id': 'create_tenant_id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'execution_time': 'execution_time',
        'end_time': 'end_time',
        'execution_state': 'execution_state',
        'release_id': 'release_id',
        'executor_id': 'executor_id',
        'executor_nick_name': 'executor_nick_name',
        'arrange_infos': 'arrange_infos'
    }

    def __init__(self, id=None, name=None, duration=None, is_disable=None, project_id=None, project_name=None, is_care=None, can_modify=None, can_delete=None, can_view=None, can_execute=None, can_copy=None, can_manage=None, can_create_env=None, can_disable=None, deploy_system=None, create_user_id=None, create_tenant_id=None, create_time=None, update_time=None, execution_time=None, end_time=None, execution_state=None, release_id=None, executor_id=None, executor_nick_name=None, arrange_infos=None):
        """AppExecutionInfo

        The model defined in huaweicloud sdk

        :param id: 应用id
        :type id: str
        :param name: 应用名称
        :type name: str
        :param duration: 部署时间
        :type duration: str
        :param is_disable: 当前应用是否被禁用
        :type is_disable: bool
        :param project_id: 项目ID
        :type project_id: str
        :param project_name: 项目名称
        :type project_name: str
        :param is_care: 当前用户是否已收藏
        :type is_care: bool
        :param can_modify: 是否有编辑权限
        :type can_modify: bool
        :param can_delete: 是否有删除的权限
        :type can_delete: bool
        :param can_view: 是否有查看权限
        :type can_view: bool
        :param can_execute: 是否有部署权限
        :type can_execute: bool
        :param can_copy: 是否有复制权限
        :type can_copy: bool
        :param can_manage: 是否有编辑应用权限矩阵的权限
        :type can_manage: bool
        :param can_create_env: 是否有创建环境的权限
        :type can_create_env: bool
        :param can_disable: 是否有禁用应用的权限
        :type can_disable: bool
        :param deploy_system: 部署类型模式，包括deployTemplate、ansible、shell
        :type deploy_system: str
        :param create_user_id: 应用创建者用户ID
        :type create_user_id: str
        :param create_tenant_id: 应用创建者租户ID
        :type create_tenant_id: str
        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 修改时间
        :type update_time: str
        :param execution_time: 最后一次部署时间
        :type execution_time: str
        :param end_time: 部署结束时间
        :type end_time: str
        :param execution_state: 部署状态
        :type execution_state: str
        :param release_id: 部署记录序列号
        :type release_id: int
        :param executor_id: 部署者id
        :type executor_id: str
        :param executor_nick_name: 部署者名称
        :type executor_nick_name: str
        :param arrange_infos: 部署任务信息
        :type arrange_infos: list[:class:`huaweicloudsdkcodeartsdeploy.v2.TaskBaseResponseBody`]
        """
        
        

        self._id = None
        self._name = None
        self._duration = None
        self._is_disable = None
        self._project_id = None
        self._project_name = None
        self._is_care = None
        self._can_modify = None
        self._can_delete = None
        self._can_view = None
        self._can_execute = None
        self._can_copy = None
        self._can_manage = None
        self._can_create_env = None
        self._can_disable = None
        self._deploy_system = None
        self._create_user_id = None
        self._create_tenant_id = None
        self._create_time = None
        self._update_time = None
        self._execution_time = None
        self._end_time = None
        self._execution_state = None
        self._release_id = None
        self._executor_id = None
        self._executor_nick_name = None
        self._arrange_infos = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if duration is not None:
            self.duration = duration
        if is_disable is not None:
            self.is_disable = is_disable
        if project_id is not None:
            self.project_id = project_id
        if project_name is not None:
            self.project_name = project_name
        if is_care is not None:
            self.is_care = is_care
        if can_modify is not None:
            self.can_modify = can_modify
        if can_delete is not None:
            self.can_delete = can_delete
        if can_view is not None:
            self.can_view = can_view
        if can_execute is not None:
            self.can_execute = can_execute
        if can_copy is not None:
            self.can_copy = can_copy
        if can_manage is not None:
            self.can_manage = can_manage
        if can_create_env is not None:
            self.can_create_env = can_create_env
        if can_disable is not None:
            self.can_disable = can_disable
        if deploy_system is not None:
            self.deploy_system = deploy_system
        if create_user_id is not None:
            self.create_user_id = create_user_id
        if create_tenant_id is not None:
            self.create_tenant_id = create_tenant_id
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if execution_time is not None:
            self.execution_time = execution_time
        if end_time is not None:
            self.end_time = end_time
        if execution_state is not None:
            self.execution_state = execution_state
        if release_id is not None:
            self.release_id = release_id
        if executor_id is not None:
            self.executor_id = executor_id
        if executor_nick_name is not None:
            self.executor_nick_name = executor_nick_name
        if arrange_infos is not None:
            self.arrange_infos = arrange_infos

    @property
    def id(self):
        """Gets the id of this AppExecutionInfo.

        应用id

        :return: The id of this AppExecutionInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AppExecutionInfo.

        应用id

        :param id: The id of this AppExecutionInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this AppExecutionInfo.

        应用名称

        :return: The name of this AppExecutionInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AppExecutionInfo.

        应用名称

        :param name: The name of this AppExecutionInfo.
        :type name: str
        """
        self._name = name

    @property
    def duration(self):
        """Gets the duration of this AppExecutionInfo.

        部署时间

        :return: The duration of this AppExecutionInfo.
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this AppExecutionInfo.

        部署时间

        :param duration: The duration of this AppExecutionInfo.
        :type duration: str
        """
        self._duration = duration

    @property
    def is_disable(self):
        """Gets the is_disable of this AppExecutionInfo.

        当前应用是否被禁用

        :return: The is_disable of this AppExecutionInfo.
        :rtype: bool
        """
        return self._is_disable

    @is_disable.setter
    def is_disable(self, is_disable):
        """Sets the is_disable of this AppExecutionInfo.

        当前应用是否被禁用

        :param is_disable: The is_disable of this AppExecutionInfo.
        :type is_disable: bool
        """
        self._is_disable = is_disable

    @property
    def project_id(self):
        """Gets the project_id of this AppExecutionInfo.

        项目ID

        :return: The project_id of this AppExecutionInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this AppExecutionInfo.

        项目ID

        :param project_id: The project_id of this AppExecutionInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def project_name(self):
        """Gets the project_name of this AppExecutionInfo.

        项目名称

        :return: The project_name of this AppExecutionInfo.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this AppExecutionInfo.

        项目名称

        :param project_name: The project_name of this AppExecutionInfo.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def is_care(self):
        """Gets the is_care of this AppExecutionInfo.

        当前用户是否已收藏

        :return: The is_care of this AppExecutionInfo.
        :rtype: bool
        """
        return self._is_care

    @is_care.setter
    def is_care(self, is_care):
        """Sets the is_care of this AppExecutionInfo.

        当前用户是否已收藏

        :param is_care: The is_care of this AppExecutionInfo.
        :type is_care: bool
        """
        self._is_care = is_care

    @property
    def can_modify(self):
        """Gets the can_modify of this AppExecutionInfo.

        是否有编辑权限

        :return: The can_modify of this AppExecutionInfo.
        :rtype: bool
        """
        return self._can_modify

    @can_modify.setter
    def can_modify(self, can_modify):
        """Sets the can_modify of this AppExecutionInfo.

        是否有编辑权限

        :param can_modify: The can_modify of this AppExecutionInfo.
        :type can_modify: bool
        """
        self._can_modify = can_modify

    @property
    def can_delete(self):
        """Gets the can_delete of this AppExecutionInfo.

        是否有删除的权限

        :return: The can_delete of this AppExecutionInfo.
        :rtype: bool
        """
        return self._can_delete

    @can_delete.setter
    def can_delete(self, can_delete):
        """Sets the can_delete of this AppExecutionInfo.

        是否有删除的权限

        :param can_delete: The can_delete of this AppExecutionInfo.
        :type can_delete: bool
        """
        self._can_delete = can_delete

    @property
    def can_view(self):
        """Gets the can_view of this AppExecutionInfo.

        是否有查看权限

        :return: The can_view of this AppExecutionInfo.
        :rtype: bool
        """
        return self._can_view

    @can_view.setter
    def can_view(self, can_view):
        """Sets the can_view of this AppExecutionInfo.

        是否有查看权限

        :param can_view: The can_view of this AppExecutionInfo.
        :type can_view: bool
        """
        self._can_view = can_view

    @property
    def can_execute(self):
        """Gets the can_execute of this AppExecutionInfo.

        是否有部署权限

        :return: The can_execute of this AppExecutionInfo.
        :rtype: bool
        """
        return self._can_execute

    @can_execute.setter
    def can_execute(self, can_execute):
        """Sets the can_execute of this AppExecutionInfo.

        是否有部署权限

        :param can_execute: The can_execute of this AppExecutionInfo.
        :type can_execute: bool
        """
        self._can_execute = can_execute

    @property
    def can_copy(self):
        """Gets the can_copy of this AppExecutionInfo.

        是否有复制权限

        :return: The can_copy of this AppExecutionInfo.
        :rtype: bool
        """
        return self._can_copy

    @can_copy.setter
    def can_copy(self, can_copy):
        """Sets the can_copy of this AppExecutionInfo.

        是否有复制权限

        :param can_copy: The can_copy of this AppExecutionInfo.
        :type can_copy: bool
        """
        self._can_copy = can_copy

    @property
    def can_manage(self):
        """Gets the can_manage of this AppExecutionInfo.

        是否有编辑应用权限矩阵的权限

        :return: The can_manage of this AppExecutionInfo.
        :rtype: bool
        """
        return self._can_manage

    @can_manage.setter
    def can_manage(self, can_manage):
        """Sets the can_manage of this AppExecutionInfo.

        是否有编辑应用权限矩阵的权限

        :param can_manage: The can_manage of this AppExecutionInfo.
        :type can_manage: bool
        """
        self._can_manage = can_manage

    @property
    def can_create_env(self):
        """Gets the can_create_env of this AppExecutionInfo.

        是否有创建环境的权限

        :return: The can_create_env of this AppExecutionInfo.
        :rtype: bool
        """
        return self._can_create_env

    @can_create_env.setter
    def can_create_env(self, can_create_env):
        """Sets the can_create_env of this AppExecutionInfo.

        是否有创建环境的权限

        :param can_create_env: The can_create_env of this AppExecutionInfo.
        :type can_create_env: bool
        """
        self._can_create_env = can_create_env

    @property
    def can_disable(self):
        """Gets the can_disable of this AppExecutionInfo.

        是否有禁用应用的权限

        :return: The can_disable of this AppExecutionInfo.
        :rtype: bool
        """
        return self._can_disable

    @can_disable.setter
    def can_disable(self, can_disable):
        """Sets the can_disable of this AppExecutionInfo.

        是否有禁用应用的权限

        :param can_disable: The can_disable of this AppExecutionInfo.
        :type can_disable: bool
        """
        self._can_disable = can_disable

    @property
    def deploy_system(self):
        """Gets the deploy_system of this AppExecutionInfo.

        部署类型模式，包括deployTemplate、ansible、shell

        :return: The deploy_system of this AppExecutionInfo.
        :rtype: str
        """
        return self._deploy_system

    @deploy_system.setter
    def deploy_system(self, deploy_system):
        """Sets the deploy_system of this AppExecutionInfo.

        部署类型模式，包括deployTemplate、ansible、shell

        :param deploy_system: The deploy_system of this AppExecutionInfo.
        :type deploy_system: str
        """
        self._deploy_system = deploy_system

    @property
    def create_user_id(self):
        """Gets the create_user_id of this AppExecutionInfo.

        应用创建者用户ID

        :return: The create_user_id of this AppExecutionInfo.
        :rtype: str
        """
        return self._create_user_id

    @create_user_id.setter
    def create_user_id(self, create_user_id):
        """Sets the create_user_id of this AppExecutionInfo.

        应用创建者用户ID

        :param create_user_id: The create_user_id of this AppExecutionInfo.
        :type create_user_id: str
        """
        self._create_user_id = create_user_id

    @property
    def create_tenant_id(self):
        """Gets the create_tenant_id of this AppExecutionInfo.

        应用创建者租户ID

        :return: The create_tenant_id of this AppExecutionInfo.
        :rtype: str
        """
        return self._create_tenant_id

    @create_tenant_id.setter
    def create_tenant_id(self, create_tenant_id):
        """Sets the create_tenant_id of this AppExecutionInfo.

        应用创建者租户ID

        :param create_tenant_id: The create_tenant_id of this AppExecutionInfo.
        :type create_tenant_id: str
        """
        self._create_tenant_id = create_tenant_id

    @property
    def create_time(self):
        """Gets the create_time of this AppExecutionInfo.

        创建时间

        :return: The create_time of this AppExecutionInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this AppExecutionInfo.

        创建时间

        :param create_time: The create_time of this AppExecutionInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this AppExecutionInfo.

        修改时间

        :return: The update_time of this AppExecutionInfo.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this AppExecutionInfo.

        修改时间

        :param update_time: The update_time of this AppExecutionInfo.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def execution_time(self):
        """Gets the execution_time of this AppExecutionInfo.

        最后一次部署时间

        :return: The execution_time of this AppExecutionInfo.
        :rtype: str
        """
        return self._execution_time

    @execution_time.setter
    def execution_time(self, execution_time):
        """Sets the execution_time of this AppExecutionInfo.

        最后一次部署时间

        :param execution_time: The execution_time of this AppExecutionInfo.
        :type execution_time: str
        """
        self._execution_time = execution_time

    @property
    def end_time(self):
        """Gets the end_time of this AppExecutionInfo.

        部署结束时间

        :return: The end_time of this AppExecutionInfo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this AppExecutionInfo.

        部署结束时间

        :param end_time: The end_time of this AppExecutionInfo.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def execution_state(self):
        """Gets the execution_state of this AppExecutionInfo.

        部署状态

        :return: The execution_state of this AppExecutionInfo.
        :rtype: str
        """
        return self._execution_state

    @execution_state.setter
    def execution_state(self, execution_state):
        """Sets the execution_state of this AppExecutionInfo.

        部署状态

        :param execution_state: The execution_state of this AppExecutionInfo.
        :type execution_state: str
        """
        self._execution_state = execution_state

    @property
    def release_id(self):
        """Gets the release_id of this AppExecutionInfo.

        部署记录序列号

        :return: The release_id of this AppExecutionInfo.
        :rtype: int
        """
        return self._release_id

    @release_id.setter
    def release_id(self, release_id):
        """Sets the release_id of this AppExecutionInfo.

        部署记录序列号

        :param release_id: The release_id of this AppExecutionInfo.
        :type release_id: int
        """
        self._release_id = release_id

    @property
    def executor_id(self):
        """Gets the executor_id of this AppExecutionInfo.

        部署者id

        :return: The executor_id of this AppExecutionInfo.
        :rtype: str
        """
        return self._executor_id

    @executor_id.setter
    def executor_id(self, executor_id):
        """Sets the executor_id of this AppExecutionInfo.

        部署者id

        :param executor_id: The executor_id of this AppExecutionInfo.
        :type executor_id: str
        """
        self._executor_id = executor_id

    @property
    def executor_nick_name(self):
        """Gets the executor_nick_name of this AppExecutionInfo.

        部署者名称

        :return: The executor_nick_name of this AppExecutionInfo.
        :rtype: str
        """
        return self._executor_nick_name

    @executor_nick_name.setter
    def executor_nick_name(self, executor_nick_name):
        """Sets the executor_nick_name of this AppExecutionInfo.

        部署者名称

        :param executor_nick_name: The executor_nick_name of this AppExecutionInfo.
        :type executor_nick_name: str
        """
        self._executor_nick_name = executor_nick_name

    @property
    def arrange_infos(self):
        """Gets the arrange_infos of this AppExecutionInfo.

        部署任务信息

        :return: The arrange_infos of this AppExecutionInfo.
        :rtype: list[:class:`huaweicloudsdkcodeartsdeploy.v2.TaskBaseResponseBody`]
        """
        return self._arrange_infos

    @arrange_infos.setter
    def arrange_infos(self, arrange_infos):
        """Sets the arrange_infos of this AppExecutionInfo.

        部署任务信息

        :param arrange_infos: The arrange_infos of this AppExecutionInfo.
        :type arrange_infos: list[:class:`huaweicloudsdkcodeartsdeploy.v2.TaskBaseResponseBody`]
        """
        self._arrange_infos = arrange_infos

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
        if not isinstance(other, AppExecutionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
