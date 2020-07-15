# coding: utf-8

import pprint
import re

import six





class SearchMeetingsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'user_uuid': 'str',
        'offset': 'int',
        'limit': 'int',
        'query_all': 'bool',
        'search_key': 'str',
        'query_conf_mode': 'str',
        'sort_type': 'str',
        'x_authorization_type': 'str',
        'x_site_id': 'str'
    }

    attribute_map = {
        'user_uuid': 'userUUID',
        'offset': 'offset',
        'limit': 'limit',
        'query_all': 'queryAll',
        'search_key': 'searchKey',
        'query_conf_mode': 'queryConfMode',
        'sort_type': 'sortType',
        'x_authorization_type': 'X-Authorization-Type',
        'x_site_id': 'X-Site-Id'
    }

    def __init__(self, user_uuid=None, offset=0, limit=20, query_all=False, search_key=None, query_conf_mode=None, sort_type=None, x_authorization_type=None, x_site_id=None):
        """SearchMeetingsRequest - a model defined in huaweicloud sdk"""
        
        

        self._user_uuid = None
        self._offset = None
        self._limit = None
        self._query_all = None
        self._search_key = None
        self._query_conf_mode = None
        self._sort_type = None
        self._x_authorization_type = None
        self._x_site_id = None
        self.discriminator = None

        if user_uuid is not None:
            self.user_uuid = user_uuid
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if query_all is not None:
            self.query_all = query_all
        if search_key is not None:
            self.search_key = search_key
        if query_conf_mode is not None:
            self.query_conf_mode = query_conf_mode
        if sort_type is not None:
            self.sort_type = sort_type
        if x_authorization_type is not None:
            self.x_authorization_type = x_authorization_type
        if x_site_id is not None:
            self.x_site_id = x_site_id

    @property
    def user_uuid(self):
        """Gets the user_uuid of this SearchMeetingsRequest.


        :return: The user_uuid of this SearchMeetingsRequest.
        :rtype: str
        """
        return self._user_uuid

    @user_uuid.setter
    def user_uuid(self, user_uuid):
        """Sets the user_uuid of this SearchMeetingsRequest.


        :param user_uuid: The user_uuid of this SearchMeetingsRequest.
        :type: str
        """
        self._user_uuid = user_uuid

    @property
    def offset(self):
        """Gets the offset of this SearchMeetingsRequest.


        :return: The offset of this SearchMeetingsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this SearchMeetingsRequest.


        :param offset: The offset of this SearchMeetingsRequest.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this SearchMeetingsRequest.


        :return: The limit of this SearchMeetingsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this SearchMeetingsRequest.


        :param limit: The limit of this SearchMeetingsRequest.
        :type: int
        """
        self._limit = limit

    @property
    def query_all(self):
        """Gets the query_all of this SearchMeetingsRequest.


        :return: The query_all of this SearchMeetingsRequest.
        :rtype: bool
        """
        return self._query_all

    @query_all.setter
    def query_all(self, query_all):
        """Sets the query_all of this SearchMeetingsRequest.


        :param query_all: The query_all of this SearchMeetingsRequest.
        :type: bool
        """
        self._query_all = query_all

    @property
    def search_key(self):
        """Gets the search_key of this SearchMeetingsRequest.


        :return: The search_key of this SearchMeetingsRequest.
        :rtype: str
        """
        return self._search_key

    @search_key.setter
    def search_key(self, search_key):
        """Sets the search_key of this SearchMeetingsRequest.


        :param search_key: The search_key of this SearchMeetingsRequest.
        :type: str
        """
        self._search_key = search_key

    @property
    def query_conf_mode(self):
        """Gets the query_conf_mode of this SearchMeetingsRequest.


        :return: The query_conf_mode of this SearchMeetingsRequest.
        :rtype: str
        """
        return self._query_conf_mode

    @query_conf_mode.setter
    def query_conf_mode(self, query_conf_mode):
        """Sets the query_conf_mode of this SearchMeetingsRequest.


        :param query_conf_mode: The query_conf_mode of this SearchMeetingsRequest.
        :type: str
        """
        self._query_conf_mode = query_conf_mode

    @property
    def sort_type(self):
        """Gets the sort_type of this SearchMeetingsRequest.


        :return: The sort_type of this SearchMeetingsRequest.
        :rtype: str
        """
        return self._sort_type

    @sort_type.setter
    def sort_type(self, sort_type):
        """Sets the sort_type of this SearchMeetingsRequest.


        :param sort_type: The sort_type of this SearchMeetingsRequest.
        :type: str
        """
        self._sort_type = sort_type

    @property
    def x_authorization_type(self):
        """Gets the x_authorization_type of this SearchMeetingsRequest.


        :return: The x_authorization_type of this SearchMeetingsRequest.
        :rtype: str
        """
        return self._x_authorization_type

    @x_authorization_type.setter
    def x_authorization_type(self, x_authorization_type):
        """Sets the x_authorization_type of this SearchMeetingsRequest.


        :param x_authorization_type: The x_authorization_type of this SearchMeetingsRequest.
        :type: str
        """
        self._x_authorization_type = x_authorization_type

    @property
    def x_site_id(self):
        """Gets the x_site_id of this SearchMeetingsRequest.


        :return: The x_site_id of this SearchMeetingsRequest.
        :rtype: str
        """
        return self._x_site_id

    @x_site_id.setter
    def x_site_id(self, x_site_id):
        """Sets the x_site_id of this SearchMeetingsRequest.


        :param x_site_id: The x_site_id of this SearchMeetingsRequest.
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
        if not isinstance(other, SearchMeetingsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
