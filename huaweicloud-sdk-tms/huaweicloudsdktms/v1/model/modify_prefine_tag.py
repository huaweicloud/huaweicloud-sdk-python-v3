# coding: utf-8

import pprint
import re

import six





class ModifyPrefineTag:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'new_tag': 'PredefineTagRequest',
        'old_tag': 'PredefineTagRequest'
    }

    attribute_map = {
        'new_tag': 'new_tag',
        'old_tag': 'old_tag'
    }

    def __init__(self, new_tag=None, old_tag=None):
        """ModifyPrefineTag - a model defined in huaweicloud sdk"""
        
        

        self._new_tag = None
        self._old_tag = None
        self.discriminator = None

        self.new_tag = new_tag
        self.old_tag = old_tag

    @property
    def new_tag(self):
        """Gets the new_tag of this ModifyPrefineTag.


        :return: The new_tag of this ModifyPrefineTag.
        :rtype: PredefineTagRequest
        """
        return self._new_tag

    @new_tag.setter
    def new_tag(self, new_tag):
        """Sets the new_tag of this ModifyPrefineTag.


        :param new_tag: The new_tag of this ModifyPrefineTag.
        :type: PredefineTagRequest
        """
        self._new_tag = new_tag

    @property
    def old_tag(self):
        """Gets the old_tag of this ModifyPrefineTag.


        :return: The old_tag of this ModifyPrefineTag.
        :rtype: PredefineTagRequest
        """
        return self._old_tag

    @old_tag.setter
    def old_tag(self, old_tag):
        """Sets the old_tag of this ModifyPrefineTag.


        :param old_tag: The old_tag of this ModifyPrefineTag.
        :type: PredefineTagRequest
        """
        self._old_tag = old_tag

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
        if not isinstance(other, ModifyPrefineTag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
