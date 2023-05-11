# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DbUserPrivilegeRequest:

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
        'authorization_type': 'str',
        'privileges': 'list[str]'
    }

    attribute_map = {
        'user_name': 'user_name',
        'authorization_type': 'authorization_type',
        'privileges': 'privileges'
    }

    def __init__(self, user_name=None, authorization_type=None, privileges=None):
        """DbUserPrivilegeRequest

        The model defined in huaweicloud sdk

        :param user_name: 账号，数据库相关联的帐号
        :type user_name: str
        :param authorization_type: 授权SQL类型,枚举： 1、ROLE(支持对指定用户设置以下权限) 2、RECYCLING_ROLE(支持对指定用户回收以下权限) 3、SYSTEM_ROLE(支持对指定用户授予以下系统角色) 4、RECYCLING_SYSTEM_ROLE(支持对指定用户回收以下系统角色)
        :type authorization_type: str
        :param privileges: 支持用户设置的权限集合。 1、privilege_type为ROLE时需要使用,枚举： CREATEDB CREATEROLE LOGIN REPLICATION 2、privilege_type为RECYCLING_ROLE时需要使用,枚举： NOCREATEDB NOCREATEROLE NOLOGIN NOREPLICATION 3、privilege_type为SYSTEM_ROLE /RECYCLING_ SYSTEM_ROLE时需要使用,枚举： pg_monitor pg_signal_backend root
        :type privileges: list[str]
        """
        
        

        self._user_name = None
        self._authorization_type = None
        self._privileges = None
        self.discriminator = None

        self.user_name = user_name
        self.authorization_type = authorization_type
        self.privileges = privileges

    @property
    def user_name(self):
        """Gets the user_name of this DbUserPrivilegeRequest.

        账号，数据库相关联的帐号

        :return: The user_name of this DbUserPrivilegeRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this DbUserPrivilegeRequest.

        账号，数据库相关联的帐号

        :param user_name: The user_name of this DbUserPrivilegeRequest.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def authorization_type(self):
        """Gets the authorization_type of this DbUserPrivilegeRequest.

        授权SQL类型,枚举： 1、ROLE(支持对指定用户设置以下权限) 2、RECYCLING_ROLE(支持对指定用户回收以下权限) 3、SYSTEM_ROLE(支持对指定用户授予以下系统角色) 4、RECYCLING_SYSTEM_ROLE(支持对指定用户回收以下系统角色)

        :return: The authorization_type of this DbUserPrivilegeRequest.
        :rtype: str
        """
        return self._authorization_type

    @authorization_type.setter
    def authorization_type(self, authorization_type):
        """Sets the authorization_type of this DbUserPrivilegeRequest.

        授权SQL类型,枚举： 1、ROLE(支持对指定用户设置以下权限) 2、RECYCLING_ROLE(支持对指定用户回收以下权限) 3、SYSTEM_ROLE(支持对指定用户授予以下系统角色) 4、RECYCLING_SYSTEM_ROLE(支持对指定用户回收以下系统角色)

        :param authorization_type: The authorization_type of this DbUserPrivilegeRequest.
        :type authorization_type: str
        """
        self._authorization_type = authorization_type

    @property
    def privileges(self):
        """Gets the privileges of this DbUserPrivilegeRequest.

        支持用户设置的权限集合。 1、privilege_type为ROLE时需要使用,枚举： CREATEDB CREATEROLE LOGIN REPLICATION 2、privilege_type为RECYCLING_ROLE时需要使用,枚举： NOCREATEDB NOCREATEROLE NOLOGIN NOREPLICATION 3、privilege_type为SYSTEM_ROLE /RECYCLING_ SYSTEM_ROLE时需要使用,枚举： pg_monitor pg_signal_backend root

        :return: The privileges of this DbUserPrivilegeRequest.
        :rtype: list[str]
        """
        return self._privileges

    @privileges.setter
    def privileges(self, privileges):
        """Sets the privileges of this DbUserPrivilegeRequest.

        支持用户设置的权限集合。 1、privilege_type为ROLE时需要使用,枚举： CREATEDB CREATEROLE LOGIN REPLICATION 2、privilege_type为RECYCLING_ROLE时需要使用,枚举： NOCREATEDB NOCREATEROLE NOLOGIN NOREPLICATION 3、privilege_type为SYSTEM_ROLE /RECYCLING_ SYSTEM_ROLE时需要使用,枚举： pg_monitor pg_signal_backend root

        :param privileges: The privileges of this DbUserPrivilegeRequest.
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
        if not isinstance(other, DbUserPrivilegeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
