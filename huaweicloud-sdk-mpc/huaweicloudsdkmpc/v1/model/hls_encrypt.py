# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HlsEncrypt:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'url': 'str',
        'iv': 'str',
        'algorithm': 'str'
    }

    attribute_map = {
        'key': 'key',
        'url': 'url',
        'iv': 'iv',
        'algorithm': 'algorithm'
    }

    def __init__(self, key=None, url=None, iv=None, algorithm=None):
        """HlsEncrypt

        The model defined in huaweicloud sdk

        :param key: 内容加密秘钥 
        :type key: str
        :param url: 秘钥获取服务的地址 
        :type url: str
        :param iv: 初始向量，base64binary，随机数 
        :type iv: str
        :param algorithm: 加密算法。 - AES-128-CTR - AES-128-CBC - SM4CBC  默认值：AES-128-CTR 
        :type algorithm: str
        """
        
        

        self._key = None
        self._url = None
        self._iv = None
        self._algorithm = None
        self.discriminator = None

        self.key = key
        self.url = url
        if iv is not None:
            self.iv = iv
        if algorithm is not None:
            self.algorithm = algorithm

    @property
    def key(self):
        """Gets the key of this HlsEncrypt.

        内容加密秘钥 

        :return: The key of this HlsEncrypt.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this HlsEncrypt.

        内容加密秘钥 

        :param key: The key of this HlsEncrypt.
        :type key: str
        """
        self._key = key

    @property
    def url(self):
        """Gets the url of this HlsEncrypt.

        秘钥获取服务的地址 

        :return: The url of this HlsEncrypt.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this HlsEncrypt.

        秘钥获取服务的地址 

        :param url: The url of this HlsEncrypt.
        :type url: str
        """
        self._url = url

    @property
    def iv(self):
        """Gets the iv of this HlsEncrypt.

        初始向量，base64binary，随机数 

        :return: The iv of this HlsEncrypt.
        :rtype: str
        """
        return self._iv

    @iv.setter
    def iv(self, iv):
        """Sets the iv of this HlsEncrypt.

        初始向量，base64binary，随机数 

        :param iv: The iv of this HlsEncrypt.
        :type iv: str
        """
        self._iv = iv

    @property
    def algorithm(self):
        """Gets the algorithm of this HlsEncrypt.

        加密算法。 - AES-128-CTR - AES-128-CBC - SM4CBC  默认值：AES-128-CTR 

        :return: The algorithm of this HlsEncrypt.
        :rtype: str
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        """Sets the algorithm of this HlsEncrypt.

        加密算法。 - AES-128-CTR - AES-128-CBC - SM4CBC  默认值：AES-128-CTR 

        :param algorithm: The algorithm of this HlsEncrypt.
        :type algorithm: str
        """
        self._algorithm = algorithm

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
        if not isinstance(other, HlsEncrypt):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
