# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExerciseCard:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'exercise_id': 'str',
        'description': 'str',
        'resource_sub_type': 'int',
        'target_score': 'int'
    }

    attribute_map = {
        'name': 'name',
        'exercise_id': 'exercise_id',
        'description': 'description',
        'resource_sub_type': 'resource_sub_type',
        'target_score': 'target_score'
    }

    def __init__(self, name=None, exercise_id=None, description=None, resource_sub_type=None, target_score=None):
        r"""ExerciseCard

        The model defined in huaweicloud sdk

        :param name: 习题名称
        :type name: str
        :param exercise_id: 习题ID
        :type exercise_id: str
        :param description: 习题描述
        :type description: str
        :param resource_sub_type: 习题子类型 1：函数c 2：函数c++ 3：函数Java 4：函数Python 5：单人项目java 6：单人项目Hadoop 7：通用 8：企业级软件项目 10：web习题 11：AI习题 12：单选题 13：多选题 14：填空题 15：单人项目C 16：单人项目C++
        :type resource_sub_type: int
        :param target_score: 习题分值
        :type target_score: int
        """
        
        

        self._name = None
        self._exercise_id = None
        self._description = None
        self._resource_sub_type = None
        self._target_score = None
        self.discriminator = None

        self.name = name
        self.exercise_id = exercise_id
        self.description = description
        self.resource_sub_type = resource_sub_type
        self.target_score = target_score

    @property
    def name(self):
        r"""Gets the name of this ExerciseCard.

        习题名称

        :return: The name of this ExerciseCard.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ExerciseCard.

        习题名称

        :param name: The name of this ExerciseCard.
        :type name: str
        """
        self._name = name

    @property
    def exercise_id(self):
        r"""Gets the exercise_id of this ExerciseCard.

        习题ID

        :return: The exercise_id of this ExerciseCard.
        :rtype: str
        """
        return self._exercise_id

    @exercise_id.setter
    def exercise_id(self, exercise_id):
        r"""Sets the exercise_id of this ExerciseCard.

        习题ID

        :param exercise_id: The exercise_id of this ExerciseCard.
        :type exercise_id: str
        """
        self._exercise_id = exercise_id

    @property
    def description(self):
        r"""Gets the description of this ExerciseCard.

        习题描述

        :return: The description of this ExerciseCard.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ExerciseCard.

        习题描述

        :param description: The description of this ExerciseCard.
        :type description: str
        """
        self._description = description

    @property
    def resource_sub_type(self):
        r"""Gets the resource_sub_type of this ExerciseCard.

        习题子类型 1：函数c 2：函数c++ 3：函数Java 4：函数Python 5：单人项目java 6：单人项目Hadoop 7：通用 8：企业级软件项目 10：web习题 11：AI习题 12：单选题 13：多选题 14：填空题 15：单人项目C 16：单人项目C++

        :return: The resource_sub_type of this ExerciseCard.
        :rtype: int
        """
        return self._resource_sub_type

    @resource_sub_type.setter
    def resource_sub_type(self, resource_sub_type):
        r"""Sets the resource_sub_type of this ExerciseCard.

        习题子类型 1：函数c 2：函数c++ 3：函数Java 4：函数Python 5：单人项目java 6：单人项目Hadoop 7：通用 8：企业级软件项目 10：web习题 11：AI习题 12：单选题 13：多选题 14：填空题 15：单人项目C 16：单人项目C++

        :param resource_sub_type: The resource_sub_type of this ExerciseCard.
        :type resource_sub_type: int
        """
        self._resource_sub_type = resource_sub_type

    @property
    def target_score(self):
        r"""Gets the target_score of this ExerciseCard.

        习题分值

        :return: The target_score of this ExerciseCard.
        :rtype: int
        """
        return self._target_score

    @target_score.setter
    def target_score(self, target_score):
        r"""Sets the target_score of this ExerciseCard.

        习题分值

        :param target_score: The target_score of this ExerciseCard.
        :type target_score: int
        """
        self._target_score = target_score

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
        if not isinstance(other, ExerciseCard):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
