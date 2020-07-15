# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class CheckTokenResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'access_token': 'str',
        'token_ip': 'str',
        'valid_period': 'int',
        'expire_time': 'int',
        'user': 'UserInfo',
        'client_type': 'int',
        'force_login_ind': 'int',
        'first_login': 'bool',
        'pwd_expired': 'bool',
        'days_pwd_available': 'int'
    }

    attribute_map = {
        'access_token': 'accessToken',
        'token_ip': 'tokenIp',
        'valid_period': 'validPeriod',
        'expire_time': 'expireTime',
        'user': 'user',
        'client_type': 'clientType',
        'force_login_ind': 'forceLoginInd',
        'first_login': 'firstLogin',
        'pwd_expired': 'pwdExpired',
        'days_pwd_available': 'daysPwdAvailable'
    }

    def __init__(self, access_token=None, token_ip=None, valid_period=None, expire_time=None, user=None, client_type=None, force_login_ind=None, first_login=False, pwd_expired=False, days_pwd_available=None):
        """CheckTokenResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._access_token = None
        self._token_ip = None
        self._valid_period = None
        self._expire_time = None
        self._user = None
        self._client_type = None
        self._force_login_ind = None
        self._first_login = None
        self._pwd_expired = None
        self._days_pwd_available = None
        self.discriminator = None

        if access_token is not None:
            self.access_token = access_token
        if token_ip is not None:
            self.token_ip = token_ip
        if valid_period is not None:
            self.valid_period = valid_period
        if expire_time is not None:
            self.expire_time = expire_time
        if user is not None:
            self.user = user
        if client_type is not None:
            self.client_type = client_type
        if force_login_ind is not None:
            self.force_login_ind = force_login_ind
        if first_login is not None:
            self.first_login = first_login
        if pwd_expired is not None:
            self.pwd_expired = pwd_expired
        if days_pwd_available is not None:
            self.days_pwd_available = days_pwd_available

    @property
    def access_token(self):
        """Gets the access_token of this CheckTokenResponse.

        接入token字符串。

        :return: The access_token of this CheckTokenResponse.
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this CheckTokenResponse.

        接入token字符串。

        :param access_token: The access_token of this CheckTokenResponse.
        :type: str
        """
        self._access_token = access_token

    @property
    def token_ip(self):
        """Gets the token_ip of this CheckTokenResponse.

        用户IP。

        :return: The token_ip of this CheckTokenResponse.
        :rtype: str
        """
        return self._token_ip

    @token_ip.setter
    def token_ip(self, token_ip):
        """Sets the token_ip of this CheckTokenResponse.

        用户IP。

        :param token_ip: The token_ip of this CheckTokenResponse.
        :type: str
        """
        self._token_ip = token_ip

    @property
    def valid_period(self):
        """Gets the valid_period of this CheckTokenResponse.

        token有效时长，单位：秒。

        :return: The valid_period of this CheckTokenResponse.
        :rtype: int
        """
        return self._valid_period

    @valid_period.setter
    def valid_period(self, valid_period):
        """Sets the valid_period of this CheckTokenResponse.

        token有效时长，单位：秒。

        :param valid_period: The valid_period of this CheckTokenResponse.
        :type: int
        """
        self._valid_period = valid_period

    @property
    def expire_time(self):
        """Gets the expire_time of this CheckTokenResponse.

        token的失效时间戳，单位：秒。

        :return: The expire_time of this CheckTokenResponse.
        :rtype: int
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this CheckTokenResponse.

        token的失效时间戳，单位：秒。

        :param expire_time: The expire_time of this CheckTokenResponse.
        :type: int
        """
        self._expire_time = expire_time

    @property
    def user(self):
        """Gets the user of this CheckTokenResponse.


        :return: The user of this CheckTokenResponse.
        :rtype: UserInfo
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this CheckTokenResponse.


        :param user: The user of this CheckTokenResponse.
        :type: UserInfo
        """
        self._user = user

    @property
    def client_type(self):
        """Gets the client_type of this CheckTokenResponse.

        登录帐号类型。 * 0：Web客户端类型； * 5：cloudlink pc； * 6：cloudlink mobile； * 16：workplace pc 

        :return: The client_type of this CheckTokenResponse.
        :rtype: int
        """
        return self._client_type

    @client_type.setter
    def client_type(self, client_type):
        """Sets the client_type of this CheckTokenResponse.

        登录帐号类型。 * 0：Web客户端类型； * 5：cloudlink pc； * 6：cloudlink mobile； * 16：workplace pc 

        :param client_type: The client_type of this CheckTokenResponse.
        :type: int
        """
        self._client_type = client_type

    @property
    def force_login_ind(self):
        """Gets the force_login_ind of this CheckTokenResponse.

        抢占登录标识 * 0：非抢占 * 1：抢占  未启用 

        :return: The force_login_ind of this CheckTokenResponse.
        :rtype: int
        """
        return self._force_login_ind

    @force_login_ind.setter
    def force_login_ind(self, force_login_ind):
        """Sets the force_login_ind of this CheckTokenResponse.

        抢占登录标识 * 0：非抢占 * 1：抢占  未启用 

        :param force_login_ind: The force_login_ind of this CheckTokenResponse.
        :type: int
        """
        self._force_login_ind = force_login_ind

    @property
    def first_login(self):
        """Gets the first_login of this CheckTokenResponse.

        是否首次登录（说明：首次登录表示尚未修改过密码。首次登录时，系统会提醒用户需要修改密码），默认值：false。

        :return: The first_login of this CheckTokenResponse.
        :rtype: bool
        """
        return self._first_login

    @first_login.setter
    def first_login(self, first_login):
        """Sets the first_login of this CheckTokenResponse.

        是否首次登录（说明：首次登录表示尚未修改过密码。首次登录时，系统会提醒用户需要修改密码），默认值：false。

        :param first_login: The first_login of this CheckTokenResponse.
        :type: bool
        """
        self._first_login = first_login

    @property
    def pwd_expired(self):
        """Gets the pwd_expired of this CheckTokenResponse.

        密码是否过期，默认值：false。

        :return: The pwd_expired of this CheckTokenResponse.
        :rtype: bool
        """
        return self._pwd_expired

    @pwd_expired.setter
    def pwd_expired(self, pwd_expired):
        """Sets the pwd_expired of this CheckTokenResponse.

        密码是否过期，默认值：false。

        :param pwd_expired: The pwd_expired of this CheckTokenResponse.
        :type: bool
        """
        self._pwd_expired = pwd_expired

    @property
    def days_pwd_available(self):
        """Gets the days_pwd_available of this CheckTokenResponse.

        密码有效天数

        :return: The days_pwd_available of this CheckTokenResponse.
        :rtype: int
        """
        return self._days_pwd_available

    @days_pwd_available.setter
    def days_pwd_available(self, days_pwd_available):
        """Sets the days_pwd_available of this CheckTokenResponse.

        密码有效天数

        :param days_pwd_available: The days_pwd_available of this CheckTokenResponse.
        :type: int
        """
        self._days_pwd_available = days_pwd_available

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
        if not isinstance(other, CheckTokenResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
