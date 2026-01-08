# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAuthConfigResponse(SdkResponse):

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
        'auth_type': 'str',
        'enable': 'bool',
        'is_multi_domain_authenticate_enabled': 'bool',
        'radius_gateway_config': 'RadiusGatewayConfigInfo',
        'third_party_auth_config': 'list[ThirdPartyAuthConfig]',
        'emergency_login_mode': 'str',
        'saml2_auth_config': 'Saml2AuthConfig'
    }

    attribute_map = {
        'id': 'id',
        'auth_type': 'auth_type',
        'enable': 'enable',
        'is_multi_domain_authenticate_enabled': 'is_multi_domain_authenticate_enabled',
        'radius_gateway_config': 'radius_gateway_config',
        'third_party_auth_config': 'third_party_auth_config',
        'emergency_login_mode': 'emergency_login_mode',
        'saml2_auth_config': 'saml2_auth_config'
    }

    def __init__(self, id=None, auth_type=None, enable=None, is_multi_domain_authenticate_enabled=None, radius_gateway_config=None, third_party_auth_config=None, emergency_login_mode=None, saml2_auth_config=None):
        r"""ShowAuthConfigResponse

        The model defined in huaweicloud sdk

        :param id: 认证配置ID。
        :type id: str
        :param auth_type: 认证类型 LOCAL_PASSWORD：本地密码认证模式 KERBEROS：Windows AD认证模式 LDAP：第三方LDAP模式 CLIENT_TOKEN：金审UKEY客户端Token认证模式 OAUTH2：第三方单点登录模式
        :type auth_type: str
        :param enable: 当前状态。
        :type enable: bool
        :param is_multi_domain_authenticate_enabled: 当前状态。
        :type is_multi_domain_authenticate_enabled: bool
        :param radius_gateway_config: 
        :type radius_gateway_config: :class:`huaweicloudsdkworkspace.v2.RadiusGatewayConfigInfo`
        :param third_party_auth_config: 第三方认证接口配置信息。
        :type third_party_auth_config: list[:class:`huaweicloudsdkworkspace.v2.ThirdPartyAuthConfig`]
        :param emergency_login_mode: 应急登录模式。
        :type emergency_login_mode: str
        :param saml2_auth_config: 
        :type saml2_auth_config: :class:`huaweicloudsdkworkspace.v2.Saml2AuthConfig`
        """
        
        super().__init__()

        self._id = None
        self._auth_type = None
        self._enable = None
        self._is_multi_domain_authenticate_enabled = None
        self._radius_gateway_config = None
        self._third_party_auth_config = None
        self._emergency_login_mode = None
        self._saml2_auth_config = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if auth_type is not None:
            self.auth_type = auth_type
        if enable is not None:
            self.enable = enable
        if is_multi_domain_authenticate_enabled is not None:
            self.is_multi_domain_authenticate_enabled = is_multi_domain_authenticate_enabled
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
        r"""Gets the id of this ShowAuthConfigResponse.

        认证配置ID。

        :return: The id of this ShowAuthConfigResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowAuthConfigResponse.

        认证配置ID。

        :param id: The id of this ShowAuthConfigResponse.
        :type id: str
        """
        self._id = id

    @property
    def auth_type(self):
        r"""Gets the auth_type of this ShowAuthConfigResponse.

        认证类型 LOCAL_PASSWORD：本地密码认证模式 KERBEROS：Windows AD认证模式 LDAP：第三方LDAP模式 CLIENT_TOKEN：金审UKEY客户端Token认证模式 OAUTH2：第三方单点登录模式

        :return: The auth_type of this ShowAuthConfigResponse.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        r"""Sets the auth_type of this ShowAuthConfigResponse.

        认证类型 LOCAL_PASSWORD：本地密码认证模式 KERBEROS：Windows AD认证模式 LDAP：第三方LDAP模式 CLIENT_TOKEN：金审UKEY客户端Token认证模式 OAUTH2：第三方单点登录模式

        :param auth_type: The auth_type of this ShowAuthConfigResponse.
        :type auth_type: str
        """
        self._auth_type = auth_type

    @property
    def enable(self):
        r"""Gets the enable of this ShowAuthConfigResponse.

        当前状态。

        :return: The enable of this ShowAuthConfigResponse.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this ShowAuthConfigResponse.

        当前状态。

        :param enable: The enable of this ShowAuthConfigResponse.
        :type enable: bool
        """
        self._enable = enable

    @property
    def is_multi_domain_authenticate_enabled(self):
        r"""Gets the is_multi_domain_authenticate_enabled of this ShowAuthConfigResponse.

        当前状态。

        :return: The is_multi_domain_authenticate_enabled of this ShowAuthConfigResponse.
        :rtype: bool
        """
        return self._is_multi_domain_authenticate_enabled

    @is_multi_domain_authenticate_enabled.setter
    def is_multi_domain_authenticate_enabled(self, is_multi_domain_authenticate_enabled):
        r"""Sets the is_multi_domain_authenticate_enabled of this ShowAuthConfigResponse.

        当前状态。

        :param is_multi_domain_authenticate_enabled: The is_multi_domain_authenticate_enabled of this ShowAuthConfigResponse.
        :type is_multi_domain_authenticate_enabled: bool
        """
        self._is_multi_domain_authenticate_enabled = is_multi_domain_authenticate_enabled

    @property
    def radius_gateway_config(self):
        r"""Gets the radius_gateway_config of this ShowAuthConfigResponse.

        :return: The radius_gateway_config of this ShowAuthConfigResponse.
        :rtype: :class:`huaweicloudsdkworkspace.v2.RadiusGatewayConfigInfo`
        """
        return self._radius_gateway_config

    @radius_gateway_config.setter
    def radius_gateway_config(self, radius_gateway_config):
        r"""Sets the radius_gateway_config of this ShowAuthConfigResponse.

        :param radius_gateway_config: The radius_gateway_config of this ShowAuthConfigResponse.
        :type radius_gateway_config: :class:`huaweicloudsdkworkspace.v2.RadiusGatewayConfigInfo`
        """
        self._radius_gateway_config = radius_gateway_config

    @property
    def third_party_auth_config(self):
        r"""Gets the third_party_auth_config of this ShowAuthConfigResponse.

        第三方认证接口配置信息。

        :return: The third_party_auth_config of this ShowAuthConfigResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.ThirdPartyAuthConfig`]
        """
        return self._third_party_auth_config

    @third_party_auth_config.setter
    def third_party_auth_config(self, third_party_auth_config):
        r"""Sets the third_party_auth_config of this ShowAuthConfigResponse.

        第三方认证接口配置信息。

        :param third_party_auth_config: The third_party_auth_config of this ShowAuthConfigResponse.
        :type third_party_auth_config: list[:class:`huaweicloudsdkworkspace.v2.ThirdPartyAuthConfig`]
        """
        self._third_party_auth_config = third_party_auth_config

    @property
    def emergency_login_mode(self):
        r"""Gets the emergency_login_mode of this ShowAuthConfigResponse.

        应急登录模式。

        :return: The emergency_login_mode of this ShowAuthConfigResponse.
        :rtype: str
        """
        return self._emergency_login_mode

    @emergency_login_mode.setter
    def emergency_login_mode(self, emergency_login_mode):
        r"""Sets the emergency_login_mode of this ShowAuthConfigResponse.

        应急登录模式。

        :param emergency_login_mode: The emergency_login_mode of this ShowAuthConfigResponse.
        :type emergency_login_mode: str
        """
        self._emergency_login_mode = emergency_login_mode

    @property
    def saml2_auth_config(self):
        r"""Gets the saml2_auth_config of this ShowAuthConfigResponse.

        :return: The saml2_auth_config of this ShowAuthConfigResponse.
        :rtype: :class:`huaweicloudsdkworkspace.v2.Saml2AuthConfig`
        """
        return self._saml2_auth_config

    @saml2_auth_config.setter
    def saml2_auth_config(self, saml2_auth_config):
        r"""Sets the saml2_auth_config of this ShowAuthConfigResponse.

        :param saml2_auth_config: The saml2_auth_config of this ShowAuthConfigResponse.
        :type saml2_auth_config: :class:`huaweicloudsdkworkspace.v2.Saml2AuthConfig`
        """
        self._saml2_auth_config = saml2_auth_config

    def to_dict(self):
        import warnings
        warnings.warn("ShowAuthConfigResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowAuthConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
