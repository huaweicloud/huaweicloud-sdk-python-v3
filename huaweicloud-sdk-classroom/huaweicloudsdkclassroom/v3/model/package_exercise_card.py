# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PackageExerciseCard:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'difficult': 'DifficultInfo',
        'exercise_type': 'int',
        'exercise_type_name': 'str',
        'order_count': 'int',
        'knowledge_point': 'list[KnowledgePointInfo]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'difficult': 'difficult',
        'exercise_type': 'exercise_type',
        'exercise_type_name': 'exercise_type_name',
        'order_count': 'order_count',
        'knowledge_point': 'knowledge_point'
    }

    def __init__(self, id=None, name=None, difficult=None, exercise_type=None, exercise_type_name=None, order_count=None, knowledge_point=None):
        """PackageExerciseCard

        The model defined in huaweicloud sdk

        :param id: 习题id
        :type id: str
        :param name: 习题名称
        :type name: str
        :param difficult: 
        :type difficult: :class:`huaweicloudsdkclassroom.v3.DifficultInfo`
        :param exercise_type: 习题类型编号
        :type exercise_type: int
        :param exercise_type_name: 习题类型名称
        :type exercise_type_name: str
        :param order_count: 习题库里习题编号
        :type order_count: int
        :param knowledge_point: 相关知识点
        :type knowledge_point: list[:class:`huaweicloudsdkclassroom.v3.KnowledgePointInfo`]
        """
        
        

        self._id = None
        self._name = None
        self._difficult = None
        self._exercise_type = None
        self._exercise_type_name = None
        self._order_count = None
        self._knowledge_point = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if difficult is not None:
            self.difficult = difficult
        if exercise_type is not None:
            self.exercise_type = exercise_type
        if exercise_type_name is not None:
            self.exercise_type_name = exercise_type_name
        if order_count is not None:
            self.order_count = order_count
        if knowledge_point is not None:
            self.knowledge_point = knowledge_point

    @property
    def id(self):
        """Gets the id of this PackageExerciseCard.

        习题id

        :return: The id of this PackageExerciseCard.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PackageExerciseCard.

        习题id

        :param id: The id of this PackageExerciseCard.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this PackageExerciseCard.

        习题名称

        :return: The name of this PackageExerciseCard.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PackageExerciseCard.

        习题名称

        :param name: The name of this PackageExerciseCard.
        :type name: str
        """
        self._name = name

    @property
    def difficult(self):
        """Gets the difficult of this PackageExerciseCard.

        :return: The difficult of this PackageExerciseCard.
        :rtype: :class:`huaweicloudsdkclassroom.v3.DifficultInfo`
        """
        return self._difficult

    @difficult.setter
    def difficult(self, difficult):
        """Sets the difficult of this PackageExerciseCard.

        :param difficult: The difficult of this PackageExerciseCard.
        :type difficult: :class:`huaweicloudsdkclassroom.v3.DifficultInfo`
        """
        self._difficult = difficult

    @property
    def exercise_type(self):
        """Gets the exercise_type of this PackageExerciseCard.

        习题类型编号

        :return: The exercise_type of this PackageExerciseCard.
        :rtype: int
        """
        return self._exercise_type

    @exercise_type.setter
    def exercise_type(self, exercise_type):
        """Sets the exercise_type of this PackageExerciseCard.

        习题类型编号

        :param exercise_type: The exercise_type of this PackageExerciseCard.
        :type exercise_type: int
        """
        self._exercise_type = exercise_type

    @property
    def exercise_type_name(self):
        """Gets the exercise_type_name of this PackageExerciseCard.

        习题类型名称

        :return: The exercise_type_name of this PackageExerciseCard.
        :rtype: str
        """
        return self._exercise_type_name

    @exercise_type_name.setter
    def exercise_type_name(self, exercise_type_name):
        """Sets the exercise_type_name of this PackageExerciseCard.

        习题类型名称

        :param exercise_type_name: The exercise_type_name of this PackageExerciseCard.
        :type exercise_type_name: str
        """
        self._exercise_type_name = exercise_type_name

    @property
    def order_count(self):
        """Gets the order_count of this PackageExerciseCard.

        习题库里习题编号

        :return: The order_count of this PackageExerciseCard.
        :rtype: int
        """
        return self._order_count

    @order_count.setter
    def order_count(self, order_count):
        """Sets the order_count of this PackageExerciseCard.

        习题库里习题编号

        :param order_count: The order_count of this PackageExerciseCard.
        :type order_count: int
        """
        self._order_count = order_count

    @property
    def knowledge_point(self):
        """Gets the knowledge_point of this PackageExerciseCard.

        相关知识点

        :return: The knowledge_point of this PackageExerciseCard.
        :rtype: list[:class:`huaweicloudsdkclassroom.v3.KnowledgePointInfo`]
        """
        return self._knowledge_point

    @knowledge_point.setter
    def knowledge_point(self, knowledge_point):
        """Sets the knowledge_point of this PackageExerciseCard.

        相关知识点

        :param knowledge_point: The knowledge_point of this PackageExerciseCard.
        :type knowledge_point: list[:class:`huaweicloudsdkclassroom.v3.KnowledgePointInfo`]
        """
        self._knowledge_point = knowledge_point

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
        if not isinstance(other, PackageExerciseCard):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
