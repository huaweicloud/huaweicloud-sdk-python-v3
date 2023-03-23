# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GenerationResult:

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
        'num_rounds': 'int',
        'num_expected': 'int',
        'num_strong_constraints': 'int',
        'num_weak_constraints': 'int',
        'prop_names': 'list[str]',
        'result': 'list[GenerationResultItem]'
    }

    attribute_map = {
        'name': 'name',
        'num_rounds': 'num_rounds',
        'num_expected': 'num_expected',
        'num_strong_constraints': 'num_strong_constraints',
        'num_weak_constraints': 'num_weak_constraints',
        'prop_names': 'prop_names',
        'result': 'result'
    }

    def __init__(self, name=None, num_rounds=None, num_expected=None, num_strong_constraints=None, num_weak_constraints=None, prop_names=None, result=None):
        """GenerationResult

        The model defined in huaweicloud sdk

        :param name: 任务名
        :type name: str
        :param num_rounds: 总生成轮数
        :type num_rounds: int
        :param num_expected: 期望条目数
        :type num_expected: int
        :param num_strong_constraints: 强约束数量
        :type num_strong_constraints: int
        :param num_weak_constraints: 弱约束数量
        :type num_weak_constraints: int
        :param prop_names: 分子ADMET属性名列表
        :type prop_names: list[str]
        :param result: 分子生成结果条目
        :type result: list[:class:`huaweicloudsdkeihealth.v1.GenerationResultItem`]
        """
        
        

        self._name = None
        self._num_rounds = None
        self._num_expected = None
        self._num_strong_constraints = None
        self._num_weak_constraints = None
        self._prop_names = None
        self._result = None
        self.discriminator = None

        self.name = name
        self.num_rounds = num_rounds
        self.num_expected = num_expected
        self.num_strong_constraints = num_strong_constraints
        self.num_weak_constraints = num_weak_constraints
        self.prop_names = prop_names
        self.result = result

    @property
    def name(self):
        """Gets the name of this GenerationResult.

        任务名

        :return: The name of this GenerationResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GenerationResult.

        任务名

        :param name: The name of this GenerationResult.
        :type name: str
        """
        self._name = name

    @property
    def num_rounds(self):
        """Gets the num_rounds of this GenerationResult.

        总生成轮数

        :return: The num_rounds of this GenerationResult.
        :rtype: int
        """
        return self._num_rounds

    @num_rounds.setter
    def num_rounds(self, num_rounds):
        """Sets the num_rounds of this GenerationResult.

        总生成轮数

        :param num_rounds: The num_rounds of this GenerationResult.
        :type num_rounds: int
        """
        self._num_rounds = num_rounds

    @property
    def num_expected(self):
        """Gets the num_expected of this GenerationResult.

        期望条目数

        :return: The num_expected of this GenerationResult.
        :rtype: int
        """
        return self._num_expected

    @num_expected.setter
    def num_expected(self, num_expected):
        """Sets the num_expected of this GenerationResult.

        期望条目数

        :param num_expected: The num_expected of this GenerationResult.
        :type num_expected: int
        """
        self._num_expected = num_expected

    @property
    def num_strong_constraints(self):
        """Gets the num_strong_constraints of this GenerationResult.

        强约束数量

        :return: The num_strong_constraints of this GenerationResult.
        :rtype: int
        """
        return self._num_strong_constraints

    @num_strong_constraints.setter
    def num_strong_constraints(self, num_strong_constraints):
        """Sets the num_strong_constraints of this GenerationResult.

        强约束数量

        :param num_strong_constraints: The num_strong_constraints of this GenerationResult.
        :type num_strong_constraints: int
        """
        self._num_strong_constraints = num_strong_constraints

    @property
    def num_weak_constraints(self):
        """Gets the num_weak_constraints of this GenerationResult.

        弱约束数量

        :return: The num_weak_constraints of this GenerationResult.
        :rtype: int
        """
        return self._num_weak_constraints

    @num_weak_constraints.setter
    def num_weak_constraints(self, num_weak_constraints):
        """Sets the num_weak_constraints of this GenerationResult.

        弱约束数量

        :param num_weak_constraints: The num_weak_constraints of this GenerationResult.
        :type num_weak_constraints: int
        """
        self._num_weak_constraints = num_weak_constraints

    @property
    def prop_names(self):
        """Gets the prop_names of this GenerationResult.

        分子ADMET属性名列表

        :return: The prop_names of this GenerationResult.
        :rtype: list[str]
        """
        return self._prop_names

    @prop_names.setter
    def prop_names(self, prop_names):
        """Sets the prop_names of this GenerationResult.

        分子ADMET属性名列表

        :param prop_names: The prop_names of this GenerationResult.
        :type prop_names: list[str]
        """
        self._prop_names = prop_names

    @property
    def result(self):
        """Gets the result of this GenerationResult.

        分子生成结果条目

        :return: The result of this GenerationResult.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.GenerationResultItem`]
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this GenerationResult.

        分子生成结果条目

        :param result: The result of this GenerationResult.
        :type result: list[:class:`huaweicloudsdkeihealth.v1.GenerationResultItem`]
        """
        self._result = result

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
        if not isinstance(other, GenerationResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
