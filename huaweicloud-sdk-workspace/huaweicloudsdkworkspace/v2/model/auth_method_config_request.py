# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AuthMethodConfigRequest:

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
        'is_multi_domain_authenticate_enabled': 'bool',
        'auth_type': 'AuthTypeEnum',
        'radius_gateway_config': 'RadiusGatewayConfig',
        'third_party_auth_config': 'ThirdPartyAuthConfig',
        'emergency_login_mode': 'str',
        'saml2_auth_config': 'Saml2AuthConfig'
    }

    attribute_map = {
        'id': 'id',
        'is_multi_domain_authenticate_enabled': 'is_multi_domain_authenticate_enabled',
        'auth_type': 'auth_type',
        'radius_gateway_config': 'radius_gateway_config',
        'third_party_auth_config': 'third_party_auth_config',
        'emergency_login_mode': 'emergency_login_mode',
        'saml2_auth_config': 'saml2_auth_config'
    }

    def __init__(self, id=None, is_multi_domain_authenticate_enabled=None, auth_type=None, radius_gateway_config=None, third_party_auth_config=None, emergency_login_mode=None, saml2_auth_config=None):
        r"""AuthMethodConfigRequest

        The model defined in huaweicloud sdk

        :param id: 认证配置id。
        :type id: str
        :param is_multi_domain_authenticate_enabled: 是否支持多域。
        :type is_multi_domain_authenticate_enabled: bool
        :param auth_type: 
        :type auth_type: :class:`huaweicloudsdkworkspace.v2.AuthTypeEnum`
        :param radius_gateway_config: 
        :type radius_gateway_config: :class:`huaweicloudsdkworkspace.v2.RadiusGatewayConfig`
        :param third_party_auth_config: 
        :type third_party_auth_config: :class:`huaweicloudsdkworkspace.v2.ThirdPartyAuthConfig`
        :param emergency_login_mode: 应急登录模式。
        :type emergency_login_mode: str
        :param saml2_auth_config: 
        :type saml2_auth_config: :class:`huaweicloudsdkworkspace.v2.Saml2AuthConfig`
        """
        
        

        self._id = None
        self._is_multi_domain_authenticate_enabled = None
        self._auth_type = None
        self._radius_gateway_config = None
        self._third_party_auth_config = None
        self._emergency_login_mode = None
        self._saml2_auth_config = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if is_multi_domain_authenticate_enabled is not None:
            self.is_multi_domain_authenticate_enabled = is_multi_domain_authenticate_enabled
        if auth_type is not None:
            self.auth_type = auth_type
        if radius_gateway_config is not None:
            self.radius_gateway_config = radius_gateway_config
        if third_party_auth_config is not None:
            self.third_party_auth_config = third_party_auth_config
        if emergency_login_mode is not None:
            self.emergency_login_mode = emergency_login_mode
        if saml2_auth_config is not None:
            self.saml2_auth_config = saml2_auth_config

    @property
    def id(self):
        r"""Gets the id of this AuthMethodConfigRequest.

        认证配置id。

        :return: The id of this AuthMethodConfigRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AuthMethodConfigRequest.

        认证配置id。

        :param id: The id of this AuthMethodConfigRequest.
        :type id: str
        """
        self._id = id

    @property
    def is_multi_domain_authenticate_enabled(self):
        r"""Gets the is_multi_domain_authenticate_enabled of this AuthMethodConfigRequest.

        是否支持多域。

        :return: The is_multi_domain_authenticate_enabled of this AuthMethodConfigRequest.
        :rtype: bool
        """
        return self._is_multi_domain_authenticate_enabled

    @is_multi_domain_authenticate_enabled.setter
    def is_multi_domain_authenticate_enabled(self, is_multi_domain_authenticate_enabled):
        r"""Sets the is_multi_domain_authenticate_enabled of this AuthMethodConfigRequest.

        是否支持多域。

        :param is_multi_domain_authenticate_enabled: The is_multi_domain_authenticate_enabled of this AuthMethodConfigRequest.
        :type is_multi_domain_authenticate_enabled: bool
        """
        self._is_multi_domain_authenticate_enabled = is_multi_domain_authenticate_enabled

    @property
    def auth_type(self):
        r"""Gets the auth_type of this AuthMethodConfigRequest.

        :return: The auth_type of this AuthMethodConfigRequest.
        :rtype: :class:`huaweicloudsdkworkspace.v2.AuthTypeEnum`
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        r"""Sets the auth_type of this AuthMethodConfigRequest.

        :param auth_type: The auth_type of this AuthMethodConfigRequest.
        :type auth_type: :class:`huaweicloudsdkworkspace.v2.AuthTypeEnum`
        """
        self._auth_type = auth_type

    @property
    def radius_gateway_config(self):
        r"""Gets the radius_gateway_config of this AuthMethodConfigRequest.

        :return: The radius_gateway_config of this AuthMethodConfigRequest.
        :rtype: :class:`huaweicloudsdkworkspace.v2.RadiusGatewayConfig`
        """
        return self._radius_gateway_config

    @radius_gateway_config.setter
    def radius_gateway_config(self, radius_gateway_config):
        r"""Sets the radius_gateway_config of this AuthMethodConfigRequest.

        :param radius_gateway_config: The radius_gateway_config of this AuthMethodConfigRequest.
        :type radius_gateway_config: :class:`huaweicloudsdkworkspace.v2.RadiusGatewayConfig`
        """
        self._radius_gateway_config = radius_gateway_config

    @property
    def third_party_auth_config(self):
        r"""Gets the third_party_auth_config of this AuthMethodConfigRequest.

        :return: The third_party_auth_config of this AuthMethodConfigRequest.
        :rtype: :class:`huaweicloudsdkworkspace.v2.ThirdPartyAuthConfig`
        """
        return self._third_party_auth_config

    @third_party_auth_config.setter
    def third_party_auth_config(self, third_party_auth_config):
        r"""Sets the third_party_auth_config of this AuthMethodConfigRequest.

        :param third_party_auth_config: The third_party_auth_config of this AuthMethodConfigRequest.
        :type third_party_auth_config: :class:`huaweicloudsdkworkspace.v2.ThirdPartyAuthConfig`
        """
        self._third_party_auth_config = third_party_auth_config

    @property
    def emergency_login_mode(self):
        r"""Gets the emergency_login_mode of this AuthMethodConfigRequest.

        应急登录模式。

        :return: The emergency_login_mode of this AuthMethodConfigRequest.
        :rtype: str
        """
        return self._emergency_login_mode

    @emergency_login_mode.setter
    def emergency_login_mode(self, emergency_login_mode):
        r"""Sets the emergency_login_mode of this AuthMethodConfigRequest.

        应急登录模式。

        :param emergency_login_mode: The emergency_login_mode of this AuthMethodConfigRequest.
        :type emergency_login_mode: str
        """
        self._emergency_login_mode = emergency_login_mode

    @property
    def saml2_auth_config(self):
        r"""Gets the saml2_auth_config of this AuthMethodConfigRequest.

        :return: The saml2_auth_config of this AuthMethodConfigRequest.
        :rtype: :class:`huaweicloudsdkworkspace.v2.Saml2AuthConfig`
        """
        return self._saml2_auth_config

    @saml2_auth_config.setter
    def saml2_auth_config(self, saml2_auth_config):
        r"""Sets the saml2_auth_config of this AuthMethodConfigRequest.

        :param saml2_auth_config: The saml2_auth_config of this AuthMethodConfigRequest.
        :type saml2_auth_config: :class:`huaweicloudsdkworkspace.v2.Saml2AuthConfig`
        """
        self._saml2_auth_config = saml2_auth_config

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
        if not isinstance(other, AuthMethodConfigRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
