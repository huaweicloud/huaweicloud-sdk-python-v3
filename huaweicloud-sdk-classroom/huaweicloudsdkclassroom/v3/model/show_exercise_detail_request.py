# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowExerciseDetailRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'exercise_id': 'str'
    }

    attribute_map = {
        'exercise_id': 'exercise_id'
    }

    def __init__(self, exercise_id=None):
        """ShowExerciseDetailRequest

        The model defined in huaweicloud sdk

        :param exercise_id: 需查询的习题id
        :type exercise_id: str
        """
        
        

        self._exercise_id = None
        self.discriminator = None

        self.exercise_id = exercise_id

    @property
    def exercise_id(self):
        """Gets the exercise_id of this ShowExerciseDetailRequest.

        需查询的习题id

        :return: The exercise_id of this ShowExerciseDetailRequest.
        :rtype: str
        """
        return self._exercise_id

    @exercise_id.setter
    def exercise_id(self, exercise_id):
        """Sets the exercise_id of this ShowExerciseDetailRequest.

        需查询的习题id

        :param exercise_id: The exercise_id of this ShowExerciseDetailRequest.
        :type exercise_id: str
        """
        self._exercise_id = exercise_id

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
        if not isinstance(other, ShowExerciseDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
