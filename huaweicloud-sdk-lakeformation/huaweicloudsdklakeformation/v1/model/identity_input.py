# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IdentityInput:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_names': 'list[str]',
        'groups': 'list[str]',
        'roles': 'list[str]'
    }

    attribute_map = {
        'user_names': 'user_names',
        'groups': 'groups',
        'roles': 'roles'
    }

    def __init__(self, user_names=None, groups=None, roles=None):
        r"""IdentityInput

        The model defined in huaweicloud sdk

        :param user_names: IAM用户
        :type user_names: list[str]
        :param groups: 用户组
        :type groups: list[str]
        :param roles: 角色
        :type roles: list[str]
        """
        
        

        self._user_names = None
        self._groups = None
        self._roles = None
        self.discriminator = None

        if user_names is not None:
            self.user_names = user_names
        if groups is not None:
            self.groups = groups
        if roles is not None:
            self.roles = roles

    @property
    def user_names(self):
        r"""Gets the user_names of this IdentityInput.

        IAM用户

        :return: The user_names of this IdentityInput.
        :rtype: list[str]
        """
        return self._user_names

    @user_names.setter
    def user_names(self, user_names):
        r"""Sets the user_names of this IdentityInput.

        IAM用户

        :param user_names: The user_names of this IdentityInput.
        :type user_names: list[str]
        """
        self._user_names = user_names

    @property
    def groups(self):
        r"""Gets the groups of this IdentityInput.

        用户组

        :return: The groups of this IdentityInput.
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        r"""Sets the groups of this IdentityInput.

        用户组

        :param groups: The groups of this IdentityInput.
        :type groups: list[str]
        """
        self._groups = groups

    @property
    def roles(self):
        r"""Gets the roles of this IdentityInput.

        角色

        :return: The roles of this IdentityInput.
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        r"""Sets the roles of this IdentityInput.

        角色

        :param roles: The roles of this IdentityInput.
        :type roles: list[str]
        """
        self._roles = roles

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
        if not isinstance(other, IdentityInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
