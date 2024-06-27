# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClickHouseDatabaseUserPSinfo:

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
        'dml': 'int'
    }

    attribute_map = {
        'user_name': 'user_name',
        'databases': 'databases',
        'dml': 'dml'
    }

    def __init__(self, user_name=None, databases=None, dml=None):
        """ClickHouseDatabaseUserPSinfo

        The model defined in huaweicloud sdk

        :param user_name: 数据库账号名。
        :type user_name: str
        :param databases: 数据库列表。“*”表示所有数据库。
        :type databases: list[str]
        :param dml: DML权限。 取值范围： - 1：只读权限 - 2：读取和设置权限
        :type dml: int
        """
        
        

        self._user_name = None
        self._databases = None
        self._dml = None
        self.discriminator = None

        self.user_name = user_name
        self.databases = databases
        self.dml = dml

    @property
    def user_name(self):
        """Gets the user_name of this ClickHouseDatabaseUserPSinfo.

        数据库账号名。

        :return: The user_name of this ClickHouseDatabaseUserPSinfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ClickHouseDatabaseUserPSinfo.

        数据库账号名。

        :param user_name: The user_name of this ClickHouseDatabaseUserPSinfo.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def databases(self):
        """Gets the databases of this ClickHouseDatabaseUserPSinfo.

        数据库列表。“*”表示所有数据库。

        :return: The databases of this ClickHouseDatabaseUserPSinfo.
        :rtype: list[str]
        """
        return self._databases

    @databases.setter
    def databases(self, databases):
        """Sets the databases of this ClickHouseDatabaseUserPSinfo.

        数据库列表。“*”表示所有数据库。

        :param databases: The databases of this ClickHouseDatabaseUserPSinfo.
        :type databases: list[str]
        """
        self._databases = databases

    @property
    def dml(self):
        """Gets the dml of this ClickHouseDatabaseUserPSinfo.

        DML权限。 取值范围： - 1：只读权限 - 2：读取和设置权限

        :return: The dml of this ClickHouseDatabaseUserPSinfo.
        :rtype: int
        """
        return self._dml

    @dml.setter
    def dml(self, dml):
        """Sets the dml of this ClickHouseDatabaseUserPSinfo.

        DML权限。 取值范围： - 1：只读权限 - 2：读取和设置权限

        :param dml: The dml of this ClickHouseDatabaseUserPSinfo.
        :type dml: int
        """
        self._dml = dml

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
        if not isinstance(other, ClickHouseDatabaseUserPSinfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
