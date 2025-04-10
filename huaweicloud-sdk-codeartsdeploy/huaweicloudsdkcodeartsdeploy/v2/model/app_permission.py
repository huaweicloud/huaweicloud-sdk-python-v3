# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppPermission:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dev_role_id': 'str',
        'can_modify': 'bool',
        'can_delete': 'bool',
        'can_view': 'bool',
        'can_execute': 'bool',
        'can_copy': 'bool',
        'can_manage': 'bool',
        'can_create_env': 'bool',
        'can_disable': 'bool'
    }

    attribute_map = {
        'dev_role_id': 'dev_role_id',
        'can_modify': 'can_modify',
        'can_delete': 'can_delete',
        'can_view': 'can_view',
        'can_execute': 'can_execute',
        'can_copy': 'can_copy',
        'can_manage': 'can_manage',
        'can_create_env': 'can_create_env',
        'can_disable': 'can_disable'
    }

    def __init__(self, dev_role_id=None, can_modify=None, can_delete=None, can_view=None, can_execute=None, can_copy=None, can_manage=None, can_create_env=None, can_disable=None):
        r"""AppPermission

        The model defined in huaweicloud sdk

        :param dev_role_id: 角色id
        :type dev_role_id: str
        :param can_modify: 是否具有编辑权限
        :type can_modify: bool
        :param can_delete: 是否具有删除权限
        :type can_delete: bool
        :param can_view: 是否具有查看权限
        :type can_view: bool
        :param can_execute: 是否具有执行权限
        :type can_execute: bool
        :param can_copy: 是否具有复制权限
        :type can_copy: bool
        :param can_manage: 是否具有权限管理权限
        :type can_manage: bool
        :param can_create_env: 是否具有创建环境权限
        :type can_create_env: bool
        :param can_disable: 是否具有禁用权限
        :type can_disable: bool
        """
        
        

        self._dev_role_id = None
        self._can_modify = None
        self._can_delete = None
        self._can_view = None
        self._can_execute = None
        self._can_copy = None
        self._can_manage = None
        self._can_create_env = None
        self._can_disable = None
        self.discriminator = None

        self.dev_role_id = dev_role_id
        self.can_modify = can_modify
        self.can_delete = can_delete
        self.can_view = can_view
        self.can_execute = can_execute
        self.can_copy = can_copy
        self.can_manage = can_manage
        self.can_create_env = can_create_env
        self.can_disable = can_disable

    @property
    def dev_role_id(self):
        r"""Gets the dev_role_id of this AppPermission.

        角色id

        :return: The dev_role_id of this AppPermission.
        :rtype: str
        """
        return self._dev_role_id

    @dev_role_id.setter
    def dev_role_id(self, dev_role_id):
        r"""Sets the dev_role_id of this AppPermission.

        角色id

        :param dev_role_id: The dev_role_id of this AppPermission.
        :type dev_role_id: str
        """
        self._dev_role_id = dev_role_id

    @property
    def can_modify(self):
        r"""Gets the can_modify of this AppPermission.

        是否具有编辑权限

        :return: The can_modify of this AppPermission.
        :rtype: bool
        """
        return self._can_modify

    @can_modify.setter
    def can_modify(self, can_modify):
        r"""Sets the can_modify of this AppPermission.

        是否具有编辑权限

        :param can_modify: The can_modify of this AppPermission.
        :type can_modify: bool
        """
        self._can_modify = can_modify

    @property
    def can_delete(self):
        r"""Gets the can_delete of this AppPermission.

        是否具有删除权限

        :return: The can_delete of this AppPermission.
        :rtype: bool
        """
        return self._can_delete

    @can_delete.setter
    def can_delete(self, can_delete):
        r"""Sets the can_delete of this AppPermission.

        是否具有删除权限

        :param can_delete: The can_delete of this AppPermission.
        :type can_delete: bool
        """
        self._can_delete = can_delete

    @property
    def can_view(self):
        r"""Gets the can_view of this AppPermission.

        是否具有查看权限

        :return: The can_view of this AppPermission.
        :rtype: bool
        """
        return self._can_view

    @can_view.setter
    def can_view(self, can_view):
        r"""Sets the can_view of this AppPermission.

        是否具有查看权限

        :param can_view: The can_view of this AppPermission.
        :type can_view: bool
        """
        self._can_view = can_view

    @property
    def can_execute(self):
        r"""Gets the can_execute of this AppPermission.

        是否具有执行权限

        :return: The can_execute of this AppPermission.
        :rtype: bool
        """
        return self._can_execute

    @can_execute.setter
    def can_execute(self, can_execute):
        r"""Sets the can_execute of this AppPermission.

        是否具有执行权限

        :param can_execute: The can_execute of this AppPermission.
        :type can_execute: bool
        """
        self._can_execute = can_execute

    @property
    def can_copy(self):
        r"""Gets the can_copy of this AppPermission.

        是否具有复制权限

        :return: The can_copy of this AppPermission.
        :rtype: bool
        """
        return self._can_copy

    @can_copy.setter
    def can_copy(self, can_copy):
        r"""Sets the can_copy of this AppPermission.

        是否具有复制权限

        :param can_copy: The can_copy of this AppPermission.
        :type can_copy: bool
        """
        self._can_copy = can_copy

    @property
    def can_manage(self):
        r"""Gets the can_manage of this AppPermission.

        是否具有权限管理权限

        :return: The can_manage of this AppPermission.
        :rtype: bool
        """
        return self._can_manage

    @can_manage.setter
    def can_manage(self, can_manage):
        r"""Sets the can_manage of this AppPermission.

        是否具有权限管理权限

        :param can_manage: The can_manage of this AppPermission.
        :type can_manage: bool
        """
        self._can_manage = can_manage

    @property
    def can_create_env(self):
        r"""Gets the can_create_env of this AppPermission.

        是否具有创建环境权限

        :return: The can_create_env of this AppPermission.
        :rtype: bool
        """
        return self._can_create_env

    @can_create_env.setter
    def can_create_env(self, can_create_env):
        r"""Sets the can_create_env of this AppPermission.

        是否具有创建环境权限

        :param can_create_env: The can_create_env of this AppPermission.
        :type can_create_env: bool
        """
        self._can_create_env = can_create_env

    @property
    def can_disable(self):
        r"""Gets the can_disable of this AppPermission.

        是否具有禁用权限

        :return: The can_disable of this AppPermission.
        :rtype: bool
        """
        return self._can_disable

    @can_disable.setter
    def can_disable(self, can_disable):
        r"""Sets the can_disable of this AppPermission.

        是否具有禁用权限

        :param can_disable: The can_disable of this AppPermission.
        :type can_disable: bool
        """
        self._can_disable = can_disable

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
        if not isinstance(other, AppPermission):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
