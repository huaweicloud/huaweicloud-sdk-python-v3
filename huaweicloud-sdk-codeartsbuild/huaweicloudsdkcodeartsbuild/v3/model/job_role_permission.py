# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobRolePermission:

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
        'role_id': 'int',
        'devuc_role_id': 'str',
        'role_name': 'str',
        'is_modify': 'bool',
        'is_delete': 'bool',
        'is_view': 'bool',
        'is_execute': 'bool',
        'is_copy': 'bool',
        'is_forbidden': 'bool',
        'is_manager': 'bool',
        'count': 'int'
    }

    attribute_map = {
        'id': 'id',
        'role_id': 'role_id',
        'devuc_role_id': 'devuc_role_id',
        'role_name': 'role_name',
        'is_modify': 'is_modify',
        'is_delete': 'is_delete',
        'is_view': 'is_view',
        'is_execute': 'is_execute',
        'is_copy': 'is_copy',
        'is_forbidden': 'is_forbidden',
        'is_manager': 'is_manager',
        'count': 'count'
    }

    def __init__(self, id=None, role_id=None, devuc_role_id=None, role_name=None, is_modify=None, is_delete=None, is_view=None, is_execute=None, is_copy=None, is_forbidden=None, is_manager=None, count=None):
        r"""JobRolePermission

        The model defined in huaweicloud sdk

        :param id: 主键ID
        :type id: int
        :param role_id: 角色ID
        :type role_id: int
        :param devuc_role_id: devuc的角色ID
        :type devuc_role_id: str
        :param role_name: 角色名称
        :type role_name: str
        :param is_modify: 修改权限
        :type is_modify: bool
        :param is_delete: 删除权限
        :type is_delete: bool
        :param is_view: 查看权限
        :type is_view: bool
        :param is_execute: 执行权限
        :type is_execute: bool
        :param is_copy: 复制权限
        :type is_copy: bool
        :param is_forbidden: 禁用权限
        :type is_forbidden: bool
        :param is_manager: 管理权限
        :type is_manager: bool
        :param count: 数量
        :type count: int
        """
        
        

        self._id = None
        self._role_id = None
        self._devuc_role_id = None
        self._role_name = None
        self._is_modify = None
        self._is_delete = None
        self._is_view = None
        self._is_execute = None
        self._is_copy = None
        self._is_forbidden = None
        self._is_manager = None
        self._count = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if role_id is not None:
            self.role_id = role_id
        if devuc_role_id is not None:
            self.devuc_role_id = devuc_role_id
        if role_name is not None:
            self.role_name = role_name
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
        if is_manager is not None:
            self.is_manager = is_manager
        if count is not None:
            self.count = count

    @property
    def id(self):
        r"""Gets the id of this JobRolePermission.

        主键ID

        :return: The id of this JobRolePermission.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this JobRolePermission.

        主键ID

        :param id: The id of this JobRolePermission.
        :type id: int
        """
        self._id = id

    @property
    def role_id(self):
        r"""Gets the role_id of this JobRolePermission.

        角色ID

        :return: The role_id of this JobRolePermission.
        :rtype: int
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        r"""Sets the role_id of this JobRolePermission.

        角色ID

        :param role_id: The role_id of this JobRolePermission.
        :type role_id: int
        """
        self._role_id = role_id

    @property
    def devuc_role_id(self):
        r"""Gets the devuc_role_id of this JobRolePermission.

        devuc的角色ID

        :return: The devuc_role_id of this JobRolePermission.
        :rtype: str
        """
        return self._devuc_role_id

    @devuc_role_id.setter
    def devuc_role_id(self, devuc_role_id):
        r"""Sets the devuc_role_id of this JobRolePermission.

        devuc的角色ID

        :param devuc_role_id: The devuc_role_id of this JobRolePermission.
        :type devuc_role_id: str
        """
        self._devuc_role_id = devuc_role_id

    @property
    def role_name(self):
        r"""Gets the role_name of this JobRolePermission.

        角色名称

        :return: The role_name of this JobRolePermission.
        :rtype: str
        """
        return self._role_name

    @role_name.setter
    def role_name(self, role_name):
        r"""Sets the role_name of this JobRolePermission.

        角色名称

        :param role_name: The role_name of this JobRolePermission.
        :type role_name: str
        """
        self._role_name = role_name

    @property
    def is_modify(self):
        r"""Gets the is_modify of this JobRolePermission.

        修改权限

        :return: The is_modify of this JobRolePermission.
        :rtype: bool
        """
        return self._is_modify

    @is_modify.setter
    def is_modify(self, is_modify):
        r"""Sets the is_modify of this JobRolePermission.

        修改权限

        :param is_modify: The is_modify of this JobRolePermission.
        :type is_modify: bool
        """
        self._is_modify = is_modify

    @property
    def is_delete(self):
        r"""Gets the is_delete of this JobRolePermission.

        删除权限

        :return: The is_delete of this JobRolePermission.
        :rtype: bool
        """
        return self._is_delete

    @is_delete.setter
    def is_delete(self, is_delete):
        r"""Sets the is_delete of this JobRolePermission.

        删除权限

        :param is_delete: The is_delete of this JobRolePermission.
        :type is_delete: bool
        """
        self._is_delete = is_delete

    @property
    def is_view(self):
        r"""Gets the is_view of this JobRolePermission.

        查看权限

        :return: The is_view of this JobRolePermission.
        :rtype: bool
        """
        return self._is_view

    @is_view.setter
    def is_view(self, is_view):
        r"""Sets the is_view of this JobRolePermission.

        查看权限

        :param is_view: The is_view of this JobRolePermission.
        :type is_view: bool
        """
        self._is_view = is_view

    @property
    def is_execute(self):
        r"""Gets the is_execute of this JobRolePermission.

        执行权限

        :return: The is_execute of this JobRolePermission.
        :rtype: bool
        """
        return self._is_execute

    @is_execute.setter
    def is_execute(self, is_execute):
        r"""Sets the is_execute of this JobRolePermission.

        执行权限

        :param is_execute: The is_execute of this JobRolePermission.
        :type is_execute: bool
        """
        self._is_execute = is_execute

    @property
    def is_copy(self):
        r"""Gets the is_copy of this JobRolePermission.

        复制权限

        :return: The is_copy of this JobRolePermission.
        :rtype: bool
        """
        return self._is_copy

    @is_copy.setter
    def is_copy(self, is_copy):
        r"""Sets the is_copy of this JobRolePermission.

        复制权限

        :param is_copy: The is_copy of this JobRolePermission.
        :type is_copy: bool
        """
        self._is_copy = is_copy

    @property
    def is_forbidden(self):
        r"""Gets the is_forbidden of this JobRolePermission.

        禁用权限

        :return: The is_forbidden of this JobRolePermission.
        :rtype: bool
        """
        return self._is_forbidden

    @is_forbidden.setter
    def is_forbidden(self, is_forbidden):
        r"""Sets the is_forbidden of this JobRolePermission.

        禁用权限

        :param is_forbidden: The is_forbidden of this JobRolePermission.
        :type is_forbidden: bool
        """
        self._is_forbidden = is_forbidden

    @property
    def is_manager(self):
        r"""Gets the is_manager of this JobRolePermission.

        管理权限

        :return: The is_manager of this JobRolePermission.
        :rtype: bool
        """
        return self._is_manager

    @is_manager.setter
    def is_manager(self, is_manager):
        r"""Sets the is_manager of this JobRolePermission.

        管理权限

        :param is_manager: The is_manager of this JobRolePermission.
        :type is_manager: bool
        """
        self._is_manager = is_manager

    @property
    def count(self):
        r"""Gets the count of this JobRolePermission.

        数量

        :return: The count of this JobRolePermission.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this JobRolePermission.

        数量

        :param count: The count of this JobRolePermission.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, JobRolePermission):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
