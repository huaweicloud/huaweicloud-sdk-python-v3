# coding: utf-8

import pprint
import re

import six





class ExerciseGroup:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'exercises': 'list[ExerciseCard]',
        'type': 'str'
    }

    attribute_map = {
        'exercises': 'exercises',
        'type': 'type'
    }

    def __init__(self, exercises=None, type=None):
        """ExerciseGroup - a model defined in huaweicloud sdk"""
        
        

        self._exercises = None
        self._type = None
        self.discriminator = None

        self.exercises = exercises
        self.type = type

    @property
    def exercises(self):
        """Gets the exercises of this ExerciseGroup.

        习题列表

        :return: The exercises of this ExerciseGroup.
        :rtype: list[ExerciseCard]
        """
        return self._exercises

    @exercises.setter
    def exercises(self, exercises):
        """Sets the exercises of this ExerciseGroup.

        习题列表

        :param exercises: The exercises of this ExerciseGroup.
        :type: list[ExerciseCard]
        """
        self._exercises = exercises

    @property
    def type(self):
        """Gets the type of this ExerciseGroup.

        习题分类

        :return: The type of this ExerciseGroup.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ExerciseGroup.

        习题分类

        :param type: The type of this ExerciseGroup.
        :type: str
        """
        self._type = type

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
        if not isinstance(other, ExerciseGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
