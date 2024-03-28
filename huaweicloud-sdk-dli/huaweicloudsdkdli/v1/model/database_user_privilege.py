# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DatabaseUserPrivilege:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_admin': 'bool',
        'user_name': 'str',
        'privileges': 'list[str]'
    }

    attribute_map = {
        'is_admin': 'is_admin',
        'user_name': 'user_name',
        'privileges': 'privileges'
    }

    def __init__(self, is_admin=None, user_name=None, privileges=None):
        """DatabaseUserPrivilege

        The model defined in huaweicloud sdk

        :param is_admin: 判断用户是否为管理员。
        :type is_admin: bool
        :param user_name: 用户名称，即该用户在当前数据库上有权限。
        :type user_name: str
        :param privileges: 该用户在数据库上的权限。
        :type privileges: list[str]
        """
        
        

        self._is_admin = None
        self._user_name = None
        self._privileges = None
        self.discriminator = None

        if is_admin is not None:
            self.is_admin = is_admin
        if user_name is not None:
            self.user_name = user_name
        if privileges is not None:
            self.privileges = privileges

    @property
    def is_admin(self):
        """Gets the is_admin of this DatabaseUserPrivilege.

        判断用户是否为管理员。

        :return: The is_admin of this DatabaseUserPrivilege.
        :rtype: bool
        """
        return self._is_admin

    @is_admin.setter
    def is_admin(self, is_admin):
        """Sets the is_admin of this DatabaseUserPrivilege.

        判断用户是否为管理员。

        :param is_admin: The is_admin of this DatabaseUserPrivilege.
        :type is_admin: bool
        """
        self._is_admin = is_admin

    @property
    def user_name(self):
        """Gets the user_name of this DatabaseUserPrivilege.

        用户名称，即该用户在当前数据库上有权限。

        :return: The user_name of this DatabaseUserPrivilege.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this DatabaseUserPrivilege.

        用户名称，即该用户在当前数据库上有权限。

        :param user_name: The user_name of this DatabaseUserPrivilege.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def privileges(self):
        """Gets the privileges of this DatabaseUserPrivilege.

        该用户在数据库上的权限。

        :return: The privileges of this DatabaseUserPrivilege.
        :rtype: list[str]
        """
        return self._privileges

    @privileges.setter
    def privileges(self, privileges):
        """Sets the privileges of this DatabaseUserPrivilege.

        该用户在数据库上的权限。

        :param privileges: The privileges of this DatabaseUserPrivilege.
        :type privileges: list[str]
        """
        self._privileges = privileges

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
        if not isinstance(other, DatabaseUserPrivilege):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
