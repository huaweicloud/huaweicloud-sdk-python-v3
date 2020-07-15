# coding: utf-8

import pprint
import re

import six





class SearchMemberVmrRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'x_request_id': 'str',
        'accept_language': 'str',
        'offset': 'int',
        'limit': 'int',
        'search_key': 'str',
        'special_vmr': 'bool'
    }

    attribute_map = {
        'x_request_id': 'X-Request-Id',
        'accept_language': 'Accept-Language',
        'offset': 'offset',
        'limit': 'limit',
        'search_key': 'searchKey',
        'special_vmr': 'specialVmr'
    }

    def __init__(self, x_request_id=None, accept_language=None, offset=0, limit=100, search_key=None, special_vmr=None):
        """SearchMemberVmrRequest - a model defined in huaweicloud sdk"""
        
        

        self._x_request_id = None
        self._accept_language = None
        self._offset = None
        self._limit = None
        self._search_key = None
        self._special_vmr = None
        self.discriminator = None

        if x_request_id is not None:
            self.x_request_id = x_request_id
        if accept_language is not None:
            self.accept_language = accept_language
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if search_key is not None:
            self.search_key = search_key
        if special_vmr is not None:
            self.special_vmr = special_vmr

    @property
    def x_request_id(self):
        """Gets the x_request_id of this SearchMemberVmrRequest.


        :return: The x_request_id of this SearchMemberVmrRequest.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this SearchMemberVmrRequest.


        :param x_request_id: The x_request_id of this SearchMemberVmrRequest.
        :type: str
        """
        self._x_request_id = x_request_id

    @property
    def accept_language(self):
        """Gets the accept_language of this SearchMemberVmrRequest.


        :return: The accept_language of this SearchMemberVmrRequest.
        :rtype: str
        """
        return self._accept_language

    @accept_language.setter
    def accept_language(self, accept_language):
        """Sets the accept_language of this SearchMemberVmrRequest.


        :param accept_language: The accept_language of this SearchMemberVmrRequest.
        :type: str
        """
        self._accept_language = accept_language

    @property
    def offset(self):
        """Gets the offset of this SearchMemberVmrRequest.


        :return: The offset of this SearchMemberVmrRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this SearchMemberVmrRequest.


        :param offset: The offset of this SearchMemberVmrRequest.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this SearchMemberVmrRequest.


        :return: The limit of this SearchMemberVmrRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this SearchMemberVmrRequest.


        :param limit: The limit of this SearchMemberVmrRequest.
        :type: int
        """
        self._limit = limit

    @property
    def search_key(self):
        """Gets the search_key of this SearchMemberVmrRequest.


        :return: The search_key of this SearchMemberVmrRequest.
        :rtype: str
        """
        return self._search_key

    @search_key.setter
    def search_key(self, search_key):
        """Sets the search_key of this SearchMemberVmrRequest.


        :param search_key: The search_key of this SearchMemberVmrRequest.
        :type: str
        """
        self._search_key = search_key

    @property
    def special_vmr(self):
        """Gets the special_vmr of this SearchMemberVmrRequest.


        :return: The special_vmr of this SearchMemberVmrRequest.
        :rtype: bool
        """
        return self._special_vmr

    @special_vmr.setter
    def special_vmr(self, special_vmr):
        """Sets the special_vmr of this SearchMemberVmrRequest.


        :param special_vmr: The special_vmr of this SearchMemberVmrRequest.
        :type: bool
        """
        self._special_vmr = special_vmr

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
        if not isinstance(other, SearchMemberVmrRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
