# coding: utf-8

import pprint
import re

import six





class ListCustomPoliciesRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'page': 'int',
        'per_page': 'int'
    }

    attribute_map = {
        'page': 'page',
        'per_page': 'per_page'
    }

    def __init__(self, page=None, per_page=None):
        """ListCustomPoliciesRequest - a model defined in huaweicloud sdk"""
        
        

        self._page = None
        self._per_page = None
        self.discriminator = None

        if page is not None:
            self.page = page
        if per_page is not None:
            self.per_page = per_page

    @property
    def page(self):
        """Gets the page of this ListCustomPoliciesRequest.


        :return: The page of this ListCustomPoliciesRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ListCustomPoliciesRequest.


        :param page: The page of this ListCustomPoliciesRequest.
        :type: int
        """
        self._page = page

    @property
    def per_page(self):
        """Gets the per_page of this ListCustomPoliciesRequest.


        :return: The per_page of this ListCustomPoliciesRequest.
        :rtype: int
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        """Sets the per_page of this ListCustomPoliciesRequest.


        :param per_page: The per_page of this ListCustomPoliciesRequest.
        :type: int
        """
        self._per_page = per_page

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
        if not isinstance(other, ListCustomPoliciesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
