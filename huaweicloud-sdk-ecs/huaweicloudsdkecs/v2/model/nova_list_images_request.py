# coding: utf-8

import pprint
import re

import six


class NovaListImagesRequest(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'changes_since': 'str',
        'min_disk': 'int',
        'min_ram': 'int',
        'name': 'str',
        'status': 'str',
        'limit': 'str',
        'marker': 'str'
    }

    attribute_map = {
        'changes_since': 'changes-since',
        'min_disk': 'minDisk',
        'min_ram': 'minRam',
        'name': 'name',
        'status': 'status',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, changes_since=None, min_disk=None, min_ram=None, name=None, status=None, limit=None, marker=None):  # noqa: E501
        """NovaListImagesRequest - a model defined in huaweicloud sdk"""

        self._changes_since = None
        self._min_disk = None
        self._min_ram = None
        self._name = None
        self._status = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        if changes_since is not None:
            self.changes_since = changes_since
        if min_disk is not None:
            self.min_disk = min_disk
        if min_ram is not None:
            self.min_ram = min_ram
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def changes_since(self):
        """Gets the changes_since of this NovaListImagesRequest.


        :return: The changes_since of this NovaListImagesRequest.
        :rtype: str
        """
        return self._changes_since

    @changes_since.setter
    def changes_since(self, changes_since):
        """Sets the changes_since of this NovaListImagesRequest.


        :param changes_since: The changes_since of this NovaListImagesRequest.
        :type: str
        """
        self._changes_since = changes_since

    @property
    def min_disk(self):
        """Gets the min_disk of this NovaListImagesRequest.


        :return: The min_disk of this NovaListImagesRequest.
        :rtype: int
        """
        return self._min_disk

    @min_disk.setter
    def min_disk(self, min_disk):
        """Sets the min_disk of this NovaListImagesRequest.


        :param min_disk: The min_disk of this NovaListImagesRequest.
        :type: int
        """
        self._min_disk = min_disk

    @property
    def min_ram(self):
        """Gets the min_ram of this NovaListImagesRequest.


        :return: The min_ram of this NovaListImagesRequest.
        :rtype: int
        """
        return self._min_ram

    @min_ram.setter
    def min_ram(self, min_ram):
        """Sets the min_ram of this NovaListImagesRequest.


        :param min_ram: The min_ram of this NovaListImagesRequest.
        :type: int
        """
        self._min_ram = min_ram

    @property
    def name(self):
        """Gets the name of this NovaListImagesRequest.


        :return: The name of this NovaListImagesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NovaListImagesRequest.


        :param name: The name of this NovaListImagesRequest.
        :type: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this NovaListImagesRequest.


        :return: The status of this NovaListImagesRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NovaListImagesRequest.


        :param status: The status of this NovaListImagesRequest.
        :type: str
        """
        self._status = status

    @property
    def limit(self):
        """Gets the limit of this NovaListImagesRequest.


        :return: The limit of this NovaListImagesRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this NovaListImagesRequest.


        :param limit: The limit of this NovaListImagesRequest.
        :type: str
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this NovaListImagesRequest.


        :return: The marker of this NovaListImagesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this NovaListImagesRequest.


        :param marker: The marker of this NovaListImagesRequest.
        :type: str
        """
        self._marker = marker

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
        if not isinstance(other, NovaListImagesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
