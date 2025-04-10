# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDatabaseUserList:

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
        'comment': 'str',
        'password': 'str',
        'hosts': 'list[str]',
        'databases': 'list[CreateDatabaseList]'
    }

    attribute_map = {
        'name': 'name',
        'comment': 'comment',
        'password': 'password',
        'hosts': 'hosts',
        'databases': 'databases'
    }

    def __init__(self, name=None, comment=None, password=None, hosts=None, databases=None):
        r"""CreateDatabaseUserList

        The model defined in huaweicloud sdk

        :param name: 数据库用户名称，数据库用户名称在1到32个字符之间，由字母、数字、下划线组成，不能包含其他特殊字符。
        :type name: str
        :param comment: 数据库备注,长度不能超过512个字符，不能包含回车和特殊字符!&lt;\&quot;&#x3D;&#39;&gt;&amp;。  该字段只针对新版本的实例生效，必须大于等于指定的内核版本-2.0.13.0，如果不符合内核版本要求，参考升级内核版本升级至最新。
        :type comment: str
        :param password: 数据库用户密码，不能同用户名称相同，非空，至少包含以下字符中的三种：大写字母、小写字母、数字和特殊符号~!@#$%^*-_&#x3D;+?,()&amp;组成，长度8~32个字符。  建议您输入高强度密码，以提高安全性，防止出现密码被暴力破解等安全风险。
        :type password: str
        :param hosts: 主机IP地址，即允许数据库用户在当前主机连接数据库，默认IP地址为%，表示允许所有地址访问TaurusDB实例。若IP地址为“10.10.10.%”，则表示10.10.10.X的IP地址都可以访问该TaurusDB实例。若您需要添加多个IP地址，请用英文逗号隔开（逗号前后都不能加空格），例如192.168.0.1,172.16.213.9，一次最多创建50个。
        :type hosts: list[str]
        :param databases: 
        :type databases: list[:class:`huaweicloudsdkgaussdb.v3.CreateDatabaseList`]
        """
        
        

        self._name = None
        self._comment = None
        self._password = None
        self._hosts = None
        self._databases = None
        self.discriminator = None

        self.name = name
        if comment is not None:
            self.comment = comment
        self.password = password
        if hosts is not None:
            self.hosts = hosts
        if databases is not None:
            self.databases = databases

    @property
    def name(self):
        r"""Gets the name of this CreateDatabaseUserList.

        数据库用户名称，数据库用户名称在1到32个字符之间，由字母、数字、下划线组成，不能包含其他特殊字符。

        :return: The name of this CreateDatabaseUserList.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateDatabaseUserList.

        数据库用户名称，数据库用户名称在1到32个字符之间，由字母、数字、下划线组成，不能包含其他特殊字符。

        :param name: The name of this CreateDatabaseUserList.
        :type name: str
        """
        self._name = name

    @property
    def comment(self):
        r"""Gets the comment of this CreateDatabaseUserList.

        数据库备注,长度不能超过512个字符，不能包含回车和特殊字符!<\"='>&。  该字段只针对新版本的实例生效，必须大于等于指定的内核版本-2.0.13.0，如果不符合内核版本要求，参考升级内核版本升级至最新。

        :return: The comment of this CreateDatabaseUserList.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        r"""Sets the comment of this CreateDatabaseUserList.

        数据库备注,长度不能超过512个字符，不能包含回车和特殊字符!<\"='>&。  该字段只针对新版本的实例生效，必须大于等于指定的内核版本-2.0.13.0，如果不符合内核版本要求，参考升级内核版本升级至最新。

        :param comment: The comment of this CreateDatabaseUserList.
        :type comment: str
        """
        self._comment = comment

    @property
    def password(self):
        r"""Gets the password of this CreateDatabaseUserList.

        数据库用户密码，不能同用户名称相同，非空，至少包含以下字符中的三种：大写字母、小写字母、数字和特殊符号~!@#$%^*-_=+?,()&组成，长度8~32个字符。  建议您输入高强度密码，以提高安全性，防止出现密码被暴力破解等安全风险。

        :return: The password of this CreateDatabaseUserList.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        r"""Sets the password of this CreateDatabaseUserList.

        数据库用户密码，不能同用户名称相同，非空，至少包含以下字符中的三种：大写字母、小写字母、数字和特殊符号~!@#$%^*-_=+?,()&组成，长度8~32个字符。  建议您输入高强度密码，以提高安全性，防止出现密码被暴力破解等安全风险。

        :param password: The password of this CreateDatabaseUserList.
        :type password: str
        """
        self._password = password

    @property
    def hosts(self):
        r"""Gets the hosts of this CreateDatabaseUserList.

        主机IP地址，即允许数据库用户在当前主机连接数据库，默认IP地址为%，表示允许所有地址访问TaurusDB实例。若IP地址为“10.10.10.%”，则表示10.10.10.X的IP地址都可以访问该TaurusDB实例。若您需要添加多个IP地址，请用英文逗号隔开（逗号前后都不能加空格），例如192.168.0.1,172.16.213.9，一次最多创建50个。

        :return: The hosts of this CreateDatabaseUserList.
        :rtype: list[str]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        r"""Sets the hosts of this CreateDatabaseUserList.

        主机IP地址，即允许数据库用户在当前主机连接数据库，默认IP地址为%，表示允许所有地址访问TaurusDB实例。若IP地址为“10.10.10.%”，则表示10.10.10.X的IP地址都可以访问该TaurusDB实例。若您需要添加多个IP地址，请用英文逗号隔开（逗号前后都不能加空格），例如192.168.0.1,172.16.213.9，一次最多创建50个。

        :param hosts: The hosts of this CreateDatabaseUserList.
        :type hosts: list[str]
        """
        self._hosts = hosts

    @property
    def databases(self):
        r"""Gets the databases of this CreateDatabaseUserList.

        :return: The databases of this CreateDatabaseUserList.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.CreateDatabaseList`]
        """
        return self._databases

    @databases.setter
    def databases(self, databases):
        r"""Sets the databases of this CreateDatabaseUserList.

        :param databases: The databases of this CreateDatabaseUserList.
        :type databases: list[:class:`huaweicloudsdkgaussdb.v3.CreateDatabaseList`]
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
        if not isinstance(other, CreateDatabaseUserList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
