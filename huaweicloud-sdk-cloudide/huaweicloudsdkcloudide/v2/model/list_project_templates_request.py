# coding: utf-8

import pprint
import re

import six





class ListProjectTemplatesRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'arch': 'str',
        'stack_id': 'str'
    }

    attribute_map = {
        'arch': 'arch',
        'stack_id': 'stack_id'
    }

    def __init__(self, arch=None, stack_id=None):
        """ListProjectTemplatesRequest - a model defined in huaweicloud sdk"""
        
        

        self._arch = None
        self._stack_id = None
        self.discriminator = None

        if arch is not None:
            self.arch = arch
        self.stack_id = stack_id

    @property
    def arch(self):
        """Gets the arch of this ListProjectTemplatesRequest.


        :return: The arch of this ListProjectTemplatesRequest.
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        """Sets the arch of this ListProjectTemplatesRequest.


        :param arch: The arch of this ListProjectTemplatesRequest.
        :type: str
        """
        self._arch = arch

    @property
    def stack_id(self):
        """Gets the stack_id of this ListProjectTemplatesRequest.


        :return: The stack_id of this ListProjectTemplatesRequest.
        :rtype: str
        """
        return self._stack_id

    @stack_id.setter
    def stack_id(self, stack_id):
        """Sets the stack_id of this ListProjectTemplatesRequest.


        :param stack_id: The stack_id of this ListProjectTemplatesRequest.
        :type: str
        """
        self._stack_id = stack_id

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
        if not isinstance(other, ListProjectTemplatesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
