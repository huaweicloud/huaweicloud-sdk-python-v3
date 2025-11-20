# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateServerCertificateDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'certificate_pem': 'str',
        'private_key': 'str',
        'private_key_password': 'str'
    }

    attribute_map = {
        'certificate_pem': 'certificate_pem',
        'private_key': 'private_key',
        'private_key_password': 'private_key_password'
    }

    def __init__(self, certificate_pem=None, private_key=None, private_key_password=None):
        r"""CreateServerCertificateDTO

        The model defined in huaweicloud sdk

        :param certificate_pem: **参数说明**：证书内容，PEM格式
        :type certificate_pem: str
        :param private_key: **参数说明**：证书私钥
        :type private_key: str
        :param private_key_password: **参数说明**：私钥密码
        :type private_key_password: str
        """
        
        

        self._certificate_pem = None
        self._private_key = None
        self._private_key_password = None
        self.discriminator = None

        self.certificate_pem = certificate_pem
        self.private_key = private_key
        if private_key_password is not None:
            self.private_key_password = private_key_password

    @property
    def certificate_pem(self):
        r"""Gets the certificate_pem of this CreateServerCertificateDTO.

        **参数说明**：证书内容，PEM格式

        :return: The certificate_pem of this CreateServerCertificateDTO.
        :rtype: str
        """
        return self._certificate_pem

    @certificate_pem.setter
    def certificate_pem(self, certificate_pem):
        r"""Sets the certificate_pem of this CreateServerCertificateDTO.

        **参数说明**：证书内容，PEM格式

        :param certificate_pem: The certificate_pem of this CreateServerCertificateDTO.
        :type certificate_pem: str
        """
        self._certificate_pem = certificate_pem

    @property
    def private_key(self):
        r"""Gets the private_key of this CreateServerCertificateDTO.

        **参数说明**：证书私钥

        :return: The private_key of this CreateServerCertificateDTO.
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        r"""Sets the private_key of this CreateServerCertificateDTO.

        **参数说明**：证书私钥

        :param private_key: The private_key of this CreateServerCertificateDTO.
        :type private_key: str
        """
        self._private_key = private_key

    @property
    def private_key_password(self):
        r"""Gets the private_key_password of this CreateServerCertificateDTO.

        **参数说明**：私钥密码

        :return: The private_key_password of this CreateServerCertificateDTO.
        :rtype: str
        """
        return self._private_key_password

    @private_key_password.setter
    def private_key_password(self, private_key_password):
        r"""Sets the private_key_password of this CreateServerCertificateDTO.

        **参数说明**：私钥密码

        :param private_key_password: The private_key_password of this CreateServerCertificateDTO.
        :type private_key_password: str
        """
        self._private_key_password = private_key_password

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateServerCertificateDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
