# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EncryptDatakeyRequestBody:

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
        'plain_text': 'str',
        'datakey_plain_length': 'str',
        'additional_authenticated_data': 'str',
        'sequence': 'str'
    }

    attribute_map = {
        'key_id': 'key_id',
        'plain_text': 'plain_text',
        'datakey_plain_length': 'datakey_plain_length',
        'additional_authenticated_data': 'additional_authenticated_data',
        'sequence': 'sequence'
    }

    def __init__(self, key_id=None, plain_text=None, datakey_plain_length=None, additional_authenticated_data=None, sequence=None):
        r"""EncryptDatakeyRequestBody

        The model defined in huaweicloud sdk

        :param key_id: 密钥ID，36字节，满足正则匹配“^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$”。 例如：0d0466b0-e727-4d9c-b35d-f84bb474a37f。
        :type key_id: str
        :param plain_text: CMK为AES时，DEK明文和DEK明文的SHA256（32字节）；CMK为SM4时，DEK明文和DEK明文的SM3（32字节），均为16进制字符串表示。
        :type plain_text: str
        :param datakey_plain_length: DEK明文字节长度，取值范围为1~1024。 DEK明文字节长度，取值为“64”。
        :type datakey_plain_length: str
        :param additional_authenticated_data: 身份验证的非敏感额外数据。任意字符串，长度不超过128字节。
        :type additional_authenticated_data: str
        :param sequence: 请求消息序列号，36字节序列号。 例如：919c82d4-8046-4722-9094-35c3c6524cff
        :type sequence: str
        """
        
        

        self._key_id = None
        self._plain_text = None
        self._datakey_plain_length = None
        self._additional_authenticated_data = None
        self._sequence = None
        self.discriminator = None

        self.key_id = key_id
        self.plain_text = plain_text
        self.datakey_plain_length = datakey_plain_length
        if additional_authenticated_data is not None:
            self.additional_authenticated_data = additional_authenticated_data
        if sequence is not None:
            self.sequence = sequence

    @property
    def key_id(self):
        r"""Gets the key_id of this EncryptDatakeyRequestBody.

        密钥ID，36字节，满足正则匹配“^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$”。 例如：0d0466b0-e727-4d9c-b35d-f84bb474a37f。

        :return: The key_id of this EncryptDatakeyRequestBody.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        r"""Sets the key_id of this EncryptDatakeyRequestBody.

        密钥ID，36字节，满足正则匹配“^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$”。 例如：0d0466b0-e727-4d9c-b35d-f84bb474a37f。

        :param key_id: The key_id of this EncryptDatakeyRequestBody.
        :type key_id: str
        """
        self._key_id = key_id

    @property
    def plain_text(self):
        r"""Gets the plain_text of this EncryptDatakeyRequestBody.

        CMK为AES时，DEK明文和DEK明文的SHA256（32字节）；CMK为SM4时，DEK明文和DEK明文的SM3（32字节），均为16进制字符串表示。

        :return: The plain_text of this EncryptDatakeyRequestBody.
        :rtype: str
        """
        return self._plain_text

    @plain_text.setter
    def plain_text(self, plain_text):
        r"""Sets the plain_text of this EncryptDatakeyRequestBody.

        CMK为AES时，DEK明文和DEK明文的SHA256（32字节）；CMK为SM4时，DEK明文和DEK明文的SM3（32字节），均为16进制字符串表示。

        :param plain_text: The plain_text of this EncryptDatakeyRequestBody.
        :type plain_text: str
        """
        self._plain_text = plain_text

    @property
    def datakey_plain_length(self):
        r"""Gets the datakey_plain_length of this EncryptDatakeyRequestBody.

        DEK明文字节长度，取值范围为1~1024。 DEK明文字节长度，取值为“64”。

        :return: The datakey_plain_length of this EncryptDatakeyRequestBody.
        :rtype: str
        """
        return self._datakey_plain_length

    @datakey_plain_length.setter
    def datakey_plain_length(self, datakey_plain_length):
        r"""Sets the datakey_plain_length of this EncryptDatakeyRequestBody.

        DEK明文字节长度，取值范围为1~1024。 DEK明文字节长度，取值为“64”。

        :param datakey_plain_length: The datakey_plain_length of this EncryptDatakeyRequestBody.
        :type datakey_plain_length: str
        """
        self._datakey_plain_length = datakey_plain_length

    @property
    def additional_authenticated_data(self):
        r"""Gets the additional_authenticated_data of this EncryptDatakeyRequestBody.

        身份验证的非敏感额外数据。任意字符串，长度不超过128字节。

        :return: The additional_authenticated_data of this EncryptDatakeyRequestBody.
        :rtype: str
        """
        return self._additional_authenticated_data

    @additional_authenticated_data.setter
    def additional_authenticated_data(self, additional_authenticated_data):
        r"""Sets the additional_authenticated_data of this EncryptDatakeyRequestBody.

        身份验证的非敏感额外数据。任意字符串，长度不超过128字节。

        :param additional_authenticated_data: The additional_authenticated_data of this EncryptDatakeyRequestBody.
        :type additional_authenticated_data: str
        """
        self._additional_authenticated_data = additional_authenticated_data

    @property
    def sequence(self):
        r"""Gets the sequence of this EncryptDatakeyRequestBody.

        请求消息序列号，36字节序列号。 例如：919c82d4-8046-4722-9094-35c3c6524cff

        :return: The sequence of this EncryptDatakeyRequestBody.
        :rtype: str
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        r"""Sets the sequence of this EncryptDatakeyRequestBody.

        请求消息序列号，36字节序列号。 例如：919c82d4-8046-4722-9094-35c3c6524cff

        :param sequence: The sequence of this EncryptDatakeyRequestBody.
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
        if not isinstance(other, EncryptDatakeyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
