# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApplicationPermissionVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'can_modify': 'bool',
        'can_delete': 'bool',
        'can_view': 'bool',
        'can_execute': 'bool',
        'can_copy': 'bool',
        'can_manage': 'bool',
        'can_create_env': 'bool',
        'can_disable': 'bool',
        'name': 'str',
        'region': 'str',
        'role_id': 'str',
        'role_type': 'str'
    }

    attribute_map = {
        'can_modify': 'can_modify',
        'can_delete': 'can_delete',
        'can_view': 'can_view',
        'can_execute': 'can_execute',
        'can_copy': 'can_copy',
        'can_manage': 'can_manage',
        'can_create_env': 'can_create_env',
        'can_disable': 'can_disable',
        'name': 'name',
        'region': 'region',
        'role_id': 'role_id',
        'role_type': 'role_type'
    }

    def __init__(self, can_modify=None, can_delete=None, can_view=None, can_execute=None, can_copy=None, can_manage=None, can_create_env=None, can_disable=None, name=None, region=None, role_id=None, role_type=None):
        r"""ApplicationPermissionVO

        The model defined in huaweicloud sdk

        :param can_modify: 是否有编辑权限
        :type can_modify: bool
        :param can_delete: 是否有删除的权限
        :type can_delete: bool
        :param can_view: 是否有查看权限
        :type can_view: bool
        :param can_execute: 是否有执行权限
        :type can_execute: bool
        :param can_copy: 是否有复制权限
        :type can_copy: bool
        :param can_manage: 是否有管理权限，包含增删改查执行以及权限修改
        :type can_manage: bool
        :param can_create_env: 是否有新建环境权限
        :type can_create_env: bool
        :param can_disable: 是否有禁用权限
        :type can_disable: bool
        :param name: 角色名称
        :type name: str
        :param region: 局点信息
        :type region: str
        :param role_id: 角色id
        :type role_id: str
        :param role_type: 角色类型， app-creator： 应用创建者； project： 项目管理员；template-customized-inst：系统角色； template-project-customized、project-customized：自定义角色
        :type role_type: str
        """
        
        

        self._can_modify = None
        self._can_delete = None
        self._can_view = None
        self._can_execute = None
        self._can_copy = None
        self._can_manage = None
        self._can_create_env = None
        self._can_disable = None
        self._name = None
        self._region = None
        self._role_id = None
        self._role_type = None
        self.discriminator = None

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
        if name is not None:
            self.name = name
        if region is not None:
            self.region = region
        if role_id is not None:
            self.role_id = role_id
        if role_type is not None:
            self.role_type = role_type

    @property
    def can_modify(self):
        r"""Gets the can_modify of this ApplicationPermissionVO.

        是否有编辑权限

        :return: The can_modify of this ApplicationPermissionVO.
        :rtype: bool
        """
        return self._can_modify

    @can_modify.setter
    def can_modify(self, can_modify):
        r"""Sets the can_modify of this ApplicationPermissionVO.

        是否有编辑权限

        :param can_modify: The can_modify of this ApplicationPermissionVO.
        :type can_modify: bool
        """
        self._can_modify = can_modify

    @property
    def can_delete(self):
        r"""Gets the can_delete of this ApplicationPermissionVO.

        是否有删除的权限

        :return: The can_delete of this ApplicationPermissionVO.
        :rtype: bool
        """
        return self._can_delete

    @can_delete.setter
    def can_delete(self, can_delete):
        r"""Sets the can_delete of this ApplicationPermissionVO.

        是否有删除的权限

        :param can_delete: The can_delete of this ApplicationPermissionVO.
        :type can_delete: bool
        """
        self._can_delete = can_delete

    @property
    def can_view(self):
        r"""Gets the can_view of this ApplicationPermissionVO.

        是否有查看权限

        :return: The can_view of this ApplicationPermissionVO.
        :rtype: bool
        """
        return self._can_view

    @can_view.setter
    def can_view(self, can_view):
        r"""Sets the can_view of this ApplicationPermissionVO.

        是否有查看权限

        :param can_view: The can_view of this ApplicationPermissionVO.
        :type can_view: bool
        """
        self._can_view = can_view

    @property
    def can_execute(self):
        r"""Gets the can_execute of this ApplicationPermissionVO.

        是否有执行权限

        :return: The can_execute of this ApplicationPermissionVO.
        :rtype: bool
        """
        return self._can_execute

    @can_execute.setter
    def can_execute(self, can_execute):
        r"""Sets the can_execute of this ApplicationPermissionVO.

        是否有执行权限

        :param can_execute: The can_execute of this ApplicationPermissionVO.
        :type can_execute: bool
        """
        self._can_execute = can_execute

    @property
    def can_copy(self):
        r"""Gets the can_copy of this ApplicationPermissionVO.

        是否有复制权限

        :return: The can_copy of this ApplicationPermissionVO.
        :rtype: bool
        """
        return self._can_copy

    @can_copy.setter
    def can_copy(self, can_copy):
        r"""Sets the can_copy of this ApplicationPermissionVO.

        是否有复制权限

        :param can_copy: The can_copy of this ApplicationPermissionVO.
        :type can_copy: bool
        """
        self._can_copy = can_copy

    @property
    def can_manage(self):
        r"""Gets the can_manage of this ApplicationPermissionVO.

        是否有管理权限，包含增删改查执行以及权限修改

        :return: The can_manage of this ApplicationPermissionVO.
        :rtype: bool
        """
        return self._can_manage

    @can_manage.setter
    def can_manage(self, can_manage):
        r"""Sets the can_manage of this ApplicationPermissionVO.

        是否有管理权限，包含增删改查执行以及权限修改

        :param can_manage: The can_manage of this ApplicationPermissionVO.
        :type can_manage: bool
        """
        self._can_manage = can_manage

    @property
    def can_create_env(self):
        r"""Gets the can_create_env of this ApplicationPermissionVO.

        是否有新建环境权限

        :return: The can_create_env of this ApplicationPermissionVO.
        :rtype: bool
        """
        return self._can_create_env

    @can_create_env.setter
    def can_create_env(self, can_create_env):
        r"""Sets the can_create_env of this ApplicationPermissionVO.

        是否有新建环境权限

        :param can_create_env: The can_create_env of this ApplicationPermissionVO.
        :type can_create_env: bool
        """
        self._can_create_env = can_create_env

    @property
    def can_disable(self):
        r"""Gets the can_disable of this ApplicationPermissionVO.

        是否有禁用权限

        :return: The can_disable of this ApplicationPermissionVO.
        :rtype: bool
        """
        return self._can_disable

    @can_disable.setter
    def can_disable(self, can_disable):
        r"""Sets the can_disable of this ApplicationPermissionVO.

        是否有禁用权限

        :param can_disable: The can_disable of this ApplicationPermissionVO.
        :type can_disable: bool
        """
        self._can_disable = can_disable

    @property
    def name(self):
        r"""Gets the name of this ApplicationPermissionVO.

        角色名称

        :return: The name of this ApplicationPermissionVO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ApplicationPermissionVO.

        角色名称

        :param name: The name of this ApplicationPermissionVO.
        :type name: str
        """
        self._name = name

    @property
    def region(self):
        r"""Gets the region of this ApplicationPermissionVO.

        局点信息

        :return: The region of this ApplicationPermissionVO.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ApplicationPermissionVO.

        局点信息

        :param region: The region of this ApplicationPermissionVO.
        :type region: str
        """
        self._region = region

    @property
    def role_id(self):
        r"""Gets the role_id of this ApplicationPermissionVO.

        角色id

        :return: The role_id of this ApplicationPermissionVO.
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        r"""Sets the role_id of this ApplicationPermissionVO.

        角色id

        :param role_id: The role_id of this ApplicationPermissionVO.
        :type role_id: str
        """
        self._role_id = role_id

    @property
    def role_type(self):
        r"""Gets the role_type of this ApplicationPermissionVO.

        角色类型， app-creator： 应用创建者； project： 项目管理员；template-customized-inst：系统角色； template-project-customized、project-customized：自定义角色

        :return: The role_type of this ApplicationPermissionVO.
        :rtype: str
        """
        return self._role_type

    @role_type.setter
    def role_type(self, role_type):
        r"""Sets the role_type of this ApplicationPermissionVO.

        角色类型， app-creator： 应用创建者； project： 项目管理员；template-customized-inst：系统角色； template-project-customized、project-customized：自定义角色

        :param role_type: The role_type of this ApplicationPermissionVO.
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
        if not isinstance(other, ApplicationPermissionVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
