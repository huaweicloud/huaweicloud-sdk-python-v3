# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserForList:

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
        'databases': 'list[DatabaseWithPrivilegeObject]',
        'hosts': 'list[str]',
        'comment': 'str'
    }

    attribute_map = {
        'name': 'name',
        'databases': 'databases',
        'hosts': 'hosts',
        'comment': 'comment'
    }

    def __init__(self, name=None, databases=None, hosts=None, comment=None):
        r"""UserForList

        The model defined in huaweicloud sdk

        :param name: 数据库用户名称。
        :type name: str
        :param databases: 数据库及其权限。
        :type databases: list[:class:`huaweicloudsdkrds.v3.DatabaseWithPrivilegeObject`]
        :param hosts: 授权用户登录主机IP列表 • 若IP地址为%，则表示允许所有地址访问MySQL实例。 • 若IP地址为“10.10.10.%”，则表示10.10.10.X的IP地址都可以访问该MySQL实例。 • 支持添加多个IP地址。
        :type hosts: list[str]
        :param comment: 数据库用户备注
        :type comment: str
        """
        
        

        self._name = None
        self._databases = None
        self._hosts = None
        self._comment = None
        self.discriminator = None

        self.name = name
        self.databases = databases
        self.hosts = hosts
        self.comment = comment

    @property
    def name(self):
        r"""Gets the name of this UserForList.

        数据库用户名称。

        :return: The name of this UserForList.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UserForList.

        数据库用户名称。

        :param name: The name of this UserForList.
        :type name: str
        """
        self._name = name

    @property
    def databases(self):
        r"""Gets the databases of this UserForList.

        数据库及其权限。

        :return: The databases of this UserForList.
        :rtype: list[:class:`huaweicloudsdkrds.v3.DatabaseWithPrivilegeObject`]
        """
        return self._databases

    @databases.setter
    def databases(self, databases):
        r"""Sets the databases of this UserForList.

        数据库及其权限。

        :param databases: The databases of this UserForList.
        :type databases: list[:class:`huaweicloudsdkrds.v3.DatabaseWithPrivilegeObject`]
        """
        self._databases = databases

    @property
    def hosts(self):
        r"""Gets the hosts of this UserForList.

        授权用户登录主机IP列表 • 若IP地址为%，则表示允许所有地址访问MySQL实例。 • 若IP地址为“10.10.10.%”，则表示10.10.10.X的IP地址都可以访问该MySQL实例。 • 支持添加多个IP地址。

        :return: The hosts of this UserForList.
        :rtype: list[str]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        r"""Sets the hosts of this UserForList.

        授权用户登录主机IP列表 • 若IP地址为%，则表示允许所有地址访问MySQL实例。 • 若IP地址为“10.10.10.%”，则表示10.10.10.X的IP地址都可以访问该MySQL实例。 • 支持添加多个IP地址。

        :param hosts: The hosts of this UserForList.
        :type hosts: list[str]
        """
        self._hosts = hosts

    @property
    def comment(self):
        r"""Gets the comment of this UserForList.

        数据库用户备注

        :return: The comment of this UserForList.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        r"""Sets the comment of this UserForList.

        数据库用户备注

        :param comment: The comment of this UserForList.
        :type comment: str
        """
        self._comment = comment

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
        if not isinstance(other, UserForList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
