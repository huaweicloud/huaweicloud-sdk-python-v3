# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDatabaseUserRequestBody:

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
        'user_pwd': 'str',
        'db_name': 'str',
        'roles': 'list[RolesOption]'
    }

    attribute_map = {
        'user_name': 'user_name',
        'user_pwd': 'user_pwd',
        'db_name': 'db_name',
        'roles': 'roles'
    }

    def __init__(self, user_name=None, user_pwd=None, db_name=None, roles=None):
        """CreateDatabaseUserRequestBody

        The model defined in huaweicloud sdk

        :param user_name: 数据库用户名称。 - 长度为1~64位，可以包含大写字母（A~Z）、小写字母（a~z）、数字（0~9）、中划线、下划线和点。
        :type user_name: str
        :param user_pwd: 数据库用户密码。 - 长度为8~32位，必须是大写字母（A~Z）、小写字母（a~z）、数字（0~9）、特殊字符~!@#%^*-_&#x3D;+?的组合。 - 建议您输入高强度密码，以提高安全性，防止出现密码被暴力破解等安全风险。
        :type user_pwd: str
        :param db_name: 新用户所在的数据库，默认为“admin”。 - 长度为1~64位，可以包含大写字母（A~Z）、小写字母（a~z）、数字（0~9）、下划线。
        :type db_name: str
        :param roles: 新用户所拥有的角色。
        :type roles: list[:class:`huaweicloudsdkdds.v3.RolesOption`]
        """
        
        

        self._user_name = None
        self._user_pwd = None
        self._db_name = None
        self._roles = None
        self.discriminator = None

        self.user_name = user_name
        self.user_pwd = user_pwd
        if db_name is not None:
            self.db_name = db_name
        self.roles = roles

    @property
    def user_name(self):
        """Gets the user_name of this CreateDatabaseUserRequestBody.

        数据库用户名称。 - 长度为1~64位，可以包含大写字母（A~Z）、小写字母（a~z）、数字（0~9）、中划线、下划线和点。

        :return: The user_name of this CreateDatabaseUserRequestBody.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this CreateDatabaseUserRequestBody.

        数据库用户名称。 - 长度为1~64位，可以包含大写字母（A~Z）、小写字母（a~z）、数字（0~9）、中划线、下划线和点。

        :param user_name: The user_name of this CreateDatabaseUserRequestBody.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def user_pwd(self):
        """Gets the user_pwd of this CreateDatabaseUserRequestBody.

        数据库用户密码。 - 长度为8~32位，必须是大写字母（A~Z）、小写字母（a~z）、数字（0~9）、特殊字符~!@#%^*-_=+?的组合。 - 建议您输入高强度密码，以提高安全性，防止出现密码被暴力破解等安全风险。

        :return: The user_pwd of this CreateDatabaseUserRequestBody.
        :rtype: str
        """
        return self._user_pwd

    @user_pwd.setter
    def user_pwd(self, user_pwd):
        """Sets the user_pwd of this CreateDatabaseUserRequestBody.

        数据库用户密码。 - 长度为8~32位，必须是大写字母（A~Z）、小写字母（a~z）、数字（0~9）、特殊字符~!@#%^*-_=+?的组合。 - 建议您输入高强度密码，以提高安全性，防止出现密码被暴力破解等安全风险。

        :param user_pwd: The user_pwd of this CreateDatabaseUserRequestBody.
        :type user_pwd: str
        """
        self._user_pwd = user_pwd

    @property
    def db_name(self):
        """Gets the db_name of this CreateDatabaseUserRequestBody.

        新用户所在的数据库，默认为“admin”。 - 长度为1~64位，可以包含大写字母（A~Z）、小写字母（a~z）、数字（0~9）、下划线。

        :return: The db_name of this CreateDatabaseUserRequestBody.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """Sets the db_name of this CreateDatabaseUserRequestBody.

        新用户所在的数据库，默认为“admin”。 - 长度为1~64位，可以包含大写字母（A~Z）、小写字母（a~z）、数字（0~9）、下划线。

        :param db_name: The db_name of this CreateDatabaseUserRequestBody.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def roles(self):
        """Gets the roles of this CreateDatabaseUserRequestBody.

        新用户所拥有的角色。

        :return: The roles of this CreateDatabaseUserRequestBody.
        :rtype: list[:class:`huaweicloudsdkdds.v3.RolesOption`]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this CreateDatabaseUserRequestBody.

        新用户所拥有的角色。

        :param roles: The roles of this CreateDatabaseUserRequestBody.
        :type roles: list[:class:`huaweicloudsdkdds.v3.RolesOption`]
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
        if not isinstance(other, CreateDatabaseUserRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
