# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CaCertificate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'serial_number': 'str',
        'signature_algorithm': 'str',
        'issuer': 'str',
        'subject': 'str',
        'expire_time': 'datetime',
        'is_updatable': 'bool'
    }

    attribute_map = {
        'serial_number': 'serial_number',
        'signature_algorithm': 'signature_algorithm',
        'issuer': 'issuer',
        'subject': 'subject',
        'expire_time': 'expire_time',
        'is_updatable': 'is_updatable'
    }

    def __init__(self, serial_number=None, signature_algorithm=None, issuer=None, subject=None, expire_time=None, is_updatable=None):
        """CaCertificate

        The model defined in huaweicloud sdk

        :param serial_number: 证书序列号
        :type serial_number: str
        :param signature_algorithm: 签名算法
        :type signature_algorithm: str
        :param issuer: 证书颁发者
        :type issuer: str
        :param subject: 证书主题
        :type subject: str
        :param expire_time: 证书过期时间
        :type expire_time: datetime
        :param is_updatable: 是否能更新内容
        :type is_updatable: bool
        """
        
        

        self._serial_number = None
        self._signature_algorithm = None
        self._issuer = None
        self._subject = None
        self._expire_time = None
        self._is_updatable = None
        self.discriminator = None

        if serial_number is not None:
            self.serial_number = serial_number
        if signature_algorithm is not None:
            self.signature_algorithm = signature_algorithm
        if issuer is not None:
            self.issuer = issuer
        if subject is not None:
            self.subject = subject
        if expire_time is not None:
            self.expire_time = expire_time
        if is_updatable is not None:
            self.is_updatable = is_updatable

    @property
    def serial_number(self):
        """Gets the serial_number of this CaCertificate.

        证书序列号

        :return: The serial_number of this CaCertificate.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this CaCertificate.

        证书序列号

        :param serial_number: The serial_number of this CaCertificate.
        :type serial_number: str
        """
        self._serial_number = serial_number

    @property
    def signature_algorithm(self):
        """Gets the signature_algorithm of this CaCertificate.

        签名算法

        :return: The signature_algorithm of this CaCertificate.
        :rtype: str
        """
        return self._signature_algorithm

    @signature_algorithm.setter
    def signature_algorithm(self, signature_algorithm):
        """Sets the signature_algorithm of this CaCertificate.

        签名算法

        :param signature_algorithm: The signature_algorithm of this CaCertificate.
        :type signature_algorithm: str
        """
        self._signature_algorithm = signature_algorithm

    @property
    def issuer(self):
        """Gets the issuer of this CaCertificate.

        证书颁发者

        :return: The issuer of this CaCertificate.
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this CaCertificate.

        证书颁发者

        :param issuer: The issuer of this CaCertificate.
        :type issuer: str
        """
        self._issuer = issuer

    @property
    def subject(self):
        """Gets the subject of this CaCertificate.

        证书主题

        :return: The subject of this CaCertificate.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this CaCertificate.

        证书主题

        :param subject: The subject of this CaCertificate.
        :type subject: str
        """
        self._subject = subject

    @property
    def expire_time(self):
        """Gets the expire_time of this CaCertificate.

        证书过期时间

        :return: The expire_time of this CaCertificate.
        :rtype: datetime
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this CaCertificate.

        证书过期时间

        :param expire_time: The expire_time of this CaCertificate.
        :type expire_time: datetime
        """
        self._expire_time = expire_time

    @property
    def is_updatable(self):
        """Gets the is_updatable of this CaCertificate.

        是否能更新内容

        :return: The is_updatable of this CaCertificate.
        :rtype: bool
        """
        return self._is_updatable

    @is_updatable.setter
    def is_updatable(self, is_updatable):
        """Sets the is_updatable of this CaCertificate.

        是否能更新内容

        :param is_updatable: The is_updatable of this CaCertificate.
        :type is_updatable: bool
        """
        self._is_updatable = is_updatable

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
        if not isinstance(other, CaCertificate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
