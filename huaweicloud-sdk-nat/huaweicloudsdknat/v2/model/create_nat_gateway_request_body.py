# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateNatGatewayRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'nat_gateway': 'CreateNatGatewayOption'
    }

    attribute_map = {
        'nat_gateway': 'nat_gateway'
    }

    def __init__(self, nat_gateway=None):
        r"""CreateNatGatewayRequestBody

        The model defined in huaweicloud sdk

        :param nat_gateway: 
        :type nat_gateway: :class:`huaweicloudsdknat.v2.CreateNatGatewayOption`
        """
        
        

        self._nat_gateway = None
        self.discriminator = None

        self.nat_gateway = nat_gateway

    @property
    def nat_gateway(self):
        r"""Gets the nat_gateway of this CreateNatGatewayRequestBody.

        :return: The nat_gateway of this CreateNatGatewayRequestBody.
        :rtype: :class:`huaweicloudsdknat.v2.CreateNatGatewayOption`
        """
        return self._nat_gateway

    @nat_gateway.setter
    def nat_gateway(self, nat_gateway):
        r"""Sets the nat_gateway of this CreateNatGatewayRequestBody.

        :param nat_gateway: The nat_gateway of this CreateNatGatewayRequestBody.
        :type nat_gateway: :class:`huaweicloudsdknat.v2.CreateNatGatewayOption`
        """
        self._nat_gateway = nat_gateway

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
        if not isinstance(other, CreateNatGatewayRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
