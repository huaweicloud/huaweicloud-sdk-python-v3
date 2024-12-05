# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowGlobalDcGatewayResponse(SdkResponse):

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
        'global_dc_gateway': 'ExternalShowGlobalDcGateway',
        'x_request_id': 'str'
    }

    attribute_map = {
        'request_id': 'request_id',
        'global_dc_gateway': 'global_dc_gateway',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, request_id=None, global_dc_gateway=None, x_request_id=None):
        """ShowGlobalDcGatewayResponse

        The model defined in huaweicloud sdk

        :param request_id: 
        :type request_id: str
        :param global_dc_gateway: 
        :type global_dc_gateway: :class:`huaweicloudsdkdc.v3.ExternalShowGlobalDcGateway`
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ShowGlobalDcGatewayResponse, self).__init__()

        self._request_id = None
        self._global_dc_gateway = None
        self._x_request_id = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if global_dc_gateway is not None:
            self.global_dc_gateway = global_dc_gateway
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def request_id(self):
        """Gets the request_id of this ShowGlobalDcGatewayResponse.

        :return: The request_id of this ShowGlobalDcGatewayResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ShowGlobalDcGatewayResponse.

        :param request_id: The request_id of this ShowGlobalDcGatewayResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def global_dc_gateway(self):
        """Gets the global_dc_gateway of this ShowGlobalDcGatewayResponse.

        :return: The global_dc_gateway of this ShowGlobalDcGatewayResponse.
        :rtype: :class:`huaweicloudsdkdc.v3.ExternalShowGlobalDcGateway`
        """
        return self._global_dc_gateway

    @global_dc_gateway.setter
    def global_dc_gateway(self, global_dc_gateway):
        """Sets the global_dc_gateway of this ShowGlobalDcGatewayResponse.

        :param global_dc_gateway: The global_dc_gateway of this ShowGlobalDcGatewayResponse.
        :type global_dc_gateway: :class:`huaweicloudsdkdc.v3.ExternalShowGlobalDcGateway`
        """
        self._global_dc_gateway = global_dc_gateway

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ShowGlobalDcGatewayResponse.

        :return: The x_request_id of this ShowGlobalDcGatewayResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ShowGlobalDcGatewayResponse.

        :param x_request_id: The x_request_id of this ShowGlobalDcGatewayResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ShowGlobalDcGatewayResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
