# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportClientConfigResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('client_config')

    openapi_types = {
        'client_config': 'str',
        'header_response_token': 'str'
    }

    attribute_map = {
        'client_config': 'client_config',
        'header_response_token': 'header-response-token'
    }

    def __init__(self, client_config=None, header_response_token=None):
        r"""ExportClientConfigResponse

        The model defined in huaweicloud sdk

        :param client_config: 客户端配置
        :type client_config: str
        :param header_response_token: 
        :type header_response_token: str
        """
        
        super(ExportClientConfigResponse, self).__init__()

        self._client_config = None
        self._header_response_token = None
        self.discriminator = None

        if client_config is not None:
            self.client_config = client_config
        if header_response_token is not None:
            self.header_response_token = header_response_token

    @property
    def client_config(self):
        r"""Gets the client_config of this ExportClientConfigResponse.

        客户端配置

        :return: The client_config of this ExportClientConfigResponse.
        :rtype: str
        """
        return self._client_config

    @client_config.setter
    def client_config(self, client_config):
        r"""Sets the client_config of this ExportClientConfigResponse.

        客户端配置

        :param client_config: The client_config of this ExportClientConfigResponse.
        :type client_config: str
        """
        self._client_config = client_config

    @property
    def header_response_token(self):
        r"""Gets the header_response_token of this ExportClientConfigResponse.

        :return: The header_response_token of this ExportClientConfigResponse.
        :rtype: str
        """
        return self._header_response_token

    @header_response_token.setter
    def header_response_token(self, header_response_token):
        r"""Sets the header_response_token of this ExportClientConfigResponse.

        :param header_response_token: The header_response_token of this ExportClientConfigResponse.
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
        if not isinstance(other, ExportClientConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
