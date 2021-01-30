# coding: utf-8

import pprint
import re

import six





class ListRecordSetsByZoneRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'zone_id': 'str',
        'marker': 'str',
        'limit': 'str',
        'offset': 'str',
        'tags': 'str',
        'status': 'str',
        'type': 'str',
        'name': 'str',
        'id': 'str',
        'sort_key': 'str',
        'sort_dir': 'str'
    }

    attribute_map = {
        'zone_id': 'zone_id',
        'marker': 'marker',
        'limit': 'limit',
        'offset': 'offset',
        'tags': 'tags',
        'status': 'status',
        'type': 'type',
        'name': 'name',
        'id': 'id',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir'
    }

    def __init__(self, zone_id=None, marker=None, limit=None, offset=None, tags=None, status=None, type=None, name=None, id=None, sort_key=None, sort_dir=None):
        """ListRecordSetsByZoneRequest - a model defined in huaweicloud sdk"""
        
        

        self._zone_id = None
        self._marker = None
        self._limit = None
        self._offset = None
        self._tags = None
        self._status = None
        self._type = None
        self._name = None
        self._id = None
        self._sort_key = None
        self._sort_dir = None
        self.discriminator = None

        self.zone_id = zone_id
        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if tags is not None:
            self.tags = tags
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir

    @property
    def zone_id(self):
        """Gets the zone_id of this ListRecordSetsByZoneRequest.


        :return: The zone_id of this ListRecordSetsByZoneRequest.
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this ListRecordSetsByZoneRequest.


        :param zone_id: The zone_id of this ListRecordSetsByZoneRequest.
        :type: str
        """
        self._zone_id = zone_id

    @property
    def marker(self):
        """Gets the marker of this ListRecordSetsByZoneRequest.


        :return: The marker of this ListRecordSetsByZoneRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListRecordSetsByZoneRequest.


        :param marker: The marker of this ListRecordSetsByZoneRequest.
        :type: str
        """
        self._marker = marker

    @property
    def limit(self):
        """Gets the limit of this ListRecordSetsByZoneRequest.


        :return: The limit of this ListRecordSetsByZoneRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListRecordSetsByZoneRequest.


        :param limit: The limit of this ListRecordSetsByZoneRequest.
        :type: str
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListRecordSetsByZoneRequest.


        :return: The offset of this ListRecordSetsByZoneRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListRecordSetsByZoneRequest.


        :param offset: The offset of this ListRecordSetsByZoneRequest.
        :type: str
        """
        self._offset = offset

    @property
    def tags(self):
        """Gets the tags of this ListRecordSetsByZoneRequest.


        :return: The tags of this ListRecordSetsByZoneRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ListRecordSetsByZoneRequest.


        :param tags: The tags of this ListRecordSetsByZoneRequest.
        :type: str
        """
        self._tags = tags

    @property
    def status(self):
        """Gets the status of this ListRecordSetsByZoneRequest.


        :return: The status of this ListRecordSetsByZoneRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListRecordSetsByZoneRequest.


        :param status: The status of this ListRecordSetsByZoneRequest.
        :type: str
        """
        self._status = status

    @property
    def type(self):
        """Gets the type of this ListRecordSetsByZoneRequest.


        :return: The type of this ListRecordSetsByZoneRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListRecordSetsByZoneRequest.


        :param type: The type of this ListRecordSetsByZoneRequest.
        :type: str
        """
        self._type = type

    @property
    def name(self):
        """Gets the name of this ListRecordSetsByZoneRequest.


        :return: The name of this ListRecordSetsByZoneRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListRecordSetsByZoneRequest.


        :param name: The name of this ListRecordSetsByZoneRequest.
        :type: str
        """
        self._name = name

    @property
    def id(self):
        """Gets the id of this ListRecordSetsByZoneRequest.


        :return: The id of this ListRecordSetsByZoneRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListRecordSetsByZoneRequest.


        :param id: The id of this ListRecordSetsByZoneRequest.
        :type: str
        """
        self._id = id

    @property
    def sort_key(self):
        """Gets the sort_key of this ListRecordSetsByZoneRequest.


        :return: The sort_key of this ListRecordSetsByZoneRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ListRecordSetsByZoneRequest.


        :param sort_key: The sort_key of this ListRecordSetsByZoneRequest.
        :type: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        """Gets the sort_dir of this ListRecordSetsByZoneRequest.


        :return: The sort_dir of this ListRecordSetsByZoneRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this ListRecordSetsByZoneRequest.


        :param sort_dir: The sort_dir of this ListRecordSetsByZoneRequest.
        :type: str
        """
        self._sort_dir = sort_dir

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
                if attr in self.sensitive_list:
                    result[attr] = "****"
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
        if not isinstance(other, ListRecordSetsByZoneRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
