# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryCondition:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'condition_name': 'str',
        'condition_value': 'str',
        'condition_values': 'list[str]',
        'conditions': 'list[QueryCondition]',
        'ignore_str': 'bool',
        'join_table_alias': 'str',
        'joiner': 'str',
        'operator': 'str',
        'pre_condition': 'QueryCondition'
    }

    attribute_map = {
        'condition_name': 'conditionName',
        'condition_value': 'conditionValue',
        'condition_values': 'conditionValues',
        'conditions': 'conditions',
        'ignore_str': 'ignoreStr',
        'join_table_alias': 'joinTableAlias',
        'joiner': 'joiner',
        'operator': 'operator',
        'pre_condition': 'preCondition'
    }

    def __init__(self, condition_name=None, condition_value=None, condition_values=None, conditions=None, ignore_str=None, join_table_alias=None, joiner=None, operator=None, pre_condition=None):
        """QueryCondition

        The model defined in huaweicloud sdk

        :param condition_name: 查询条件的名称（数据模型的属性英文名称）。
        :type condition_name: str
        :param condition_value: 查询条件值（已过时）。
        :type condition_value: str
        :param condition_values: 查询条件的值。operator为in时有多值，operator为其他操作符时均为单值。
        :type condition_values: list[str]
        :param conditions: 查询条件列表。
        :type conditions: list[:class:`huaweicloudsdkidmeclassicapi.v1.QueryCondition`]
        :param ignore_str: 是否忽略大小写。 - true：表示忽略。 - false：表示不忽略。
        :type ignore_str: bool
        :param join_table_alias: 关联查询时被关联表的别名。
        :type join_table_alias: str
        :param joiner: 连接符。
        :type joiner: str
        :param operator: 操作符。 - &#x3D;：等于查询。 - like：模糊查询。 - customLike：支持输入*或%的模糊查询。 - in：包含查询。 - &lt;：小于查询。 - \\&gt;：大于查询。 - \\&gt;&#x3D;：大于等于查询。 - &lt;&#x3D;：小于等于查询。 - &lt;&gt;：不等于查询。
        :type operator: str
        :param pre_condition: 
        :type pre_condition: :class:`huaweicloudsdkidmeclassicapi.v1.QueryCondition`
        """
        
        

        self._condition_name = None
        self._condition_value = None
        self._condition_values = None
        self._conditions = None
        self._ignore_str = None
        self._join_table_alias = None
        self._joiner = None
        self._operator = None
        self._pre_condition = None
        self.discriminator = None

        if condition_name is not None:
            self.condition_name = condition_name
        if condition_value is not None:
            self.condition_value = condition_value
        if condition_values is not None:
            self.condition_values = condition_values
        if conditions is not None:
            self.conditions = conditions
        if ignore_str is not None:
            self.ignore_str = ignore_str
        if join_table_alias is not None:
            self.join_table_alias = join_table_alias
        if joiner is not None:
            self.joiner = joiner
        if operator is not None:
            self.operator = operator
        if pre_condition is not None:
            self.pre_condition = pre_condition

    @property
    def condition_name(self):
        """Gets the condition_name of this QueryCondition.

        查询条件的名称（数据模型的属性英文名称）。

        :return: The condition_name of this QueryCondition.
        :rtype: str
        """
        return self._condition_name

    @condition_name.setter
    def condition_name(self, condition_name):
        """Sets the condition_name of this QueryCondition.

        查询条件的名称（数据模型的属性英文名称）。

        :param condition_name: The condition_name of this QueryCondition.
        :type condition_name: str
        """
        self._condition_name = condition_name

    @property
    def condition_value(self):
        """Gets the condition_value of this QueryCondition.

        查询条件值（已过时）。

        :return: The condition_value of this QueryCondition.
        :rtype: str
        """
        return self._condition_value

    @condition_value.setter
    def condition_value(self, condition_value):
        """Sets the condition_value of this QueryCondition.

        查询条件值（已过时）。

        :param condition_value: The condition_value of this QueryCondition.
        :type condition_value: str
        """
        self._condition_value = condition_value

    @property
    def condition_values(self):
        """Gets the condition_values of this QueryCondition.

        查询条件的值。operator为in时有多值，operator为其他操作符时均为单值。

        :return: The condition_values of this QueryCondition.
        :rtype: list[str]
        """
        return self._condition_values

    @condition_values.setter
    def condition_values(self, condition_values):
        """Sets the condition_values of this QueryCondition.

        查询条件的值。operator为in时有多值，operator为其他操作符时均为单值。

        :param condition_values: The condition_values of this QueryCondition.
        :type condition_values: list[str]
        """
        self._condition_values = condition_values

    @property
    def conditions(self):
        """Gets the conditions of this QueryCondition.

        查询条件列表。

        :return: The conditions of this QueryCondition.
        :rtype: list[:class:`huaweicloudsdkidmeclassicapi.v1.QueryCondition`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this QueryCondition.

        查询条件列表。

        :param conditions: The conditions of this QueryCondition.
        :type conditions: list[:class:`huaweicloudsdkidmeclassicapi.v1.QueryCondition`]
        """
        self._conditions = conditions

    @property
    def ignore_str(self):
        """Gets the ignore_str of this QueryCondition.

        是否忽略大小写。 - true：表示忽略。 - false：表示不忽略。

        :return: The ignore_str of this QueryCondition.
        :rtype: bool
        """
        return self._ignore_str

    @ignore_str.setter
    def ignore_str(self, ignore_str):
        """Sets the ignore_str of this QueryCondition.

        是否忽略大小写。 - true：表示忽略。 - false：表示不忽略。

        :param ignore_str: The ignore_str of this QueryCondition.
        :type ignore_str: bool
        """
        self._ignore_str = ignore_str

    @property
    def join_table_alias(self):
        """Gets the join_table_alias of this QueryCondition.

        关联查询时被关联表的别名。

        :return: The join_table_alias of this QueryCondition.
        :rtype: str
        """
        return self._join_table_alias

    @join_table_alias.setter
    def join_table_alias(self, join_table_alias):
        """Sets the join_table_alias of this QueryCondition.

        关联查询时被关联表的别名。

        :param join_table_alias: The join_table_alias of this QueryCondition.
        :type join_table_alias: str
        """
        self._join_table_alias = join_table_alias

    @property
    def joiner(self):
        """Gets the joiner of this QueryCondition.

        连接符。

        :return: The joiner of this QueryCondition.
        :rtype: str
        """
        return self._joiner

    @joiner.setter
    def joiner(self, joiner):
        """Sets the joiner of this QueryCondition.

        连接符。

        :param joiner: The joiner of this QueryCondition.
        :type joiner: str
        """
        self._joiner = joiner

    @property
    def operator(self):
        """Gets the operator of this QueryCondition.

        操作符。 - =：等于查询。 - like：模糊查询。 - customLike：支持输入*或%的模糊查询。 - in：包含查询。 - <：小于查询。 - \\>：大于查询。 - \\>=：大于等于查询。 - <=：小于等于查询。 - <>：不等于查询。

        :return: The operator of this QueryCondition.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this QueryCondition.

        操作符。 - =：等于查询。 - like：模糊查询。 - customLike：支持输入*或%的模糊查询。 - in：包含查询。 - <：小于查询。 - \\>：大于查询。 - \\>=：大于等于查询。 - <=：小于等于查询。 - <>：不等于查询。

        :param operator: The operator of this QueryCondition.
        :type operator: str
        """
        self._operator = operator

    @property
    def pre_condition(self):
        """Gets the pre_condition of this QueryCondition.

        :return: The pre_condition of this QueryCondition.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.QueryCondition`
        """
        return self._pre_condition

    @pre_condition.setter
    def pre_condition(self, pre_condition):
        """Sets the pre_condition of this QueryCondition.

        :param pre_condition: The pre_condition of this QueryCondition.
        :type pre_condition: :class:`huaweicloudsdkidmeclassicapi.v1.QueryCondition`
        """
        self._pre_condition = pre_condition

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
        if not isinstance(other, QueryCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
