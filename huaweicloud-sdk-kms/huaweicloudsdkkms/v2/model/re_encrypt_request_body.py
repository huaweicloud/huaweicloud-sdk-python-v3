# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReEncryptRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_key_id': 'str',
        'source_additional_authenticated_data': 'str',
        'source_encryption_algorithm': 'str',
        'destination_key_id': 'str',
        'destination_additional_authenticated_data': 'str',
        'destination_encryption_algorithm': 'str',
        'datakey_cipher_length': 'str',
        'cipher_text': 'str'
    }

    attribute_map = {
        'source_key_id': 'source_key_id',
        'source_additional_authenticated_data': 'source_additional_authenticated_data',
        'source_encryption_algorithm': 'source_encryption_algorithm',
        'destination_key_id': 'destination_key_id',
        'destination_additional_authenticated_data': 'destination_additional_authenticated_data',
        'destination_encryption_algorithm': 'destination_encryption_algorithm',
        'datakey_cipher_length': 'datakey_cipher_length',
        'cipher_text': 'cipher_text'
    }

    def __init__(self, source_key_id=None, source_additional_authenticated_data=None, source_encryption_algorithm=None, destination_key_id=None, destination_additional_authenticated_data=None, destination_encryption_algorithm=None, datakey_cipher_length=None, cipher_text=None):
        r"""ReEncryptRequestBody

        The model defined in huaweicloud sdk

        :param source_key_id: 原密钥ID，用于解密密文。对于非对称密钥加密的密文source_key_id必填。对于对称密钥加密的密文，推荐填写source_key_id。kms会优先使用您填写的source_key_id进行解密。不填时会尝试从密文中解析出加密时使用的密钥ID进行解密。
        :type source_key_id: str
        :param source_additional_authenticated_data: 加密原密文时使用的aad信息。如果加密时，没指定aad，则不能填写，否则会造成解密失败
        :type source_additional_authenticated_data: str
        :param source_encryption_algorithm: 加密原密文时使用的加密算法。默认值为“SYMMETRIC_DEFAULT”，合法枚举值如下： SYMMETRIC_DEFAULT RSAES_OAEP_SHA_1 RSAES_OAEP_SHA_256 SM2_ENCRYPT 注意：RSAES_OAEP_SHA_1已不再安全，请谨慎使用
        :type source_encryption_algorithm: str
        :param destination_key_id: 目的密钥ID,用于加密解密后的明文
        :type destination_key_id: str
        :param destination_additional_authenticated_data: 如果指定了值，会在重加密时，作为aad参与计算
        :type destination_additional_authenticated_data: str
        :param destination_encryption_algorithm: 重加密新密文时使用的加密算法。默认值为“SYMMETRIC_DEFAULT”，合法枚举值如下： SYMMETRIC_DEFAULT RSAES_OAEP_SHA_1 RSAES_OAEP_SHA_256 SM2_ENCRYPT 注意：RSAES_OAEP_SHA_1已不再安全，请谨慎使用
        :type destination_encryption_algorithm: str
        :param datakey_cipher_length: 当密文是CBC 模式加密的 数据密钥时，需要指定datakey_cipher_length。表示明文密钥材料的字节数
        :type datakey_cipher_length: str
        :param cipher_text: 需要进行重加密的密文。
        :type cipher_text: str
        """
        
        

        self._source_key_id = None
        self._source_additional_authenticated_data = None
        self._source_encryption_algorithm = None
        self._destination_key_id = None
        self._destination_additional_authenticated_data = None
        self._destination_encryption_algorithm = None
        self._datakey_cipher_length = None
        self._cipher_text = None
        self.discriminator = None

        if source_key_id is not None:
            self.source_key_id = source_key_id
        if source_additional_authenticated_data is not None:
            self.source_additional_authenticated_data = source_additional_authenticated_data
        if source_encryption_algorithm is not None:
            self.source_encryption_algorithm = source_encryption_algorithm
        self.destination_key_id = destination_key_id
        if destination_additional_authenticated_data is not None:
            self.destination_additional_authenticated_data = destination_additional_authenticated_data
        if destination_encryption_algorithm is not None:
            self.destination_encryption_algorithm = destination_encryption_algorithm
        if datakey_cipher_length is not None:
            self.datakey_cipher_length = datakey_cipher_length
        self.cipher_text = cipher_text

    @property
    def source_key_id(self):
        r"""Gets the source_key_id of this ReEncryptRequestBody.

        原密钥ID，用于解密密文。对于非对称密钥加密的密文source_key_id必填。对于对称密钥加密的密文，推荐填写source_key_id。kms会优先使用您填写的source_key_id进行解密。不填时会尝试从密文中解析出加密时使用的密钥ID进行解密。

        :return: The source_key_id of this ReEncryptRequestBody.
        :rtype: str
        """
        return self._source_key_id

    @source_key_id.setter
    def source_key_id(self, source_key_id):
        r"""Sets the source_key_id of this ReEncryptRequestBody.

        原密钥ID，用于解密密文。对于非对称密钥加密的密文source_key_id必填。对于对称密钥加密的密文，推荐填写source_key_id。kms会优先使用您填写的source_key_id进行解密。不填时会尝试从密文中解析出加密时使用的密钥ID进行解密。

        :param source_key_id: The source_key_id of this ReEncryptRequestBody.
        :type source_key_id: str
        """
        self._source_key_id = source_key_id

    @property
    def source_additional_authenticated_data(self):
        r"""Gets the source_additional_authenticated_data of this ReEncryptRequestBody.

        加密原密文时使用的aad信息。如果加密时，没指定aad，则不能填写，否则会造成解密失败

        :return: The source_additional_authenticated_data of this ReEncryptRequestBody.
        :rtype: str
        """
        return self._source_additional_authenticated_data

    @source_additional_authenticated_data.setter
    def source_additional_authenticated_data(self, source_additional_authenticated_data):
        r"""Sets the source_additional_authenticated_data of this ReEncryptRequestBody.

        加密原密文时使用的aad信息。如果加密时，没指定aad，则不能填写，否则会造成解密失败

        :param source_additional_authenticated_data: The source_additional_authenticated_data of this ReEncryptRequestBody.
        :type source_additional_authenticated_data: str
        """
        self._source_additional_authenticated_data = source_additional_authenticated_data

    @property
    def source_encryption_algorithm(self):
        r"""Gets the source_encryption_algorithm of this ReEncryptRequestBody.

        加密原密文时使用的加密算法。默认值为“SYMMETRIC_DEFAULT”，合法枚举值如下： SYMMETRIC_DEFAULT RSAES_OAEP_SHA_1 RSAES_OAEP_SHA_256 SM2_ENCRYPT 注意：RSAES_OAEP_SHA_1已不再安全，请谨慎使用

        :return: The source_encryption_algorithm of this ReEncryptRequestBody.
        :rtype: str
        """
        return self._source_encryption_algorithm

    @source_encryption_algorithm.setter
    def source_encryption_algorithm(self, source_encryption_algorithm):
        r"""Sets the source_encryption_algorithm of this ReEncryptRequestBody.

        加密原密文时使用的加密算法。默认值为“SYMMETRIC_DEFAULT”，合法枚举值如下： SYMMETRIC_DEFAULT RSAES_OAEP_SHA_1 RSAES_OAEP_SHA_256 SM2_ENCRYPT 注意：RSAES_OAEP_SHA_1已不再安全，请谨慎使用

        :param source_encryption_algorithm: The source_encryption_algorithm of this ReEncryptRequestBody.
        :type source_encryption_algorithm: str
        """
        self._source_encryption_algorithm = source_encryption_algorithm

    @property
    def destination_key_id(self):
        r"""Gets the destination_key_id of this ReEncryptRequestBody.

        目的密钥ID,用于加密解密后的明文

        :return: The destination_key_id of this ReEncryptRequestBody.
        :rtype: str
        """
        return self._destination_key_id

    @destination_key_id.setter
    def destination_key_id(self, destination_key_id):
        r"""Sets the destination_key_id of this ReEncryptRequestBody.

        目的密钥ID,用于加密解密后的明文

        :param destination_key_id: The destination_key_id of this ReEncryptRequestBody.
        :type destination_key_id: str
        """
        self._destination_key_id = destination_key_id

    @property
    def destination_additional_authenticated_data(self):
        r"""Gets the destination_additional_authenticated_data of this ReEncryptRequestBody.

        如果指定了值，会在重加密时，作为aad参与计算

        :return: The destination_additional_authenticated_data of this ReEncryptRequestBody.
        :rtype: str
        """
        return self._destination_additional_authenticated_data

    @destination_additional_authenticated_data.setter
    def destination_additional_authenticated_data(self, destination_additional_authenticated_data):
        r"""Sets the destination_additional_authenticated_data of this ReEncryptRequestBody.

        如果指定了值，会在重加密时，作为aad参与计算

        :param destination_additional_authenticated_data: The destination_additional_authenticated_data of this ReEncryptRequestBody.
        :type destination_additional_authenticated_data: str
        """
        self._destination_additional_authenticated_data = destination_additional_authenticated_data

    @property
    def destination_encryption_algorithm(self):
        r"""Gets the destination_encryption_algorithm of this ReEncryptRequestBody.

        重加密新密文时使用的加密算法。默认值为“SYMMETRIC_DEFAULT”，合法枚举值如下： SYMMETRIC_DEFAULT RSAES_OAEP_SHA_1 RSAES_OAEP_SHA_256 SM2_ENCRYPT 注意：RSAES_OAEP_SHA_1已不再安全，请谨慎使用

        :return: The destination_encryption_algorithm of this ReEncryptRequestBody.
        :rtype: str
        """
        return self._destination_encryption_algorithm

    @destination_encryption_algorithm.setter
    def destination_encryption_algorithm(self, destination_encryption_algorithm):
        r"""Sets the destination_encryption_algorithm of this ReEncryptRequestBody.

        重加密新密文时使用的加密算法。默认值为“SYMMETRIC_DEFAULT”，合法枚举值如下： SYMMETRIC_DEFAULT RSAES_OAEP_SHA_1 RSAES_OAEP_SHA_256 SM2_ENCRYPT 注意：RSAES_OAEP_SHA_1已不再安全，请谨慎使用

        :param destination_encryption_algorithm: The destination_encryption_algorithm of this ReEncryptRequestBody.
        :type destination_encryption_algorithm: str
        """
        self._destination_encryption_algorithm = destination_encryption_algorithm

    @property
    def datakey_cipher_length(self):
        r"""Gets the datakey_cipher_length of this ReEncryptRequestBody.

        当密文是CBC 模式加密的 数据密钥时，需要指定datakey_cipher_length。表示明文密钥材料的字节数

        :return: The datakey_cipher_length of this ReEncryptRequestBody.
        :rtype: str
        """
        return self._datakey_cipher_length

    @datakey_cipher_length.setter
    def datakey_cipher_length(self, datakey_cipher_length):
        r"""Sets the datakey_cipher_length of this ReEncryptRequestBody.

        当密文是CBC 模式加密的 数据密钥时，需要指定datakey_cipher_length。表示明文密钥材料的字节数

        :param datakey_cipher_length: The datakey_cipher_length of this ReEncryptRequestBody.
        :type datakey_cipher_length: str
        """
        self._datakey_cipher_length = datakey_cipher_length

    @property
    def cipher_text(self):
        r"""Gets the cipher_text of this ReEncryptRequestBody.

        需要进行重加密的密文。

        :return: The cipher_text of this ReEncryptRequestBody.
        :rtype: str
        """
        return self._cipher_text

    @cipher_text.setter
    def cipher_text(self, cipher_text):
        r"""Sets the cipher_text of this ReEncryptRequestBody.

        需要进行重加密的密文。

        :param cipher_text: The cipher_text of this ReEncryptRequestBody.
        :type cipher_text: str
        """
        self._cipher_text = cipher_text

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
        if not isinstance(other, ReEncryptRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
