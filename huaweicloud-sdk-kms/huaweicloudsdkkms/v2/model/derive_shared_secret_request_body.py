# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeriveSharedSecretRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key_id': 'str',
        'key_agreement_algorithm': 'str',
        'public_key': 'str',
        'recipient': 'Recipient'
    }

    attribute_map = {
        'key_id': 'key_id',
        'key_agreement_algorithm': 'key_agreement_algorithm',
        'public_key': 'public_key',
        'recipient': 'recipient'
    }

    def __init__(self, key_id=None, key_agreement_algorithm=None, public_key=None, recipient=None):
        r"""DeriveSharedSecretRequestBody

        The model defined in huaweicloud sdk

        :param key_id: 密钥ID
        :type key_id: str
        :param key_agreement_algorithm: 密钥协商算法，仅支持ECDH
        :type key_agreement_algorithm: str
        :param public_key: 对端密钥对的的公钥，您需要保证是EC_P256，EC_384，SECP256K1或SM2(仅中国区域支持)密钥对的公钥。公钥的格式必须是DER-encoded X.509类型的Base64的字符串
        :type public_key: str
        :param recipient: 
        :type recipient: :class:`huaweicloudsdkkms.v2.Recipient`
        """
        
        

        self._key_id = None
        self._key_agreement_algorithm = None
        self._public_key = None
        self._recipient = None
        self.discriminator = None

        self.key_id = key_id
        self.key_agreement_algorithm = key_agreement_algorithm
        self.public_key = public_key
        if recipient is not None:
            self.recipient = recipient

    @property
    def key_id(self):
        r"""Gets the key_id of this DeriveSharedSecretRequestBody.

        密钥ID

        :return: The key_id of this DeriveSharedSecretRequestBody.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        r"""Sets the key_id of this DeriveSharedSecretRequestBody.

        密钥ID

        :param key_id: The key_id of this DeriveSharedSecretRequestBody.
        :type key_id: str
        """
        self._key_id = key_id

    @property
    def key_agreement_algorithm(self):
        r"""Gets the key_agreement_algorithm of this DeriveSharedSecretRequestBody.

        密钥协商算法，仅支持ECDH

        :return: The key_agreement_algorithm of this DeriveSharedSecretRequestBody.
        :rtype: str
        """
        return self._key_agreement_algorithm

    @key_agreement_algorithm.setter
    def key_agreement_algorithm(self, key_agreement_algorithm):
        r"""Sets the key_agreement_algorithm of this DeriveSharedSecretRequestBody.

        密钥协商算法，仅支持ECDH

        :param key_agreement_algorithm: The key_agreement_algorithm of this DeriveSharedSecretRequestBody.
        :type key_agreement_algorithm: str
        """
        self._key_agreement_algorithm = key_agreement_algorithm

    @property
    def public_key(self):
        r"""Gets the public_key of this DeriveSharedSecretRequestBody.

        对端密钥对的的公钥，您需要保证是EC_P256，EC_384，SECP256K1或SM2(仅中国区域支持)密钥对的公钥。公钥的格式必须是DER-encoded X.509类型的Base64的字符串

        :return: The public_key of this DeriveSharedSecretRequestBody.
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        r"""Sets the public_key of this DeriveSharedSecretRequestBody.

        对端密钥对的的公钥，您需要保证是EC_P256，EC_384，SECP256K1或SM2(仅中国区域支持)密钥对的公钥。公钥的格式必须是DER-encoded X.509类型的Base64的字符串

        :param public_key: The public_key of this DeriveSharedSecretRequestBody.
        :type public_key: str
        """
        self._public_key = public_key

    @property
    def recipient(self):
        r"""Gets the recipient of this DeriveSharedSecretRequestBody.

        :return: The recipient of this DeriveSharedSecretRequestBody.
        :rtype: :class:`huaweicloudsdkkms.v2.Recipient`
        """
        return self._recipient

    @recipient.setter
    def recipient(self, recipient):
        r"""Sets the recipient of this DeriveSharedSecretRequestBody.

        :param recipient: The recipient of this DeriveSharedSecretRequestBody.
        :type recipient: :class:`huaweicloudsdkkms.v2.Recipient`
        """
        self._recipient = recipient

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
        if not isinstance(other, DeriveSharedSecretRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
