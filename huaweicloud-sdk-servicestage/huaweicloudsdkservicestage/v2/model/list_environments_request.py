# coding: utf-8

import pprint
import re

import six





class ListEnvironmentsRequest:


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
        'offset': 'int',
        'order_by': 'str',
        'order': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'order_by': 'order_by',
        'order': 'order'
    }

    def __init__(self, limit=None, offset=None, order_by=None, order=None):
        """ListEnvironmentsRequest - a model defined in huaweicloud sdk"""
        
        

        self._limit = None
        self._offset = None
        self._order_by = None
        self._order = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if order_by is not None:
            self.order_by = order_by
        if order is not None:
            self.order = order

    @property
    def limit(self):
        """Gets the limit of this ListEnvironmentsRequest.


        :return: The limit of this ListEnvironmentsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListEnvironmentsRequest.


        :param limit: The limit of this ListEnvironmentsRequest.
        :type: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListEnvironmentsRequest.


        :return: The offset of this ListEnvironmentsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListEnvironmentsRequest.


        :param offset: The offset of this ListEnvironmentsRequest.
        :type: int
        """
        self._offset = offset

    @property
    def order_by(self):
        """Gets the order_by of this ListEnvironmentsRequest.


        :return: The order_by of this ListEnvironmentsRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        """Sets the order_by of this ListEnvironmentsRequest.


        :param order_by: The order_by of this ListEnvironmentsRequest.
        :type: str
        """
        self._order_by = order_by

    @property
    def order(self):
        """Gets the order of this ListEnvironmentsRequest.


        :return: The order of this ListEnvironmentsRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this ListEnvironmentsRequest.


        :param order: The order of this ListEnvironmentsRequest.
        :type: str
        """
        self._order = order

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
        if not isinstance(other, ListEnvironmentsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
