# coding: utf-8

import pprint
import re

import six





class UpdateNatGatewayRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'nat_gateway_id': 'str',
        'body': 'UpdateNatGatewayRequestBody'
    }

    attribute_map = {
        'nat_gateway_id': 'nat_gateway_id',
        'body': 'body'
    }

    def __init__(self, nat_gateway_id=None, body=None):
        """UpdateNatGatewayRequest - a model defined in huaweicloud sdk"""
        
        

        self._nat_gateway_id = None
        self._body = None
        self.discriminator = None

        self.nat_gateway_id = nat_gateway_id
        if body is not None:
            self.body = body

    @property
    def nat_gateway_id(self):
        """Gets the nat_gateway_id of this UpdateNatGatewayRequest.


        :return: The nat_gateway_id of this UpdateNatGatewayRequest.
        :rtype: str
        """
        return self._nat_gateway_id

    @nat_gateway_id.setter
    def nat_gateway_id(self, nat_gateway_id):
        """Sets the nat_gateway_id of this UpdateNatGatewayRequest.


        :param nat_gateway_id: The nat_gateway_id of this UpdateNatGatewayRequest.
        :type: str
        """
        self._nat_gateway_id = nat_gateway_id

    @property
    def body(self):
        """Gets the body of this UpdateNatGatewayRequest.


        :return: The body of this UpdateNatGatewayRequest.
        :rtype: UpdateNatGatewayRequestBody
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateNatGatewayRequest.


        :param body: The body of this UpdateNatGatewayRequest.
        :type: UpdateNatGatewayRequestBody
        """
        self._body = body

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
        if not isinstance(other, UpdateNatGatewayRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
