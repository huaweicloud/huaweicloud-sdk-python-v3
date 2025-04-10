# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateVpnConnectionsLogConfigResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'log_config': 'ConnectionsLogConfig',
        'request_id': 'str',
        'header_response_token': 'str'
    }

    attribute_map = {
        'log_config': 'log_config',
        'request_id': 'request_id',
        'header_response_token': 'header-response-token'
    }

    def __init__(self, log_config=None, request_id=None, header_response_token=None):
        r"""UpdateVpnConnectionsLogConfigResponse

        The model defined in huaweicloud sdk

        :param log_config: 
        :type log_config: :class:`huaweicloudsdkvpn.v5.ConnectionsLogConfig`
        :param request_id: 请求id
        :type request_id: str
        :param header_response_token: 
        :type header_response_token: str
        """
        
        super(UpdateVpnConnectionsLogConfigResponse, self).__init__()

        self._log_config = None
        self._request_id = None
        self._header_response_token = None
        self.discriminator = None

        if log_config is not None:
            self.log_config = log_config
        if request_id is not None:
            self.request_id = request_id
        if header_response_token is not None:
            self.header_response_token = header_response_token

    @property
    def log_config(self):
        r"""Gets the log_config of this UpdateVpnConnectionsLogConfigResponse.

        :return: The log_config of this UpdateVpnConnectionsLogConfigResponse.
        :rtype: :class:`huaweicloudsdkvpn.v5.ConnectionsLogConfig`
        """
        return self._log_config

    @log_config.setter
    def log_config(self, log_config):
        r"""Sets the log_config of this UpdateVpnConnectionsLogConfigResponse.

        :param log_config: The log_config of this UpdateVpnConnectionsLogConfigResponse.
        :type log_config: :class:`huaweicloudsdkvpn.v5.ConnectionsLogConfig`
        """
        self._log_config = log_config

    @property
    def request_id(self):
        r"""Gets the request_id of this UpdateVpnConnectionsLogConfigResponse.

        请求id

        :return: The request_id of this UpdateVpnConnectionsLogConfigResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this UpdateVpnConnectionsLogConfigResponse.

        请求id

        :param request_id: The request_id of this UpdateVpnConnectionsLogConfigResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def header_response_token(self):
        r"""Gets the header_response_token of this UpdateVpnConnectionsLogConfigResponse.

        :return: The header_response_token of this UpdateVpnConnectionsLogConfigResponse.
        :rtype: str
        """
        return self._header_response_token

    @header_response_token.setter
    def header_response_token(self, header_response_token):
        r"""Sets the header_response_token of this UpdateVpnConnectionsLogConfigResponse.

        :param header_response_token: The header_response_token of this UpdateVpnConnectionsLogConfigResponse.
        :type header_response_token: str
        """
        self._header_response_token = header_response_token

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
        if not isinstance(other, UpdateVpnConnectionsLogConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
