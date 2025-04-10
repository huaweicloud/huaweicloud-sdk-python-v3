# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowExerciseDetailResponse(SdkResponse):

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
        'description': 'str',
        'difficult': 'DifficultInfo',
        'exercise_type': 'int',
        'exercise_type_name': 'str',
        'order_count': 'int',
        'test_case_description': 'str',
        'knowledge_point': 'list[KnowledgePointInfo]',
        'judge_type': 'int',
        'exercise_data': 'ExerciseDetailData'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'difficult': 'difficult',
        'exercise_type': 'exercise_type',
        'exercise_type_name': 'exercise_type_name',
        'order_count': 'order_count',
        'test_case_description': 'test_case_description',
        'knowledge_point': 'knowledge_point',
        'judge_type': 'judge_type',
        'exercise_data': 'exercise_data'
    }

    def __init__(self, id=None, name=None, description=None, difficult=None, exercise_type=None, exercise_type_name=None, order_count=None, test_case_description=None, knowledge_point=None, judge_type=None, exercise_data=None):
        r"""ShowExerciseDetailResponse

        The model defined in huaweicloud sdk

        :param id: 习题id
        :type id: str
        :param name: 习题名称
        :type name: str
        :param description: 习题描述
        :type description: str
        :param difficult: 
        :type difficult: :class:`huaweicloudsdkclassroom.v3.DifficultInfo`
        :param exercise_type: 习题类型编号
        :type exercise_type: int
        :param exercise_type_name: 习题类型名称
        :type exercise_type_name: str
        :param order_count: 习题库里习题编号
        :type order_count: int
        :param test_case_description: 测试用例描述
        :type test_case_description: str
        :param knowledge_point: 相关知识点
        :type knowledge_point: list[:class:`huaweicloudsdkclassroom.v3.KnowledgePointInfo`]
        :param judge_type: 判题类型
        :type judge_type: int
        :param exercise_data: 
        :type exercise_data: :class:`huaweicloudsdkclassroom.v3.ExerciseDetailData`
        """
        
        super(ShowExerciseDetailResponse, self).__init__()

        self._id = None
        self._name = None
        self._description = None
        self._difficult = None
        self._exercise_type = None
        self._exercise_type_name = None
        self._order_count = None
        self._test_case_description = None
        self._knowledge_point = None
        self._judge_type = None
        self._exercise_data = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if difficult is not None:
            self.difficult = difficult
        if exercise_type is not None:
            self.exercise_type = exercise_type
        if exercise_type_name is not None:
            self.exercise_type_name = exercise_type_name
        if order_count is not None:
            self.order_count = order_count
        if test_case_description is not None:
            self.test_case_description = test_case_description
        if knowledge_point is not None:
            self.knowledge_point = knowledge_point
        if judge_type is not None:
            self.judge_type = judge_type
        if exercise_data is not None:
            self.exercise_data = exercise_data

    @property
    def id(self):
        r"""Gets the id of this ShowExerciseDetailResponse.

        习题id

        :return: The id of this ShowExerciseDetailResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowExerciseDetailResponse.

        习题id

        :param id: The id of this ShowExerciseDetailResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ShowExerciseDetailResponse.

        习题名称

        :return: The name of this ShowExerciseDetailResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowExerciseDetailResponse.

        习题名称

        :param name: The name of this ShowExerciseDetailResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ShowExerciseDetailResponse.

        习题描述

        :return: The description of this ShowExerciseDetailResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowExerciseDetailResponse.

        习题描述

        :param description: The description of this ShowExerciseDetailResponse.
        :type description: str
        """
        self._description = description

    @property
    def difficult(self):
        r"""Gets the difficult of this ShowExerciseDetailResponse.

        :return: The difficult of this ShowExerciseDetailResponse.
        :rtype: :class:`huaweicloudsdkclassroom.v3.DifficultInfo`
        """
        return self._difficult

    @difficult.setter
    def difficult(self, difficult):
        r"""Sets the difficult of this ShowExerciseDetailResponse.

        :param difficult: The difficult of this ShowExerciseDetailResponse.
        :type difficult: :class:`huaweicloudsdkclassroom.v3.DifficultInfo`
        """
        self._difficult = difficult

    @property
    def exercise_type(self):
        r"""Gets the exercise_type of this ShowExerciseDetailResponse.

        习题类型编号

        :return: The exercise_type of this ShowExerciseDetailResponse.
        :rtype: int
        """
        return self._exercise_type

    @exercise_type.setter
    def exercise_type(self, exercise_type):
        r"""Sets the exercise_type of this ShowExerciseDetailResponse.

        习题类型编号

        :param exercise_type: The exercise_type of this ShowExerciseDetailResponse.
        :type exercise_type: int
        """
        self._exercise_type = exercise_type

    @property
    def exercise_type_name(self):
        r"""Gets the exercise_type_name of this ShowExerciseDetailResponse.

        习题类型名称

        :return: The exercise_type_name of this ShowExerciseDetailResponse.
        :rtype: str
        """
        return self._exercise_type_name

    @exercise_type_name.setter
    def exercise_type_name(self, exercise_type_name):
        r"""Sets the exercise_type_name of this ShowExerciseDetailResponse.

        习题类型名称

        :param exercise_type_name: The exercise_type_name of this ShowExerciseDetailResponse.
        :type exercise_type_name: str
        """
        self._exercise_type_name = exercise_type_name

    @property
    def order_count(self):
        r"""Gets the order_count of this ShowExerciseDetailResponse.

        习题库里习题编号

        :return: The order_count of this ShowExerciseDetailResponse.
        :rtype: int
        """
        return self._order_count

    @order_count.setter
    def order_count(self, order_count):
        r"""Sets the order_count of this ShowExerciseDetailResponse.

        习题库里习题编号

        :param order_count: The order_count of this ShowExerciseDetailResponse.
        :type order_count: int
        """
        self._order_count = order_count

    @property
    def test_case_description(self):
        r"""Gets the test_case_description of this ShowExerciseDetailResponse.

        测试用例描述

        :return: The test_case_description of this ShowExerciseDetailResponse.
        :rtype: str
        """
        return self._test_case_description

    @test_case_description.setter
    def test_case_description(self, test_case_description):
        r"""Sets the test_case_description of this ShowExerciseDetailResponse.

        测试用例描述

        :param test_case_description: The test_case_description of this ShowExerciseDetailResponse.
        :type test_case_description: str
        """
        self._test_case_description = test_case_description

    @property
    def knowledge_point(self):
        r"""Gets the knowledge_point of this ShowExerciseDetailResponse.

        相关知识点

        :return: The knowledge_point of this ShowExerciseDetailResponse.
        :rtype: list[:class:`huaweicloudsdkclassroom.v3.KnowledgePointInfo`]
        """
        return self._knowledge_point

    @knowledge_point.setter
    def knowledge_point(self, knowledge_point):
        r"""Sets the knowledge_point of this ShowExerciseDetailResponse.

        相关知识点

        :param knowledge_point: The knowledge_point of this ShowExerciseDetailResponse.
        :type knowledge_point: list[:class:`huaweicloudsdkclassroom.v3.KnowledgePointInfo`]
        """
        self._knowledge_point = knowledge_point

    @property
    def judge_type(self):
        r"""Gets the judge_type of this ShowExerciseDetailResponse.

        判题类型

        :return: The judge_type of this ShowExerciseDetailResponse.
        :rtype: int
        """
        return self._judge_type

    @judge_type.setter
    def judge_type(self, judge_type):
        r"""Sets the judge_type of this ShowExerciseDetailResponse.

        判题类型

        :param judge_type: The judge_type of this ShowExerciseDetailResponse.
        :type judge_type: int
        """
        self._judge_type = judge_type

    @property
    def exercise_data(self):
        r"""Gets the exercise_data of this ShowExerciseDetailResponse.

        :return: The exercise_data of this ShowExerciseDetailResponse.
        :rtype: :class:`huaweicloudsdkclassroom.v3.ExerciseDetailData`
        """
        return self._exercise_data

    @exercise_data.setter
    def exercise_data(self, exercise_data):
        r"""Sets the exercise_data of this ShowExerciseDetailResponse.

        :param exercise_data: The exercise_data of this ShowExerciseDetailResponse.
        :type exercise_data: :class:`huaweicloudsdkclassroom.v3.ExerciseDetailData`
        """
        self._exercise_data = exercise_data

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
        if not isinstance(other, ShowExerciseDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
