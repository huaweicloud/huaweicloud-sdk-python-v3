# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RedisDbUserInfo:

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
        'type': 'str',
        'privilege': 'str',
        'databases': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'privilege': 'privilege',
        'databases': 'databases'
    }

    def __init__(self, name=None, type=None, privilege=None, databases=None):
        """RedisDbUserInfo

        The model defined in huaweicloud sdk

        :param name: 账号名称。  小于36个字符，以字母开头，仅包含数字、字母、中划线、下划线。
        :type name: str
        :param type: 账号类型。  - rwuser：管理员用户 - acluser：普通用户
        :type type: str
        :param privilege: 账号权限。  - 取值\&quot;ReadOnly\&quot;：账号为只读权限； - 取值\&quot;ReadWrite\&quot;：账号为读写权限。
        :type privilege: str
        :param databases: 账号已授权的数据库名称列表。
        :type databases: list[str]
        """
        
        

        self._name = None
        self._type = None
        self._privilege = None
        self._databases = None
        self.discriminator = None

        self.name = name
        self.type = type
        self.privilege = privilege
        self.databases = databases

    @property
    def name(self):
        """Gets the name of this RedisDbUserInfo.

        账号名称。  小于36个字符，以字母开头，仅包含数字、字母、中划线、下划线。

        :return: The name of this RedisDbUserInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RedisDbUserInfo.

        账号名称。  小于36个字符，以字母开头，仅包含数字、字母、中划线、下划线。

        :param name: The name of this RedisDbUserInfo.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this RedisDbUserInfo.

        账号类型。  - rwuser：管理员用户 - acluser：普通用户

        :return: The type of this RedisDbUserInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RedisDbUserInfo.

        账号类型。  - rwuser：管理员用户 - acluser：普通用户

        :param type: The type of this RedisDbUserInfo.
        :type type: str
        """
        self._type = type

    @property
    def privilege(self):
        """Gets the privilege of this RedisDbUserInfo.

        账号权限。  - 取值\"ReadOnly\"：账号为只读权限； - 取值\"ReadWrite\"：账号为读写权限。

        :return: The privilege of this RedisDbUserInfo.
        :rtype: str
        """
        return self._privilege

    @privilege.setter
    def privilege(self, privilege):
        """Sets the privilege of this RedisDbUserInfo.

        账号权限。  - 取值\"ReadOnly\"：账号为只读权限； - 取值\"ReadWrite\"：账号为读写权限。

        :param privilege: The privilege of this RedisDbUserInfo.
        :type privilege: str
        """
        self._privilege = privilege

    @property
    def databases(self):
        """Gets the databases of this RedisDbUserInfo.

        账号已授权的数据库名称列表。

        :return: The databases of this RedisDbUserInfo.
        :rtype: list[str]
        """
        return self._databases

    @databases.setter
    def databases(self, databases):
        """Sets the databases of this RedisDbUserInfo.

        账号已授权的数据库名称列表。

        :param databases: The databases of this RedisDbUserInfo.
        :type databases: list[str]
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
        if not isinstance(other, RedisDbUserInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
