# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceDistribution:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'encrypt_decrypt': 'int',
        'sign_verify': 'int',
        'kms': 'int',
        'timestamp': 'int',
        'colla_sign': 'int',
        'otp': 'int',
        'db_encrypt': 'int',
        'file_encrypt': 'int',
        'digit_seal': 'int',
        'ssl_vpn': 'int'
    }

    attribute_map = {
        'encrypt_decrypt': 'encrypt_decrypt',
        'sign_verify': 'sign_verify',
        'kms': 'kms',
        'timestamp': 'timestamp',
        'colla_sign': 'colla_sign',
        'otp': 'otp',
        'db_encrypt': 'db_encrypt',
        'file_encrypt': 'file_encrypt',
        'digit_seal': 'digit_seal',
        'ssl_vpn': 'ssl_vpn'
    }

    def __init__(self, encrypt_decrypt=None, sign_verify=None, kms=None, timestamp=None, colla_sign=None, otp=None, db_encrypt=None, file_encrypt=None, digit_seal=None, ssl_vpn=None):
        r"""InstanceDistribution

        The model defined in huaweicloud sdk

        :param encrypt_decrypt: 加解密服务实例数量
        :type encrypt_decrypt: int
        :param sign_verify: 签名验签服务实例数量
        :type sign_verify: int
        :param kms: 密钥管理服务实例数量
        :type kms: int
        :param timestamp: 时间戳服务实例数量
        :type timestamp: int
        :param colla_sign: 协同签名服务实例数量
        :type colla_sign: int
        :param otp: 动态口令服务实例数量
        :type otp: int
        :param db_encrypt: 数据库加密服务实例数量
        :type db_encrypt: int
        :param file_encrypt: 文件加密服务实例数量
        :type file_encrypt: int
        :param digit_seal: 电子签章服务实例数量
        :type digit_seal: int
        :param ssl_vpn: ssl vpn服务实例数量
        :type ssl_vpn: int
        """
        
        

        self._encrypt_decrypt = None
        self._sign_verify = None
        self._kms = None
        self._timestamp = None
        self._colla_sign = None
        self._otp = None
        self._db_encrypt = None
        self._file_encrypt = None
        self._digit_seal = None
        self._ssl_vpn = None
        self.discriminator = None

        self.encrypt_decrypt = encrypt_decrypt
        self.sign_verify = sign_verify
        self.kms = kms
        self.timestamp = timestamp
        self.colla_sign = colla_sign
        self.otp = otp
        self.db_encrypt = db_encrypt
        self.file_encrypt = file_encrypt
        self.digit_seal = digit_seal
        self.ssl_vpn = ssl_vpn

    @property
    def encrypt_decrypt(self):
        r"""Gets the encrypt_decrypt of this InstanceDistribution.

        加解密服务实例数量

        :return: The encrypt_decrypt of this InstanceDistribution.
        :rtype: int
        """
        return self._encrypt_decrypt

    @encrypt_decrypt.setter
    def encrypt_decrypt(self, encrypt_decrypt):
        r"""Sets the encrypt_decrypt of this InstanceDistribution.

        加解密服务实例数量

        :param encrypt_decrypt: The encrypt_decrypt of this InstanceDistribution.
        :type encrypt_decrypt: int
        """
        self._encrypt_decrypt = encrypt_decrypt

    @property
    def sign_verify(self):
        r"""Gets the sign_verify of this InstanceDistribution.

        签名验签服务实例数量

        :return: The sign_verify of this InstanceDistribution.
        :rtype: int
        """
        return self._sign_verify

    @sign_verify.setter
    def sign_verify(self, sign_verify):
        r"""Sets the sign_verify of this InstanceDistribution.

        签名验签服务实例数量

        :param sign_verify: The sign_verify of this InstanceDistribution.
        :type sign_verify: int
        """
        self._sign_verify = sign_verify

    @property
    def kms(self):
        r"""Gets the kms of this InstanceDistribution.

        密钥管理服务实例数量

        :return: The kms of this InstanceDistribution.
        :rtype: int
        """
        return self._kms

    @kms.setter
    def kms(self, kms):
        r"""Sets the kms of this InstanceDistribution.

        密钥管理服务实例数量

        :param kms: The kms of this InstanceDistribution.
        :type kms: int
        """
        self._kms = kms

    @property
    def timestamp(self):
        r"""Gets the timestamp of this InstanceDistribution.

        时间戳服务实例数量

        :return: The timestamp of this InstanceDistribution.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        r"""Sets the timestamp of this InstanceDistribution.

        时间戳服务实例数量

        :param timestamp: The timestamp of this InstanceDistribution.
        :type timestamp: int
        """
        self._timestamp = timestamp

    @property
    def colla_sign(self):
        r"""Gets the colla_sign of this InstanceDistribution.

        协同签名服务实例数量

        :return: The colla_sign of this InstanceDistribution.
        :rtype: int
        """
        return self._colla_sign

    @colla_sign.setter
    def colla_sign(self, colla_sign):
        r"""Sets the colla_sign of this InstanceDistribution.

        协同签名服务实例数量

        :param colla_sign: The colla_sign of this InstanceDistribution.
        :type colla_sign: int
        """
        self._colla_sign = colla_sign

    @property
    def otp(self):
        r"""Gets the otp of this InstanceDistribution.

        动态口令服务实例数量

        :return: The otp of this InstanceDistribution.
        :rtype: int
        """
        return self._otp

    @otp.setter
    def otp(self, otp):
        r"""Sets the otp of this InstanceDistribution.

        动态口令服务实例数量

        :param otp: The otp of this InstanceDistribution.
        :type otp: int
        """
        self._otp = otp

    @property
    def db_encrypt(self):
        r"""Gets the db_encrypt of this InstanceDistribution.

        数据库加密服务实例数量

        :return: The db_encrypt of this InstanceDistribution.
        :rtype: int
        """
        return self._db_encrypt

    @db_encrypt.setter
    def db_encrypt(self, db_encrypt):
        r"""Sets the db_encrypt of this InstanceDistribution.

        数据库加密服务实例数量

        :param db_encrypt: The db_encrypt of this InstanceDistribution.
        :type db_encrypt: int
        """
        self._db_encrypt = db_encrypt

    @property
    def file_encrypt(self):
        r"""Gets the file_encrypt of this InstanceDistribution.

        文件加密服务实例数量

        :return: The file_encrypt of this InstanceDistribution.
        :rtype: int
        """
        return self._file_encrypt

    @file_encrypt.setter
    def file_encrypt(self, file_encrypt):
        r"""Sets the file_encrypt of this InstanceDistribution.

        文件加密服务实例数量

        :param file_encrypt: The file_encrypt of this InstanceDistribution.
        :type file_encrypt: int
        """
        self._file_encrypt = file_encrypt

    @property
    def digit_seal(self):
        r"""Gets the digit_seal of this InstanceDistribution.

        电子签章服务实例数量

        :return: The digit_seal of this InstanceDistribution.
        :rtype: int
        """
        return self._digit_seal

    @digit_seal.setter
    def digit_seal(self, digit_seal):
        r"""Sets the digit_seal of this InstanceDistribution.

        电子签章服务实例数量

        :param digit_seal: The digit_seal of this InstanceDistribution.
        :type digit_seal: int
        """
        self._digit_seal = digit_seal

    @property
    def ssl_vpn(self):
        r"""Gets the ssl_vpn of this InstanceDistribution.

        ssl vpn服务实例数量

        :return: The ssl_vpn of this InstanceDistribution.
        :rtype: int
        """
        return self._ssl_vpn

    @ssl_vpn.setter
    def ssl_vpn(self, ssl_vpn):
        r"""Sets the ssl_vpn of this InstanceDistribution.

        ssl vpn服务实例数量

        :param ssl_vpn: The ssl_vpn of this InstanceDistribution.
        :type ssl_vpn: int
        """
        self._ssl_vpn = ssl_vpn

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
        if not isinstance(other, InstanceDistribution):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
