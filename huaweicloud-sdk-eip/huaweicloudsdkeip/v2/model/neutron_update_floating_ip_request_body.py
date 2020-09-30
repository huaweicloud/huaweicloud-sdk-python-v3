# coding: utf-8

import pprint
import re

import six





class NeutronUpdateFloatingIpRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'floatingip': 'UpdateFloatingIpOption'
    }

    attribute_map = {
        'floatingip': 'floatingip'
    }

    def __init__(self, floatingip=None):
        """NeutronUpdateFloatingIpRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._floatingip = None
        self.discriminator = None

        self.floatingip = floatingip

    @property
    def floatingip(self):
        """Gets the floatingip of this NeutronUpdateFloatingIpRequestBody.


        :return: The floatingip of this NeutronUpdateFloatingIpRequestBody.
        :rtype: UpdateFloatingIpOption
        """
        return self._floatingip

    @floatingip.setter
    def floatingip(self, floatingip):
        """Sets the floatingip of this NeutronUpdateFloatingIpRequestBody.


        :param floatingip: The floatingip of this NeutronUpdateFloatingIpRequestBody.
        :type: UpdateFloatingIpOption
        """
        self._floatingip = floatingip

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
        if not isinstance(other, NeutronUpdateFloatingIpRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
