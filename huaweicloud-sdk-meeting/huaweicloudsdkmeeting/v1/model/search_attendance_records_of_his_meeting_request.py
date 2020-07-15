# coding: utf-8

import pprint
import re

import six





class SearchAttendanceRecordsOfHisMeetingRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'conf_uuid': 'str',
        'offset': 'int',
        'limit': 'int',
        'search_key': 'str',
        'user_uuid': 'str',
        'x_authorization_type': 'str',
        'x_site_id': 'str',
        'accept_language': 'str'
    }

    attribute_map = {
        'conf_uuid': 'confUUID',
        'offset': 'offset',
        'limit': 'limit',
        'search_key': 'searchKey',
        'user_uuid': 'userUUID',
        'x_authorization_type': 'X-Authorization-Type',
        'x_site_id': 'X-Site-Id',
        'accept_language': 'Accept-Language'
    }

    def __init__(self, conf_uuid=None, offset=0, limit=20, search_key=None, user_uuid=None, x_authorization_type=None, x_site_id=None, accept_language='zh-CN'):
        """SearchAttendanceRecordsOfHisMeetingRequest - a model defined in huaweicloud sdk"""
        
        

        self._conf_uuid = None
        self._offset = None
        self._limit = None
        self._search_key = None
        self._user_uuid = None
        self._x_authorization_type = None
        self._x_site_id = None
        self._accept_language = None
        self.discriminator = None

        self.conf_uuid = conf_uuid
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if search_key is not None:
            self.search_key = search_key
        if user_uuid is not None:
            self.user_uuid = user_uuid
        if x_authorization_type is not None:
            self.x_authorization_type = x_authorization_type
        if x_site_id is not None:
            self.x_site_id = x_site_id
        if accept_language is not None:
            self.accept_language = accept_language

    @property
    def conf_uuid(self):
        """Gets the conf_uuid of this SearchAttendanceRecordsOfHisMeetingRequest.


        :return: The conf_uuid of this SearchAttendanceRecordsOfHisMeetingRequest.
        :rtype: str
        """
        return self._conf_uuid

    @conf_uuid.setter
    def conf_uuid(self, conf_uuid):
        """Sets the conf_uuid of this SearchAttendanceRecordsOfHisMeetingRequest.


        :param conf_uuid: The conf_uuid of this SearchAttendanceRecordsOfHisMeetingRequest.
        :type: str
        """
        self._conf_uuid = conf_uuid

    @property
    def offset(self):
        """Gets the offset of this SearchAttendanceRecordsOfHisMeetingRequest.


        :return: The offset of this SearchAttendanceRecordsOfHisMeetingRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this SearchAttendanceRecordsOfHisMeetingRequest.


        :param offset: The offset of this SearchAttendanceRecordsOfHisMeetingRequest.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this SearchAttendanceRecordsOfHisMeetingRequest.


        :return: The limit of this SearchAttendanceRecordsOfHisMeetingRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this SearchAttendanceRecordsOfHisMeetingRequest.


        :param limit: The limit of this SearchAttendanceRecordsOfHisMeetingRequest.
        :type: int
        """
        self._limit = limit

    @property
    def search_key(self):
        """Gets the search_key of this SearchAttendanceRecordsOfHisMeetingRequest.


        :return: The search_key of this SearchAttendanceRecordsOfHisMeetingRequest.
        :rtype: str
        """
        return self._search_key

    @search_key.setter
    def search_key(self, search_key):
        """Sets the search_key of this SearchAttendanceRecordsOfHisMeetingRequest.


        :param search_key: The search_key of this SearchAttendanceRecordsOfHisMeetingRequest.
        :type: str
        """
        self._search_key = search_key

    @property
    def user_uuid(self):
        """Gets the user_uuid of this SearchAttendanceRecordsOfHisMeetingRequest.


        :return: The user_uuid of this SearchAttendanceRecordsOfHisMeetingRequest.
        :rtype: str
        """
        return self._user_uuid

    @user_uuid.setter
    def user_uuid(self, user_uuid):
        """Sets the user_uuid of this SearchAttendanceRecordsOfHisMeetingRequest.


        :param user_uuid: The user_uuid of this SearchAttendanceRecordsOfHisMeetingRequest.
        :type: str
        """
        self._user_uuid = user_uuid

    @property
    def x_authorization_type(self):
        """Gets the x_authorization_type of this SearchAttendanceRecordsOfHisMeetingRequest.


        :return: The x_authorization_type of this SearchAttendanceRecordsOfHisMeetingRequest.
        :rtype: str
        """
        return self._x_authorization_type

    @x_authorization_type.setter
    def x_authorization_type(self, x_authorization_type):
        """Sets the x_authorization_type of this SearchAttendanceRecordsOfHisMeetingRequest.


        :param x_authorization_type: The x_authorization_type of this SearchAttendanceRecordsOfHisMeetingRequest.
        :type: str
        """
        self._x_authorization_type = x_authorization_type

    @property
    def x_site_id(self):
        """Gets the x_site_id of this SearchAttendanceRecordsOfHisMeetingRequest.


        :return: The x_site_id of this SearchAttendanceRecordsOfHisMeetingRequest.
        :rtype: str
        """
        return self._x_site_id

    @x_site_id.setter
    def x_site_id(self, x_site_id):
        """Sets the x_site_id of this SearchAttendanceRecordsOfHisMeetingRequest.


        :param x_site_id: The x_site_id of this SearchAttendanceRecordsOfHisMeetingRequest.
        :type: str
        """
        self._x_site_id = x_site_id

    @property
    def accept_language(self):
        """Gets the accept_language of this SearchAttendanceRecordsOfHisMeetingRequest.


        :return: The accept_language of this SearchAttendanceRecordsOfHisMeetingRequest.
        :rtype: str
        """
        return self._accept_language

    @accept_language.setter
    def accept_language(self, accept_language):
        """Sets the accept_language of this SearchAttendanceRecordsOfHisMeetingRequest.


        :param accept_language: The accept_language of this SearchAttendanceRecordsOfHisMeetingRequest.
        :type: str
        """
        self._accept_language = accept_language

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
        if not isinstance(other, SearchAttendanceRecordsOfHisMeetingRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
