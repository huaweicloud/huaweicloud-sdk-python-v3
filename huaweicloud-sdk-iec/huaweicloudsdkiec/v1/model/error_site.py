# coding: utf-8

import pprint
import re

import six





class ErrorSite:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'err_sites': 'list[str]'
    }

    attribute_map = {
        'err_sites': 'err_sites'
    }

    def __init__(self, err_sites=None):
        """ErrorSite - a model defined in huaweicloud sdk"""
        
        

        self._err_sites = None
        self.discriminator = None

        if err_sites is not None:
            self.err_sites = err_sites

    @property
    def err_sites(self):
        """Gets the err_sites of this ErrorSite.

        异常站点。

        :return: The err_sites of this ErrorSite.
        :rtype: list[str]
        """
        return self._err_sites

    @err_sites.setter
    def err_sites(self, err_sites):
        """Sets the err_sites of this ErrorSite.

        异常站点。

        :param err_sites: The err_sites of this ErrorSite.
        :type: list[str]
        """
        self._err_sites = err_sites

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
        if not isinstance(other, ErrorSite):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
