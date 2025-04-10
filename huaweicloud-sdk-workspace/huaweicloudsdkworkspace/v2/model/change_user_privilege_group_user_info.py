# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeUserPrivilegeGroupUserInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_name': 'str',
        'user_privilege_group': 'str',
        'type': 'str'
    }

    attribute_map = {
        'user_name': 'user_name',
        'user_privilege_group': 'user_privilege_group',
        'type': 'type'
    }

    def __init__(self, user_name=None, user_privilege_group=None, type=None):
        r"""ChangeUserPrivilegeGroupUserInfo

        The model defined in huaweicloud sdk

        :param user_name: 桌面分配对象的名称，当type类型USER时填写用户名字；当type类型GROUP时填写用户组名称。
        :type user_name: str
        :param user_privilege_group: 桌面用户所属的用户组。 - sudo：Linux管理员组。 - default：Linux默认用户组。 - administrators：Windows管理员组。管理员拥有对该桌面的完全访问权，可以做任何需要的更改（禁用操作除外）。 - users：Windows标准用户组。标准用户可以使用大多数软件，并可以更改不影响其他用户的系统设置。
        :type user_privilege_group: str
        :param type: 对象类型，可选值为： - USER：用户。 - GROUP：用户组。
        :type type: str
        """
        
        

        self._user_name = None
        self._user_privilege_group = None
        self._type = None
        self.discriminator = None

        self.user_name = user_name
        if user_privilege_group is not None:
            self.user_privilege_group = user_privilege_group
        self.type = type

    @property
    def user_name(self):
        r"""Gets the user_name of this ChangeUserPrivilegeGroupUserInfo.

        桌面分配对象的名称，当type类型USER时填写用户名字；当type类型GROUP时填写用户组名称。

        :return: The user_name of this ChangeUserPrivilegeGroupUserInfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ChangeUserPrivilegeGroupUserInfo.

        桌面分配对象的名称，当type类型USER时填写用户名字；当type类型GROUP时填写用户组名称。

        :param user_name: The user_name of this ChangeUserPrivilegeGroupUserInfo.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def user_privilege_group(self):
        r"""Gets the user_privilege_group of this ChangeUserPrivilegeGroupUserInfo.

        桌面用户所属的用户组。 - sudo：Linux管理员组。 - default：Linux默认用户组。 - administrators：Windows管理员组。管理员拥有对该桌面的完全访问权，可以做任何需要的更改（禁用操作除外）。 - users：Windows标准用户组。标准用户可以使用大多数软件，并可以更改不影响其他用户的系统设置。

        :return: The user_privilege_group of this ChangeUserPrivilegeGroupUserInfo.
        :rtype: str
        """
        return self._user_privilege_group

    @user_privilege_group.setter
    def user_privilege_group(self, user_privilege_group):
        r"""Sets the user_privilege_group of this ChangeUserPrivilegeGroupUserInfo.

        桌面用户所属的用户组。 - sudo：Linux管理员组。 - default：Linux默认用户组。 - administrators：Windows管理员组。管理员拥有对该桌面的完全访问权，可以做任何需要的更改（禁用操作除外）。 - users：Windows标准用户组。标准用户可以使用大多数软件，并可以更改不影响其他用户的系统设置。

        :param user_privilege_group: The user_privilege_group of this ChangeUserPrivilegeGroupUserInfo.
        :type user_privilege_group: str
        """
        self._user_privilege_group = user_privilege_group

    @property
    def type(self):
        r"""Gets the type of this ChangeUserPrivilegeGroupUserInfo.

        对象类型，可选值为： - USER：用户。 - GROUP：用户组。

        :return: The type of this ChangeUserPrivilegeGroupUserInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ChangeUserPrivilegeGroupUserInfo.

        对象类型，可选值为： - USER：用户。 - GROUP：用户组。

        :param type: The type of this ChangeUserPrivilegeGroupUserInfo.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, ChangeUserPrivilegeGroupUserInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
