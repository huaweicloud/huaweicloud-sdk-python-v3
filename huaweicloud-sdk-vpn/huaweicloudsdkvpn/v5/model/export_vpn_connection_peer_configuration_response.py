# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportVpnConnectionPeerConfigurationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'peer_config': 'str',
        'header_response_token': 'str'
    }

    attribute_map = {
        'request_id': 'request_id',
        'peer_config': 'peer_config',
        'header_response_token': 'header-response-token'
    }

    def __init__(self, request_id=None, peer_config=None, header_response_token=None):
        r"""ExportVpnConnectionPeerConfigurationResponse

        The model defined in huaweicloud sdk

        :param request_id: 请求ID
        :type request_id: str
        :param peer_config: 对端配置
        :type peer_config: str
        :param header_response_token: 
        :type header_response_token: str
        """
        
        super().__init__()

        self._request_id = None
        self._peer_config = None
        self._header_response_token = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if peer_config is not None:
            self.peer_config = peer_config
        if header_response_token is not None:
            self.header_response_token = header_response_token

    @property
    def request_id(self):
        r"""Gets the request_id of this ExportVpnConnectionPeerConfigurationResponse.

        请求ID

        :return: The request_id of this ExportVpnConnectionPeerConfigurationResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ExportVpnConnectionPeerConfigurationResponse.

        请求ID

        :param request_id: The request_id of this ExportVpnConnectionPeerConfigurationResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def peer_config(self):
        r"""Gets the peer_config of this ExportVpnConnectionPeerConfigurationResponse.

        对端配置

        :return: The peer_config of this ExportVpnConnectionPeerConfigurationResponse.
        :rtype: str
        """
        return self._peer_config

    @peer_config.setter
    def peer_config(self, peer_config):
        r"""Sets the peer_config of this ExportVpnConnectionPeerConfigurationResponse.

        对端配置

        :param peer_config: The peer_config of this ExportVpnConnectionPeerConfigurationResponse.
        :type peer_config: str
        """
        self._peer_config = peer_config

    @property
    def header_response_token(self):
        r"""Gets the header_response_token of this ExportVpnConnectionPeerConfigurationResponse.

        :return: The header_response_token of this ExportVpnConnectionPeerConfigurationResponse.
        :rtype: str
        """
        return self._header_response_token

    @header_response_token.setter
    def header_response_token(self, header_response_token):
        r"""Sets the header_response_token of this ExportVpnConnectionPeerConfigurationResponse.

        :param header_response_token: The header_response_token of this ExportVpnConnectionPeerConfigurationResponse.
        :type header_response_token: str
        """
        self._header_response_token = header_response_token

    def to_dict(self):
        import warnings
        warnings.warn("ExportVpnConnectionPeerConfigurationResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ExportVpnConnectionPeerConfigurationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
