# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDomainSettingsResponseBody:

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
        'login_url': 'str',
        'login_username': 'str',
        'login_password': 'str',
        'login_cookies': 'str',
        'verify_url': 'str',
        'http_headers': 'dict(str, str)',
        'domain_name': 'str'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'login_url': 'login_url',
        'login_username': 'login_username',
        'login_password': 'login_password',
        'login_cookies': 'login_cookies',
        'verify_url': 'verify_url',
        'http_headers': 'http_headers',
        'domain_name': 'domain_name'
    }

    def __init__(self, domain_id=None, login_url=None, login_username=None, login_password=None, login_cookies=None, verify_url=None, http_headers=None, domain_name=None):
        r"""UpdateDomainSettingsResponseBody

        The model defined in huaweicloud sdk

        :param domain_id: 网站域名ID
        :type domain_id: str
        :param login_url: 网站需要登录时，设置登录页面
        :type login_url: str
        :param login_username: 网站需要登录时，设置登录用户名
        :type login_username: str
        :param login_password: 网站需要登录时，设置登录密码
        :type login_password: str
        :param login_cookies: 网站需要登录时，设置登录cookie
        :type login_cookies: str
        :param verify_url: 设置用于验证登录是否成功的网址
        :type verify_url: str
        :param http_headers: 设置自定义HTTP请求头
        :type http_headers: dict(str, str)
        :param domain_name: 网站域名
        :type domain_name: str
        """
        
        

        self._domain_id = None
        self._login_url = None
        self._login_username = None
        self._login_password = None
        self._login_cookies = None
        self._verify_url = None
        self._http_headers = None
        self._domain_name = None
        self.discriminator = None

        if domain_id is not None:
            self.domain_id = domain_id
        if login_url is not None:
            self.login_url = login_url
        if login_username is not None:
            self.login_username = login_username
        if login_password is not None:
            self.login_password = login_password
        if login_cookies is not None:
            self.login_cookies = login_cookies
        if verify_url is not None:
            self.verify_url = verify_url
        if http_headers is not None:
            self.http_headers = http_headers
        if domain_name is not None:
            self.domain_name = domain_name

    @property
    def domain_id(self):
        r"""Gets the domain_id of this UpdateDomainSettingsResponseBody.

        网站域名ID

        :return: The domain_id of this UpdateDomainSettingsResponseBody.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this UpdateDomainSettingsResponseBody.

        网站域名ID

        :param domain_id: The domain_id of this UpdateDomainSettingsResponseBody.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def login_url(self):
        r"""Gets the login_url of this UpdateDomainSettingsResponseBody.

        网站需要登录时，设置登录页面

        :return: The login_url of this UpdateDomainSettingsResponseBody.
        :rtype: str
        """
        return self._login_url

    @login_url.setter
    def login_url(self, login_url):
        r"""Sets the login_url of this UpdateDomainSettingsResponseBody.

        网站需要登录时，设置登录页面

        :param login_url: The login_url of this UpdateDomainSettingsResponseBody.
        :type login_url: str
        """
        self._login_url = login_url

    @property
    def login_username(self):
        r"""Gets the login_username of this UpdateDomainSettingsResponseBody.

        网站需要登录时，设置登录用户名

        :return: The login_username of this UpdateDomainSettingsResponseBody.
        :rtype: str
        """
        return self._login_username

    @login_username.setter
    def login_username(self, login_username):
        r"""Sets the login_username of this UpdateDomainSettingsResponseBody.

        网站需要登录时，设置登录用户名

        :param login_username: The login_username of this UpdateDomainSettingsResponseBody.
        :type login_username: str
        """
        self._login_username = login_username

    @property
    def login_password(self):
        r"""Gets the login_password of this UpdateDomainSettingsResponseBody.

        网站需要登录时，设置登录密码

        :return: The login_password of this UpdateDomainSettingsResponseBody.
        :rtype: str
        """
        return self._login_password

    @login_password.setter
    def login_password(self, login_password):
        r"""Sets the login_password of this UpdateDomainSettingsResponseBody.

        网站需要登录时，设置登录密码

        :param login_password: The login_password of this UpdateDomainSettingsResponseBody.
        :type login_password: str
        """
        self._login_password = login_password

    @property
    def login_cookies(self):
        r"""Gets the login_cookies of this UpdateDomainSettingsResponseBody.

        网站需要登录时，设置登录cookie

        :return: The login_cookies of this UpdateDomainSettingsResponseBody.
        :rtype: str
        """
        return self._login_cookies

    @login_cookies.setter
    def login_cookies(self, login_cookies):
        r"""Sets the login_cookies of this UpdateDomainSettingsResponseBody.

        网站需要登录时，设置登录cookie

        :param login_cookies: The login_cookies of this UpdateDomainSettingsResponseBody.
        :type login_cookies: str
        """
        self._login_cookies = login_cookies

    @property
    def verify_url(self):
        r"""Gets the verify_url of this UpdateDomainSettingsResponseBody.

        设置用于验证登录是否成功的网址

        :return: The verify_url of this UpdateDomainSettingsResponseBody.
        :rtype: str
        """
        return self._verify_url

    @verify_url.setter
    def verify_url(self, verify_url):
        r"""Sets the verify_url of this UpdateDomainSettingsResponseBody.

        设置用于验证登录是否成功的网址

        :param verify_url: The verify_url of this UpdateDomainSettingsResponseBody.
        :type verify_url: str
        """
        self._verify_url = verify_url

    @property
    def http_headers(self):
        r"""Gets the http_headers of this UpdateDomainSettingsResponseBody.

        设置自定义HTTP请求头

        :return: The http_headers of this UpdateDomainSettingsResponseBody.
        :rtype: dict(str, str)
        """
        return self._http_headers

    @http_headers.setter
    def http_headers(self, http_headers):
        r"""Sets the http_headers of this UpdateDomainSettingsResponseBody.

        设置自定义HTTP请求头

        :param http_headers: The http_headers of this UpdateDomainSettingsResponseBody.
        :type http_headers: dict(str, str)
        """
        self._http_headers = http_headers

    @property
    def domain_name(self):
        r"""Gets the domain_name of this UpdateDomainSettingsResponseBody.

        网站域名

        :return: The domain_name of this UpdateDomainSettingsResponseBody.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this UpdateDomainSettingsResponseBody.

        网站域名

        :param domain_name: The domain_name of this UpdateDomainSettingsResponseBody.
        :type domain_name: str
        """
        self._domain_name = domain_name

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
        if not isinstance(other, UpdateDomainSettingsResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
