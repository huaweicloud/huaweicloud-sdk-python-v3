# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UrlDomainRefInfo:

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
        'verified_client_certificate_enabled': 'bool',
        'ssl_id': 'str',
        'ssl_name': 'str',
        'api_group_id': 'str',
        'api_group_name': 'str',
        'instance_id': 'str'
    }

    attribute_map = {
        'url_domain': 'url_domain',
        'id': 'id',
        'status': 'status',
        'min_ssl_version': 'min_ssl_version',
        'is_http_redirect_to_https': 'is_http_redirect_to_https',
        'verified_client_certificate_enabled': 'verified_client_certificate_enabled',
        'ssl_id': 'ssl_id',
        'ssl_name': 'ssl_name',
        'api_group_id': 'api_group_id',
        'api_group_name': 'api_group_name',
        'instance_id': 'instance_id'
    }

    def __init__(self, url_domain=None, id=None, status=None, min_ssl_version=None, is_http_redirect_to_https=None, verified_client_certificate_enabled=None, ssl_id=None, ssl_name=None, api_group_id=None, api_group_name=None, instance_id=None):
        """UrlDomainRefInfo

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
        :param ssl_id: 证书ID
        :type ssl_id: str
        :param ssl_name: 证书名称
        :type ssl_name: str
        :param api_group_id: 所属API分组ID
        :type api_group_id: str
        :param api_group_name: 所属API分组名称
        :type api_group_name: str
        :param instance_id: 所属实例ID
        :type instance_id: str
        """
        
        

        self._url_domain = None
        self._id = None
        self._status = None
        self._min_ssl_version = None
        self._is_http_redirect_to_https = None
        self._verified_client_certificate_enabled = None
        self._ssl_id = None
        self._ssl_name = None
        self._api_group_id = None
        self._api_group_name = None
        self._instance_id = None
        self.discriminator = None

        self.url_domain = url_domain
        self.id = id
        self.status = status
        self.min_ssl_version = min_ssl_version
        if is_http_redirect_to_https is not None:
            self.is_http_redirect_to_https = is_http_redirect_to_https
        if verified_client_certificate_enabled is not None:
            self.verified_client_certificate_enabled = verified_client_certificate_enabled
        if ssl_id is not None:
            self.ssl_id = ssl_id
        if ssl_name is not None:
            self.ssl_name = ssl_name
        self.api_group_id = api_group_id
        self.api_group_name = api_group_name
        self.instance_id = instance_id

    @property
    def url_domain(self):
        """Gets the url_domain of this UrlDomainRefInfo.

        自定义域名

        :return: The url_domain of this UrlDomainRefInfo.
        :rtype: str
        """
        return self._url_domain

    @url_domain.setter
    def url_domain(self, url_domain):
        """Sets the url_domain of this UrlDomainRefInfo.

        自定义域名

        :param url_domain: The url_domain of this UrlDomainRefInfo.
        :type url_domain: str
        """
        self._url_domain = url_domain

    @property
    def id(self):
        """Gets the id of this UrlDomainRefInfo.

        自定义域名的编号

        :return: The id of this UrlDomainRefInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UrlDomainRefInfo.

        自定义域名的编号

        :param id: The id of this UrlDomainRefInfo.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        """Gets the status of this UrlDomainRefInfo.

        CNAME解析状态 - 1: 未解析 - 2: 解析中 - 3: 解析成功 - 4: 解析失败

        :return: The status of this UrlDomainRefInfo.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UrlDomainRefInfo.

        CNAME解析状态 - 1: 未解析 - 2: 解析中 - 3: 解析成功 - 4: 解析失败

        :param status: The status of this UrlDomainRefInfo.
        :type status: int
        """
        self._status = status

    @property
    def min_ssl_version(self):
        """Gets the min_ssl_version of this UrlDomainRefInfo.

        支持的最小SSL版本

        :return: The min_ssl_version of this UrlDomainRefInfo.
        :rtype: str
        """
        return self._min_ssl_version

    @min_ssl_version.setter
    def min_ssl_version(self, min_ssl_version):
        """Sets the min_ssl_version of this UrlDomainRefInfo.

        支持的最小SSL版本

        :param min_ssl_version: The min_ssl_version of this UrlDomainRefInfo.
        :type min_ssl_version: str
        """
        self._min_ssl_version = min_ssl_version

    @property
    def is_http_redirect_to_https(self):
        """Gets the is_http_redirect_to_https of this UrlDomainRefInfo.

        是否开启http到https的重定向，false为关闭，true为开启，默认为false

        :return: The is_http_redirect_to_https of this UrlDomainRefInfo.
        :rtype: bool
        """
        return self._is_http_redirect_to_https

    @is_http_redirect_to_https.setter
    def is_http_redirect_to_https(self, is_http_redirect_to_https):
        """Sets the is_http_redirect_to_https of this UrlDomainRefInfo.

        是否开启http到https的重定向，false为关闭，true为开启，默认为false

        :param is_http_redirect_to_https: The is_http_redirect_to_https of this UrlDomainRefInfo.
        :type is_http_redirect_to_https: bool
        """
        self._is_http_redirect_to_https = is_http_redirect_to_https

    @property
    def verified_client_certificate_enabled(self):
        """Gets the verified_client_certificate_enabled of this UrlDomainRefInfo.

        是否开启客户端证书校验。只有绑定证书时，该参数才生效。当绑定证书存在trusted_root_ca时，默认开启；当绑定证书不存在trusted_root_ca时，默认关闭。

        :return: The verified_client_certificate_enabled of this UrlDomainRefInfo.
        :rtype: bool
        """
        return self._verified_client_certificate_enabled

    @verified_client_certificate_enabled.setter
    def verified_client_certificate_enabled(self, verified_client_certificate_enabled):
        """Sets the verified_client_certificate_enabled of this UrlDomainRefInfo.

        是否开启客户端证书校验。只有绑定证书时，该参数才生效。当绑定证书存在trusted_root_ca时，默认开启；当绑定证书不存在trusted_root_ca时，默认关闭。

        :param verified_client_certificate_enabled: The verified_client_certificate_enabled of this UrlDomainRefInfo.
        :type verified_client_certificate_enabled: bool
        """
        self._verified_client_certificate_enabled = verified_client_certificate_enabled

    @property
    def ssl_id(self):
        """Gets the ssl_id of this UrlDomainRefInfo.

        证书ID

        :return: The ssl_id of this UrlDomainRefInfo.
        :rtype: str
        """
        return self._ssl_id

    @ssl_id.setter
    def ssl_id(self, ssl_id):
        """Sets the ssl_id of this UrlDomainRefInfo.

        证书ID

        :param ssl_id: The ssl_id of this UrlDomainRefInfo.
        :type ssl_id: str
        """
        self._ssl_id = ssl_id

    @property
    def ssl_name(self):
        """Gets the ssl_name of this UrlDomainRefInfo.

        证书名称

        :return: The ssl_name of this UrlDomainRefInfo.
        :rtype: str
        """
        return self._ssl_name

    @ssl_name.setter
    def ssl_name(self, ssl_name):
        """Sets the ssl_name of this UrlDomainRefInfo.

        证书名称

        :param ssl_name: The ssl_name of this UrlDomainRefInfo.
        :type ssl_name: str
        """
        self._ssl_name = ssl_name

    @property
    def api_group_id(self):
        """Gets the api_group_id of this UrlDomainRefInfo.

        所属API分组ID

        :return: The api_group_id of this UrlDomainRefInfo.
        :rtype: str
        """
        return self._api_group_id

    @api_group_id.setter
    def api_group_id(self, api_group_id):
        """Sets the api_group_id of this UrlDomainRefInfo.

        所属API分组ID

        :param api_group_id: The api_group_id of this UrlDomainRefInfo.
        :type api_group_id: str
        """
        self._api_group_id = api_group_id

    @property
    def api_group_name(self):
        """Gets the api_group_name of this UrlDomainRefInfo.

        所属API分组名称

        :return: The api_group_name of this UrlDomainRefInfo.
        :rtype: str
        """
        return self._api_group_name

    @api_group_name.setter
    def api_group_name(self, api_group_name):
        """Sets the api_group_name of this UrlDomainRefInfo.

        所属API分组名称

        :param api_group_name: The api_group_name of this UrlDomainRefInfo.
        :type api_group_name: str
        """
        self._api_group_name = api_group_name

    @property
    def instance_id(self):
        """Gets the instance_id of this UrlDomainRefInfo.

        所属实例ID

        :return: The instance_id of this UrlDomainRefInfo.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this UrlDomainRefInfo.

        所属实例ID

        :param instance_id: The instance_id of this UrlDomainRefInfo.
        :type instance_id: str
        """
        self._instance_id = instance_id

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
        if not isinstance(other, UrlDomainRefInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
