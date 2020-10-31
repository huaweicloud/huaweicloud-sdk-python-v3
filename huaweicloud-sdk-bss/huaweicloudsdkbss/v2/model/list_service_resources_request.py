# coding: utf-8

import pprint
import re

import six





class ListServiceResourcesRequest:


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
        'service_type_code': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'service_type_code': 'service_type_code',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, x_language='zh_cn', service_type_code=None, limit=10, offset=0):
        """ListServiceResourcesRequest - a model defined in huaweicloud sdk"""
        
        

        self._x_language = None
        self._service_type_code = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.service_type_code = service_type_code
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def x_language(self):
        """Gets the x_language of this ListServiceResourcesRequest.


        :return: The x_language of this ListServiceResourcesRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListServiceResourcesRequest.


        :param x_language: The x_language of this ListServiceResourcesRequest.
        :type: str
        """
        self._x_language = x_language

    @property
    def service_type_code(self):
        """Gets the service_type_code of this ListServiceResourcesRequest.


        :return: The service_type_code of this ListServiceResourcesRequest.
        :rtype: str
        """
        return self._service_type_code

    @service_type_code.setter
    def service_type_code(self, service_type_code):
        """Sets the service_type_code of this ListServiceResourcesRequest.


        :param service_type_code: The service_type_code of this ListServiceResourcesRequest.
        :type: str
        """
        self._service_type_code = service_type_code

    @property
    def limit(self):
        """Gets the limit of this ListServiceResourcesRequest.


        :return: The limit of this ListServiceResourcesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListServiceResourcesRequest.


        :param limit: The limit of this ListServiceResourcesRequest.
        :type: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListServiceResourcesRequest.


        :return: The offset of this ListServiceResourcesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListServiceResourcesRequest.


        :param offset: The offset of this ListServiceResourcesRequest.
        :type: int
        """
        self._offset = offset

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
        if not isinstance(other, ListServiceResourcesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
