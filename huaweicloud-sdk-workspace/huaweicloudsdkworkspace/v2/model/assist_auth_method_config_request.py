# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssistAuthMethodConfigRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'auth_type': 'AuthAssistEnum',
        'otp_config_info': 'OtpConfigInfo',
        'radius_auth_config': 'RadiusAuthConfig',
        'radius_gateway_config': 'RadiusGatewayConfig'
    }

    attribute_map = {
        'auth_type': 'auth_type',
        'otp_config_info': 'otp_config_info',
        'radius_auth_config': 'radius_auth_config',
        'radius_gateway_config': 'radius_gateway_config'
    }

    def __init__(self, auth_type=None, otp_config_info=None, radius_auth_config=None, radius_gateway_config=None):
        """AssistAuthMethodConfigRequest

        The model defined in huaweicloud sdk

        :param auth_type: 
        :type auth_type: :class:`huaweicloudsdkworkspace.v2.AuthAssistEnum`
        :param otp_config_info: 
        :type otp_config_info: :class:`huaweicloudsdkworkspace.v2.OtpConfigInfo`
        :param radius_auth_config: 
        :type radius_auth_config: :class:`huaweicloudsdkworkspace.v2.RadiusAuthConfig`
        :param radius_gateway_config: 
        :type radius_gateway_config: :class:`huaweicloudsdkworkspace.v2.RadiusGatewayConfig`
        """
        
        

        self._auth_type = None
        self._otp_config_info = None
        self._radius_auth_config = None
        self._radius_gateway_config = None
        self.discriminator = None

        if auth_type is not None:
            self.auth_type = auth_type
        if otp_config_info is not None:
            self.otp_config_info = otp_config_info
        if radius_auth_config is not None:
            self.radius_auth_config = radius_auth_config
        if radius_gateway_config is not None:
            self.radius_gateway_config = radius_gateway_config

    @property
    def auth_type(self):
        """Gets the auth_type of this AssistAuthMethodConfigRequest.

        :return: The auth_type of this AssistAuthMethodConfigRequest.
        :rtype: :class:`huaweicloudsdkworkspace.v2.AuthAssistEnum`
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        """Sets the auth_type of this AssistAuthMethodConfigRequest.

        :param auth_type: The auth_type of this AssistAuthMethodConfigRequest.
        :type auth_type: :class:`huaweicloudsdkworkspace.v2.AuthAssistEnum`
        """
        self._auth_type = auth_type

    @property
    def otp_config_info(self):
        """Gets the otp_config_info of this AssistAuthMethodConfigRequest.

        :return: The otp_config_info of this AssistAuthMethodConfigRequest.
        :rtype: :class:`huaweicloudsdkworkspace.v2.OtpConfigInfo`
        """
        return self._otp_config_info

    @otp_config_info.setter
    def otp_config_info(self, otp_config_info):
        """Sets the otp_config_info of this AssistAuthMethodConfigRequest.

        :param otp_config_info: The otp_config_info of this AssistAuthMethodConfigRequest.
        :type otp_config_info: :class:`huaweicloudsdkworkspace.v2.OtpConfigInfo`
        """
        self._otp_config_info = otp_config_info

    @property
    def radius_auth_config(self):
        """Gets the radius_auth_config of this AssistAuthMethodConfigRequest.

        :return: The radius_auth_config of this AssistAuthMethodConfigRequest.
        :rtype: :class:`huaweicloudsdkworkspace.v2.RadiusAuthConfig`
        """
        return self._radius_auth_config

    @radius_auth_config.setter
    def radius_auth_config(self, radius_auth_config):
        """Sets the radius_auth_config of this AssistAuthMethodConfigRequest.

        :param radius_auth_config: The radius_auth_config of this AssistAuthMethodConfigRequest.
        :type radius_auth_config: :class:`huaweicloudsdkworkspace.v2.RadiusAuthConfig`
        """
        self._radius_auth_config = radius_auth_config

    @property
    def radius_gateway_config(self):
        """Gets the radius_gateway_config of this AssistAuthMethodConfigRequest.

        :return: The radius_gateway_config of this AssistAuthMethodConfigRequest.
        :rtype: :class:`huaweicloudsdkworkspace.v2.RadiusGatewayConfig`
        """
        return self._radius_gateway_config

    @radius_gateway_config.setter
    def radius_gateway_config(self, radius_gateway_config):
        """Sets the radius_gateway_config of this AssistAuthMethodConfigRequest.

        :param radius_gateway_config: The radius_gateway_config of this AssistAuthMethodConfigRequest.
        :type radius_gateway_config: :class:`huaweicloudsdkworkspace.v2.RadiusGatewayConfig`
        """
        self._radius_gateway_config = radius_gateway_config

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
        if not isinstance(other, AssistAuthMethodConfigRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
