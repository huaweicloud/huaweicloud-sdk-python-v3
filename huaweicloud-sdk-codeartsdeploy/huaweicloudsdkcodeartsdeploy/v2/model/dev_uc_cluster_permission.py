# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DevUcClusterPermission:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region': 'str',
        'role_id': 'str',
        'devuc_role_id_list': 'list[str]',
        'name': 'str',
        'group_id': 'str',
        'can_view': 'bool',
        'can_edit': 'bool',
        'can_delete': 'bool',
        'can_add_host': 'bool',
        'can_manage': 'bool',
        'can_copy': 'bool',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'role_type': 'str'
    }

    attribute_map = {
        'region': 'region',
        'role_id': 'role_id',
        'devuc_role_id_list': 'devuc_role_id_list',
        'name': 'name',
        'group_id': 'group_id',
        'can_view': 'can_view',
        'can_edit': 'can_edit',
        'can_delete': 'can_delete',
        'can_add_host': 'can_add_host',
        'can_manage': 'can_manage',
        'can_copy': 'can_copy',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'role_type': 'role_type'
    }

    def __init__(self, region=None, role_id=None, devuc_role_id_list=None, name=None, group_id=None, can_view=None, can_edit=None, can_delete=None, can_add_host=None, can_manage=None, can_copy=None, create_time=None, update_time=None, role_type=None):
        r"""DevUcClusterPermission

        The model defined in huaweicloud sdk

        :param region: 局点信息
        :type region: str
        :param role_id: 角色id
        :type role_id: str
        :param devuc_role_id_list: 角色id列表
        :type devuc_role_id_list: list[str]
        :param name: 角色名称
        :type name: str
        :param group_id: 主机集群id
        :type group_id: str
        :param can_view: 是否有查看权限
        :type can_view: bool
        :param can_edit: 是否有编辑权限
        :type can_edit: bool
        :param can_delete: 是否有删除权限
        :type can_delete: bool
        :param can_add_host: 是否有添加主机权限
        :type can_add_host: bool
        :param can_manage: 是否有权限管理权限
        :type can_manage: bool
        :param can_copy: 是否有拷贝权限
        :type can_copy: bool
        :param create_time: 创建时间
        :type create_time: datetime
        :param update_time: 修改时间
        :type update_time: datetime
        :param role_type: 角色类型，project-customized：自定义角色；template-project-customized：系统自定义角色； template-customized-inst：系统角色；cluster-creator：集群创建者；project_admin：项目创建者
        :type role_type: str
        """
        
        

        self._region = None
        self._role_id = None
        self._devuc_role_id_list = None
        self._name = None
        self._group_id = None
        self._can_view = None
        self._can_edit = None
        self._can_delete = None
        self._can_add_host = None
        self._can_manage = None
        self._can_copy = None
        self._create_time = None
        self._update_time = None
        self._role_type = None
        self.discriminator = None

        if region is not None:
            self.region = region
        if role_id is not None:
            self.role_id = role_id
        if devuc_role_id_list is not None:
            self.devuc_role_id_list = devuc_role_id_list
        if name is not None:
            self.name = name
        if group_id is not None:
            self.group_id = group_id
        if can_view is not None:
            self.can_view = can_view
        if can_edit is not None:
            self.can_edit = can_edit
        if can_delete is not None:
            self.can_delete = can_delete
        if can_add_host is not None:
            self.can_add_host = can_add_host
        if can_manage is not None:
            self.can_manage = can_manage
        if can_copy is not None:
            self.can_copy = can_copy
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if role_type is not None:
            self.role_type = role_type

    @property
    def region(self):
        r"""Gets the region of this DevUcClusterPermission.

        局点信息

        :return: The region of this DevUcClusterPermission.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this DevUcClusterPermission.

        局点信息

        :param region: The region of this DevUcClusterPermission.
        :type region: str
        """
        self._region = region

    @property
    def role_id(self):
        r"""Gets the role_id of this DevUcClusterPermission.

        角色id

        :return: The role_id of this DevUcClusterPermission.
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        r"""Sets the role_id of this DevUcClusterPermission.

        角色id

        :param role_id: The role_id of this DevUcClusterPermission.
        :type role_id: str
        """
        self._role_id = role_id

    @property
    def devuc_role_id_list(self):
        r"""Gets the devuc_role_id_list of this DevUcClusterPermission.

        角色id列表

        :return: The devuc_role_id_list of this DevUcClusterPermission.
        :rtype: list[str]
        """
        return self._devuc_role_id_list

    @devuc_role_id_list.setter
    def devuc_role_id_list(self, devuc_role_id_list):
        r"""Sets the devuc_role_id_list of this DevUcClusterPermission.

        角色id列表

        :param devuc_role_id_list: The devuc_role_id_list of this DevUcClusterPermission.
        :type devuc_role_id_list: list[str]
        """
        self._devuc_role_id_list = devuc_role_id_list

    @property
    def name(self):
        r"""Gets the name of this DevUcClusterPermission.

        角色名称

        :return: The name of this DevUcClusterPermission.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DevUcClusterPermission.

        角色名称

        :param name: The name of this DevUcClusterPermission.
        :type name: str
        """
        self._name = name

    @property
    def group_id(self):
        r"""Gets the group_id of this DevUcClusterPermission.

        主机集群id

        :return: The group_id of this DevUcClusterPermission.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this DevUcClusterPermission.

        主机集群id

        :param group_id: The group_id of this DevUcClusterPermission.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def can_view(self):
        r"""Gets the can_view of this DevUcClusterPermission.

        是否有查看权限

        :return: The can_view of this DevUcClusterPermission.
        :rtype: bool
        """
        return self._can_view

    @can_view.setter
    def can_view(self, can_view):
        r"""Sets the can_view of this DevUcClusterPermission.

        是否有查看权限

        :param can_view: The can_view of this DevUcClusterPermission.
        :type can_view: bool
        """
        self._can_view = can_view

    @property
    def can_edit(self):
        r"""Gets the can_edit of this DevUcClusterPermission.

        是否有编辑权限

        :return: The can_edit of this DevUcClusterPermission.
        :rtype: bool
        """
        return self._can_edit

    @can_edit.setter
    def can_edit(self, can_edit):
        r"""Sets the can_edit of this DevUcClusterPermission.

        是否有编辑权限

        :param can_edit: The can_edit of this DevUcClusterPermission.
        :type can_edit: bool
        """
        self._can_edit = can_edit

    @property
    def can_delete(self):
        r"""Gets the can_delete of this DevUcClusterPermission.

        是否有删除权限

        :return: The can_delete of this DevUcClusterPermission.
        :rtype: bool
        """
        return self._can_delete

    @can_delete.setter
    def can_delete(self, can_delete):
        r"""Sets the can_delete of this DevUcClusterPermission.

        是否有删除权限

        :param can_delete: The can_delete of this DevUcClusterPermission.
        :type can_delete: bool
        """
        self._can_delete = can_delete

    @property
    def can_add_host(self):
        r"""Gets the can_add_host of this DevUcClusterPermission.

        是否有添加主机权限

        :return: The can_add_host of this DevUcClusterPermission.
        :rtype: bool
        """
        return self._can_add_host

    @can_add_host.setter
    def can_add_host(self, can_add_host):
        r"""Sets the can_add_host of this DevUcClusterPermission.

        是否有添加主机权限

        :param can_add_host: The can_add_host of this DevUcClusterPermission.
        :type can_add_host: bool
        """
        self._can_add_host = can_add_host

    @property
    def can_manage(self):
        r"""Gets the can_manage of this DevUcClusterPermission.

        是否有权限管理权限

        :return: The can_manage of this DevUcClusterPermission.
        :rtype: bool
        """
        return self._can_manage

    @can_manage.setter
    def can_manage(self, can_manage):
        r"""Sets the can_manage of this DevUcClusterPermission.

        是否有权限管理权限

        :param can_manage: The can_manage of this DevUcClusterPermission.
        :type can_manage: bool
        """
        self._can_manage = can_manage

    @property
    def can_copy(self):
        r"""Gets the can_copy of this DevUcClusterPermission.

        是否有拷贝权限

        :return: The can_copy of this DevUcClusterPermission.
        :rtype: bool
        """
        return self._can_copy

    @can_copy.setter
    def can_copy(self, can_copy):
        r"""Sets the can_copy of this DevUcClusterPermission.

        是否有拷贝权限

        :param can_copy: The can_copy of this DevUcClusterPermission.
        :type can_copy: bool
        """
        self._can_copy = can_copy

    @property
    def create_time(self):
        r"""Gets the create_time of this DevUcClusterPermission.

        创建时间

        :return: The create_time of this DevUcClusterPermission.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this DevUcClusterPermission.

        创建时间

        :param create_time: The create_time of this DevUcClusterPermission.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this DevUcClusterPermission.

        修改时间

        :return: The update_time of this DevUcClusterPermission.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this DevUcClusterPermission.

        修改时间

        :param update_time: The update_time of this DevUcClusterPermission.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def role_type(self):
        r"""Gets the role_type of this DevUcClusterPermission.

        角色类型，project-customized：自定义角色；template-project-customized：系统自定义角色； template-customized-inst：系统角色；cluster-creator：集群创建者；project_admin：项目创建者

        :return: The role_type of this DevUcClusterPermission.
        :rtype: str
        """
        return self._role_type

    @role_type.setter
    def role_type(self, role_type):
        r"""Sets the role_type of this DevUcClusterPermission.

        角色类型，project-customized：自定义角色；template-project-customized：系统自定义角色； template-customized-inst：系统角色；cluster-creator：集群创建者；project_admin：项目创建者

        :param role_type: The role_type of this DevUcClusterPermission.
        :type role_type: str
        """
        self._role_type = role_type

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
        if not isinstance(other, DevUcClusterPermission):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
