# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CertificateDto:

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
        'certificate': 'str',
        'certificate_id': 'str',
        'expiry_date': 'int',
        'status': 'str',
        'key_size': 'str',
        'issue_date': 'int'
    }

    attribute_map = {
        'algorithm': 'algorithm',
        'certificate': 'certificate',
        'certificate_id': 'certificate_id',
        'expiry_date': 'expiry_date',
        'status': 'status',
        'key_size': 'key_size',
        'issue_date': 'issue_date'
    }

    def __init__(self, algorithm=None, certificate=None, certificate_id=None, expiry_date=None, status=None, key_size=None, issue_date=None):
        r"""CertificateDto

        The model defined in huaweicloud sdk

        :param algorithm: 证书生成算法
        :type algorithm: str
        :param certificate: 应用程序证书
        :type certificate: str
        :param certificate_id: 应用程序证书Id
        :type certificate_id: str
        :param expiry_date: 证书过期时间
        :type expiry_date: int
        :param status: 证书状态
        :type status: str
        :param key_size: 密钥大小
        :type key_size: str
        :param issue_date: 证书生成时间
        :type issue_date: int
        """
        
        

        self._algorithm = None
        self._certificate = None
        self._certificate_id = None
        self._expiry_date = None
        self._status = None
        self._key_size = None
        self._issue_date = None
        self.discriminator = None

        self.algorithm = algorithm
        self.certificate = certificate
        self.certificate_id = certificate_id
        self.expiry_date = expiry_date
        self.status = status
        self.key_size = key_size
        self.issue_date = issue_date

    @property
    def algorithm(self):
        r"""Gets the algorithm of this CertificateDto.

        证书生成算法

        :return: The algorithm of this CertificateDto.
        :rtype: str
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        r"""Sets the algorithm of this CertificateDto.

        证书生成算法

        :param algorithm: The algorithm of this CertificateDto.
        :type algorithm: str
        """
        self._algorithm = algorithm

    @property
    def certificate(self):
        r"""Gets the certificate of this CertificateDto.

        应用程序证书

        :return: The certificate of this CertificateDto.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        r"""Sets the certificate of this CertificateDto.

        应用程序证书

        :param certificate: The certificate of this CertificateDto.
        :type certificate: str
        """
        self._certificate = certificate

    @property
    def certificate_id(self):
        r"""Gets the certificate_id of this CertificateDto.

        应用程序证书Id

        :return: The certificate_id of this CertificateDto.
        :rtype: str
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        r"""Sets the certificate_id of this CertificateDto.

        应用程序证书Id

        :param certificate_id: The certificate_id of this CertificateDto.
        :type certificate_id: str
        """
        self._certificate_id = certificate_id

    @property
    def expiry_date(self):
        r"""Gets the expiry_date of this CertificateDto.

        证书过期时间

        :return: The expiry_date of this CertificateDto.
        :rtype: int
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        r"""Sets the expiry_date of this CertificateDto.

        证书过期时间

        :param expiry_date: The expiry_date of this CertificateDto.
        :type expiry_date: int
        """
        self._expiry_date = expiry_date

    @property
    def status(self):
        r"""Gets the status of this CertificateDto.

        证书状态

        :return: The status of this CertificateDto.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CertificateDto.

        证书状态

        :param status: The status of this CertificateDto.
        :type status: str
        """
        self._status = status

    @property
    def key_size(self):
        r"""Gets the key_size of this CertificateDto.

        密钥大小

        :return: The key_size of this CertificateDto.
        :rtype: str
        """
        return self._key_size

    @key_size.setter
    def key_size(self, key_size):
        r"""Sets the key_size of this CertificateDto.

        密钥大小

        :param key_size: The key_size of this CertificateDto.
        :type key_size: str
        """
        self._key_size = key_size

    @property
    def issue_date(self):
        r"""Gets the issue_date of this CertificateDto.

        证书生成时间

        :return: The issue_date of this CertificateDto.
        :rtype: int
        """
        return self._issue_date

    @issue_date.setter
    def issue_date(self, issue_date):
        r"""Sets the issue_date of this CertificateDto.

        证书生成时间

        :param issue_date: The issue_date of this CertificateDto.
        :type issue_date: int
        """
        self._issue_date = issue_date

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
        if not isinstance(other, CertificateDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
