# coding: utf-8

import pprint
import re

import six





class ShowMeetingDetailRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'conference_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'search_key': 'str',
        'user_uuid': 'str',
        'x_type': 'str',
        'x_query_type': 'str',
        'x_authorization_type': 'str',
        'x_site_id': 'str'
    }

    attribute_map = {
        'conference_id': 'conferenceID',
        'offset': 'offset',
        'limit': 'limit',
        'search_key': 'searchKey',
        'user_uuid': 'userUUID',
        'x_type': 'X-Type',
        'x_query_type': 'X-Query-Type',
        'x_authorization_type': 'X-Authorization-Type',
        'x_site_id': 'X-Site-Id'
    }

    def __init__(self, conference_id=None, offset=0, limit=20, search_key=None, user_uuid=None, x_type='0', x_query_type='0', x_authorization_type=None, x_site_id=None):
        """ShowMeetingDetailRequest - a model defined in huaweicloud sdk"""
        
        

        self._conference_id = None
        self._offset = None
        self._limit = None
        self._search_key = None
        self._user_uuid = None
        self._x_type = None
        self._x_query_type = None
        self._x_authorization_type = None
        self._x_site_id = None
        self.discriminator = None

        self.conference_id = conference_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if search_key is not None:
            self.search_key = search_key
        if user_uuid is not None:
            self.user_uuid = user_uuid
        if x_type is not None:
            self.x_type = x_type
        if x_query_type is not None:
            self.x_query_type = x_query_type
        if x_authorization_type is not None:
            self.x_authorization_type = x_authorization_type
        if x_site_id is not None:
            self.x_site_id = x_site_id

    @property
    def conference_id(self):
        """Gets the conference_id of this ShowMeetingDetailRequest.


        :return: The conference_id of this ShowMeetingDetailRequest.
        :rtype: str
        """
        return self._conference_id

    @conference_id.setter
    def conference_id(self, conference_id):
        """Sets the conference_id of this ShowMeetingDetailRequest.


        :param conference_id: The conference_id of this ShowMeetingDetailRequest.
        :type: str
        """
        self._conference_id = conference_id

    @property
    def offset(self):
        """Gets the offset of this ShowMeetingDetailRequest.


        :return: The offset of this ShowMeetingDetailRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowMeetingDetailRequest.


        :param offset: The offset of this ShowMeetingDetailRequest.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ShowMeetingDetailRequest.


        :return: The limit of this ShowMeetingDetailRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowMeetingDetailRequest.


        :param limit: The limit of this ShowMeetingDetailRequest.
        :type: int
        """
        self._limit = limit

    @property
    def search_key(self):
        """Gets the search_key of this ShowMeetingDetailRequest.


        :return: The search_key of this ShowMeetingDetailRequest.
        :rtype: str
        """
        return self._search_key

    @search_key.setter
    def search_key(self, search_key):
        """Sets the search_key of this ShowMeetingDetailRequest.


        :param search_key: The search_key of this ShowMeetingDetailRequest.
        :type: str
        """
        self._search_key = search_key

    @property
    def user_uuid(self):
        """Gets the user_uuid of this ShowMeetingDetailRequest.


        :return: The user_uuid of this ShowMeetingDetailRequest.
        :rtype: str
        """
        return self._user_uuid

    @user_uuid.setter
    def user_uuid(self, user_uuid):
        """Sets the user_uuid of this ShowMeetingDetailRequest.


        :param user_uuid: The user_uuid of this ShowMeetingDetailRequest.
        :type: str
        """
        self._user_uuid = user_uuid

    @property
    def x_type(self):
        """Gets the x_type of this ShowMeetingDetailRequest.


        :return: The x_type of this ShowMeetingDetailRequest.
        :rtype: str
        """
        return self._x_type

    @x_type.setter
    def x_type(self, x_type):
        """Sets the x_type of this ShowMeetingDetailRequest.


        :param x_type: The x_type of this ShowMeetingDetailRequest.
        :type: str
        """
        self._x_type = x_type

    @property
    def x_query_type(self):
        """Gets the x_query_type of this ShowMeetingDetailRequest.


        :return: The x_query_type of this ShowMeetingDetailRequest.
        :rtype: str
        """
        return self._x_query_type

    @x_query_type.setter
    def x_query_type(self, x_query_type):
        """Sets the x_query_type of this ShowMeetingDetailRequest.


        :param x_query_type: The x_query_type of this ShowMeetingDetailRequest.
        :type: str
        """
        self._x_query_type = x_query_type

    @property
    def x_authorization_type(self):
        """Gets the x_authorization_type of this ShowMeetingDetailRequest.


        :return: The x_authorization_type of this ShowMeetingDetailRequest.
        :rtype: str
        """
        return self._x_authorization_type

    @x_authorization_type.setter
    def x_authorization_type(self, x_authorization_type):
        """Sets the x_authorization_type of this ShowMeetingDetailRequest.


        :param x_authorization_type: The x_authorization_type of this ShowMeetingDetailRequest.
        :type: str
        """
        self._x_authorization_type = x_authorization_type

    @property
    def x_site_id(self):
        """Gets the x_site_id of this ShowMeetingDetailRequest.


        :return: The x_site_id of this ShowMeetingDetailRequest.
        :rtype: str
        """
        return self._x_site_id

    @x_site_id.setter
    def x_site_id(self, x_site_id):
        """Sets the x_site_id of this ShowMeetingDetailRequest.


        :param x_site_id: The x_site_id of this ShowMeetingDetailRequest.
        :type: str
        """
        self._x_site_id = x_site_id

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
        if not isinstance(other, ShowMeetingDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
