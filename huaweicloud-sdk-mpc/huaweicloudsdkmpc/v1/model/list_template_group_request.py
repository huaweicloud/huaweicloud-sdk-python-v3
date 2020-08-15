# coding: utf-8

import pprint
import re

import six





class ListTemplateGroupRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'group_id': 'list[str]',
        'group_name': 'list[str]',
        'page': 'int',
        'size': 'int'
    }

    attribute_map = {
        'group_id': 'group_id',
        'group_name': 'group_name',
        'page': 'page',
        'size': 'size'
    }

    def __init__(self, group_id=None, group_name=None, page=0, size=10):
        """ListTemplateGroupRequest - a model defined in huaweicloud sdk"""
        
        

        self._group_id = None
        self._group_name = None
        self._page = None
        self._size = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if group_name is not None:
            self.group_name = group_name
        if page is not None:
            self.page = page
        if size is not None:
            self.size = size

    @property
    def group_id(self):
        """Gets the group_id of this ListTemplateGroupRequest.


        :return: The group_id of this ListTemplateGroupRequest.
        :rtype: list[str]
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ListTemplateGroupRequest.


        :param group_id: The group_id of this ListTemplateGroupRequest.
        :type: list[str]
        """
        self._group_id = group_id

    @property
    def group_name(self):
        """Gets the group_name of this ListTemplateGroupRequest.


        :return: The group_name of this ListTemplateGroupRequest.
        :rtype: list[str]
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this ListTemplateGroupRequest.


        :param group_name: The group_name of this ListTemplateGroupRequest.
        :type: list[str]
        """
        self._group_name = group_name

    @property
    def page(self):
        """Gets the page of this ListTemplateGroupRequest.


        :return: The page of this ListTemplateGroupRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ListTemplateGroupRequest.


        :param page: The page of this ListTemplateGroupRequest.
        :type: int
        """
        self._page = page

    @property
    def size(self):
        """Gets the size of this ListTemplateGroupRequest.


        :return: The size of this ListTemplateGroupRequest.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ListTemplateGroupRequest.


        :param size: The size of this ListTemplateGroupRequest.
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
        if not isinstance(other, ListTemplateGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
