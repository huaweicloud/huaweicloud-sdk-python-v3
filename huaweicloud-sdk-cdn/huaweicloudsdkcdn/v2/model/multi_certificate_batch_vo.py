# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MultiCertificateBatchVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cert_name': 'str',
        'certificate_category': 'int',
        'certificate_type': 'int',
        'certificate': 'str',
        'private_key': 'str',
        'enc_certificate': 'str',
        'enc_private_key': 'str',
        'scm_certificate_id': 'str'
    }

    attribute_map = {
        'cert_name': 'cert_name',
        'certificate_category': 'certificate_category',
        'certificate_type': 'certificate_type',
        'certificate': 'certificate',
        'private_key': 'private_key',
        'enc_certificate': 'enc_certificate',
        'enc_private_key': 'enc_private_key',
        'scm_certificate_id': 'scm_certificate_id'
    }

    def __init__(self, cert_name=None, certificate_category=None, certificate_type=None, certificate=None, private_key=None, enc_certificate=None, enc_private_key=None, scm_certificate_id=None):
        r"""MultiCertificateBatchVo

        The model defined in huaweicloud sdk

        :param cert_name: **参数解释：** 证书名称 **约束限制：** 不涉及 **取值范围：** - 3-64个字符 - 由英文字母、数字及“-”、“_”、空格组成  **默认取值：** 不涉及
        :type cert_name: str
        :param certificate_category: **参数解释：** 证书类型 **约束限制：** 不涉及 **取值范围：** - 0: 国际证书 - 1: 国密证书  **默认取值：** 不涉及
        :type certificate_category: int
        :param certificate_type: **参数解释：** 证书类型 **约束限制：** 不涉及 **取值范围：** - 0: 自有证书 - 1: 云托管证书 - 2: SCM证书  **默认取值：** 不涉及
        :type certificate_type: int
        :param certificate: **参数解释：** SSL证书内容 **约束限制：** - 仅支持PEM编码格式 - 需要传入完整证书链  **取值范围：** 证书链长度不超过20KB **默认取值：** 不涉及
        :type certificate: str
        :param private_key: **参数解释：** SSL证书私钥内容 **约束限制：** - 仅支持PEM编码格式  **取值范围：** 不涉及 **默认取值：** 不涉及
        :type private_key: str
        :param enc_certificate: **参数解释：** 国密证书加密证书内容 **约束限制：** certificate_category 为 1 且 certificate_type 为 0 时必传，须与 enc_private_key 同时传入 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type enc_certificate: str
        :param enc_private_key: **参数解释：** 国密证书加密私钥内容 **约束限制：** certificate_category 为 1 且 certificate_type 为 0 时必传，须与 enc_certificate 同时传入 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type enc_private_key: str
        :param scm_certificate_id: **参数解释：** SCM证书ID，配置SCM证书时必传 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type scm_certificate_id: str
        """
        
        

        self._cert_name = None
        self._certificate_category = None
        self._certificate_type = None
        self._certificate = None
        self._private_key = None
        self._enc_certificate = None
        self._enc_private_key = None
        self._scm_certificate_id = None
        self.discriminator = None

        if cert_name is not None:
            self.cert_name = cert_name
        if certificate_category is not None:
            self.certificate_category = certificate_category
        if certificate_type is not None:
            self.certificate_type = certificate_type
        if certificate is not None:
            self.certificate = certificate
        if private_key is not None:
            self.private_key = private_key
        if enc_certificate is not None:
            self.enc_certificate = enc_certificate
        if enc_private_key is not None:
            self.enc_private_key = enc_private_key
        if scm_certificate_id is not None:
            self.scm_certificate_id = scm_certificate_id

    @property
    def cert_name(self):
        r"""Gets the cert_name of this MultiCertificateBatchVo.

        **参数解释：** 证书名称 **约束限制：** 不涉及 **取值范围：** - 3-64个字符 - 由英文字母、数字及“-”、“_”、空格组成  **默认取值：** 不涉及

        :return: The cert_name of this MultiCertificateBatchVo.
        :rtype: str
        """
        return self._cert_name

    @cert_name.setter
    def cert_name(self, cert_name):
        r"""Sets the cert_name of this MultiCertificateBatchVo.

        **参数解释：** 证书名称 **约束限制：** 不涉及 **取值范围：** - 3-64个字符 - 由英文字母、数字及“-”、“_”、空格组成  **默认取值：** 不涉及

        :param cert_name: The cert_name of this MultiCertificateBatchVo.
        :type cert_name: str
        """
        self._cert_name = cert_name

    @property
    def certificate_category(self):
        r"""Gets the certificate_category of this MultiCertificateBatchVo.

        **参数解释：** 证书类型 **约束限制：** 不涉及 **取值范围：** - 0: 国际证书 - 1: 国密证书  **默认取值：** 不涉及

        :return: The certificate_category of this MultiCertificateBatchVo.
        :rtype: int
        """
        return self._certificate_category

    @certificate_category.setter
    def certificate_category(self, certificate_category):
        r"""Sets the certificate_category of this MultiCertificateBatchVo.

        **参数解释：** 证书类型 **约束限制：** 不涉及 **取值范围：** - 0: 国际证书 - 1: 国密证书  **默认取值：** 不涉及

        :param certificate_category: The certificate_category of this MultiCertificateBatchVo.
        :type certificate_category: int
        """
        self._certificate_category = certificate_category

    @property
    def certificate_type(self):
        r"""Gets the certificate_type of this MultiCertificateBatchVo.

        **参数解释：** 证书类型 **约束限制：** 不涉及 **取值范围：** - 0: 自有证书 - 1: 云托管证书 - 2: SCM证书  **默认取值：** 不涉及

        :return: The certificate_type of this MultiCertificateBatchVo.
        :rtype: int
        """
        return self._certificate_type

    @certificate_type.setter
    def certificate_type(self, certificate_type):
        r"""Sets the certificate_type of this MultiCertificateBatchVo.

        **参数解释：** 证书类型 **约束限制：** 不涉及 **取值范围：** - 0: 自有证书 - 1: 云托管证书 - 2: SCM证书  **默认取值：** 不涉及

        :param certificate_type: The certificate_type of this MultiCertificateBatchVo.
        :type certificate_type: int
        """
        self._certificate_type = certificate_type

    @property
    def certificate(self):
        r"""Gets the certificate of this MultiCertificateBatchVo.

        **参数解释：** SSL证书内容 **约束限制：** - 仅支持PEM编码格式 - 需要传入完整证书链  **取值范围：** 证书链长度不超过20KB **默认取值：** 不涉及

        :return: The certificate of this MultiCertificateBatchVo.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        r"""Sets the certificate of this MultiCertificateBatchVo.

        **参数解释：** SSL证书内容 **约束限制：** - 仅支持PEM编码格式 - 需要传入完整证书链  **取值范围：** 证书链长度不超过20KB **默认取值：** 不涉及

        :param certificate: The certificate of this MultiCertificateBatchVo.
        :type certificate: str
        """
        self._certificate = certificate

    @property
    def private_key(self):
        r"""Gets the private_key of this MultiCertificateBatchVo.

        **参数解释：** SSL证书私钥内容 **约束限制：** - 仅支持PEM编码格式  **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The private_key of this MultiCertificateBatchVo.
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        r"""Sets the private_key of this MultiCertificateBatchVo.

        **参数解释：** SSL证书私钥内容 **约束限制：** - 仅支持PEM编码格式  **取值范围：** 不涉及 **默认取值：** 不涉及

        :param private_key: The private_key of this MultiCertificateBatchVo.
        :type private_key: str
        """
        self._private_key = private_key

    @property
    def enc_certificate(self):
        r"""Gets the enc_certificate of this MultiCertificateBatchVo.

        **参数解释：** 国密证书加密证书内容 **约束限制：** certificate_category 为 1 且 certificate_type 为 0 时必传，须与 enc_private_key 同时传入 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The enc_certificate of this MultiCertificateBatchVo.
        :rtype: str
        """
        return self._enc_certificate

    @enc_certificate.setter
    def enc_certificate(self, enc_certificate):
        r"""Sets the enc_certificate of this MultiCertificateBatchVo.

        **参数解释：** 国密证书加密证书内容 **约束限制：** certificate_category 为 1 且 certificate_type 为 0 时必传，须与 enc_private_key 同时传入 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param enc_certificate: The enc_certificate of this MultiCertificateBatchVo.
        :type enc_certificate: str
        """
        self._enc_certificate = enc_certificate

    @property
    def enc_private_key(self):
        r"""Gets the enc_private_key of this MultiCertificateBatchVo.

        **参数解释：** 国密证书加密私钥内容 **约束限制：** certificate_category 为 1 且 certificate_type 为 0 时必传，须与 enc_certificate 同时传入 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The enc_private_key of this MultiCertificateBatchVo.
        :rtype: str
        """
        return self._enc_private_key

    @enc_private_key.setter
    def enc_private_key(self, enc_private_key):
        r"""Sets the enc_private_key of this MultiCertificateBatchVo.

        **参数解释：** 国密证书加密私钥内容 **约束限制：** certificate_category 为 1 且 certificate_type 为 0 时必传，须与 enc_certificate 同时传入 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param enc_private_key: The enc_private_key of this MultiCertificateBatchVo.
        :type enc_private_key: str
        """
        self._enc_private_key = enc_private_key

    @property
    def scm_certificate_id(self):
        r"""Gets the scm_certificate_id of this MultiCertificateBatchVo.

        **参数解释：** SCM证书ID，配置SCM证书时必传 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The scm_certificate_id of this MultiCertificateBatchVo.
        :rtype: str
        """
        return self._scm_certificate_id

    @scm_certificate_id.setter
    def scm_certificate_id(self, scm_certificate_id):
        r"""Sets the scm_certificate_id of this MultiCertificateBatchVo.

        **参数解释：** SCM证书ID，配置SCM证书时必传 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param scm_certificate_id: The scm_certificate_id of this MultiCertificateBatchVo.
        :type scm_certificate_id: str
        """
        self._scm_certificate_id = scm_certificate_id

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
        if not isinstance(other, MultiCertificateBatchVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
