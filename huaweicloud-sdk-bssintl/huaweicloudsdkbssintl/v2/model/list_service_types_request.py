# coding: utf-8

import pprint
import re

import six





class ListServiceTypesRequest:


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
        'service_type_code': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'service_type_code': 'service_type_code'
    }

    def __init__(self, x_language='zh_cn', service_type_code=None):
        """ListServiceTypesRequest - a model defined in huaweicloud sdk"""
        
        

        self._x_language = None
        self._service_type_code = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        if service_type_code is not None:
            self.service_type_code = service_type_code

    @property
    def x_language(self):
        """Gets the x_language of this ListServiceTypesRequest.


        :return: The x_language of this ListServiceTypesRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListServiceTypesRequest.


        :param x_language: The x_language of this ListServiceTypesRequest.
        :type: str
        """
        self._x_language = x_language

    @property
    def service_type_code(self):
        """Gets the service_type_code of this ListServiceTypesRequest.


        :return: The service_type_code of this ListServiceTypesRequest.
        :rtype: str
        """
        return self._service_type_code

    @service_type_code.setter
    def service_type_code(self, service_type_code):
        """Sets the service_type_code of this ListServiceTypesRequest.


        :param service_type_code: The service_type_code of this ListServiceTypesRequest.
        :type: str
        """
        self._service_type_code = service_type_code

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
        if not isinstance(other, ListServiceTypesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
