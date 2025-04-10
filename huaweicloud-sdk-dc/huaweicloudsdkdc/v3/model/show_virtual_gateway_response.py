# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowVirtualGatewayResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'virtual_gateway': 'VirtualGateway',
        'request_id': 'str'
    }

    attribute_map = {
        'virtual_gateway': 'virtual_gateway',
        'request_id': 'request_id'
    }

    def __init__(self, virtual_gateway=None, request_id=None):
        r"""ShowVirtualGatewayResponse

        The model defined in huaweicloud sdk

        :param virtual_gateway: 
        :type virtual_gateway: :class:`huaweicloudsdkdc.v3.VirtualGateway`
        :param request_id: 操作请求ID
        :type request_id: str
        """
        
        super(ShowVirtualGatewayResponse, self).__init__()

        self._virtual_gateway = None
        self._request_id = None
        self.discriminator = None

        if virtual_gateway is not None:
            self.virtual_gateway = virtual_gateway
        if request_id is not None:
            self.request_id = request_id

    @property
    def virtual_gateway(self):
        r"""Gets the virtual_gateway of this ShowVirtualGatewayResponse.

        :return: The virtual_gateway of this ShowVirtualGatewayResponse.
        :rtype: :class:`huaweicloudsdkdc.v3.VirtualGateway`
        """
        return self._virtual_gateway

    @virtual_gateway.setter
    def virtual_gateway(self, virtual_gateway):
        r"""Sets the virtual_gateway of this ShowVirtualGatewayResponse.

        :param virtual_gateway: The virtual_gateway of this ShowVirtualGatewayResponse.
        :type virtual_gateway: :class:`huaweicloudsdkdc.v3.VirtualGateway`
        """
        self._virtual_gateway = virtual_gateway

    @property
    def request_id(self):
        r"""Gets the request_id of this ShowVirtualGatewayResponse.

        操作请求ID

        :return: The request_id of this ShowVirtualGatewayResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ShowVirtualGatewayResponse.

        操作请求ID

        :param request_id: The request_id of this ShowVirtualGatewayResponse.
        :type request_id: str
        """
        self._request_id = request_id

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
        if not isinstance(other, ShowVirtualGatewayResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
