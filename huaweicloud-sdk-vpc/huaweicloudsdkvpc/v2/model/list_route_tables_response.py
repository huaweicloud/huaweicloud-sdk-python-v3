# coding: utf-8

import pprint
import re

import six


class ListRouteTablesResponse(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'routetables': 'list[RouteTableListResp]'
    }

    attribute_map = {
        'routetables': 'routetables'
    }

    def __init__(self, routetables=None):  # noqa: E501
        """ListRouteTablesResponse - a model defined in huaweicloud sdk"""

        self._routetables = None
        self.discriminator = None

        if routetables is not None:
            self.routetables = routetables

    @property
    def routetables(self):
        """Gets the routetables of this ListRouteTablesResponse.

        路由表对象列表

        :return: The routetables of this ListRouteTablesResponse.
        :rtype: list[RouteTableListResp]
        """
        return self._routetables

    @routetables.setter
    def routetables(self, routetables):
        """Sets the routetables of this ListRouteTablesResponse.

        路由表对象列表

        :param routetables: The routetables of this ListRouteTablesResponse.
        :type: list[RouteTableListResp]
        """
        self._routetables = routetables

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
        if not isinstance(other, ListRouteTablesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
