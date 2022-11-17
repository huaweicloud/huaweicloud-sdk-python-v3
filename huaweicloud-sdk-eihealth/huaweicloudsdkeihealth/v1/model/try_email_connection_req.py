# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TryEmailConnectionReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server': 'str',
        'user_name': 'str',
        'password': 'str',
        'email': 'str',
        'language': 'LanguageEnum'
    }

    attribute_map = {
        'server': 'server',
        'user_name': 'user_name',
        'password': 'password',
        'email': 'email',
        'language': 'language'
    }

    def __init__(self, server=None, user_name=None, password=None, email=None, language=None):
        """TryEmailConnectionReq

        The model defined in huaweicloud sdk

        :param server: 服务器地址
        :type server: str
        :param user_name: 用户名
        :type user_name: str
        :param password: 密码
        :type password: str
        :param email: 邮箱
        :type email: str
        :param language: 
        :type language: :class:`huaweicloudsdkeihealth.v1.LanguageEnum`
        """
        
        

        self._server = None
        self._user_name = None
        self._password = None
        self._email = None
        self._language = None
        self.discriminator = None

        self.server = server
        self.user_name = user_name
        self.password = password
        self.email = email
        self.language = language

    @property
    def server(self):
        """Gets the server of this TryEmailConnectionReq.

        服务器地址

        :return: The server of this TryEmailConnectionReq.
        :rtype: str
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this TryEmailConnectionReq.

        服务器地址

        :param server: The server of this TryEmailConnectionReq.
        :type server: str
        """
        self._server = server

    @property
    def user_name(self):
        """Gets the user_name of this TryEmailConnectionReq.

        用户名

        :return: The user_name of this TryEmailConnectionReq.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this TryEmailConnectionReq.

        用户名

        :param user_name: The user_name of this TryEmailConnectionReq.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def password(self):
        """Gets the password of this TryEmailConnectionReq.

        密码

        :return: The password of this TryEmailConnectionReq.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this TryEmailConnectionReq.

        密码

        :param password: The password of this TryEmailConnectionReq.
        :type password: str
        """
        self._password = password

    @property
    def email(self):
        """Gets the email of this TryEmailConnectionReq.

        邮箱

        :return: The email of this TryEmailConnectionReq.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this TryEmailConnectionReq.

        邮箱

        :param email: The email of this TryEmailConnectionReq.
        :type email: str
        """
        self._email = email

    @property
    def language(self):
        """Gets the language of this TryEmailConnectionReq.

        :return: The language of this TryEmailConnectionReq.
        :rtype: :class:`huaweicloudsdkeihealth.v1.LanguageEnum`
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this TryEmailConnectionReq.

        :param language: The language of this TryEmailConnectionReq.
        :type language: :class:`huaweicloudsdkeihealth.v1.LanguageEnum`
        """
        self._language = language

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
        if not isinstance(other, TryEmailConnectionReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
