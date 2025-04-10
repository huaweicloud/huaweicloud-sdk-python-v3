# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GaussDBListDatabaseRolesPriv:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rolsuper': 'bool',
        'rolinherit': 'bool',
        'rolcreaterole': 'bool',
        'rolcreatedb': 'bool',
        'rolcanlogin': 'bool',
        'rolconnlimit': 'int',
        'rolreplication': 'bool',
        'rolbypassrls': 'bool',
        'rolpassworddeadline': 'str'
    }

    attribute_map = {
        'rolsuper': 'rolsuper',
        'rolinherit': 'rolinherit',
        'rolcreaterole': 'rolcreaterole',
        'rolcreatedb': 'rolcreatedb',
        'rolcanlogin': 'rolcanlogin',
        'rolconnlimit': 'rolconnlimit',
        'rolreplication': 'rolreplication',
        'rolbypassrls': 'rolbypassrls',
        'rolpassworddeadline': 'rolpassworddeadline'
    }

    def __init__(self, rolsuper=None, rolinherit=None, rolcreaterole=None, rolcreatedb=None, rolcanlogin=None, rolconnlimit=None, rolreplication=None, rolbypassrls=None, rolpassworddeadline=None):
        r"""GaussDBListDatabaseRolesPriv

        The model defined in huaweicloud sdk

        :param rolsuper: 用户/角色是否具有管理员权限。
        :type rolsuper: bool
        :param rolinherit: 用户/角色是否自动继承其所属角色的权限。
        :type rolinherit: bool
        :param rolcreaterole: 用户/角色是否支持创建其他子用户。
        :type rolcreaterole: bool
        :param rolcreatedb: 用户/角色是否可以创建数据库。
        :type rolcreatedb: bool
        :param rolcanlogin: 用户/角色是否可以登录数据库。
        :type rolcanlogin: bool
        :param rolconnlimit: 用户/角色连接实例的最大并发连接数。-1表示没有限制。
        :type rolconnlimit: int
        :param rolreplication: 用户/角色是否属于复制角色。
        :type rolreplication: bool
        :param rolbypassrls: 用户/角色是否绕过每个行级安全策略。
        :type rolbypassrls: bool
        :param rolpassworddeadline: 用户/角色密码过期时间。
        :type rolpassworddeadline: str
        """
        
        

        self._rolsuper = None
        self._rolinherit = None
        self._rolcreaterole = None
        self._rolcreatedb = None
        self._rolcanlogin = None
        self._rolconnlimit = None
        self._rolreplication = None
        self._rolbypassrls = None
        self._rolpassworddeadline = None
        self.discriminator = None

        if rolsuper is not None:
            self.rolsuper = rolsuper
        if rolinherit is not None:
            self.rolinherit = rolinherit
        if rolcreaterole is not None:
            self.rolcreaterole = rolcreaterole
        if rolcreatedb is not None:
            self.rolcreatedb = rolcreatedb
        if rolcanlogin is not None:
            self.rolcanlogin = rolcanlogin
        if rolconnlimit is not None:
            self.rolconnlimit = rolconnlimit
        if rolreplication is not None:
            self.rolreplication = rolreplication
        if rolbypassrls is not None:
            self.rolbypassrls = rolbypassrls
        if rolpassworddeadline is not None:
            self.rolpassworddeadline = rolpassworddeadline

    @property
    def rolsuper(self):
        r"""Gets the rolsuper of this GaussDBListDatabaseRolesPriv.

        用户/角色是否具有管理员权限。

        :return: The rolsuper of this GaussDBListDatabaseRolesPriv.
        :rtype: bool
        """
        return self._rolsuper

    @rolsuper.setter
    def rolsuper(self, rolsuper):
        r"""Sets the rolsuper of this GaussDBListDatabaseRolesPriv.

        用户/角色是否具有管理员权限。

        :param rolsuper: The rolsuper of this GaussDBListDatabaseRolesPriv.
        :type rolsuper: bool
        """
        self._rolsuper = rolsuper

    @property
    def rolinherit(self):
        r"""Gets the rolinherit of this GaussDBListDatabaseRolesPriv.

        用户/角色是否自动继承其所属角色的权限。

        :return: The rolinherit of this GaussDBListDatabaseRolesPriv.
        :rtype: bool
        """
        return self._rolinherit

    @rolinherit.setter
    def rolinherit(self, rolinherit):
        r"""Sets the rolinherit of this GaussDBListDatabaseRolesPriv.

        用户/角色是否自动继承其所属角色的权限。

        :param rolinherit: The rolinherit of this GaussDBListDatabaseRolesPriv.
        :type rolinherit: bool
        """
        self._rolinherit = rolinherit

    @property
    def rolcreaterole(self):
        r"""Gets the rolcreaterole of this GaussDBListDatabaseRolesPriv.

        用户/角色是否支持创建其他子用户。

        :return: The rolcreaterole of this GaussDBListDatabaseRolesPriv.
        :rtype: bool
        """
        return self._rolcreaterole

    @rolcreaterole.setter
    def rolcreaterole(self, rolcreaterole):
        r"""Sets the rolcreaterole of this GaussDBListDatabaseRolesPriv.

        用户/角色是否支持创建其他子用户。

        :param rolcreaterole: The rolcreaterole of this GaussDBListDatabaseRolesPriv.
        :type rolcreaterole: bool
        """
        self._rolcreaterole = rolcreaterole

    @property
    def rolcreatedb(self):
        r"""Gets the rolcreatedb of this GaussDBListDatabaseRolesPriv.

        用户/角色是否可以创建数据库。

        :return: The rolcreatedb of this GaussDBListDatabaseRolesPriv.
        :rtype: bool
        """
        return self._rolcreatedb

    @rolcreatedb.setter
    def rolcreatedb(self, rolcreatedb):
        r"""Sets the rolcreatedb of this GaussDBListDatabaseRolesPriv.

        用户/角色是否可以创建数据库。

        :param rolcreatedb: The rolcreatedb of this GaussDBListDatabaseRolesPriv.
        :type rolcreatedb: bool
        """
        self._rolcreatedb = rolcreatedb

    @property
    def rolcanlogin(self):
        r"""Gets the rolcanlogin of this GaussDBListDatabaseRolesPriv.

        用户/角色是否可以登录数据库。

        :return: The rolcanlogin of this GaussDBListDatabaseRolesPriv.
        :rtype: bool
        """
        return self._rolcanlogin

    @rolcanlogin.setter
    def rolcanlogin(self, rolcanlogin):
        r"""Sets the rolcanlogin of this GaussDBListDatabaseRolesPriv.

        用户/角色是否可以登录数据库。

        :param rolcanlogin: The rolcanlogin of this GaussDBListDatabaseRolesPriv.
        :type rolcanlogin: bool
        """
        self._rolcanlogin = rolcanlogin

    @property
    def rolconnlimit(self):
        r"""Gets the rolconnlimit of this GaussDBListDatabaseRolesPriv.

        用户/角色连接实例的最大并发连接数。-1表示没有限制。

        :return: The rolconnlimit of this GaussDBListDatabaseRolesPriv.
        :rtype: int
        """
        return self._rolconnlimit

    @rolconnlimit.setter
    def rolconnlimit(self, rolconnlimit):
        r"""Sets the rolconnlimit of this GaussDBListDatabaseRolesPriv.

        用户/角色连接实例的最大并发连接数。-1表示没有限制。

        :param rolconnlimit: The rolconnlimit of this GaussDBListDatabaseRolesPriv.
        :type rolconnlimit: int
        """
        self._rolconnlimit = rolconnlimit

    @property
    def rolreplication(self):
        r"""Gets the rolreplication of this GaussDBListDatabaseRolesPriv.

        用户/角色是否属于复制角色。

        :return: The rolreplication of this GaussDBListDatabaseRolesPriv.
        :rtype: bool
        """
        return self._rolreplication

    @rolreplication.setter
    def rolreplication(self, rolreplication):
        r"""Sets the rolreplication of this GaussDBListDatabaseRolesPriv.

        用户/角色是否属于复制角色。

        :param rolreplication: The rolreplication of this GaussDBListDatabaseRolesPriv.
        :type rolreplication: bool
        """
        self._rolreplication = rolreplication

    @property
    def rolbypassrls(self):
        r"""Gets the rolbypassrls of this GaussDBListDatabaseRolesPriv.

        用户/角色是否绕过每个行级安全策略。

        :return: The rolbypassrls of this GaussDBListDatabaseRolesPriv.
        :rtype: bool
        """
        return self._rolbypassrls

    @rolbypassrls.setter
    def rolbypassrls(self, rolbypassrls):
        r"""Sets the rolbypassrls of this GaussDBListDatabaseRolesPriv.

        用户/角色是否绕过每个行级安全策略。

        :param rolbypassrls: The rolbypassrls of this GaussDBListDatabaseRolesPriv.
        :type rolbypassrls: bool
        """
        self._rolbypassrls = rolbypassrls

    @property
    def rolpassworddeadline(self):
        r"""Gets the rolpassworddeadline of this GaussDBListDatabaseRolesPriv.

        用户/角色密码过期时间。

        :return: The rolpassworddeadline of this GaussDBListDatabaseRolesPriv.
        :rtype: str
        """
        return self._rolpassworddeadline

    @rolpassworddeadline.setter
    def rolpassworddeadline(self, rolpassworddeadline):
        r"""Sets the rolpassworddeadline of this GaussDBListDatabaseRolesPriv.

        用户/角色密码过期时间。

        :param rolpassworddeadline: The rolpassworddeadline of this GaussDBListDatabaseRolesPriv.
        :type rolpassworddeadline: str
        """
        self._rolpassworddeadline = rolpassworddeadline

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
        if not isinstance(other, GaussDBListDatabaseRolesPriv):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
