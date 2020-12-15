# coding: utf-8

import pprint
import re

import six





class UserPassword:


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
        'username': 'str'
    }

    attribute_map = {
        'password': 'password',
        'username': 'username'
    }

    def __init__(self, password=None, username='root'):
        """UserPassword - a model defined in huaweicloud sdk"""
        
        

        self._password = None
        self._username = None
        self.discriminator = None

        self.password = password
        if username is not None:
            self.username = username

    @property
    def password(self):
        """Gets the password of this UserPassword.

        登录密码，取值请参见[创建云服务器](https://support.huaweicloud.com/api-ecs/zh-cn_topic_0020212668.html)中**adminPass**参数的描述。若创建节点通过用户名密码方式，即使用该字段，则响应体中该字段作屏蔽展示。创建节点时password字段需要加盐加密，具体方法请参见[创建节点时password字段加盐加密](https://support.huaweicloud.com/bestpractice-cce/cce_bestpractice_0058.html)。 

        :return: The password of this UserPassword.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this UserPassword.

        登录密码，取值请参见[创建云服务器](https://support.huaweicloud.com/api-ecs/zh-cn_topic_0020212668.html)中**adminPass**参数的描述。若创建节点通过用户名密码方式，即使用该字段，则响应体中该字段作屏蔽展示。创建节点时password字段需要加盐加密，具体方法请参见[创建节点时password字段加盐加密](https://support.huaweicloud.com/bestpractice-cce/cce_bestpractice_0058.html)。 

        :param password: The password of this UserPassword.
        :type: str
        """
        self._password = password

    @property
    def username(self):
        """Gets the username of this UserPassword.

        登录帐号，默认为“root”

        :return: The username of this UserPassword.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UserPassword.

        登录帐号，默认为“root”

        :param username: The username of this UserPassword.
        :type: str
        """
        self._username = username

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
        if not isinstance(other, UserPassword):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
