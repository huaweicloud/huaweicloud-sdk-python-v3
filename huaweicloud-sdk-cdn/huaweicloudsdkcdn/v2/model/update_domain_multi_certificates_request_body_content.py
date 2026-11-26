# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDomainMultiCertificatesRequestBodyContent:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_name': 'str',
        'https_switch': 'int',
        'access_origin_way': 'int',
        'force_redirect_https': 'int',
        'force_redirect_config': 'ForceRedirect',
        'http2': 'int',
        'cert_name': 'str',
        'certificate': 'str',
        'private_key': 'str',
        'certificate_type': 'int',
        'scm_certificate_id': 'str',
        'certificates': 'list[MultiCertificateBatchVo]'
    }

    attribute_map = {
        'domain_name': 'domain_name',
        'https_switch': 'https_switch',
        'access_origin_way': 'access_origin_way',
        'force_redirect_https': 'force_redirect_https',
        'force_redirect_config': 'force_redirect_config',
        'http2': 'http2',
        'cert_name': 'cert_name',
        'certificate': 'certificate',
        'private_key': 'private_key',
        'certificate_type': 'certificate_type',
        'scm_certificate_id': 'scm_certificate_id',
        'certificates': 'certificates'
    }

    def __init__(self, domain_name=None, https_switch=None, access_origin_way=None, force_redirect_https=None, force_redirect_config=None, http2=None, cert_name=None, certificate=None, private_key=None, certificate_type=None, scm_certificate_id=None, certificates=None):
        r"""UpdateDomainMultiCertificatesRequestBodyContent

        The model defined in huaweicloud sdk

        :param domain_name: **参数解释：** 需要配置HTTPS证书的域名 **约束限制：** - 域名间以“,”分隔 - 最多配置50个域名  **取值范围：** 不涉及 **默认取值：** 不涉及
        :type domain_name: str
        :param https_switch: **参数解释：** 证书配置开关 **约束限制：** https_switch为1时，证书参数不能为空 **取值范围：** - 0: 关闭 - 1: 开启  **默认取值：** 不涉及
        :type https_switch: int
        :param access_origin_way: **参数解释：** 回源协议 **约束限制：** 不涉及 **取值范围：** - 1: 协议跟随 - 2: http协议 - 3: https协议  **默认取值：** 2: http协议
        :type access_origin_way: int
        :param force_redirect_https: **参数解释：** 是否开启HTTPS强制跳转，强制客户端使用HTTPS协议访问CDN节点 &gt; 此参数即将下线，建议使用force_redirect_config修改配置  **约束限制：** 不涉及 **取值范围：** - 0: 关闭 - 1: 开启  **默认取值：** 0: 关闭
        :type force_redirect_https: int
        :param force_redirect_config: 
        :type force_redirect_config: :class:`huaweicloudsdkcdn.v2.ForceRedirect`
        :param http2: **参数解释：** HTTP/2开关，支持客户端采用HTTP/2协议访问CDN节点 **约束限制：** 不涉及 **取值范围：** - 0: 关闭 - 1: 开启  **默认取值：** 0: 关闭
        :type http2: int
        :param cert_name: **参数解释：** 证书名称 **约束限制：** https_switch为1时，该参数必填 **取值范围：** 3-64个字符，由英文字母、数字及“-”、“_”、空格组成 **默认取值：** 不涉及
        :type cert_name: str
        :param certificate: **参数解释：** SSL证书内容 **约束限制：** - 仅支持PEM编码格式 - 不启用证书则无需输入 - 初次配置证书时必传 - 需要传入完整证书链  **取值范围：** 证书链长度不超过20KB **默认取值：** 不涉及
        :type certificate: str
        :param private_key: **参数解释：** SSL证书私钥内容 **约束限制：** - 仅支持PEM编码格式 - 不启用证书则无需输入 - 初次配置证书时必传  **取值范围：** 不涉及 **默认取值：** 不涉及
        :type private_key: str
        :param certificate_type: **参数解释：** 证书类型 **约束限制：** 不涉及 **取值范围：** - 0: 自有证书 - 2: SCM证书  **默认取值：** 0: 自有证书
        :type certificate_type: int
        :param scm_certificate_id: **参数解释：** SCM证书ID，可使用云证书与管理服务（CCM）的查询证书列表接口获取 **约束限制：** 配置SCM证书时必传 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type scm_certificate_id: str
        :param certificates: **参数解释：** 配置国际证书和国密证书双证书场景下的证书列表 **约束限制：** - 配置双证书时最多传2个证书，只能包含1个国际证书和1个国密证书 - 使用双证书配置时，cert_name/certificate/private_key等单证书参数不可再使用  **取值范围：** 不涉及
        :type certificates: list[:class:`huaweicloudsdkcdn.v2.MultiCertificateBatchVo`]
        """
        
        

        self._domain_name = None
        self._https_switch = None
        self._access_origin_way = None
        self._force_redirect_https = None
        self._force_redirect_config = None
        self._http2 = None
        self._cert_name = None
        self._certificate = None
        self._private_key = None
        self._certificate_type = None
        self._scm_certificate_id = None
        self._certificates = None
        self.discriminator = None

        self.domain_name = domain_name
        self.https_switch = https_switch
        if access_origin_way is not None:
            self.access_origin_way = access_origin_way
        if force_redirect_https is not None:
            self.force_redirect_https = force_redirect_https
        if force_redirect_config is not None:
            self.force_redirect_config = force_redirect_config
        if http2 is not None:
            self.http2 = http2
        if cert_name is not None:
            self.cert_name = cert_name
        if certificate is not None:
            self.certificate = certificate
        if private_key is not None:
            self.private_key = private_key
        if certificate_type is not None:
            self.certificate_type = certificate_type
        if scm_certificate_id is not None:
            self.scm_certificate_id = scm_certificate_id
        if certificates is not None:
            self.certificates = certificates

    @property
    def domain_name(self):
        r"""Gets the domain_name of this UpdateDomainMultiCertificatesRequestBodyContent.

        **参数解释：** 需要配置HTTPS证书的域名 **约束限制：** - 域名间以“,”分隔 - 最多配置50个域名  **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The domain_name of this UpdateDomainMultiCertificatesRequestBodyContent.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this UpdateDomainMultiCertificatesRequestBodyContent.

        **参数解释：** 需要配置HTTPS证书的域名 **约束限制：** - 域名间以“,”分隔 - 最多配置50个域名  **取值范围：** 不涉及 **默认取值：** 不涉及

        :param domain_name: The domain_name of this UpdateDomainMultiCertificatesRequestBodyContent.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def https_switch(self):
        r"""Gets the https_switch of this UpdateDomainMultiCertificatesRequestBodyContent.

        **参数解释：** 证书配置开关 **约束限制：** https_switch为1时，证书参数不能为空 **取值范围：** - 0: 关闭 - 1: 开启  **默认取值：** 不涉及

        :return: The https_switch of this UpdateDomainMultiCertificatesRequestBodyContent.
        :rtype: int
        """
        return self._https_switch

    @https_switch.setter
    def https_switch(self, https_switch):
        r"""Sets the https_switch of this UpdateDomainMultiCertificatesRequestBodyContent.

        **参数解释：** 证书配置开关 **约束限制：** https_switch为1时，证书参数不能为空 **取值范围：** - 0: 关闭 - 1: 开启  **默认取值：** 不涉及

        :param https_switch: The https_switch of this UpdateDomainMultiCertificatesRequestBodyContent.
        :type https_switch: int
        """
        self._https_switch = https_switch

    @property
    def access_origin_way(self):
        r"""Gets the access_origin_way of this UpdateDomainMultiCertificatesRequestBodyContent.

        **参数解释：** 回源协议 **约束限制：** 不涉及 **取值范围：** - 1: 协议跟随 - 2: http协议 - 3: https协议  **默认取值：** 2: http协议

        :return: The access_origin_way of this UpdateDomainMultiCertificatesRequestBodyContent.
        :rtype: int
        """
        return self._access_origin_way

    @access_origin_way.setter
    def access_origin_way(self, access_origin_way):
        r"""Sets the access_origin_way of this UpdateDomainMultiCertificatesRequestBodyContent.

        **参数解释：** 回源协议 **约束限制：** 不涉及 **取值范围：** - 1: 协议跟随 - 2: http协议 - 3: https协议  **默认取值：** 2: http协议

        :param access_origin_way: The access_origin_way of this UpdateDomainMultiCertificatesRequestBodyContent.
        :type access_origin_way: int
        """
        self._access_origin_way = access_origin_way

    @property
    def force_redirect_https(self):
        r"""Gets the force_redirect_https of this UpdateDomainMultiCertificatesRequestBodyContent.

        **参数解释：** 是否开启HTTPS强制跳转，强制客户端使用HTTPS协议访问CDN节点 > 此参数即将下线，建议使用force_redirect_config修改配置  **约束限制：** 不涉及 **取值范围：** - 0: 关闭 - 1: 开启  **默认取值：** 0: 关闭

        :return: The force_redirect_https of this UpdateDomainMultiCertificatesRequestBodyContent.
        :rtype: int
        """
        return self._force_redirect_https

    @force_redirect_https.setter
    def force_redirect_https(self, force_redirect_https):
        r"""Sets the force_redirect_https of this UpdateDomainMultiCertificatesRequestBodyContent.

        **参数解释：** 是否开启HTTPS强制跳转，强制客户端使用HTTPS协议访问CDN节点 > 此参数即将下线，建议使用force_redirect_config修改配置  **约束限制：** 不涉及 **取值范围：** - 0: 关闭 - 1: 开启  **默认取值：** 0: 关闭

        :param force_redirect_https: The force_redirect_https of this UpdateDomainMultiCertificatesRequestBodyContent.
        :type force_redirect_https: int
        """
        self._force_redirect_https = force_redirect_https

    @property
    def force_redirect_config(self):
        r"""Gets the force_redirect_config of this UpdateDomainMultiCertificatesRequestBodyContent.

        :return: The force_redirect_config of this UpdateDomainMultiCertificatesRequestBodyContent.
        :rtype: :class:`huaweicloudsdkcdn.v2.ForceRedirect`
        """
        return self._force_redirect_config

    @force_redirect_config.setter
    def force_redirect_config(self, force_redirect_config):
        r"""Sets the force_redirect_config of this UpdateDomainMultiCertificatesRequestBodyContent.

        :param force_redirect_config: The force_redirect_config of this UpdateDomainMultiCertificatesRequestBodyContent.
        :type force_redirect_config: :class:`huaweicloudsdkcdn.v2.ForceRedirect`
        """
        self._force_redirect_config = force_redirect_config

    @property
    def http2(self):
        r"""Gets the http2 of this UpdateDomainMultiCertificatesRequestBodyContent.

        **参数解释：** HTTP/2开关，支持客户端采用HTTP/2协议访问CDN节点 **约束限制：** 不涉及 **取值范围：** - 0: 关闭 - 1: 开启  **默认取值：** 0: 关闭

        :return: The http2 of this UpdateDomainMultiCertificatesRequestBodyContent.
        :rtype: int
        """
        return self._http2

    @http2.setter
    def http2(self, http2):
        r"""Sets the http2 of this UpdateDomainMultiCertificatesRequestBodyContent.

        **参数解释：** HTTP/2开关，支持客户端采用HTTP/2协议访问CDN节点 **约束限制：** 不涉及 **取值范围：** - 0: 关闭 - 1: 开启  **默认取值：** 0: 关闭

        :param http2: The http2 of this UpdateDomainMultiCertificatesRequestBodyContent.
        :type http2: int
        """
        self._http2 = http2

    @property
    def cert_name(self):
        r"""Gets the cert_name of this UpdateDomainMultiCertificatesRequestBodyContent.

        **参数解释：** 证书名称 **约束限制：** https_switch为1时，该参数必填 **取值范围：** 3-64个字符，由英文字母、数字及“-”、“_”、空格组成 **默认取值：** 不涉及

        :return: The cert_name of this UpdateDomainMultiCertificatesRequestBodyContent.
        :rtype: str
        """
        return self._cert_name

    @cert_name.setter
    def cert_name(self, cert_name):
        r"""Sets the cert_name of this UpdateDomainMultiCertificatesRequestBodyContent.

        **参数解释：** 证书名称 **约束限制：** https_switch为1时，该参数必填 **取值范围：** 3-64个字符，由英文字母、数字及“-”、“_”、空格组成 **默认取值：** 不涉及

        :param cert_name: The cert_name of this UpdateDomainMultiCertificatesRequestBodyContent.
        :type cert_name: str
        """
        self._cert_name = cert_name

    @property
    def certificate(self):
        r"""Gets the certificate of this UpdateDomainMultiCertificatesRequestBodyContent.

        **参数解释：** SSL证书内容 **约束限制：** - 仅支持PEM编码格式 - 不启用证书则无需输入 - 初次配置证书时必传 - 需要传入完整证书链  **取值范围：** 证书链长度不超过20KB **默认取值：** 不涉及

        :return: The certificate of this UpdateDomainMultiCertificatesRequestBodyContent.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        r"""Sets the certificate of this UpdateDomainMultiCertificatesRequestBodyContent.

        **参数解释：** SSL证书内容 **约束限制：** - 仅支持PEM编码格式 - 不启用证书则无需输入 - 初次配置证书时必传 - 需要传入完整证书链  **取值范围：** 证书链长度不超过20KB **默认取值：** 不涉及

        :param certificate: The certificate of this UpdateDomainMultiCertificatesRequestBodyContent.
        :type certificate: str
        """
        self._certificate = certificate

    @property
    def private_key(self):
        r"""Gets the private_key of this UpdateDomainMultiCertificatesRequestBodyContent.

        **参数解释：** SSL证书私钥内容 **约束限制：** - 仅支持PEM编码格式 - 不启用证书则无需输入 - 初次配置证书时必传  **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The private_key of this UpdateDomainMultiCertificatesRequestBodyContent.
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        r"""Sets the private_key of this UpdateDomainMultiCertificatesRequestBodyContent.

        **参数解释：** SSL证书私钥内容 **约束限制：** - 仅支持PEM编码格式 - 不启用证书则无需输入 - 初次配置证书时必传  **取值范围：** 不涉及 **默认取值：** 不涉及

        :param private_key: The private_key of this UpdateDomainMultiCertificatesRequestBodyContent.
        :type private_key: str
        """
        self._private_key = private_key

    @property
    def certificate_type(self):
        r"""Gets the certificate_type of this UpdateDomainMultiCertificatesRequestBodyContent.

        **参数解释：** 证书类型 **约束限制：** 不涉及 **取值范围：** - 0: 自有证书 - 2: SCM证书  **默认取值：** 0: 自有证书

        :return: The certificate_type of this UpdateDomainMultiCertificatesRequestBodyContent.
        :rtype: int
        """
        return self._certificate_type

    @certificate_type.setter
    def certificate_type(self, certificate_type):
        r"""Sets the certificate_type of this UpdateDomainMultiCertificatesRequestBodyContent.

        **参数解释：** 证书类型 **约束限制：** 不涉及 **取值范围：** - 0: 自有证书 - 2: SCM证书  **默认取值：** 0: 自有证书

        :param certificate_type: The certificate_type of this UpdateDomainMultiCertificatesRequestBodyContent.
        :type certificate_type: int
        """
        self._certificate_type = certificate_type

    @property
    def scm_certificate_id(self):
        r"""Gets the scm_certificate_id of this UpdateDomainMultiCertificatesRequestBodyContent.

        **参数解释：** SCM证书ID，可使用云证书与管理服务（CCM）的查询证书列表接口获取 **约束限制：** 配置SCM证书时必传 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The scm_certificate_id of this UpdateDomainMultiCertificatesRequestBodyContent.
        :rtype: str
        """
        return self._scm_certificate_id

    @scm_certificate_id.setter
    def scm_certificate_id(self, scm_certificate_id):
        r"""Sets the scm_certificate_id of this UpdateDomainMultiCertificatesRequestBodyContent.

        **参数解释：** SCM证书ID，可使用云证书与管理服务（CCM）的查询证书列表接口获取 **约束限制：** 配置SCM证书时必传 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param scm_certificate_id: The scm_certificate_id of this UpdateDomainMultiCertificatesRequestBodyContent.
        :type scm_certificate_id: str
        """
        self._scm_certificate_id = scm_certificate_id

    @property
    def certificates(self):
        r"""Gets the certificates of this UpdateDomainMultiCertificatesRequestBodyContent.

        **参数解释：** 配置国际证书和国密证书双证书场景下的证书列表 **约束限制：** - 配置双证书时最多传2个证书，只能包含1个国际证书和1个国密证书 - 使用双证书配置时，cert_name/certificate/private_key等单证书参数不可再使用  **取值范围：** 不涉及

        :return: The certificates of this UpdateDomainMultiCertificatesRequestBodyContent.
        :rtype: list[:class:`huaweicloudsdkcdn.v2.MultiCertificateBatchVo`]
        """
        return self._certificates

    @certificates.setter
    def certificates(self, certificates):
        r"""Sets the certificates of this UpdateDomainMultiCertificatesRequestBodyContent.

        **参数解释：** 配置国际证书和国密证书双证书场景下的证书列表 **约束限制：** - 配置双证书时最多传2个证书，只能包含1个国际证书和1个国密证书 - 使用双证书配置时，cert_name/certificate/private_key等单证书参数不可再使用  **取值范围：** 不涉及

        :param certificates: The certificates of this UpdateDomainMultiCertificatesRequestBodyContent.
        :type certificates: list[:class:`huaweicloudsdkcdn.v2.MultiCertificateBatchVo`]
        """
        self._certificates = certificates

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateDomainMultiCertificatesRequestBodyContent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
