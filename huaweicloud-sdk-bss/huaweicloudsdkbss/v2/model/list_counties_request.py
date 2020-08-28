# coding: utf-8

import pprint
import re

import six





class ListCountiesRequest:


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
        'city_code': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'city_code': 'city_code',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, x_language='zh_cn', city_code=None, offset=None, limit=10):
        """ListCountiesRequest - a model defined in huaweicloud sdk"""
        
        

        self._x_language = None
        self._city_code = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.city_code = city_code
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def x_language(self):
        """Gets the x_language of this ListCountiesRequest.


        :return: The x_language of this ListCountiesRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListCountiesRequest.


        :param x_language: The x_language of this ListCountiesRequest.
        :type: str
        """
        self._x_language = x_language

    @property
    def city_code(self):
        """Gets the city_code of this ListCountiesRequest.


        :return: The city_code of this ListCountiesRequest.
        :rtype: str
        """
        return self._city_code

    @city_code.setter
    def city_code(self, city_code):
        """Sets the city_code of this ListCountiesRequest.


        :param city_code: The city_code of this ListCountiesRequest.
        :type: str
        """
        self._city_code = city_code

    @property
    def offset(self):
        """Gets the offset of this ListCountiesRequest.


        :return: The offset of this ListCountiesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListCountiesRequest.


        :param offset: The offset of this ListCountiesRequest.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListCountiesRequest.


        :return: The limit of this ListCountiesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListCountiesRequest.


        :param limit: The limit of this ListCountiesRequest.
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
        if not isinstance(other, ListCountiesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
