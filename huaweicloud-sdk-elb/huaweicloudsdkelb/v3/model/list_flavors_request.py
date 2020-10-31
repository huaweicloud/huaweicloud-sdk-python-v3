# coding: utf-8

import pprint
import re

import six





class ListFlavorsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'list[str]',
        'limit': 'int',
        'marker': 'str',
        'name': 'list[str]',
        'page_reverse': 'bool',
        'shared': 'bool',
        'type': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'limit': 'limit',
        'marker': 'marker',
        'name': 'name',
        'page_reverse': 'page_reverse',
        'shared': 'shared',
        'type': 'type'
    }

    def __init__(self, id=None, limit=None, marker=None, name=None, page_reverse=None, shared=None, type=None):
        """ListFlavorsRequest - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._limit = None
        self._marker = None
        self._name = None
        self._page_reverse = None
        self._shared = None
        self._type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if name is not None:
            self.name = name
        if page_reverse is not None:
            self.page_reverse = page_reverse
        if shared is not None:
            self.shared = shared
        if type is not None:
            self.type = type

    @property
    def id(self):
        """Gets the id of this ListFlavorsRequest.


        :return: The id of this ListFlavorsRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListFlavorsRequest.


        :param id: The id of this ListFlavorsRequest.
        :type: list[str]
        """
        self._id = id

    @property
    def limit(self):
        """Gets the limit of this ListFlavorsRequest.


        :return: The limit of this ListFlavorsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListFlavorsRequest.


        :param limit: The limit of this ListFlavorsRequest.
        :type: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListFlavorsRequest.


        :return: The marker of this ListFlavorsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListFlavorsRequest.


        :param marker: The marker of this ListFlavorsRequest.
        :type: str
        """
        self._marker = marker

    @property
    def name(self):
        """Gets the name of this ListFlavorsRequest.


        :return: The name of this ListFlavorsRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListFlavorsRequest.


        :param name: The name of this ListFlavorsRequest.
        :type: list[str]
        """
        self._name = name

    @property
    def page_reverse(self):
        """Gets the page_reverse of this ListFlavorsRequest.


        :return: The page_reverse of this ListFlavorsRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        """Sets the page_reverse of this ListFlavorsRequest.


        :param page_reverse: The page_reverse of this ListFlavorsRequest.
        :type: bool
        """
        self._page_reverse = page_reverse

    @property
    def shared(self):
        """Gets the shared of this ListFlavorsRequest.


        :return: The shared of this ListFlavorsRequest.
        :rtype: bool
        """
        return self._shared

    @shared.setter
    def shared(self, shared):
        """Sets the shared of this ListFlavorsRequest.


        :param shared: The shared of this ListFlavorsRequest.
        :type: bool
        """
        self._shared = shared

    @property
    def type(self):
        """Gets the type of this ListFlavorsRequest.


        :return: The type of this ListFlavorsRequest.
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListFlavorsRequest.


        :param type: The type of this ListFlavorsRequest.
        :type: list[str]
        """
        self._type = type

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
        if not isinstance(other, ListFlavorsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
