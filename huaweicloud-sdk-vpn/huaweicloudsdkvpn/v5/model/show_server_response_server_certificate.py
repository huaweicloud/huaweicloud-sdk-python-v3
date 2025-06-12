# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowServerResponseServerCertificate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'issuer': 'str',
        'subject': 'str',
        'serial_number': 'str',
        'expiration_time': 'datetime',
        'signature_algorithm': 'str',
        'source': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'issuer': 'issuer',
        'subject': 'subject',
        'serial_number': 'serial_number',
        'expiration_time': 'expiration_time',
        'signature_algorithm': 'signature_algorithm',
        'source': 'source'
    }

    def __init__(self, id=None, name=None, issuer=None, subject=None, serial_number=None, expiration_time=None, signature_algorithm=None, source=None):
        r"""ShowServerResponseServerCertificate

        The model defined in huaweicloud sdk

        :param id: 证书 ID，CCM 服务中的certificate_id，证书在CCM中被删除后，该ID为空
        :type id: str
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
        :param signature_algorithm: 证书签名算法
        :type signature_algorithm: str
        :param source: 证书来源
        :type source: str
        """
        
        

        self._id = None
        self._name = None
        self._issuer = None
        self._subject = None
        self._serial_number = None
        self._expiration_time = None
        self._signature_algorithm = None
        self._source = None
        self.discriminator = None

        if id is not None:
            self.id = id
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
        if source is not None:
            self.source = source

    @property
    def id(self):
        r"""Gets the id of this ShowServerResponseServerCertificate.

        证书 ID，CCM 服务中的certificate_id，证书在CCM中被删除后，该ID为空

        :return: The id of this ShowServerResponseServerCertificate.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowServerResponseServerCertificate.

        证书 ID，CCM 服务中的certificate_id，证书在CCM中被删除后，该ID为空

        :param id: The id of this ShowServerResponseServerCertificate.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ShowServerResponseServerCertificate.

        证书名

        :return: The name of this ShowServerResponseServerCertificate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowServerResponseServerCertificate.

        证书名

        :param name: The name of this ShowServerResponseServerCertificate.
        :type name: str
        """
        self._name = name

    @property
    def issuer(self):
        r"""Gets the issuer of this ShowServerResponseServerCertificate.

        颁发者

        :return: The issuer of this ShowServerResponseServerCertificate.
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        r"""Sets the issuer of this ShowServerResponseServerCertificate.

        颁发者

        :param issuer: The issuer of this ShowServerResponseServerCertificate.
        :type issuer: str
        """
        self._issuer = issuer

    @property
    def subject(self):
        r"""Gets the subject of this ShowServerResponseServerCertificate.

        主体

        :return: The subject of this ShowServerResponseServerCertificate.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        r"""Sets the subject of this ShowServerResponseServerCertificate.

        主体

        :param subject: The subject of this ShowServerResponseServerCertificate.
        :type subject: str
        """
        self._subject = subject

    @property
    def serial_number(self):
        r"""Gets the serial_number of this ShowServerResponseServerCertificate.

        序列号

        :return: The serial_number of this ShowServerResponseServerCertificate.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        r"""Sets the serial_number of this ShowServerResponseServerCertificate.

        序列号

        :param serial_number: The serial_number of this ShowServerResponseServerCertificate.
        :type serial_number: str
        """
        self._serial_number = serial_number

    @property
    def expiration_time(self):
        r"""Gets the expiration_time of this ShowServerResponseServerCertificate.

        过期时间

        :return: The expiration_time of this ShowServerResponseServerCertificate.
        :rtype: datetime
        """
        return self._expiration_time

    @expiration_time.setter
    def expiration_time(self, expiration_time):
        r"""Sets the expiration_time of this ShowServerResponseServerCertificate.

        过期时间

        :param expiration_time: The expiration_time of this ShowServerResponseServerCertificate.
        :type expiration_time: datetime
        """
        self._expiration_time = expiration_time

    @property
    def signature_algorithm(self):
        r"""Gets the signature_algorithm of this ShowServerResponseServerCertificate.

        证书签名算法

        :return: The signature_algorithm of this ShowServerResponseServerCertificate.
        :rtype: str
        """
        return self._signature_algorithm

    @signature_algorithm.setter
    def signature_algorithm(self, signature_algorithm):
        r"""Sets the signature_algorithm of this ShowServerResponseServerCertificate.

        证书签名算法

        :param signature_algorithm: The signature_algorithm of this ShowServerResponseServerCertificate.
        :type signature_algorithm: str
        """
        self._signature_algorithm = signature_algorithm

    @property
    def source(self):
        r"""Gets the source of this ShowServerResponseServerCertificate.

        证书来源

        :return: The source of this ShowServerResponseServerCertificate.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this ShowServerResponseServerCertificate.

        证书来源

        :param source: The source of this ShowServerResponseServerCertificate.
        :type source: str
        """
        self._source = source

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
        if not isinstance(other, ShowServerResponseServerCertificate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
