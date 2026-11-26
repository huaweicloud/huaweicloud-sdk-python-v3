# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HttpTemplateBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'https_status': 'str',
        'certificate_type': 'str',
        'certificate_source': 'int',
        'scm_certificate_id': 'str',
        'certificate_name': 'str',
        'certificate_value': 'str',
        'private_key': 'str',
        'enc_certificate_value': 'str',
        'enc_private_key': 'str',
        'certificates': 'list[CertificatesPutBody]',
        'http2_status': 'str',
        'ocsp_stapling_status': 'str'
    }

    attribute_map = {
        'https_status': 'https_status',
        'certificate_type': 'certificate_type',
        'certificate_source': 'certificate_source',
        'scm_certificate_id': 'scm_certificate_id',
        'certificate_name': 'certificate_name',
        'certificate_value': 'certificate_value',
        'private_key': 'private_key',
        'enc_certificate_value': 'enc_certificate_value',
        'enc_private_key': 'enc_private_key',
        'certificates': 'certificates',
        'http2_status': 'http2_status',
        'ocsp_stapling_status': 'ocsp_stapling_status'
    }

    def __init__(self, https_status=None, certificate_type=None, certificate_source=None, scm_certificate_id=None, certificate_name=None, certificate_value=None, private_key=None, enc_certificate_value=None, enc_private_key=None, certificates=None, http2_status=None, ocsp_stapling_status=None):
        r"""HttpTemplateBody

        The model defined in huaweicloud sdk

        :param https_status: **参数解释：** 证书配置开关 **约束限制：** 不涉及 **取值范围：** - on: 开启 - off: 关闭 **默认取值：** 不涉及
        :type https_status: str
        :param certificate_type: **参数解释：** 证书类型 **约束限制：** 不涉及 **取值范围：** - server: 国际证书 - server_sm: 国密证书 **默认取值：** 不涉及
        :type certificate_type: str
        :param certificate_source: **参数解释：** 证书来源 **约束限制：** 证书开启时必传 **取值范围：** - 0: 自有证书 - 2: SCM证书 **默认取值：** 不涉及
        :type certificate_source: int
        :param scm_certificate_id: **参数解释：** SCM证书ID，可使用云证书与管理服务（CCM）的查询证书列表接口获取 **约束限制：** 配置SCM证书时必传 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type scm_certificate_id: str
        :param certificate_name: **参数解释：** 证书名称 **约束限制：** - 当证书开启时必传 - 3-64个字符 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type certificate_name: str
        :param certificate_value: **参数解释：** HTTPS协议使用的证书内容 **约束限制：** - 仅支持PEM编码格式 - 当证书开启时必传 -  需要传入完整证书链 **取值范围：** 证书链长度不超过20KB **默认取值：** 不涉及
        :type certificate_value: str
        :param private_key: **参数解释：** HTTPS协议使用的私钥 **约束限制：** - 当证书开启时必传 - 仅支持PEM编码格式 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type private_key: str
        :param enc_certificate_value: **参数解释：** 加密证书内容 **约束限制：** - 证书类型为国密证书时必传 - 仅支持PEM编码格式 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type enc_certificate_value: str
        :param enc_private_key: **参数解释：** 加密私钥内容 **约束限制：** - 证书类型为国密证书时必传 - 仅支持PEM编码格式 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type enc_private_key: str
        :param certificates: 
        :type certificates: list[:class:`huaweicloudsdkcdn.v2.CertificatesPutBody`]
        :param http2_status: **参数解释：** HTTP/2开关，支持客户端采用HTTP/2协议访问CDN节点 **约束限制：** https_status&#x3D;off时，该值不生效 **取值范围：** - on: 是 - off: 否 **默认取值：** off: 否
        :type http2_status: str
        :param ocsp_stapling_status: **参数解释：** 是否开启ocsp stapling **约束限制：** 不涉及 **取值范围：** - on: 是 - off: 否 **默认取值：** 不涉及
        :type ocsp_stapling_status: str
        """
        
        

        self._https_status = None
        self._certificate_type = None
        self._certificate_source = None
        self._scm_certificate_id = None
        self._certificate_name = None
        self._certificate_value = None
        self._private_key = None
        self._enc_certificate_value = None
        self._enc_private_key = None
        self._certificates = None
        self._http2_status = None
        self._ocsp_stapling_status = None
        self.discriminator = None

        if https_status is not None:
            self.https_status = https_status
        if certificate_type is not None:
            self.certificate_type = certificate_type
        if certificate_source is not None:
            self.certificate_source = certificate_source
        if scm_certificate_id is not None:
            self.scm_certificate_id = scm_certificate_id
        if certificate_name is not None:
            self.certificate_name = certificate_name
        if certificate_value is not None:
            self.certificate_value = certificate_value
        if private_key is not None:
            self.private_key = private_key
        if enc_certificate_value is not None:
            self.enc_certificate_value = enc_certificate_value
        if enc_private_key is not None:
            self.enc_private_key = enc_private_key
        if certificates is not None:
            self.certificates = certificates
        if http2_status is not None:
            self.http2_status = http2_status
        if ocsp_stapling_status is not None:
            self.ocsp_stapling_status = ocsp_stapling_status

    @property
    def https_status(self):
        r"""Gets the https_status of this HttpTemplateBody.

        **参数解释：** 证书配置开关 **约束限制：** 不涉及 **取值范围：** - on: 开启 - off: 关闭 **默认取值：** 不涉及

        :return: The https_status of this HttpTemplateBody.
        :rtype: str
        """
        return self._https_status

    @https_status.setter
    def https_status(self, https_status):
        r"""Sets the https_status of this HttpTemplateBody.

        **参数解释：** 证书配置开关 **约束限制：** 不涉及 **取值范围：** - on: 开启 - off: 关闭 **默认取值：** 不涉及

        :param https_status: The https_status of this HttpTemplateBody.
        :type https_status: str
        """
        self._https_status = https_status

    @property
    def certificate_type(self):
        r"""Gets the certificate_type of this HttpTemplateBody.

        **参数解释：** 证书类型 **约束限制：** 不涉及 **取值范围：** - server: 国际证书 - server_sm: 国密证书 **默认取值：** 不涉及

        :return: The certificate_type of this HttpTemplateBody.
        :rtype: str
        """
        return self._certificate_type

    @certificate_type.setter
    def certificate_type(self, certificate_type):
        r"""Sets the certificate_type of this HttpTemplateBody.

        **参数解释：** 证书类型 **约束限制：** 不涉及 **取值范围：** - server: 国际证书 - server_sm: 国密证书 **默认取值：** 不涉及

        :param certificate_type: The certificate_type of this HttpTemplateBody.
        :type certificate_type: str
        """
        self._certificate_type = certificate_type

    @property
    def certificate_source(self):
        r"""Gets the certificate_source of this HttpTemplateBody.

        **参数解释：** 证书来源 **约束限制：** 证书开启时必传 **取值范围：** - 0: 自有证书 - 2: SCM证书 **默认取值：** 不涉及

        :return: The certificate_source of this HttpTemplateBody.
        :rtype: int
        """
        return self._certificate_source

    @certificate_source.setter
    def certificate_source(self, certificate_source):
        r"""Sets the certificate_source of this HttpTemplateBody.

        **参数解释：** 证书来源 **约束限制：** 证书开启时必传 **取值范围：** - 0: 自有证书 - 2: SCM证书 **默认取值：** 不涉及

        :param certificate_source: The certificate_source of this HttpTemplateBody.
        :type certificate_source: int
        """
        self._certificate_source = certificate_source

    @property
    def scm_certificate_id(self):
        r"""Gets the scm_certificate_id of this HttpTemplateBody.

        **参数解释：** SCM证书ID，可使用云证书与管理服务（CCM）的查询证书列表接口获取 **约束限制：** 配置SCM证书时必传 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The scm_certificate_id of this HttpTemplateBody.
        :rtype: str
        """
        return self._scm_certificate_id

    @scm_certificate_id.setter
    def scm_certificate_id(self, scm_certificate_id):
        r"""Sets the scm_certificate_id of this HttpTemplateBody.

        **参数解释：** SCM证书ID，可使用云证书与管理服务（CCM）的查询证书列表接口获取 **约束限制：** 配置SCM证书时必传 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param scm_certificate_id: The scm_certificate_id of this HttpTemplateBody.
        :type scm_certificate_id: str
        """
        self._scm_certificate_id = scm_certificate_id

    @property
    def certificate_name(self):
        r"""Gets the certificate_name of this HttpTemplateBody.

        **参数解释：** 证书名称 **约束限制：** - 当证书开启时必传 - 3-64个字符 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The certificate_name of this HttpTemplateBody.
        :rtype: str
        """
        return self._certificate_name

    @certificate_name.setter
    def certificate_name(self, certificate_name):
        r"""Sets the certificate_name of this HttpTemplateBody.

        **参数解释：** 证书名称 **约束限制：** - 当证书开启时必传 - 3-64个字符 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param certificate_name: The certificate_name of this HttpTemplateBody.
        :type certificate_name: str
        """
        self._certificate_name = certificate_name

    @property
    def certificate_value(self):
        r"""Gets the certificate_value of this HttpTemplateBody.

        **参数解释：** HTTPS协议使用的证书内容 **约束限制：** - 仅支持PEM编码格式 - 当证书开启时必传 -  需要传入完整证书链 **取值范围：** 证书链长度不超过20KB **默认取值：** 不涉及

        :return: The certificate_value of this HttpTemplateBody.
        :rtype: str
        """
        return self._certificate_value

    @certificate_value.setter
    def certificate_value(self, certificate_value):
        r"""Sets the certificate_value of this HttpTemplateBody.

        **参数解释：** HTTPS协议使用的证书内容 **约束限制：** - 仅支持PEM编码格式 - 当证书开启时必传 -  需要传入完整证书链 **取值范围：** 证书链长度不超过20KB **默认取值：** 不涉及

        :param certificate_value: The certificate_value of this HttpTemplateBody.
        :type certificate_value: str
        """
        self._certificate_value = certificate_value

    @property
    def private_key(self):
        r"""Gets the private_key of this HttpTemplateBody.

        **参数解释：** HTTPS协议使用的私钥 **约束限制：** - 当证书开启时必传 - 仅支持PEM编码格式 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The private_key of this HttpTemplateBody.
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        r"""Sets the private_key of this HttpTemplateBody.

        **参数解释：** HTTPS协议使用的私钥 **约束限制：** - 当证书开启时必传 - 仅支持PEM编码格式 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param private_key: The private_key of this HttpTemplateBody.
        :type private_key: str
        """
        self._private_key = private_key

    @property
    def enc_certificate_value(self):
        r"""Gets the enc_certificate_value of this HttpTemplateBody.

        **参数解释：** 加密证书内容 **约束限制：** - 证书类型为国密证书时必传 - 仅支持PEM编码格式 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The enc_certificate_value of this HttpTemplateBody.
        :rtype: str
        """
        return self._enc_certificate_value

    @enc_certificate_value.setter
    def enc_certificate_value(self, enc_certificate_value):
        r"""Sets the enc_certificate_value of this HttpTemplateBody.

        **参数解释：** 加密证书内容 **约束限制：** - 证书类型为国密证书时必传 - 仅支持PEM编码格式 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param enc_certificate_value: The enc_certificate_value of this HttpTemplateBody.
        :type enc_certificate_value: str
        """
        self._enc_certificate_value = enc_certificate_value

    @property
    def enc_private_key(self):
        r"""Gets the enc_private_key of this HttpTemplateBody.

        **参数解释：** 加密私钥内容 **约束限制：** - 证书类型为国密证书时必传 - 仅支持PEM编码格式 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The enc_private_key of this HttpTemplateBody.
        :rtype: str
        """
        return self._enc_private_key

    @enc_private_key.setter
    def enc_private_key(self, enc_private_key):
        r"""Sets the enc_private_key of this HttpTemplateBody.

        **参数解释：** 加密私钥内容 **约束限制：** - 证书类型为国密证书时必传 - 仅支持PEM编码格式 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param enc_private_key: The enc_private_key of this HttpTemplateBody.
        :type enc_private_key: str
        """
        self._enc_private_key = enc_private_key

    @property
    def certificates(self):
        r"""Gets the certificates of this HttpTemplateBody.

        :return: The certificates of this HttpTemplateBody.
        :rtype: list[:class:`huaweicloudsdkcdn.v2.CertificatesPutBody`]
        """
        return self._certificates

    @certificates.setter
    def certificates(self, certificates):
        r"""Sets the certificates of this HttpTemplateBody.

        :param certificates: The certificates of this HttpTemplateBody.
        :type certificates: list[:class:`huaweicloudsdkcdn.v2.CertificatesPutBody`]
        """
        self._certificates = certificates

    @property
    def http2_status(self):
        r"""Gets the http2_status of this HttpTemplateBody.

        **参数解释：** HTTP/2开关，支持客户端采用HTTP/2协议访问CDN节点 **约束限制：** https_status=off时，该值不生效 **取值范围：** - on: 是 - off: 否 **默认取值：** off: 否

        :return: The http2_status of this HttpTemplateBody.
        :rtype: str
        """
        return self._http2_status

    @http2_status.setter
    def http2_status(self, http2_status):
        r"""Sets the http2_status of this HttpTemplateBody.

        **参数解释：** HTTP/2开关，支持客户端采用HTTP/2协议访问CDN节点 **约束限制：** https_status=off时，该值不生效 **取值范围：** - on: 是 - off: 否 **默认取值：** off: 否

        :param http2_status: The http2_status of this HttpTemplateBody.
        :type http2_status: str
        """
        self._http2_status = http2_status

    @property
    def ocsp_stapling_status(self):
        r"""Gets the ocsp_stapling_status of this HttpTemplateBody.

        **参数解释：** 是否开启ocsp stapling **约束限制：** 不涉及 **取值范围：** - on: 是 - off: 否 **默认取值：** 不涉及

        :return: The ocsp_stapling_status of this HttpTemplateBody.
        :rtype: str
        """
        return self._ocsp_stapling_status

    @ocsp_stapling_status.setter
    def ocsp_stapling_status(self, ocsp_stapling_status):
        r"""Sets the ocsp_stapling_status of this HttpTemplateBody.

        **参数解释：** 是否开启ocsp stapling **约束限制：** 不涉及 **取值范围：** - on: 是 - off: 否 **默认取值：** 不涉及

        :param ocsp_stapling_status: The ocsp_stapling_status of this HttpTemplateBody.
        :type ocsp_stapling_status: str
        """
        self._ocsp_stapling_status = ocsp_stapling_status

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
        if not isinstance(other, HttpTemplateBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
