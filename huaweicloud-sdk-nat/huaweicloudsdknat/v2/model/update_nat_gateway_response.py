# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class UpdateNatGatewayResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'nat_gateway': 'NatGatewayResponseBody'
    }

    attribute_map = {
        'nat_gateway': 'nat_gateway'
    }

    def __init__(self, nat_gateway=None):
        """UpdateNatGatewayResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._nat_gateway = None
        self.discriminator = None

        if nat_gateway is not None:
            self.nat_gateway = nat_gateway

    @property
    def nat_gateway(self):
        """Gets the nat_gateway of this UpdateNatGatewayResponse.


        :return: The nat_gateway of this UpdateNatGatewayResponse.
        :rtype: NatGatewayResponseBody
        """
        return self._nat_gateway

    @nat_gateway.setter
    def nat_gateway(self, nat_gateway):
        """Sets the nat_gateway of this UpdateNatGatewayResponse.


        :param nat_gateway: The nat_gateway of this UpdateNatGatewayResponse.
        :type: NatGatewayResponseBody
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateNatGatewayResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
