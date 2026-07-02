# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoreGatewayApiKeyConfiguration:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'api_key_name': 'str',
        'api_key': 'str'
    }

    attribute_map = {
        'api_key_name': 'api_key_name',
        'api_key': 'api_key'
    }

    def __init__(self, api_key_name=None, api_key=None):
        r"""CoreGatewayApiKeyConfiguration

        The model defined in huaweicloud sdk

        :param api_key_name: API 密钥的资源名称。
        :type api_key_name: str
        :param api_key: API 密钥值。
        :type api_key: str
        """
        
        

        self._api_key_name = None
        self._api_key = None
        self.discriminator = None

        self.api_key_name = api_key_name
        if api_key is not None:
            self.api_key = api_key

    @property
    def api_key_name(self):
        r"""Gets the api_key_name of this CoreGatewayApiKeyConfiguration.

        API 密钥的资源名称。

        :return: The api_key_name of this CoreGatewayApiKeyConfiguration.
        :rtype: str
        """
        return self._api_key_name

    @api_key_name.setter
    def api_key_name(self, api_key_name):
        r"""Sets the api_key_name of this CoreGatewayApiKeyConfiguration.

        API 密钥的资源名称。

        :param api_key_name: The api_key_name of this CoreGatewayApiKeyConfiguration.
        :type api_key_name: str
        """
        self._api_key_name = api_key_name

    @property
    def api_key(self):
        r"""Gets the api_key of this CoreGatewayApiKeyConfiguration.

        API 密钥值。

        :return: The api_key of this CoreGatewayApiKeyConfiguration.
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        r"""Sets the api_key of this CoreGatewayApiKeyConfiguration.

        API 密钥值。

        :param api_key: The api_key of this CoreGatewayApiKeyConfiguration.
        :type api_key: str
        """
        self._api_key = api_key

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
        if not isinstance(other, CoreGatewayApiKeyConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
