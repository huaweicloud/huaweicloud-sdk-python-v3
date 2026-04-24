# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KeyAuthAuthorizerConfiguration:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'api_keys': 'list[ApiKeyInfo]'
    }

    attribute_map = {
        'api_keys': 'api_keys'
    }

    def __init__(self, api_keys=None):
        r"""KeyAuthAuthorizerConfiguration

        The model defined in huaweicloud sdk

        :param api_keys: 
        :type api_keys: list[:class:`huaweicloudsdkagentidentity.v1.ApiKeyInfo`]
        """
        
        

        self._api_keys = None
        self.discriminator = None

        self.api_keys = api_keys

    @property
    def api_keys(self):
        r"""Gets the api_keys of this KeyAuthAuthorizerConfiguration.

        :return: The api_keys of this KeyAuthAuthorizerConfiguration.
        :rtype: list[:class:`huaweicloudsdkagentidentity.v1.ApiKeyInfo`]
        """
        return self._api_keys

    @api_keys.setter
    def api_keys(self, api_keys):
        r"""Sets the api_keys of this KeyAuthAuthorizerConfiguration.

        :param api_keys: The api_keys of this KeyAuthAuthorizerConfiguration.
        :type api_keys: list[:class:`huaweicloudsdkagentidentity.v1.ApiKeyInfo`]
        """
        self._api_keys = api_keys

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
        if not isinstance(other, KeyAuthAuthorizerConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
