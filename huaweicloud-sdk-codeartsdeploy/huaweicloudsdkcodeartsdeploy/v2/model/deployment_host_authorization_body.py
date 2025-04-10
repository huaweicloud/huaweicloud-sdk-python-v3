# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeploymentHostAuthorizationBody:

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
        'password': 'str',
        'private_key': 'str',
        'trusted_type': 'int'
    }

    attribute_map = {
        'username': 'username',
        'password': 'password',
        'private_key': 'private_key',
        'trusted_type': 'trusted_type'
    }

    def __init__(self, username=None, password=None, private_key=None, trusted_type=None):
        r"""DeploymentHostAuthorizationBody

        The model defined in huaweicloud sdk

        :param username: 用户名，可输入中英文，数字和符号(-_.)。
        :type username: str
        :param password: 密码，认证类型为0时，密码必填。
        :type password: str
        :param private_key: 密钥，认证类型为1时，密钥必填
        :type private_key: str
        :param trusted_type: 认证类型，0表示使用密码认证，1表示使用密钥认证
        :type trusted_type: int
        """
        
        

        self._username = None
        self._password = None
        self._private_key = None
        self._trusted_type = None
        self.discriminator = None

        self.username = username
        if password is not None:
            self.password = password
        if private_key is not None:
            self.private_key = private_key
        self.trusted_type = trusted_type

    @property
    def username(self):
        r"""Gets the username of this DeploymentHostAuthorizationBody.

        用户名，可输入中英文，数字和符号(-_.)。

        :return: The username of this DeploymentHostAuthorizationBody.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        r"""Sets the username of this DeploymentHostAuthorizationBody.

        用户名，可输入中英文，数字和符号(-_.)。

        :param username: The username of this DeploymentHostAuthorizationBody.
        :type username: str
        """
        self._username = username

    @property
    def password(self):
        r"""Gets the password of this DeploymentHostAuthorizationBody.

        密码，认证类型为0时，密码必填。

        :return: The password of this DeploymentHostAuthorizationBody.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        r"""Sets the password of this DeploymentHostAuthorizationBody.

        密码，认证类型为0时，密码必填。

        :param password: The password of this DeploymentHostAuthorizationBody.
        :type password: str
        """
        self._password = password

    @property
    def private_key(self):
        r"""Gets the private_key of this DeploymentHostAuthorizationBody.

        密钥，认证类型为1时，密钥必填

        :return: The private_key of this DeploymentHostAuthorizationBody.
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        r"""Sets the private_key of this DeploymentHostAuthorizationBody.

        密钥，认证类型为1时，密钥必填

        :param private_key: The private_key of this DeploymentHostAuthorizationBody.
        :type private_key: str
        """
        self._private_key = private_key

    @property
    def trusted_type(self):
        r"""Gets the trusted_type of this DeploymentHostAuthorizationBody.

        认证类型，0表示使用密码认证，1表示使用密钥认证

        :return: The trusted_type of this DeploymentHostAuthorizationBody.
        :rtype: int
        """
        return self._trusted_type

    @trusted_type.setter
    def trusted_type(self, trusted_type):
        r"""Sets the trusted_type of this DeploymentHostAuthorizationBody.

        认证类型，0表示使用密码认证，1表示使用密钥认证

        :param trusted_type: The trusted_type of this DeploymentHostAuthorizationBody.
        :type trusted_type: int
        """
        self._trusted_type = trusted_type

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
        if not isinstance(other, DeploymentHostAuthorizationBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
