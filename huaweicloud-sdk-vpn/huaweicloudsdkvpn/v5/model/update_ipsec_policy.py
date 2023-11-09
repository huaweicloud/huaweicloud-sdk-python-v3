# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateIpsecPolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'authentication_algorithm': 'str',
        'encryption_algorithm': 'str',
        'pfs': 'str',
        'transform_protocol': 'str',
        'lifetime_seconds': 'int',
        'encapsulation_mode': 'str'
    }

    attribute_map = {
        'authentication_algorithm': 'authentication_algorithm',
        'encryption_algorithm': 'encryption_algorithm',
        'pfs': 'pfs',
        'transform_protocol': 'transform_protocol',
        'lifetime_seconds': 'lifetime_seconds',
        'encapsulation_mode': 'encapsulation_mode'
    }

    def __init__(self, authentication_algorithm=None, encryption_algorithm=None, pfs=None, transform_protocol=None, lifetime_seconds=None, encapsulation_mode=None):
        """UpdateIpsecPolicy

        The model defined in huaweicloud sdk

        :param authentication_algorithm: 认证算法，SHA1和MD5安全性较低，请慎用
        :type authentication_algorithm: str
        :param encryption_algorithm: 加密算法，3DES安全性较低，请慎用
        :type encryption_algorithm: str
        :param pfs: PFS使用的DH密钥组
        :type pfs: str
        :param transform_protocol: 传输模式
        :type transform_protocol: str
        :param lifetime_seconds: 表示配置IPSec连接建立的隧道以时间为基准的生存周期
        :type lifetime_seconds: int
        :param encapsulation_mode: 封装模式，当前只有tunnel模式
        :type encapsulation_mode: str
        """
        
        

        self._authentication_algorithm = None
        self._encryption_algorithm = None
        self._pfs = None
        self._transform_protocol = None
        self._lifetime_seconds = None
        self._encapsulation_mode = None
        self.discriminator = None

        if authentication_algorithm is not None:
            self.authentication_algorithm = authentication_algorithm
        if encryption_algorithm is not None:
            self.encryption_algorithm = encryption_algorithm
        if pfs is not None:
            self.pfs = pfs
        if transform_protocol is not None:
            self.transform_protocol = transform_protocol
        if lifetime_seconds is not None:
            self.lifetime_seconds = lifetime_seconds
        if encapsulation_mode is not None:
            self.encapsulation_mode = encapsulation_mode

    @property
    def authentication_algorithm(self):
        """Gets the authentication_algorithm of this UpdateIpsecPolicy.

        认证算法，SHA1和MD5安全性较低，请慎用

        :return: The authentication_algorithm of this UpdateIpsecPolicy.
        :rtype: str
        """
        return self._authentication_algorithm

    @authentication_algorithm.setter
    def authentication_algorithm(self, authentication_algorithm):
        """Sets the authentication_algorithm of this UpdateIpsecPolicy.

        认证算法，SHA1和MD5安全性较低，请慎用

        :param authentication_algorithm: The authentication_algorithm of this UpdateIpsecPolicy.
        :type authentication_algorithm: str
        """
        self._authentication_algorithm = authentication_algorithm

    @property
    def encryption_algorithm(self):
        """Gets the encryption_algorithm of this UpdateIpsecPolicy.

        加密算法，3DES安全性较低，请慎用

        :return: The encryption_algorithm of this UpdateIpsecPolicy.
        :rtype: str
        """
        return self._encryption_algorithm

    @encryption_algorithm.setter
    def encryption_algorithm(self, encryption_algorithm):
        """Sets the encryption_algorithm of this UpdateIpsecPolicy.

        加密算法，3DES安全性较低，请慎用

        :param encryption_algorithm: The encryption_algorithm of this UpdateIpsecPolicy.
        :type encryption_algorithm: str
        """
        self._encryption_algorithm = encryption_algorithm

    @property
    def pfs(self):
        """Gets the pfs of this UpdateIpsecPolicy.

        PFS使用的DH密钥组

        :return: The pfs of this UpdateIpsecPolicy.
        :rtype: str
        """
        return self._pfs

    @pfs.setter
    def pfs(self, pfs):
        """Sets the pfs of this UpdateIpsecPolicy.

        PFS使用的DH密钥组

        :param pfs: The pfs of this UpdateIpsecPolicy.
        :type pfs: str
        """
        self._pfs = pfs

    @property
    def transform_protocol(self):
        """Gets the transform_protocol of this UpdateIpsecPolicy.

        传输模式

        :return: The transform_protocol of this UpdateIpsecPolicy.
        :rtype: str
        """
        return self._transform_protocol

    @transform_protocol.setter
    def transform_protocol(self, transform_protocol):
        """Sets the transform_protocol of this UpdateIpsecPolicy.

        传输模式

        :param transform_protocol: The transform_protocol of this UpdateIpsecPolicy.
        :type transform_protocol: str
        """
        self._transform_protocol = transform_protocol

    @property
    def lifetime_seconds(self):
        """Gets the lifetime_seconds of this UpdateIpsecPolicy.

        表示配置IPSec连接建立的隧道以时间为基准的生存周期

        :return: The lifetime_seconds of this UpdateIpsecPolicy.
        :rtype: int
        """
        return self._lifetime_seconds

    @lifetime_seconds.setter
    def lifetime_seconds(self, lifetime_seconds):
        """Sets the lifetime_seconds of this UpdateIpsecPolicy.

        表示配置IPSec连接建立的隧道以时间为基准的生存周期

        :param lifetime_seconds: The lifetime_seconds of this UpdateIpsecPolicy.
        :type lifetime_seconds: int
        """
        self._lifetime_seconds = lifetime_seconds

    @property
    def encapsulation_mode(self):
        """Gets the encapsulation_mode of this UpdateIpsecPolicy.

        封装模式，当前只有tunnel模式

        :return: The encapsulation_mode of this UpdateIpsecPolicy.
        :rtype: str
        """
        return self._encapsulation_mode

    @encapsulation_mode.setter
    def encapsulation_mode(self, encapsulation_mode):
        """Sets the encapsulation_mode of this UpdateIpsecPolicy.

        封装模式，当前只有tunnel模式

        :param encapsulation_mode: The encapsulation_mode of this UpdateIpsecPolicy.
        :type encapsulation_mode: str
        """
        self._encapsulation_mode = encapsulation_mode

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
        if not isinstance(other, UpdateIpsecPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
