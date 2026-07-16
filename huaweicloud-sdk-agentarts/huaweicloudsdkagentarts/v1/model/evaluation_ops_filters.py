# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EvaluationOpsFilters:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'logic_op': 'str',
        'filter_conditions': 'list[object]'
    }

    attribute_map = {
        'logic_op': 'logic_op',
        'filter_conditions': 'filter_conditions'
    }

    def __init__(self, logic_op=None, filter_conditions=None):
        r"""EvaluationOpsFilters

        The model defined in huaweicloud sdk

        :param logic_op: **参数解释：** 过滤条件的逻辑运算符。And表示全显，Or表示任一。 **约束限制：** 0到10000字符。 **取值范围：** And, Or。 **默认取值：** 不涉及。
        :type logic_op: str
        :param filter_conditions: **参数解释：** 具体的过滤条件列表。每个元素为一个JSON格式的字符串。 **约束限制：** 数组长度为0到10000。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type filter_conditions: list[object]
        """
        
        

        self._logic_op = None
        self._filter_conditions = None
        self.discriminator = None

        if logic_op is not None:
            self.logic_op = logic_op
        if filter_conditions is not None:
            self.filter_conditions = filter_conditions

    @property
    def logic_op(self):
        r"""Gets the logic_op of this EvaluationOpsFilters.

        **参数解释：** 过滤条件的逻辑运算符。And表示全显，Or表示任一。 **约束限制：** 0到10000字符。 **取值范围：** And, Or。 **默认取值：** 不涉及。

        :return: The logic_op of this EvaluationOpsFilters.
        :rtype: str
        """
        return self._logic_op

    @logic_op.setter
    def logic_op(self, logic_op):
        r"""Sets the logic_op of this EvaluationOpsFilters.

        **参数解释：** 过滤条件的逻辑运算符。And表示全显，Or表示任一。 **约束限制：** 0到10000字符。 **取值范围：** And, Or。 **默认取值：** 不涉及。

        :param logic_op: The logic_op of this EvaluationOpsFilters.
        :type logic_op: str
        """
        self._logic_op = logic_op

    @property
    def filter_conditions(self):
        r"""Gets the filter_conditions of this EvaluationOpsFilters.

        **参数解释：** 具体的过滤条件列表。每个元素为一个JSON格式的字符串。 **约束限制：** 数组长度为0到10000。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The filter_conditions of this EvaluationOpsFilters.
        :rtype: list[object]
        """
        return self._filter_conditions

    @filter_conditions.setter
    def filter_conditions(self, filter_conditions):
        r"""Sets the filter_conditions of this EvaluationOpsFilters.

        **参数解释：** 具体的过滤条件列表。每个元素为一个JSON格式的字符串。 **约束限制：** 数组长度为0到10000。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param filter_conditions: The filter_conditions of this EvaluationOpsFilters.
        :type filter_conditions: list[object]
        """
        self._filter_conditions = filter_conditions

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EvaluationOpsFilters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
