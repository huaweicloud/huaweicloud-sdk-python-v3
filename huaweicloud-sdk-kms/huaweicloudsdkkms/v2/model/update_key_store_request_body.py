# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateKeyStoreRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'proxy_access_key_id': 'str',
        'proxy_secret_access_key': 'str'
    }

    attribute_map = {
        'proxy_access_key_id': 'proxy_access_key_id',
        'proxy_secret_access_key': 'proxy_secret_access_key'
    }

    def __init__(self, proxy_access_key_id=None, proxy_secret_access_key=None):
        r"""UpdateKeyStoreRequestBody

        The model defined in huaweicloud sdk

        :param proxy_access_key_id: 访问XKS-Proxy的凭据ID
        :type proxy_access_key_id: str
        :param proxy_secret_access_key: 访问XKS-Proxy的凭据Key
        :type proxy_secret_access_key: str
        """
        
        

        self._proxy_access_key_id = None
        self._proxy_secret_access_key = None
        self.discriminator = None

        self.proxy_access_key_id = proxy_access_key_id
        self.proxy_secret_access_key = proxy_secret_access_key

    @property
    def proxy_access_key_id(self):
        r"""Gets the proxy_access_key_id of this UpdateKeyStoreRequestBody.

        访问XKS-Proxy的凭据ID

        :return: The proxy_access_key_id of this UpdateKeyStoreRequestBody.
        :rtype: str
        """
        return self._proxy_access_key_id

    @proxy_access_key_id.setter
    def proxy_access_key_id(self, proxy_access_key_id):
        r"""Sets the proxy_access_key_id of this UpdateKeyStoreRequestBody.

        访问XKS-Proxy的凭据ID

        :param proxy_access_key_id: The proxy_access_key_id of this UpdateKeyStoreRequestBody.
        :type proxy_access_key_id: str
        """
        self._proxy_access_key_id = proxy_access_key_id

    @property
    def proxy_secret_access_key(self):
        r"""Gets the proxy_secret_access_key of this UpdateKeyStoreRequestBody.

        访问XKS-Proxy的凭据Key

        :return: The proxy_secret_access_key of this UpdateKeyStoreRequestBody.
        :rtype: str
        """
        return self._proxy_secret_access_key

    @proxy_secret_access_key.setter
    def proxy_secret_access_key(self, proxy_secret_access_key):
        r"""Sets the proxy_secret_access_key of this UpdateKeyStoreRequestBody.

        访问XKS-Proxy的凭据Key

        :param proxy_secret_access_key: The proxy_secret_access_key of this UpdateKeyStoreRequestBody.
        :type proxy_secret_access_key: str
        """
        self._proxy_secret_access_key = proxy_secret_access_key

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
        if not isinstance(other, UpdateKeyStoreRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
