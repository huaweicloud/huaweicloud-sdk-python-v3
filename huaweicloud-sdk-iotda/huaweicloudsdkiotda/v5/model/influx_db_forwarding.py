# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InfluxDBForwarding:

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
        'measurement': 'str',
        'column_mappings': 'list[ColumnMapping]'
    }

    attribute_map = {
        'address': 'address',
        'db_name': 'db_name',
        'username': 'username',
        'password': 'password',
        'measurement': 'measurement',
        'column_mappings': 'column_mappings'
    }

    def __init__(self, address=None, db_name=None, username=None, password=None, measurement=None, column_mappings=None):
        """InfluxDBForwarding

        The model defined in huaweicloud sdk

        :param address: 
        :type address: :class:`huaweicloudsdkiotda.v5.NetAddress`
        :param db_name: **参数说明**：连接InfluxDB数据库的库名,不存在会自动创建
        :type db_name: str
        :param username: **参数说明**：连接InfluxDB数据库的用户名
        :type username: str
        :param password: **参数说明**：连接InfluxDB数据库的密码
        :type password: str
        :param measurement: **参数说明**：InfluxDB数据库的measurement,不存在会自动创建
        :type measurement: str
        :param column_mappings: **参数说明**：InfluxDB数据库和流转数据的对应关系列表。
        :type column_mappings: list[:class:`huaweicloudsdkiotda.v5.ColumnMapping`]
        """
        
        

        self._address = None
        self._db_name = None
        self._username = None
        self._password = None
        self._measurement = None
        self._column_mappings = None
        self.discriminator = None

        self.address = address
        self.db_name = db_name
        self.username = username
        self.password = password
        self.measurement = measurement
        self.column_mappings = column_mappings

    @property
    def address(self):
        """Gets the address of this InfluxDBForwarding.

        :return: The address of this InfluxDBForwarding.
        :rtype: :class:`huaweicloudsdkiotda.v5.NetAddress`
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this InfluxDBForwarding.

        :param address: The address of this InfluxDBForwarding.
        :type address: :class:`huaweicloudsdkiotda.v5.NetAddress`
        """
        self._address = address

    @property
    def db_name(self):
        """Gets the db_name of this InfluxDBForwarding.

        **参数说明**：连接InfluxDB数据库的库名,不存在会自动创建

        :return: The db_name of this InfluxDBForwarding.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """Sets the db_name of this InfluxDBForwarding.

        **参数说明**：连接InfluxDB数据库的库名,不存在会自动创建

        :param db_name: The db_name of this InfluxDBForwarding.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def username(self):
        """Gets the username of this InfluxDBForwarding.

        **参数说明**：连接InfluxDB数据库的用户名

        :return: The username of this InfluxDBForwarding.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this InfluxDBForwarding.

        **参数说明**：连接InfluxDB数据库的用户名

        :param username: The username of this InfluxDBForwarding.
        :type username: str
        """
        self._username = username

    @property
    def password(self):
        """Gets the password of this InfluxDBForwarding.

        **参数说明**：连接InfluxDB数据库的密码

        :return: The password of this InfluxDBForwarding.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this InfluxDBForwarding.

        **参数说明**：连接InfluxDB数据库的密码

        :param password: The password of this InfluxDBForwarding.
        :type password: str
        """
        self._password = password

    @property
    def measurement(self):
        """Gets the measurement of this InfluxDBForwarding.

        **参数说明**：InfluxDB数据库的measurement,不存在会自动创建

        :return: The measurement of this InfluxDBForwarding.
        :rtype: str
        """
        return self._measurement

    @measurement.setter
    def measurement(self, measurement):
        """Sets the measurement of this InfluxDBForwarding.

        **参数说明**：InfluxDB数据库的measurement,不存在会自动创建

        :param measurement: The measurement of this InfluxDBForwarding.
        :type measurement: str
        """
        self._measurement = measurement

    @property
    def column_mappings(self):
        """Gets the column_mappings of this InfluxDBForwarding.

        **参数说明**：InfluxDB数据库和流转数据的对应关系列表。

        :return: The column_mappings of this InfluxDBForwarding.
        :rtype: list[:class:`huaweicloudsdkiotda.v5.ColumnMapping`]
        """
        return self._column_mappings

    @column_mappings.setter
    def column_mappings(self, column_mappings):
        """Sets the column_mappings of this InfluxDBForwarding.

        **参数说明**：InfluxDB数据库和流转数据的对应关系列表。

        :param column_mappings: The column_mappings of this InfluxDBForwarding.
        :type column_mappings: list[:class:`huaweicloudsdkiotda.v5.ColumnMapping`]
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
        if not isinstance(other, InfluxDBForwarding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
