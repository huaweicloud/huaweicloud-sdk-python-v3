# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KmsInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'aes_256': 'int',
        'sm4': 'int',
        'rsa_2048': 'int',
        'rsa_3072': 'int',
        'rsa_4096': 'int',
        'ec_p256': 'int',
        'ec_p384': 'int',
        'sm2': 'int'
    }

    attribute_map = {
        'aes_256': 'aes_256',
        'sm4': 'sm4',
        'rsa_2048': 'rsa_2048',
        'rsa_3072': 'rsa_3072',
        'rsa_4096': 'rsa_4096',
        'ec_p256': 'ec_p256',
        'ec_p384': 'ec_p384',
        'sm2': 'sm2'
    }

    def __init__(self, aes_256=None, sm4=None, rsa_2048=None, rsa_3072=None, rsa_4096=None, ec_p256=None, ec_p384=None, sm2=None):
        r"""KmsInfo

        The model defined in huaweicloud sdk

        :param aes_256: AES_256算法密钥数量
        :type aes_256: int
        :param sm4: SM4算法密钥数量
        :type sm4: int
        :param rsa_2048: RSA_2048算法密钥数量
        :type rsa_2048: int
        :param rsa_3072: RSA_3072算法密钥数量
        :type rsa_3072: int
        :param rsa_4096: RSA_4096算法密钥数量
        :type rsa_4096: int
        :param ec_p256: EC_P256算法密钥数量
        :type ec_p256: int
        :param ec_p384: EC_P384务算法密钥数量
        :type ec_p384: int
        :param sm2: SM2算法密钥数量
        :type sm2: int
        """
        
        

        self._aes_256 = None
        self._sm4 = None
        self._rsa_2048 = None
        self._rsa_3072 = None
        self._rsa_4096 = None
        self._ec_p256 = None
        self._ec_p384 = None
        self._sm2 = None
        self.discriminator = None

        if aes_256 is not None:
            self.aes_256 = aes_256
        if sm4 is not None:
            self.sm4 = sm4
        if rsa_2048 is not None:
            self.rsa_2048 = rsa_2048
        if rsa_3072 is not None:
            self.rsa_3072 = rsa_3072
        if rsa_4096 is not None:
            self.rsa_4096 = rsa_4096
        if ec_p256 is not None:
            self.ec_p256 = ec_p256
        if ec_p384 is not None:
            self.ec_p384 = ec_p384
        if sm2 is not None:
            self.sm2 = sm2

    @property
    def aes_256(self):
        r"""Gets the aes_256 of this KmsInfo.

        AES_256算法密钥数量

        :return: The aes_256 of this KmsInfo.
        :rtype: int
        """
        return self._aes_256

    @aes_256.setter
    def aes_256(self, aes_256):
        r"""Sets the aes_256 of this KmsInfo.

        AES_256算法密钥数量

        :param aes_256: The aes_256 of this KmsInfo.
        :type aes_256: int
        """
        self._aes_256 = aes_256

    @property
    def sm4(self):
        r"""Gets the sm4 of this KmsInfo.

        SM4算法密钥数量

        :return: The sm4 of this KmsInfo.
        :rtype: int
        """
        return self._sm4

    @sm4.setter
    def sm4(self, sm4):
        r"""Sets the sm4 of this KmsInfo.

        SM4算法密钥数量

        :param sm4: The sm4 of this KmsInfo.
        :type sm4: int
        """
        self._sm4 = sm4

    @property
    def rsa_2048(self):
        r"""Gets the rsa_2048 of this KmsInfo.

        RSA_2048算法密钥数量

        :return: The rsa_2048 of this KmsInfo.
        :rtype: int
        """
        return self._rsa_2048

    @rsa_2048.setter
    def rsa_2048(self, rsa_2048):
        r"""Sets the rsa_2048 of this KmsInfo.

        RSA_2048算法密钥数量

        :param rsa_2048: The rsa_2048 of this KmsInfo.
        :type rsa_2048: int
        """
        self._rsa_2048 = rsa_2048

    @property
    def rsa_3072(self):
        r"""Gets the rsa_3072 of this KmsInfo.

        RSA_3072算法密钥数量

        :return: The rsa_3072 of this KmsInfo.
        :rtype: int
        """
        return self._rsa_3072

    @rsa_3072.setter
    def rsa_3072(self, rsa_3072):
        r"""Sets the rsa_3072 of this KmsInfo.

        RSA_3072算法密钥数量

        :param rsa_3072: The rsa_3072 of this KmsInfo.
        :type rsa_3072: int
        """
        self._rsa_3072 = rsa_3072

    @property
    def rsa_4096(self):
        r"""Gets the rsa_4096 of this KmsInfo.

        RSA_4096算法密钥数量

        :return: The rsa_4096 of this KmsInfo.
        :rtype: int
        """
        return self._rsa_4096

    @rsa_4096.setter
    def rsa_4096(self, rsa_4096):
        r"""Sets the rsa_4096 of this KmsInfo.

        RSA_4096算法密钥数量

        :param rsa_4096: The rsa_4096 of this KmsInfo.
        :type rsa_4096: int
        """
        self._rsa_4096 = rsa_4096

    @property
    def ec_p256(self):
        r"""Gets the ec_p256 of this KmsInfo.

        EC_P256算法密钥数量

        :return: The ec_p256 of this KmsInfo.
        :rtype: int
        """
        return self._ec_p256

    @ec_p256.setter
    def ec_p256(self, ec_p256):
        r"""Sets the ec_p256 of this KmsInfo.

        EC_P256算法密钥数量

        :param ec_p256: The ec_p256 of this KmsInfo.
        :type ec_p256: int
        """
        self._ec_p256 = ec_p256

    @property
    def ec_p384(self):
        r"""Gets the ec_p384 of this KmsInfo.

        EC_P384务算法密钥数量

        :return: The ec_p384 of this KmsInfo.
        :rtype: int
        """
        return self._ec_p384

    @ec_p384.setter
    def ec_p384(self, ec_p384):
        r"""Sets the ec_p384 of this KmsInfo.

        EC_P384务算法密钥数量

        :param ec_p384: The ec_p384 of this KmsInfo.
        :type ec_p384: int
        """
        self._ec_p384 = ec_p384

    @property
    def sm2(self):
        r"""Gets the sm2 of this KmsInfo.

        SM2算法密钥数量

        :return: The sm2 of this KmsInfo.
        :rtype: int
        """
        return self._sm2

    @sm2.setter
    def sm2(self, sm2):
        r"""Sets the sm2 of this KmsInfo.

        SM2算法密钥数量

        :param sm2: The sm2 of this KmsInfo.
        :type sm2: int
        """
        self._sm2 = sm2

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
        if not isinstance(other, KmsInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
