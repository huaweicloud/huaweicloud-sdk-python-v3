# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataFilteringCondition:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'value': 'str',
        'filtering_type': 'str'
    }

    attribute_map = {
        'value': 'value',
        'filtering_type': 'filtering_type'
    }

    def __init__(self, value=None, filtering_type=None):
        r"""DataFilteringCondition

        The model defined in huaweicloud sdk

        :param value: 过滤条件 当filtering_type是configConditionalFilter时， value默认填写config 当filtering_type是contentConditionalFilter时， value默认填写过滤条件  注意： 每张表仅支持添加一个校验规则。 数据过滤每次最多支持500张表。 过滤表达式不支持使用某种数据库引擎特有的package、函数、变量、常量等写法，须使用通用SQL标准。请直接输入SQL语句中WHERE之后的部分（不包含WHERE和分号，例如：sid &gt; 3 and sname like \&quot;G %\&quot;），最多支持输入512个字符。 过滤条件填写的SQL语句中，关键字需要用反引号，datatime类型（包含日期和时间）需要用单引号，例如：update &gt; &#39;2022-07-13 00:00:00&#39; and age &gt;10。 不支持对LOB字段设置过滤条件，如CLOB、BLOB、BYTEA等大字段类型。 不支持库名、表名带有换行符的对象设置过滤规则。 建议不要对非精确类型字段设置过滤条件，如FLOAT、DECIMAL、DOUBLE等。 建议不要对带有特殊字符的字段设置过滤条件。 不建议使用非幂等表达式或函数作为数据加工条件，如SYSTIMESTAMP，SYSDATE等，因其每次调用返回的结果可能会有差异，导致达不到预期。
        :type value: str
        :param filtering_type: 过滤条件类型  contentConditionalFilter: 简单条件过滤 configConditionalFilter: 关联表过滤
        :type filtering_type: str
        """
        
        

        self._value = None
        self._filtering_type = None
        self.discriminator = None

        if value is not None:
            self.value = value
        if filtering_type is not None:
            self.filtering_type = filtering_type

    @property
    def value(self):
        r"""Gets the value of this DataFilteringCondition.

        过滤条件 当filtering_type是configConditionalFilter时， value默认填写config 当filtering_type是contentConditionalFilter时， value默认填写过滤条件  注意： 每张表仅支持添加一个校验规则。 数据过滤每次最多支持500张表。 过滤表达式不支持使用某种数据库引擎特有的package、函数、变量、常量等写法，须使用通用SQL标准。请直接输入SQL语句中WHERE之后的部分（不包含WHERE和分号，例如：sid > 3 and sname like \"G %\"），最多支持输入512个字符。 过滤条件填写的SQL语句中，关键字需要用反引号，datatime类型（包含日期和时间）需要用单引号，例如：update > '2022-07-13 00:00:00' and age >10。 不支持对LOB字段设置过滤条件，如CLOB、BLOB、BYTEA等大字段类型。 不支持库名、表名带有换行符的对象设置过滤规则。 建议不要对非精确类型字段设置过滤条件，如FLOAT、DECIMAL、DOUBLE等。 建议不要对带有特殊字符的字段设置过滤条件。 不建议使用非幂等表达式或函数作为数据加工条件，如SYSTIMESTAMP，SYSDATE等，因其每次调用返回的结果可能会有差异，导致达不到预期。

        :return: The value of this DataFilteringCondition.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this DataFilteringCondition.

        过滤条件 当filtering_type是configConditionalFilter时， value默认填写config 当filtering_type是contentConditionalFilter时， value默认填写过滤条件  注意： 每张表仅支持添加一个校验规则。 数据过滤每次最多支持500张表。 过滤表达式不支持使用某种数据库引擎特有的package、函数、变量、常量等写法，须使用通用SQL标准。请直接输入SQL语句中WHERE之后的部分（不包含WHERE和分号，例如：sid > 3 and sname like \"G %\"），最多支持输入512个字符。 过滤条件填写的SQL语句中，关键字需要用反引号，datatime类型（包含日期和时间）需要用单引号，例如：update > '2022-07-13 00:00:00' and age >10。 不支持对LOB字段设置过滤条件，如CLOB、BLOB、BYTEA等大字段类型。 不支持库名、表名带有换行符的对象设置过滤规则。 建议不要对非精确类型字段设置过滤条件，如FLOAT、DECIMAL、DOUBLE等。 建议不要对带有特殊字符的字段设置过滤条件。 不建议使用非幂等表达式或函数作为数据加工条件，如SYSTIMESTAMP，SYSDATE等，因其每次调用返回的结果可能会有差异，导致达不到预期。

        :param value: The value of this DataFilteringCondition.
        :type value: str
        """
        self._value = value

    @property
    def filtering_type(self):
        r"""Gets the filtering_type of this DataFilteringCondition.

        过滤条件类型  contentConditionalFilter: 简单条件过滤 configConditionalFilter: 关联表过滤

        :return: The filtering_type of this DataFilteringCondition.
        :rtype: str
        """
        return self._filtering_type

    @filtering_type.setter
    def filtering_type(self, filtering_type):
        r"""Sets the filtering_type of this DataFilteringCondition.

        过滤条件类型  contentConditionalFilter: 简单条件过滤 configConditionalFilter: 关联表过滤

        :param filtering_type: The filtering_type of this DataFilteringCondition.
        :type filtering_type: str
        """
        self._filtering_type = filtering_type

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
        if not isinstance(other, DataFilteringCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
