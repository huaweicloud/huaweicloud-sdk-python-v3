# coding: utf-8

import pprint
import re

import six


class NovaShowImageResponse(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'image': 'NovaImage'
    }

    attribute_map = {
        'image': 'image'
    }

    def __init__(self, image=None):  # noqa: E501
        """NovaShowImageResponse - a model defined in huaweicloud sdk"""

        self._image = None
        self.discriminator = None

        if image is not None:
            self.image = image

    @property
    def image(self):
        """Gets the image of this NovaShowImageResponse.


        :return: The image of this NovaShowImageResponse.
        :rtype: NovaImage
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this NovaShowImageResponse.


        :param image: The image of this NovaShowImageResponse.
        :type: NovaImage
        """
        self._image = image

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
        if not isinstance(other, NovaShowImageResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
