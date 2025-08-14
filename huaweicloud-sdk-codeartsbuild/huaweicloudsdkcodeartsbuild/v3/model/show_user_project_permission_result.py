# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowUserProjectPermissionResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'create_permission': 'bool',
        'modify_permission': 'bool',
        'group_permission': 'bool',
        'delete_permission': 'bool',
        'view_permission': 'bool',
        'execute_permission': 'bool',
        'copy_permission': 'bool',
        'forbidden_permission': 'bool',
        'manager_permission': 'bool',
        'role_id': 'str',
        'role_name': 'str',
        'role_ids': 'list[str]',
        'role_names': 'list[str]'
    }

    attribute_map = {
        'project_id': 'project_id',
        'create_permission': 'create_permission',
        'modify_permission': 'modify_permission',
        'group_permission': 'group_permission',
        'delete_permission': 'delete_permission',
        'view_permission': 'view_permission',
        'execute_permission': 'execute_permission',
        'copy_permission': 'copy_permission',
        'forbidden_permission': 'forbidden_permission',
        'manager_permission': 'manager_permission',
        'role_id': 'role_id',
        'role_name': 'role_name',
        'role_ids': 'role_ids',
        'role_names': 'role_names'
    }

    def __init__(self, project_id=None, create_permission=None, modify_permission=None, group_permission=None, delete_permission=None, view_permission=None, execute_permission=None, copy_permission=None, forbidden_permission=None, manager_permission=None, role_id=None, role_name=None, role_ids=None, role_names=None):
        r"""ShowUserProjectPermissionResult

        The model defined in huaweicloud sdk

        :param project_id: 工程编号
        :type project_id: str
        :param create_permission: 用户是否有创建权限
        :type create_permission: bool
        :param modify_permission: 用户是否有修改权限
        :type modify_permission: bool
        :param group_permission: 用户是否有分类权限
        :type group_permission: bool
        :param delete_permission: 用户是否有删除权限。
        :type delete_permission: bool
        :param view_permission: 用户是否有查看权限。
        :type view_permission: bool
        :param execute_permission: 用户是否有执行权限。
        :type execute_permission: bool
        :param copy_permission: 用户是否有克隆权限。
        :type copy_permission: bool
        :param forbidden_permission: 用户是否有禁用权限。
        :type forbidden_permission: bool
        :param manager_permission: 用户是否有管理权限。
        :type manager_permission: bool
        :param role_id: 角色ID
        :type role_id: str
        :param role_name: 角色名
        :type role_name: str
        :param role_ids: 角色编码集合。
        :type role_ids: list[str]
        :param role_names: 角色名称集合。
        :type role_names: list[str]
        """
        
        

        self._project_id = None
        self._create_permission = None
        self._modify_permission = None
        self._group_permission = None
        self._delete_permission = None
        self._view_permission = None
        self._execute_permission = None
        self._copy_permission = None
        self._forbidden_permission = None
        self._manager_permission = None
        self._role_id = None
        self._role_name = None
        self._role_ids = None
        self._role_names = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        if create_permission is not None:
            self.create_permission = create_permission
        if modify_permission is not None:
            self.modify_permission = modify_permission
        if group_permission is not None:
            self.group_permission = group_permission
        if delete_permission is not None:
            self.delete_permission = delete_permission
        if view_permission is not None:
            self.view_permission = view_permission
        if execute_permission is not None:
            self.execute_permission = execute_permission
        if copy_permission is not None:
            self.copy_permission = copy_permission
        if forbidden_permission is not None:
            self.forbidden_permission = forbidden_permission
        if manager_permission is not None:
            self.manager_permission = manager_permission
        if role_id is not None:
            self.role_id = role_id
        if role_name is not None:
            self.role_name = role_name
        if role_ids is not None:
            self.role_ids = role_ids
        if role_names is not None:
            self.role_names = role_names

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowUserProjectPermissionResult.

        工程编号

        :return: The project_id of this ShowUserProjectPermissionResult.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowUserProjectPermissionResult.

        工程编号

        :param project_id: The project_id of this ShowUserProjectPermissionResult.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def create_permission(self):
        r"""Gets the create_permission of this ShowUserProjectPermissionResult.

        用户是否有创建权限

        :return: The create_permission of this ShowUserProjectPermissionResult.
        :rtype: bool
        """
        return self._create_permission

    @create_permission.setter
    def create_permission(self, create_permission):
        r"""Sets the create_permission of this ShowUserProjectPermissionResult.

        用户是否有创建权限

        :param create_permission: The create_permission of this ShowUserProjectPermissionResult.
        :type create_permission: bool
        """
        self._create_permission = create_permission

    @property
    def modify_permission(self):
        r"""Gets the modify_permission of this ShowUserProjectPermissionResult.

        用户是否有修改权限

        :return: The modify_permission of this ShowUserProjectPermissionResult.
        :rtype: bool
        """
        return self._modify_permission

    @modify_permission.setter
    def modify_permission(self, modify_permission):
        r"""Sets the modify_permission of this ShowUserProjectPermissionResult.

        用户是否有修改权限

        :param modify_permission: The modify_permission of this ShowUserProjectPermissionResult.
        :type modify_permission: bool
        """
        self._modify_permission = modify_permission

    @property
    def group_permission(self):
        r"""Gets the group_permission of this ShowUserProjectPermissionResult.

        用户是否有分类权限

        :return: The group_permission of this ShowUserProjectPermissionResult.
        :rtype: bool
        """
        return self._group_permission

    @group_permission.setter
    def group_permission(self, group_permission):
        r"""Sets the group_permission of this ShowUserProjectPermissionResult.

        用户是否有分类权限

        :param group_permission: The group_permission of this ShowUserProjectPermissionResult.
        :type group_permission: bool
        """
        self._group_permission = group_permission

    @property
    def delete_permission(self):
        r"""Gets the delete_permission of this ShowUserProjectPermissionResult.

        用户是否有删除权限。

        :return: The delete_permission of this ShowUserProjectPermissionResult.
        :rtype: bool
        """
        return self._delete_permission

    @delete_permission.setter
    def delete_permission(self, delete_permission):
        r"""Sets the delete_permission of this ShowUserProjectPermissionResult.

        用户是否有删除权限。

        :param delete_permission: The delete_permission of this ShowUserProjectPermissionResult.
        :type delete_permission: bool
        """
        self._delete_permission = delete_permission

    @property
    def view_permission(self):
        r"""Gets the view_permission of this ShowUserProjectPermissionResult.

        用户是否有查看权限。

        :return: The view_permission of this ShowUserProjectPermissionResult.
        :rtype: bool
        """
        return self._view_permission

    @view_permission.setter
    def view_permission(self, view_permission):
        r"""Sets the view_permission of this ShowUserProjectPermissionResult.

        用户是否有查看权限。

        :param view_permission: The view_permission of this ShowUserProjectPermissionResult.
        :type view_permission: bool
        """
        self._view_permission = view_permission

    @property
    def execute_permission(self):
        r"""Gets the execute_permission of this ShowUserProjectPermissionResult.

        用户是否有执行权限。

        :return: The execute_permission of this ShowUserProjectPermissionResult.
        :rtype: bool
        """
        return self._execute_permission

    @execute_permission.setter
    def execute_permission(self, execute_permission):
        r"""Sets the execute_permission of this ShowUserProjectPermissionResult.

        用户是否有执行权限。

        :param execute_permission: The execute_permission of this ShowUserProjectPermissionResult.
        :type execute_permission: bool
        """
        self._execute_permission = execute_permission

    @property
    def copy_permission(self):
        r"""Gets the copy_permission of this ShowUserProjectPermissionResult.

        用户是否有克隆权限。

        :return: The copy_permission of this ShowUserProjectPermissionResult.
        :rtype: bool
        """
        return self._copy_permission

    @copy_permission.setter
    def copy_permission(self, copy_permission):
        r"""Sets the copy_permission of this ShowUserProjectPermissionResult.

        用户是否有克隆权限。

        :param copy_permission: The copy_permission of this ShowUserProjectPermissionResult.
        :type copy_permission: bool
        """
        self._copy_permission = copy_permission

    @property
    def forbidden_permission(self):
        r"""Gets the forbidden_permission of this ShowUserProjectPermissionResult.

        用户是否有禁用权限。

        :return: The forbidden_permission of this ShowUserProjectPermissionResult.
        :rtype: bool
        """
        return self._forbidden_permission

    @forbidden_permission.setter
    def forbidden_permission(self, forbidden_permission):
        r"""Sets the forbidden_permission of this ShowUserProjectPermissionResult.

        用户是否有禁用权限。

        :param forbidden_permission: The forbidden_permission of this ShowUserProjectPermissionResult.
        :type forbidden_permission: bool
        """
        self._forbidden_permission = forbidden_permission

    @property
    def manager_permission(self):
        r"""Gets the manager_permission of this ShowUserProjectPermissionResult.

        用户是否有管理权限。

        :return: The manager_permission of this ShowUserProjectPermissionResult.
        :rtype: bool
        """
        return self._manager_permission

    @manager_permission.setter
    def manager_permission(self, manager_permission):
        r"""Sets the manager_permission of this ShowUserProjectPermissionResult.

        用户是否有管理权限。

        :param manager_permission: The manager_permission of this ShowUserProjectPermissionResult.
        :type manager_permission: bool
        """
        self._manager_permission = manager_permission

    @property
    def role_id(self):
        r"""Gets the role_id of this ShowUserProjectPermissionResult.

        角色ID

        :return: The role_id of this ShowUserProjectPermissionResult.
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        r"""Sets the role_id of this ShowUserProjectPermissionResult.

        角色ID

        :param role_id: The role_id of this ShowUserProjectPermissionResult.
        :type role_id: str
        """
        self._role_id = role_id

    @property
    def role_name(self):
        r"""Gets the role_name of this ShowUserProjectPermissionResult.

        角色名

        :return: The role_name of this ShowUserProjectPermissionResult.
        :rtype: str
        """
        return self._role_name

    @role_name.setter
    def role_name(self, role_name):
        r"""Sets the role_name of this ShowUserProjectPermissionResult.

        角色名

        :param role_name: The role_name of this ShowUserProjectPermissionResult.
        :type role_name: str
        """
        self._role_name = role_name

    @property
    def role_ids(self):
        r"""Gets the role_ids of this ShowUserProjectPermissionResult.

        角色编码集合。

        :return: The role_ids of this ShowUserProjectPermissionResult.
        :rtype: list[str]
        """
        return self._role_ids

    @role_ids.setter
    def role_ids(self, role_ids):
        r"""Sets the role_ids of this ShowUserProjectPermissionResult.

        角色编码集合。

        :param role_ids: The role_ids of this ShowUserProjectPermissionResult.
        :type role_ids: list[str]
        """
        self._role_ids = role_ids

    @property
    def role_names(self):
        r"""Gets the role_names of this ShowUserProjectPermissionResult.

        角色名称集合。

        :return: The role_names of this ShowUserProjectPermissionResult.
        :rtype: list[str]
        """
        return self._role_names

    @role_names.setter
    def role_names(self, role_names):
        r"""Sets the role_names of this ShowUserProjectPermissionResult.

        角色名称集合。

        :param role_names: The role_names of this ShowUserProjectPermissionResult.
        :type role_names: list[str]
        """
        self._role_names = role_names

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
        if not isinstance(other, ShowUserProjectPermissionResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
