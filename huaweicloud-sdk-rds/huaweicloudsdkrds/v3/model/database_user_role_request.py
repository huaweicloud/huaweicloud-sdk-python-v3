# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DatabaseUserRoleRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user': 'str',
        'roles': 'list[str]'
    }

    attribute_map = {
        'user': 'user',
        'roles': 'roles'
    }

    def __init__(self, user=None, roles=None):
        r"""DatabaseUserRoleRequest

        The model defined in huaweicloud sdk

        :param user: 用户名称
        :type user: str
        :param roles: 角色名称
        :type roles: list[str]
        """
        
        

        self._user = None
        self._roles = None
        self.discriminator = None

        self.user = user
        self.roles = roles

    @property
    def user(self):
        r"""Gets the user of this DatabaseUserRoleRequest.

        用户名称

        :return: The user of this DatabaseUserRoleRequest.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this DatabaseUserRoleRequest.

        用户名称

        :param user: The user of this DatabaseUserRoleRequest.
        :type user: str
        """
        self._user = user

    @property
    def roles(self):
        r"""Gets the roles of this DatabaseUserRoleRequest.

        角色名称

        :return: The roles of this DatabaseUserRoleRequest.
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        r"""Sets the roles of this DatabaseUserRoleRequest.

        角色名称

        :param roles: The roles of this DatabaseUserRoleRequest.
        :type roles: list[str]
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
        if not isinstance(other, DatabaseUserRoleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
