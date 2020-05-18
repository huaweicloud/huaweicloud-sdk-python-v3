# coding: utf-8

import pprint
import re

import six


class NovaShowServerActionResponse(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'instance_action': 'NovaServerActionDetail'
    }

    attribute_map = {
        'instance_action': 'instanceAction'
    }

    def __init__(self, instance_action=None):  # noqa: E501
        """NovaShowServerActionResponse - a model defined in huaweicloud sdk"""

        self._instance_action = None
        self.discriminator = None

        if instance_action is not None:
            self.instance_action = instance_action

    @property
    def instance_action(self):
        """Gets the instance_action of this NovaShowServerActionResponse.


        :return: The instance_action of this NovaShowServerActionResponse.
        :rtype: NovaServerActionDetail
        """
        return self._instance_action

    @instance_action.setter
    def instance_action(self, instance_action):
        """Sets the instance_action of this NovaShowServerActionResponse.


        :param instance_action: The instance_action of this NovaShowServerActionResponse.
        :type: NovaServerActionDetail
        """
        self._instance_action = instance_action

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
        if not isinstance(other, NovaShowServerActionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
