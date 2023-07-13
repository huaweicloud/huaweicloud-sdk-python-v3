# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGaussMySqlDatabaseUser:

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
        'host': 'str',
        'comment': 'str',
        'databases': 'list[ListGaussMySqlDatabase]'
    }

    attribute_map = {
        'name': 'name',
        'host': 'host',
        'comment': 'comment',
        'databases': 'databases'
    }

    def __init__(self, name=None, host=None, comment=None, databases=None):
        """ListGaussMySqlDatabaseUser

        The model defined in huaweicloud sdk

        :param name: 数据库用户名。
        :type name: str
        :param host: 主机地址。
        :type host: str
        :param comment: 数据库用户备注。
        :type comment: str
        :param databases: 数据库列表。
        :type databases: list[:class:`huaweicloudsdkgaussdb.v3.ListGaussMySqlDatabase`]
        """
        
        

        self._name = None
        self._host = None
        self._comment = None
        self._databases = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if host is not None:
            self.host = host
        if comment is not None:
            self.comment = comment
        if databases is not None:
            self.databases = databases

    @property
    def name(self):
        """Gets the name of this ListGaussMySqlDatabaseUser.

        数据库用户名。

        :return: The name of this ListGaussMySqlDatabaseUser.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListGaussMySqlDatabaseUser.

        数据库用户名。

        :param name: The name of this ListGaussMySqlDatabaseUser.
        :type name: str
        """
        self._name = name

    @property
    def host(self):
        """Gets the host of this ListGaussMySqlDatabaseUser.

        主机地址。

        :return: The host of this ListGaussMySqlDatabaseUser.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this ListGaussMySqlDatabaseUser.

        主机地址。

        :param host: The host of this ListGaussMySqlDatabaseUser.
        :type host: str
        """
        self._host = host

    @property
    def comment(self):
        """Gets the comment of this ListGaussMySqlDatabaseUser.

        数据库用户备注。

        :return: The comment of this ListGaussMySqlDatabaseUser.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this ListGaussMySqlDatabaseUser.

        数据库用户备注。

        :param comment: The comment of this ListGaussMySqlDatabaseUser.
        :type comment: str
        """
        self._comment = comment

    @property
    def databases(self):
        """Gets the databases of this ListGaussMySqlDatabaseUser.

        数据库列表。

        :return: The databases of this ListGaussMySqlDatabaseUser.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.ListGaussMySqlDatabase`]
        """
        return self._databases

    @databases.setter
    def databases(self, databases):
        """Sets the databases of this ListGaussMySqlDatabaseUser.

        数据库列表。

        :param databases: The databases of this ListGaussMySqlDatabaseUser.
        :type databases: list[:class:`huaweicloudsdkgaussdb.v3.ListGaussMySqlDatabase`]
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
        if not isinstance(other, ListGaussMySqlDatabaseUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
