# coding: utf-8

import pprint
import re

import six


class ListFpgaImagesRequest(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'page': 'int',
        'size': 'int'
    }

    attribute_map = {
        'page': 'page',
        'size': 'size'
    }

    def __init__(self, page=None, size=None):  # noqa: E501
        """ListFpgaImagesRequest - a model defined in huaweicloud sdk"""

        self._page = None
        self._size = None
        self.discriminator = None

        if page is not None:
            self.page = page
        if size is not None:
            self.size = size

    @property
    def page(self):
        """Gets the page of this ListFpgaImagesRequest.


        :return: The page of this ListFpgaImagesRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ListFpgaImagesRequest.


        :param page: The page of this ListFpgaImagesRequest.
        :type: int
        """
        self._page = page

    @property
    def size(self):
        """Gets the size of this ListFpgaImagesRequest.


        :return: The size of this ListFpgaImagesRequest.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ListFpgaImagesRequest.


        :param size: The size of this ListFpgaImagesRequest.
        :type: int
        """
        self._size = size

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
        if not isinstance(other, ListFpgaImagesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
