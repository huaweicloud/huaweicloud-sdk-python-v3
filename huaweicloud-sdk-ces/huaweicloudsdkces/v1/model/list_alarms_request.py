# coding: utf-8

import pprint
import re

import six





class ListAlarmsRequest:


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
        'order': 'str',
        'start': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'order': 'order',
        'start': 'start'
    }

    def __init__(self, limit=None, order=None, start=None):
        """ListAlarmsRequest - a model defined in huaweicloud sdk"""
        
        

        self._limit = None
        self._order = None
        self._start = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if order is not None:
            self.order = order
        if start is not None:
            self.start = start

    @property
    def limit(self):
        """Gets the limit of this ListAlarmsRequest.


        :return: The limit of this ListAlarmsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAlarmsRequest.


        :param limit: The limit of this ListAlarmsRequest.
        :type: int
        """
        self._limit = limit

    @property
    def order(self):
        """Gets the order of this ListAlarmsRequest.


        :return: The order of this ListAlarmsRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this ListAlarmsRequest.


        :param order: The order of this ListAlarmsRequest.
        :type: str
        """
        self._order = order

    @property
    def start(self):
        """Gets the start of this ListAlarmsRequest.


        :return: The start of this ListAlarmsRequest.
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this ListAlarmsRequest.


        :param start: The start of this ListAlarmsRequest.
        :type: str
        """
        self._start = start

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
        if not isinstance(other, ListAlarmsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
