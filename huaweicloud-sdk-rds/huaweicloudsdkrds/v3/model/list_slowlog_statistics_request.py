# coding: utf-8

import pprint
import re

import six





class ListSlowlogStatisticsRequest:


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
        'instance_id': 'str',
        'cur_page': 'int',
        'per_page': 'int',
        'start_date': 'str',
        'end_date': 'str',
        'type': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'instance_id': 'instance_id',
        'cur_page': 'cur_page',
        'per_page': 'per_page',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'type': 'type'
    }

    def __init__(self, x_language=None, instance_id=None, cur_page=None, per_page=None, start_date=None, end_date=None, type=None):
        """ListSlowlogStatisticsRequest - a model defined in huaweicloud sdk"""
        
        

        self._x_language = None
        self._instance_id = None
        self._cur_page = None
        self._per_page = None
        self._start_date = None
        self._end_date = None
        self._type = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.instance_id = instance_id
        self.cur_page = cur_page
        self.per_page = per_page
        self.start_date = start_date
        self.end_date = end_date
        self.type = type

    @property
    def x_language(self):
        """Gets the x_language of this ListSlowlogStatisticsRequest.


        :return: The x_language of this ListSlowlogStatisticsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListSlowlogStatisticsRequest.


        :param x_language: The x_language of this ListSlowlogStatisticsRequest.
        :type: str
        """
        self._x_language = x_language

    @property
    def instance_id(self):
        """Gets the instance_id of this ListSlowlogStatisticsRequest.


        :return: The instance_id of this ListSlowlogStatisticsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListSlowlogStatisticsRequest.


        :param instance_id: The instance_id of this ListSlowlogStatisticsRequest.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def cur_page(self):
        """Gets the cur_page of this ListSlowlogStatisticsRequest.


        :return: The cur_page of this ListSlowlogStatisticsRequest.
        :rtype: int
        """
        return self._cur_page

    @cur_page.setter
    def cur_page(self, cur_page):
        """Sets the cur_page of this ListSlowlogStatisticsRequest.


        :param cur_page: The cur_page of this ListSlowlogStatisticsRequest.
        :type: int
        """
        self._cur_page = cur_page

    @property
    def per_page(self):
        """Gets the per_page of this ListSlowlogStatisticsRequest.


        :return: The per_page of this ListSlowlogStatisticsRequest.
        :rtype: int
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        """Sets the per_page of this ListSlowlogStatisticsRequest.


        :param per_page: The per_page of this ListSlowlogStatisticsRequest.
        :type: int
        """
        self._per_page = per_page

    @property
    def start_date(self):
        """Gets the start_date of this ListSlowlogStatisticsRequest.


        :return: The start_date of this ListSlowlogStatisticsRequest.
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ListSlowlogStatisticsRequest.


        :param start_date: The start_date of this ListSlowlogStatisticsRequest.
        :type: str
        """
        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this ListSlowlogStatisticsRequest.


        :return: The end_date of this ListSlowlogStatisticsRequest.
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this ListSlowlogStatisticsRequest.


        :param end_date: The end_date of this ListSlowlogStatisticsRequest.
        :type: str
        """
        self._end_date = end_date

    @property
    def type(self):
        """Gets the type of this ListSlowlogStatisticsRequest.


        :return: The type of this ListSlowlogStatisticsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListSlowlogStatisticsRequest.


        :param type: The type of this ListSlowlogStatisticsRequest.
        :type: str
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
        if not isinstance(other, ListSlowlogStatisticsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
