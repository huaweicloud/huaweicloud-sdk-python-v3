# coding: utf-8

import pprint
import re

import six


class ListServerResizeFlavorsRequest(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'instance_uuid': 'str',
        'source_flavor_name': 'str',
        'sort_key': 'str',
        'sort_dir': 'str',
        'limit': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'instance_uuid': 'instance_uuid',
        'source_flavor_name': 'source_flavor_name',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, instance_uuid=None, source_flavor_name=None, sort_key='flavorid', sort_dir='asc', limit=None, marker=None):  # noqa: E501
        """ListServerResizeFlavorsRequest - a model defined in huaweicloud sdk"""

        self._instance_uuid = None
        self._source_flavor_name = None
        self._sort_key = None
        self._sort_dir = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        if instance_uuid is not None:
            self.instance_uuid = instance_uuid
        if source_flavor_name is not None:
            self.source_flavor_name = source_flavor_name
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def instance_uuid(self):
        """Gets the instance_uuid of this ListServerResizeFlavorsRequest.


        :return: The instance_uuid of this ListServerResizeFlavorsRequest.
        :rtype: str
        """
        return self._instance_uuid

    @instance_uuid.setter
    def instance_uuid(self, instance_uuid):
        """Sets the instance_uuid of this ListServerResizeFlavorsRequest.


        :param instance_uuid: The instance_uuid of this ListServerResizeFlavorsRequest.
        :type: str
        """
        self._instance_uuid = instance_uuid

    @property
    def source_flavor_name(self):
        """Gets the source_flavor_name of this ListServerResizeFlavorsRequest.


        :return: The source_flavor_name of this ListServerResizeFlavorsRequest.
        :rtype: str
        """
        return self._source_flavor_name

    @source_flavor_name.setter
    def source_flavor_name(self, source_flavor_name):
        """Sets the source_flavor_name of this ListServerResizeFlavorsRequest.


        :param source_flavor_name: The source_flavor_name of this ListServerResizeFlavorsRequest.
        :type: str
        """
        self._source_flavor_name = source_flavor_name

    @property
    def sort_key(self):
        """Gets the sort_key of this ListServerResizeFlavorsRequest.


        :return: The sort_key of this ListServerResizeFlavorsRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ListServerResizeFlavorsRequest.


        :param sort_key: The sort_key of this ListServerResizeFlavorsRequest.
        :type: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        """Gets the sort_dir of this ListServerResizeFlavorsRequest.


        :return: The sort_dir of this ListServerResizeFlavorsRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this ListServerResizeFlavorsRequest.


        :param sort_dir: The sort_dir of this ListServerResizeFlavorsRequest.
        :type: str
        """
        self._sort_dir = sort_dir

    @property
    def limit(self):
        """Gets the limit of this ListServerResizeFlavorsRequest.


        :return: The limit of this ListServerResizeFlavorsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListServerResizeFlavorsRequest.


        :param limit: The limit of this ListServerResizeFlavorsRequest.
        :type: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListServerResizeFlavorsRequest.


        :return: The marker of this ListServerResizeFlavorsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListServerResizeFlavorsRequest.


        :param marker: The marker of this ListServerResizeFlavorsRequest.
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
        if not isinstance(other, ListServerResizeFlavorsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
