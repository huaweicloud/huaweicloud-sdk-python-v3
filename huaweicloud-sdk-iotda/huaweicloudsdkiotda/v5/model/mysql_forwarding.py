# coding: utf-8

import pprint
import re

import six





class MysqlForwarding:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []
    sensitive_list.append('password')

    openapi_types = {
        'address': 'NetAddress',
        'db_name': 'str',
        'username': 'str',
        'password': 'str',
        'table_name': 'str',
        'column_mappings': 'list[ColumnMapping]'
    }

    attribute_map = {
        'address': 'address',
        'db_name': 'db_name',
        'username': 'username',
        'password': 'password',
        'table_name': 'table_name',
        'column_mappings': 'column_mappings'
    }

    def __init__(self, address=None, db_name=None, username=None, password=None, table_name=None, column_mappings=None):
        """MysqlForwarding - a model defined in huaweicloud sdk"""
        
        

        self._address = None
        self._db_name = None
        self._username = None
        self._password = None
        self._table_name = None
        self._column_mappings = None
        self.discriminator = None

        self.address = address
        self.db_name = db_name
        self.username = username
        self.password = password
        self.table_name = table_name
        self.column_mappings = column_mappings

    @property
    def address(self):
        """Gets the address of this MysqlForwarding.


        :return: The address of this MysqlForwarding.
        :rtype: NetAddress
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this MysqlForwarding.


        :param address: The address of this MysqlForwarding.
        :type: NetAddress
        """
        self._address = address

    @property
    def db_name(self):
        """Gets the db_name of this MysqlForwarding.

        连接MYSQL数据库的库名

        :return: The db_name of this MysqlForwarding.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """Sets the db_name of this MysqlForwarding.

        连接MYSQL数据库的库名

        :param db_name: The db_name of this MysqlForwarding.
        :type: str
        """
        self._db_name = db_name

    @property
    def username(self):
        """Gets the username of this MysqlForwarding.

        连接MYSQL数据库的用户名

        :return: The username of this MysqlForwarding.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this MysqlForwarding.

        连接MYSQL数据库的用户名

        :param username: The username of this MysqlForwarding.
        :type: str
        """
        self._username = username

    @property
    def password(self):
        """Gets the password of this MysqlForwarding.

        连接MYSQL数据库的密码

        :return: The password of this MysqlForwarding.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this MysqlForwarding.

        连接MYSQL数据库的密码

        :param password: The password of this MysqlForwarding.
        :type: str
        """
        self._password = password

    @property
    def table_name(self):
        """Gets the table_name of this MysqlForwarding.

        MYSQL数据库的表名

        :return: The table_name of this MysqlForwarding.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this MysqlForwarding.

        MYSQL数据库的表名

        :param table_name: The table_name of this MysqlForwarding.
        :type: str
        """
        self._table_name = table_name

    @property
    def column_mappings(self):
        """Gets the column_mappings of this MysqlForwarding.

        MYSQL数据库的列和流转数据的对应关系列表。

        :return: The column_mappings of this MysqlForwarding.
        :rtype: list[ColumnMapping]
        """
        return self._column_mappings

    @column_mappings.setter
    def column_mappings(self, column_mappings):
        """Sets the column_mappings of this MysqlForwarding.

        MYSQL数据库的列和流转数据的对应关系列表。

        :param column_mappings: The column_mappings of this MysqlForwarding.
        :type: list[ColumnMapping]
        """
        self._column_mappings = column_mappings

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MysqlForwarding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
