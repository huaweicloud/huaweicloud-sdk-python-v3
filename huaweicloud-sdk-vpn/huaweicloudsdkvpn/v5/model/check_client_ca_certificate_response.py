# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckClientCaCertificateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'issuer': 'str',
        'subject': 'str',
        'serial_number': 'str',
        'expiration_time': 'datetime',
        'signature_algorithm': 'str'
    }

    attribute_map = {
        'name': 'name',
        'issuer': 'issuer',
        'subject': 'subject',
        'serial_number': 'serial_number',
        'expiration_time': 'expiration_time',
        'signature_algorithm': 'signature_algorithm'
    }

    def __init__(self, name=None, issuer=None, subject=None, serial_number=None, expiration_time=None, signature_algorithm=None):
        r"""CheckClientCaCertificateResponse

        The model defined in huaweicloud sdk

        :param name: 证书名
        :type name: str
        :param issuer: 颁发者
        :type issuer: str
        :param subject: 主体
        :type subject: str
        :param serial_number: 序列号
        :type serial_number: str
        :param expiration_time: 过期时间
        :type expiration_time: datetime
        :param signature_algorithm: 客户端 CA 证书签名算法
        :type signature_algorithm: str
        """
        
        super(CheckClientCaCertificateResponse, self).__init__()

        self._name = None
        self._issuer = None
        self._subject = None
        self._serial_number = None
        self._expiration_time = None
        self._signature_algorithm = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if issuer is not None:
            self.issuer = issuer
        if subject is not None:
            self.subject = subject
        if serial_number is not None:
            self.serial_number = serial_number
        if expiration_time is not None:
            self.expiration_time = expiration_time
        if signature_algorithm is not None:
            self.signature_algorithm = signature_algorithm

    @property
    def name(self):
        r"""Gets the name of this CheckClientCaCertificateResponse.

        证书名

        :return: The name of this CheckClientCaCertificateResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CheckClientCaCertificateResponse.

        证书名

        :param name: The name of this CheckClientCaCertificateResponse.
        :type name: str
        """
        self._name = name

    @property
    def issuer(self):
        r"""Gets the issuer of this CheckClientCaCertificateResponse.

        颁发者

        :return: The issuer of this CheckClientCaCertificateResponse.
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        r"""Sets the issuer of this CheckClientCaCertificateResponse.

        颁发者

        :param issuer: The issuer of this CheckClientCaCertificateResponse.
        :type issuer: str
        """
        self._issuer = issuer

    @property
    def subject(self):
        r"""Gets the subject of this CheckClientCaCertificateResponse.

        主体

        :return: The subject of this CheckClientCaCertificateResponse.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        r"""Sets the subject of this CheckClientCaCertificateResponse.

        主体

        :param subject: The subject of this CheckClientCaCertificateResponse.
        :type subject: str
        """
        self._subject = subject

    @property
    def serial_number(self):
        r"""Gets the serial_number of this CheckClientCaCertificateResponse.

        序列号

        :return: The serial_number of this CheckClientCaCertificateResponse.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        r"""Sets the serial_number of this CheckClientCaCertificateResponse.

        序列号

        :param serial_number: The serial_number of this CheckClientCaCertificateResponse.
        :type serial_number: str
        """
        self._serial_number = serial_number

    @property
    def expiration_time(self):
        r"""Gets the expiration_time of this CheckClientCaCertificateResponse.

        过期时间

        :return: The expiration_time of this CheckClientCaCertificateResponse.
        :rtype: datetime
        """
        return self._expiration_time

    @expiration_time.setter
    def expiration_time(self, expiration_time):
        r"""Sets the expiration_time of this CheckClientCaCertificateResponse.

        过期时间

        :param expiration_time: The expiration_time of this CheckClientCaCertificateResponse.
        :type expiration_time: datetime
        """
        self._expiration_time = expiration_time

    @property
    def signature_algorithm(self):
        r"""Gets the signature_algorithm of this CheckClientCaCertificateResponse.

        客户端 CA 证书签名算法

        :return: The signature_algorithm of this CheckClientCaCertificateResponse.
        :rtype: str
        """
        return self._signature_algorithm

    @signature_algorithm.setter
    def signature_algorithm(self, signature_algorithm):
        r"""Sets the signature_algorithm of this CheckClientCaCertificateResponse.

        客户端 CA 证书签名算法

        :param signature_algorithm: The signature_algorithm of this CheckClientCaCertificateResponse.
        :type signature_algorithm: str
        """
        self._signature_algorithm = signature_algorithm

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
        if not isinstance(other, CheckClientCaCertificateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
