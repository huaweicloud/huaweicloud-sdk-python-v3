# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RetryLoginInfo:

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
        'is_save_password': 'bool'
    }

    attribute_map = {
        'username': 'username',
        'password': 'password',
        'is_save_password': 'is_save_password'
    }

    def __init__(self, username=None, password=None, is_save_password=None):
        r"""RetryLoginInfo

        The model defined in huaweicloud sdk

        :param username: 登录数据库的用户名
        :type username: str
        :param password: 登录数据库的密码
        :type password: str
        :param is_save_password: 是否保存密码
        :type is_save_password: bool
        """
        
        

        self._username = None
        self._password = None
        self._is_save_password = None
        self.discriminator = None

        if username is not None:
            self.username = username
        self.password = password
        self.is_save_password = is_save_password

    @property
    def username(self):
        r"""Gets the username of this RetryLoginInfo.

        登录数据库的用户名

        :return: The username of this RetryLoginInfo.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        r"""Sets the username of this RetryLoginInfo.

        登录数据库的用户名

        :param username: The username of this RetryLoginInfo.
        :type username: str
        """
        self._username = username

    @property
    def password(self):
        r"""Gets the password of this RetryLoginInfo.

        登录数据库的密码

        :return: The password of this RetryLoginInfo.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        r"""Sets the password of this RetryLoginInfo.

        登录数据库的密码

        :param password: The password of this RetryLoginInfo.
        :type password: str
        """
        self._password = password

    @property
    def is_save_password(self):
        r"""Gets the is_save_password of this RetryLoginInfo.

        是否保存密码

        :return: The is_save_password of this RetryLoginInfo.
        :rtype: bool
        """
        return self._is_save_password

    @is_save_password.setter
    def is_save_password(self, is_save_password):
        r"""Sets the is_save_password of this RetryLoginInfo.

        是否保存密码

        :param is_save_password: The is_save_password of this RetryLoginInfo.
        :type is_save_password: bool
        """
        self._is_save_password = is_save_password

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
        if not isinstance(other, RetryLoginInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
