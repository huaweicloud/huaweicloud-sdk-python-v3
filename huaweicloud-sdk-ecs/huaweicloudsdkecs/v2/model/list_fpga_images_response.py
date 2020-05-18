# coding: utf-8

import pprint
import re

import six


class ListFpgaImagesResponse(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'count': 'int',
        'fpgaimages': 'list[FpgaImage]'
    }

    attribute_map = {
        'count': 'count',
        'fpgaimages': 'fpgaimages'
    }

    def __init__(self, count=None, fpgaimages=None):  # noqa: E501
        """ListFpgaImagesResponse - a model defined in huaweicloud sdk"""

        self._count = None
        self._fpgaimages = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if fpgaimages is not None:
            self.fpgaimages = fpgaimages

    @property
    def count(self):
        """Gets the count of this ListFpgaImagesResponse.

        查询的FPGA镜像数量。

        :return: The count of this ListFpgaImagesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListFpgaImagesResponse.

        查询的FPGA镜像数量。

        :param count: The count of this ListFpgaImagesResponse.
        :type: int
        """
        self._count = count

    @property
    def fpgaimages(self):
        """Gets the fpgaimages of this ListFpgaImagesResponse.

        查询的FPGA镜像详情列表。

        :return: The fpgaimages of this ListFpgaImagesResponse.
        :rtype: list[FpgaImage]
        """
        return self._fpgaimages

    @fpgaimages.setter
    def fpgaimages(self, fpgaimages):
        """Sets the fpgaimages of this ListFpgaImagesResponse.

        查询的FPGA镜像详情列表。

        :param fpgaimages: The fpgaimages of this ListFpgaImagesResponse.
        :type: list[FpgaImage]
        """
        self._fpgaimages = fpgaimages

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
        if not isinstance(other, ListFpgaImagesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
