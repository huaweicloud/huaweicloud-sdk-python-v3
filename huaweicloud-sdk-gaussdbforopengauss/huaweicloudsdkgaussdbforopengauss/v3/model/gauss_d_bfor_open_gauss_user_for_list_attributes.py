# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GaussDBforOpenGaussUserForListAttributes:

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
        'rolbypassrls': 'bool'
    }

    attribute_map = {
        'rolsuper': 'rolsuper',
        'rolinherit': 'rolinherit',
        'rolcreaterole': 'rolcreaterole',
        'rolcreatedb': 'rolcreatedb',
        'rolcanlogin': 'rolcanlogin',
        'rolconnlimit': 'rolconnlimit',
        'rolreplication': 'rolreplication',
        'rolbypassrls': 'rolbypassrls'
    }

    def __init__(self, rolsuper=None, rolinherit=None, rolcreaterole=None, rolcreatedb=None, rolcanlogin=None, rolconnlimit=None, rolreplication=None, rolbypassrls=None):
        """GaussDBforOpenGaussUserForListAttributes

        The model defined in huaweicloud sdk

        :param rolsuper: 用户是否具有超级用户权限，取值为“true”或“false”。
        :type rolsuper: bool
        :param rolinherit: 用户是否自动继承其所属角色的权限，取值为“true”或“false”。
        :type rolinherit: bool
        :param rolcreaterole: 用户是否支持创建其他子用户，取值为“true”或“false”。
        :type rolcreaterole: bool
        :param rolcreatedb: 用户是否可以创建数据库，取值为“true”或“false”。
        :type rolcreatedb: bool
        :param rolcanlogin: 用户是否可以登录数据库，取值为“true”或“false”。
        :type rolcanlogin: bool
        :param rolconnlimit: 用户连接实例的最大并发连接数。-1表示没有限制。
        :type rolconnlimit: int
        :param rolreplication: 用户是否属于复制角色，取值为“true”或“false”。
        :type rolreplication: bool
        :param rolbypassrls: 用户是否绕过每个行级安全策略，取值为“true”或“false”。
        :type rolbypassrls: bool
        """
        
        

        self._rolsuper = None
        self._rolinherit = None
        self._rolcreaterole = None
        self._rolcreatedb = None
        self._rolcanlogin = None
        self._rolconnlimit = None
        self._rolreplication = None
        self._rolbypassrls = None
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

    @property
    def rolsuper(self):
        """Gets the rolsuper of this GaussDBforOpenGaussUserForListAttributes.

        用户是否具有超级用户权限，取值为“true”或“false”。

        :return: The rolsuper of this GaussDBforOpenGaussUserForListAttributes.
        :rtype: bool
        """
        return self._rolsuper

    @rolsuper.setter
    def rolsuper(self, rolsuper):
        """Sets the rolsuper of this GaussDBforOpenGaussUserForListAttributes.

        用户是否具有超级用户权限，取值为“true”或“false”。

        :param rolsuper: The rolsuper of this GaussDBforOpenGaussUserForListAttributes.
        :type rolsuper: bool
        """
        self._rolsuper = rolsuper

    @property
    def rolinherit(self):
        """Gets the rolinherit of this GaussDBforOpenGaussUserForListAttributes.

        用户是否自动继承其所属角色的权限，取值为“true”或“false”。

        :return: The rolinherit of this GaussDBforOpenGaussUserForListAttributes.
        :rtype: bool
        """
        return self._rolinherit

    @rolinherit.setter
    def rolinherit(self, rolinherit):
        """Sets the rolinherit of this GaussDBforOpenGaussUserForListAttributes.

        用户是否自动继承其所属角色的权限，取值为“true”或“false”。

        :param rolinherit: The rolinherit of this GaussDBforOpenGaussUserForListAttributes.
        :type rolinherit: bool
        """
        self._rolinherit = rolinherit

    @property
    def rolcreaterole(self):
        """Gets the rolcreaterole of this GaussDBforOpenGaussUserForListAttributes.

        用户是否支持创建其他子用户，取值为“true”或“false”。

        :return: The rolcreaterole of this GaussDBforOpenGaussUserForListAttributes.
        :rtype: bool
        """
        return self._rolcreaterole

    @rolcreaterole.setter
    def rolcreaterole(self, rolcreaterole):
        """Sets the rolcreaterole of this GaussDBforOpenGaussUserForListAttributes.

        用户是否支持创建其他子用户，取值为“true”或“false”。

        :param rolcreaterole: The rolcreaterole of this GaussDBforOpenGaussUserForListAttributes.
        :type rolcreaterole: bool
        """
        self._rolcreaterole = rolcreaterole

    @property
    def rolcreatedb(self):
        """Gets the rolcreatedb of this GaussDBforOpenGaussUserForListAttributes.

        用户是否可以创建数据库，取值为“true”或“false”。

        :return: The rolcreatedb of this GaussDBforOpenGaussUserForListAttributes.
        :rtype: bool
        """
        return self._rolcreatedb

    @rolcreatedb.setter
    def rolcreatedb(self, rolcreatedb):
        """Sets the rolcreatedb of this GaussDBforOpenGaussUserForListAttributes.

        用户是否可以创建数据库，取值为“true”或“false”。

        :param rolcreatedb: The rolcreatedb of this GaussDBforOpenGaussUserForListAttributes.
        :type rolcreatedb: bool
        """
        self._rolcreatedb = rolcreatedb

    @property
    def rolcanlogin(self):
        """Gets the rolcanlogin of this GaussDBforOpenGaussUserForListAttributes.

        用户是否可以登录数据库，取值为“true”或“false”。

        :return: The rolcanlogin of this GaussDBforOpenGaussUserForListAttributes.
        :rtype: bool
        """
        return self._rolcanlogin

    @rolcanlogin.setter
    def rolcanlogin(self, rolcanlogin):
        """Sets the rolcanlogin of this GaussDBforOpenGaussUserForListAttributes.

        用户是否可以登录数据库，取值为“true”或“false”。

        :param rolcanlogin: The rolcanlogin of this GaussDBforOpenGaussUserForListAttributes.
        :type rolcanlogin: bool
        """
        self._rolcanlogin = rolcanlogin

    @property
    def rolconnlimit(self):
        """Gets the rolconnlimit of this GaussDBforOpenGaussUserForListAttributes.

        用户连接实例的最大并发连接数。-1表示没有限制。

        :return: The rolconnlimit of this GaussDBforOpenGaussUserForListAttributes.
        :rtype: int
        """
        return self._rolconnlimit

    @rolconnlimit.setter
    def rolconnlimit(self, rolconnlimit):
        """Sets the rolconnlimit of this GaussDBforOpenGaussUserForListAttributes.

        用户连接实例的最大并发连接数。-1表示没有限制。

        :param rolconnlimit: The rolconnlimit of this GaussDBforOpenGaussUserForListAttributes.
        :type rolconnlimit: int
        """
        self._rolconnlimit = rolconnlimit

    @property
    def rolreplication(self):
        """Gets the rolreplication of this GaussDBforOpenGaussUserForListAttributes.

        用户是否属于复制角色，取值为“true”或“false”。

        :return: The rolreplication of this GaussDBforOpenGaussUserForListAttributes.
        :rtype: bool
        """
        return self._rolreplication

    @rolreplication.setter
    def rolreplication(self, rolreplication):
        """Sets the rolreplication of this GaussDBforOpenGaussUserForListAttributes.

        用户是否属于复制角色，取值为“true”或“false”。

        :param rolreplication: The rolreplication of this GaussDBforOpenGaussUserForListAttributes.
        :type rolreplication: bool
        """
        self._rolreplication = rolreplication

    @property
    def rolbypassrls(self):
        """Gets the rolbypassrls of this GaussDBforOpenGaussUserForListAttributes.

        用户是否绕过每个行级安全策略，取值为“true”或“false”。

        :return: The rolbypassrls of this GaussDBforOpenGaussUserForListAttributes.
        :rtype: bool
        """
        return self._rolbypassrls

    @rolbypassrls.setter
    def rolbypassrls(self, rolbypassrls):
        """Sets the rolbypassrls of this GaussDBforOpenGaussUserForListAttributes.

        用户是否绕过每个行级安全策略，取值为“true”或“false”。

        :param rolbypassrls: The rolbypassrls of this GaussDBforOpenGaussUserForListAttributes.
        :type rolbypassrls: bool
        """
        self._rolbypassrls = rolbypassrls

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
        if not isinstance(other, GaussDBforOpenGaussUserForListAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
