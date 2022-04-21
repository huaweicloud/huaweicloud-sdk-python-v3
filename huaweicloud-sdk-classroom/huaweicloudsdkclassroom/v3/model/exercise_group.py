# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        """ExerciseGroup

        The model defined in huaweicloud sdk

        :param exercises: 习题列表
        :type exercises: list[:class:`huaweicloudsdkclassroom.v3.ExerciseCard`]
        :param type: 习题分类
        :type type: str
        """
        
        

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
        :rtype: list[:class:`huaweicloudsdkclassroom.v3.ExerciseCard`]
        """
        return self._exercises

    @exercises.setter
    def exercises(self, exercises):
        """Sets the exercises of this ExerciseGroup.

        习题列表

        :param exercises: The exercises of this ExerciseGroup.
        :type exercises: list[:class:`huaweicloudsdkclassroom.v3.ExerciseCard`]
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
        :type type: str
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
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ExerciseGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
