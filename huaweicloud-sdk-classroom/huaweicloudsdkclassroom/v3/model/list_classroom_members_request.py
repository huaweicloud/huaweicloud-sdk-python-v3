# coding: utf-8

import pprint
import re

import six





class ListClassroomMembersRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'classroom_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'filter': 'str'
    }

    attribute_map = {
        'classroom_id': 'classroom_id',
        'offset': 'offset',
        'limit': 'limit',
        'filter': 'filter'
    }

    def __init__(self, classroom_id=None, offset=None, limit=None, filter=None):
        """ListClassroomMembersRequest - a model defined in huaweicloud sdk"""
        
        

        self._classroom_id = None
        self._offset = None
        self._limit = None
        self._filter = None
        self.discriminator = None

        self.classroom_id = classroom_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if filter is not None:
            self.filter = filter

    @property
    def classroom_id(self):
        """Gets the classroom_id of this ListClassroomMembersRequest.


        :return: The classroom_id of this ListClassroomMembersRequest.
        :rtype: str
        """
        return self._classroom_id

    @classroom_id.setter
    def classroom_id(self, classroom_id):
        """Sets the classroom_id of this ListClassroomMembersRequest.


        :param classroom_id: The classroom_id of this ListClassroomMembersRequest.
        :type: str
        """
        self._classroom_id = classroom_id

    @property
    def offset(self):
        """Gets the offset of this ListClassroomMembersRequest.


        :return: The offset of this ListClassroomMembersRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListClassroomMembersRequest.


        :param offset: The offset of this ListClassroomMembersRequest.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListClassroomMembersRequest.


        :return: The limit of this ListClassroomMembersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListClassroomMembersRequest.


        :param limit: The limit of this ListClassroomMembersRequest.
        :type: int
        """
        self._limit = limit

    @property
    def filter(self):
        """Gets the filter of this ListClassroomMembersRequest.


        :return: The filter of this ListClassroomMembersRequest.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this ListClassroomMembersRequest.


        :param filter: The filter of this ListClassroomMembersRequest.
        :type: str
        """
        self._filter = filter

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
        if not isinstance(other, ListClassroomMembersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
