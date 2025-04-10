# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssociateCertificateV2Response(SdkResponse):

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
        'ssl_name': 'str',
        'ssl_id': 'str',
        'ssl_infos': 'list[SslInfo]'
    }

    attribute_map = {
        'url_domain': 'url_domain',
        'id': 'id',
        'status': 'status',
        'min_ssl_version': 'min_ssl_version',
        'is_http_redirect_to_https': 'is_http_redirect_to_https',
        'verified_client_certificate_enabled': 'verified_client_certificate_enabled',
        'ssl_name': 'ssl_name',
        'ssl_id': 'ssl_id',
        'ssl_infos': 'ssl_infos'
    }

    def __init__(self, url_domain=None, id=None, status=None, min_ssl_version=None, is_http_redirect_to_https=None, verified_client_certificate_enabled=None, ssl_name=None, ssl_id=None, ssl_infos=None):
        r"""AssociateCertificateV2Response

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
        :param ssl_name: 证书的名称
        :type ssl_name: str
        :param ssl_id: 证书的编号
        :type ssl_id: str
        :param ssl_infos: SSL证书列表  [暂不支持](tag:hws;hws_hk;fcs;g42;Site)
        :type ssl_infos: list[:class:`huaweicloudsdkroma.v2.SslInfo`]
        """
        
        super(AssociateCertificateV2Response, self).__init__()

        self._url_domain = None
        self._id = None
        self._status = None
        self._min_ssl_version = None
        self._is_http_redirect_to_https = None
        self._verified_client_certificate_enabled = None
        self._ssl_name = None
        self._ssl_id = None
        self._ssl_infos = None
        self.discriminator = None

        self.url_domain = url_domain
        self.id = id
        self.status = status
        self.min_ssl_version = min_ssl_version
        if is_http_redirect_to_https is not None:
            self.is_http_redirect_to_https = is_http_redirect_to_https
        if verified_client_certificate_enabled is not None:
            self.verified_client_certificate_enabled = verified_client_certificate_enabled
        if ssl_name is not None:
            self.ssl_name = ssl_name
        if ssl_id is not None:
            self.ssl_id = ssl_id
        if ssl_infos is not None:
            self.ssl_infos = ssl_infos

    @property
    def url_domain(self):
        r"""Gets the url_domain of this AssociateCertificateV2Response.

        自定义域名

        :return: The url_domain of this AssociateCertificateV2Response.
        :rtype: str
        """
        return self._url_domain

    @url_domain.setter
    def url_domain(self, url_domain):
        r"""Sets the url_domain of this AssociateCertificateV2Response.

        自定义域名

        :param url_domain: The url_domain of this AssociateCertificateV2Response.
        :type url_domain: str
        """
        self._url_domain = url_domain

    @property
    def id(self):
        r"""Gets the id of this AssociateCertificateV2Response.

        自定义域名的编号

        :return: The id of this AssociateCertificateV2Response.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AssociateCertificateV2Response.

        自定义域名的编号

        :param id: The id of this AssociateCertificateV2Response.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        r"""Gets the status of this AssociateCertificateV2Response.

        CNAME解析状态 - 1: 未解析 - 2: 解析中 - 3: 解析成功 - 4: 解析失败

        :return: The status of this AssociateCertificateV2Response.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this AssociateCertificateV2Response.

        CNAME解析状态 - 1: 未解析 - 2: 解析中 - 3: 解析成功 - 4: 解析失败

        :param status: The status of this AssociateCertificateV2Response.
        :type status: int
        """
        self._status = status

    @property
    def min_ssl_version(self):
        r"""Gets the min_ssl_version of this AssociateCertificateV2Response.

        支持的最小SSL版本

        :return: The min_ssl_version of this AssociateCertificateV2Response.
        :rtype: str
        """
        return self._min_ssl_version

    @min_ssl_version.setter
    def min_ssl_version(self, min_ssl_version):
        r"""Sets the min_ssl_version of this AssociateCertificateV2Response.

        支持的最小SSL版本

        :param min_ssl_version: The min_ssl_version of this AssociateCertificateV2Response.
        :type min_ssl_version: str
        """
        self._min_ssl_version = min_ssl_version

    @property
    def is_http_redirect_to_https(self):
        r"""Gets the is_http_redirect_to_https of this AssociateCertificateV2Response.

        是否开启http到https的重定向，false为关闭，true为开启，默认为false

        :return: The is_http_redirect_to_https of this AssociateCertificateV2Response.
        :rtype: bool
        """
        return self._is_http_redirect_to_https

    @is_http_redirect_to_https.setter
    def is_http_redirect_to_https(self, is_http_redirect_to_https):
        r"""Sets the is_http_redirect_to_https of this AssociateCertificateV2Response.

        是否开启http到https的重定向，false为关闭，true为开启，默认为false

        :param is_http_redirect_to_https: The is_http_redirect_to_https of this AssociateCertificateV2Response.
        :type is_http_redirect_to_https: bool
        """
        self._is_http_redirect_to_https = is_http_redirect_to_https

    @property
    def verified_client_certificate_enabled(self):
        r"""Gets the verified_client_certificate_enabled of this AssociateCertificateV2Response.

        是否开启客户端证书校验。只有绑定证书时，该参数才生效。当绑定证书存在trusted_root_ca时，默认开启；当绑定证书不存在trusted_root_ca时，默认关闭。

        :return: The verified_client_certificate_enabled of this AssociateCertificateV2Response.
        :rtype: bool
        """
        return self._verified_client_certificate_enabled

    @verified_client_certificate_enabled.setter
    def verified_client_certificate_enabled(self, verified_client_certificate_enabled):
        r"""Sets the verified_client_certificate_enabled of this AssociateCertificateV2Response.

        是否开启客户端证书校验。只有绑定证书时，该参数才生效。当绑定证书存在trusted_root_ca时，默认开启；当绑定证书不存在trusted_root_ca时，默认关闭。

        :param verified_client_certificate_enabled: The verified_client_certificate_enabled of this AssociateCertificateV2Response.
        :type verified_client_certificate_enabled: bool
        """
        self._verified_client_certificate_enabled = verified_client_certificate_enabled

    @property
    def ssl_name(self):
        r"""Gets the ssl_name of this AssociateCertificateV2Response.

        证书的名称

        :return: The ssl_name of this AssociateCertificateV2Response.
        :rtype: str
        """
        return self._ssl_name

    @ssl_name.setter
    def ssl_name(self, ssl_name):
        r"""Sets the ssl_name of this AssociateCertificateV2Response.

        证书的名称

        :param ssl_name: The ssl_name of this AssociateCertificateV2Response.
        :type ssl_name: str
        """
        self._ssl_name = ssl_name

    @property
    def ssl_id(self):
        r"""Gets the ssl_id of this AssociateCertificateV2Response.

        证书的编号

        :return: The ssl_id of this AssociateCertificateV2Response.
        :rtype: str
        """
        return self._ssl_id

    @ssl_id.setter
    def ssl_id(self, ssl_id):
        r"""Sets the ssl_id of this AssociateCertificateV2Response.

        证书的编号

        :param ssl_id: The ssl_id of this AssociateCertificateV2Response.
        :type ssl_id: str
        """
        self._ssl_id = ssl_id

    @property
    def ssl_infos(self):
        r"""Gets the ssl_infos of this AssociateCertificateV2Response.

        SSL证书列表  [暂不支持](tag:hws;hws_hk;fcs;g42;Site)

        :return: The ssl_infos of this AssociateCertificateV2Response.
        :rtype: list[:class:`huaweicloudsdkroma.v2.SslInfo`]
        """
        return self._ssl_infos

    @ssl_infos.setter
    def ssl_infos(self, ssl_infos):
        r"""Sets the ssl_infos of this AssociateCertificateV2Response.

        SSL证书列表  [暂不支持](tag:hws;hws_hk;fcs;g42;Site)

        :param ssl_infos: The ssl_infos of this AssociateCertificateV2Response.
        :type ssl_infos: list[:class:`huaweicloudsdkroma.v2.SslInfo`]
        """
        self._ssl_infos = ssl_infos

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
        if not isinstance(other, AssociateCertificateV2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
