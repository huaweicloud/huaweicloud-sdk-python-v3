# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'accesses': 'list[PolicyItemAccess]',
        'conditions': 'list[PolicyItemCondition]',
        'delegate_admin': 'bool',
        'groups': 'list[str]',
        'roles': 'list[str]',
        'users': 'list[str]'
    }

    attribute_map = {
        'accesses': 'accesses',
        'conditions': 'conditions',
        'delegate_admin': 'delegate_admin',
        'groups': 'groups',
        'roles': 'roles',
        'users': 'users'
    }

    def __init__(self, accesses=None, conditions=None, delegate_admin=None, groups=None, roles=None, users=None):
        """PolicyItem

        The model defined in huaweicloud sdk

        :param accesses: 访问控制数据
        :type accesses: list[:class:`huaweicloudsdklakeformation.v1.PolicyItemAccess`]
        :param conditions: 条件
        :type conditions: list[:class:`huaweicloudsdklakeformation.v1.PolicyItemCondition`]
        :param delegate_admin: 是否传递
        :type delegate_admin: bool
        :param groups: 组
        :type groups: list[str]
        :param roles: 角色
        :type roles: list[str]
        :param users: 用户
        :type users: list[str]
        """
        
        

        self._accesses = None
        self._conditions = None
        self._delegate_admin = None
        self._groups = None
        self._roles = None
        self._users = None
        self.discriminator = None

        if accesses is not None:
            self.accesses = accesses
        if conditions is not None:
            self.conditions = conditions
        if delegate_admin is not None:
            self.delegate_admin = delegate_admin
        if groups is not None:
            self.groups = groups
        if roles is not None:
            self.roles = roles
        if users is not None:
            self.users = users

    @property
    def accesses(self):
        """Gets the accesses of this PolicyItem.

        访问控制数据

        :return: The accesses of this PolicyItem.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.PolicyItemAccess`]
        """
        return self._accesses

    @accesses.setter
    def accesses(self, accesses):
        """Sets the accesses of this PolicyItem.

        访问控制数据

        :param accesses: The accesses of this PolicyItem.
        :type accesses: list[:class:`huaweicloudsdklakeformation.v1.PolicyItemAccess`]
        """
        self._accesses = accesses

    @property
    def conditions(self):
        """Gets the conditions of this PolicyItem.

        条件

        :return: The conditions of this PolicyItem.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.PolicyItemCondition`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this PolicyItem.

        条件

        :param conditions: The conditions of this PolicyItem.
        :type conditions: list[:class:`huaweicloudsdklakeformation.v1.PolicyItemCondition`]
        """
        self._conditions = conditions

    @property
    def delegate_admin(self):
        """Gets the delegate_admin of this PolicyItem.

        是否传递

        :return: The delegate_admin of this PolicyItem.
        :rtype: bool
        """
        return self._delegate_admin

    @delegate_admin.setter
    def delegate_admin(self, delegate_admin):
        """Sets the delegate_admin of this PolicyItem.

        是否传递

        :param delegate_admin: The delegate_admin of this PolicyItem.
        :type delegate_admin: bool
        """
        self._delegate_admin = delegate_admin

    @property
    def groups(self):
        """Gets the groups of this PolicyItem.

        组

        :return: The groups of this PolicyItem.
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this PolicyItem.

        组

        :param groups: The groups of this PolicyItem.
        :type groups: list[str]
        """
        self._groups = groups

    @property
    def roles(self):
        """Gets the roles of this PolicyItem.

        角色

        :return: The roles of this PolicyItem.
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this PolicyItem.

        角色

        :param roles: The roles of this PolicyItem.
        :type roles: list[str]
        """
        self._roles = roles

    @property
    def users(self):
        """Gets the users of this PolicyItem.

        用户

        :return: The users of this PolicyItem.
        :rtype: list[str]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this PolicyItem.

        用户

        :param users: The users of this PolicyItem.
        :type users: list[str]
        """
        self._users = users

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
        if not isinstance(other, PolicyItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
