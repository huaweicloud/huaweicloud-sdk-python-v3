# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CasAuthenticationSuccessAttributes:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'authentication_date': 'str',
        'long_term_authentication_request_token_used': 'bool',
        'is_from_new_login': 'bool',
        'token': 'str',
        'logo': 'str',
        'display_name': 'str',
        'uid': 'str'
    }

    attribute_map = {
        'authentication_date': 'authenticationDate',
        'long_term_authentication_request_token_used': 'longTermAuthenticationRequestTokenUsed',
        'is_from_new_login': 'isFromNewLogin',
        'token': 'token',
        'logo': 'logo',
        'display_name': 'displayName',
        'uid': 'uid'
    }

    def __init__(self, authentication_date=None, long_term_authentication_request_token_used=None, is_from_new_login=None, token=None, logo=None, display_name=None, uid=None):
        r"""CasAuthenticationSuccessAttributes

        The model defined in huaweicloud sdk

        :param authentication_date: 认证时间
        :type authentication_date: str
        :param long_term_authentication_request_token_used: longTermAuthenticationRequestTokenUsed
        :type long_term_authentication_request_token_used: bool
        :param is_from_new_login: isFromNewLogin
        :type is_from_new_login: bool
        :param token: 用户获取用户信息的token
        :type token: str
        :param logo: 用户头像URL
        :type logo: str
        :param display_name: 用户显示名
        :type display_name: str
        :param uid: 华为账号uid
        :type uid: str
        """
        
        

        self._authentication_date = None
        self._long_term_authentication_request_token_used = None
        self._is_from_new_login = None
        self._token = None
        self._logo = None
        self._display_name = None
        self._uid = None
        self.discriminator = None

        if authentication_date is not None:
            self.authentication_date = authentication_date
        if long_term_authentication_request_token_used is not None:
            self.long_term_authentication_request_token_used = long_term_authentication_request_token_used
        if is_from_new_login is not None:
            self.is_from_new_login = is_from_new_login
        if token is not None:
            self.token = token
        if logo is not None:
            self.logo = logo
        if display_name is not None:
            self.display_name = display_name
        if uid is not None:
            self.uid = uid

    @property
    def authentication_date(self):
        r"""Gets the authentication_date of this CasAuthenticationSuccessAttributes.

        认证时间

        :return: The authentication_date of this CasAuthenticationSuccessAttributes.
        :rtype: str
        """
        return self._authentication_date

    @authentication_date.setter
    def authentication_date(self, authentication_date):
        r"""Sets the authentication_date of this CasAuthenticationSuccessAttributes.

        认证时间

        :param authentication_date: The authentication_date of this CasAuthenticationSuccessAttributes.
        :type authentication_date: str
        """
        self._authentication_date = authentication_date

    @property
    def long_term_authentication_request_token_used(self):
        r"""Gets the long_term_authentication_request_token_used of this CasAuthenticationSuccessAttributes.

        longTermAuthenticationRequestTokenUsed

        :return: The long_term_authentication_request_token_used of this CasAuthenticationSuccessAttributes.
        :rtype: bool
        """
        return self._long_term_authentication_request_token_used

    @long_term_authentication_request_token_used.setter
    def long_term_authentication_request_token_used(self, long_term_authentication_request_token_used):
        r"""Sets the long_term_authentication_request_token_used of this CasAuthenticationSuccessAttributes.

        longTermAuthenticationRequestTokenUsed

        :param long_term_authentication_request_token_used: The long_term_authentication_request_token_used of this CasAuthenticationSuccessAttributes.
        :type long_term_authentication_request_token_used: bool
        """
        self._long_term_authentication_request_token_used = long_term_authentication_request_token_used

    @property
    def is_from_new_login(self):
        r"""Gets the is_from_new_login of this CasAuthenticationSuccessAttributes.

        isFromNewLogin

        :return: The is_from_new_login of this CasAuthenticationSuccessAttributes.
        :rtype: bool
        """
        return self._is_from_new_login

    @is_from_new_login.setter
    def is_from_new_login(self, is_from_new_login):
        r"""Sets the is_from_new_login of this CasAuthenticationSuccessAttributes.

        isFromNewLogin

        :param is_from_new_login: The is_from_new_login of this CasAuthenticationSuccessAttributes.
        :type is_from_new_login: bool
        """
        self._is_from_new_login = is_from_new_login

    @property
    def token(self):
        r"""Gets the token of this CasAuthenticationSuccessAttributes.

        用户获取用户信息的token

        :return: The token of this CasAuthenticationSuccessAttributes.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        r"""Sets the token of this CasAuthenticationSuccessAttributes.

        用户获取用户信息的token

        :param token: The token of this CasAuthenticationSuccessAttributes.
        :type token: str
        """
        self._token = token

    @property
    def logo(self):
        r"""Gets the logo of this CasAuthenticationSuccessAttributes.

        用户头像URL

        :return: The logo of this CasAuthenticationSuccessAttributes.
        :rtype: str
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        r"""Sets the logo of this CasAuthenticationSuccessAttributes.

        用户头像URL

        :param logo: The logo of this CasAuthenticationSuccessAttributes.
        :type logo: str
        """
        self._logo = logo

    @property
    def display_name(self):
        r"""Gets the display_name of this CasAuthenticationSuccessAttributes.

        用户显示名

        :return: The display_name of this CasAuthenticationSuccessAttributes.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this CasAuthenticationSuccessAttributes.

        用户显示名

        :param display_name: The display_name of this CasAuthenticationSuccessAttributes.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def uid(self):
        r"""Gets the uid of this CasAuthenticationSuccessAttributes.

        华为账号uid

        :return: The uid of this CasAuthenticationSuccessAttributes.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        r"""Sets the uid of this CasAuthenticationSuccessAttributes.

        华为账号uid

        :param uid: The uid of this CasAuthenticationSuccessAttributes.
        :type uid: str
        """
        self._uid = uid

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
        if not isinstance(other, CasAuthenticationSuccessAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
