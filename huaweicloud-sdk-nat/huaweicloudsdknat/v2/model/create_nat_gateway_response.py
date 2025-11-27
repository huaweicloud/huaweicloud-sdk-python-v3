# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateNatGatewayResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'nat_gateway': 'NatGatewayResponseBody',
        'order_id': 'str',
        'nat_gateway_id': 'str'
    }

    attribute_map = {
        'nat_gateway': 'nat_gateway',
        'order_id': 'order_id',
        'nat_gateway_id': 'nat_gateway_id'
    }

    def __init__(self, nat_gateway=None, order_id=None, nat_gateway_id=None):
        r"""CreateNatGatewayResponse

        The model defined in huaweicloud sdk

        :param nat_gateway: 
        :type nat_gateway: :class:`huaweicloudsdknat.v2.NatGatewayResponseBody`
        :param order_id: 订单ID。
        :type order_id: str
        :param nat_gateway_id: 公网NAT网关实例的ID。
        :type nat_gateway_id: str
        """
        
        super().__init__()

        self._nat_gateway = None
        self._order_id = None
        self._nat_gateway_id = None
        self.discriminator = None

        if nat_gateway is not None:
            self.nat_gateway = nat_gateway
        if order_id is not None:
            self.order_id = order_id
        if nat_gateway_id is not None:
            self.nat_gateway_id = nat_gateway_id

    @property
    def nat_gateway(self):
        r"""Gets the nat_gateway of this CreateNatGatewayResponse.

        :return: The nat_gateway of this CreateNatGatewayResponse.
        :rtype: :class:`huaweicloudsdknat.v2.NatGatewayResponseBody`
        """
        return self._nat_gateway

    @nat_gateway.setter
    def nat_gateway(self, nat_gateway):
        r"""Sets the nat_gateway of this CreateNatGatewayResponse.

        :param nat_gateway: The nat_gateway of this CreateNatGatewayResponse.
        :type nat_gateway: :class:`huaweicloudsdknat.v2.NatGatewayResponseBody`
        """
        self._nat_gateway = nat_gateway

    @property
    def order_id(self):
        r"""Gets the order_id of this CreateNatGatewayResponse.

        订单ID。

        :return: The order_id of this CreateNatGatewayResponse.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this CreateNatGatewayResponse.

        订单ID。

        :param order_id: The order_id of this CreateNatGatewayResponse.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def nat_gateway_id(self):
        r"""Gets the nat_gateway_id of this CreateNatGatewayResponse.

        公网NAT网关实例的ID。

        :return: The nat_gateway_id of this CreateNatGatewayResponse.
        :rtype: str
        """
        return self._nat_gateway_id

    @nat_gateway_id.setter
    def nat_gateway_id(self, nat_gateway_id):
        r"""Sets the nat_gateway_id of this CreateNatGatewayResponse.

        公网NAT网关实例的ID。

        :param nat_gateway_id: The nat_gateway_id of this CreateNatGatewayResponse.
        :type nat_gateway_id: str
        """
        self._nat_gateway_id = nat_gateway_id

    def to_dict(self):
        import warnings
        warnings.warn("CreateNatGatewayResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, CreateNatGatewayResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
