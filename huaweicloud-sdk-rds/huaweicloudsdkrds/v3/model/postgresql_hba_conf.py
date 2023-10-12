# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PostgresqlHbaConf:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'database': 'str',
        'user': 'str',
        'address': 'str',
        'mask': 'str',
        'method': 'str',
        'priority': 'int'
    }

    attribute_map = {
        'type': 'type',
        'database': 'database',
        'user': 'user',
        'address': 'address',
        'mask': 'mask',
        'method': 'method',
        'priority': 'priority'
    }

    def __init__(self, type=None, database=None, user=None, address=None, mask=None, method=None, priority=None):
        """PostgresqlHbaConf

        The model defined in huaweicloud sdk

        :param type: 连接类型，枚举，host、hostssl、hostnossl
        :type type: str
        :param database: 数据库名，除template0，template1的数据库名，多个以逗号隔开
        :type database: str
        :param user: 用户名，all，除内置用户（rdsAdmin, rdsMetric, rdsBackup, rdsRepl, rdsProxy）以外，多个以逗号隔开
        :type user: str
        :param address: 客户端IP地址。0.0.0.0/0表示允许用户从任意IP地址访问数据库
        :type address: str
        :param mask: 掩码，默认为空字符串
        :type mask: str
        :param method: 认证方式。枚举：reject、md5、scram-sha-256
        :type method: str
        :param priority: 优先级，表示配置的先后
        :type priority: int
        """
        
        

        self._type = None
        self._database = None
        self._user = None
        self._address = None
        self._mask = None
        self._method = None
        self._priority = None
        self.discriminator = None

        self.type = type
        self.database = database
        self.user = user
        self.address = address
        if mask is not None:
            self.mask = mask
        self.method = method
        self.priority = priority

    @property
    def type(self):
        """Gets the type of this PostgresqlHbaConf.

        连接类型，枚举，host、hostssl、hostnossl

        :return: The type of this PostgresqlHbaConf.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PostgresqlHbaConf.

        连接类型，枚举，host、hostssl、hostnossl

        :param type: The type of this PostgresqlHbaConf.
        :type type: str
        """
        self._type = type

    @property
    def database(self):
        """Gets the database of this PostgresqlHbaConf.

        数据库名，除template0，template1的数据库名，多个以逗号隔开

        :return: The database of this PostgresqlHbaConf.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        """Sets the database of this PostgresqlHbaConf.

        数据库名，除template0，template1的数据库名，多个以逗号隔开

        :param database: The database of this PostgresqlHbaConf.
        :type database: str
        """
        self._database = database

    @property
    def user(self):
        """Gets the user of this PostgresqlHbaConf.

        用户名，all，除内置用户（rdsAdmin, rdsMetric, rdsBackup, rdsRepl, rdsProxy）以外，多个以逗号隔开

        :return: The user of this PostgresqlHbaConf.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this PostgresqlHbaConf.

        用户名，all，除内置用户（rdsAdmin, rdsMetric, rdsBackup, rdsRepl, rdsProxy）以外，多个以逗号隔开

        :param user: The user of this PostgresqlHbaConf.
        :type user: str
        """
        self._user = user

    @property
    def address(self):
        """Gets the address of this PostgresqlHbaConf.

        客户端IP地址。0.0.0.0/0表示允许用户从任意IP地址访问数据库

        :return: The address of this PostgresqlHbaConf.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this PostgresqlHbaConf.

        客户端IP地址。0.0.0.0/0表示允许用户从任意IP地址访问数据库

        :param address: The address of this PostgresqlHbaConf.
        :type address: str
        """
        self._address = address

    @property
    def mask(self):
        """Gets the mask of this PostgresqlHbaConf.

        掩码，默认为空字符串

        :return: The mask of this PostgresqlHbaConf.
        :rtype: str
        """
        return self._mask

    @mask.setter
    def mask(self, mask):
        """Sets the mask of this PostgresqlHbaConf.

        掩码，默认为空字符串

        :param mask: The mask of this PostgresqlHbaConf.
        :type mask: str
        """
        self._mask = mask

    @property
    def method(self):
        """Gets the method of this PostgresqlHbaConf.

        认证方式。枚举：reject、md5、scram-sha-256

        :return: The method of this PostgresqlHbaConf.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this PostgresqlHbaConf.

        认证方式。枚举：reject、md5、scram-sha-256

        :param method: The method of this PostgresqlHbaConf.
        :type method: str
        """
        self._method = method

    @property
    def priority(self):
        """Gets the priority of this PostgresqlHbaConf.

        优先级，表示配置的先后

        :return: The priority of this PostgresqlHbaConf.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this PostgresqlHbaConf.

        优先级，表示配置的先后

        :param priority: The priority of this PostgresqlHbaConf.
        :type priority: int
        """
        self._priority = priority

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
        if not isinstance(other, PostgresqlHbaConf):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
