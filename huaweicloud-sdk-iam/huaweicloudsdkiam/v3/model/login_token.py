# coding: utf-8

import pprint
import re

import six





class LoginToken:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'expires_at': 'str',
        'method': 'str',
        'user_id': 'str',
        'user_name': 'str',
        'session_id': 'str',
        'session_name': 'str',
        'assumed_by': 'LoginTokenAssumedBy'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'expires_at': 'expires_at',
        'method': 'method',
        'user_id': 'user_id',
        'user_name': 'user_name',
        'session_id': 'session_id',
        'session_name': 'session_name',
        'assumed_by': 'assumed_by'
    }

    def __init__(self, domain_id=None, expires_at=None, method=None, user_id=None, user_name=None, session_id=None, session_name=None, assumed_by=None):
        """LoginToken - a model defined in huaweicloud sdk"""
        
        

        self._domain_id = None
        self._expires_at = None
        self._method = None
        self._user_id = None
        self._user_name = None
        self._session_id = None
        self._session_name = None
        self._assumed_by = None
        self.discriminator = None

        self.domain_id = domain_id
        self.expires_at = expires_at
        self.method = method
        self.user_id = user_id
        self.user_name = user_name
        self.session_id = session_id
        if session_name is not None:
            self.session_name = session_name
        if assumed_by is not None:
            self.assumed_by = assumed_by

    @property
    def domain_id(self):
        """Gets the domain_id of this LoginToken.

        账号ID。

        :return: The domain_id of this LoginToken.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this LoginToken.

        账号ID。

        :param domain_id: The domain_id of this LoginToken.
        :type: str
        """
        self._domain_id = domain_id

    @property
    def expires_at(self):
        """Gets the expires_at of this LoginToken.

        logintoken的过期时间，默认10min。

        :return: The expires_at of this LoginToken.
        :rtype: str
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """Sets the expires_at of this LoginToken.

        logintoken的过期时间，默认10min。

        :param expires_at: The expires_at of this LoginToken.
        :type: str
        """
        self._expires_at = expires_at

    @property
    def method(self):
        """Gets the method of this LoginToken.

        认证方法。当认证用户为华为云用户时，该字段内容为“token”，当认证用户为自定义代理用户时，该字段内容为“federation_proxy”。

        :return: The method of this LoginToken.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this LoginToken.

        认证方法。当认证用户为华为云用户时，该字段内容为“token”，当认证用户为自定义代理用户时，该字段内容为“federation_proxy”。

        :param method: The method of this LoginToken.
        :type: str
        """
        self._method = method

    @property
    def user_id(self):
        """Gets the user_id of this LoginToken.

        用户ID。

        :return: The user_id of this LoginToken.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this LoginToken.

        用户ID。

        :param user_id: The user_id of this LoginToken.
        :type: str
        """
        self._user_id = user_id

    @property
    def user_name(self):
        """Gets the user_name of this LoginToken.

        用户名。

        :return: The user_name of this LoginToken.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this LoginToken.

        用户名。

        :param user_name: The user_name of this LoginToken.
        :type: str
        """
        self._user_name = user_name

    @property
    def session_id(self):
        """Gets the session_id of this LoginToken.

        会话ID。

        :return: The session_id of this LoginToken.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this LoginToken.

        会话ID。

        :param session_id: The session_id of this LoginToken.
        :type: str
        """
        self._session_id = session_id

    @property
    def session_name(self):
        """Gets the session_name of this LoginToken.

        自定义代理用户名。 > - [通过委托获取临时访问密钥和securitytoken](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=IAM&api=CreateTemporaryAccessKeyByAgency)且请求体中填写session_user.name参数时，会返回该字段。该字段的值即为session_user.name所填写的值。

        :return: The session_name of this LoginToken.
        :rtype: str
        """
        return self._session_name

    @session_name.setter
    def session_name(self, session_name):
        """Sets the session_name of this LoginToken.

        自定义代理用户名。 > - [通过委托获取临时访问密钥和securitytoken](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=IAM&api=CreateTemporaryAccessKeyByAgency)且请求体中填写session_user.name参数时，会返回该字段。该字段的值即为session_user.name所填写的值。

        :param session_name: The session_name of this LoginToken.
        :type: str
        """
        self._session_name = session_name

    @property
    def assumed_by(self):
        """Gets the assumed_by of this LoginToken.


        :return: The assumed_by of this LoginToken.
        :rtype: LoginTokenAssumedBy
        """
        return self._assumed_by

    @assumed_by.setter
    def assumed_by(self, assumed_by):
        """Sets the assumed_by of this LoginToken.


        :param assumed_by: The assumed_by of this LoginToken.
        :type: LoginTokenAssumedBy
        """
        self._assumed_by = assumed_by

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
        if not isinstance(other, LoginToken):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
