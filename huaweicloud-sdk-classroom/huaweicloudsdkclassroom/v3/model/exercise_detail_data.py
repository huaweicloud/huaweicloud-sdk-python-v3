# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExerciseDetailData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'exercise_code_resource': 'ExerciseCodeResource',
        'exercise_case_resource': 'list[ExerciseCaseResource]'
    }

    attribute_map = {
        'exercise_code_resource': 'exercise_code_resource',
        'exercise_case_resource': 'exercise_case_resource'
    }

    def __init__(self, exercise_code_resource=None, exercise_case_resource=None):
        """ExerciseDetailData

        The model defined in huaweicloud sdk

        :param exercise_code_resource: 
        :type exercise_code_resource: :class:`huaweicloudsdkclassroom.v3.ExerciseCodeResource`
        :param exercise_case_resource: 测试用例信息
        :type exercise_case_resource: list[:class:`huaweicloudsdkclassroom.v3.ExerciseCaseResource`]
        """
        
        

        self._exercise_code_resource = None
        self._exercise_case_resource = None
        self.discriminator = None

        if exercise_code_resource is not None:
            self.exercise_code_resource = exercise_code_resource
        if exercise_case_resource is not None:
            self.exercise_case_resource = exercise_case_resource

    @property
    def exercise_code_resource(self):
        """Gets the exercise_code_resource of this ExerciseDetailData.

        :return: The exercise_code_resource of this ExerciseDetailData.
        :rtype: :class:`huaweicloudsdkclassroom.v3.ExerciseCodeResource`
        """
        return self._exercise_code_resource

    @exercise_code_resource.setter
    def exercise_code_resource(self, exercise_code_resource):
        """Sets the exercise_code_resource of this ExerciseDetailData.

        :param exercise_code_resource: The exercise_code_resource of this ExerciseDetailData.
        :type exercise_code_resource: :class:`huaweicloudsdkclassroom.v3.ExerciseCodeResource`
        """
        self._exercise_code_resource = exercise_code_resource

    @property
    def exercise_case_resource(self):
        """Gets the exercise_case_resource of this ExerciseDetailData.

        测试用例信息

        :return: The exercise_case_resource of this ExerciseDetailData.
        :rtype: list[:class:`huaweicloudsdkclassroom.v3.ExerciseCaseResource`]
        """
        return self._exercise_case_resource

    @exercise_case_resource.setter
    def exercise_case_resource(self, exercise_case_resource):
        """Sets the exercise_case_resource of this ExerciseDetailData.

        测试用例信息

        :param exercise_case_resource: The exercise_case_resource of this ExerciseDetailData.
        :type exercise_case_resource: list[:class:`huaweicloudsdkclassroom.v3.ExerciseCaseResource`]
        """
        self._exercise_case_resource = exercise_case_resource

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
        if not isinstance(other, ExerciseDetailData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
