# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'create_time': 'int',
        'user': 'UserInfo',
        'client_type': 'int',
        'force_login_ind': 'int',
        'first_login': 'bool',
        'pwd_expired': 'bool',
        'days_pwd_available': 'int',
        'proxy_token': 'ProxyTokenDTO',
        'delay_delete': 'bool',
        'token_type': 'int',
        'refresh_token': 'str',
        'refresh_valid_period': 'int',
        'refresh_expire_time': 'int',
        'refresh_create_time': 'int'
    }

    attribute_map = {
        'access_token': 'accessToken',
        'token_ip': 'tokenIp',
        'valid_period': 'validPeriod',
        'expire_time': 'expireTime',
        'create_time': 'createTime',
        'user': 'user',
        'client_type': 'clientType',
        'force_login_ind': 'forceLoginInd',
        'first_login': 'firstLogin',
        'pwd_expired': 'pwdExpired',
        'days_pwd_available': 'daysPwdAvailable',
        'proxy_token': 'proxyToken',
        'delay_delete': 'delayDelete',
        'token_type': 'tokenType',
        'refresh_token': 'refreshToken',
        'refresh_valid_period': 'refreshValidPeriod',
        'refresh_expire_time': 'refreshExpireTime',
        'refresh_create_time': 'refreshCreateTime'
    }

    def __init__(self, access_token=None, token_ip=None, valid_period=None, expire_time=None, create_time=None, user=None, client_type=None, force_login_ind=None, first_login=None, pwd_expired=None, days_pwd_available=None, proxy_token=None, delay_delete=None, token_type=None, refresh_token=None, refresh_valid_period=None, refresh_expire_time=None, refresh_create_time=None):
        """CheckTokenResponse

        The model defined in huaweicloud sdk

        :param access_token: Access Token字符串。
        :type access_token: str
        :param token_ip: 用户IP。
        :type token_ip: str
        :param valid_period: Access Token有效时长，单位：秒。
        :type valid_period: int
        :param expire_time: Access Token的失效时间戳，单位：秒。
        :type expire_time: int
        :param create_time: Access Token的创建时间戳，单位：毫秒。
        :type create_time: int
        :param user: 
        :type user: :class:`huaweicloudsdkmeeting.v1.UserInfo`
        :param client_type: 登录帐号类型。 * 72：API调用类型 
        :type client_type: int
        :param force_login_ind: 抢占登录标识。 * 0： 非抢占 * 1： 抢占 
        :type force_login_ind: int
        :param first_login: 是否首次登录。 &gt; 首次登录表示尚未修改过密码。首次登录时，系统会提醒用户需要修改密码。 默认值：false。 
        :type first_login: bool
        :param pwd_expired: 密码是否过期，默认值：false。
        :type pwd_expired: bool
        :param days_pwd_available: 密码有效天数。
        :type days_pwd_available: int
        :param proxy_token: 
        :type proxy_token: :class:`huaweicloudsdkmeeting.v1.ProxyTokenDTO`
        :param delay_delete: 是否延时删除状态。
        :type delay_delete: bool
        :param token_type: Token类型。 * 0：用户Access Token * 1：会控TOKEN * 2：一次性TOKEN 
        :type token_type: int
        :param refresh_token: Refresh Token字符串。
        :type refresh_token: str
        :param refresh_valid_period: Refresh Token有效时长，单位：秒。
        :type refresh_valid_period: int
        :param refresh_expire_time: Refresh Token的失效时间戳，单位：秒。
        :type refresh_expire_time: int
        :param refresh_create_time: Refresh Token的创建时间戳，单位：毫秒。
        :type refresh_create_time: int
        """
        
        super(CheckTokenResponse, self).__init__()

        self._access_token = None
        self._token_ip = None
        self._valid_period = None
        self._expire_time = None
        self._create_time = None
        self._user = None
        self._client_type = None
        self._force_login_ind = None
        self._first_login = None
        self._pwd_expired = None
        self._days_pwd_available = None
        self._proxy_token = None
        self._delay_delete = None
        self._token_type = None
        self._refresh_token = None
        self._refresh_valid_period = None
        self._refresh_expire_time = None
        self._refresh_create_time = None
        self.discriminator = None

        if access_token is not None:
            self.access_token = access_token
        if token_ip is not None:
            self.token_ip = token_ip
        if valid_period is not None:
            self.valid_period = valid_period
        if expire_time is not None:
            self.expire_time = expire_time
        if create_time is not None:
            self.create_time = create_time
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
        if proxy_token is not None:
            self.proxy_token = proxy_token
        if delay_delete is not None:
            self.delay_delete = delay_delete
        if token_type is not None:
            self.token_type = token_type
        if refresh_token is not None:
            self.refresh_token = refresh_token
        if refresh_valid_period is not None:
            self.refresh_valid_period = refresh_valid_period
        if refresh_expire_time is not None:
            self.refresh_expire_time = refresh_expire_time
        if refresh_create_time is not None:
            self.refresh_create_time = refresh_create_time

    @property
    def access_token(self):
        """Gets the access_token of this CheckTokenResponse.

        Access Token字符串。

        :return: The access_token of this CheckTokenResponse.
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this CheckTokenResponse.

        Access Token字符串。

        :param access_token: The access_token of this CheckTokenResponse.
        :type access_token: str
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
        :type token_ip: str
        """
        self._token_ip = token_ip

    @property
    def valid_period(self):
        """Gets the valid_period of this CheckTokenResponse.

        Access Token有效时长，单位：秒。

        :return: The valid_period of this CheckTokenResponse.
        :rtype: int
        """
        return self._valid_period

    @valid_period.setter
    def valid_period(self, valid_period):
        """Sets the valid_period of this CheckTokenResponse.

        Access Token有效时长，单位：秒。

        :param valid_period: The valid_period of this CheckTokenResponse.
        :type valid_period: int
        """
        self._valid_period = valid_period

    @property
    def expire_time(self):
        """Gets the expire_time of this CheckTokenResponse.

        Access Token的失效时间戳，单位：秒。

        :return: The expire_time of this CheckTokenResponse.
        :rtype: int
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this CheckTokenResponse.

        Access Token的失效时间戳，单位：秒。

        :param expire_time: The expire_time of this CheckTokenResponse.
        :type expire_time: int
        """
        self._expire_time = expire_time

    @property
    def create_time(self):
        """Gets the create_time of this CheckTokenResponse.

        Access Token的创建时间戳，单位：毫秒。

        :return: The create_time of this CheckTokenResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this CheckTokenResponse.

        Access Token的创建时间戳，单位：毫秒。

        :param create_time: The create_time of this CheckTokenResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def user(self):
        """Gets the user of this CheckTokenResponse.

        :return: The user of this CheckTokenResponse.
        :rtype: :class:`huaweicloudsdkmeeting.v1.UserInfo`
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this CheckTokenResponse.

        :param user: The user of this CheckTokenResponse.
        :type user: :class:`huaweicloudsdkmeeting.v1.UserInfo`
        """
        self._user = user

    @property
    def client_type(self):
        """Gets the client_type of this CheckTokenResponse.

        登录帐号类型。 * 72：API调用类型 

        :return: The client_type of this CheckTokenResponse.
        :rtype: int
        """
        return self._client_type

    @client_type.setter
    def client_type(self, client_type):
        """Sets the client_type of this CheckTokenResponse.

        登录帐号类型。 * 72：API调用类型 

        :param client_type: The client_type of this CheckTokenResponse.
        :type client_type: int
        """
        self._client_type = client_type

    @property
    def force_login_ind(self):
        """Gets the force_login_ind of this CheckTokenResponse.

        抢占登录标识。 * 0： 非抢占 * 1： 抢占 

        :return: The force_login_ind of this CheckTokenResponse.
        :rtype: int
        """
        return self._force_login_ind

    @force_login_ind.setter
    def force_login_ind(self, force_login_ind):
        """Sets the force_login_ind of this CheckTokenResponse.

        抢占登录标识。 * 0： 非抢占 * 1： 抢占 

        :param force_login_ind: The force_login_ind of this CheckTokenResponse.
        :type force_login_ind: int
        """
        self._force_login_ind = force_login_ind

    @property
    def first_login(self):
        """Gets the first_login of this CheckTokenResponse.

        是否首次登录。 > 首次登录表示尚未修改过密码。首次登录时，系统会提醒用户需要修改密码。 默认值：false。 

        :return: The first_login of this CheckTokenResponse.
        :rtype: bool
        """
        return self._first_login

    @first_login.setter
    def first_login(self, first_login):
        """Sets the first_login of this CheckTokenResponse.

        是否首次登录。 > 首次登录表示尚未修改过密码。首次登录时，系统会提醒用户需要修改密码。 默认值：false。 

        :param first_login: The first_login of this CheckTokenResponse.
        :type first_login: bool
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
        :type pwd_expired: bool
        """
        self._pwd_expired = pwd_expired

    @property
    def days_pwd_available(self):
        """Gets the days_pwd_available of this CheckTokenResponse.

        密码有效天数。

        :return: The days_pwd_available of this CheckTokenResponse.
        :rtype: int
        """
        return self._days_pwd_available

    @days_pwd_available.setter
    def days_pwd_available(self, days_pwd_available):
        """Sets the days_pwd_available of this CheckTokenResponse.

        密码有效天数。

        :param days_pwd_available: The days_pwd_available of this CheckTokenResponse.
        :type days_pwd_available: int
        """
        self._days_pwd_available = days_pwd_available

    @property
    def proxy_token(self):
        """Gets the proxy_token of this CheckTokenResponse.

        :return: The proxy_token of this CheckTokenResponse.
        :rtype: :class:`huaweicloudsdkmeeting.v1.ProxyTokenDTO`
        """
        return self._proxy_token

    @proxy_token.setter
    def proxy_token(self, proxy_token):
        """Sets the proxy_token of this CheckTokenResponse.

        :param proxy_token: The proxy_token of this CheckTokenResponse.
        :type proxy_token: :class:`huaweicloudsdkmeeting.v1.ProxyTokenDTO`
        """
        self._proxy_token = proxy_token

    @property
    def delay_delete(self):
        """Gets the delay_delete of this CheckTokenResponse.

        是否延时删除状态。

        :return: The delay_delete of this CheckTokenResponse.
        :rtype: bool
        """
        return self._delay_delete

    @delay_delete.setter
    def delay_delete(self, delay_delete):
        """Sets the delay_delete of this CheckTokenResponse.

        是否延时删除状态。

        :param delay_delete: The delay_delete of this CheckTokenResponse.
        :type delay_delete: bool
        """
        self._delay_delete = delay_delete

    @property
    def token_type(self):
        """Gets the token_type of this CheckTokenResponse.

        Token类型。 * 0：用户Access Token * 1：会控TOKEN * 2：一次性TOKEN 

        :return: The token_type of this CheckTokenResponse.
        :rtype: int
        """
        return self._token_type

    @token_type.setter
    def token_type(self, token_type):
        """Sets the token_type of this CheckTokenResponse.

        Token类型。 * 0：用户Access Token * 1：会控TOKEN * 2：一次性TOKEN 

        :param token_type: The token_type of this CheckTokenResponse.
        :type token_type: int
        """
        self._token_type = token_type

    @property
    def refresh_token(self):
        """Gets the refresh_token of this CheckTokenResponse.

        Refresh Token字符串。

        :return: The refresh_token of this CheckTokenResponse.
        :rtype: str
        """
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token):
        """Sets the refresh_token of this CheckTokenResponse.

        Refresh Token字符串。

        :param refresh_token: The refresh_token of this CheckTokenResponse.
        :type refresh_token: str
        """
        self._refresh_token = refresh_token

    @property
    def refresh_valid_period(self):
        """Gets the refresh_valid_period of this CheckTokenResponse.

        Refresh Token有效时长，单位：秒。

        :return: The refresh_valid_period of this CheckTokenResponse.
        :rtype: int
        """
        return self._refresh_valid_period

    @refresh_valid_period.setter
    def refresh_valid_period(self, refresh_valid_period):
        """Sets the refresh_valid_period of this CheckTokenResponse.

        Refresh Token有效时长，单位：秒。

        :param refresh_valid_period: The refresh_valid_period of this CheckTokenResponse.
        :type refresh_valid_period: int
        """
        self._refresh_valid_period = refresh_valid_period

    @property
    def refresh_expire_time(self):
        """Gets the refresh_expire_time of this CheckTokenResponse.

        Refresh Token的失效时间戳，单位：秒。

        :return: The refresh_expire_time of this CheckTokenResponse.
        :rtype: int
        """
        return self._refresh_expire_time

    @refresh_expire_time.setter
    def refresh_expire_time(self, refresh_expire_time):
        """Sets the refresh_expire_time of this CheckTokenResponse.

        Refresh Token的失效时间戳，单位：秒。

        :param refresh_expire_time: The refresh_expire_time of this CheckTokenResponse.
        :type refresh_expire_time: int
        """
        self._refresh_expire_time = refresh_expire_time

    @property
    def refresh_create_time(self):
        """Gets the refresh_create_time of this CheckTokenResponse.

        Refresh Token的创建时间戳，单位：毫秒。

        :return: The refresh_create_time of this CheckTokenResponse.
        :rtype: int
        """
        return self._refresh_create_time

    @refresh_create_time.setter
    def refresh_create_time(self, refresh_create_time):
        """Sets the refresh_create_time of this CheckTokenResponse.

        Refresh Token的创建时间戳，单位：毫秒。

        :param refresh_create_time: The refresh_create_time of this CheckTokenResponse.
        :type refresh_create_time: int
        """
        self._refresh_create_time = refresh_create_time

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
        if not isinstance(other, CheckTokenResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
