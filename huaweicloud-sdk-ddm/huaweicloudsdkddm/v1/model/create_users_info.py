# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateUsersInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'password': 'str',
        'base_authority': 'list[str]',
        'description': 'str',
        'databases': 'list[CreateUsersDatabases]'
    }

    attribute_map = {
        'name': 'name',
        'password': 'password',
        'base_authority': 'base_authority',
        'description': 'description',
        'databases': 'databases'
    }

    def __init__(self, name=None, password=None, base_authority=None, description=None, databases=None):
        r"""CreateUsersInfo

        The model defined in huaweicloud sdk

        :param name: DDM实例帐号名称，命名要求如下。  - 长度为1-32个字符。 - 必须以字母开头。 - 可以包含字母，数字、下划线，不能包含其它特殊字符。
        :type name: str
        :param password: DDM实例帐号密码。
        :type password: str
        :param base_authority: DDM实例帐号的基础权限。  取值为：CREATE、DROP、ALTER、INDEX、INSERT、DELETE、UPDATE、SELECT
        :type base_authority: list[str]
        :param description: DDM实例帐号的描述，最大长度不能超过256。默认值为空。
        :type description: str
        :param databases: 关联的逻辑库的集合。 databases字段可以省略，即创建用户时可以不关联逻辑库。
        :type databases: list[:class:`huaweicloudsdkddm.v1.CreateUsersDatabases`]
        """
        
        

        self._name = None
        self._password = None
        self._base_authority = None
        self._description = None
        self._databases = None
        self.discriminator = None

        self.name = name
        self.password = password
        self.base_authority = base_authority
        if description is not None:
            self.description = description
        if databases is not None:
            self.databases = databases

    @property
    def name(self):
        r"""Gets the name of this CreateUsersInfo.

        DDM实例帐号名称，命名要求如下。  - 长度为1-32个字符。 - 必须以字母开头。 - 可以包含字母，数字、下划线，不能包含其它特殊字符。

        :return: The name of this CreateUsersInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateUsersInfo.

        DDM实例帐号名称，命名要求如下。  - 长度为1-32个字符。 - 必须以字母开头。 - 可以包含字母，数字、下划线，不能包含其它特殊字符。

        :param name: The name of this CreateUsersInfo.
        :type name: str
        """
        self._name = name

    @property
    def password(self):
        r"""Gets the password of this CreateUsersInfo.

        DDM实例帐号密码。

        :return: The password of this CreateUsersInfo.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        r"""Sets the password of this CreateUsersInfo.

        DDM实例帐号密码。

        :param password: The password of this CreateUsersInfo.
        :type password: str
        """
        self._password = password

    @property
    def base_authority(self):
        r"""Gets the base_authority of this CreateUsersInfo.

        DDM实例帐号的基础权限。  取值为：CREATE、DROP、ALTER、INDEX、INSERT、DELETE、UPDATE、SELECT

        :return: The base_authority of this CreateUsersInfo.
        :rtype: list[str]
        """
        return self._base_authority

    @base_authority.setter
    def base_authority(self, base_authority):
        r"""Sets the base_authority of this CreateUsersInfo.

        DDM实例帐号的基础权限。  取值为：CREATE、DROP、ALTER、INDEX、INSERT、DELETE、UPDATE、SELECT

        :param base_authority: The base_authority of this CreateUsersInfo.
        :type base_authority: list[str]
        """
        self._base_authority = base_authority

    @property
    def description(self):
        r"""Gets the description of this CreateUsersInfo.

        DDM实例帐号的描述，最大长度不能超过256。默认值为空。

        :return: The description of this CreateUsersInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateUsersInfo.

        DDM实例帐号的描述，最大长度不能超过256。默认值为空。

        :param description: The description of this CreateUsersInfo.
        :type description: str
        """
        self._description = description

    @property
    def databases(self):
        r"""Gets the databases of this CreateUsersInfo.

        关联的逻辑库的集合。 databases字段可以省略，即创建用户时可以不关联逻辑库。

        :return: The databases of this CreateUsersInfo.
        :rtype: list[:class:`huaweicloudsdkddm.v1.CreateUsersDatabases`]
        """
        return self._databases

    @databases.setter
    def databases(self, databases):
        r"""Sets the databases of this CreateUsersInfo.

        关联的逻辑库的集合。 databases字段可以省略，即创建用户时可以不关联逻辑库。

        :param databases: The databases of this CreateUsersInfo.
        :type databases: list[:class:`huaweicloudsdkddm.v1.CreateUsersDatabases`]
        """
        self._databases = databases

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
        if not isinstance(other, CreateUsersInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
