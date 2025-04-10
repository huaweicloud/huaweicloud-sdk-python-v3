# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateConnectGatewayResponse(SdkResponse):

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
        'connect_gateway': 'ConnectGatewayResponse'
    }

    attribute_map = {
        'request_id': 'request_id',
        'connect_gateway': 'connect_gateway'
    }

    def __init__(self, request_id=None, connect_gateway=None):
        r"""CreateConnectGatewayResponse

        The model defined in huaweicloud sdk

        :param request_id: 请求ID
        :type request_id: str
        :param connect_gateway: 
        :type connect_gateway: :class:`huaweicloudsdkdc.v3.ConnectGatewayResponse`
        """
        
        super(CreateConnectGatewayResponse, self).__init__()

        self._request_id = None
        self._connect_gateway = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if connect_gateway is not None:
            self.connect_gateway = connect_gateway

    @property
    def request_id(self):
        r"""Gets the request_id of this CreateConnectGatewayResponse.

        请求ID

        :return: The request_id of this CreateConnectGatewayResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this CreateConnectGatewayResponse.

        请求ID

        :param request_id: The request_id of this CreateConnectGatewayResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def connect_gateway(self):
        r"""Gets the connect_gateway of this CreateConnectGatewayResponse.

        :return: The connect_gateway of this CreateConnectGatewayResponse.
        :rtype: :class:`huaweicloudsdkdc.v3.ConnectGatewayResponse`
        """
        return self._connect_gateway

    @connect_gateway.setter
    def connect_gateway(self, connect_gateway):
        r"""Sets the connect_gateway of this CreateConnectGatewayResponse.

        :param connect_gateway: The connect_gateway of this CreateConnectGatewayResponse.
        :type connect_gateway: :class:`huaweicloudsdkdc.v3.ConnectGatewayResponse`
        """
        self._connect_gateway = connect_gateway

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
        if not isinstance(other, CreateConnectGatewayResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
