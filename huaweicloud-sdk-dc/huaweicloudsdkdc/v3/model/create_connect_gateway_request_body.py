# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateConnectGatewayRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'connect_gateway': 'CreateConnectGateway'
    }

    attribute_map = {
        'connect_gateway': 'connect_gateway'
    }

    def __init__(self, connect_gateway=None):
        r"""CreateConnectGatewayRequestBody

        The model defined in huaweicloud sdk

        :param connect_gateway: 
        :type connect_gateway: :class:`huaweicloudsdkdc.v3.CreateConnectGateway`
        """
        
        

        self._connect_gateway = None
        self.discriminator = None

        self.connect_gateway = connect_gateway

    @property
    def connect_gateway(self):
        r"""Gets the connect_gateway of this CreateConnectGatewayRequestBody.

        :return: The connect_gateway of this CreateConnectGatewayRequestBody.
        :rtype: :class:`huaweicloudsdkdc.v3.CreateConnectGateway`
        """
        return self._connect_gateway

    @connect_gateway.setter
    def connect_gateway(self, connect_gateway):
        r"""Sets the connect_gateway of this CreateConnectGatewayRequestBody.

        :param connect_gateway: The connect_gateway of this CreateConnectGatewayRequestBody.
        :type connect_gateway: :class:`huaweicloudsdkdc.v3.CreateConnectGateway`
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
        if not isinstance(other, CreateConnectGatewayRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
