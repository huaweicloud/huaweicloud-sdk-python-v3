# coding: utf-8

import pprint
import re

import six


class NovaShowServerConsoleLogsResponse(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'output': 'str'
    }

    attribute_map = {
        'output': 'output'
    }

    def __init__(self, output=None):  # noqa: E501
        """NovaShowServerConsoleLogsResponse - a model defined in huaweicloud sdk"""

        self._output = None
        self.discriminator = None

        if output is not None:
            self.output = output

    @property
    def output(self):
        """Gets the output of this NovaShowServerConsoleLogsResponse.

        控制台输出为字符串。控制字符将被转义以创建有效的JSON字符串。

        :return: The output of this NovaShowServerConsoleLogsResponse.
        :rtype: str
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this NovaShowServerConsoleLogsResponse.

        控制台输出为字符串。控制字符将被转义以创建有效的JSON字符串。

        :param output: The output of this NovaShowServerConsoleLogsResponse.
        :type: str
        """
        self._output = output

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
        if not isinstance(other, NovaShowServerConsoleLogsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
