# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExerciseFilter:

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
        'exercise_type': 'list[int]',
        'difficult_ids': 'list[str]',
        'knowledge_point_ids': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'exercise_type': 'exercise_type',
        'difficult_ids': 'difficult_ids',
        'knowledge_point_ids': 'knowledge_point_ids'
    }

    def __init__(self, name=None, exercise_type=None, difficult_ids=None, knowledge_point_ids=None):
        r"""ExerciseFilter

        The model defined in huaweicloud sdk

        :param name: 需查询的习题名称
        :type name: str
        :param exercise_type: 习题类型列表
        :type exercise_type: list[int]
        :param difficult_ids: 难度id列表
        :type difficult_ids: list[str]
        :param knowledge_point_ids: 知识点id列表
        :type knowledge_point_ids: list[str]
        """
        
        

        self._name = None
        self._exercise_type = None
        self._difficult_ids = None
        self._knowledge_point_ids = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if exercise_type is not None:
            self.exercise_type = exercise_type
        if difficult_ids is not None:
            self.difficult_ids = difficult_ids
        if knowledge_point_ids is not None:
            self.knowledge_point_ids = knowledge_point_ids

    @property
    def name(self):
        r"""Gets the name of this ExerciseFilter.

        需查询的习题名称

        :return: The name of this ExerciseFilter.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ExerciseFilter.

        需查询的习题名称

        :param name: The name of this ExerciseFilter.
        :type name: str
        """
        self._name = name

    @property
    def exercise_type(self):
        r"""Gets the exercise_type of this ExerciseFilter.

        习题类型列表

        :return: The exercise_type of this ExerciseFilter.
        :rtype: list[int]
        """
        return self._exercise_type

    @exercise_type.setter
    def exercise_type(self, exercise_type):
        r"""Sets the exercise_type of this ExerciseFilter.

        习题类型列表

        :param exercise_type: The exercise_type of this ExerciseFilter.
        :type exercise_type: list[int]
        """
        self._exercise_type = exercise_type

    @property
    def difficult_ids(self):
        r"""Gets the difficult_ids of this ExerciseFilter.

        难度id列表

        :return: The difficult_ids of this ExerciseFilter.
        :rtype: list[str]
        """
        return self._difficult_ids

    @difficult_ids.setter
    def difficult_ids(self, difficult_ids):
        r"""Sets the difficult_ids of this ExerciseFilter.

        难度id列表

        :param difficult_ids: The difficult_ids of this ExerciseFilter.
        :type difficult_ids: list[str]
        """
        self._difficult_ids = difficult_ids

    @property
    def knowledge_point_ids(self):
        r"""Gets the knowledge_point_ids of this ExerciseFilter.

        知识点id列表

        :return: The knowledge_point_ids of this ExerciseFilter.
        :rtype: list[str]
        """
        return self._knowledge_point_ids

    @knowledge_point_ids.setter
    def knowledge_point_ids(self, knowledge_point_ids):
        r"""Sets the knowledge_point_ids of this ExerciseFilter.

        知识点id列表

        :param knowledge_point_ids: The knowledge_point_ids of this ExerciseFilter.
        :type knowledge_point_ids: list[str]
        """
        self._knowledge_point_ids = knowledge_point_ids

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
        if not isinstance(other, ExerciseFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
