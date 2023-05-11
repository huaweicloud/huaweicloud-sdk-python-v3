# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJobExercisesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_exercises': 'list[ExerciseGroup]',
        'total': 'int'
    }

    attribute_map = {
        'group_exercises': 'group_exercises',
        'total': 'total'
    }

    def __init__(self, group_exercises=None, total=None):
        """ShowJobExercisesResponse

        The model defined in huaweicloud sdk

        :param group_exercises: 作业下习题列表
        :type group_exercises: list[:class:`huaweicloudsdkclassroom.v3.ExerciseGroup`]
        :param total: 作业下习题总数
        :type total: int
        """
        
        super(ShowJobExercisesResponse, self).__init__()

        self._group_exercises = None
        self._total = None
        self.discriminator = None

        if group_exercises is not None:
            self.group_exercises = group_exercises
        if total is not None:
            self.total = total

    @property
    def group_exercises(self):
        """Gets the group_exercises of this ShowJobExercisesResponse.

        作业下习题列表

        :return: The group_exercises of this ShowJobExercisesResponse.
        :rtype: list[:class:`huaweicloudsdkclassroom.v3.ExerciseGroup`]
        """
        return self._group_exercises

    @group_exercises.setter
    def group_exercises(self, group_exercises):
        """Sets the group_exercises of this ShowJobExercisesResponse.

        作业下习题列表

        :param group_exercises: The group_exercises of this ShowJobExercisesResponse.
        :type group_exercises: list[:class:`huaweicloudsdkclassroom.v3.ExerciseGroup`]
        """
        self._group_exercises = group_exercises

    @property
    def total(self):
        """Gets the total of this ShowJobExercisesResponse.

        作业下习题总数

        :return: The total of this ShowJobExercisesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ShowJobExercisesResponse.

        作业下习题总数

        :param total: The total of this ShowJobExercisesResponse.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, ShowJobExercisesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
