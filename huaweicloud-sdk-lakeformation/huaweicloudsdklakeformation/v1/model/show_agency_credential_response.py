# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAgencyCredentialResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agency_type': 'str',
        'agency_name': 'str',
        'security_token': 'str',
        'expires_at': 'str',
        'issued_at': 'str',
        'access': 'str',
        'secret': 'str'
    }

    attribute_map = {
        'agency_type': 'agency_type',
        'agency_name': 'agency_name',
        'security_token': 'security_token',
        'expires_at': 'expires_at',
        'issued_at': 'issued_at',
        'access': 'access',
        'secret': 'secret'
    }

    def __init__(self, agency_type=None, agency_name=None, security_token=None, expires_at=None, issued_at=None, access=None, secret=None):
        r"""ShowAgencyCredentialResponse

        The model defined in huaweicloud sdk

        :param agency_type: 委托类型：TABLE_SERVICE_TRUST-表服务委托。
        :type agency_type: str
        :param agency_name: 委托名称
        :type agency_name: str
        :param security_token: security token
        :type security_token: str
        :param expires_at: token到期时间
        :type expires_at: str
        :param issued_at: token下发时间
        :type issued_at: str
        :param access: ak
        :type access: str
        :param secret: sk
        :type secret: str
        """
        
        super().__init__()

        self._agency_type = None
        self._agency_name = None
        self._security_token = None
        self._expires_at = None
        self._issued_at = None
        self._access = None
        self._secret = None
        self.discriminator = None

        if agency_type is not None:
            self.agency_type = agency_type
        if agency_name is not None:
            self.agency_name = agency_name
        if security_token is not None:
            self.security_token = security_token
        if expires_at is not None:
            self.expires_at = expires_at
        if issued_at is not None:
            self.issued_at = issued_at
        if access is not None:
            self.access = access
        if secret is not None:
            self.secret = secret

    @property
    def agency_type(self):
        r"""Gets the agency_type of this ShowAgencyCredentialResponse.

        委托类型：TABLE_SERVICE_TRUST-表服务委托。

        :return: The agency_type of this ShowAgencyCredentialResponse.
        :rtype: str
        """
        return self._agency_type

    @agency_type.setter
    def agency_type(self, agency_type):
        r"""Sets the agency_type of this ShowAgencyCredentialResponse.

        委托类型：TABLE_SERVICE_TRUST-表服务委托。

        :param agency_type: The agency_type of this ShowAgencyCredentialResponse.
        :type agency_type: str
        """
        self._agency_type = agency_type

    @property
    def agency_name(self):
        r"""Gets the agency_name of this ShowAgencyCredentialResponse.

        委托名称

        :return: The agency_name of this ShowAgencyCredentialResponse.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        r"""Sets the agency_name of this ShowAgencyCredentialResponse.

        委托名称

        :param agency_name: The agency_name of this ShowAgencyCredentialResponse.
        :type agency_name: str
        """
        self._agency_name = agency_name

    @property
    def security_token(self):
        r"""Gets the security_token of this ShowAgencyCredentialResponse.

        security token

        :return: The security_token of this ShowAgencyCredentialResponse.
        :rtype: str
        """
        return self._security_token

    @security_token.setter
    def security_token(self, security_token):
        r"""Sets the security_token of this ShowAgencyCredentialResponse.

        security token

        :param security_token: The security_token of this ShowAgencyCredentialResponse.
        :type security_token: str
        """
        self._security_token = security_token

    @property
    def expires_at(self):
        r"""Gets the expires_at of this ShowAgencyCredentialResponse.

        token到期时间

        :return: The expires_at of this ShowAgencyCredentialResponse.
        :rtype: str
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        r"""Sets the expires_at of this ShowAgencyCredentialResponse.

        token到期时间

        :param expires_at: The expires_at of this ShowAgencyCredentialResponse.
        :type expires_at: str
        """
        self._expires_at = expires_at

    @property
    def issued_at(self):
        r"""Gets the issued_at of this ShowAgencyCredentialResponse.

        token下发时间

        :return: The issued_at of this ShowAgencyCredentialResponse.
        :rtype: str
        """
        return self._issued_at

    @issued_at.setter
    def issued_at(self, issued_at):
        r"""Sets the issued_at of this ShowAgencyCredentialResponse.

        token下发时间

        :param issued_at: The issued_at of this ShowAgencyCredentialResponse.
        :type issued_at: str
        """
        self._issued_at = issued_at

    @property
    def access(self):
        r"""Gets the access of this ShowAgencyCredentialResponse.

        ak

        :return: The access of this ShowAgencyCredentialResponse.
        :rtype: str
        """
        return self._access

    @access.setter
    def access(self, access):
        r"""Sets the access of this ShowAgencyCredentialResponse.

        ak

        :param access: The access of this ShowAgencyCredentialResponse.
        :type access: str
        """
        self._access = access

    @property
    def secret(self):
        r"""Gets the secret of this ShowAgencyCredentialResponse.

        sk

        :return: The secret of this ShowAgencyCredentialResponse.
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        r"""Sets the secret of this ShowAgencyCredentialResponse.

        sk

        :param secret: The secret of this ShowAgencyCredentialResponse.
        :type secret: str
        """
        self._secret = secret

    def to_dict(self):
        import warnings
        warnings.warn("ShowAgencyCredentialResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowAgencyCredentialResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
