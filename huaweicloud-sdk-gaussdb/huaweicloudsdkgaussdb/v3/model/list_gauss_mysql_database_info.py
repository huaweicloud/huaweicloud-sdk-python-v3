# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGaussMysqlDatabaseInfo:

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
        'charset': 'str',
        'comment': 'str',
        'users': 'list[GaussMySqlDatabaseInfo]'
    }

    attribute_map = {
        'name': 'name',
        'charset': 'charset',
        'comment': 'comment',
        'users': 'users'
    }

    def __init__(self, name=None, charset=None, comment=None, users=None):
        r"""ListGaussMysqlDatabaseInfo

        The model defined in huaweicloud sdk

        :param name: 数据库名称。
        :type name: str
        :param charset: 数据库使用的字符集，如utf8mb4、gbk等。
        :type charset: str
        :param comment: 数据库备注。
        :type comment: str
        :param users: 已授权数据库用户列表。
        :type users: list[:class:`huaweicloudsdkgaussdb.v3.GaussMySqlDatabaseInfo`]
        """
        
        

        self._name = None
        self._charset = None
        self._comment = None
        self._users = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if charset is not None:
            self.charset = charset
        if comment is not None:
            self.comment = comment
        if users is not None:
            self.users = users

    @property
    def name(self):
        r"""Gets the name of this ListGaussMysqlDatabaseInfo.

        数据库名称。

        :return: The name of this ListGaussMysqlDatabaseInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListGaussMysqlDatabaseInfo.

        数据库名称。

        :param name: The name of this ListGaussMysqlDatabaseInfo.
        :type name: str
        """
        self._name = name

    @property
    def charset(self):
        r"""Gets the charset of this ListGaussMysqlDatabaseInfo.

        数据库使用的字符集，如utf8mb4、gbk等。

        :return: The charset of this ListGaussMysqlDatabaseInfo.
        :rtype: str
        """
        return self._charset

    @charset.setter
    def charset(self, charset):
        r"""Sets the charset of this ListGaussMysqlDatabaseInfo.

        数据库使用的字符集，如utf8mb4、gbk等。

        :param charset: The charset of this ListGaussMysqlDatabaseInfo.
        :type charset: str
        """
        self._charset = charset

    @property
    def comment(self):
        r"""Gets the comment of this ListGaussMysqlDatabaseInfo.

        数据库备注。

        :return: The comment of this ListGaussMysqlDatabaseInfo.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        r"""Sets the comment of this ListGaussMysqlDatabaseInfo.

        数据库备注。

        :param comment: The comment of this ListGaussMysqlDatabaseInfo.
        :type comment: str
        """
        self._comment = comment

    @property
    def users(self):
        r"""Gets the users of this ListGaussMysqlDatabaseInfo.

        已授权数据库用户列表。

        :return: The users of this ListGaussMysqlDatabaseInfo.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.GaussMySqlDatabaseInfo`]
        """
        return self._users

    @users.setter
    def users(self, users):
        r"""Sets the users of this ListGaussMysqlDatabaseInfo.

        已授权数据库用户列表。

        :param users: The users of this ListGaussMysqlDatabaseInfo.
        :type users: list[:class:`huaweicloudsdkgaussdb.v3.GaussMySqlDatabaseInfo`]
        """
        self._users = users

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
        if not isinstance(other, ListGaussMysqlDatabaseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
