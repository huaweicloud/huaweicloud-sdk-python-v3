# coding: utf-8

import pprint
import re

import six





class StacksConfig:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'attributes': 'StacksAttribute',
        'recipe': 'Recipe'
    }

    attribute_map = {
        'attributes': 'attributes',
        'recipe': 'recipe'
    }

    def __init__(self, attributes=None, recipe=None):
        """StacksConfig - a model defined in huaweicloud sdk"""
        
        

        self._attributes = None
        self._recipe = None
        self.discriminator = None

        if attributes is not None:
            self.attributes = attributes
        if recipe is not None:
            self.recipe = recipe

    @property
    def attributes(self):
        """Gets the attributes of this StacksConfig.


        :return: The attributes of this StacksConfig.
        :rtype: StacksAttribute
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this StacksConfig.


        :param attributes: The attributes of this StacksConfig.
        :type: StacksAttribute
        """
        self._attributes = attributes

    @property
    def recipe(self):
        """Gets the recipe of this StacksConfig.


        :return: The recipe of this StacksConfig.
        :rtype: Recipe
        """
        return self._recipe

    @recipe.setter
    def recipe(self, recipe):
        """Sets the recipe of this StacksConfig.


        :param recipe: The recipe of this StacksConfig.
        :type: Recipe
        """
        self._recipe = recipe

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
        if not isinstance(other, StacksConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
