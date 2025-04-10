# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConditionInstance:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'condition_index': 'int',
        'condition_map': 'dict(str, list[str])',
        'dep_param_map': 'dict(str, DepParamInstance)',
        'statement_index': 'int'
    }

    attribute_map = {
        'condition_index': 'conditionIndex',
        'condition_map': 'conditionMap',
        'dep_param_map': 'depParamMap',
        'statement_index': 'statementIndex'
    }

    def __init__(self, condition_index=None, condition_map=None, dep_param_map=None, statement_index=None):
        r"""ConditionInstance

        The model defined in huaweicloud sdk

        :param condition_index: 条件索引，用于标识当前处理的是哪个条件
        :type condition_index: int
        :param condition_map: 条件映射，键为整数，值为字符串列表，用于存储各个条件的信息
        :type condition_map: dict(str, list[str])
        :param dep_param_map: 依赖参数实例的映射
        :type dep_param_map: dict(str, DepParamInstance)
        :param statement_index: 声明索引，用于标识当前处理的是哪个声明
        :type statement_index: int
        """
        
        

        self._condition_index = None
        self._condition_map = None
        self._dep_param_map = None
        self._statement_index = None
        self.discriminator = None

        if condition_index is not None:
            self.condition_index = condition_index
        if condition_map is not None:
            self.condition_map = condition_map
        if dep_param_map is not None:
            self.dep_param_map = dep_param_map
        if statement_index is not None:
            self.statement_index = statement_index

    @property
    def condition_index(self):
        r"""Gets the condition_index of this ConditionInstance.

        条件索引，用于标识当前处理的是哪个条件

        :return: The condition_index of this ConditionInstance.
        :rtype: int
        """
        return self._condition_index

    @condition_index.setter
    def condition_index(self, condition_index):
        r"""Sets the condition_index of this ConditionInstance.

        条件索引，用于标识当前处理的是哪个条件

        :param condition_index: The condition_index of this ConditionInstance.
        :type condition_index: int
        """
        self._condition_index = condition_index

    @property
    def condition_map(self):
        r"""Gets the condition_map of this ConditionInstance.

        条件映射，键为整数，值为字符串列表，用于存储各个条件的信息

        :return: The condition_map of this ConditionInstance.
        :rtype: dict(str, list[str])
        """
        return self._condition_map

    @condition_map.setter
    def condition_map(self, condition_map):
        r"""Sets the condition_map of this ConditionInstance.

        条件映射，键为整数，值为字符串列表，用于存储各个条件的信息

        :param condition_map: The condition_map of this ConditionInstance.
        :type condition_map: dict(str, list[str])
        """
        self._condition_map = condition_map

    @property
    def dep_param_map(self):
        r"""Gets the dep_param_map of this ConditionInstance.

        依赖参数实例的映射

        :return: The dep_param_map of this ConditionInstance.
        :rtype: dict(str, DepParamInstance)
        """
        return self._dep_param_map

    @dep_param_map.setter
    def dep_param_map(self, dep_param_map):
        r"""Sets the dep_param_map of this ConditionInstance.

        依赖参数实例的映射

        :param dep_param_map: The dep_param_map of this ConditionInstance.
        :type dep_param_map: dict(str, DepParamInstance)
        """
        self._dep_param_map = dep_param_map

    @property
    def statement_index(self):
        r"""Gets the statement_index of this ConditionInstance.

        声明索引，用于标识当前处理的是哪个声明

        :return: The statement_index of this ConditionInstance.
        :rtype: int
        """
        return self._statement_index

    @statement_index.setter
    def statement_index(self, statement_index):
        r"""Sets the statement_index of this ConditionInstance.

        声明索引，用于标识当前处理的是哪个声明

        :param statement_index: The statement_index of this ConditionInstance.
        :type statement_index: int
        """
        self._statement_index = statement_index

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
        if not isinstance(other, ConditionInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
