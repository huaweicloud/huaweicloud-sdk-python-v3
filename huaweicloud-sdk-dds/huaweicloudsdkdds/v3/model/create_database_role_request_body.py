# coding: utf-8

import pprint
import re

import six





class CreateDatabaseRoleRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'role_name': 'str',
        'db_name': 'str',
        'roles': 'RolesOption'
    }

    attribute_map = {
        'role_name': 'role_name',
        'db_name': 'db_name',
        'roles': 'roles'
    }

    def __init__(self, role_name=None, db_name=None, roles=None):
        """CreateDatabaseRoleRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._role_name = None
        self._db_name = None
        self._roles = None
        self.discriminator = None

        self.role_name = role_name
        if db_name is not None:
            self.db_name = db_name
        if roles is not None:
            self.roles = roles

    @property
    def role_name(self):
        """Gets the role_name of this CreateDatabaseRoleRequestBody.

        创建角色名称。 - 长度为1~64位，可以包含大写字母（A~Z）、小写字母（a~z）、数字（0~9）、中划线、下划线和点。

        :return: The role_name of this CreateDatabaseRoleRequestBody.
        :rtype: str
        """
        return self._role_name

    @role_name.setter
    def role_name(self, role_name):
        """Sets the role_name of this CreateDatabaseRoleRequestBody.

        创建角色名称。 - 长度为1~64位，可以包含大写字母（A~Z）、小写字母（a~z）、数字（0~9）、中划线、下划线和点。

        :param role_name: The role_name of this CreateDatabaseRoleRequestBody.
        :type: str
        """
        self._role_name = role_name

    @property
    def db_name(self):
        """Gets the db_name of this CreateDatabaseRoleRequestBody.

        角色所在的数据库名称，默认admin。 - 长度为1~64位，可以包含大写字母（A~Z）、小写字母（a~z）、数字（0~9）、下划线。

        :return: The db_name of this CreateDatabaseRoleRequestBody.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """Sets the db_name of this CreateDatabaseRoleRequestBody.

        角色所在的数据库名称，默认admin。 - 长度为1~64位，可以包含大写字母（A~Z）、小写字母（a~z）、数字（0~9）、下划线。

        :param db_name: The db_name of this CreateDatabaseRoleRequestBody.
        :type: str
        """
        self._db_name = db_name

    @property
    def roles(self):
        """Gets the roles of this CreateDatabaseRoleRequestBody.


        :return: The roles of this CreateDatabaseRoleRequestBody.
        :rtype: RolesOption
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this CreateDatabaseRoleRequestBody.


        :param roles: The roles of this CreateDatabaseRoleRequestBody.
        :type: RolesOption
        """
        self._roles = roles

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
        if not isinstance(other, CreateDatabaseRoleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
