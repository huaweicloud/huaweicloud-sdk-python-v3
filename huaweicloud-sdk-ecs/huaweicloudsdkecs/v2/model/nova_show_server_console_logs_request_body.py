# coding: utf-8

import pprint
import re

import six


class NovaShowServerConsoleLogsRequestBody(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'os_get_console_output': 'NovaGetServerConsoleLogOption'
    }

    attribute_map = {
        'os_get_console_output': 'os-getConsoleOutput'
    }

    def __init__(self, os_get_console_output=None):  # noqa: E501
        """NovaShowServerConsoleLogsRequestBody - a model defined in huaweicloud sdk"""

        self._os_get_console_output = None
        self.discriminator = None

        self.os_get_console_output = os_get_console_output

    @property
    def os_get_console_output(self):
        """Gets the os_get_console_output of this NovaShowServerConsoleLogsRequestBody.


        :return: The os_get_console_output of this NovaShowServerConsoleLogsRequestBody.
        :rtype: NovaGetServerConsoleLogOption
        """
        return self._os_get_console_output

    @os_get_console_output.setter
    def os_get_console_output(self, os_get_console_output):
        """Sets the os_get_console_output of this NovaShowServerConsoleLogsRequestBody.


        :param os_get_console_output: The os_get_console_output of this NovaShowServerConsoleLogsRequestBody.
        :type: NovaGetServerConsoleLogOption
        """
        self._os_get_console_output = os_get_console_output

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
        if not isinstance(other, NovaShowServerConsoleLogsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
