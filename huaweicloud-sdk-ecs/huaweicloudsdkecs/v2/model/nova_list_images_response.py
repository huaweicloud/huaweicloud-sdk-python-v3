# coding: utf-8

import pprint
import re

import six


class NovaListImagesResponse(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'images': 'list[NovaSimpleImage]',
        'images_links': 'list[NovaLink]'
    }

    attribute_map = {
        'images': 'images',
        'images_links': 'images_links'
    }

    def __init__(self, images=None, images_links=None):  # noqa: E501
        """NovaListImagesResponse - a model defined in huaweicloud sdk"""

        self._images = None
        self._images_links = None
        self.discriminator = None

        if images is not None:
            self.images = images
        if images_links is not None:
            self.images_links = images_links

    @property
    def images(self):
        """Gets the images of this NovaListImagesResponse.

        镜像信息

        :return: The images of this NovaListImagesResponse.
        :rtype: list[NovaSimpleImage]
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this NovaListImagesResponse.

        镜像信息

        :param images: The images of this NovaListImagesResponse.
        :type: list[NovaSimpleImage]
        """
        self._images = images

    @property
    def images_links(self):
        """Gets the images_links of this NovaListImagesResponse.

        分页查询时下一页的信息

        :return: The images_links of this NovaListImagesResponse.
        :rtype: list[NovaLink]
        """
        return self._images_links

    @images_links.setter
    def images_links(self, images_links):
        """Sets the images_links of this NovaListImagesResponse.

        分页查询时下一页的信息

        :param images_links: The images_links of this NovaListImagesResponse.
        :type: list[NovaLink]
        """
        self._images_links = images_links

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
        if not isinstance(other, NovaListImagesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
