# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoreRunAuthorizerConfiguration:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'custom_jwt': 'CoreRunCustomJWTAuthorizerConfiguration',
        'key_auth': 'CoreRunKeyAuthAuthorizerConfiguration'
    }

    attribute_map = {
        'custom_jwt': 'custom_jwt',
        'key_auth': 'key_auth'
    }

    def __init__(self, custom_jwt=None, key_auth=None):
        r"""CoreRunAuthorizerConfiguration

        The model defined in huaweicloud sdk

        :param custom_jwt: 
        :type custom_jwt: :class:`huaweicloudsdkagentarts.v1.CoreRunCustomJWTAuthorizerConfiguration`
        :param key_auth: 
        :type key_auth: :class:`huaweicloudsdkagentarts.v1.CoreRunKeyAuthAuthorizerConfiguration`
        """
        
        

        self._custom_jwt = None
        self._key_auth = None
        self.discriminator = None

        if custom_jwt is not None:
            self.custom_jwt = custom_jwt
        if key_auth is not None:
            self.key_auth = key_auth

    @property
    def custom_jwt(self):
        r"""Gets the custom_jwt of this CoreRunAuthorizerConfiguration.

        :return: The custom_jwt of this CoreRunAuthorizerConfiguration.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreRunCustomJWTAuthorizerConfiguration`
        """
        return self._custom_jwt

    @custom_jwt.setter
    def custom_jwt(self, custom_jwt):
        r"""Sets the custom_jwt of this CoreRunAuthorizerConfiguration.

        :param custom_jwt: The custom_jwt of this CoreRunAuthorizerConfiguration.
        :type custom_jwt: :class:`huaweicloudsdkagentarts.v1.CoreRunCustomJWTAuthorizerConfiguration`
        """
        self._custom_jwt = custom_jwt

    @property
    def key_auth(self):
        r"""Gets the key_auth of this CoreRunAuthorizerConfiguration.

        :return: The key_auth of this CoreRunAuthorizerConfiguration.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreRunKeyAuthAuthorizerConfiguration`
        """
        return self._key_auth

    @key_auth.setter
    def key_auth(self, key_auth):
        r"""Sets the key_auth of this CoreRunAuthorizerConfiguration.

        :param key_auth: The key_auth of this CoreRunAuthorizerConfiguration.
        :type key_auth: :class:`huaweicloudsdkagentarts.v1.CoreRunKeyAuthAuthorizerConfiguration`
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
        if not isinstance(other, CoreRunAuthorizerConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
