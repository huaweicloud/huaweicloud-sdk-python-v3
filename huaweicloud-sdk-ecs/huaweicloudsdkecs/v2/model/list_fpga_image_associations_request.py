# coding: utf-8

import pprint
import re

import six


class ListFpgaImageAssociationsRequest(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'fpga_image_id': 'str',
        'image_id': 'str',
        'page': 'int'
    }

    attribute_map = {
        'fpga_image_id': 'fpga_image_id',
        'image_id': 'image_id',
        'page': 'page'
    }

    def __init__(self, fpga_image_id=None, image_id=None, page=None):  # noqa: E501
        """ListFpgaImageAssociationsRequest - a model defined in huaweicloud sdk"""

        self._fpga_image_id = None
        self._image_id = None
        self._page = None
        self.discriminator = None

        if fpga_image_id is not None:
            self.fpga_image_id = fpga_image_id
        if image_id is not None:
            self.image_id = image_id
        if page is not None:
            self.page = page

    @property
    def fpga_image_id(self):
        """Gets the fpga_image_id of this ListFpgaImageAssociationsRequest.


        :return: The fpga_image_id of this ListFpgaImageAssociationsRequest.
        :rtype: str
        """
        return self._fpga_image_id

    @fpga_image_id.setter
    def fpga_image_id(self, fpga_image_id):
        """Sets the fpga_image_id of this ListFpgaImageAssociationsRequest.


        :param fpga_image_id: The fpga_image_id of this ListFpgaImageAssociationsRequest.
        :type: str
        """
        self._fpga_image_id = fpga_image_id

    @property
    def image_id(self):
        """Gets the image_id of this ListFpgaImageAssociationsRequest.


        :return: The image_id of this ListFpgaImageAssociationsRequest.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this ListFpgaImageAssociationsRequest.


        :param image_id: The image_id of this ListFpgaImageAssociationsRequest.
        :type: str
        """
        self._image_id = image_id

    @property
    def page(self):
        """Gets the page of this ListFpgaImageAssociationsRequest.


        :return: The page of this ListFpgaImageAssociationsRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ListFpgaImageAssociationsRequest.


        :param page: The page of this ListFpgaImageAssociationsRequest.
        :type: int
        """
        self._page = page

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
        if not isinstance(other, ListFpgaImageAssociationsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
