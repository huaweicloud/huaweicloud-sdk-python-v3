# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateCentralNetworkGdgwAttachmentResponse(SdkResponse):

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
        'central_network_gdgw_attachment': 'CentralNetworkGdgwAttachment'
    }

    attribute_map = {
        'request_id': 'request_id',
        'central_network_gdgw_attachment': 'central_network_gdgw_attachment'
    }

    def __init__(self, request_id=None, central_network_gdgw_attachment=None):
        """UpdateCentralNetworkGdgwAttachmentResponse

        The model defined in huaweicloud sdk

        :param request_id: 资源ID标识符。
        :type request_id: str
        :param central_network_gdgw_attachment: 
        :type central_network_gdgw_attachment: :class:`huaweicloudsdkcc.v3.CentralNetworkGdgwAttachment`
        """
        
        super(UpdateCentralNetworkGdgwAttachmentResponse, self).__init__()

        self._request_id = None
        self._central_network_gdgw_attachment = None
        self.discriminator = None

        self.request_id = request_id
        self.central_network_gdgw_attachment = central_network_gdgw_attachment

    @property
    def request_id(self):
        """Gets the request_id of this UpdateCentralNetworkGdgwAttachmentResponse.

        资源ID标识符。

        :return: The request_id of this UpdateCentralNetworkGdgwAttachmentResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this UpdateCentralNetworkGdgwAttachmentResponse.

        资源ID标识符。

        :param request_id: The request_id of this UpdateCentralNetworkGdgwAttachmentResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def central_network_gdgw_attachment(self):
        """Gets the central_network_gdgw_attachment of this UpdateCentralNetworkGdgwAttachmentResponse.

        :return: The central_network_gdgw_attachment of this UpdateCentralNetworkGdgwAttachmentResponse.
        :rtype: :class:`huaweicloudsdkcc.v3.CentralNetworkGdgwAttachment`
        """
        return self._central_network_gdgw_attachment

    @central_network_gdgw_attachment.setter
    def central_network_gdgw_attachment(self, central_network_gdgw_attachment):
        """Sets the central_network_gdgw_attachment of this UpdateCentralNetworkGdgwAttachmentResponse.

        :param central_network_gdgw_attachment: The central_network_gdgw_attachment of this UpdateCentralNetworkGdgwAttachmentResponse.
        :type central_network_gdgw_attachment: :class:`huaweicloudsdkcc.v3.CentralNetworkGdgwAttachment`
        """
        self._central_network_gdgw_attachment = central_network_gdgw_attachment

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
        if not isinstance(other, UpdateCentralNetworkGdgwAttachmentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
