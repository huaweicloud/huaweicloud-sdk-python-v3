# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangePasswordRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'new_password': 'str',
        'user_name': 'str'
    }

    attribute_map = {
        'new_password': 'new_password',
        'user_name': 'user_name'
    }

    def __init__(self, new_password=None, user_name=None):
        r"""ChangePasswordRequest

        The model defined in huaweicloud sdk

        :param new_password: 新密码
        :type new_password: str
        :param user_name: 用户名
        :type user_name: str
        """
        
        

        self._new_password = None
        self._user_name = None
        self.discriminator = None

        self.new_password = new_password
        self.user_name = user_name

    @property
    def new_password(self):
        r"""Gets the new_password of this ChangePasswordRequest.

        新密码

        :return: The new_password of this ChangePasswordRequest.
        :rtype: str
        """
        return self._new_password

    @new_password.setter
    def new_password(self, new_password):
        r"""Sets the new_password of this ChangePasswordRequest.

        新密码

        :param new_password: The new_password of this ChangePasswordRequest.
        :type new_password: str
        """
        self._new_password = new_password

    @property
    def user_name(self):
        r"""Gets the user_name of this ChangePasswordRequest.

        用户名

        :return: The user_name of this ChangePasswordRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ChangePasswordRequest.

        用户名

        :param user_name: The user_name of this ChangePasswordRequest.
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
        if not isinstance(other, ChangePasswordRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
