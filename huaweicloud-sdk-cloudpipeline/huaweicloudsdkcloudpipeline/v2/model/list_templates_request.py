# coding: utf-8

import pprint
import re

import six





class ListTemplatesRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'template_type': 'str',
        'is_build_in': 'str',
        'offset': 'int',
        'limit': 'int',
        'name': 'str',
        'sort': 'str',
        'asc': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'template_type': 'template_type',
        'is_build_in': 'is_build_in',
        'offset': 'offset',
        'limit': 'limit',
        'name': 'name',
        'sort': 'sort',
        'asc': 'asc'
    }

    def __init__(self, x_language=None, template_type=None, is_build_in=None, offset=None, limit=None, name=None, sort=None, asc=None):
        """ListTemplatesRequest - a model defined in huaweicloud sdk"""
        
        

        self._x_language = None
        self._template_type = None
        self._is_build_in = None
        self._offset = None
        self._limit = None
        self._name = None
        self._sort = None
        self._asc = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.template_type = template_type
        self.is_build_in = is_build_in
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if name is not None:
            self.name = name
        if sort is not None:
            self.sort = sort
        if asc is not None:
            self.asc = asc

    @property
    def x_language(self):
        """Gets the x_language of this ListTemplatesRequest.


        :return: The x_language of this ListTemplatesRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListTemplatesRequest.


        :param x_language: The x_language of this ListTemplatesRequest.
        :type: str
        """
        self._x_language = x_language

    @property
    def template_type(self):
        """Gets the template_type of this ListTemplatesRequest.


        :return: The template_type of this ListTemplatesRequest.
        :rtype: str
        """
        return self._template_type

    @template_type.setter
    def template_type(self, template_type):
        """Sets the template_type of this ListTemplatesRequest.


        :param template_type: The template_type of this ListTemplatesRequest.
        :type: str
        """
        self._template_type = template_type

    @property
    def is_build_in(self):
        """Gets the is_build_in of this ListTemplatesRequest.


        :return: The is_build_in of this ListTemplatesRequest.
        :rtype: str
        """
        return self._is_build_in

    @is_build_in.setter
    def is_build_in(self, is_build_in):
        """Sets the is_build_in of this ListTemplatesRequest.


        :param is_build_in: The is_build_in of this ListTemplatesRequest.
        :type: str
        """
        self._is_build_in = is_build_in

    @property
    def offset(self):
        """Gets the offset of this ListTemplatesRequest.


        :return: The offset of this ListTemplatesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListTemplatesRequest.


        :param offset: The offset of this ListTemplatesRequest.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListTemplatesRequest.


        :return: The limit of this ListTemplatesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListTemplatesRequest.


        :param limit: The limit of this ListTemplatesRequest.
        :type: int
        """
        self._limit = limit

    @property
    def name(self):
        """Gets the name of this ListTemplatesRequest.


        :return: The name of this ListTemplatesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListTemplatesRequest.


        :param name: The name of this ListTemplatesRequest.
        :type: str
        """
        self._name = name

    @property
    def sort(self):
        """Gets the sort of this ListTemplatesRequest.


        :return: The sort of this ListTemplatesRequest.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this ListTemplatesRequest.


        :param sort: The sort of this ListTemplatesRequest.
        :type: str
        """
        self._sort = sort

    @property
    def asc(self):
        """Gets the asc of this ListTemplatesRequest.


        :return: The asc of this ListTemplatesRequest.
        :rtype: str
        """
        return self._asc

    @asc.setter
    def asc(self, asc):
        """Sets the asc of this ListTemplatesRequest.


        :param asc: The asc of this ListTemplatesRequest.
        :type: str
        """
        self._asc = asc

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
        if not isinstance(other, ListTemplatesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
