# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EncryptDatakeyResponse(SdkResponse):

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
        'datakey_length': 'str'
    }

    attribute_map = {
        'key_id': 'key_id',
        'cipher_text': 'cipher_text',
        'datakey_length': 'datakey_length'
    }

    def __init__(self, key_id=None, cipher_text=None, datakey_length=None):
        """EncryptDatakeyResponse

        The model defined in huaweicloud sdk

        :param key_id: 密钥ID
        :type key_id: str
        :param cipher_text: DEK密文16进制，两位表示1byte。
        :type cipher_text: str
        :param datakey_length: DEK字节长度。
        :type datakey_length: str
        """
        
        super(EncryptDatakeyResponse, self).__init__()

        self._key_id = None
        self._cipher_text = None
        self._datakey_length = None
        self.discriminator = None

        if key_id is not None:
            self.key_id = key_id
        if cipher_text is not None:
            self.cipher_text = cipher_text
        if datakey_length is not None:
            self.datakey_length = datakey_length

    @property
    def key_id(self):
        """Gets the key_id of this EncryptDatakeyResponse.

        密钥ID

        :return: The key_id of this EncryptDatakeyResponse.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """Sets the key_id of this EncryptDatakeyResponse.

        密钥ID

        :param key_id: The key_id of this EncryptDatakeyResponse.
        :type key_id: str
        """
        self._key_id = key_id

    @property
    def cipher_text(self):
        """Gets the cipher_text of this EncryptDatakeyResponse.

        DEK密文16进制，两位表示1byte。

        :return: The cipher_text of this EncryptDatakeyResponse.
        :rtype: str
        """
        return self._cipher_text

    @cipher_text.setter
    def cipher_text(self, cipher_text):
        """Sets the cipher_text of this EncryptDatakeyResponse.

        DEK密文16进制，两位表示1byte。

        :param cipher_text: The cipher_text of this EncryptDatakeyResponse.
        :type cipher_text: str
        """
        self._cipher_text = cipher_text

    @property
    def datakey_length(self):
        """Gets the datakey_length of this EncryptDatakeyResponse.

        DEK字节长度。

        :return: The datakey_length of this EncryptDatakeyResponse.
        :rtype: str
        """
        return self._datakey_length

    @datakey_length.setter
    def datakey_length(self, datakey_length):
        """Sets the datakey_length of this EncryptDatakeyResponse.

        DEK字节长度。

        :param datakey_length: The datakey_length of this EncryptDatakeyResponse.
        :type datakey_length: str
        """
        self._datakey_length = datakey_length

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
        if not isinstance(other, EncryptDatakeyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
