# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SignRequestBody:

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
        'message': 'str',
        'signing_algorithm': 'str',
        'message_type': 'str',
        'sequence': 'str'
    }

    attribute_map = {
        'key_id': 'key_id',
        'message': 'message',
        'signing_algorithm': 'signing_algorithm',
        'message_type': 'message_type',
        'sequence': 'sequence'
    }

    def __init__(self, key_id=None, message=None, signing_algorithm=None, message_type=None, sequence=None):
        """SignRequestBody

        The model defined in huaweicloud sdk

        :param key_id: 密钥ID，36字节，满足正则匹配“^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$”。 例如：0d0466b0-e727-4d9c-b35d-f84bb474a37f。
        :type key_id: str
        :param message: 待签名的消息摘要或者消息，消息长度要求小于4096字节，使用Base64编码。
        :type message: str
        :param signing_algorithm: 签名算法，枚举如下：  - RSASSA_PSS_SHA_256  - RSASSA_PSS_SHA_384  - RSASSA_PSS_SHA_512  - RSASSA_PKCS1_V1_5_SHA_256  - RSASSA_PKCS1_V1_5_SHA_384  - RSASSA_PKCS1_V1_5_SHA_512  - ECDSA_SHA_256  - ECDSA_SHA_384  - ECDSA_SHA_512  - SM2DSA_SM3
        :type signing_algorithm: str
        :param message_type: 消息类型，默认为“DIGEST”，枚举如下：  - DIGEST 表示消息摘要  - RAW 表示消息原文
        :type message_type: str
        :param sequence: 请求消息序列号，36字节序列号。 例如：919c82d4-8046-4722-9094-35c3c6524cff。
        :type sequence: str
        """
        
        

        self._key_id = None
        self._message = None
        self._signing_algorithm = None
        self._message_type = None
        self._sequence = None
        self.discriminator = None

        self.key_id = key_id
        self.message = message
        self.signing_algorithm = signing_algorithm
        if message_type is not None:
            self.message_type = message_type
        if sequence is not None:
            self.sequence = sequence

    @property
    def key_id(self):
        """Gets the key_id of this SignRequestBody.

        密钥ID，36字节，满足正则匹配“^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$”。 例如：0d0466b0-e727-4d9c-b35d-f84bb474a37f。

        :return: The key_id of this SignRequestBody.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """Sets the key_id of this SignRequestBody.

        密钥ID，36字节，满足正则匹配“^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$”。 例如：0d0466b0-e727-4d9c-b35d-f84bb474a37f。

        :param key_id: The key_id of this SignRequestBody.
        :type key_id: str
        """
        self._key_id = key_id

    @property
    def message(self):
        """Gets the message of this SignRequestBody.

        待签名的消息摘要或者消息，消息长度要求小于4096字节，使用Base64编码。

        :return: The message of this SignRequestBody.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this SignRequestBody.

        待签名的消息摘要或者消息，消息长度要求小于4096字节，使用Base64编码。

        :param message: The message of this SignRequestBody.
        :type message: str
        """
        self._message = message

    @property
    def signing_algorithm(self):
        """Gets the signing_algorithm of this SignRequestBody.

        签名算法，枚举如下：  - RSASSA_PSS_SHA_256  - RSASSA_PSS_SHA_384  - RSASSA_PSS_SHA_512  - RSASSA_PKCS1_V1_5_SHA_256  - RSASSA_PKCS1_V1_5_SHA_384  - RSASSA_PKCS1_V1_5_SHA_512  - ECDSA_SHA_256  - ECDSA_SHA_384  - ECDSA_SHA_512  - SM2DSA_SM3

        :return: The signing_algorithm of this SignRequestBody.
        :rtype: str
        """
        return self._signing_algorithm

    @signing_algorithm.setter
    def signing_algorithm(self, signing_algorithm):
        """Sets the signing_algorithm of this SignRequestBody.

        签名算法，枚举如下：  - RSASSA_PSS_SHA_256  - RSASSA_PSS_SHA_384  - RSASSA_PSS_SHA_512  - RSASSA_PKCS1_V1_5_SHA_256  - RSASSA_PKCS1_V1_5_SHA_384  - RSASSA_PKCS1_V1_5_SHA_512  - ECDSA_SHA_256  - ECDSA_SHA_384  - ECDSA_SHA_512  - SM2DSA_SM3

        :param signing_algorithm: The signing_algorithm of this SignRequestBody.
        :type signing_algorithm: str
        """
        self._signing_algorithm = signing_algorithm

    @property
    def message_type(self):
        """Gets the message_type of this SignRequestBody.

        消息类型，默认为“DIGEST”，枚举如下：  - DIGEST 表示消息摘要  - RAW 表示消息原文

        :return: The message_type of this SignRequestBody.
        :rtype: str
        """
        return self._message_type

    @message_type.setter
    def message_type(self, message_type):
        """Sets the message_type of this SignRequestBody.

        消息类型，默认为“DIGEST”，枚举如下：  - DIGEST 表示消息摘要  - RAW 表示消息原文

        :param message_type: The message_type of this SignRequestBody.
        :type message_type: str
        """
        self._message_type = message_type

    @property
    def sequence(self):
        """Gets the sequence of this SignRequestBody.

        请求消息序列号，36字节序列号。 例如：919c82d4-8046-4722-9094-35c3c6524cff。

        :return: The sequence of this SignRequestBody.
        :rtype: str
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """Sets the sequence of this SignRequestBody.

        请求消息序列号，36字节序列号。 例如：919c82d4-8046-4722-9094-35c3c6524cff。

        :param sequence: The sequence of this SignRequestBody.
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
        if not isinstance(other, SignRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
