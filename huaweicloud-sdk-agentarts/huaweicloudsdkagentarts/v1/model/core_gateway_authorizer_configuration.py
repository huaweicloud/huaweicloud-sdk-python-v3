# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoreGatewayAuthorizerConfiguration:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'custom_jwt_authorizer': 'CoreGatewayCustomJWTAuthorizerConfiguration',
        'key_auth': 'CoreGatewayKeyAuthAuthorizerConfiguration'
    }

    attribute_map = {
        'custom_jwt_authorizer': 'custom_jwt_authorizer',
        'key_auth': 'key_auth'
    }

    def __init__(self, custom_jwt_authorizer=None, key_auth=None):
        r"""CoreGatewayAuthorizerConfiguration

        The model defined in huaweicloud sdk

        :param custom_jwt_authorizer: 
        :type custom_jwt_authorizer: :class:`huaweicloudsdkagentarts.v1.CoreGatewayCustomJWTAuthorizerConfiguration`
        :param key_auth: 
        :type key_auth: :class:`huaweicloudsdkagentarts.v1.CoreGatewayKeyAuthAuthorizerConfiguration`
        """
        
        

        self._custom_jwt_authorizer = None
        self._key_auth = None
        self.discriminator = None

        if custom_jwt_authorizer is not None:
            self.custom_jwt_authorizer = custom_jwt_authorizer
        if key_auth is not None:
            self.key_auth = key_auth

    @property
    def custom_jwt_authorizer(self):
        r"""Gets the custom_jwt_authorizer of this CoreGatewayAuthorizerConfiguration.

        :return: The custom_jwt_authorizer of this CoreGatewayAuthorizerConfiguration.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreGatewayCustomJWTAuthorizerConfiguration`
        """
        return self._custom_jwt_authorizer

    @custom_jwt_authorizer.setter
    def custom_jwt_authorizer(self, custom_jwt_authorizer):
        r"""Sets the custom_jwt_authorizer of this CoreGatewayAuthorizerConfiguration.

        :param custom_jwt_authorizer: The custom_jwt_authorizer of this CoreGatewayAuthorizerConfiguration.
        :type custom_jwt_authorizer: :class:`huaweicloudsdkagentarts.v1.CoreGatewayCustomJWTAuthorizerConfiguration`
        """
        self._custom_jwt_authorizer = custom_jwt_authorizer

    @property
    def key_auth(self):
        r"""Gets the key_auth of this CoreGatewayAuthorizerConfiguration.

        :return: The key_auth of this CoreGatewayAuthorizerConfiguration.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreGatewayKeyAuthAuthorizerConfiguration`
        """
        return self._key_auth

    @key_auth.setter
    def key_auth(self, key_auth):
        r"""Sets the key_auth of this CoreGatewayAuthorizerConfiguration.

        :param key_auth: The key_auth of this CoreGatewayAuthorizerConfiguration.
        :type key_auth: :class:`huaweicloudsdkagentarts.v1.CoreGatewayKeyAuthAuthorizerConfiguration`
        """
        self._key_auth = key_auth

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
        if not isinstance(other, CoreGatewayAuthorizerConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
