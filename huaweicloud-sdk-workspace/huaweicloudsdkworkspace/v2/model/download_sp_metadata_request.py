# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DownloadSpMetadataRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'identity_provider': 'str',
        'access_server_address': 'str'
    }

    attribute_map = {
        'identity_provider': 'identity_provider',
        'access_server_address': 'access_server_address'
    }

    def __init__(self, identity_provider=None, access_server_address=None):
        r"""DownloadSpMetadataRequest

        The model defined in huaweicloud sdk

        :param identity_provider: 身份提供者名称。
        :type identity_provider: str
        :param access_server_address: 接入服务器地址。
        :type access_server_address: str
        """
        
        

        self._identity_provider = None
        self._access_server_address = None
        self.discriminator = None

        self.identity_provider = identity_provider
        self.access_server_address = access_server_address

    @property
    def identity_provider(self):
        r"""Gets the identity_provider of this DownloadSpMetadataRequest.

        身份提供者名称。

        :return: The identity_provider of this DownloadSpMetadataRequest.
        :rtype: str
        """
        return self._identity_provider

    @identity_provider.setter
    def identity_provider(self, identity_provider):
        r"""Sets the identity_provider of this DownloadSpMetadataRequest.

        身份提供者名称。

        :param identity_provider: The identity_provider of this DownloadSpMetadataRequest.
        :type identity_provider: str
        """
        self._identity_provider = identity_provider

    @property
    def access_server_address(self):
        r"""Gets the access_server_address of this DownloadSpMetadataRequest.

        接入服务器地址。

        :return: The access_server_address of this DownloadSpMetadataRequest.
        :rtype: str
        """
        return self._access_server_address

    @access_server_address.setter
    def access_server_address(self, access_server_address):
        r"""Sets the access_server_address of this DownloadSpMetadataRequest.

        接入服务器地址。

        :param access_server_address: The access_server_address of this DownloadSpMetadataRequest.
        :type access_server_address: str
        """
        self._access_server_address = access_server_address

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
        if not isinstance(other, DownloadSpMetadataRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
