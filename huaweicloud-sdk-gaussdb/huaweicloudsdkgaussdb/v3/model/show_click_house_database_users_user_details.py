# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowClickHouseDatabaseUsersUserDetails:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_name': 'str',
        'databases': 'list[str]',
        'dml': 'int',
        'ddl': 'int'
    }

    attribute_map = {
        'user_name': 'user_name',
        'databases': 'databases',
        'dml': 'dml',
        'ddl': 'ddl'
    }

    def __init__(self, user_name=None, databases=None, dml=None, ddl=None):
        """ShowClickHouseDatabaseUsersUserDetails

        The model defined in huaweicloud sdk

        :param user_name: 数据库账户名。
        :type user_name: str
        :param databases: 已授权数据库。
        :type databases: list[str]
        :param dml: DML权限。 取值范围： - 1：只读权限 - 2：读取和设置权限
        :type dml: int
        :param ddl: DDL授权。 取值范围： - 0：无DDL权限 - 1：有DDL权限
        :type ddl: int
        """
        
        

        self._user_name = None
        self._databases = None
        self._dml = None
        self._ddl = None
        self.discriminator = None

        self.user_name = user_name
        self.databases = databases
        self.dml = dml
        self.ddl = ddl

    @property
    def user_name(self):
        """Gets the user_name of this ShowClickHouseDatabaseUsersUserDetails.

        数据库账户名。

        :return: The user_name of this ShowClickHouseDatabaseUsersUserDetails.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ShowClickHouseDatabaseUsersUserDetails.

        数据库账户名。

        :param user_name: The user_name of this ShowClickHouseDatabaseUsersUserDetails.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def databases(self):
        """Gets the databases of this ShowClickHouseDatabaseUsersUserDetails.

        已授权数据库。

        :return: The databases of this ShowClickHouseDatabaseUsersUserDetails.
        :rtype: list[str]
        """
        return self._databases

    @databases.setter
    def databases(self, databases):
        """Sets the databases of this ShowClickHouseDatabaseUsersUserDetails.

        已授权数据库。

        :param databases: The databases of this ShowClickHouseDatabaseUsersUserDetails.
        :type databases: list[str]
        """
        self._databases = databases

    @property
    def dml(self):
        """Gets the dml of this ShowClickHouseDatabaseUsersUserDetails.

        DML权限。 取值范围： - 1：只读权限 - 2：读取和设置权限

        :return: The dml of this ShowClickHouseDatabaseUsersUserDetails.
        :rtype: int
        """
        return self._dml

    @dml.setter
    def dml(self, dml):
        """Sets the dml of this ShowClickHouseDatabaseUsersUserDetails.

        DML权限。 取值范围： - 1：只读权限 - 2：读取和设置权限

        :param dml: The dml of this ShowClickHouseDatabaseUsersUserDetails.
        :type dml: int
        """
        self._dml = dml

    @property
    def ddl(self):
        """Gets the ddl of this ShowClickHouseDatabaseUsersUserDetails.

        DDL授权。 取值范围： - 0：无DDL权限 - 1：有DDL权限

        :return: The ddl of this ShowClickHouseDatabaseUsersUserDetails.
        :rtype: int
        """
        return self._ddl

    @ddl.setter
    def ddl(self, ddl):
        """Sets the ddl of this ShowClickHouseDatabaseUsersUserDetails.

        DDL授权。 取值范围： - 0：无DDL权限 - 1：有DDL权限

        :param ddl: The ddl of this ShowClickHouseDatabaseUsersUserDetails.
        :type ddl: int
        """
        self._ddl = ddl

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
        if not isinstance(other, ShowClickHouseDatabaseUsersUserDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
