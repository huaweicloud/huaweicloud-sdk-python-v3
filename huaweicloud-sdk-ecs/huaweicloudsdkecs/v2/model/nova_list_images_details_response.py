# coding: utf-8

import pprint
import re

import six


class NovaListImagesDetailsResponse(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'images': 'list[NovaImage]'
    }

    attribute_map = {
        'images': 'images'
    }

    def __init__(self, images=None):  # noqa: E501
        """NovaListImagesDetailsResponse - a model defined in huaweicloud sdk"""

        self._images = None
        self.discriminator = None

        if images is not None:
            self.images = images

    @property
    def images(self):
        """Gets the images of this NovaListImagesDetailsResponse.

        镜像信息

        :return: The images of this NovaListImagesDetailsResponse.
        :rtype: list[NovaImage]
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this NovaListImagesDetailsResponse.

        镜像信息

        :param images: The images of this NovaListImagesDetailsResponse.
        :type: list[NovaImage]
        """
        self._images = images

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
        if not isinstance(other, NovaListImagesDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
