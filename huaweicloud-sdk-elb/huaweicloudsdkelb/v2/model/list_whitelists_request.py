# coding: utf-8

import pprint
import re

import six





class ListWhitelistsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'marker': 'str',
        'page_reverse': 'bool',
        'id': 'str',
        'enable_whitelist': 'bool',
        'listener_id': 'str',
        'whitelist': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'page_reverse': 'page_reverse',
        'id': 'id',
        'enable_whitelist': 'enable_whitelist',
        'listener_id': 'listener_id',
        'whitelist': 'whitelist'
    }

    def __init__(self, limit=None, marker=None, page_reverse=None, id=None, enable_whitelist=None, listener_id=None, whitelist=None):
        """ListWhitelistsRequest - a model defined in huaweicloud sdk"""
        
        

        self._limit = None
        self._marker = None
        self._page_reverse = None
        self._id = None
        self._enable_whitelist = None
        self._listener_id = None
        self._whitelist = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if page_reverse is not None:
            self.page_reverse = page_reverse
        if id is not None:
            self.id = id
        if enable_whitelist is not None:
            self.enable_whitelist = enable_whitelist
        if listener_id is not None:
            self.listener_id = listener_id
        if whitelist is not None:
            self.whitelist = whitelist

    @property
    def limit(self):
        """Gets the limit of this ListWhitelistsRequest.


        :return: The limit of this ListWhitelistsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListWhitelistsRequest.


        :param limit: The limit of this ListWhitelistsRequest.
        :type: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListWhitelistsRequest.


        :return: The marker of this ListWhitelistsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListWhitelistsRequest.


        :param marker: The marker of this ListWhitelistsRequest.
        :type: str
        """
        self._marker = marker

    @property
    def page_reverse(self):
        """Gets the page_reverse of this ListWhitelistsRequest.


        :return: The page_reverse of this ListWhitelistsRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        """Sets the page_reverse of this ListWhitelistsRequest.


        :param page_reverse: The page_reverse of this ListWhitelistsRequest.
        :type: bool
        """
        self._page_reverse = page_reverse

    @property
    def id(self):
        """Gets the id of this ListWhitelistsRequest.


        :return: The id of this ListWhitelistsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListWhitelistsRequest.


        :param id: The id of this ListWhitelistsRequest.
        :type: str
        """
        self._id = id

    @property
    def enable_whitelist(self):
        """Gets the enable_whitelist of this ListWhitelistsRequest.


        :return: The enable_whitelist of this ListWhitelistsRequest.
        :rtype: bool
        """
        return self._enable_whitelist

    @enable_whitelist.setter
    def enable_whitelist(self, enable_whitelist):
        """Sets the enable_whitelist of this ListWhitelistsRequest.


        :param enable_whitelist: The enable_whitelist of this ListWhitelistsRequest.
        :type: bool
        """
        self._enable_whitelist = enable_whitelist

    @property
    def listener_id(self):
        """Gets the listener_id of this ListWhitelistsRequest.


        :return: The listener_id of this ListWhitelistsRequest.
        :rtype: str
        """
        return self._listener_id

    @listener_id.setter
    def listener_id(self, listener_id):
        """Sets the listener_id of this ListWhitelistsRequest.


        :param listener_id: The listener_id of this ListWhitelistsRequest.
        :type: str
        """
        self._listener_id = listener_id

    @property
    def whitelist(self):
        """Gets the whitelist of this ListWhitelistsRequest.


        :return: The whitelist of this ListWhitelistsRequest.
        :rtype: str
        """
        return self._whitelist

    @whitelist.setter
    def whitelist(self, whitelist):
        """Sets the whitelist of this ListWhitelistsRequest.


        :param whitelist: The whitelist of this ListWhitelistsRequest.
        :type: str
        """
        self._whitelist = whitelist

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
        if not isinstance(other, ListWhitelistsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
