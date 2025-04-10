# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DecryptDataResponse(SdkResponse):

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
        'plain_text_base64': 'str'
    }

    attribute_map = {
        'key_id': 'key_id',
        'plain_text': 'plain_text',
        'plain_text_base64': 'plain_text_base64'
    }

    def __init__(self, key_id=None, plain_text=None, plain_text_base64=None):
        r"""DecryptDataResponse

        The model defined in huaweicloud sdk

        :param key_id: 密钥ID。
        :type key_id: str
        :param plain_text: 明文。
        :type plain_text: str
        :param plain_text_base64: 明文的Base64值，在非对称加密场景下，若加密的明文中含有不可见字符，则解密结果以该值为准。
        :type plain_text_base64: str
        """
        
        super(DecryptDataResponse, self).__init__()

        self._key_id = None
        self._plain_text = None
        self._plain_text_base64 = None
        self.discriminator = None

        if key_id is not None:
            self.key_id = key_id
        if plain_text is not None:
            self.plain_text = plain_text
        if plain_text_base64 is not None:
            self.plain_text_base64 = plain_text_base64

    @property
    def key_id(self):
        r"""Gets the key_id of this DecryptDataResponse.

        密钥ID。

        :return: The key_id of this DecryptDataResponse.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        r"""Sets the key_id of this DecryptDataResponse.

        密钥ID。

        :param key_id: The key_id of this DecryptDataResponse.
        :type key_id: str
        """
        self._key_id = key_id

    @property
    def plain_text(self):
        r"""Gets the plain_text of this DecryptDataResponse.

        明文。

        :return: The plain_text of this DecryptDataResponse.
        :rtype: str
        """
        return self._plain_text

    @plain_text.setter
    def plain_text(self, plain_text):
        r"""Sets the plain_text of this DecryptDataResponse.

        明文。

        :param plain_text: The plain_text of this DecryptDataResponse.
        :type plain_text: str
        """
        self._plain_text = plain_text

    @property
    def plain_text_base64(self):
        r"""Gets the plain_text_base64 of this DecryptDataResponse.

        明文的Base64值，在非对称加密场景下，若加密的明文中含有不可见字符，则解密结果以该值为准。

        :return: The plain_text_base64 of this DecryptDataResponse.
        :rtype: str
        """
        return self._plain_text_base64

    @plain_text_base64.setter
    def plain_text_base64(self, plain_text_base64):
        r"""Sets the plain_text_base64 of this DecryptDataResponse.

        明文的Base64值，在非对称加密场景下，若加密的明文中含有不可见字符，则解密结果以该值为准。

        :param plain_text_base64: The plain_text_base64 of this DecryptDataResponse.
        :type plain_text_base64: str
        """
        self._plain_text_base64 = plain_text_base64

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
        if not isinstance(other, DecryptDataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
