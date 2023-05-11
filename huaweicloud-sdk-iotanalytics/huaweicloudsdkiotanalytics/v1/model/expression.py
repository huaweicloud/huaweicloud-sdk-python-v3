# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Expression:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'formula': 'str',
        'formulas': 'list[NamedFormula]',
        'time_range': 'str'
    }

    attribute_map = {
        'formula': 'formula',
        'formulas': 'formulas',
        'time_range': 'time_range'
    }

    def __init__(self, formula=None, formulas=None, time_range=None):
        """Expression

        The model defined in huaweicloud sdk

        :param formula: 公式，最多1024个字符(分析任务单输出场景，配合TransformModel或AggregateModel的output_property使用)
        :type formula: str
        :param formulas: 带名称的公式
        :type formulas: list[:class:`huaweicloudsdkiotanalytics.v1.NamedFormula`]
        :param time_range: 时间范围，调度时间往前的时间范围，比如1m表示调度时间往前1分钟到调度时间的时间范围，正则：\&quot;1m|5m|15m|1h\&quot;
        :type time_range: str
        """
        
        

        self._formula = None
        self._formulas = None
        self._time_range = None
        self.discriminator = None

        if formula is not None:
            self.formula = formula
        if formulas is not None:
            self.formulas = formulas
        self.time_range = time_range

    @property
    def formula(self):
        """Gets the formula of this Expression.

        公式，最多1024个字符(分析任务单输出场景，配合TransformModel或AggregateModel的output_property使用)

        :return: The formula of this Expression.
        :rtype: str
        """
        return self._formula

    @formula.setter
    def formula(self, formula):
        """Sets the formula of this Expression.

        公式，最多1024个字符(分析任务单输出场景，配合TransformModel或AggregateModel的output_property使用)

        :param formula: The formula of this Expression.
        :type formula: str
        """
        self._formula = formula

    @property
    def formulas(self):
        """Gets the formulas of this Expression.

        带名称的公式

        :return: The formulas of this Expression.
        :rtype: list[:class:`huaweicloudsdkiotanalytics.v1.NamedFormula`]
        """
        return self._formulas

    @formulas.setter
    def formulas(self, formulas):
        """Sets the formulas of this Expression.

        带名称的公式

        :param formulas: The formulas of this Expression.
        :type formulas: list[:class:`huaweicloudsdkiotanalytics.v1.NamedFormula`]
        """
        self._formulas = formulas

    @property
    def time_range(self):
        """Gets the time_range of this Expression.

        时间范围，调度时间往前的时间范围，比如1m表示调度时间往前1分钟到调度时间的时间范围，正则：\"1m|5m|15m|1h\"

        :return: The time_range of this Expression.
        :rtype: str
        """
        return self._time_range

    @time_range.setter
    def time_range(self, time_range):
        """Sets the time_range of this Expression.

        时间范围，调度时间往前的时间范围，比如1m表示调度时间往前1分钟到调度时间的时间范围，正则：\"1m|5m|15m|1h\"

        :param time_range: The time_range of this Expression.
        :type time_range: str
        """
        self._time_range = time_range

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
        if not isinstance(other, Expression):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
