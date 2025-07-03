# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlowSourceDecryption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'algorithm': 'str',
        'key_type': 'str',
        'passphrase': 'str'
    }

    attribute_map = {
        'algorithm': 'algorithm',
        'key_type': 'key_type',
        'passphrase': 'passphrase'
    }

    def __init__(self, algorithm=None, key_type=None, passphrase=None):
        r"""FlowSourceDecryption

        The model defined in huaweicloud sdk

        :param algorithm: 加密算法，aes128: 加密算法为aes-128，aes192:加密算法为aes-192，aes256: 加密算法为AES-256
        :type algorithm: str
        :param key_type: 秘钥类型,speke:使用speke协议获取秘钥,static-key:静态秘钥,srt-password:SRT协议秘钥 目前仅支持srt-password类型，其他类型暂不支持
        :type key_type: str
        :param passphrase: srt解密秘钥，用于flow对srt流进行解密
        :type passphrase: str
        """
        
        

        self._algorithm = None
        self._key_type = None
        self._passphrase = None
        self.discriminator = None

        if algorithm is not None:
            self.algorithm = algorithm
        self.key_type = key_type
        self.passphrase = passphrase

    @property
    def algorithm(self):
        r"""Gets the algorithm of this FlowSourceDecryption.

        加密算法，aes128: 加密算法为aes-128，aes192:加密算法为aes-192，aes256: 加密算法为AES-256

        :return: The algorithm of this FlowSourceDecryption.
        :rtype: str
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        r"""Sets the algorithm of this FlowSourceDecryption.

        加密算法，aes128: 加密算法为aes-128，aes192:加密算法为aes-192，aes256: 加密算法为AES-256

        :param algorithm: The algorithm of this FlowSourceDecryption.
        :type algorithm: str
        """
        self._algorithm = algorithm

    @property
    def key_type(self):
        r"""Gets the key_type of this FlowSourceDecryption.

        秘钥类型,speke:使用speke协议获取秘钥,static-key:静态秘钥,srt-password:SRT协议秘钥 目前仅支持srt-password类型，其他类型暂不支持

        :return: The key_type of this FlowSourceDecryption.
        :rtype: str
        """
        return self._key_type

    @key_type.setter
    def key_type(self, key_type):
        r"""Sets the key_type of this FlowSourceDecryption.

        秘钥类型,speke:使用speke协议获取秘钥,static-key:静态秘钥,srt-password:SRT协议秘钥 目前仅支持srt-password类型，其他类型暂不支持

        :param key_type: The key_type of this FlowSourceDecryption.
        :type key_type: str
        """
        self._key_type = key_type

    @property
    def passphrase(self):
        r"""Gets the passphrase of this FlowSourceDecryption.

        srt解密秘钥，用于flow对srt流进行解密

        :return: The passphrase of this FlowSourceDecryption.
        :rtype: str
        """
        return self._passphrase

    @passphrase.setter
    def passphrase(self, passphrase):
        r"""Sets the passphrase of this FlowSourceDecryption.

        srt解密秘钥，用于flow对srt流进行解密

        :param passphrase: The passphrase of this FlowSourceDecryption.
        :type passphrase: str
        """
        self._passphrase = passphrase

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
        if not isinstance(other, FlowSourceDecryption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
