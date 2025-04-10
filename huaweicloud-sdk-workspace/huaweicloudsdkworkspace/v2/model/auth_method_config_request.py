# coding: utf-8

import six

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
        'auth_type': 'AuthTypeEnum',
        'radius_gateway_config': 'RadiusGatewayConfig',
        'third_party_auth_config': 'ThirdPartyAuthConfig',
        'emergency_login_mode': 'str'
    }

    attribute_map = {
        'auth_type': 'auth_type',
        'radius_gateway_config': 'radius_gateway_config',
        'third_party_auth_config': 'third_party_auth_config',
        'emergency_login_mode': 'emergency_login_mode'
    }

    def __init__(self, auth_type=None, radius_gateway_config=None, third_party_auth_config=None, emergency_login_mode=None):
        r"""AuthMethodConfigRequest

        The model defined in huaweicloud sdk

        :param auth_type: 
        :type auth_type: :class:`huaweicloudsdkworkspace.v2.AuthTypeEnum`
        :param radius_gateway_config: 
        :type radius_gateway_config: :class:`huaweicloudsdkworkspace.v2.RadiusGatewayConfig`
        :param third_party_auth_config: 
        :type third_party_auth_config: :class:`huaweicloudsdkworkspace.v2.ThirdPartyAuthConfig`
        :param emergency_login_mode: 应急登录模式。
        :type emergency_login_mode: str
        """
        
        

        self._auth_type = None
        self._radius_gateway_config = None
        self._third_party_auth_config = None
        self._emergency_login_mode = None
        self.discriminator = None

        if auth_type is not None:
            self.auth_type = auth_type
        if radius_gateway_config is not None:
            self.radius_gateway_config = radius_gateway_config
        if third_party_auth_config is not None:
            self.third_party_auth_config = third_party_auth_config
        if emergency_login_mode is not None:
            self.emergency_login_mode = emergency_login_mode

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
        if not isinstance(other, AuthMethodConfigRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
