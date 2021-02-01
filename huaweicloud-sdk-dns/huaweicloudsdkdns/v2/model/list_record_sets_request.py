# coding: utf-8

import pprint
import re

import six





class ListRecordSetsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'zone_type': 'str',
        'marker': 'str',
        'limit': 'str',
        'offset': 'str',
        'tags': 'str',
        'status': 'str',
        'type': 'str',
        'name': 'str',
        'id': 'str',
        'records': 'str',
        'sort_key': 'str',
        'sort_dir': 'str'
    }

    attribute_map = {
        'zone_type': 'zone_type',
        'marker': 'marker',
        'limit': 'limit',
        'offset': 'offset',
        'tags': 'tags',
        'status': 'status',
        'type': 'type',
        'name': 'name',
        'id': 'id',
        'records': 'records',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir'
    }

    def __init__(self, zone_type=None, marker=None, limit=None, offset=None, tags=None, status=None, type=None, name=None, id=None, records=None, sort_key=None, sort_dir=None):
        """ListRecordSetsRequest - a model defined in huaweicloud sdk"""
        
        

        self._zone_type = None
        self._marker = None
        self._limit = None
        self._offset = None
        self._tags = None
        self._status = None
        self._type = None
        self._name = None
        self._id = None
        self._records = None
        self._sort_key = None
        self._sort_dir = None
        self.discriminator = None

        if zone_type is not None:
            self.zone_type = zone_type
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
        if records is not None:
            self.records = records
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir

    @property
    def zone_type(self):
        """Gets the zone_type of this ListRecordSetsRequest.


        :return: The zone_type of this ListRecordSetsRequest.
        :rtype: str
        """
        return self._zone_type

    @zone_type.setter
    def zone_type(self, zone_type):
        """Sets the zone_type of this ListRecordSetsRequest.


        :param zone_type: The zone_type of this ListRecordSetsRequest.
        :type: str
        """
        self._zone_type = zone_type

    @property
    def marker(self):
        """Gets the marker of this ListRecordSetsRequest.


        :return: The marker of this ListRecordSetsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListRecordSetsRequest.


        :param marker: The marker of this ListRecordSetsRequest.
        :type: str
        """
        self._marker = marker

    @property
    def limit(self):
        """Gets the limit of this ListRecordSetsRequest.


        :return: The limit of this ListRecordSetsRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListRecordSetsRequest.


        :param limit: The limit of this ListRecordSetsRequest.
        :type: str
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListRecordSetsRequest.


        :return: The offset of this ListRecordSetsRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListRecordSetsRequest.


        :param offset: The offset of this ListRecordSetsRequest.
        :type: str
        """
        self._offset = offset

    @property
    def tags(self):
        """Gets the tags of this ListRecordSetsRequest.


        :return: The tags of this ListRecordSetsRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ListRecordSetsRequest.


        :param tags: The tags of this ListRecordSetsRequest.
        :type: str
        """
        self._tags = tags

    @property
    def status(self):
        """Gets the status of this ListRecordSetsRequest.


        :return: The status of this ListRecordSetsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListRecordSetsRequest.


        :param status: The status of this ListRecordSetsRequest.
        :type: str
        """
        self._status = status

    @property
    def type(self):
        """Gets the type of this ListRecordSetsRequest.


        :return: The type of this ListRecordSetsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListRecordSetsRequest.


        :param type: The type of this ListRecordSetsRequest.
        :type: str
        """
        self._type = type

    @property
    def name(self):
        """Gets the name of this ListRecordSetsRequest.


        :return: The name of this ListRecordSetsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListRecordSetsRequest.


        :param name: The name of this ListRecordSetsRequest.
        :type: str
        """
        self._name = name

    @property
    def id(self):
        """Gets the id of this ListRecordSetsRequest.


        :return: The id of this ListRecordSetsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListRecordSetsRequest.


        :param id: The id of this ListRecordSetsRequest.
        :type: str
        """
        self._id = id

    @property
    def records(self):
        """Gets the records of this ListRecordSetsRequest.


        :return: The records of this ListRecordSetsRequest.
        :rtype: str
        """
        return self._records

    @records.setter
    def records(self, records):
        """Sets the records of this ListRecordSetsRequest.


        :param records: The records of this ListRecordSetsRequest.
        :type: str
        """
        self._records = records

    @property
    def sort_key(self):
        """Gets the sort_key of this ListRecordSetsRequest.


        :return: The sort_key of this ListRecordSetsRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ListRecordSetsRequest.


        :param sort_key: The sort_key of this ListRecordSetsRequest.
        :type: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        """Gets the sort_dir of this ListRecordSetsRequest.


        :return: The sort_dir of this ListRecordSetsRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this ListRecordSetsRequest.


        :param sort_dir: The sort_dir of this ListRecordSetsRequest.
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
        if not isinstance(other, ListRecordSetsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
