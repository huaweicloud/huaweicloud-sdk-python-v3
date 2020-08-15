# coding: utf-8

import pprint
import re

import six





class StacksTag:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'stack_list': 'list[Stacks]',
        'tags': 'list[str]'
    }

    attribute_map = {
        'stack_list': 'stack_list',
        'tags': 'tags'
    }

    def __init__(self, stack_list=None, tags=None):
        """StacksTag - a model defined in huaweicloud sdk"""
        
        

        self._stack_list = None
        self._tags = None
        self.discriminator = None

        if stack_list is not None:
            self.stack_list = stack_list
        if tags is not None:
            self.tags = tags

    @property
    def stack_list(self):
        """Gets the stack_list of this StacksTag.

        技术栈列表

        :return: The stack_list of this StacksTag.
        :rtype: list[Stacks]
        """
        return self._stack_list

    @stack_list.setter
    def stack_list(self, stack_list):
        """Sets the stack_list of this StacksTag.

        技术栈列表

        :param stack_list: The stack_list of this StacksTag.
        :type: list[Stacks]
        """
        self._stack_list = stack_list

    @property
    def tags(self):
        """Gets the tags of this StacksTag.

        技术栈tag集合

        :return: The tags of this StacksTag.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this StacksTag.

        技术栈tag集合

        :param tags: The tags of this StacksTag.
        :type: list[str]
        """
        self._tags = tags

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
        if not isinstance(other, StacksTag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
