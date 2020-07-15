# coding: utf-8

import pprint
import re

import six





class UpdateServerRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'server': 'UpdateServerOption'
    }

    attribute_map = {
        'server': 'server'
    }

    def __init__(self, server=None):
        """UpdateServerRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._server = None
        self.discriminator = None

        self.server = server

    @property
    def server(self):
        """Gets the server of this UpdateServerRequestBody.


        :return: The server of this UpdateServerRequestBody.
        :rtype: UpdateServerOption
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this UpdateServerRequestBody.


        :param server: The server of this UpdateServerRequestBody.
        :type: UpdateServerOption
        """
        self._server = server

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
        if not isinstance(other, UpdateServerRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
