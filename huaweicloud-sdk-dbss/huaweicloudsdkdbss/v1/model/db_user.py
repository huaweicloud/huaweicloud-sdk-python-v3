# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DbUser:

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
        'user_permission': 'str'
    }

    attribute_map = {
        'user_name': 'user_name',
        'user_permission': 'user_permission'
    }

    def __init__(self, user_name=None, user_permission=None):
        r"""DbUser

        The model defined in huaweicloud sdk

        :param user_name: 用户名称
        :type user_name: str
        :param user_permission: 用户权限
        :type user_permission: str
        """
        
        

        self._user_name = None
        self._user_permission = None
        self.discriminator = None

        if user_name is not None:
            self.user_name = user_name
        if user_permission is not None:
            self.user_permission = user_permission

    @property
    def user_name(self):
        r"""Gets the user_name of this DbUser.

        用户名称

        :return: The user_name of this DbUser.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this DbUser.

        用户名称

        :param user_name: The user_name of this DbUser.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def user_permission(self):
        r"""Gets the user_permission of this DbUser.

        用户权限

        :return: The user_permission of this DbUser.
        :rtype: str
        """
        return self._user_permission

    @user_permission.setter
    def user_permission(self, user_permission):
        r"""Sets the user_permission of this DbUser.

        用户权限

        :param user_permission: The user_permission of this DbUser.
        :type user_permission: str
        """
        self._user_permission = user_permission

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DbUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
