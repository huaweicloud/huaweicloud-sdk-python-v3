# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApigWorkspaceUserDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'int',
        'user_ids': 'list[ApigIamUserDto]',
        'groups': 'list[Group]',
        'roles_ids': 'list[ApigRole]'
    }

    attribute_map = {
        'type': 'type',
        'user_ids': 'user_ids',
        'groups': 'groups',
        'roles_ids': 'roles_ids'
    }

    def __init__(self, type=None, user_ids=None, groups=None, roles_ids=None):
        """ApigWorkspaceUserDto

        The model defined in huaweicloud sdk

        :param type: 用户类型，0:添加用户;1:添加用户组
        :type type: int
        :param user_ids: 用户列表信息
        :type user_ids: list[:class:`huaweicloudsdkdataartsstudio.v1.ApigIamUserDto`]
        :param groups: 用户组列表信息
        :type groups: list[:class:`huaweicloudsdkdataartsstudio.v1.Group`]
        :param roles_ids: 空间角色列表
        :type roles_ids: list[:class:`huaweicloudsdkdataartsstudio.v1.ApigRole`]
        """
        
        

        self._type = None
        self._user_ids = None
        self._groups = None
        self._roles_ids = None
        self.discriminator = None

        self.type = type
        if user_ids is not None:
            self.user_ids = user_ids
        if groups is not None:
            self.groups = groups
        self.roles_ids = roles_ids

    @property
    def type(self):
        """Gets the type of this ApigWorkspaceUserDto.

        用户类型，0:添加用户;1:添加用户组

        :return: The type of this ApigWorkspaceUserDto.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ApigWorkspaceUserDto.

        用户类型，0:添加用户;1:添加用户组

        :param type: The type of this ApigWorkspaceUserDto.
        :type type: int
        """
        self._type = type

    @property
    def user_ids(self):
        """Gets the user_ids of this ApigWorkspaceUserDto.

        用户列表信息

        :return: The user_ids of this ApigWorkspaceUserDto.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.ApigIamUserDto`]
        """
        return self._user_ids

    @user_ids.setter
    def user_ids(self, user_ids):
        """Sets the user_ids of this ApigWorkspaceUserDto.

        用户列表信息

        :param user_ids: The user_ids of this ApigWorkspaceUserDto.
        :type user_ids: list[:class:`huaweicloudsdkdataartsstudio.v1.ApigIamUserDto`]
        """
        self._user_ids = user_ids

    @property
    def groups(self):
        """Gets the groups of this ApigWorkspaceUserDto.

        用户组列表信息

        :return: The groups of this ApigWorkspaceUserDto.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.Group`]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this ApigWorkspaceUserDto.

        用户组列表信息

        :param groups: The groups of this ApigWorkspaceUserDto.
        :type groups: list[:class:`huaweicloudsdkdataartsstudio.v1.Group`]
        """
        self._groups = groups

    @property
    def roles_ids(self):
        """Gets the roles_ids of this ApigWorkspaceUserDto.

        空间角色列表

        :return: The roles_ids of this ApigWorkspaceUserDto.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.ApigRole`]
        """
        return self._roles_ids

    @roles_ids.setter
    def roles_ids(self, roles_ids):
        """Sets the roles_ids of this ApigWorkspaceUserDto.

        空间角色列表

        :param roles_ids: The roles_ids of this ApigWorkspaceUserDto.
        :type roles_ids: list[:class:`huaweicloudsdkdataartsstudio.v1.ApigRole`]
        """
        self._roles_ids = roles_ids

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
        if not isinstance(other, ApigWorkspaceUserDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
