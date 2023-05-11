# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTablePrivilegesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'database_name': 'str',
        'table_name': 'str',
        'user_name': 'str'
    }

    attribute_map = {
        'database_name': 'database_name',
        'table_name': 'table_name',
        'user_name': 'user_name'
    }

    def __init__(self, database_name=None, table_name=None, user_name=None):
        """ListTablePrivilegesRequest

        The model defined in huaweicloud sdk

        :param database_name: 被查询的数据库名称。
        :type database_name: str
        :param table_name: 被查询的表名称。
        :type table_name: str
        :param user_name: 被查询的用户名称。
        :type user_name: str
        """
        
        

        self._database_name = None
        self._table_name = None
        self._user_name = None
        self.discriminator = None

        self.database_name = database_name
        self.table_name = table_name
        self.user_name = user_name

    @property
    def database_name(self):
        """Gets the database_name of this ListTablePrivilegesRequest.

        被查询的数据库名称。

        :return: The database_name of this ListTablePrivilegesRequest.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """Sets the database_name of this ListTablePrivilegesRequest.

        被查询的数据库名称。

        :param database_name: The database_name of this ListTablePrivilegesRequest.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def table_name(self):
        """Gets the table_name of this ListTablePrivilegesRequest.

        被查询的表名称。

        :return: The table_name of this ListTablePrivilegesRequest.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this ListTablePrivilegesRequest.

        被查询的表名称。

        :param table_name: The table_name of this ListTablePrivilegesRequest.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def user_name(self):
        """Gets the user_name of this ListTablePrivilegesRequest.

        被查询的用户名称。

        :return: The user_name of this ListTablePrivilegesRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ListTablePrivilegesRequest.

        被查询的用户名称。

        :param user_name: The user_name of this ListTablePrivilegesRequest.
        :type user_name: str
        """
        self._user_name = user_name

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
        if not isinstance(other, ListTablePrivilegesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
