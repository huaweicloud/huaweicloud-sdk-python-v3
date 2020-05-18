# coding: utf-8

import pprint
import re

import six


class NovaListServerActionsResponse(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'instance_actions': 'list[NovaServerAction]'
    }

    attribute_map = {
        'instance_actions': 'instanceActions'
    }

    def __init__(self, instance_actions=None):  # noqa: E501
        """NovaListServerActionsResponse - a model defined in huaweicloud sdk"""

        self._instance_actions = None
        self.discriminator = None

        if instance_actions is not None:
            self.instance_actions = instance_actions

    @property
    def instance_actions(self):
        """Gets the instance_actions of this NovaListServerActionsResponse.

        云服务器操作行为列表。

        :return: The instance_actions of this NovaListServerActionsResponse.
        :rtype: list[NovaServerAction]
        """
        return self._instance_actions

    @instance_actions.setter
    def instance_actions(self, instance_actions):
        """Sets the instance_actions of this NovaListServerActionsResponse.

        云服务器操作行为列表。

        :param instance_actions: The instance_actions of this NovaListServerActionsResponse.
        :type: list[NovaServerAction]
        """
        self._instance_actions = instance_actions

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
        if not isinstance(other, NovaListServerActionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
