# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateEcDatakeyPairResponse(SdkResponse):

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
        'key_spec': 'str',
        'public_key': 'str',
        'private_key_cipher_text': 'str',
        'private_key_plain_text': 'str',
        'wrapped_private_key': 'str',
        'ciphertext_recipient': 'str'
    }

    attribute_map = {
        'key_id': 'key_id',
        'key_spec': 'key_spec',
        'public_key': 'public_key',
        'private_key_cipher_text': 'private_key_cipher_text',
        'private_key_plain_text': 'private_key_plain_text',
        'wrapped_private_key': 'wrapped_private_key',
        'ciphertext_recipient': 'ciphertext_recipient'
    }

    def __init__(self, key_id=None, key_spec=None, public_key=None, private_key_cipher_text=None, private_key_plain_text=None, wrapped_private_key=None, ciphertext_recipient=None):
        r"""CreateEcDatakeyPairResponse

        The model defined in huaweicloud sdk

        :param key_id: 密钥ID。
        :type key_id: str
        :param key_spec: 需要包含算法、长度、曲线信息。可选值有RSA_2048 | RSA_3072 | RSA_4096 | ECC_NIST_P256 | ECC_NIST_P384 | ECC_NIST_P521 | ECC_SECG_P256K1 | SM2
        :type key_spec: str
        :param public_key: 明文公钥信息
        :type public_key: str
        :param private_key_cipher_text: 密文私钥
        :type private_key_cipher_text: str
        :param private_key_plain_text: 明文私钥。private_key_plain_text、wrapped_private_key和ciphertext_recipient只能有一个有值
        :type private_key_plain_text: str
        :param wrapped_private_key: 由自定义私钥加密的密文私钥。private_key_plain_text、wrapped_private_key和ciphertext_recipient只能有一个有值
        :type wrapped_private_key: str
        :param ciphertext_recipient: 由擎天公钥信息加密的密文私钥。private_key_plain_text、wrapped_private_key和ciphertext_recipient只能有一个有值
        :type ciphertext_recipient: str
        """
        
        super(CreateEcDatakeyPairResponse, self).__init__()

        self._key_id = None
        self._key_spec = None
        self._public_key = None
        self._private_key_cipher_text = None
        self._private_key_plain_text = None
        self._wrapped_private_key = None
        self._ciphertext_recipient = None
        self.discriminator = None

        if key_id is not None:
            self.key_id = key_id
        if key_spec is not None:
            self.key_spec = key_spec
        if public_key is not None:
            self.public_key = public_key
        if private_key_cipher_text is not None:
            self.private_key_cipher_text = private_key_cipher_text
        if private_key_plain_text is not None:
            self.private_key_plain_text = private_key_plain_text
        if wrapped_private_key is not None:
            self.wrapped_private_key = wrapped_private_key
        if ciphertext_recipient is not None:
            self.ciphertext_recipient = ciphertext_recipient

    @property
    def key_id(self):
        r"""Gets the key_id of this CreateEcDatakeyPairResponse.

        密钥ID。

        :return: The key_id of this CreateEcDatakeyPairResponse.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        r"""Sets the key_id of this CreateEcDatakeyPairResponse.

        密钥ID。

        :param key_id: The key_id of this CreateEcDatakeyPairResponse.
        :type key_id: str
        """
        self._key_id = key_id

    @property
    def key_spec(self):
        r"""Gets the key_spec of this CreateEcDatakeyPairResponse.

        需要包含算法、长度、曲线信息。可选值有RSA_2048 | RSA_3072 | RSA_4096 | ECC_NIST_P256 | ECC_NIST_P384 | ECC_NIST_P521 | ECC_SECG_P256K1 | SM2

        :return: The key_spec of this CreateEcDatakeyPairResponse.
        :rtype: str
        """
        return self._key_spec

    @key_spec.setter
    def key_spec(self, key_spec):
        r"""Sets the key_spec of this CreateEcDatakeyPairResponse.

        需要包含算法、长度、曲线信息。可选值有RSA_2048 | RSA_3072 | RSA_4096 | ECC_NIST_P256 | ECC_NIST_P384 | ECC_NIST_P521 | ECC_SECG_P256K1 | SM2

        :param key_spec: The key_spec of this CreateEcDatakeyPairResponse.
        :type key_spec: str
        """
        self._key_spec = key_spec

    @property
    def public_key(self):
        r"""Gets the public_key of this CreateEcDatakeyPairResponse.

        明文公钥信息

        :return: The public_key of this CreateEcDatakeyPairResponse.
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        r"""Sets the public_key of this CreateEcDatakeyPairResponse.

        明文公钥信息

        :param public_key: The public_key of this CreateEcDatakeyPairResponse.
        :type public_key: str
        """
        self._public_key = public_key

    @property
    def private_key_cipher_text(self):
        r"""Gets the private_key_cipher_text of this CreateEcDatakeyPairResponse.

        密文私钥

        :return: The private_key_cipher_text of this CreateEcDatakeyPairResponse.
        :rtype: str
        """
        return self._private_key_cipher_text

    @private_key_cipher_text.setter
    def private_key_cipher_text(self, private_key_cipher_text):
        r"""Sets the private_key_cipher_text of this CreateEcDatakeyPairResponse.

        密文私钥

        :param private_key_cipher_text: The private_key_cipher_text of this CreateEcDatakeyPairResponse.
        :type private_key_cipher_text: str
        """
        self._private_key_cipher_text = private_key_cipher_text

    @property
    def private_key_plain_text(self):
        r"""Gets the private_key_plain_text of this CreateEcDatakeyPairResponse.

        明文私钥。private_key_plain_text、wrapped_private_key和ciphertext_recipient只能有一个有值

        :return: The private_key_plain_text of this CreateEcDatakeyPairResponse.
        :rtype: str
        """
        return self._private_key_plain_text

    @private_key_plain_text.setter
    def private_key_plain_text(self, private_key_plain_text):
        r"""Sets the private_key_plain_text of this CreateEcDatakeyPairResponse.

        明文私钥。private_key_plain_text、wrapped_private_key和ciphertext_recipient只能有一个有值

        :param private_key_plain_text: The private_key_plain_text of this CreateEcDatakeyPairResponse.
        :type private_key_plain_text: str
        """
        self._private_key_plain_text = private_key_plain_text

    @property
    def wrapped_private_key(self):
        r"""Gets the wrapped_private_key of this CreateEcDatakeyPairResponse.

        由自定义私钥加密的密文私钥。private_key_plain_text、wrapped_private_key和ciphertext_recipient只能有一个有值

        :return: The wrapped_private_key of this CreateEcDatakeyPairResponse.
        :rtype: str
        """
        return self._wrapped_private_key

    @wrapped_private_key.setter
    def wrapped_private_key(self, wrapped_private_key):
        r"""Sets the wrapped_private_key of this CreateEcDatakeyPairResponse.

        由自定义私钥加密的密文私钥。private_key_plain_text、wrapped_private_key和ciphertext_recipient只能有一个有值

        :param wrapped_private_key: The wrapped_private_key of this CreateEcDatakeyPairResponse.
        :type wrapped_private_key: str
        """
        self._wrapped_private_key = wrapped_private_key

    @property
    def ciphertext_recipient(self):
        r"""Gets the ciphertext_recipient of this CreateEcDatakeyPairResponse.

        由擎天公钥信息加密的密文私钥。private_key_plain_text、wrapped_private_key和ciphertext_recipient只能有一个有值

        :return: The ciphertext_recipient of this CreateEcDatakeyPairResponse.
        :rtype: str
        """
        return self._ciphertext_recipient

    @ciphertext_recipient.setter
    def ciphertext_recipient(self, ciphertext_recipient):
        r"""Sets the ciphertext_recipient of this CreateEcDatakeyPairResponse.

        由擎天公钥信息加密的密文私钥。private_key_plain_text、wrapped_private_key和ciphertext_recipient只能有一个有值

        :param ciphertext_recipient: The ciphertext_recipient of this CreateEcDatakeyPairResponse.
        :type ciphertext_recipient: str
        """
        self._ciphertext_recipient = ciphertext_recipient

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
        if not isinstance(other, CreateEcDatakeyPairResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
