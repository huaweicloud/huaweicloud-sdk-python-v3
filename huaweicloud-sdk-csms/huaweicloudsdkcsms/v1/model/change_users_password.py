# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeUsersPassword:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'password': 'str',
        'old_password': 'str'
    }

    attribute_map = {
        'password': 'password',
        'old_password': 'old_password'
    }

    def __init__(self, password=None, old_password=None):
        r"""ChangeUsersPassword

        The model defined in huaweicloud sdk

        :param password: 新密码。
        :type password: str
        :param old_password: 旧密码。
        :type old_password: str
        """
        
        

        self._password = None
        self._old_password = None
        self.discriminator = None

        self.password = password
        self.old_password = old_password

    @property
    def password(self):
        r"""Gets the password of this ChangeUsersPassword.

        新密码。

        :return: The password of this ChangeUsersPassword.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        r"""Sets the password of this ChangeUsersPassword.

        新密码。

        :param password: The password of this ChangeUsersPassword.
        :type password: str
        """
        self._password = password

    @property
    def old_password(self):
        r"""Gets the old_password of this ChangeUsersPassword.

        旧密码。

        :return: The old_password of this ChangeUsersPassword.
        :rtype: str
        """
        return self._old_password

    @old_password.setter
    def old_password(self, old_password):
        r"""Sets the old_password of this ChangeUsersPassword.

        旧密码。

        :param old_password: The old_password of this ChangeUsersPassword.
        :type old_password: str
        """
        self._old_password = old_password

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
        if not isinstance(other, ChangeUsersPassword):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
