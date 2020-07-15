# coding: utf-8

import pprint
import re

import six





class ListPredefineTagsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'value': 'str',
        'limit': 'int',
        'marker': 'str',
        'order_field': 'str',
        'order_method': 'str'
    }

    attribute_map = {
        'key': 'key',
        'value': 'value',
        'limit': 'limit',
        'marker': 'marker',
        'order_field': 'order_field',
        'order_method': 'order_method'
    }

    def __init__(self, key=None, value=None, limit=10, marker=None, order_field='update_time', order_method='desc'):
        """ListPredefineTagsRequest - a model defined in huaweicloud sdk"""
        
        

        self._key = None
        self._value = None
        self._limit = None
        self._marker = None
        self._order_field = None
        self._order_method = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if value is not None:
            self.value = value
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if order_field is not None:
            self.order_field = order_field
        if order_method is not None:
            self.order_method = order_method

    @property
    def key(self):
        """Gets the key of this ListPredefineTagsRequest.


        :return: The key of this ListPredefineTagsRequest.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ListPredefineTagsRequest.


        :param key: The key of this ListPredefineTagsRequest.
        :type: str
        """
        self._key = key

    @property
    def value(self):
        """Gets the value of this ListPredefineTagsRequest.


        :return: The value of this ListPredefineTagsRequest.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ListPredefineTagsRequest.


        :param value: The value of this ListPredefineTagsRequest.
        :type: str
        """
        self._value = value

    @property
    def limit(self):
        """Gets the limit of this ListPredefineTagsRequest.


        :return: The limit of this ListPredefineTagsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPredefineTagsRequest.


        :param limit: The limit of this ListPredefineTagsRequest.
        :type: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListPredefineTagsRequest.


        :return: The marker of this ListPredefineTagsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListPredefineTagsRequest.


        :param marker: The marker of this ListPredefineTagsRequest.
        :type: str
        """
        self._marker = marker

    @property
    def order_field(self):
        """Gets the order_field of this ListPredefineTagsRequest.


        :return: The order_field of this ListPredefineTagsRequest.
        :rtype: str
        """
        return self._order_field

    @order_field.setter
    def order_field(self, order_field):
        """Sets the order_field of this ListPredefineTagsRequest.


        :param order_field: The order_field of this ListPredefineTagsRequest.
        :type: str
        """
        self._order_field = order_field

    @property
    def order_method(self):
        """Gets the order_method of this ListPredefineTagsRequest.


        :return: The order_method of this ListPredefineTagsRequest.
        :rtype: str
        """
        return self._order_method

    @order_method.setter
    def order_method(self, order_method):
        """Sets the order_method of this ListPredefineTagsRequest.


        :param order_method: The order_method of this ListPredefineTagsRequest.
        :type: str
        """
        self._order_method = order_method

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
        if not isinstance(other, ListPredefineTagsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
