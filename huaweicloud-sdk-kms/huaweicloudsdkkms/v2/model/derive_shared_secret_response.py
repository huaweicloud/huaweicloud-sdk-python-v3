# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeriveSharedSecretResponse(SdkResponse):

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
        'shared_secret': 'str',
        'ciphertext_recipient': 'str'
    }

    attribute_map = {
        'key_id': 'key_id',
        'key_agreement_algorithm': 'key_agreement_algorithm',
        'shared_secret': 'shared_secret',
        'ciphertext_recipient': 'ciphertext_recipient'
    }

    def __init__(self, key_id=None, key_agreement_algorithm=None, shared_secret=None, ciphertext_recipient=None):
        r"""DeriveSharedSecretResponse

        The model defined in huaweicloud sdk

        :param key_id: 密钥ID
        :type key_id: str
        :param key_agreement_algorithm: 密钥协商算法
        :type key_agreement_algorithm: str
        :param shared_secret: 由KMS私钥和您的对端公钥协商出的密钥，Base64格式，如果响应体包含了ciphertext_recipient，则不会包含shared_secret
        :type shared_secret: str
        :param ciphertext_recipient: KMS私钥和您的对端公钥协商出的密钥经过擎天证明文档加密后的密文，密文仅能被机密环境中的私钥解密，指定擎天证明文档后，才会响应ciphertext_recipient，否则通过shared_secret响应明文的共享密钥
        :type ciphertext_recipient: str
        """
        
        super().__init__()

        self._key_id = None
        self._key_agreement_algorithm = None
        self._shared_secret = None
        self._ciphertext_recipient = None
        self.discriminator = None

        if key_id is not None:
            self.key_id = key_id
        if key_agreement_algorithm is not None:
            self.key_agreement_algorithm = key_agreement_algorithm
        if shared_secret is not None:
            self.shared_secret = shared_secret
        if ciphertext_recipient is not None:
            self.ciphertext_recipient = ciphertext_recipient

    @property
    def key_id(self):
        r"""Gets the key_id of this DeriveSharedSecretResponse.

        密钥ID

        :return: The key_id of this DeriveSharedSecretResponse.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        r"""Sets the key_id of this DeriveSharedSecretResponse.

        密钥ID

        :param key_id: The key_id of this DeriveSharedSecretResponse.
        :type key_id: str
        """
        self._key_id = key_id

    @property
    def key_agreement_algorithm(self):
        r"""Gets the key_agreement_algorithm of this DeriveSharedSecretResponse.

        密钥协商算法

        :return: The key_agreement_algorithm of this DeriveSharedSecretResponse.
        :rtype: str
        """
        return self._key_agreement_algorithm

    @key_agreement_algorithm.setter
    def key_agreement_algorithm(self, key_agreement_algorithm):
        r"""Sets the key_agreement_algorithm of this DeriveSharedSecretResponse.

        密钥协商算法

        :param key_agreement_algorithm: The key_agreement_algorithm of this DeriveSharedSecretResponse.
        :type key_agreement_algorithm: str
        """
        self._key_agreement_algorithm = key_agreement_algorithm

    @property
    def shared_secret(self):
        r"""Gets the shared_secret of this DeriveSharedSecretResponse.

        由KMS私钥和您的对端公钥协商出的密钥，Base64格式，如果响应体包含了ciphertext_recipient，则不会包含shared_secret

        :return: The shared_secret of this DeriveSharedSecretResponse.
        :rtype: str
        """
        return self._shared_secret

    @shared_secret.setter
    def shared_secret(self, shared_secret):
        r"""Sets the shared_secret of this DeriveSharedSecretResponse.

        由KMS私钥和您的对端公钥协商出的密钥，Base64格式，如果响应体包含了ciphertext_recipient，则不会包含shared_secret

        :param shared_secret: The shared_secret of this DeriveSharedSecretResponse.
        :type shared_secret: str
        """
        self._shared_secret = shared_secret

    @property
    def ciphertext_recipient(self):
        r"""Gets the ciphertext_recipient of this DeriveSharedSecretResponse.

        KMS私钥和您的对端公钥协商出的密钥经过擎天证明文档加密后的密文，密文仅能被机密环境中的私钥解密，指定擎天证明文档后，才会响应ciphertext_recipient，否则通过shared_secret响应明文的共享密钥

        :return: The ciphertext_recipient of this DeriveSharedSecretResponse.
        :rtype: str
        """
        return self._ciphertext_recipient

    @ciphertext_recipient.setter
    def ciphertext_recipient(self, ciphertext_recipient):
        r"""Sets the ciphertext_recipient of this DeriveSharedSecretResponse.

        KMS私钥和您的对端公钥协商出的密钥经过擎天证明文档加密后的密文，密文仅能被机密环境中的私钥解密，指定擎天证明文档后，才会响应ciphertext_recipient，否则通过shared_secret响应明文的共享密钥

        :param ciphertext_recipient: The ciphertext_recipient of this DeriveSharedSecretResponse.
        :type ciphertext_recipient: str
        """
        self._ciphertext_recipient = ciphertext_recipient

    def to_dict(self):
        import warnings
        warnings.warn("DeriveSharedSecretResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, DeriveSharedSecretResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
