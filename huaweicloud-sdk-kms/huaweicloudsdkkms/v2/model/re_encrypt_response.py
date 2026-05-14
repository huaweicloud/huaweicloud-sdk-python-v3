# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReEncryptResponse(SdkResponse):

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
        'source_key_id': 'str',
        'source_encryption_algorithm': 'str',
        'destination_encryption_algorithm': 'str',
        'cipher_text': 'str'
    }

    attribute_map = {
        'key_id': 'key_id',
        'source_key_id': 'source_key_id',
        'source_encryption_algorithm': 'source_encryption_algorithm',
        'destination_encryption_algorithm': 'destination_encryption_algorithm',
        'cipher_text': 'cipher_text'
    }

    def __init__(self, key_id=None, source_key_id=None, source_encryption_algorithm=None, destination_encryption_algorithm=None, cipher_text=None):
        r"""ReEncryptResponse

        The model defined in huaweicloud sdk

        :param key_id: 重新加密时使用的密钥ID
        :type key_id: str
        :param source_key_id: 加密原密文时使用的密钥ID
        :type source_key_id: str
        :param source_encryption_algorithm: 原密文加密时使用的加密算法
        :type source_encryption_algorithm: str
        :param destination_encryption_algorithm: 重新加密时使用的加密算法
        :type destination_encryption_algorithm: str
        :param cipher_text: 重新加密后的密文
        :type cipher_text: str
        """
        
        super().__init__()

        self._key_id = None
        self._source_key_id = None
        self._source_encryption_algorithm = None
        self._destination_encryption_algorithm = None
        self._cipher_text = None
        self.discriminator = None

        if key_id is not None:
            self.key_id = key_id
        if source_key_id is not None:
            self.source_key_id = source_key_id
        if source_encryption_algorithm is not None:
            self.source_encryption_algorithm = source_encryption_algorithm
        if destination_encryption_algorithm is not None:
            self.destination_encryption_algorithm = destination_encryption_algorithm
        if cipher_text is not None:
            self.cipher_text = cipher_text

    @property
    def key_id(self):
        r"""Gets the key_id of this ReEncryptResponse.

        重新加密时使用的密钥ID

        :return: The key_id of this ReEncryptResponse.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        r"""Sets the key_id of this ReEncryptResponse.

        重新加密时使用的密钥ID

        :param key_id: The key_id of this ReEncryptResponse.
        :type key_id: str
        """
        self._key_id = key_id

    @property
    def source_key_id(self):
        r"""Gets the source_key_id of this ReEncryptResponse.

        加密原密文时使用的密钥ID

        :return: The source_key_id of this ReEncryptResponse.
        :rtype: str
        """
        return self._source_key_id

    @source_key_id.setter
    def source_key_id(self, source_key_id):
        r"""Sets the source_key_id of this ReEncryptResponse.

        加密原密文时使用的密钥ID

        :param source_key_id: The source_key_id of this ReEncryptResponse.
        :type source_key_id: str
        """
        self._source_key_id = source_key_id

    @property
    def source_encryption_algorithm(self):
        r"""Gets the source_encryption_algorithm of this ReEncryptResponse.

        原密文加密时使用的加密算法

        :return: The source_encryption_algorithm of this ReEncryptResponse.
        :rtype: str
        """
        return self._source_encryption_algorithm

    @source_encryption_algorithm.setter
    def source_encryption_algorithm(self, source_encryption_algorithm):
        r"""Sets the source_encryption_algorithm of this ReEncryptResponse.

        原密文加密时使用的加密算法

        :param source_encryption_algorithm: The source_encryption_algorithm of this ReEncryptResponse.
        :type source_encryption_algorithm: str
        """
        self._source_encryption_algorithm = source_encryption_algorithm

    @property
    def destination_encryption_algorithm(self):
        r"""Gets the destination_encryption_algorithm of this ReEncryptResponse.

        重新加密时使用的加密算法

        :return: The destination_encryption_algorithm of this ReEncryptResponse.
        :rtype: str
        """
        return self._destination_encryption_algorithm

    @destination_encryption_algorithm.setter
    def destination_encryption_algorithm(self, destination_encryption_algorithm):
        r"""Sets the destination_encryption_algorithm of this ReEncryptResponse.

        重新加密时使用的加密算法

        :param destination_encryption_algorithm: The destination_encryption_algorithm of this ReEncryptResponse.
        :type destination_encryption_algorithm: str
        """
        self._destination_encryption_algorithm = destination_encryption_algorithm

    @property
    def cipher_text(self):
        r"""Gets the cipher_text of this ReEncryptResponse.

        重新加密后的密文

        :return: The cipher_text of this ReEncryptResponse.
        :rtype: str
        """
        return self._cipher_text

    @cipher_text.setter
    def cipher_text(self, cipher_text):
        r"""Sets the cipher_text of this ReEncryptResponse.

        重新加密后的密文

        :param cipher_text: The cipher_text of this ReEncryptResponse.
        :type cipher_text: str
        """
        self._cipher_text = cipher_text

    def to_dict(self):
        import warnings
        warnings.warn("ReEncryptResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ReEncryptResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
