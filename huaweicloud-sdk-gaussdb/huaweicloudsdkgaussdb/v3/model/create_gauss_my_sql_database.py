# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateGaussMySqlDatabase:

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
        'character_set': 'str',
        'users': 'list[GaussMySqlDatabaseUser]'
    }

    attribute_map = {
        'name': 'name',
        'comment': 'comment',
        'character_set': 'character_set',
        'users': 'users'
    }

    def __init__(self, name=None, comment=None, character_set=None, users=None):
        """CreateGaussMySqlDatabase

        The model defined in huaweicloud sdk

        :param name: 数据库名称,数据库名称长度可在1～64个字符之间，由字母、数字、下划线、中划线组成，中划线的累计总长度小于等于10个字符，且不能包含其他特殊字符。
        :type name: str
        :param comment: 数据库备注,长度不能超过512个字符，不能包含回车和特殊字符!&lt;\&quot;&#x3D;&#39;&gt;&amp;。
        :type comment: str
        :param character_set: 数据库使用的字符集名称，如utf8mb4、gbk。
        :type character_set: str
        :param users: 数据库用户列表，即创建数据库时同步授权给列表中的用户，列表最大长度为50。列表可以为空，即创建数据库时不授予其权限到数据库用户，在需要给该数据库授权某数据库用户时，调用数据库用户授权接口即可。
        :type users: list[:class:`huaweicloudsdkgaussdb.v3.GaussMySqlDatabaseUser`]
        """
        
        

        self._name = None
        self._comment = None
        self._character_set = None
        self._users = None
        self.discriminator = None

        self.name = name
        if comment is not None:
            self.comment = comment
        self.character_set = character_set
        if users is not None:
            self.users = users

    @property
    def name(self):
        """Gets the name of this CreateGaussMySqlDatabase.

        数据库名称,数据库名称长度可在1～64个字符之间，由字母、数字、下划线、中划线组成，中划线的累计总长度小于等于10个字符，且不能包含其他特殊字符。

        :return: The name of this CreateGaussMySqlDatabase.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateGaussMySqlDatabase.

        数据库名称,数据库名称长度可在1～64个字符之间，由字母、数字、下划线、中划线组成，中划线的累计总长度小于等于10个字符，且不能包含其他特殊字符。

        :param name: The name of this CreateGaussMySqlDatabase.
        :type name: str
        """
        self._name = name

    @property
    def comment(self):
        """Gets the comment of this CreateGaussMySqlDatabase.

        数据库备注,长度不能超过512个字符，不能包含回车和特殊字符!<\"='>&。

        :return: The comment of this CreateGaussMySqlDatabase.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this CreateGaussMySqlDatabase.

        数据库备注,长度不能超过512个字符，不能包含回车和特殊字符!<\"='>&。

        :param comment: The comment of this CreateGaussMySqlDatabase.
        :type comment: str
        """
        self._comment = comment

    @property
    def character_set(self):
        """Gets the character_set of this CreateGaussMySqlDatabase.

        数据库使用的字符集名称，如utf8mb4、gbk。

        :return: The character_set of this CreateGaussMySqlDatabase.
        :rtype: str
        """
        return self._character_set

    @character_set.setter
    def character_set(self, character_set):
        """Sets the character_set of this CreateGaussMySqlDatabase.

        数据库使用的字符集名称，如utf8mb4、gbk。

        :param character_set: The character_set of this CreateGaussMySqlDatabase.
        :type character_set: str
        """
        self._character_set = character_set

    @property
    def users(self):
        """Gets the users of this CreateGaussMySqlDatabase.

        数据库用户列表，即创建数据库时同步授权给列表中的用户，列表最大长度为50。列表可以为空，即创建数据库时不授予其权限到数据库用户，在需要给该数据库授权某数据库用户时，调用数据库用户授权接口即可。

        :return: The users of this CreateGaussMySqlDatabase.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.GaussMySqlDatabaseUser`]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this CreateGaussMySqlDatabase.

        数据库用户列表，即创建数据库时同步授权给列表中的用户，列表最大长度为50。列表可以为空，即创建数据库时不授予其权限到数据库用户，在需要给该数据库授权某数据库用户时，调用数据库用户授权接口即可。

        :param users: The users of this CreateGaussMySqlDatabase.
        :type users: list[:class:`huaweicloudsdkgaussdb.v3.GaussMySqlDatabaseUser`]
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
        if not isinstance(other, CreateGaussMySqlDatabase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
