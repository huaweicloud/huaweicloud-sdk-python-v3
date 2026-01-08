# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCertDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cert_id': 'str',
        'serial_number': 'str',
        'type': 'str',
        'apply': 'str',
        'distinguished_name': 'DistinguishedName',
        'key_algorithm': 'str',
        'signature_algorithm': 'str',
        'not_before': 'str',
        'not_after': 'str',
        'status': 'str',
        'pem_code': 'str',
        'issuer_name': 'str',
        'crl_configuration': 'CrlConfigurationData'
    }

    attribute_map = {
        'cert_id': 'cert_id',
        'serial_number': 'serial_number',
        'type': 'type',
        'apply': 'apply',
        'distinguished_name': 'distinguished_name',
        'key_algorithm': 'key_algorithm',
        'signature_algorithm': 'signature_algorithm',
        'not_before': 'not_before',
        'not_after': 'not_after',
        'status': 'status',
        'pem_code': 'pem_code',
        'issuer_name': 'issuer_name',
        'crl_configuration': 'crl_configuration'
    }

    def __init__(self, cert_id=None, serial_number=None, type=None, apply=None, distinguished_name=None, key_algorithm=None, signature_algorithm=None, not_before=None, not_after=None, status=None, pem_code=None, issuer_name=None, crl_configuration=None):
        r"""ShowCertDetailResponse

        The model defined in huaweicloud sdk

        :param cert_id: 证书id。
        :type cert_id: str
        :param serial_number: 序列号。
        :type serial_number: str
        :param type: 证书类型。
        :type type: str
        :param apply: 证书应用范围。
        :type apply: str
        :param distinguished_name: 
        :type distinguished_name: :class:`huaweicloudsdkworkspace.v2.DistinguishedName`
        :param key_algorithm: 密钥对生成算法 RSA-2048 RSA-3072。
        :type key_algorithm: str
        :param signature_algorithm: 签名哈希算法 SHA-256 SHA-512。
        :type signature_algorithm: str
        :param not_before: 生效时间。
        :type not_before: str
        :param not_after: 过期时间。
        :type not_after: str
        :param status: 证书状态 DISABLE,ENABLE,EXPIRED,DELETE。
        :type status: str
        :param pem_code: 证书pem编码。
        :type pem_code: str
        :param issuer_name: 颁发者名字。
        :type issuer_name: str
        :param crl_configuration: 
        :type crl_configuration: :class:`huaweicloudsdkworkspace.v2.CrlConfigurationData`
        """
        
        super().__init__()

        self._cert_id = None
        self._serial_number = None
        self._type = None
        self._apply = None
        self._distinguished_name = None
        self._key_algorithm = None
        self._signature_algorithm = None
        self._not_before = None
        self._not_after = None
        self._status = None
        self._pem_code = None
        self._issuer_name = None
        self._crl_configuration = None
        self.discriminator = None

        if cert_id is not None:
            self.cert_id = cert_id
        if serial_number is not None:
            self.serial_number = serial_number
        if type is not None:
            self.type = type
        if apply is not None:
            self.apply = apply
        if distinguished_name is not None:
            self.distinguished_name = distinguished_name
        if key_algorithm is not None:
            self.key_algorithm = key_algorithm
        if signature_algorithm is not None:
            self.signature_algorithm = signature_algorithm
        if not_before is not None:
            self.not_before = not_before
        if not_after is not None:
            self.not_after = not_after
        if status is not None:
            self.status = status
        if pem_code is not None:
            self.pem_code = pem_code
        if issuer_name is not None:
            self.issuer_name = issuer_name
        if crl_configuration is not None:
            self.crl_configuration = crl_configuration

    @property
    def cert_id(self):
        r"""Gets the cert_id of this ShowCertDetailResponse.

        证书id。

        :return: The cert_id of this ShowCertDetailResponse.
        :rtype: str
        """
        return self._cert_id

    @cert_id.setter
    def cert_id(self, cert_id):
        r"""Sets the cert_id of this ShowCertDetailResponse.

        证书id。

        :param cert_id: The cert_id of this ShowCertDetailResponse.
        :type cert_id: str
        """
        self._cert_id = cert_id

    @property
    def serial_number(self):
        r"""Gets the serial_number of this ShowCertDetailResponse.

        序列号。

        :return: The serial_number of this ShowCertDetailResponse.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        r"""Sets the serial_number of this ShowCertDetailResponse.

        序列号。

        :param serial_number: The serial_number of this ShowCertDetailResponse.
        :type serial_number: str
        """
        self._serial_number = serial_number

    @property
    def type(self):
        r"""Gets the type of this ShowCertDetailResponse.

        证书类型。

        :return: The type of this ShowCertDetailResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowCertDetailResponse.

        证书类型。

        :param type: The type of this ShowCertDetailResponse.
        :type type: str
        """
        self._type = type

    @property
    def apply(self):
        r"""Gets the apply of this ShowCertDetailResponse.

        证书应用范围。

        :return: The apply of this ShowCertDetailResponse.
        :rtype: str
        """
        return self._apply

    @apply.setter
    def apply(self, apply):
        r"""Sets the apply of this ShowCertDetailResponse.

        证书应用范围。

        :param apply: The apply of this ShowCertDetailResponse.
        :type apply: str
        """
        self._apply = apply

    @property
    def distinguished_name(self):
        r"""Gets the distinguished_name of this ShowCertDetailResponse.

        :return: The distinguished_name of this ShowCertDetailResponse.
        :rtype: :class:`huaweicloudsdkworkspace.v2.DistinguishedName`
        """
        return self._distinguished_name

    @distinguished_name.setter
    def distinguished_name(self, distinguished_name):
        r"""Sets the distinguished_name of this ShowCertDetailResponse.

        :param distinguished_name: The distinguished_name of this ShowCertDetailResponse.
        :type distinguished_name: :class:`huaweicloudsdkworkspace.v2.DistinguishedName`
        """
        self._distinguished_name = distinguished_name

    @property
    def key_algorithm(self):
        r"""Gets the key_algorithm of this ShowCertDetailResponse.

        密钥对生成算法 RSA-2048 RSA-3072。

        :return: The key_algorithm of this ShowCertDetailResponse.
        :rtype: str
        """
        return self._key_algorithm

    @key_algorithm.setter
    def key_algorithm(self, key_algorithm):
        r"""Sets the key_algorithm of this ShowCertDetailResponse.

        密钥对生成算法 RSA-2048 RSA-3072。

        :param key_algorithm: The key_algorithm of this ShowCertDetailResponse.
        :type key_algorithm: str
        """
        self._key_algorithm = key_algorithm

    @property
    def signature_algorithm(self):
        r"""Gets the signature_algorithm of this ShowCertDetailResponse.

        签名哈希算法 SHA-256 SHA-512。

        :return: The signature_algorithm of this ShowCertDetailResponse.
        :rtype: str
        """
        return self._signature_algorithm

    @signature_algorithm.setter
    def signature_algorithm(self, signature_algorithm):
        r"""Sets the signature_algorithm of this ShowCertDetailResponse.

        签名哈希算法 SHA-256 SHA-512。

        :param signature_algorithm: The signature_algorithm of this ShowCertDetailResponse.
        :type signature_algorithm: str
        """
        self._signature_algorithm = signature_algorithm

    @property
    def not_before(self):
        r"""Gets the not_before of this ShowCertDetailResponse.

        生效时间。

        :return: The not_before of this ShowCertDetailResponse.
        :rtype: str
        """
        return self._not_before

    @not_before.setter
    def not_before(self, not_before):
        r"""Sets the not_before of this ShowCertDetailResponse.

        生效时间。

        :param not_before: The not_before of this ShowCertDetailResponse.
        :type not_before: str
        """
        self._not_before = not_before

    @property
    def not_after(self):
        r"""Gets the not_after of this ShowCertDetailResponse.

        过期时间。

        :return: The not_after of this ShowCertDetailResponse.
        :rtype: str
        """
        return self._not_after

    @not_after.setter
    def not_after(self, not_after):
        r"""Sets the not_after of this ShowCertDetailResponse.

        过期时间。

        :param not_after: The not_after of this ShowCertDetailResponse.
        :type not_after: str
        """
        self._not_after = not_after

    @property
    def status(self):
        r"""Gets the status of this ShowCertDetailResponse.

        证书状态 DISABLE,ENABLE,EXPIRED,DELETE。

        :return: The status of this ShowCertDetailResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowCertDetailResponse.

        证书状态 DISABLE,ENABLE,EXPIRED,DELETE。

        :param status: The status of this ShowCertDetailResponse.
        :type status: str
        """
        self._status = status

    @property
    def pem_code(self):
        r"""Gets the pem_code of this ShowCertDetailResponse.

        证书pem编码。

        :return: The pem_code of this ShowCertDetailResponse.
        :rtype: str
        """
        return self._pem_code

    @pem_code.setter
    def pem_code(self, pem_code):
        r"""Sets the pem_code of this ShowCertDetailResponse.

        证书pem编码。

        :param pem_code: The pem_code of this ShowCertDetailResponse.
        :type pem_code: str
        """
        self._pem_code = pem_code

    @property
    def issuer_name(self):
        r"""Gets the issuer_name of this ShowCertDetailResponse.

        颁发者名字。

        :return: The issuer_name of this ShowCertDetailResponse.
        :rtype: str
        """
        return self._issuer_name

    @issuer_name.setter
    def issuer_name(self, issuer_name):
        r"""Sets the issuer_name of this ShowCertDetailResponse.

        颁发者名字。

        :param issuer_name: The issuer_name of this ShowCertDetailResponse.
        :type issuer_name: str
        """
        self._issuer_name = issuer_name

    @property
    def crl_configuration(self):
        r"""Gets the crl_configuration of this ShowCertDetailResponse.

        :return: The crl_configuration of this ShowCertDetailResponse.
        :rtype: :class:`huaweicloudsdkworkspace.v2.CrlConfigurationData`
        """
        return self._crl_configuration

    @crl_configuration.setter
    def crl_configuration(self, crl_configuration):
        r"""Sets the crl_configuration of this ShowCertDetailResponse.

        :param crl_configuration: The crl_configuration of this ShowCertDetailResponse.
        :type crl_configuration: :class:`huaweicloudsdkworkspace.v2.CrlConfigurationData`
        """
        self._crl_configuration = crl_configuration

    def to_dict(self):
        import warnings
        warnings.warn("ShowCertDetailResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowCertDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
