# coding: utf-8

import pprint
import re

import six


class ListVpcRoutesResponse(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'routes': 'list[VpcRoute]'
    }

    attribute_map = {
        'routes': 'routes'
    }

    def __init__(self, routes=None):  # noqa: E501
        """ListVpcRoutesResponse - a model defined in huaweicloud sdk"""

        self._routes = None
        self.discriminator = None

        if routes is not None:
            self.routes = routes

    @property
    def routes(self):
        """Gets the routes of this ListVpcRoutesResponse.

        route对象列表

        :return: The routes of this ListVpcRoutesResponse.
        :rtype: list[VpcRoute]
        """
        return self._routes

    @routes.setter
    def routes(self, routes):
        """Sets the routes of this ListVpcRoutesResponse.

        route对象列表

        :param routes: The routes of this ListVpcRoutesResponse.
        :type: list[VpcRoute]
        """
        self._routes = routes

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
        if not isinstance(other, ListVpcRoutesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
