# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DecryptDataRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cipher_text': 'str',
        'encryption_algorithm': 'str',
        'key_id': 'str',
        'sequence': 'str'
    }

    attribute_map = {
        'cipher_text': 'cipher_text',
        'encryption_algorithm': 'encryption_algorithm',
        'key_id': 'key_id',
        'sequence': 'sequence'
    }

    def __init__(self, cipher_text=None, encryption_algorithm=None, key_id=None, sequence=None):
        """DecryptDataRequestBody

        The model defined in huaweicloud sdk

        :param cipher_text: 被加密数据密文。取值为加密数据结果中的cipher_text的值，满足正则匹配“^[0-9a-zA-Z+/&#x3D;]{128,5648}$”。
        :type cipher_text: str
        :param encryption_algorithm: 数据加密算法，仅使用非对称密钥需要指定该参数，默认值为“SYMMETRIC_DEFAULT”，合法枚举值如下：  - SYMMETRIC_DEFAULT  - RSAES_OAEP_SHA_256  - SM2_ENCRYPT
        :type encryption_algorithm: str
        :param key_id: 密钥ID，36字节，满足正则匹配“^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$”。仅当密文使用非对称密钥加密时才需要此参数。 例如：0d0466b0-e727-4d9c-b35d-f84bb474a37f。
        :type key_id: str
        :param sequence: 请求消息序列号，36字节序列号。 例如：919c82d4-8046-4722-9094-35c3c6524cff
        :type sequence: str
        """
        
        

        self._cipher_text = None
        self._encryption_algorithm = None
        self._key_id = None
        self._sequence = None
        self.discriminator = None

        self.cipher_text = cipher_text
        if encryption_algorithm is not None:
            self.encryption_algorithm = encryption_algorithm
        if key_id is not None:
            self.key_id = key_id
        if sequence is not None:
            self.sequence = sequence

    @property
    def cipher_text(self):
        """Gets the cipher_text of this DecryptDataRequestBody.

        被加密数据密文。取值为加密数据结果中的cipher_text的值，满足正则匹配“^[0-9a-zA-Z+/=]{128,5648}$”。

        :return: The cipher_text of this DecryptDataRequestBody.
        :rtype: str
        """
        return self._cipher_text

    @cipher_text.setter
    def cipher_text(self, cipher_text):
        """Sets the cipher_text of this DecryptDataRequestBody.

        被加密数据密文。取值为加密数据结果中的cipher_text的值，满足正则匹配“^[0-9a-zA-Z+/=]{128,5648}$”。

        :param cipher_text: The cipher_text of this DecryptDataRequestBody.
        :type cipher_text: str
        """
        self._cipher_text = cipher_text

    @property
    def encryption_algorithm(self):
        """Gets the encryption_algorithm of this DecryptDataRequestBody.

        数据加密算法，仅使用非对称密钥需要指定该参数，默认值为“SYMMETRIC_DEFAULT”，合法枚举值如下：  - SYMMETRIC_DEFAULT  - RSAES_OAEP_SHA_256  - SM2_ENCRYPT

        :return: The encryption_algorithm of this DecryptDataRequestBody.
        :rtype: str
        """
        return self._encryption_algorithm

    @encryption_algorithm.setter
    def encryption_algorithm(self, encryption_algorithm):
        """Sets the encryption_algorithm of this DecryptDataRequestBody.

        数据加密算法，仅使用非对称密钥需要指定该参数，默认值为“SYMMETRIC_DEFAULT”，合法枚举值如下：  - SYMMETRIC_DEFAULT  - RSAES_OAEP_SHA_256  - SM2_ENCRYPT

        :param encryption_algorithm: The encryption_algorithm of this DecryptDataRequestBody.
        :type encryption_algorithm: str
        """
        self._encryption_algorithm = encryption_algorithm

    @property
    def key_id(self):
        """Gets the key_id of this DecryptDataRequestBody.

        密钥ID，36字节，满足正则匹配“^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$”。仅当密文使用非对称密钥加密时才需要此参数。 例如：0d0466b0-e727-4d9c-b35d-f84bb474a37f。

        :return: The key_id of this DecryptDataRequestBody.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """Sets the key_id of this DecryptDataRequestBody.

        密钥ID，36字节，满足正则匹配“^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$”。仅当密文使用非对称密钥加密时才需要此参数。 例如：0d0466b0-e727-4d9c-b35d-f84bb474a37f。

        :param key_id: The key_id of this DecryptDataRequestBody.
        :type key_id: str
        """
        self._key_id = key_id

    @property
    def sequence(self):
        """Gets the sequence of this DecryptDataRequestBody.

        请求消息序列号，36字节序列号。 例如：919c82d4-8046-4722-9094-35c3c6524cff

        :return: The sequence of this DecryptDataRequestBody.
        :rtype: str
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """Sets the sequence of this DecryptDataRequestBody.

        请求消息序列号，36字节序列号。 例如：919c82d4-8046-4722-9094-35c3c6524cff

        :param sequence: The sequence of this DecryptDataRequestBody.
        :type sequence: str
        """
        self._sequence = sequence

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
        if not isinstance(other, DecryptDataRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
