# coding: utf-8

import pprint
import re

import six





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
        'encryption_context': 'object',
        'sequence': 'str'
    }

    attribute_map = {
        'cipher_text': 'cipher_text',
        'encryption_context': 'encryption_context',
        'sequence': 'sequence'
    }

    def __init__(self, cipher_text=None, encryption_context=None, sequence=None):
        """DecryptDataRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._cipher_text = None
        self._encryption_context = None
        self._sequence = None
        self.discriminator = None

        if cipher_text is not None:
            self.cipher_text = cipher_text
        if encryption_context is not None:
            self.encryption_context = encryption_context
        if sequence is not None:
            self.sequence = sequence

    @property
    def cipher_text(self):
        """Gets the cipher_text of this DecryptDataRequestBody.

        被加密数据密文。取值为加密数据结果中的cipher_text的值，满足正则匹配“^[0-9a-zA-Z+/=]{188,5648}$”。

        :return: The cipher_text of this DecryptDataRequestBody.
        :rtype: str
        """
        return self._cipher_text

    @cipher_text.setter
    def cipher_text(self, cipher_text):
        """Sets the cipher_text of this DecryptDataRequestBody.

        被加密数据密文。取值为加密数据结果中的cipher_text的值，满足正则匹配“^[0-9a-zA-Z+/=]{188,5648}$”。

        :param cipher_text: The cipher_text of this DecryptDataRequestBody.
        :type: str
        """
        self._cipher_text = cipher_text

    @property
    def encryption_context(self):
        """Gets the encryption_context of this DecryptDataRequestBody.

        一系列key-value键值对，用于记录资源上下文信息，用于保护数据的完整性，不应包含敏感信息，最大长度为8192。 当在加密时指定了该参数时，解密密文时，需要传入相同的参数，才能正确的解密。 例如：{\"Key1\":\"Value1\",\"Key2\":\"Value2\"}

        :return: The encryption_context of this DecryptDataRequestBody.
        :rtype: object
        """
        return self._encryption_context

    @encryption_context.setter
    def encryption_context(self, encryption_context):
        """Sets the encryption_context of this DecryptDataRequestBody.

        一系列key-value键值对，用于记录资源上下文信息，用于保护数据的完整性，不应包含敏感信息，最大长度为8192。 当在加密时指定了该参数时，解密密文时，需要传入相同的参数，才能正确的解密。 例如：{\"Key1\":\"Value1\",\"Key2\":\"Value2\"}

        :param encryption_context: The encryption_context of this DecryptDataRequestBody.
        :type: object
        """
        self._encryption_context = encryption_context

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
        :type: str
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DecryptDataRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
