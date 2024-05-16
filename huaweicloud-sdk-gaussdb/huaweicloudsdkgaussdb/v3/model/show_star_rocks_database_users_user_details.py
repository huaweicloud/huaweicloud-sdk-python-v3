# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowStarRocksDatabaseUsersUserDetails:

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
        'data_bases': 'list[str]',
        'dml': 'int',
        'ddl': 'int'
    }

    attribute_map = {
        'user_name': 'user_name',
        'data_bases': 'data_bases',
        'dml': 'dml',
        'ddl': 'ddl'
    }

    def __init__(self, user_name=None, data_bases=None, dml=None, ddl=None):
        """ShowStarRocksDatabaseUsersUserDetails

        The model defined in huaweicloud sdk

        :param user_name: 数据库账户名。
        :type user_name: str
        :param data_bases: 已授权数据库。
        :type data_bases: list[str]
        :param dml: DML授权。 - 0：读写权限 - 1：只读权限 - 2：只读和设置权限 - 3：读写和设置权限
        :type dml: int
        :param ddl: DDL授权。 - 0：无DDL权限 - 1：有DDL权限
        :type ddl: int
        """
        
        

        self._user_name = None
        self._data_bases = None
        self._dml = None
        self._ddl = None
        self.discriminator = None

        self.user_name = user_name
        self.data_bases = data_bases
        self.dml = dml
        self.ddl = ddl

    @property
    def user_name(self):
        """Gets the user_name of this ShowStarRocksDatabaseUsersUserDetails.

        数据库账户名。

        :return: The user_name of this ShowStarRocksDatabaseUsersUserDetails.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ShowStarRocksDatabaseUsersUserDetails.

        数据库账户名。

        :param user_name: The user_name of this ShowStarRocksDatabaseUsersUserDetails.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def data_bases(self):
        """Gets the data_bases of this ShowStarRocksDatabaseUsersUserDetails.

        已授权数据库。

        :return: The data_bases of this ShowStarRocksDatabaseUsersUserDetails.
        :rtype: list[str]
        """
        return self._data_bases

    @data_bases.setter
    def data_bases(self, data_bases):
        """Sets the data_bases of this ShowStarRocksDatabaseUsersUserDetails.

        已授权数据库。

        :param data_bases: The data_bases of this ShowStarRocksDatabaseUsersUserDetails.
        :type data_bases: list[str]
        """
        self._data_bases = data_bases

    @property
    def dml(self):
        """Gets the dml of this ShowStarRocksDatabaseUsersUserDetails.

        DML授权。 - 0：读写权限 - 1：只读权限 - 2：只读和设置权限 - 3：读写和设置权限

        :return: The dml of this ShowStarRocksDatabaseUsersUserDetails.
        :rtype: int
        """
        return self._dml

    @dml.setter
    def dml(self, dml):
        """Sets the dml of this ShowStarRocksDatabaseUsersUserDetails.

        DML授权。 - 0：读写权限 - 1：只读权限 - 2：只读和设置权限 - 3：读写和设置权限

        :param dml: The dml of this ShowStarRocksDatabaseUsersUserDetails.
        :type dml: int
        """
        self._dml = dml

    @property
    def ddl(self):
        """Gets the ddl of this ShowStarRocksDatabaseUsersUserDetails.

        DDL授权。 - 0：无DDL权限 - 1：有DDL权限

        :return: The ddl of this ShowStarRocksDatabaseUsersUserDetails.
        :rtype: int
        """
        return self._ddl

    @ddl.setter
    def ddl(self, ddl):
        """Sets the ddl of this ShowStarRocksDatabaseUsersUserDetails.

        DDL授权。 - 0：无DDL权限 - 1：有DDL权限

        :param ddl: The ddl of this ShowStarRocksDatabaseUsersUserDetails.
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
        if not isinstance(other, ShowStarRocksDatabaseUsersUserDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
