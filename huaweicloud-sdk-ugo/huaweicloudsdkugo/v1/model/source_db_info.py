# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SourceDBInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'connection_string': 'str',
        'user_name': 'str',
        'password': 'str',
        'source_db_type': 'str',
        'source_db_version': 'str'
    }

    attribute_map = {
        'connection_string': 'connection_string',
        'user_name': 'user_name',
        'password': 'password',
        'source_db_type': 'source_db_type',
        'source_db_version': 'source_db_version'
    }

    def __init__(self, connection_string=None, user_name=None, password=None, source_db_type=None, source_db_version=None):
        """SourceDBInfo

        The model defined in huaweicloud sdk

        :param connection_string: 连接字符串。
        :type connection_string: str
        :param user_name: 用户名。
        :type user_name: str
        :param password: 用户密码。
        :type password: str
        :param source_db_type: 数据库类型。
        :type source_db_type: str
        :param source_db_version: 数据库版本。 （注意：该字段的值是数据库类型source_db_type对应的版本，当前支持以下组合： ORACLE-11g； ORACLE-12c； ORACLE-18c； ORACLE-19c。）
        :type source_db_version: str
        """
        
        

        self._connection_string = None
        self._user_name = None
        self._password = None
        self._source_db_type = None
        self._source_db_version = None
        self.discriminator = None

        self.connection_string = connection_string
        self.user_name = user_name
        self.password = password
        self.source_db_type = source_db_type
        self.source_db_version = source_db_version

    @property
    def connection_string(self):
        """Gets the connection_string of this SourceDBInfo.

        连接字符串。

        :return: The connection_string of this SourceDBInfo.
        :rtype: str
        """
        return self._connection_string

    @connection_string.setter
    def connection_string(self, connection_string):
        """Sets the connection_string of this SourceDBInfo.

        连接字符串。

        :param connection_string: The connection_string of this SourceDBInfo.
        :type connection_string: str
        """
        self._connection_string = connection_string

    @property
    def user_name(self):
        """Gets the user_name of this SourceDBInfo.

        用户名。

        :return: The user_name of this SourceDBInfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this SourceDBInfo.

        用户名。

        :param user_name: The user_name of this SourceDBInfo.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def password(self):
        """Gets the password of this SourceDBInfo.

        用户密码。

        :return: The password of this SourceDBInfo.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this SourceDBInfo.

        用户密码。

        :param password: The password of this SourceDBInfo.
        :type password: str
        """
        self._password = password

    @property
    def source_db_type(self):
        """Gets the source_db_type of this SourceDBInfo.

        数据库类型。

        :return: The source_db_type of this SourceDBInfo.
        :rtype: str
        """
        return self._source_db_type

    @source_db_type.setter
    def source_db_type(self, source_db_type):
        """Sets the source_db_type of this SourceDBInfo.

        数据库类型。

        :param source_db_type: The source_db_type of this SourceDBInfo.
        :type source_db_type: str
        """
        self._source_db_type = source_db_type

    @property
    def source_db_version(self):
        """Gets the source_db_version of this SourceDBInfo.

        数据库版本。 （注意：该字段的值是数据库类型source_db_type对应的版本，当前支持以下组合： ORACLE-11g； ORACLE-12c； ORACLE-18c； ORACLE-19c。）

        :return: The source_db_version of this SourceDBInfo.
        :rtype: str
        """
        return self._source_db_version

    @source_db_version.setter
    def source_db_version(self, source_db_version):
        """Sets the source_db_version of this SourceDBInfo.

        数据库版本。 （注意：该字段的值是数据库类型source_db_type对应的版本，当前支持以下组合： ORACLE-11g； ORACLE-12c； ORACLE-18c； ORACLE-19c。）

        :param source_db_version: The source_db_version of this SourceDBInfo.
        :type source_db_version: str
        """
        self._source_db_version = source_db_version

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
        if not isinstance(other, SourceDBInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
