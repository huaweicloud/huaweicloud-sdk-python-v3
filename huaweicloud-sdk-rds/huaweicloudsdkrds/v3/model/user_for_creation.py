# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserForCreation:

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
        'comment': 'str',
        'hosts': 'list[str]',
        'databases': 'list[DatabaseWithPrivilegeObject]'
    }

    attribute_map = {
        'name': 'name',
        'password': 'password',
        'comment': 'comment',
        'hosts': 'hosts',
        'databases': 'databases'
    }

    def __init__(self, name=None, password=None, comment=None, hosts=None, databases=None):
        """UserForCreation

        The model defined in huaweicloud sdk

        :param name: 数据库用户名称。 数据库帐号名称在1到32个字符之间，由字母、数字、中划线或下划线组成，不能包含其他特殊字符。 - 若数据库版本为MySQL5.6，帐号长度为1～16个字符。 - 若数据库版本为MySQL5.7和8.0，帐号长度为1～32个字符。
        :type name: str
        :param password: 数据库帐号密码。  取值范围：  非空，由大小写字母、数字和特殊符号~!@#$%^*-_&#x3D;+?,()&amp;组成，长度8~32个字符，不能和数据库帐号“name”或“name”的逆序相同。  建议您输入高强度密码，以提高安全性，防止出现密码被暴力破解等安全风险。
        :type password: str
        :param comment: 数据库用户备注。 取值范围：长度1~512个字符。目前仅支持MySQL 8.0.25及以上版本。
        :type comment: str
        :param hosts: 授权用户登录主机IP列表 • 若IP地址为%，则表示允许所有地址访问MySQL实例。 • 若IP地址为“10.10.10.%”，则表示10.10.10.X的IP地址都可以访问该MySQL实例。 • 支持添加多个IP地址。
        :type hosts: list[str]
        :param databases: 授权用户数据库权限
        :type databases: list[:class:`huaweicloudsdkrds.v3.DatabaseWithPrivilegeObject`]
        """
        
        

        self._name = None
        self._password = None
        self._comment = None
        self._hosts = None
        self._databases = None
        self.discriminator = None

        self.name = name
        self.password = password
        if comment is not None:
            self.comment = comment
        if hosts is not None:
            self.hosts = hosts
        if databases is not None:
            self.databases = databases

    @property
    def name(self):
        """Gets the name of this UserForCreation.

        数据库用户名称。 数据库帐号名称在1到32个字符之间，由字母、数字、中划线或下划线组成，不能包含其他特殊字符。 - 若数据库版本为MySQL5.6，帐号长度为1～16个字符。 - 若数据库版本为MySQL5.7和8.0，帐号长度为1～32个字符。

        :return: The name of this UserForCreation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserForCreation.

        数据库用户名称。 数据库帐号名称在1到32个字符之间，由字母、数字、中划线或下划线组成，不能包含其他特殊字符。 - 若数据库版本为MySQL5.6，帐号长度为1～16个字符。 - 若数据库版本为MySQL5.7和8.0，帐号长度为1～32个字符。

        :param name: The name of this UserForCreation.
        :type name: str
        """
        self._name = name

    @property
    def password(self):
        """Gets the password of this UserForCreation.

        数据库帐号密码。  取值范围：  非空，由大小写字母、数字和特殊符号~!@#$%^*-_=+?,()&组成，长度8~32个字符，不能和数据库帐号“name”或“name”的逆序相同。  建议您输入高强度密码，以提高安全性，防止出现密码被暴力破解等安全风险。

        :return: The password of this UserForCreation.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this UserForCreation.

        数据库帐号密码。  取值范围：  非空，由大小写字母、数字和特殊符号~!@#$%^*-_=+?,()&组成，长度8~32个字符，不能和数据库帐号“name”或“name”的逆序相同。  建议您输入高强度密码，以提高安全性，防止出现密码被暴力破解等安全风险。

        :param password: The password of this UserForCreation.
        :type password: str
        """
        self._password = password

    @property
    def comment(self):
        """Gets the comment of this UserForCreation.

        数据库用户备注。 取值范围：长度1~512个字符。目前仅支持MySQL 8.0.25及以上版本。

        :return: The comment of this UserForCreation.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this UserForCreation.

        数据库用户备注。 取值范围：长度1~512个字符。目前仅支持MySQL 8.0.25及以上版本。

        :param comment: The comment of this UserForCreation.
        :type comment: str
        """
        self._comment = comment

    @property
    def hosts(self):
        """Gets the hosts of this UserForCreation.

        授权用户登录主机IP列表 • 若IP地址为%，则表示允许所有地址访问MySQL实例。 • 若IP地址为“10.10.10.%”，则表示10.10.10.X的IP地址都可以访问该MySQL实例。 • 支持添加多个IP地址。

        :return: The hosts of this UserForCreation.
        :rtype: list[str]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this UserForCreation.

        授权用户登录主机IP列表 • 若IP地址为%，则表示允许所有地址访问MySQL实例。 • 若IP地址为“10.10.10.%”，则表示10.10.10.X的IP地址都可以访问该MySQL实例。 • 支持添加多个IP地址。

        :param hosts: The hosts of this UserForCreation.
        :type hosts: list[str]
        """
        self._hosts = hosts

    @property
    def databases(self):
        """Gets the databases of this UserForCreation.

        授权用户数据库权限

        :return: The databases of this UserForCreation.
        :rtype: list[:class:`huaweicloudsdkrds.v3.DatabaseWithPrivilegeObject`]
        """
        return self._databases

    @databases.setter
    def databases(self, databases):
        """Sets the databases of this UserForCreation.

        授权用户数据库权限

        :param databases: The databases of this UserForCreation.
        :type databases: list[:class:`huaweicloudsdkrds.v3.DatabaseWithPrivilegeObject`]
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
        if not isinstance(other, UserForCreation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
