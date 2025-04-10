# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppDetailInfo:

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
        'region': 'str',
        'description': 'str',
        'is_disable': 'bool',
        'create_type': 'str',
        'project_id': 'str',
        'project_name': 'str',
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
        'owner_tenant_id': 'str',
        'create_user_id': 'str',
        'create_tenant_id': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'permission_level': 'str',
        'arrange_infos': 'list[TaskV2Info]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'region': 'region',
        'description': 'description',
        'is_disable': 'is_disable',
        'create_type': 'create_type',
        'project_id': 'project_id',
        'project_name': 'project_name',
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
        'owner_tenant_id': 'owner_tenant_id',
        'create_user_id': 'create_user_id',
        'create_tenant_id': 'create_tenant_id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'permission_level': 'permission_level',
        'arrange_infos': 'arrange_infos'
    }

    def __init__(self, id=None, name=None, region=None, description=None, is_disable=None, create_type=None, project_id=None, project_name=None, slave_cluster_id=None, is_care=None, can_modify=None, can_delete=None, can_view=None, can_execute=None, can_copy=None, can_manage=None, can_create_env=None, can_disable=None, owner_tenant_id=None, create_user_id=None, create_tenant_id=None, create_time=None, update_time=None, permission_level=None, arrange_infos=None):
        r"""AppDetailInfo

        The model defined in huaweicloud sdk

        :param id: 应用id
        :type id: str
        :param name: 应用名称
        :type name: str
        :param region: 应用所属区域
        :type region: str
        :param description: 描述
        :type description: str
        :param is_disable: 当前应用是否被禁用
        :type is_disable: bool
        :param create_type: 创建方式
        :type create_type: str
        :param project_id: 项目id
        :type project_id: str
        :param project_name: 项目名称
        :type project_name: str
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
        :param owner_tenant_id: 应用所属人租户id
        :type owner_tenant_id: str
        :param create_user_id: 应用创建者用户名
        :type create_user_id: str
        :param create_tenant_id: 应用创建人租户id
        :type create_tenant_id: str
        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 修改时间
        :type update_time: str
        :param permission_level: 权限等级
        :type permission_level: str
        :param arrange_infos: 部署任务信息
        :type arrange_infos: list[:class:`huaweicloudsdkcodeartsdeploy.v2.TaskV2Info`]
        """
        
        

        self._id = None
        self._name = None
        self._region = None
        self._description = None
        self._is_disable = None
        self._create_type = None
        self._project_id = None
        self._project_name = None
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
        self._owner_tenant_id = None
        self._create_user_id = None
        self._create_tenant_id = None
        self._create_time = None
        self._update_time = None
        self._permission_level = None
        self._arrange_infos = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if region is not None:
            self.region = region
        if description is not None:
            self.description = description
        if is_disable is not None:
            self.is_disable = is_disable
        if create_type is not None:
            self.create_type = create_type
        if project_id is not None:
            self.project_id = project_id
        if project_name is not None:
            self.project_name = project_name
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
        if owner_tenant_id is not None:
            self.owner_tenant_id = owner_tenant_id
        if create_user_id is not None:
            self.create_user_id = create_user_id
        if create_tenant_id is not None:
            self.create_tenant_id = create_tenant_id
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if permission_level is not None:
            self.permission_level = permission_level
        if arrange_infos is not None:
            self.arrange_infos = arrange_infos

    @property
    def id(self):
        r"""Gets the id of this AppDetailInfo.

        应用id

        :return: The id of this AppDetailInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AppDetailInfo.

        应用id

        :param id: The id of this AppDetailInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this AppDetailInfo.

        应用名称

        :return: The name of this AppDetailInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AppDetailInfo.

        应用名称

        :param name: The name of this AppDetailInfo.
        :type name: str
        """
        self._name = name

    @property
    def region(self):
        r"""Gets the region of this AppDetailInfo.

        应用所属区域

        :return: The region of this AppDetailInfo.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this AppDetailInfo.

        应用所属区域

        :param region: The region of this AppDetailInfo.
        :type region: str
        """
        self._region = region

    @property
    def description(self):
        r"""Gets the description of this AppDetailInfo.

        描述

        :return: The description of this AppDetailInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AppDetailInfo.

        描述

        :param description: The description of this AppDetailInfo.
        :type description: str
        """
        self._description = description

    @property
    def is_disable(self):
        r"""Gets the is_disable of this AppDetailInfo.

        当前应用是否被禁用

        :return: The is_disable of this AppDetailInfo.
        :rtype: bool
        """
        return self._is_disable

    @is_disable.setter
    def is_disable(self, is_disable):
        r"""Sets the is_disable of this AppDetailInfo.

        当前应用是否被禁用

        :param is_disable: The is_disable of this AppDetailInfo.
        :type is_disable: bool
        """
        self._is_disable = is_disable

    @property
    def create_type(self):
        r"""Gets the create_type of this AppDetailInfo.

        创建方式

        :return: The create_type of this AppDetailInfo.
        :rtype: str
        """
        return self._create_type

    @create_type.setter
    def create_type(self, create_type):
        r"""Sets the create_type of this AppDetailInfo.

        创建方式

        :param create_type: The create_type of this AppDetailInfo.
        :type create_type: str
        """
        self._create_type = create_type

    @property
    def project_id(self):
        r"""Gets the project_id of this AppDetailInfo.

        项目id

        :return: The project_id of this AppDetailInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this AppDetailInfo.

        项目id

        :param project_id: The project_id of this AppDetailInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def project_name(self):
        r"""Gets the project_name of this AppDetailInfo.

        项目名称

        :return: The project_name of this AppDetailInfo.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        r"""Sets the project_name of this AppDetailInfo.

        项目名称

        :param project_name: The project_name of this AppDetailInfo.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def slave_cluster_id(self):
        r"""Gets the slave_cluster_id of this AppDetailInfo.

        slave集群id，默认为null时使用默认slave集群，用户自定义slave时为slave集群id

        :return: The slave_cluster_id of this AppDetailInfo.
        :rtype: str
        """
        return self._slave_cluster_id

    @slave_cluster_id.setter
    def slave_cluster_id(self, slave_cluster_id):
        r"""Sets the slave_cluster_id of this AppDetailInfo.

        slave集群id，默认为null时使用默认slave集群，用户自定义slave时为slave集群id

        :param slave_cluster_id: The slave_cluster_id of this AppDetailInfo.
        :type slave_cluster_id: str
        """
        self._slave_cluster_id = slave_cluster_id

    @property
    def is_care(self):
        r"""Gets the is_care of this AppDetailInfo.

        当前用户是否已收藏

        :return: The is_care of this AppDetailInfo.
        :rtype: bool
        """
        return self._is_care

    @is_care.setter
    def is_care(self, is_care):
        r"""Sets the is_care of this AppDetailInfo.

        当前用户是否已收藏

        :param is_care: The is_care of this AppDetailInfo.
        :type is_care: bool
        """
        self._is_care = is_care

    @property
    def can_modify(self):
        r"""Gets the can_modify of this AppDetailInfo.

        是否有编辑权限

        :return: The can_modify of this AppDetailInfo.
        :rtype: bool
        """
        return self._can_modify

    @can_modify.setter
    def can_modify(self, can_modify):
        r"""Sets the can_modify of this AppDetailInfo.

        是否有编辑权限

        :param can_modify: The can_modify of this AppDetailInfo.
        :type can_modify: bool
        """
        self._can_modify = can_modify

    @property
    def can_delete(self):
        r"""Gets the can_delete of this AppDetailInfo.

        是否有删除的权限

        :return: The can_delete of this AppDetailInfo.
        :rtype: bool
        """
        return self._can_delete

    @can_delete.setter
    def can_delete(self, can_delete):
        r"""Sets the can_delete of this AppDetailInfo.

        是否有删除的权限

        :param can_delete: The can_delete of this AppDetailInfo.
        :type can_delete: bool
        """
        self._can_delete = can_delete

    @property
    def can_view(self):
        r"""Gets the can_view of this AppDetailInfo.

        是否有查看权限

        :return: The can_view of this AppDetailInfo.
        :rtype: bool
        """
        return self._can_view

    @can_view.setter
    def can_view(self, can_view):
        r"""Sets the can_view of this AppDetailInfo.

        是否有查看权限

        :param can_view: The can_view of this AppDetailInfo.
        :type can_view: bool
        """
        self._can_view = can_view

    @property
    def can_execute(self):
        r"""Gets the can_execute of this AppDetailInfo.

        是否有部署权限

        :return: The can_execute of this AppDetailInfo.
        :rtype: bool
        """
        return self._can_execute

    @can_execute.setter
    def can_execute(self, can_execute):
        r"""Sets the can_execute of this AppDetailInfo.

        是否有部署权限

        :param can_execute: The can_execute of this AppDetailInfo.
        :type can_execute: bool
        """
        self._can_execute = can_execute

    @property
    def can_copy(self):
        r"""Gets the can_copy of this AppDetailInfo.

        是否有复制权限

        :return: The can_copy of this AppDetailInfo.
        :rtype: bool
        """
        return self._can_copy

    @can_copy.setter
    def can_copy(self, can_copy):
        r"""Sets the can_copy of this AppDetailInfo.

        是否有复制权限

        :param can_copy: The can_copy of this AppDetailInfo.
        :type can_copy: bool
        """
        self._can_copy = can_copy

    @property
    def can_manage(self):
        r"""Gets the can_manage of this AppDetailInfo.

        是否有编辑应用权限矩阵的权限

        :return: The can_manage of this AppDetailInfo.
        :rtype: bool
        """
        return self._can_manage

    @can_manage.setter
    def can_manage(self, can_manage):
        r"""Sets the can_manage of this AppDetailInfo.

        是否有编辑应用权限矩阵的权限

        :param can_manage: The can_manage of this AppDetailInfo.
        :type can_manage: bool
        """
        self._can_manage = can_manage

    @property
    def can_create_env(self):
        r"""Gets the can_create_env of this AppDetailInfo.

        是否有创建环境的权限

        :return: The can_create_env of this AppDetailInfo.
        :rtype: bool
        """
        return self._can_create_env

    @can_create_env.setter
    def can_create_env(self, can_create_env):
        r"""Sets the can_create_env of this AppDetailInfo.

        是否有创建环境的权限

        :param can_create_env: The can_create_env of this AppDetailInfo.
        :type can_create_env: bool
        """
        self._can_create_env = can_create_env

    @property
    def can_disable(self):
        r"""Gets the can_disable of this AppDetailInfo.

        是否有禁用应用的权限

        :return: The can_disable of this AppDetailInfo.
        :rtype: bool
        """
        return self._can_disable

    @can_disable.setter
    def can_disable(self, can_disable):
        r"""Sets the can_disable of this AppDetailInfo.

        是否有禁用应用的权限

        :param can_disable: The can_disable of this AppDetailInfo.
        :type can_disable: bool
        """
        self._can_disable = can_disable

    @property
    def owner_tenant_id(self):
        r"""Gets the owner_tenant_id of this AppDetailInfo.

        应用所属人租户id

        :return: The owner_tenant_id of this AppDetailInfo.
        :rtype: str
        """
        return self._owner_tenant_id

    @owner_tenant_id.setter
    def owner_tenant_id(self, owner_tenant_id):
        r"""Sets the owner_tenant_id of this AppDetailInfo.

        应用所属人租户id

        :param owner_tenant_id: The owner_tenant_id of this AppDetailInfo.
        :type owner_tenant_id: str
        """
        self._owner_tenant_id = owner_tenant_id

    @property
    def create_user_id(self):
        r"""Gets the create_user_id of this AppDetailInfo.

        应用创建者用户名

        :return: The create_user_id of this AppDetailInfo.
        :rtype: str
        """
        return self._create_user_id

    @create_user_id.setter
    def create_user_id(self, create_user_id):
        r"""Sets the create_user_id of this AppDetailInfo.

        应用创建者用户名

        :param create_user_id: The create_user_id of this AppDetailInfo.
        :type create_user_id: str
        """
        self._create_user_id = create_user_id

    @property
    def create_tenant_id(self):
        r"""Gets the create_tenant_id of this AppDetailInfo.

        应用创建人租户id

        :return: The create_tenant_id of this AppDetailInfo.
        :rtype: str
        """
        return self._create_tenant_id

    @create_tenant_id.setter
    def create_tenant_id(self, create_tenant_id):
        r"""Sets the create_tenant_id of this AppDetailInfo.

        应用创建人租户id

        :param create_tenant_id: The create_tenant_id of this AppDetailInfo.
        :type create_tenant_id: str
        """
        self._create_tenant_id = create_tenant_id

    @property
    def create_time(self):
        r"""Gets the create_time of this AppDetailInfo.

        创建时间

        :return: The create_time of this AppDetailInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this AppDetailInfo.

        创建时间

        :param create_time: The create_time of this AppDetailInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this AppDetailInfo.

        修改时间

        :return: The update_time of this AppDetailInfo.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this AppDetailInfo.

        修改时间

        :param update_time: The update_time of this AppDetailInfo.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def permission_level(self):
        r"""Gets the permission_level of this AppDetailInfo.

        权限等级

        :return: The permission_level of this AppDetailInfo.
        :rtype: str
        """
        return self._permission_level

    @permission_level.setter
    def permission_level(self, permission_level):
        r"""Sets the permission_level of this AppDetailInfo.

        权限等级

        :param permission_level: The permission_level of this AppDetailInfo.
        :type permission_level: str
        """
        self._permission_level = permission_level

    @property
    def arrange_infos(self):
        r"""Gets the arrange_infos of this AppDetailInfo.

        部署任务信息

        :return: The arrange_infos of this AppDetailInfo.
        :rtype: list[:class:`huaweicloudsdkcodeartsdeploy.v2.TaskV2Info`]
        """
        return self._arrange_infos

    @arrange_infos.setter
    def arrange_infos(self, arrange_infos):
        r"""Sets the arrange_infos of this AppDetailInfo.

        部署任务信息

        :param arrange_infos: The arrange_infos of this AppDetailInfo.
        :type arrange_infos: list[:class:`huaweicloudsdkcodeartsdeploy.v2.TaskV2Info`]
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
        if not isinstance(other, AppDetailInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
