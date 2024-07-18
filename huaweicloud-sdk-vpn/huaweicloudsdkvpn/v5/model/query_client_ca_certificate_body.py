# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryClientCaCertificateBody:

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
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'issuer': 'issuer',
        'subject': 'subject',
        'serial_number': 'serial_number',
        'expiration_time': 'expiration_time',
        'signature_algorithm': 'signature_algorithm',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, name=None, issuer=None, subject=None, serial_number=None, expiration_time=None, signature_algorithm=None, created_at=None, updated_at=None):
        """QueryClientCaCertificateBody

        The model defined in huaweicloud sdk

        :param id: ID
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
        :param signature_algorithm: 客户端 CA 证书签名算法
        :type signature_algorithm: str
        :param created_at: 创建时间
        :type created_at: datetime
        :param updated_at: 更新时间
        :type updated_at: datetime
        """
        
        

        self._id = None
        self._name = None
        self._issuer = None
        self._subject = None
        self._serial_number = None
        self._expiration_time = None
        self._signature_algorithm = None
        self._created_at = None
        self._updated_at = None
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
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this QueryClientCaCertificateBody.

        ID

        :return: The id of this QueryClientCaCertificateBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this QueryClientCaCertificateBody.

        ID

        :param id: The id of this QueryClientCaCertificateBody.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this QueryClientCaCertificateBody.

        证书名

        :return: The name of this QueryClientCaCertificateBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this QueryClientCaCertificateBody.

        证书名

        :param name: The name of this QueryClientCaCertificateBody.
        :type name: str
        """
        self._name = name

    @property
    def issuer(self):
        """Gets the issuer of this QueryClientCaCertificateBody.

        颁发者

        :return: The issuer of this QueryClientCaCertificateBody.
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this QueryClientCaCertificateBody.

        颁发者

        :param issuer: The issuer of this QueryClientCaCertificateBody.
        :type issuer: str
        """
        self._issuer = issuer

    @property
    def subject(self):
        """Gets the subject of this QueryClientCaCertificateBody.

        主体

        :return: The subject of this QueryClientCaCertificateBody.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this QueryClientCaCertificateBody.

        主体

        :param subject: The subject of this QueryClientCaCertificateBody.
        :type subject: str
        """
        self._subject = subject

    @property
    def serial_number(self):
        """Gets the serial_number of this QueryClientCaCertificateBody.

        序列号

        :return: The serial_number of this QueryClientCaCertificateBody.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this QueryClientCaCertificateBody.

        序列号

        :param serial_number: The serial_number of this QueryClientCaCertificateBody.
        :type serial_number: str
        """
        self._serial_number = serial_number

    @property
    def expiration_time(self):
        """Gets the expiration_time of this QueryClientCaCertificateBody.

        过期时间

        :return: The expiration_time of this QueryClientCaCertificateBody.
        :rtype: datetime
        """
        return self._expiration_time

    @expiration_time.setter
    def expiration_time(self, expiration_time):
        """Sets the expiration_time of this QueryClientCaCertificateBody.

        过期时间

        :param expiration_time: The expiration_time of this QueryClientCaCertificateBody.
        :type expiration_time: datetime
        """
        self._expiration_time = expiration_time

    @property
    def signature_algorithm(self):
        """Gets the signature_algorithm of this QueryClientCaCertificateBody.

        客户端 CA 证书签名算法

        :return: The signature_algorithm of this QueryClientCaCertificateBody.
        :rtype: str
        """
        return self._signature_algorithm

    @signature_algorithm.setter
    def signature_algorithm(self, signature_algorithm):
        """Sets the signature_algorithm of this QueryClientCaCertificateBody.

        客户端 CA 证书签名算法

        :param signature_algorithm: The signature_algorithm of this QueryClientCaCertificateBody.
        :type signature_algorithm: str
        """
        self._signature_algorithm = signature_algorithm

    @property
    def created_at(self):
        """Gets the created_at of this QueryClientCaCertificateBody.

        创建时间

        :return: The created_at of this QueryClientCaCertificateBody.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this QueryClientCaCertificateBody.

        创建时间

        :param created_at: The created_at of this QueryClientCaCertificateBody.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this QueryClientCaCertificateBody.

        更新时间

        :return: The updated_at of this QueryClientCaCertificateBody.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this QueryClientCaCertificateBody.

        更新时间

        :param updated_at: The updated_at of this QueryClientCaCertificateBody.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

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
        if not isinstance(other, QueryClientCaCertificateBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
