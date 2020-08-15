# coding: utf-8

import pprint
import re

import six





class ListComponentsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'application_id': 'str',
        'limit': 'int',
        'offset': 'int',
        'order_by': 'str',
        'order': 'str'
    }

    attribute_map = {
        'application_id': 'application_id',
        'limit': 'limit',
        'offset': 'offset',
        'order_by': 'order_by',
        'order': 'order'
    }

    def __init__(self, application_id=None, limit=None, offset=None, order_by=None, order=None):
        """ListComponentsRequest - a model defined in huaweicloud sdk"""
        
        

        self._application_id = None
        self._limit = None
        self._offset = None
        self._order_by = None
        self._order = None
        self.discriminator = None

        self.application_id = application_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if order_by is not None:
            self.order_by = order_by
        if order is not None:
            self.order = order

    @property
    def application_id(self):
        """Gets the application_id of this ListComponentsRequest.


        :return: The application_id of this ListComponentsRequest.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this ListComponentsRequest.


        :param application_id: The application_id of this ListComponentsRequest.
        :type: str
        """
        self._application_id = application_id

    @property
    def limit(self):
        """Gets the limit of this ListComponentsRequest.


        :return: The limit of this ListComponentsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListComponentsRequest.


        :param limit: The limit of this ListComponentsRequest.
        :type: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListComponentsRequest.


        :return: The offset of this ListComponentsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListComponentsRequest.


        :param offset: The offset of this ListComponentsRequest.
        :type: int
        """
        self._offset = offset

    @property
    def order_by(self):
        """Gets the order_by of this ListComponentsRequest.


        :return: The order_by of this ListComponentsRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        """Sets the order_by of this ListComponentsRequest.


        :param order_by: The order_by of this ListComponentsRequest.
        :type: str
        """
        self._order_by = order_by

    @property
    def order(self):
        """Gets the order of this ListComponentsRequest.


        :return: The order of this ListComponentsRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this ListComponentsRequest.


        :param order: The order of this ListComponentsRequest.
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
        if not isinstance(other, ListComponentsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
