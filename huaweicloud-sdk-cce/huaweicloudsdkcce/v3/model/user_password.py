# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'username': 'str',
        'password': 'str'
    }

    attribute_map = {
        'username': 'username',
        'password': 'password'
    }

    def __init__(self, username=None, password=None):
        r"""UserPassword

        The model defined in huaweicloud sdk

        :param username: 登录帐号，默认为“root”
        :type username: str
        :param password: 登录密码，若创建节点通过用户名密码方式，即使用该字段，则响应体中该字段作屏蔽展示。 密码复杂度要求： - 长度为8-26位。 - 密码至少必须包含大写字母、小写字母、数字和特殊字符（!@$%^-_&#x3D;+[{}]:,./?~#*）中的三种。 - 密码不能包含用户名或用户名的逆序。 创建节点时password字段需要加盐加密，具体方法请参见[创建节点时password字段加盐加密](add-salt.xml)。 
        :type password: str
        """
        
        

        self._username = None
        self._password = None
        self.discriminator = None

        if username is not None:
            self.username = username
        self.password = password

    @property
    def username(self):
        r"""Gets the username of this UserPassword.

        登录帐号，默认为“root”

        :return: The username of this UserPassword.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        r"""Sets the username of this UserPassword.

        登录帐号，默认为“root”

        :param username: The username of this UserPassword.
        :type username: str
        """
        self._username = username

    @property
    def password(self):
        r"""Gets the password of this UserPassword.

        登录密码，若创建节点通过用户名密码方式，即使用该字段，则响应体中该字段作屏蔽展示。 密码复杂度要求： - 长度为8-26位。 - 密码至少必须包含大写字母、小写字母、数字和特殊字符（!@$%^-_=+[{}]:,./?~#*）中的三种。 - 密码不能包含用户名或用户名的逆序。 创建节点时password字段需要加盐加密，具体方法请参见[创建节点时password字段加盐加密](add-salt.xml)。 

        :return: The password of this UserPassword.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        r"""Sets the password of this UserPassword.

        登录密码，若创建节点通过用户名密码方式，即使用该字段，则响应体中该字段作屏蔽展示。 密码复杂度要求： - 长度为8-26位。 - 密码至少必须包含大写字母、小写字母、数字和特殊字符（!@$%^-_=+[{}]:,./?~#*）中的三种。 - 密码不能包含用户名或用户名的逆序。 创建节点时password字段需要加盐加密，具体方法请参见[创建节点时password字段加盐加密](add-salt.xml)。 

        :param password: The password of this UserPassword.
        :type password: str
        """
        self._password = password

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
        if not isinstance(other, UserPassword):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
