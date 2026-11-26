# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HttpsDetailCertificates:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'certificate_type': 'str',
        'certificate_source': 'int',
        'certificate_name': 'str',
        'certificate_value': 'str',
        'private_key': 'str',
        'enc_certificate_value': 'str',
        'enc_private_key': 'str',
        'expire_time': 'int',
        'scm_certificate_id': 'str'
    }

    attribute_map = {
        'certificate_type': 'certificate_type',
        'certificate_source': 'certificate_source',
        'certificate_name': 'certificate_name',
        'certificate_value': 'certificate_value',
        'private_key': 'private_key',
        'enc_certificate_value': 'enc_certificate_value',
        'enc_private_key': 'enc_private_key',
        'expire_time': 'expire_time',
        'scm_certificate_id': 'scm_certificate_id'
    }

    def __init__(self, certificate_type=None, certificate_source=None, certificate_name=None, certificate_value=None, private_key=None, enc_certificate_value=None, enc_private_key=None, expire_time=None, scm_certificate_id=None):
        r"""HttpsDetailCertificates

        The model defined in huaweicloud sdk

        :param certificate_type: **参数解释：** 证书类型 **约束限制：** 不涉及 **取值范围：** - server: 国际证书 - server_sm: 国密证书  **默认取值：** 不涉及
        :type certificate_type: str
        :param certificate_source: **参数解释：** 证书来源 **约束限制：** 不涉及 **取值范围：** - 0: 自有证书 - 1: 云托管证书 - 2: SCM证书  **默认取值：** 不涉及
        :type certificate_source: int
        :param certificate_name: **参数解释：** 证书名称 **约束限制：** 不涉及 **取值范围：** 不涉及
        :type certificate_name: str
        :param certificate_value: **参数解释：** 证书内容 **约束限制：** 不涉及 **取值范围：** 不涉及
        :type certificate_value: str
        :param private_key: **参数解释：** 私钥内容 **约束限制：** 不涉及 **取值范围：** 不涉及
        :type private_key: str
        :param enc_certificate_value: **参数解释：** 国密证书加密证书内容 **约束限制：** 不涉及 **取值范围：** 不涉及
        :type enc_certificate_value: str
        :param enc_private_key: **参数解释：** 国密证书加密私钥内容 **约束限制：** 不涉及 **取值范围：** 不涉及
        :type enc_private_key: str
        :param expire_time: **参数解释：** 证书过期时间，Unix时间戳格式，单位为毫秒 **约束限制：** 不涉及 **取值范围：** 不涉及
        :type expire_time: int
        :param scm_certificate_id: **参数解释：** SCM证书ID **约束限制：** 不涉及 **取值范围：** 不涉及
        :type scm_certificate_id: str
        """
        
        

        self._certificate_type = None
        self._certificate_source = None
        self._certificate_name = None
        self._certificate_value = None
        self._private_key = None
        self._enc_certificate_value = None
        self._enc_private_key = None
        self._expire_time = None
        self._scm_certificate_id = None
        self.discriminator = None

        if certificate_type is not None:
            self.certificate_type = certificate_type
        if certificate_source is not None:
            self.certificate_source = certificate_source
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
        if expire_time is not None:
            self.expire_time = expire_time
        if scm_certificate_id is not None:
            self.scm_certificate_id = scm_certificate_id

    @property
    def certificate_type(self):
        r"""Gets the certificate_type of this HttpsDetailCertificates.

        **参数解释：** 证书类型 **约束限制：** 不涉及 **取值范围：** - server: 国际证书 - server_sm: 国密证书  **默认取值：** 不涉及

        :return: The certificate_type of this HttpsDetailCertificates.
        :rtype: str
        """
        return self._certificate_type

    @certificate_type.setter
    def certificate_type(self, certificate_type):
        r"""Sets the certificate_type of this HttpsDetailCertificates.

        **参数解释：** 证书类型 **约束限制：** 不涉及 **取值范围：** - server: 国际证书 - server_sm: 国密证书  **默认取值：** 不涉及

        :param certificate_type: The certificate_type of this HttpsDetailCertificates.
        :type certificate_type: str
        """
        self._certificate_type = certificate_type

    @property
    def certificate_source(self):
        r"""Gets the certificate_source of this HttpsDetailCertificates.

        **参数解释：** 证书来源 **约束限制：** 不涉及 **取值范围：** - 0: 自有证书 - 1: 云托管证书 - 2: SCM证书  **默认取值：** 不涉及

        :return: The certificate_source of this HttpsDetailCertificates.
        :rtype: int
        """
        return self._certificate_source

    @certificate_source.setter
    def certificate_source(self, certificate_source):
        r"""Sets the certificate_source of this HttpsDetailCertificates.

        **参数解释：** 证书来源 **约束限制：** 不涉及 **取值范围：** - 0: 自有证书 - 1: 云托管证书 - 2: SCM证书  **默认取值：** 不涉及

        :param certificate_source: The certificate_source of this HttpsDetailCertificates.
        :type certificate_source: int
        """
        self._certificate_source = certificate_source

    @property
    def certificate_name(self):
        r"""Gets the certificate_name of this HttpsDetailCertificates.

        **参数解释：** 证书名称 **约束限制：** 不涉及 **取值范围：** 不涉及

        :return: The certificate_name of this HttpsDetailCertificates.
        :rtype: str
        """
        return self._certificate_name

    @certificate_name.setter
    def certificate_name(self, certificate_name):
        r"""Sets the certificate_name of this HttpsDetailCertificates.

        **参数解释：** 证书名称 **约束限制：** 不涉及 **取值范围：** 不涉及

        :param certificate_name: The certificate_name of this HttpsDetailCertificates.
        :type certificate_name: str
        """
        self._certificate_name = certificate_name

    @property
    def certificate_value(self):
        r"""Gets the certificate_value of this HttpsDetailCertificates.

        **参数解释：** 证书内容 **约束限制：** 不涉及 **取值范围：** 不涉及

        :return: The certificate_value of this HttpsDetailCertificates.
        :rtype: str
        """
        return self._certificate_value

    @certificate_value.setter
    def certificate_value(self, certificate_value):
        r"""Sets the certificate_value of this HttpsDetailCertificates.

        **参数解释：** 证书内容 **约束限制：** 不涉及 **取值范围：** 不涉及

        :param certificate_value: The certificate_value of this HttpsDetailCertificates.
        :type certificate_value: str
        """
        self._certificate_value = certificate_value

    @property
    def private_key(self):
        r"""Gets the private_key of this HttpsDetailCertificates.

        **参数解释：** 私钥内容 **约束限制：** 不涉及 **取值范围：** 不涉及

        :return: The private_key of this HttpsDetailCertificates.
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        r"""Sets the private_key of this HttpsDetailCertificates.

        **参数解释：** 私钥内容 **约束限制：** 不涉及 **取值范围：** 不涉及

        :param private_key: The private_key of this HttpsDetailCertificates.
        :type private_key: str
        """
        self._private_key = private_key

    @property
    def enc_certificate_value(self):
        r"""Gets the enc_certificate_value of this HttpsDetailCertificates.

        **参数解释：** 国密证书加密证书内容 **约束限制：** 不涉及 **取值范围：** 不涉及

        :return: The enc_certificate_value of this HttpsDetailCertificates.
        :rtype: str
        """
        return self._enc_certificate_value

    @enc_certificate_value.setter
    def enc_certificate_value(self, enc_certificate_value):
        r"""Sets the enc_certificate_value of this HttpsDetailCertificates.

        **参数解释：** 国密证书加密证书内容 **约束限制：** 不涉及 **取值范围：** 不涉及

        :param enc_certificate_value: The enc_certificate_value of this HttpsDetailCertificates.
        :type enc_certificate_value: str
        """
        self._enc_certificate_value = enc_certificate_value

    @property
    def enc_private_key(self):
        r"""Gets the enc_private_key of this HttpsDetailCertificates.

        **参数解释：** 国密证书加密私钥内容 **约束限制：** 不涉及 **取值范围：** 不涉及

        :return: The enc_private_key of this HttpsDetailCertificates.
        :rtype: str
        """
        return self._enc_private_key

    @enc_private_key.setter
    def enc_private_key(self, enc_private_key):
        r"""Sets the enc_private_key of this HttpsDetailCertificates.

        **参数解释：** 国密证书加密私钥内容 **约束限制：** 不涉及 **取值范围：** 不涉及

        :param enc_private_key: The enc_private_key of this HttpsDetailCertificates.
        :type enc_private_key: str
        """
        self._enc_private_key = enc_private_key

    @property
    def expire_time(self):
        r"""Gets the expire_time of this HttpsDetailCertificates.

        **参数解释：** 证书过期时间，Unix时间戳格式，单位为毫秒 **约束限制：** 不涉及 **取值范围：** 不涉及

        :return: The expire_time of this HttpsDetailCertificates.
        :rtype: int
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this HttpsDetailCertificates.

        **参数解释：** 证书过期时间，Unix时间戳格式，单位为毫秒 **约束限制：** 不涉及 **取值范围：** 不涉及

        :param expire_time: The expire_time of this HttpsDetailCertificates.
        :type expire_time: int
        """
        self._expire_time = expire_time

    @property
    def scm_certificate_id(self):
        r"""Gets the scm_certificate_id of this HttpsDetailCertificates.

        **参数解释：** SCM证书ID **约束限制：** 不涉及 **取值范围：** 不涉及

        :return: The scm_certificate_id of this HttpsDetailCertificates.
        :rtype: str
        """
        return self._scm_certificate_id

    @scm_certificate_id.setter
    def scm_certificate_id(self, scm_certificate_id):
        r"""Sets the scm_certificate_id of this HttpsDetailCertificates.

        **参数解释：** SCM证书ID **约束限制：** 不涉及 **取值范围：** 不涉及

        :param scm_certificate_id: The scm_certificate_id of this HttpsDetailCertificates.
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
        if not isinstance(other, HttpsDetailCertificates):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
