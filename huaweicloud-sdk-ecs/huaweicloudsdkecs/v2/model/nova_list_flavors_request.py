# coding: utf-8

import pprint
import re

import six


class NovaListFlavorsRequest(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'min_disk': 'int',
        'min_ram': 'int',
        'sort_dir': 'str',
        'sort_key': 'str'
    }

    attribute_map = {
        'min_disk': 'minDisk',
        'min_ram': 'minRam',
        'sort_dir': 'sort_dir',
        'sort_key': 'sort_key'
    }

    def __init__(self, min_disk=None, min_ram=None, sort_dir='asc', sort_key='flavorid'):  # noqa: E501
        """NovaListFlavorsRequest - a model defined in huaweicloud sdk"""

        self._min_disk = None
        self._min_ram = None
        self._sort_dir = None
        self._sort_key = None
        self.discriminator = None

        if min_disk is not None:
            self.min_disk = min_disk
        if min_ram is not None:
            self.min_ram = min_ram
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if sort_key is not None:
            self.sort_key = sort_key

    @property
    def min_disk(self):
        """Gets the min_disk of this NovaListFlavorsRequest.


        :return: The min_disk of this NovaListFlavorsRequest.
        :rtype: int
        """
        return self._min_disk

    @min_disk.setter
    def min_disk(self, min_disk):
        """Sets the min_disk of this NovaListFlavorsRequest.


        :param min_disk: The min_disk of this NovaListFlavorsRequest.
        :type: int
        """
        self._min_disk = min_disk

    @property
    def min_ram(self):
        """Gets the min_ram of this NovaListFlavorsRequest.


        :return: The min_ram of this NovaListFlavorsRequest.
        :rtype: int
        """
        return self._min_ram

    @min_ram.setter
    def min_ram(self, min_ram):
        """Sets the min_ram of this NovaListFlavorsRequest.


        :param min_ram: The min_ram of this NovaListFlavorsRequest.
        :type: int
        """
        self._min_ram = min_ram

    @property
    def sort_dir(self):
        """Gets the sort_dir of this NovaListFlavorsRequest.


        :return: The sort_dir of this NovaListFlavorsRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this NovaListFlavorsRequest.


        :param sort_dir: The sort_dir of this NovaListFlavorsRequest.
        :type: str
        """
        self._sort_dir = sort_dir

    @property
    def sort_key(self):
        """Gets the sort_key of this NovaListFlavorsRequest.


        :return: The sort_key of this NovaListFlavorsRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this NovaListFlavorsRequest.


        :param sort_key: The sort_key of this NovaListFlavorsRequest.
        :type: str
        """
        self._sort_key = sort_key

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
        if not isinstance(other, NovaListFlavorsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
