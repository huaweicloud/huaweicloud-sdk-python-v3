# coding: utf-8

import pprint
import re

import six





class ListPipleineBuildResultRequest:


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
        'start_date': 'str',
        'end_date': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, x_language=None, start_date=None, end_date=None, offset=None, limit=None):
        """ListPipleineBuildResultRequest - a model defined in huaweicloud sdk"""
        
        

        self._x_language = None
        self._start_date = None
        self._end_date = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.start_date = start_date
        self.end_date = end_date
        self.offset = offset
        self.limit = limit

    @property
    def x_language(self):
        """Gets the x_language of this ListPipleineBuildResultRequest.


        :return: The x_language of this ListPipleineBuildResultRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListPipleineBuildResultRequest.


        :param x_language: The x_language of this ListPipleineBuildResultRequest.
        :type: str
        """
        self._x_language = x_language

    @property
    def start_date(self):
        """Gets the start_date of this ListPipleineBuildResultRequest.


        :return: The start_date of this ListPipleineBuildResultRequest.
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ListPipleineBuildResultRequest.


        :param start_date: The start_date of this ListPipleineBuildResultRequest.
        :type: str
        """
        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this ListPipleineBuildResultRequest.


        :return: The end_date of this ListPipleineBuildResultRequest.
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this ListPipleineBuildResultRequest.


        :param end_date: The end_date of this ListPipleineBuildResultRequest.
        :type: str
        """
        self._end_date = end_date

    @property
    def offset(self):
        """Gets the offset of this ListPipleineBuildResultRequest.


        :return: The offset of this ListPipleineBuildResultRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListPipleineBuildResultRequest.


        :param offset: The offset of this ListPipleineBuildResultRequest.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListPipleineBuildResultRequest.


        :return: The limit of this ListPipleineBuildResultRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPipleineBuildResultRequest.


        :param limit: The limit of this ListPipleineBuildResultRequest.
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
        if not isinstance(other, ListPipleineBuildResultRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
