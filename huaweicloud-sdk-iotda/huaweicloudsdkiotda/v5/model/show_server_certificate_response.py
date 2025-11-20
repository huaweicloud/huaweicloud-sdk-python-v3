# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowServerCertificateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_certificate_id': 'str',
        'common_name': 'str',
        'certificate_pem': 'str',
        'effective_date': 'str',
        'expiry_date': 'str',
        'certificate_owner': 'str',
        'certificate_issuer': 'str'
    }

    attribute_map = {
        'server_certificate_id': 'server_certificate_id',
        'common_name': 'common_name',
        'certificate_pem': 'certificate_pem',
        'effective_date': 'effective_date',
        'expiry_date': 'expiry_date',
        'certificate_owner': 'certificate_owner',
        'certificate_issuer': 'certificate_issuer'
    }

    def __init__(self, server_certificate_id=None, common_name=None, certificate_pem=None, effective_date=None, expiry_date=None, certificate_owner=None, certificate_issuer=None):
        r"""ShowServerCertificateResponse

        The model defined in huaweicloud sdk

        :param server_certificate_id: 唯一标识ID
        :type server_certificate_id: str
        :param common_name: **参数说明**：证书通用名
        :type common_name: str
        :param certificate_pem: **参数说明**：证书内容，PEM格式
        :type certificate_pem: str
        :param effective_date: 证书生效日期。格式：yyyyMMdd&#39;T&#39;HHmmss&#39;Z&#39;，如20151212T121212Z。
        :type effective_date: str
        :param expiry_date: 证书失效日期。格式：yyyyMMdd&#39;T&#39;HHmmss&#39;Z&#39;，如20151212T121212Z。
        :type expiry_date: str
        :param certificate_owner: 证书所有者。
        :type certificate_owner: str
        :param certificate_issuer: 证书颁发者。
        :type certificate_issuer: str
        """
        
        super().__init__()

        self._server_certificate_id = None
        self._common_name = None
        self._certificate_pem = None
        self._effective_date = None
        self._expiry_date = None
        self._certificate_owner = None
        self._certificate_issuer = None
        self.discriminator = None

        if server_certificate_id is not None:
            self.server_certificate_id = server_certificate_id
        if common_name is not None:
            self.common_name = common_name
        if certificate_pem is not None:
            self.certificate_pem = certificate_pem
        if effective_date is not None:
            self.effective_date = effective_date
        if expiry_date is not None:
            self.expiry_date = expiry_date
        if certificate_owner is not None:
            self.certificate_owner = certificate_owner
        if certificate_issuer is not None:
            self.certificate_issuer = certificate_issuer

    @property
    def server_certificate_id(self):
        r"""Gets the server_certificate_id of this ShowServerCertificateResponse.

        唯一标识ID

        :return: The server_certificate_id of this ShowServerCertificateResponse.
        :rtype: str
        """
        return self._server_certificate_id

    @server_certificate_id.setter
    def server_certificate_id(self, server_certificate_id):
        r"""Sets the server_certificate_id of this ShowServerCertificateResponse.

        唯一标识ID

        :param server_certificate_id: The server_certificate_id of this ShowServerCertificateResponse.
        :type server_certificate_id: str
        """
        self._server_certificate_id = server_certificate_id

    @property
    def common_name(self):
        r"""Gets the common_name of this ShowServerCertificateResponse.

        **参数说明**：证书通用名

        :return: The common_name of this ShowServerCertificateResponse.
        :rtype: str
        """
        return self._common_name

    @common_name.setter
    def common_name(self, common_name):
        r"""Sets the common_name of this ShowServerCertificateResponse.

        **参数说明**：证书通用名

        :param common_name: The common_name of this ShowServerCertificateResponse.
        :type common_name: str
        """
        self._common_name = common_name

    @property
    def certificate_pem(self):
        r"""Gets the certificate_pem of this ShowServerCertificateResponse.

        **参数说明**：证书内容，PEM格式

        :return: The certificate_pem of this ShowServerCertificateResponse.
        :rtype: str
        """
        return self._certificate_pem

    @certificate_pem.setter
    def certificate_pem(self, certificate_pem):
        r"""Sets the certificate_pem of this ShowServerCertificateResponse.

        **参数说明**：证书内容，PEM格式

        :param certificate_pem: The certificate_pem of this ShowServerCertificateResponse.
        :type certificate_pem: str
        """
        self._certificate_pem = certificate_pem

    @property
    def effective_date(self):
        r"""Gets the effective_date of this ShowServerCertificateResponse.

        证书生效日期。格式：yyyyMMdd'T'HHmmss'Z'，如20151212T121212Z。

        :return: The effective_date of this ShowServerCertificateResponse.
        :rtype: str
        """
        return self._effective_date

    @effective_date.setter
    def effective_date(self, effective_date):
        r"""Sets the effective_date of this ShowServerCertificateResponse.

        证书生效日期。格式：yyyyMMdd'T'HHmmss'Z'，如20151212T121212Z。

        :param effective_date: The effective_date of this ShowServerCertificateResponse.
        :type effective_date: str
        """
        self._effective_date = effective_date

    @property
    def expiry_date(self):
        r"""Gets the expiry_date of this ShowServerCertificateResponse.

        证书失效日期。格式：yyyyMMdd'T'HHmmss'Z'，如20151212T121212Z。

        :return: The expiry_date of this ShowServerCertificateResponse.
        :rtype: str
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        r"""Sets the expiry_date of this ShowServerCertificateResponse.

        证书失效日期。格式：yyyyMMdd'T'HHmmss'Z'，如20151212T121212Z。

        :param expiry_date: The expiry_date of this ShowServerCertificateResponse.
        :type expiry_date: str
        """
        self._expiry_date = expiry_date

    @property
    def certificate_owner(self):
        r"""Gets the certificate_owner of this ShowServerCertificateResponse.

        证书所有者。

        :return: The certificate_owner of this ShowServerCertificateResponse.
        :rtype: str
        """
        return self._certificate_owner

    @certificate_owner.setter
    def certificate_owner(self, certificate_owner):
        r"""Sets the certificate_owner of this ShowServerCertificateResponse.

        证书所有者。

        :param certificate_owner: The certificate_owner of this ShowServerCertificateResponse.
        :type certificate_owner: str
        """
        self._certificate_owner = certificate_owner

    @property
    def certificate_issuer(self):
        r"""Gets the certificate_issuer of this ShowServerCertificateResponse.

        证书颁发者。

        :return: The certificate_issuer of this ShowServerCertificateResponse.
        :rtype: str
        """
        return self._certificate_issuer

    @certificate_issuer.setter
    def certificate_issuer(self, certificate_issuer):
        r"""Sets the certificate_issuer of this ShowServerCertificateResponse.

        证书颁发者。

        :param certificate_issuer: The certificate_issuer of this ShowServerCertificateResponse.
        :type certificate_issuer: str
        """
        self._certificate_issuer = certificate_issuer

    def to_dict(self):
        import warnings
        warnings.warn("ShowServerCertificateResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowServerCertificateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
