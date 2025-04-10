# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UrlDomain:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'domain': 'str',
        'cname_status': 'int',
        'ssl_id': 'str',
        'ssl_name': 'str',
        'min_ssl_version': 'str',
        'verified_client_certificate_enabled': 'bool',
        'is_has_trusted_root_ca': 'bool',
        'ingress_http_port': 'int',
        'ingress_https_port': 'int',
        'ssl_infos': 'list[SslInfo]'
    }

    attribute_map = {
        'id': 'id',
        'domain': 'domain',
        'cname_status': 'cname_status',
        'ssl_id': 'ssl_id',
        'ssl_name': 'ssl_name',
        'min_ssl_version': 'min_ssl_version',
        'verified_client_certificate_enabled': 'verified_client_certificate_enabled',
        'is_has_trusted_root_ca': 'is_has_trusted_root_ca',
        'ingress_http_port': 'ingress_http_port',
        'ingress_https_port': 'ingress_https_port',
        'ssl_infos': 'ssl_infos'
    }

    def __init__(self, id=None, domain=None, cname_status=None, ssl_id=None, ssl_name=None, min_ssl_version=None, verified_client_certificate_enabled=None, is_has_trusted_root_ca=None, ingress_http_port=None, ingress_https_port=None, ssl_infos=None):
        r"""UrlDomain

        The model defined in huaweicloud sdk

        :param id: 域名编号
        :type id: str
        :param domain: 访问域名
        :type domain: str
        :param cname_status: 域名cname状态： - 1：未解析 - 2：解析中 - 3：解析成功 - 4：解析失败
        :type cname_status: int
        :param ssl_id: SSL证书编号
        :type ssl_id: str
        :param ssl_name: SSL证书名称
        :type ssl_name: str
        :param min_ssl_version: 最小ssl协议版本号。支持TLSv1.1或TLSv1.2
        :type min_ssl_version: str
        :param verified_client_certificate_enabled: 是否开启客户端证书校验。只有绑定证书时，该参数才生效。当绑定证书存在trusted_root_ca时，默认开启；当绑定证书不存在trusted_root_ca时，默认关闭。
        :type verified_client_certificate_enabled: bool
        :param is_has_trusted_root_ca: 是否存在信任的根证书CA。当绑定证书存在trusted_root_ca时为true。
        :type is_has_trusted_root_ca: bool
        :param ingress_http_port: 访问该域名绑定的http协议入方向端口，-1表示无端口且协议不支持，可使用80默认端口，其他有效端口允许的取值范围为1024~49151，需为实例已开放的HTTP协议的自定义入方向端口。  当创建域名时，该参数未填表示用默认80端口；如果填写该参数，则必须同时填写https_port；如果要http_port和https_port同时使用默认端口，则两个参数都不填。  当修改域名时，该参数未填表示不修改该端口。 
        :type ingress_http_port: int
        :param ingress_https_port: 访问该域名绑定的https协议入方向端口，-1表示无端口且协议不支持，可使用443默认端口，其他有效端口允许的取值范围为1024~49151，需为实例已开放的HTTPS协议的自定义入方向端口。  当创建域名时，该参数未填表示用默认443端口；如果填写该参数，则必须同时填写http_port；如果要http_port和https_port同时使用默认端口，则两个参数都不填。  当修改域名时，该参数未填表示不修改该端口。 
        :type ingress_https_port: int
        :param ssl_infos: SSL证书列表。
        :type ssl_infos: list[:class:`huaweicloudsdkapig.v2.SslInfo`]
        """
        
        

        self._id = None
        self._domain = None
        self._cname_status = None
        self._ssl_id = None
        self._ssl_name = None
        self._min_ssl_version = None
        self._verified_client_certificate_enabled = None
        self._is_has_trusted_root_ca = None
        self._ingress_http_port = None
        self._ingress_https_port = None
        self._ssl_infos = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if domain is not None:
            self.domain = domain
        if cname_status is not None:
            self.cname_status = cname_status
        if ssl_id is not None:
            self.ssl_id = ssl_id
        if ssl_name is not None:
            self.ssl_name = ssl_name
        if min_ssl_version is not None:
            self.min_ssl_version = min_ssl_version
        if verified_client_certificate_enabled is not None:
            self.verified_client_certificate_enabled = verified_client_certificate_enabled
        if is_has_trusted_root_ca is not None:
            self.is_has_trusted_root_ca = is_has_trusted_root_ca
        if ingress_http_port is not None:
            self.ingress_http_port = ingress_http_port
        if ingress_https_port is not None:
            self.ingress_https_port = ingress_https_port
        if ssl_infos is not None:
            self.ssl_infos = ssl_infos

    @property
    def id(self):
        r"""Gets the id of this UrlDomain.

        域名编号

        :return: The id of this UrlDomain.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UrlDomain.

        域名编号

        :param id: The id of this UrlDomain.
        :type id: str
        """
        self._id = id

    @property
    def domain(self):
        r"""Gets the domain of this UrlDomain.

        访问域名

        :return: The domain of this UrlDomain.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this UrlDomain.

        访问域名

        :param domain: The domain of this UrlDomain.
        :type domain: str
        """
        self._domain = domain

    @property
    def cname_status(self):
        r"""Gets the cname_status of this UrlDomain.

        域名cname状态： - 1：未解析 - 2：解析中 - 3：解析成功 - 4：解析失败

        :return: The cname_status of this UrlDomain.
        :rtype: int
        """
        return self._cname_status

    @cname_status.setter
    def cname_status(self, cname_status):
        r"""Sets the cname_status of this UrlDomain.

        域名cname状态： - 1：未解析 - 2：解析中 - 3：解析成功 - 4：解析失败

        :param cname_status: The cname_status of this UrlDomain.
        :type cname_status: int
        """
        self._cname_status = cname_status

    @property
    def ssl_id(self):
        r"""Gets the ssl_id of this UrlDomain.

        SSL证书编号

        :return: The ssl_id of this UrlDomain.
        :rtype: str
        """
        return self._ssl_id

    @ssl_id.setter
    def ssl_id(self, ssl_id):
        r"""Sets the ssl_id of this UrlDomain.

        SSL证书编号

        :param ssl_id: The ssl_id of this UrlDomain.
        :type ssl_id: str
        """
        self._ssl_id = ssl_id

    @property
    def ssl_name(self):
        r"""Gets the ssl_name of this UrlDomain.

        SSL证书名称

        :return: The ssl_name of this UrlDomain.
        :rtype: str
        """
        return self._ssl_name

    @ssl_name.setter
    def ssl_name(self, ssl_name):
        r"""Sets the ssl_name of this UrlDomain.

        SSL证书名称

        :param ssl_name: The ssl_name of this UrlDomain.
        :type ssl_name: str
        """
        self._ssl_name = ssl_name

    @property
    def min_ssl_version(self):
        r"""Gets the min_ssl_version of this UrlDomain.

        最小ssl协议版本号。支持TLSv1.1或TLSv1.2

        :return: The min_ssl_version of this UrlDomain.
        :rtype: str
        """
        return self._min_ssl_version

    @min_ssl_version.setter
    def min_ssl_version(self, min_ssl_version):
        r"""Sets the min_ssl_version of this UrlDomain.

        最小ssl协议版本号。支持TLSv1.1或TLSv1.2

        :param min_ssl_version: The min_ssl_version of this UrlDomain.
        :type min_ssl_version: str
        """
        self._min_ssl_version = min_ssl_version

    @property
    def verified_client_certificate_enabled(self):
        r"""Gets the verified_client_certificate_enabled of this UrlDomain.

        是否开启客户端证书校验。只有绑定证书时，该参数才生效。当绑定证书存在trusted_root_ca时，默认开启；当绑定证书不存在trusted_root_ca时，默认关闭。

        :return: The verified_client_certificate_enabled of this UrlDomain.
        :rtype: bool
        """
        return self._verified_client_certificate_enabled

    @verified_client_certificate_enabled.setter
    def verified_client_certificate_enabled(self, verified_client_certificate_enabled):
        r"""Sets the verified_client_certificate_enabled of this UrlDomain.

        是否开启客户端证书校验。只有绑定证书时，该参数才生效。当绑定证书存在trusted_root_ca时，默认开启；当绑定证书不存在trusted_root_ca时，默认关闭。

        :param verified_client_certificate_enabled: The verified_client_certificate_enabled of this UrlDomain.
        :type verified_client_certificate_enabled: bool
        """
        self._verified_client_certificate_enabled = verified_client_certificate_enabled

    @property
    def is_has_trusted_root_ca(self):
        r"""Gets the is_has_trusted_root_ca of this UrlDomain.

        是否存在信任的根证书CA。当绑定证书存在trusted_root_ca时为true。

        :return: The is_has_trusted_root_ca of this UrlDomain.
        :rtype: bool
        """
        return self._is_has_trusted_root_ca

    @is_has_trusted_root_ca.setter
    def is_has_trusted_root_ca(self, is_has_trusted_root_ca):
        r"""Sets the is_has_trusted_root_ca of this UrlDomain.

        是否存在信任的根证书CA。当绑定证书存在trusted_root_ca时为true。

        :param is_has_trusted_root_ca: The is_has_trusted_root_ca of this UrlDomain.
        :type is_has_trusted_root_ca: bool
        """
        self._is_has_trusted_root_ca = is_has_trusted_root_ca

    @property
    def ingress_http_port(self):
        r"""Gets the ingress_http_port of this UrlDomain.

        访问该域名绑定的http协议入方向端口，-1表示无端口且协议不支持，可使用80默认端口，其他有效端口允许的取值范围为1024~49151，需为实例已开放的HTTP协议的自定义入方向端口。  当创建域名时，该参数未填表示用默认80端口；如果填写该参数，则必须同时填写https_port；如果要http_port和https_port同时使用默认端口，则两个参数都不填。  当修改域名时，该参数未填表示不修改该端口。 

        :return: The ingress_http_port of this UrlDomain.
        :rtype: int
        """
        return self._ingress_http_port

    @ingress_http_port.setter
    def ingress_http_port(self, ingress_http_port):
        r"""Sets the ingress_http_port of this UrlDomain.

        访问该域名绑定的http协议入方向端口，-1表示无端口且协议不支持，可使用80默认端口，其他有效端口允许的取值范围为1024~49151，需为实例已开放的HTTP协议的自定义入方向端口。  当创建域名时，该参数未填表示用默认80端口；如果填写该参数，则必须同时填写https_port；如果要http_port和https_port同时使用默认端口，则两个参数都不填。  当修改域名时，该参数未填表示不修改该端口。 

        :param ingress_http_port: The ingress_http_port of this UrlDomain.
        :type ingress_http_port: int
        """
        self._ingress_http_port = ingress_http_port

    @property
    def ingress_https_port(self):
        r"""Gets the ingress_https_port of this UrlDomain.

        访问该域名绑定的https协议入方向端口，-1表示无端口且协议不支持，可使用443默认端口，其他有效端口允许的取值范围为1024~49151，需为实例已开放的HTTPS协议的自定义入方向端口。  当创建域名时，该参数未填表示用默认443端口；如果填写该参数，则必须同时填写http_port；如果要http_port和https_port同时使用默认端口，则两个参数都不填。  当修改域名时，该参数未填表示不修改该端口。 

        :return: The ingress_https_port of this UrlDomain.
        :rtype: int
        """
        return self._ingress_https_port

    @ingress_https_port.setter
    def ingress_https_port(self, ingress_https_port):
        r"""Sets the ingress_https_port of this UrlDomain.

        访问该域名绑定的https协议入方向端口，-1表示无端口且协议不支持，可使用443默认端口，其他有效端口允许的取值范围为1024~49151，需为实例已开放的HTTPS协议的自定义入方向端口。  当创建域名时，该参数未填表示用默认443端口；如果填写该参数，则必须同时填写http_port；如果要http_port和https_port同时使用默认端口，则两个参数都不填。  当修改域名时，该参数未填表示不修改该端口。 

        :param ingress_https_port: The ingress_https_port of this UrlDomain.
        :type ingress_https_port: int
        """
        self._ingress_https_port = ingress_https_port

    @property
    def ssl_infos(self):
        r"""Gets the ssl_infos of this UrlDomain.

        SSL证书列表。

        :return: The ssl_infos of this UrlDomain.
        :rtype: list[:class:`huaweicloudsdkapig.v2.SslInfo`]
        """
        return self._ssl_infos

    @ssl_infos.setter
    def ssl_infos(self, ssl_infos):
        r"""Sets the ssl_infos of this UrlDomain.

        SSL证书列表。

        :param ssl_infos: The ssl_infos of this UrlDomain.
        :type ssl_infos: list[:class:`huaweicloudsdkapig.v2.SslInfo`]
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
        if not isinstance(other, UrlDomain):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
