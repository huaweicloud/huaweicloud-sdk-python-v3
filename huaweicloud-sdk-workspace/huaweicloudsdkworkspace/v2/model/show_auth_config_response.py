# coding: utf-8

import six

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
        'auth_type': 'str',
        'enable': 'bool',
        'radius_gateway_config': 'RadiusGatewayConfigInfo',
        'third_party_auth_config': 'list[ThirdPartyAuthConfig]',
        'emergency_login_mode': 'str'
    }

    attribute_map = {
        'auth_type': 'auth_type',
        'enable': 'enable',
        'radius_gateway_config': 'radius_gateway_config',
        'third_party_auth_config': 'third_party_auth_config',
        'emergency_login_mode': 'emergency_login_mode'
    }

    def __init__(self, auth_type=None, enable=None, radius_gateway_config=None, third_party_auth_config=None, emergency_login_mode=None):
        r"""ShowAuthConfigResponse

        The model defined in huaweicloud sdk

        :param auth_type: 认证类型 LOCAL_PASSWORD：本地密码认证模式 KERBEROS：Windows AD认证模式 LDAP：第三方LDAP模式 CLIENT_TOKEN：金审UKEY客户端Token认证模式 OAUTH2：第三方单点登录模式
        :type auth_type: str
        :param enable: 当前状态。
        :type enable: bool
        :param radius_gateway_config: 
        :type radius_gateway_config: :class:`huaweicloudsdkworkspace.v2.RadiusGatewayConfigInfo`
        :param third_party_auth_config: 第三方认证接口配置信息。
        :type third_party_auth_config: list[:class:`huaweicloudsdkworkspace.v2.ThirdPartyAuthConfig`]
        :param emergency_login_mode: 应急登录模式。
        :type emergency_login_mode: str
        """
        
        super(ShowAuthConfigResponse, self).__init__()

        self._auth_type = None
        self._enable = None
        self._radius_gateway_config = None
        self._third_party_auth_config = None
        self._emergency_login_mode = None
        self.discriminator = None

        if auth_type is not None:
            self.auth_type = auth_type
        if enable is not None:
            self.enable = enable
        if radius_gateway_config is not None:
            self.radius_gateway_config = radius_gateway_config
        if third_party_auth_config is not None:
            self.third_party_auth_config = third_party_auth_config
        if emergency_login_mode is not None:
            self.emergency_login_mode = emergency_login_mode

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
        if not isinstance(other, ShowAuthConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
