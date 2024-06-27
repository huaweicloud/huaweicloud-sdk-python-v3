# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DepParamInstance:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'compare_value': 'str',
        'comparison': 'str',
        'condition': 'bool',
        'in_valid_values': 'list[str]',
        'name': 'str',
        'null_info': 'str',
        'relation_map': 'dict(str, str)',
        'relation_num': 'int',
        'values': 'list[str]'
    }

    attribute_map = {
        'compare_value': 'compareValue',
        'comparison': 'comparison',
        'condition': 'condition',
        'in_valid_values': 'inValidValues',
        'name': 'name',
        'null_info': 'nullInfo',
        'relation_map': 'relationMap',
        'relation_num': 'relationNum',
        'values': 'values'
    }

    def __init__(self, compare_value=None, comparison=None, condition=None, in_valid_values=None, name=None, null_info=None, relation_map=None, relation_num=None, values=None):
        """DepParamInstance

        The model defined in huaweicloud sdk

        :param compare_value: 比较值
        :type compare_value: str
        :param comparison: 比较
        :type comparison: str
        :param condition: 条件
        :type condition: bool
        :param in_valid_values: 无效值列表
        :type in_valid_values: list[str]
        :param name: 名称
        :type name: str
        :param null_info: 空值信息
        :type null_info: str
        :param relation_map: 关系映射，key为整数，value为字符串
        :type relation_map: dict(str, str)
        :param relation_num: 关系数量
        :type relation_num: int
        :param values: 值列表
        :type values: list[str]
        """
        
        

        self._compare_value = None
        self._comparison = None
        self._condition = None
        self._in_valid_values = None
        self._name = None
        self._null_info = None
        self._relation_map = None
        self._relation_num = None
        self._values = None
        self.discriminator = None

        if compare_value is not None:
            self.compare_value = compare_value
        if comparison is not None:
            self.comparison = comparison
        if condition is not None:
            self.condition = condition
        if in_valid_values is not None:
            self.in_valid_values = in_valid_values
        if name is not None:
            self.name = name
        if null_info is not None:
            self.null_info = null_info
        if relation_map is not None:
            self.relation_map = relation_map
        if relation_num is not None:
            self.relation_num = relation_num
        if values is not None:
            self.values = values

    @property
    def compare_value(self):
        """Gets the compare_value of this DepParamInstance.

        比较值

        :return: The compare_value of this DepParamInstance.
        :rtype: str
        """
        return self._compare_value

    @compare_value.setter
    def compare_value(self, compare_value):
        """Sets the compare_value of this DepParamInstance.

        比较值

        :param compare_value: The compare_value of this DepParamInstance.
        :type compare_value: str
        """
        self._compare_value = compare_value

    @property
    def comparison(self):
        """Gets the comparison of this DepParamInstance.

        比较

        :return: The comparison of this DepParamInstance.
        :rtype: str
        """
        return self._comparison

    @comparison.setter
    def comparison(self, comparison):
        """Sets the comparison of this DepParamInstance.

        比较

        :param comparison: The comparison of this DepParamInstance.
        :type comparison: str
        """
        self._comparison = comparison

    @property
    def condition(self):
        """Gets the condition of this DepParamInstance.

        条件

        :return: The condition of this DepParamInstance.
        :rtype: bool
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this DepParamInstance.

        条件

        :param condition: The condition of this DepParamInstance.
        :type condition: bool
        """
        self._condition = condition

    @property
    def in_valid_values(self):
        """Gets the in_valid_values of this DepParamInstance.

        无效值列表

        :return: The in_valid_values of this DepParamInstance.
        :rtype: list[str]
        """
        return self._in_valid_values

    @in_valid_values.setter
    def in_valid_values(self, in_valid_values):
        """Sets the in_valid_values of this DepParamInstance.

        无效值列表

        :param in_valid_values: The in_valid_values of this DepParamInstance.
        :type in_valid_values: list[str]
        """
        self._in_valid_values = in_valid_values

    @property
    def name(self):
        """Gets the name of this DepParamInstance.

        名称

        :return: The name of this DepParamInstance.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DepParamInstance.

        名称

        :param name: The name of this DepParamInstance.
        :type name: str
        """
        self._name = name

    @property
    def null_info(self):
        """Gets the null_info of this DepParamInstance.

        空值信息

        :return: The null_info of this DepParamInstance.
        :rtype: str
        """
        return self._null_info

    @null_info.setter
    def null_info(self, null_info):
        """Sets the null_info of this DepParamInstance.

        空值信息

        :param null_info: The null_info of this DepParamInstance.
        :type null_info: str
        """
        self._null_info = null_info

    @property
    def relation_map(self):
        """Gets the relation_map of this DepParamInstance.

        关系映射，key为整数，value为字符串

        :return: The relation_map of this DepParamInstance.
        :rtype: dict(str, str)
        """
        return self._relation_map

    @relation_map.setter
    def relation_map(self, relation_map):
        """Sets the relation_map of this DepParamInstance.

        关系映射，key为整数，value为字符串

        :param relation_map: The relation_map of this DepParamInstance.
        :type relation_map: dict(str, str)
        """
        self._relation_map = relation_map

    @property
    def relation_num(self):
        """Gets the relation_num of this DepParamInstance.

        关系数量

        :return: The relation_num of this DepParamInstance.
        :rtype: int
        """
        return self._relation_num

    @relation_num.setter
    def relation_num(self, relation_num):
        """Sets the relation_num of this DepParamInstance.

        关系数量

        :param relation_num: The relation_num of this DepParamInstance.
        :type relation_num: int
        """
        self._relation_num = relation_num

    @property
    def values(self):
        """Gets the values of this DepParamInstance.

        值列表

        :return: The values of this DepParamInstance.
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this DepParamInstance.

        值列表

        :param values: The values of this DepParamInstance.
        :type values: list[str]
        """
        self._values = values

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
        if not isinstance(other, DepParamInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
