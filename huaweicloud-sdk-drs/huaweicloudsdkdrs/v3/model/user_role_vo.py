# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserRoleVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'role': 'str',
        'comment': 'str',
        'is_transfer': 'bool',
        'privileges': 'str',
        'inherits_roles': 'list[str]',
        'selected': 'bool'
    }

    attribute_map = {
        'role': 'role',
        'comment': 'comment',
        'is_transfer': 'is_transfer',
        'privileges': 'privileges',
        'inherits_roles': 'inherits_roles',
        'selected': 'selected'
    }

    def __init__(self, role=None, comment=None, is_transfer=None, privileges=None, inherits_roles=None, selected=None):
        """UserRoleVO

        The model defined in huaweicloud sdk

        :param role: 角色
        :type role: str
        :param comment: 说明
        :type comment: str
        :param is_transfer: 是否支持迁移。
        :type is_transfer: bool
        :param privileges: 权限
        :type privileges: str
        :param inherits_roles: 继承角色列表
        :type inherits_roles: list[str]
        :param selected: 是否选择。
        :type selected: bool
        """
        
        

        self._role = None
        self._comment = None
        self._is_transfer = None
        self._privileges = None
        self._inherits_roles = None
        self._selected = None
        self.discriminator = None

        self.role = role
        if comment is not None:
            self.comment = comment
        self.is_transfer = is_transfer
        self.privileges = privileges
        if inherits_roles is not None:
            self.inherits_roles = inherits_roles
        if selected is not None:
            self.selected = selected

    @property
    def role(self):
        """Gets the role of this UserRoleVO.

        角色

        :return: The role of this UserRoleVO.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this UserRoleVO.

        角色

        :param role: The role of this UserRoleVO.
        :type role: str
        """
        self._role = role

    @property
    def comment(self):
        """Gets the comment of this UserRoleVO.

        说明

        :return: The comment of this UserRoleVO.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this UserRoleVO.

        说明

        :param comment: The comment of this UserRoleVO.
        :type comment: str
        """
        self._comment = comment

    @property
    def is_transfer(self):
        """Gets the is_transfer of this UserRoleVO.

        是否支持迁移。

        :return: The is_transfer of this UserRoleVO.
        :rtype: bool
        """
        return self._is_transfer

    @is_transfer.setter
    def is_transfer(self, is_transfer):
        """Sets the is_transfer of this UserRoleVO.

        是否支持迁移。

        :param is_transfer: The is_transfer of this UserRoleVO.
        :type is_transfer: bool
        """
        self._is_transfer = is_transfer

    @property
    def privileges(self):
        """Gets the privileges of this UserRoleVO.

        权限

        :return: The privileges of this UserRoleVO.
        :rtype: str
        """
        return self._privileges

    @privileges.setter
    def privileges(self, privileges):
        """Sets the privileges of this UserRoleVO.

        权限

        :param privileges: The privileges of this UserRoleVO.
        :type privileges: str
        """
        self._privileges = privileges

    @property
    def inherits_roles(self):
        """Gets the inherits_roles of this UserRoleVO.

        继承角色列表

        :return: The inherits_roles of this UserRoleVO.
        :rtype: list[str]
        """
        return self._inherits_roles

    @inherits_roles.setter
    def inherits_roles(self, inherits_roles):
        """Sets the inherits_roles of this UserRoleVO.

        继承角色列表

        :param inherits_roles: The inherits_roles of this UserRoleVO.
        :type inherits_roles: list[str]
        """
        self._inherits_roles = inherits_roles

    @property
    def selected(self):
        """Gets the selected of this UserRoleVO.

        是否选择。

        :return: The selected of this UserRoleVO.
        :rtype: bool
        """
        return self._selected

    @selected.setter
    def selected(self, selected):
        """Sets the selected of this UserRoleVO.

        是否选择。

        :param selected: The selected of this UserRoleVO.
        :type selected: bool
        """
        self._selected = selected

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
        if not isinstance(other, UserRoleVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
