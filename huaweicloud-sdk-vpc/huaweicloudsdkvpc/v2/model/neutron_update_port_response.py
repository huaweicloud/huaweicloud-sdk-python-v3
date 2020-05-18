# coding: utf-8

import pprint
import re

import six


class NeutronUpdatePortResponse(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'port': 'NeutronPort'
    }

    attribute_map = {
        'port': 'port'
    }

    def __init__(self, port=None):  # noqa: E501
        """NeutronUpdatePortResponse - a model defined in huaweicloud sdk"""

        self._port = None
        self.discriminator = None

        if port is not None:
            self.port = port

    @property
    def port(self):
        """Gets the port of this NeutronUpdatePortResponse.


        :return: The port of this NeutronUpdatePortResponse.
        :rtype: NeutronPort
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this NeutronUpdatePortResponse.


        :param port: The port of this NeutronUpdatePortResponse.
        :type: NeutronPort
        """
        self._port = port

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
        if not isinstance(other, NeutronUpdatePortResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
