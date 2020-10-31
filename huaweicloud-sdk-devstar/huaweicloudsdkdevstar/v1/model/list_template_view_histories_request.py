# coding: utf-8

import pprint
import re

import six





class ListTemplateViewHistoriesRequest:


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
        'platform_source': 'int'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'platform_source': 'platform_source'
    }

    def __init__(self, x_language='zh-cn', platform_source=None):
        """ListTemplateViewHistoriesRequest - a model defined in huaweicloud sdk"""
        
        

        self._x_language = None
        self._platform_source = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.platform_source = platform_source

    @property
    def x_language(self):
        """Gets the x_language of this ListTemplateViewHistoriesRequest.


        :return: The x_language of this ListTemplateViewHistoriesRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListTemplateViewHistoriesRequest.


        :param x_language: The x_language of this ListTemplateViewHistoriesRequest.
        :type: str
        """
        self._x_language = x_language

    @property
    def platform_source(self):
        """Gets the platform_source of this ListTemplateViewHistoriesRequest.


        :return: The platform_source of this ListTemplateViewHistoriesRequest.
        :rtype: int
        """
        return self._platform_source

    @platform_source.setter
    def platform_source(self, platform_source):
        """Sets the platform_source of this ListTemplateViewHistoriesRequest.


        :param platform_source: The platform_source of this ListTemplateViewHistoriesRequest.
        :type: int
        """
        self._platform_source = platform_source

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
        if not isinstance(other, ListTemplateViewHistoriesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
