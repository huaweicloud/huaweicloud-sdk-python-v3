# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowHttpsConfigResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source': 'str',
        'cert_name': 'str',
        'cert_id': 'str',
        'https_status': 'int',
        'certificate': 'str',
        'force_redirect_https': 'int',
        'http2': 'int'
    }

    attribute_map = {
        'source': 'source',
        'cert_name': 'cert_name',
        'cert_id': 'cert_id',
        'https_status': 'https_status',
        'certificate': 'certificate',
        'force_redirect_https': 'force_redirect_https',
        'http2': 'http2'
    }

    def __init__(self, source=None, cert_name=None, cert_id=None, https_status=None, certificate=None, force_redirect_https=None, http2=None):
        r"""ShowHttpsConfigResponse

        The model defined in huaweicloud sdk

        :param source: 来源，user表示用户自己上传，scm表示scm证书 
        :type source: str
        :param cert_name: 证书名称 
        :type cert_name: str
        :param cert_id: 证书id 
        :type cert_id: str
        :param https_status: https配置 
        :type https_status: int
        :param certificate: 证书内容 
        :type certificate: str
        :param force_redirect_https: 客户端请求是否强制重定向，0表示不重定向，1表示重定向 
        :type force_redirect_https: int
        :param http2: 是否使用HTTP2.0，0表示不使用HTTP2.0，1表示使用 
        :type http2: int
        """
        
        super().__init__()

        self._source = None
        self._cert_name = None
        self._cert_id = None
        self._https_status = None
        self._certificate = None
        self._force_redirect_https = None
        self._http2 = None
        self.discriminator = None

        if source is not None:
            self.source = source
        if cert_name is not None:
            self.cert_name = cert_name
        if cert_id is not None:
            self.cert_id = cert_id
        if https_status is not None:
            self.https_status = https_status
        if certificate is not None:
            self.certificate = certificate
        if force_redirect_https is not None:
            self.force_redirect_https = force_redirect_https
        if http2 is not None:
            self.http2 = http2

    @property
    def source(self):
        r"""Gets the source of this ShowHttpsConfigResponse.

        来源，user表示用户自己上传，scm表示scm证书 

        :return: The source of this ShowHttpsConfigResponse.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this ShowHttpsConfigResponse.

        来源，user表示用户自己上传，scm表示scm证书 

        :param source: The source of this ShowHttpsConfigResponse.
        :type source: str
        """
        self._source = source

    @property
    def cert_name(self):
        r"""Gets the cert_name of this ShowHttpsConfigResponse.

        证书名称 

        :return: The cert_name of this ShowHttpsConfigResponse.
        :rtype: str
        """
        return self._cert_name

    @cert_name.setter
    def cert_name(self, cert_name):
        r"""Sets the cert_name of this ShowHttpsConfigResponse.

        证书名称 

        :param cert_name: The cert_name of this ShowHttpsConfigResponse.
        :type cert_name: str
        """
        self._cert_name = cert_name

    @property
    def cert_id(self):
        r"""Gets the cert_id of this ShowHttpsConfigResponse.

        证书id 

        :return: The cert_id of this ShowHttpsConfigResponse.
        :rtype: str
        """
        return self._cert_id

    @cert_id.setter
    def cert_id(self, cert_id):
        r"""Sets the cert_id of this ShowHttpsConfigResponse.

        证书id 

        :param cert_id: The cert_id of this ShowHttpsConfigResponse.
        :type cert_id: str
        """
        self._cert_id = cert_id

    @property
    def https_status(self):
        r"""Gets the https_status of this ShowHttpsConfigResponse.

        https配置 

        :return: The https_status of this ShowHttpsConfigResponse.
        :rtype: int
        """
        return self._https_status

    @https_status.setter
    def https_status(self, https_status):
        r"""Sets the https_status of this ShowHttpsConfigResponse.

        https配置 

        :param https_status: The https_status of this ShowHttpsConfigResponse.
        :type https_status: int
        """
        self._https_status = https_status

    @property
    def certificate(self):
        r"""Gets the certificate of this ShowHttpsConfigResponse.

        证书内容 

        :return: The certificate of this ShowHttpsConfigResponse.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        r"""Sets the certificate of this ShowHttpsConfigResponse.

        证书内容 

        :param certificate: The certificate of this ShowHttpsConfigResponse.
        :type certificate: str
        """
        self._certificate = certificate

    @property
    def force_redirect_https(self):
        r"""Gets the force_redirect_https of this ShowHttpsConfigResponse.

        客户端请求是否强制重定向，0表示不重定向，1表示重定向 

        :return: The force_redirect_https of this ShowHttpsConfigResponse.
        :rtype: int
        """
        return self._force_redirect_https

    @force_redirect_https.setter
    def force_redirect_https(self, force_redirect_https):
        r"""Sets the force_redirect_https of this ShowHttpsConfigResponse.

        客户端请求是否强制重定向，0表示不重定向，1表示重定向 

        :param force_redirect_https: The force_redirect_https of this ShowHttpsConfigResponse.
        :type force_redirect_https: int
        """
        self._force_redirect_https = force_redirect_https

    @property
    def http2(self):
        r"""Gets the http2 of this ShowHttpsConfigResponse.

        是否使用HTTP2.0，0表示不使用HTTP2.0，1表示使用 

        :return: The http2 of this ShowHttpsConfigResponse.
        :rtype: int
        """
        return self._http2

    @http2.setter
    def http2(self, http2):
        r"""Sets the http2 of this ShowHttpsConfigResponse.

        是否使用HTTP2.0，0表示不使用HTTP2.0，1表示使用 

        :param http2: The http2 of this ShowHttpsConfigResponse.
        :type http2: int
        """
        self._http2 = http2

    def to_dict(self):
        import warnings
        warnings.warn("ShowHttpsConfigResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowHttpsConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
