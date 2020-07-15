# coding: utf-8

import pprint
import re

import six





class ListClassroomMemberJobsRequest:


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
        'member_id': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'classroom_id': 'classroom_id',
        'member_id': 'member_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, classroom_id=None, member_id=None, offset=None, limit=None):
        """ListClassroomMemberJobsRequest - a model defined in huaweicloud sdk"""
        
        

        self._classroom_id = None
        self._member_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.classroom_id = classroom_id
        self.member_id = member_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def classroom_id(self):
        """Gets the classroom_id of this ListClassroomMemberJobsRequest.


        :return: The classroom_id of this ListClassroomMemberJobsRequest.
        :rtype: str
        """
        return self._classroom_id

    @classroom_id.setter
    def classroom_id(self, classroom_id):
        """Sets the classroom_id of this ListClassroomMemberJobsRequest.


        :param classroom_id: The classroom_id of this ListClassroomMemberJobsRequest.
        :type: str
        """
        self._classroom_id = classroom_id

    @property
    def member_id(self):
        """Gets the member_id of this ListClassroomMemberJobsRequest.


        :return: The member_id of this ListClassroomMemberJobsRequest.
        :rtype: str
        """
        return self._member_id

    @member_id.setter
    def member_id(self, member_id):
        """Sets the member_id of this ListClassroomMemberJobsRequest.


        :param member_id: The member_id of this ListClassroomMemberJobsRequest.
        :type: str
        """
        self._member_id = member_id

    @property
    def offset(self):
        """Gets the offset of this ListClassroomMemberJobsRequest.


        :return: The offset of this ListClassroomMemberJobsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListClassroomMemberJobsRequest.


        :param offset: The offset of this ListClassroomMemberJobsRequest.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListClassroomMemberJobsRequest.


        :return: The limit of this ListClassroomMemberJobsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListClassroomMemberJobsRequest.


        :param limit: The limit of this ListClassroomMemberJobsRequest.
        :type: int
        """
        self._limit = limit

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
        if not isinstance(other, ListClassroomMemberJobsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
