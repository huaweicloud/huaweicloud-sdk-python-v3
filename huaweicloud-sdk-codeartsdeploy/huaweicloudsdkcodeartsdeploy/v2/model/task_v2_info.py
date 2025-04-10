# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskV2Info:

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
        'state': 'str',
        'description': 'str',
        'owner': 'str',
        'steps': 'dict(str, Step)',
        'project_id': 'str',
        'project_name': 'str',
        'deploy_system': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'role_id': 'int',
        'is_defaut_permission': 'bool',
        'template_id': 'str',
        'nick_name': 'str',
        'owner_id': 'str',
        'tenant_id': 'str',
        'tenant_name': 'str',
        'slave_cluster_id': 'str',
        'is_care': 'bool',
        'can_modify': 'bool',
        'can_delete': 'bool',
        'can_view': 'bool',
        'can_execute': 'bool',
        'can_copy': 'bool',
        'can_manage': 'bool',
        'can_create_env': 'bool',
        'can_disable': 'bool',
        'app_component_list': 'list[AppComponentDao]',
        'release_id': 'int',
        'app_id': 'str',
        'is_disable': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'state': 'state',
        'description': 'description',
        'owner': 'owner',
        'steps': 'steps',
        'project_id': 'project_id',
        'project_name': 'project_name',
        'deploy_system': 'deploy_system',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'role_id': 'role_id',
        'is_defaut_permission': 'is_defaut_permission',
        'template_id': 'template_id',
        'nick_name': 'nick_name',
        'owner_id': 'owner_id',
        'tenant_id': 'tenant_id',
        'tenant_name': 'tenant_name',
        'slave_cluster_id': 'slave_cluster_id',
        'is_care': 'is_care',
        'can_modify': 'can_modify',
        'can_delete': 'can_delete',
        'can_view': 'can_view',
        'can_execute': 'can_execute',
        'can_copy': 'can_copy',
        'can_manage': 'can_manage',
        'can_create_env': 'can_create_env',
        'can_disable': 'can_disable',
        'app_component_list': 'app_component_list',
        'release_id': 'release_id',
        'app_id': 'app_id',
        'is_disable': 'is_disable'
    }

    def __init__(self, id=None, name=None, state=None, description=None, owner=None, steps=None, project_id=None, project_name=None, deploy_system=None, create_time=None, update_time=None, role_id=None, is_defaut_permission=None, template_id=None, nick_name=None, owner_id=None, tenant_id=None, tenant_name=None, slave_cluster_id=None, is_care=None, can_modify=None, can_delete=None, can_view=None, can_execute=None, can_copy=None, can_manage=None, can_create_env=None, can_disable=None, app_component_list=None, release_id=None, app_id=None, is_disable=None):
        r"""TaskV2Info

        The model defined in huaweicloud sdk

        :param id: 部署任务id
        :type id: str
        :param name: 部署任务名称
        :type name: str
        :param state: 部署任务状态
        :type state: str
        :param description: 描述
        :type description: str
        :param owner: 部署任务所属人
        :type owner: str
        :param steps: 部署步骤
        :type steps: dict(str, Step)
        :param project_id: 项目id
        :type project_id: str
        :param project_name: 项目名称
        :type project_name: str
        :param deploy_system: 部署类型模式，包括deployTemplate、ansible、shell
        :type deploy_system: str
        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 修改时间
        :type update_time: str
        :param role_id: 角色id
        :type role_id: int
        :param is_defaut_permission: 是否为默认角色
        :type is_defaut_permission: bool
        :param template_id: 模板id
        :type template_id: str
        :param nick_name: 应用创建者昵称
        :type nick_name: str
        :param owner_id: 应用创建者用户id
        :type owner_id: str
        :param tenant_id: 应用创建者租户id
        :type tenant_id: str
        :param tenant_name: 应用创建者租户名
        :type tenant_name: str
        :param slave_cluster_id: slave集群id，默认为null时使用默认slave集群，用户自定义slave时为slave集群id
        :type slave_cluster_id: str
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
        :param app_component_list: 应用组件列表
        :type app_component_list: list[:class:`huaweicloudsdkcodeartsdeploy.v2.AppComponentDao`]
        :param release_id: 部署记录序列号
        :type release_id: int
        :param app_id: 部署任务所属应用id
        :type app_id: str
        :param is_disable: 当前应用是否被禁用
        :type is_disable: bool
        """
        
        

        self._id = None
        self._name = None
        self._state = None
        self._description = None
        self._owner = None
        self._steps = None
        self._project_id = None
        self._project_name = None
        self._deploy_system = None
        self._create_time = None
        self._update_time = None
        self._role_id = None
        self._is_defaut_permission = None
        self._template_id = None
        self._nick_name = None
        self._owner_id = None
        self._tenant_id = None
        self._tenant_name = None
        self._slave_cluster_id = None
        self._is_care = None
        self._can_modify = None
        self._can_delete = None
        self._can_view = None
        self._can_execute = None
        self._can_copy = None
        self._can_manage = None
        self._can_create_env = None
        self._can_disable = None
        self._app_component_list = None
        self._release_id = None
        self._app_id = None
        self._is_disable = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if state is not None:
            self.state = state
        if description is not None:
            self.description = description
        if owner is not None:
            self.owner = owner
        if steps is not None:
            self.steps = steps
        if project_id is not None:
            self.project_id = project_id
        if project_name is not None:
            self.project_name = project_name
        if deploy_system is not None:
            self.deploy_system = deploy_system
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if role_id is not None:
            self.role_id = role_id
        if is_defaut_permission is not None:
            self.is_defaut_permission = is_defaut_permission
        if template_id is not None:
            self.template_id = template_id
        if nick_name is not None:
            self.nick_name = nick_name
        if owner_id is not None:
            self.owner_id = owner_id
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if tenant_name is not None:
            self.tenant_name = tenant_name
        if slave_cluster_id is not None:
            self.slave_cluster_id = slave_cluster_id
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
        if app_component_list is not None:
            self.app_component_list = app_component_list
        if release_id is not None:
            self.release_id = release_id
        if app_id is not None:
            self.app_id = app_id
        if is_disable is not None:
            self.is_disable = is_disable

    @property
    def id(self):
        r"""Gets the id of this TaskV2Info.

        部署任务id

        :return: The id of this TaskV2Info.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this TaskV2Info.

        部署任务id

        :param id: The id of this TaskV2Info.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this TaskV2Info.

        部署任务名称

        :return: The name of this TaskV2Info.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this TaskV2Info.

        部署任务名称

        :param name: The name of this TaskV2Info.
        :type name: str
        """
        self._name = name

    @property
    def state(self):
        r"""Gets the state of this TaskV2Info.

        部署任务状态

        :return: The state of this TaskV2Info.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this TaskV2Info.

        部署任务状态

        :param state: The state of this TaskV2Info.
        :type state: str
        """
        self._state = state

    @property
    def description(self):
        r"""Gets the description of this TaskV2Info.

        描述

        :return: The description of this TaskV2Info.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this TaskV2Info.

        描述

        :param description: The description of this TaskV2Info.
        :type description: str
        """
        self._description = description

    @property
    def owner(self):
        r"""Gets the owner of this TaskV2Info.

        部署任务所属人

        :return: The owner of this TaskV2Info.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this TaskV2Info.

        部署任务所属人

        :param owner: The owner of this TaskV2Info.
        :type owner: str
        """
        self._owner = owner

    @property
    def steps(self):
        r"""Gets the steps of this TaskV2Info.

        部署步骤

        :return: The steps of this TaskV2Info.
        :rtype: dict(str, Step)
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        r"""Sets the steps of this TaskV2Info.

        部署步骤

        :param steps: The steps of this TaskV2Info.
        :type steps: dict(str, Step)
        """
        self._steps = steps

    @property
    def project_id(self):
        r"""Gets the project_id of this TaskV2Info.

        项目id

        :return: The project_id of this TaskV2Info.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this TaskV2Info.

        项目id

        :param project_id: The project_id of this TaskV2Info.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def project_name(self):
        r"""Gets the project_name of this TaskV2Info.

        项目名称

        :return: The project_name of this TaskV2Info.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        r"""Sets the project_name of this TaskV2Info.

        项目名称

        :param project_name: The project_name of this TaskV2Info.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def deploy_system(self):
        r"""Gets the deploy_system of this TaskV2Info.

        部署类型模式，包括deployTemplate、ansible、shell

        :return: The deploy_system of this TaskV2Info.
        :rtype: str
        """
        return self._deploy_system

    @deploy_system.setter
    def deploy_system(self, deploy_system):
        r"""Sets the deploy_system of this TaskV2Info.

        部署类型模式，包括deployTemplate、ansible、shell

        :param deploy_system: The deploy_system of this TaskV2Info.
        :type deploy_system: str
        """
        self._deploy_system = deploy_system

    @property
    def create_time(self):
        r"""Gets the create_time of this TaskV2Info.

        创建时间

        :return: The create_time of this TaskV2Info.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this TaskV2Info.

        创建时间

        :param create_time: The create_time of this TaskV2Info.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this TaskV2Info.

        修改时间

        :return: The update_time of this TaskV2Info.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this TaskV2Info.

        修改时间

        :param update_time: The update_time of this TaskV2Info.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def role_id(self):
        r"""Gets the role_id of this TaskV2Info.

        角色id

        :return: The role_id of this TaskV2Info.
        :rtype: int
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        r"""Sets the role_id of this TaskV2Info.

        角色id

        :param role_id: The role_id of this TaskV2Info.
        :type role_id: int
        """
        self._role_id = role_id

    @property
    def is_defaut_permission(self):
        r"""Gets the is_defaut_permission of this TaskV2Info.

        是否为默认角色

        :return: The is_defaut_permission of this TaskV2Info.
        :rtype: bool
        """
        return self._is_defaut_permission

    @is_defaut_permission.setter
    def is_defaut_permission(self, is_defaut_permission):
        r"""Sets the is_defaut_permission of this TaskV2Info.

        是否为默认角色

        :param is_defaut_permission: The is_defaut_permission of this TaskV2Info.
        :type is_defaut_permission: bool
        """
        self._is_defaut_permission = is_defaut_permission

    @property
    def template_id(self):
        r"""Gets the template_id of this TaskV2Info.

        模板id

        :return: The template_id of this TaskV2Info.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this TaskV2Info.

        模板id

        :param template_id: The template_id of this TaskV2Info.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def nick_name(self):
        r"""Gets the nick_name of this TaskV2Info.

        应用创建者昵称

        :return: The nick_name of this TaskV2Info.
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        r"""Sets the nick_name of this TaskV2Info.

        应用创建者昵称

        :param nick_name: The nick_name of this TaskV2Info.
        :type nick_name: str
        """
        self._nick_name = nick_name

    @property
    def owner_id(self):
        r"""Gets the owner_id of this TaskV2Info.

        应用创建者用户id

        :return: The owner_id of this TaskV2Info.
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        r"""Sets the owner_id of this TaskV2Info.

        应用创建者用户id

        :param owner_id: The owner_id of this TaskV2Info.
        :type owner_id: str
        """
        self._owner_id = owner_id

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this TaskV2Info.

        应用创建者租户id

        :return: The tenant_id of this TaskV2Info.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this TaskV2Info.

        应用创建者租户id

        :param tenant_id: The tenant_id of this TaskV2Info.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def tenant_name(self):
        r"""Gets the tenant_name of this TaskV2Info.

        应用创建者租户名

        :return: The tenant_name of this TaskV2Info.
        :rtype: str
        """
        return self._tenant_name

    @tenant_name.setter
    def tenant_name(self, tenant_name):
        r"""Sets the tenant_name of this TaskV2Info.

        应用创建者租户名

        :param tenant_name: The tenant_name of this TaskV2Info.
        :type tenant_name: str
        """
        self._tenant_name = tenant_name

    @property
    def slave_cluster_id(self):
        r"""Gets the slave_cluster_id of this TaskV2Info.

        slave集群id，默认为null时使用默认slave集群，用户自定义slave时为slave集群id

        :return: The slave_cluster_id of this TaskV2Info.
        :rtype: str
        """
        return self._slave_cluster_id

    @slave_cluster_id.setter
    def slave_cluster_id(self, slave_cluster_id):
        r"""Sets the slave_cluster_id of this TaskV2Info.

        slave集群id，默认为null时使用默认slave集群，用户自定义slave时为slave集群id

        :param slave_cluster_id: The slave_cluster_id of this TaskV2Info.
        :type slave_cluster_id: str
        """
        self._slave_cluster_id = slave_cluster_id

    @property
    def is_care(self):
        r"""Gets the is_care of this TaskV2Info.

        当前用户是否已收藏

        :return: The is_care of this TaskV2Info.
        :rtype: bool
        """
        return self._is_care

    @is_care.setter
    def is_care(self, is_care):
        r"""Sets the is_care of this TaskV2Info.

        当前用户是否已收藏

        :param is_care: The is_care of this TaskV2Info.
        :type is_care: bool
        """
        self._is_care = is_care

    @property
    def can_modify(self):
        r"""Gets the can_modify of this TaskV2Info.

        是否有编辑权限

        :return: The can_modify of this TaskV2Info.
        :rtype: bool
        """
        return self._can_modify

    @can_modify.setter
    def can_modify(self, can_modify):
        r"""Sets the can_modify of this TaskV2Info.

        是否有编辑权限

        :param can_modify: The can_modify of this TaskV2Info.
        :type can_modify: bool
        """
        self._can_modify = can_modify

    @property
    def can_delete(self):
        r"""Gets the can_delete of this TaskV2Info.

        是否有删除的权限

        :return: The can_delete of this TaskV2Info.
        :rtype: bool
        """
        return self._can_delete

    @can_delete.setter
    def can_delete(self, can_delete):
        r"""Sets the can_delete of this TaskV2Info.

        是否有删除的权限

        :param can_delete: The can_delete of this TaskV2Info.
        :type can_delete: bool
        """
        self._can_delete = can_delete

    @property
    def can_view(self):
        r"""Gets the can_view of this TaskV2Info.

        是否有查看权限

        :return: The can_view of this TaskV2Info.
        :rtype: bool
        """
        return self._can_view

    @can_view.setter
    def can_view(self, can_view):
        r"""Sets the can_view of this TaskV2Info.

        是否有查看权限

        :param can_view: The can_view of this TaskV2Info.
        :type can_view: bool
        """
        self._can_view = can_view

    @property
    def can_execute(self):
        r"""Gets the can_execute of this TaskV2Info.

        是否有部署权限

        :return: The can_execute of this TaskV2Info.
        :rtype: bool
        """
        return self._can_execute

    @can_execute.setter
    def can_execute(self, can_execute):
        r"""Sets the can_execute of this TaskV2Info.

        是否有部署权限

        :param can_execute: The can_execute of this TaskV2Info.
        :type can_execute: bool
        """
        self._can_execute = can_execute

    @property
    def can_copy(self):
        r"""Gets the can_copy of this TaskV2Info.

        是否有复制权限

        :return: The can_copy of this TaskV2Info.
        :rtype: bool
        """
        return self._can_copy

    @can_copy.setter
    def can_copy(self, can_copy):
        r"""Sets the can_copy of this TaskV2Info.

        是否有复制权限

        :param can_copy: The can_copy of this TaskV2Info.
        :type can_copy: bool
        """
        self._can_copy = can_copy

    @property
    def can_manage(self):
        r"""Gets the can_manage of this TaskV2Info.

        是否有编辑应用权限矩阵的权限

        :return: The can_manage of this TaskV2Info.
        :rtype: bool
        """
        return self._can_manage

    @can_manage.setter
    def can_manage(self, can_manage):
        r"""Sets the can_manage of this TaskV2Info.

        是否有编辑应用权限矩阵的权限

        :param can_manage: The can_manage of this TaskV2Info.
        :type can_manage: bool
        """
        self._can_manage = can_manage

    @property
    def can_create_env(self):
        r"""Gets the can_create_env of this TaskV2Info.

        是否有创建环境的权限

        :return: The can_create_env of this TaskV2Info.
        :rtype: bool
        """
        return self._can_create_env

    @can_create_env.setter
    def can_create_env(self, can_create_env):
        r"""Sets the can_create_env of this TaskV2Info.

        是否有创建环境的权限

        :param can_create_env: The can_create_env of this TaskV2Info.
        :type can_create_env: bool
        """
        self._can_create_env = can_create_env

    @property
    def can_disable(self):
        r"""Gets the can_disable of this TaskV2Info.

        是否有禁用应用的权限

        :return: The can_disable of this TaskV2Info.
        :rtype: bool
        """
        return self._can_disable

    @can_disable.setter
    def can_disable(self, can_disable):
        r"""Sets the can_disable of this TaskV2Info.

        是否有禁用应用的权限

        :param can_disable: The can_disable of this TaskV2Info.
        :type can_disable: bool
        """
        self._can_disable = can_disable

    @property
    def app_component_list(self):
        r"""Gets the app_component_list of this TaskV2Info.

        应用组件列表

        :return: The app_component_list of this TaskV2Info.
        :rtype: list[:class:`huaweicloudsdkcodeartsdeploy.v2.AppComponentDao`]
        """
        return self._app_component_list

    @app_component_list.setter
    def app_component_list(self, app_component_list):
        r"""Sets the app_component_list of this TaskV2Info.

        应用组件列表

        :param app_component_list: The app_component_list of this TaskV2Info.
        :type app_component_list: list[:class:`huaweicloudsdkcodeartsdeploy.v2.AppComponentDao`]
        """
        self._app_component_list = app_component_list

    @property
    def release_id(self):
        r"""Gets the release_id of this TaskV2Info.

        部署记录序列号

        :return: The release_id of this TaskV2Info.
        :rtype: int
        """
        return self._release_id

    @release_id.setter
    def release_id(self, release_id):
        r"""Sets the release_id of this TaskV2Info.

        部署记录序列号

        :param release_id: The release_id of this TaskV2Info.
        :type release_id: int
        """
        self._release_id = release_id

    @property
    def app_id(self):
        r"""Gets the app_id of this TaskV2Info.

        部署任务所属应用id

        :return: The app_id of this TaskV2Info.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this TaskV2Info.

        部署任务所属应用id

        :param app_id: The app_id of this TaskV2Info.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def is_disable(self):
        r"""Gets the is_disable of this TaskV2Info.

        当前应用是否被禁用

        :return: The is_disable of this TaskV2Info.
        :rtype: bool
        """
        return self._is_disable

    @is_disable.setter
    def is_disable(self, is_disable):
        r"""Sets the is_disable of this TaskV2Info.

        当前应用是否被禁用

        :param is_disable: The is_disable of this TaskV2Info.
        :type is_disable: bool
        """
        self._is_disable = is_disable

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
        if not isinstance(other, TaskV2Info):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
