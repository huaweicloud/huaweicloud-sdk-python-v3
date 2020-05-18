# coding: utf-8

import pprint
import re

import six


class AssociateRouteTableAndSubnetReq(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'associate': 'list[str]',
        'disassociate': 'list[str]'
    }

    attribute_map = {
        'associate': 'associate',
        'disassociate': 'disassociate'
    }

    def __init__(self, associate=None, disassociate=None):  # noqa: E501
        """AssociateRouteTableAndSubnetReq - a model defined in huaweicloud sdk"""

        self._associate = None
        self._disassociate = None
        self.discriminator = None

        if associate is not None:
            self.associate = associate
        if disassociate is not None:
            self.disassociate = disassociate

    @property
    def associate(self):
        """Gets the associate of this AssociateRouteTableAndSubnetReq.

        路由表关联子网ID列表 

        :return: The associate of this AssociateRouteTableAndSubnetReq.
        :rtype: list[str]
        """
        return self._associate

    @associate.setter
    def associate(self, associate):
        """Sets the associate of this AssociateRouteTableAndSubnetReq.

        路由表关联子网ID列表 

        :param associate: The associate of this AssociateRouteTableAndSubnetReq.
        :type: list[str]
        """
        self._associate = associate

    @property
    def disassociate(self):
        """Gets the disassociate of this AssociateRouteTableAndSubnetReq.

        路由表解除关联子网ID列表

        :return: The disassociate of this AssociateRouteTableAndSubnetReq.
        :rtype: list[str]
        """
        return self._disassociate

    @disassociate.setter
    def disassociate(self, disassociate):
        """Sets the disassociate of this AssociateRouteTableAndSubnetReq.

        路由表解除关联子网ID列表

        :param disassociate: The disassociate of this AssociateRouteTableAndSubnetReq.
        :type: list[str]
        """
        self._disassociate = disassociate

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
        if not isinstance(other, AssociateRouteTableAndSubnetReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
