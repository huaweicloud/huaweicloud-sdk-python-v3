# coding: utf-8

import pprint
import re

import six





class DeleteVpcPeeringRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'peering_id': 'str'
    }

    attribute_map = {
        'peering_id': 'peering_id'
    }

    def __init__(self, peering_id=None):
        """DeleteVpcPeeringRequest - a model defined in huaweicloud sdk"""
        
        

        self._peering_id = None
        self.discriminator = None

        self.peering_id = peering_id

    @property
    def peering_id(self):
        """Gets the peering_id of this DeleteVpcPeeringRequest.


        :return: The peering_id of this DeleteVpcPeeringRequest.
        :rtype: str
        """
        return self._peering_id

    @peering_id.setter
    def peering_id(self, peering_id):
        """Sets the peering_id of this DeleteVpcPeeringRequest.


        :param peering_id: The peering_id of this DeleteVpcPeeringRequest.
        :type: str
        """
        self._peering_id = peering_id

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
        if not isinstance(other, DeleteVpcPeeringRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
