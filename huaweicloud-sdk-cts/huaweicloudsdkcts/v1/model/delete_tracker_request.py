# coding: utf-8

import pprint
import re

import six


class DeleteTrackerRequest(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'tracker_name': 'str'
    }

    attribute_map = {
        'tracker_name': 'tracker_name'
    }

    def __init__(self, tracker_name=None):  # noqa: E501
        """DeleteTrackerRequest - a model defined in huaweicloud sdk"""

        self._tracker_name = None
        self.discriminator = None

        self.tracker_name = tracker_name

    @property
    def tracker_name(self):
        """Gets the tracker_name of this DeleteTrackerRequest.


        :return: The tracker_name of this DeleteTrackerRequest.
        :rtype: str
        """
        return self._tracker_name

    @tracker_name.setter
    def tracker_name(self, tracker_name):
        """Sets the tracker_name of this DeleteTrackerRequest.


        :param tracker_name: The tracker_name of this DeleteTrackerRequest.
        :type: str
        """
        self._tracker_name = tracker_name

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
        if not isinstance(other, DeleteTrackerRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
