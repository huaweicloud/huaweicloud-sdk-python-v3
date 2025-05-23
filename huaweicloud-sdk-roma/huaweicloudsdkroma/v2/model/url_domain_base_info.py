# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UrlDomainBaseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'url_domain': 'str',
        'id': 'str',
        'status': 'int',
        'min_ssl_version': 'str',
        'is_http_redirect_to_https': 'bool',
        'verified_client_certificate_enabled': 'bool'
    }

    attribute_map = {
        'url_domain': 'url_domain',
        'id': 'id',
        'status': 'status',
        'min_ssl_version': 'min_ssl_version',
        'is_http_redirect_to_https': 'is_http_redirect_to_https',
        'verified_client_certificate_enabled': 'verified_client_certificate_enabled'
    }

    def __init__(self, url_domain=None, id=None, status=None, min_ssl_version=None, is_http_redirect_to_https=None, verified_client_certificate_enabled=None):
        r"""UrlDomainBaseInfo

        The model defined in huaweicloud sdk

        :param url_domain: 自定义域名
        :type url_domain: str
        :param id: 自定义域名的编号
        :type id: str
        :param status: CNAME解析状态 - 1: 未解析 - 2: 解析中 - 3: 解析成功 - 4: 解析失败
        :type status: int
        :param min_ssl_version: 支持的最小SSL版本
        :type min_ssl_version: str
        :param is_http_redirect_to_https: 是否开启http到https的重定向，false为关闭，true为开启，默认为false
        :type is_http_redirect_to_https: bool
        :param verified_client_certificate_enabled: 是否开启客户端证书校验。只有绑定证书时，该参数才生效。当绑定证书存在trusted_root_ca时，默认开启；当绑定证书不存在trusted_root_ca时，默认关闭。
        :type verified_client_certificate_enabled: bool
        """
        
        

        self._url_domain = None
        self._id = None
        self._status = None
        self._min_ssl_version = None
        self._is_http_redirect_to_https = None
        self._verified_client_certificate_enabled = None
        self.discriminator = None

        self.url_domain = url_domain
        self.id = id
        self.status = status
        self.min_ssl_version = min_ssl_version
        if is_http_redirect_to_https is not None:
            self.is_http_redirect_to_https = is_http_redirect_to_https
        if verified_client_certificate_enabled is not None:
            self.verified_client_certificate_enabled = verified_client_certificate_enabled

    @property
    def url_domain(self):
        r"""Gets the url_domain of this UrlDomainBaseInfo.

        自定义域名

        :return: The url_domain of this UrlDomainBaseInfo.
        :rtype: str
        """
        return self._url_domain

    @url_domain.setter
    def url_domain(self, url_domain):
        r"""Sets the url_domain of this UrlDomainBaseInfo.

        自定义域名

        :param url_domain: The url_domain of this UrlDomainBaseInfo.
        :type url_domain: str
        """
        self._url_domain = url_domain

    @property
    def id(self):
        r"""Gets the id of this UrlDomainBaseInfo.

        自定义域名的编号

        :return: The id of this UrlDomainBaseInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UrlDomainBaseInfo.

        自定义域名的编号

        :param id: The id of this UrlDomainBaseInfo.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        r"""Gets the status of this UrlDomainBaseInfo.

        CNAME解析状态 - 1: 未解析 - 2: 解析中 - 3: 解析成功 - 4: 解析失败

        :return: The status of this UrlDomainBaseInfo.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UrlDomainBaseInfo.

        CNAME解析状态 - 1: 未解析 - 2: 解析中 - 3: 解析成功 - 4: 解析失败

        :param status: The status of this UrlDomainBaseInfo.
        :type status: int
        """
        self._status = status

    @property
    def min_ssl_version(self):
        r"""Gets the min_ssl_version of this UrlDomainBaseInfo.

        支持的最小SSL版本

        :return: The min_ssl_version of this UrlDomainBaseInfo.
        :rtype: str
        """
        return self._min_ssl_version

    @min_ssl_version.setter
    def min_ssl_version(self, min_ssl_version):
        r"""Sets the min_ssl_version of this UrlDomainBaseInfo.

        支持的最小SSL版本

        :param min_ssl_version: The min_ssl_version of this UrlDomainBaseInfo.
        :type min_ssl_version: str
        """
        self._min_ssl_version = min_ssl_version

    @property
    def is_http_redirect_to_https(self):
        r"""Gets the is_http_redirect_to_https of this UrlDomainBaseInfo.

        是否开启http到https的重定向，false为关闭，true为开启，默认为false

        :return: The is_http_redirect_to_https of this UrlDomainBaseInfo.
        :rtype: bool
        """
        return self._is_http_redirect_to_https

    @is_http_redirect_to_https.setter
    def is_http_redirect_to_https(self, is_http_redirect_to_https):
        r"""Sets the is_http_redirect_to_https of this UrlDomainBaseInfo.

        是否开启http到https的重定向，false为关闭，true为开启，默认为false

        :param is_http_redirect_to_https: The is_http_redirect_to_https of this UrlDomainBaseInfo.
        :type is_http_redirect_to_https: bool
        """
        self._is_http_redirect_to_https = is_http_redirect_to_https

    @property
    def verified_client_certificate_enabled(self):
        r"""Gets the verified_client_certificate_enabled of this UrlDomainBaseInfo.

        是否开启客户端证书校验。只有绑定证书时，该参数才生效。当绑定证书存在trusted_root_ca时，默认开启；当绑定证书不存在trusted_root_ca时，默认关闭。

        :return: The verified_client_certificate_enabled of this UrlDomainBaseInfo.
        :rtype: bool
        """
        return self._verified_client_certificate_enabled

    @verified_client_certificate_enabled.setter
    def verified_client_certificate_enabled(self, verified_client_certificate_enabled):
        r"""Sets the verified_client_certificate_enabled of this UrlDomainBaseInfo.

        是否开启客户端证书校验。只有绑定证书时，该参数才生效。当绑定证书存在trusted_root_ca时，默认开启；当绑定证书不存在trusted_root_ca时，默认关闭。

        :param verified_client_certificate_enabled: The verified_client_certificate_enabled of this UrlDomainBaseInfo.
        :type verified_client_certificate_enabled: bool
        """
        self._verified_client_certificate_enabled = verified_client_certificate_enabled

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
        if not isinstance(other, UrlDomainBaseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
