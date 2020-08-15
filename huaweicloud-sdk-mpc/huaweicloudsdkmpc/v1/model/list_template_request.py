# coding: utf-8

import pprint
import re

import six





class ListTemplateRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'template_id': 'list[int]',
        'page': 'int',
        'size': 'int'
    }

    attribute_map = {
        'template_id': 'template_id',
        'page': 'page',
        'size': 'size'
    }

    def __init__(self, template_id=None, page=0, size=10):
        """ListTemplateRequest - a model defined in huaweicloud sdk"""
        
        

        self._template_id = None
        self._page = None
        self._size = None
        self.discriminator = None

        if template_id is not None:
            self.template_id = template_id
        if page is not None:
            self.page = page
        if size is not None:
            self.size = size

    @property
    def template_id(self):
        """Gets the template_id of this ListTemplateRequest.


        :return: The template_id of this ListTemplateRequest.
        :rtype: list[int]
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this ListTemplateRequest.


        :param template_id: The template_id of this ListTemplateRequest.
        :type: list[int]
        """
        self._template_id = template_id

    @property
    def page(self):
        """Gets the page of this ListTemplateRequest.


        :return: The page of this ListTemplateRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ListTemplateRequest.


        :param page: The page of this ListTemplateRequest.
        :type: int
        """
        self._page = page

    @property
    def size(self):
        """Gets the size of this ListTemplateRequest.


        :return: The size of this ListTemplateRequest.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ListTemplateRequest.


        :param size: The size of this ListTemplateRequest.
        :type: int
        """
        self._size = size

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
        if not isinstance(other, ListTemplateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
