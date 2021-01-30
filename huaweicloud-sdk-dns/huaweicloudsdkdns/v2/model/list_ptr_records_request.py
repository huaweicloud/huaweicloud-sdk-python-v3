# coding: utf-8

import pprint
import re

import six





class ListPtrRecordsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'marker': 'str',
        'limit': 'int',
        'offset': 'int',
        'enterprise_project_id': 'str',
        'tags': 'str',
        'status': 'str'
    }

    attribute_map = {
        'marker': 'marker',
        'limit': 'limit',
        'offset': 'offset',
        'enterprise_project_id': 'enterprise_project_id',
        'tags': 'tags',
        'status': 'status'
    }

    def __init__(self, marker=None, limit=None, offset=None, enterprise_project_id=None, tags=None, status=None):
        """ListPtrRecordsRequest - a model defined in huaweicloud sdk"""
        
        

        self._marker = None
        self._limit = None
        self._offset = None
        self._enterprise_project_id = None
        self._tags = None
        self._status = None
        self.discriminator = None

        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if tags is not None:
            self.tags = tags
        if status is not None:
            self.status = status

    @property
    def marker(self):
        """Gets the marker of this ListPtrRecordsRequest.


        :return: The marker of this ListPtrRecordsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListPtrRecordsRequest.


        :param marker: The marker of this ListPtrRecordsRequest.
        :type: str
        """
        self._marker = marker

    @property
    def limit(self):
        """Gets the limit of this ListPtrRecordsRequest.


        :return: The limit of this ListPtrRecordsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPtrRecordsRequest.


        :param limit: The limit of this ListPtrRecordsRequest.
        :type: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListPtrRecordsRequest.


        :return: The offset of this ListPtrRecordsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListPtrRecordsRequest.


        :param offset: The offset of this ListPtrRecordsRequest.
        :type: int
        """
        self._offset = offset

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListPtrRecordsRequest.


        :return: The enterprise_project_id of this ListPtrRecordsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListPtrRecordsRequest.


        :param enterprise_project_id: The enterprise_project_id of this ListPtrRecordsRequest.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        """Gets the tags of this ListPtrRecordsRequest.


        :return: The tags of this ListPtrRecordsRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ListPtrRecordsRequest.


        :param tags: The tags of this ListPtrRecordsRequest.
        :type: str
        """
        self._tags = tags

    @property
    def status(self):
        """Gets the status of this ListPtrRecordsRequest.


        :return: The status of this ListPtrRecordsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListPtrRecordsRequest.


        :param status: The status of this ListPtrRecordsRequest.
        :type: str
        """
        self._status = status

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
        if not isinstance(other, ListPtrRecordsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
