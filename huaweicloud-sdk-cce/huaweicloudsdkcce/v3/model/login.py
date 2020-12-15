# coding: utf-8

import pprint
import re

import six





class Login:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'ssh_key': 'str',
        'user_password': 'UserPassword'
    }

    attribute_map = {
        'ssh_key': 'sshKey',
        'user_password': 'userPassword'
    }

    def __init__(self, ssh_key=None, user_password=None):
        """Login - a model defined in huaweicloud sdk"""
        
        

        self._ssh_key = None
        self._user_password = None
        self.discriminator = None

        if ssh_key is not None:
            self.ssh_key = ssh_key
        if user_password is not None:
            self.user_password = user_password

    @property
    def ssh_key(self):
        """Gets the ssh_key of this Login.

        选择密钥对方式登录时的密钥对名称。密钥对和密码登录方式二者必选其一。

        :return: The ssh_key of this Login.
        :rtype: str
        """
        return self._ssh_key

    @ssh_key.setter
    def ssh_key(self, ssh_key):
        """Sets the ssh_key of this Login.

        选择密钥对方式登录时的密钥对名称。密钥对和密码登录方式二者必选其一。

        :param ssh_key: The ssh_key of this Login.
        :type: str
        """
        self._ssh_key = ssh_key

    @property
    def user_password(self):
        """Gets the user_password of this Login.


        :return: The user_password of this Login.
        :rtype: UserPassword
        """
        return self._user_password

    @user_password.setter
    def user_password(self, user_password):
        """Sets the user_password of this Login.


        :param user_password: The user_password of this Login.
        :type: UserPassword
        """
        self._user_password = user_password

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
        if not isinstance(other, Login):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
