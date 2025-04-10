# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DevUcEnvironmentPermission:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'role_id': 'str',
        'devuc_role_id_list': 'list[str]',
        'role_type': 'str',
        'name': 'str',
        'region': 'str',
        'environment_id': 'str',
        'can_view': 'bool',
        'can_edit': 'bool',
        'can_delete': 'bool',
        'can_deploy': 'bool',
        'can_manage': 'bool',
        'create_time': 'datetime',
        'update_time': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'role_id': 'role_id',
        'devuc_role_id_list': 'devuc_role_id_list',
        'role_type': 'role_type',
        'name': 'name',
        'region': 'region',
        'environment_id': 'environment_id',
        'can_view': 'can_view',
        'can_edit': 'can_edit',
        'can_delete': 'can_delete',
        'can_deploy': 'can_deploy',
        'can_manage': 'can_manage',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, role_id=None, devuc_role_id_list=None, role_type=None, name=None, region=None, environment_id=None, can_view=None, can_edit=None, can_delete=None, can_deploy=None, can_manage=None, create_time=None, update_time=None):
        r"""DevUcEnvironmentPermission

        The model defined in huaweicloud sdk

        :param id: 权限id
        :type id: int
        :param role_id: 角色id
        :type role_id: str
        :param devuc_role_id_list: 角色id列表
        :type devuc_role_id_list: list[str]
        :param role_type: 角色类型， environment-creator： 环境创建者； project： 项目管理员；template-customized-inst：系统角色； template-project-customized、project-customized：自定义角色
        :type role_type: str
        :param name: 角色名称
        :type name: str
        :param region: 局点信息
        :type region: str
        :param environment_id: 环境id
        :type environment_id: str
        :param can_view: 是否有查看权限
        :type can_view: bool
        :param can_edit: 是否有编辑权限
        :type can_edit: bool
        :param can_delete: 是否有删除权限
        :type can_delete: bool
        :param can_deploy: 是否有部署权限
        :type can_deploy: bool
        :param can_manage: 是否有权限管理权限
        :type can_manage: bool
        :param create_time: 创建时间
        :type create_time: datetime
        :param update_time: 修改时间
        :type update_time: datetime
        """
        
        

        self._id = None
        self._role_id = None
        self._devuc_role_id_list = None
        self._role_type = None
        self._name = None
        self._region = None
        self._environment_id = None
        self._can_view = None
        self._can_edit = None
        self._can_delete = None
        self._can_deploy = None
        self._can_manage = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if role_id is not None:
            self.role_id = role_id
        if devuc_role_id_list is not None:
            self.devuc_role_id_list = devuc_role_id_list
        if role_type is not None:
            self.role_type = role_type
        if name is not None:
            self.name = name
        if region is not None:
            self.region = region
        if environment_id is not None:
            self.environment_id = environment_id
        if can_view is not None:
            self.can_view = can_view
        if can_edit is not None:
            self.can_edit = can_edit
        if can_delete is not None:
            self.can_delete = can_delete
        if can_deploy is not None:
            self.can_deploy = can_deploy
        if can_manage is not None:
            self.can_manage = can_manage
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        r"""Gets the id of this DevUcEnvironmentPermission.

        权限id

        :return: The id of this DevUcEnvironmentPermission.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DevUcEnvironmentPermission.

        权限id

        :param id: The id of this DevUcEnvironmentPermission.
        :type id: int
        """
        self._id = id

    @property
    def role_id(self):
        r"""Gets the role_id of this DevUcEnvironmentPermission.

        角色id

        :return: The role_id of this DevUcEnvironmentPermission.
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        r"""Sets the role_id of this DevUcEnvironmentPermission.

        角色id

        :param role_id: The role_id of this DevUcEnvironmentPermission.
        :type role_id: str
        """
        self._role_id = role_id

    @property
    def devuc_role_id_list(self):
        r"""Gets the devuc_role_id_list of this DevUcEnvironmentPermission.

        角色id列表

        :return: The devuc_role_id_list of this DevUcEnvironmentPermission.
        :rtype: list[str]
        """
        return self._devuc_role_id_list

    @devuc_role_id_list.setter
    def devuc_role_id_list(self, devuc_role_id_list):
        r"""Sets the devuc_role_id_list of this DevUcEnvironmentPermission.

        角色id列表

        :param devuc_role_id_list: The devuc_role_id_list of this DevUcEnvironmentPermission.
        :type devuc_role_id_list: list[str]
        """
        self._devuc_role_id_list = devuc_role_id_list

    @property
    def role_type(self):
        r"""Gets the role_type of this DevUcEnvironmentPermission.

        角色类型， environment-creator： 环境创建者； project： 项目管理员；template-customized-inst：系统角色； template-project-customized、project-customized：自定义角色

        :return: The role_type of this DevUcEnvironmentPermission.
        :rtype: str
        """
        return self._role_type

    @role_type.setter
    def role_type(self, role_type):
        r"""Sets the role_type of this DevUcEnvironmentPermission.

        角色类型， environment-creator： 环境创建者； project： 项目管理员；template-customized-inst：系统角色； template-project-customized、project-customized：自定义角色

        :param role_type: The role_type of this DevUcEnvironmentPermission.
        :type role_type: str
        """
        self._role_type = role_type

    @property
    def name(self):
        r"""Gets the name of this DevUcEnvironmentPermission.

        角色名称

        :return: The name of this DevUcEnvironmentPermission.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DevUcEnvironmentPermission.

        角色名称

        :param name: The name of this DevUcEnvironmentPermission.
        :type name: str
        """
        self._name = name

    @property
    def region(self):
        r"""Gets the region of this DevUcEnvironmentPermission.

        局点信息

        :return: The region of this DevUcEnvironmentPermission.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this DevUcEnvironmentPermission.

        局点信息

        :param region: The region of this DevUcEnvironmentPermission.
        :type region: str
        """
        self._region = region

    @property
    def environment_id(self):
        r"""Gets the environment_id of this DevUcEnvironmentPermission.

        环境id

        :return: The environment_id of this DevUcEnvironmentPermission.
        :rtype: str
        """
        return self._environment_id

    @environment_id.setter
    def environment_id(self, environment_id):
        r"""Sets the environment_id of this DevUcEnvironmentPermission.

        环境id

        :param environment_id: The environment_id of this DevUcEnvironmentPermission.
        :type environment_id: str
        """
        self._environment_id = environment_id

    @property
    def can_view(self):
        r"""Gets the can_view of this DevUcEnvironmentPermission.

        是否有查看权限

        :return: The can_view of this DevUcEnvironmentPermission.
        :rtype: bool
        """
        return self._can_view

    @can_view.setter
    def can_view(self, can_view):
        r"""Sets the can_view of this DevUcEnvironmentPermission.

        是否有查看权限

        :param can_view: The can_view of this DevUcEnvironmentPermission.
        :type can_view: bool
        """
        self._can_view = can_view

    @property
    def can_edit(self):
        r"""Gets the can_edit of this DevUcEnvironmentPermission.

        是否有编辑权限

        :return: The can_edit of this DevUcEnvironmentPermission.
        :rtype: bool
        """
        return self._can_edit

    @can_edit.setter
    def can_edit(self, can_edit):
        r"""Sets the can_edit of this DevUcEnvironmentPermission.

        是否有编辑权限

        :param can_edit: The can_edit of this DevUcEnvironmentPermission.
        :type can_edit: bool
        """
        self._can_edit = can_edit

    @property
    def can_delete(self):
        r"""Gets the can_delete of this DevUcEnvironmentPermission.

        是否有删除权限

        :return: The can_delete of this DevUcEnvironmentPermission.
        :rtype: bool
        """
        return self._can_delete

    @can_delete.setter
    def can_delete(self, can_delete):
        r"""Sets the can_delete of this DevUcEnvironmentPermission.

        是否有删除权限

        :param can_delete: The can_delete of this DevUcEnvironmentPermission.
        :type can_delete: bool
        """
        self._can_delete = can_delete

    @property
    def can_deploy(self):
        r"""Gets the can_deploy of this DevUcEnvironmentPermission.

        是否有部署权限

        :return: The can_deploy of this DevUcEnvironmentPermission.
        :rtype: bool
        """
        return self._can_deploy

    @can_deploy.setter
    def can_deploy(self, can_deploy):
        r"""Sets the can_deploy of this DevUcEnvironmentPermission.

        是否有部署权限

        :param can_deploy: The can_deploy of this DevUcEnvironmentPermission.
        :type can_deploy: bool
        """
        self._can_deploy = can_deploy

    @property
    def can_manage(self):
        r"""Gets the can_manage of this DevUcEnvironmentPermission.

        是否有权限管理权限

        :return: The can_manage of this DevUcEnvironmentPermission.
        :rtype: bool
        """
        return self._can_manage

    @can_manage.setter
    def can_manage(self, can_manage):
        r"""Sets the can_manage of this DevUcEnvironmentPermission.

        是否有权限管理权限

        :param can_manage: The can_manage of this DevUcEnvironmentPermission.
        :type can_manage: bool
        """
        self._can_manage = can_manage

    @property
    def create_time(self):
        r"""Gets the create_time of this DevUcEnvironmentPermission.

        创建时间

        :return: The create_time of this DevUcEnvironmentPermission.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this DevUcEnvironmentPermission.

        创建时间

        :param create_time: The create_time of this DevUcEnvironmentPermission.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this DevUcEnvironmentPermission.

        修改时间

        :return: The update_time of this DevUcEnvironmentPermission.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this DevUcEnvironmentPermission.

        修改时间

        :param update_time: The update_time of this DevUcEnvironmentPermission.
        :type update_time: datetime
        """
        self._update_time = update_time

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
        if not isinstance(other, DevUcEnvironmentPermission):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
