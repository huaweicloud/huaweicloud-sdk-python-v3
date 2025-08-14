# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSpCertificateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'certificate_id': 'str',
        'x509certificate': 'str',
        'algorithm': 'str',
        'expiry_date': 'int',
        'state': 'str'
    }

    attribute_map = {
        'certificate_id': 'certificate_id',
        'x509certificate': 'x509certificate',
        'algorithm': 'algorithm',
        'expiry_date': 'expiry_date',
        'state': 'state'
    }

    def __init__(self, certificate_id=None, x509certificate=None, algorithm=None, expiry_date=None, state=None):
        r"""CreateSpCertificateResponse

        The model defined in huaweicloud sdk

        :param certificate_id: 证书ID
        :type certificate_id: str
        :param x509certificate: x509证书
        :type x509certificate: str
        :param algorithm: 签名算法
        :type algorithm: str
        :param expiry_date: 证书过期时间戳
        :type expiry_date: int
        :param state: 证书激活状态
        :type state: str
        """
        
        super(CreateSpCertificateResponse, self).__init__()

        self._certificate_id = None
        self._x509certificate = None
        self._algorithm = None
        self._expiry_date = None
        self._state = None
        self.discriminator = None

        if certificate_id is not None:
            self.certificate_id = certificate_id
        if x509certificate is not None:
            self.x509certificate = x509certificate
        if algorithm is not None:
            self.algorithm = algorithm
        if expiry_date is not None:
            self.expiry_date = expiry_date
        if state is not None:
            self.state = state

    @property
    def certificate_id(self):
        r"""Gets the certificate_id of this CreateSpCertificateResponse.

        证书ID

        :return: The certificate_id of this CreateSpCertificateResponse.
        :rtype: str
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        r"""Sets the certificate_id of this CreateSpCertificateResponse.

        证书ID

        :param certificate_id: The certificate_id of this CreateSpCertificateResponse.
        :type certificate_id: str
        """
        self._certificate_id = certificate_id

    @property
    def x509certificate(self):
        r"""Gets the x509certificate of this CreateSpCertificateResponse.

        x509证书

        :return: The x509certificate of this CreateSpCertificateResponse.
        :rtype: str
        """
        return self._x509certificate

    @x509certificate.setter
    def x509certificate(self, x509certificate):
        r"""Sets the x509certificate of this CreateSpCertificateResponse.

        x509证书

        :param x509certificate: The x509certificate of this CreateSpCertificateResponse.
        :type x509certificate: str
        """
        self._x509certificate = x509certificate

    @property
    def algorithm(self):
        r"""Gets the algorithm of this CreateSpCertificateResponse.

        签名算法

        :return: The algorithm of this CreateSpCertificateResponse.
        :rtype: str
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        r"""Sets the algorithm of this CreateSpCertificateResponse.

        签名算法

        :param algorithm: The algorithm of this CreateSpCertificateResponse.
        :type algorithm: str
        """
        self._algorithm = algorithm

    @property
    def expiry_date(self):
        r"""Gets the expiry_date of this CreateSpCertificateResponse.

        证书过期时间戳

        :return: The expiry_date of this CreateSpCertificateResponse.
        :rtype: int
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        r"""Sets the expiry_date of this CreateSpCertificateResponse.

        证书过期时间戳

        :param expiry_date: The expiry_date of this CreateSpCertificateResponse.
        :type expiry_date: int
        """
        self._expiry_date = expiry_date

    @property
    def state(self):
        r"""Gets the state of this CreateSpCertificateResponse.

        证书激活状态

        :return: The state of this CreateSpCertificateResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this CreateSpCertificateResponse.

        证书激活状态

        :param state: The state of this CreateSpCertificateResponse.
        :type state: str
        """
        self._state = state

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
        if not isinstance(other, CreateSpCertificateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
