# coding: utf-8

import pprint
import re

import six





class CreateServerGroupRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'server_group': 'CreateServerGroupOption'
    }

    attribute_map = {
        'server_group': 'server_group'
    }

    def __init__(self, server_group=None):
        """CreateServerGroupRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._server_group = None
        self.discriminator = None

        self.server_group = server_group

    @property
    def server_group(self):
        """Gets the server_group of this CreateServerGroupRequestBody.


        :return: The server_group of this CreateServerGroupRequestBody.
        :rtype: CreateServerGroupOption
        """
        return self._server_group

    @server_group.setter
    def server_group(self, server_group):
        """Sets the server_group of this CreateServerGroupRequestBody.


        :param server_group: The server_group of this CreateServerGroupRequestBody.
        :type: CreateServerGroupOption
        """
        self._server_group = server_group

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
        if not isinstance(other, CreateServerGroupRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
