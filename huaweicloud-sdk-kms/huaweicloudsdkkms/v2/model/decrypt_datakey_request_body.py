# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DecryptDatakeyRequestBody:

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
        'cipher_text': 'str',
        'datakey_cipher_length': 'str',
        'sequence': 'str'
    }

    attribute_map = {
        'key_id': 'key_id',
        'cipher_text': 'cipher_text',
        'datakey_cipher_length': 'datakey_cipher_length',
        'sequence': 'sequence'
    }

    def __init__(self, key_id=None, cipher_text=None, datakey_cipher_length=None, sequence=None):
        """DecryptDatakeyRequestBody

        The model defined in huaweicloud sdk

        :param key_id: 密钥ID，36字节，满足正则匹配“^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$”。 例如：0d0466b0-e727-4d9c-b35d-f84bb474a37f。
        :type key_id: str
        :param cipher_text: DEK密文及元数据的16进制字符串。取值为加密数据密钥结果中的cipher_text的值。
        :type cipher_text: str
        :param datakey_cipher_length: 密钥字节长度，取值范围为1~1024。 密钥字节长度，取值为“64”。
        :type datakey_cipher_length: str
        :param sequence: 请求消息序列号，36字节序列号。 例如：919c82d4-8046-4722-9094-35c3c6524cff
        :type sequence: str
        """
        
        

        self._key_id = None
        self._cipher_text = None
        self._datakey_cipher_length = None
        self._sequence = None
        self.discriminator = None

        self.key_id = key_id
        self.cipher_text = cipher_text
        self.datakey_cipher_length = datakey_cipher_length
        if sequence is not None:
            self.sequence = sequence

    @property
    def key_id(self):
        """Gets the key_id of this DecryptDatakeyRequestBody.

        密钥ID，36字节，满足正则匹配“^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$”。 例如：0d0466b0-e727-4d9c-b35d-f84bb474a37f。

        :return: The key_id of this DecryptDatakeyRequestBody.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """Sets the key_id of this DecryptDatakeyRequestBody.

        密钥ID，36字节，满足正则匹配“^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$”。 例如：0d0466b0-e727-4d9c-b35d-f84bb474a37f。

        :param key_id: The key_id of this DecryptDatakeyRequestBody.
        :type key_id: str
        """
        self._key_id = key_id

    @property
    def cipher_text(self):
        """Gets the cipher_text of this DecryptDatakeyRequestBody.

        DEK密文及元数据的16进制字符串。取值为加密数据密钥结果中的cipher_text的值。

        :return: The cipher_text of this DecryptDatakeyRequestBody.
        :rtype: str
        """
        return self._cipher_text

    @cipher_text.setter
    def cipher_text(self, cipher_text):
        """Sets the cipher_text of this DecryptDatakeyRequestBody.

        DEK密文及元数据的16进制字符串。取值为加密数据密钥结果中的cipher_text的值。

        :param cipher_text: The cipher_text of this DecryptDatakeyRequestBody.
        :type cipher_text: str
        """
        self._cipher_text = cipher_text

    @property
    def datakey_cipher_length(self):
        """Gets the datakey_cipher_length of this DecryptDatakeyRequestBody.

        密钥字节长度，取值范围为1~1024。 密钥字节长度，取值为“64”。

        :return: The datakey_cipher_length of this DecryptDatakeyRequestBody.
        :rtype: str
        """
        return self._datakey_cipher_length

    @datakey_cipher_length.setter
    def datakey_cipher_length(self, datakey_cipher_length):
        """Sets the datakey_cipher_length of this DecryptDatakeyRequestBody.

        密钥字节长度，取值范围为1~1024。 密钥字节长度，取值为“64”。

        :param datakey_cipher_length: The datakey_cipher_length of this DecryptDatakeyRequestBody.
        :type datakey_cipher_length: str
        """
        self._datakey_cipher_length = datakey_cipher_length

    @property
    def sequence(self):
        """Gets the sequence of this DecryptDatakeyRequestBody.

        请求消息序列号，36字节序列号。 例如：919c82d4-8046-4722-9094-35c3c6524cff

        :return: The sequence of this DecryptDatakeyRequestBody.
        :rtype: str
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """Sets the sequence of this DecryptDatakeyRequestBody.

        请求消息序列号，36字节序列号。 例如：919c82d4-8046-4722-9094-35c3c6524cff

        :param sequence: The sequence of this DecryptDatakeyRequestBody.
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
        if not isinstance(other, DecryptDatakeyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
