# coding: utf-8

import pprint
import re

import six


class UpdateRoutetableReqBody(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'routetable': 'UpdateRouteTableReq'
    }

    attribute_map = {
        'routetable': 'routetable'
    }

    def __init__(self, routetable=None):  # noqa: E501
        """UpdateRoutetableReqBody - a model defined in huaweicloud sdk"""

        self._routetable = None
        self.discriminator = None

        self.routetable = routetable

    @property
    def routetable(self):
        """Gets the routetable of this UpdateRoutetableReqBody.


        :return: The routetable of this UpdateRoutetableReqBody.
        :rtype: UpdateRouteTableReq
        """
        return self._routetable

    @routetable.setter
    def routetable(self, routetable):
        """Sets the routetable of this UpdateRoutetableReqBody.


        :param routetable: The routetable of this UpdateRoutetableReqBody.
        :type: UpdateRouteTableReq
        """
        self._routetable = routetable

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
        if not isinstance(other, UpdateRoutetableReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
