# coding: utf-8

import pprint
import re

import six





class ShowServerRemoteConsoleRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'remote_console': 'GetServerRemoteConsoleOption'
    }

    attribute_map = {
        'remote_console': 'remote_console'
    }

    def __init__(self, remote_console=None):
        """ShowServerRemoteConsoleRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._remote_console = None
        self.discriminator = None

        self.remote_console = remote_console

    @property
    def remote_console(self):
        """Gets the remote_console of this ShowServerRemoteConsoleRequestBody.


        :return: The remote_console of this ShowServerRemoteConsoleRequestBody.
        :rtype: GetServerRemoteConsoleOption
        """
        return self._remote_console

    @remote_console.setter
    def remote_console(self, remote_console):
        """Sets the remote_console of this ShowServerRemoteConsoleRequestBody.


        :param remote_console: The remote_console of this ShowServerRemoteConsoleRequestBody.
        :type: GetServerRemoteConsoleOption
        """
        self._remote_console = remote_console

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
        if not isinstance(other, ShowServerRemoteConsoleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
