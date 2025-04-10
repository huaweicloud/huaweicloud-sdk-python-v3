# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetDatabaseUserPrivilegeReqV3:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'all_users': 'bool',
        'user_name': 'str',
        'readonly': 'bool'
    }

    attribute_map = {
        'all_users': 'all_users',
        'user_name': 'user_name',
        'readonly': 'readonly'
    }

    def __init__(self, all_users=None, user_name=None, readonly=None):
        r"""SetDatabaseUserPrivilegeReqV3

        The model defined in huaweicloud sdk

        :param all_users: 是否设置所有用户。
        :type all_users: bool
        :param user_name: 数据库用户名。
        :type user_name: str
        :param readonly: 是否为只读权限。
        :type readonly: bool
        """
        
        

        self._all_users = None
        self._user_name = None
        self._readonly = None
        self.discriminator = None

        self.all_users = all_users
        if user_name is not None:
            self.user_name = user_name
        self.readonly = readonly

    @property
    def all_users(self):
        r"""Gets the all_users of this SetDatabaseUserPrivilegeReqV3.

        是否设置所有用户。

        :return: The all_users of this SetDatabaseUserPrivilegeReqV3.
        :rtype: bool
        """
        return self._all_users

    @all_users.setter
    def all_users(self, all_users):
        r"""Sets the all_users of this SetDatabaseUserPrivilegeReqV3.

        是否设置所有用户。

        :param all_users: The all_users of this SetDatabaseUserPrivilegeReqV3.
        :type all_users: bool
        """
        self._all_users = all_users

    @property
    def user_name(self):
        r"""Gets the user_name of this SetDatabaseUserPrivilegeReqV3.

        数据库用户名。

        :return: The user_name of this SetDatabaseUserPrivilegeReqV3.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this SetDatabaseUserPrivilegeReqV3.

        数据库用户名。

        :param user_name: The user_name of this SetDatabaseUserPrivilegeReqV3.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def readonly(self):
        r"""Gets the readonly of this SetDatabaseUserPrivilegeReqV3.

        是否为只读权限。

        :return: The readonly of this SetDatabaseUserPrivilegeReqV3.
        :rtype: bool
        """
        return self._readonly

    @readonly.setter
    def readonly(self, readonly):
        r"""Sets the readonly of this SetDatabaseUserPrivilegeReqV3.

        是否为只读权限。

        :param readonly: The readonly of this SetDatabaseUserPrivilegeReqV3.
        :type readonly: bool
        """
        self._readonly = readonly

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
        if not isinstance(other, SetDatabaseUserPrivilegeReqV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
