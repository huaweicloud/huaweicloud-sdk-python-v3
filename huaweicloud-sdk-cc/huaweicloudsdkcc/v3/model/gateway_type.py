# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GatewayType:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'gateway_type': 'str'
    }

    attribute_map = {
        'gateway_type': 'gateway_type'
    }

    def __init__(self, gateway_type=None):
        r"""GatewayType

        The model defined in huaweicloud sdk

        :param gateway_type: 网关的类型。GDGW：全球接入网关。
        :type gateway_type: str
        """
        
        

        self._gateway_type = None
        self.discriminator = None

        self.gateway_type = gateway_type

    @property
    def gateway_type(self):
        r"""Gets the gateway_type of this GatewayType.

        网关的类型。GDGW：全球接入网关。

        :return: The gateway_type of this GatewayType.
        :rtype: str
        """
        return self._gateway_type

    @gateway_type.setter
    def gateway_type(self, gateway_type):
        r"""Sets the gateway_type of this GatewayType.

        网关的类型。GDGW：全球接入网关。

        :param gateway_type: The gateway_type of this GatewayType.
        :type gateway_type: str
        """
        self._gateway_type = gateway_type

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
        if not isinstance(other, GatewayType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
