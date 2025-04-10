# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HitConditionTag:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tag': 'str',
        'operation': 'str',
        'match': 'str',
        'value': 'str'
    }

    attribute_map = {
        'tag': 'tag',
        'operation': 'operation',
        'match': 'match',
        'value': 'value'
    }

    def __init__(self, tag=None, operation=None, match=None, value=None):
        r"""HitConditionTag

        The model defined in huaweicloud sdk

        :param tag: **参数解释**： 事件内容关键字段 &gt; * event_type为1,2,3,4：与LiveEventReport中event.content中反序列化后的JSON字段对应。如：弹幕事件上报事件。   {     \&quot;timestamp\&quot;: 1694481224245,     \&quot;type\&quot;: 1,     \&quot;content\&quot;: \&quot;{\\\&quot;user\\\&quot;:{\\\&quot;userId\\\&quot;:\\\&quot;2027271526\\\&quot;,\\\&quot;name\\\&quot;:\\\&quot;***\\\&quot;,\\\&quot;level\\\&quot;:17,\\\&quot;badge\\\&quot;:\\\&quot;\\\&quot;,\\\&quot;badgeLevel\\\&quot;:0},\\\&quot;content\\\&quot;:\\\&quot;***\\\&quot;}\&quot;   }   匹配弹幕内容，填写content；匹配用户平台等级，填写level。 &gt; * 10：固定填写content即可。  **约束限制**： 不涉及 **取值范围**： 字符长度0-256位 **默认取值**： 不涉及
        :type tag: str
        :param operation: **参数解释**： 字段取值处理 **约束限制**： 不涉及 **取值范围**： * SUM：累计 * AVG：平均 * COUNT：计数 * NONE：无处理
        :type operation: str
        :param match: **参数解释**： 匹配类型。关键词匹配建议使用REGEX。 **约束限制**： 不涉及。 **取值范围**： * EQUAL: 完全相等 * REGEX：正则匹配 * MATH_GT：数值大于 * MATH_GE：数值大于等于  * MATH_LT：数值小于 * MATH_LE：数值小于等于 * MATH_EQ：数值相等  **默认取值**： 不涉及
        :type match: str
        :param value: **参数解释**： 匹配值。 **约束限制**： 不涉及 **取值范围**： 字符长度0-1024 **默认取值**： 不涉及。
        :type value: str
        """
        
        

        self._tag = None
        self._operation = None
        self._match = None
        self._value = None
        self.discriminator = None

        if tag is not None:
            self.tag = tag
        if operation is not None:
            self.operation = operation
        if match is not None:
            self.match = match
        if value is not None:
            self.value = value

    @property
    def tag(self):
        r"""Gets the tag of this HitConditionTag.

        **参数解释**： 事件内容关键字段 > * event_type为1,2,3,4：与LiveEventReport中event.content中反序列化后的JSON字段对应。如：弹幕事件上报事件。   {     \"timestamp\": 1694481224245,     \"type\": 1,     \"content\": \"{\\\"user\\\":{\\\"userId\\\":\\\"2027271526\\\",\\\"name\\\":\\\"***\\\",\\\"level\\\":17,\\\"badge\\\":\\\"\\\",\\\"badgeLevel\\\":0},\\\"content\\\":\\\"***\\\"}\"   }   匹配弹幕内容，填写content；匹配用户平台等级，填写level。 > * 10：固定填写content即可。  **约束限制**： 不涉及 **取值范围**： 字符长度0-256位 **默认取值**： 不涉及

        :return: The tag of this HitConditionTag.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this HitConditionTag.

        **参数解释**： 事件内容关键字段 > * event_type为1,2,3,4：与LiveEventReport中event.content中反序列化后的JSON字段对应。如：弹幕事件上报事件。   {     \"timestamp\": 1694481224245,     \"type\": 1,     \"content\": \"{\\\"user\\\":{\\\"userId\\\":\\\"2027271526\\\",\\\"name\\\":\\\"***\\\",\\\"level\\\":17,\\\"badge\\\":\\\"\\\",\\\"badgeLevel\\\":0},\\\"content\\\":\\\"***\\\"}\"   }   匹配弹幕内容，填写content；匹配用户平台等级，填写level。 > * 10：固定填写content即可。  **约束限制**： 不涉及 **取值范围**： 字符长度0-256位 **默认取值**： 不涉及

        :param tag: The tag of this HitConditionTag.
        :type tag: str
        """
        self._tag = tag

    @property
    def operation(self):
        r"""Gets the operation of this HitConditionTag.

        **参数解释**： 字段取值处理 **约束限制**： 不涉及 **取值范围**： * SUM：累计 * AVG：平均 * COUNT：计数 * NONE：无处理

        :return: The operation of this HitConditionTag.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        r"""Sets the operation of this HitConditionTag.

        **参数解释**： 字段取值处理 **约束限制**： 不涉及 **取值范围**： * SUM：累计 * AVG：平均 * COUNT：计数 * NONE：无处理

        :param operation: The operation of this HitConditionTag.
        :type operation: str
        """
        self._operation = operation

    @property
    def match(self):
        r"""Gets the match of this HitConditionTag.

        **参数解释**： 匹配类型。关键词匹配建议使用REGEX。 **约束限制**： 不涉及。 **取值范围**： * EQUAL: 完全相等 * REGEX：正则匹配 * MATH_GT：数值大于 * MATH_GE：数值大于等于  * MATH_LT：数值小于 * MATH_LE：数值小于等于 * MATH_EQ：数值相等  **默认取值**： 不涉及

        :return: The match of this HitConditionTag.
        :rtype: str
        """
        return self._match

    @match.setter
    def match(self, match):
        r"""Sets the match of this HitConditionTag.

        **参数解释**： 匹配类型。关键词匹配建议使用REGEX。 **约束限制**： 不涉及。 **取值范围**： * EQUAL: 完全相等 * REGEX：正则匹配 * MATH_GT：数值大于 * MATH_GE：数值大于等于  * MATH_LT：数值小于 * MATH_LE：数值小于等于 * MATH_EQ：数值相等  **默认取值**： 不涉及

        :param match: The match of this HitConditionTag.
        :type match: str
        """
        self._match = match

    @property
    def value(self):
        r"""Gets the value of this HitConditionTag.

        **参数解释**： 匹配值。 **约束限制**： 不涉及 **取值范围**： 字符长度0-1024 **默认取值**： 不涉及。

        :return: The value of this HitConditionTag.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this HitConditionTag.

        **参数解释**： 匹配值。 **约束限制**： 不涉及 **取值范围**： 字符长度0-1024 **默认取值**： 不涉及。

        :param value: The value of this HitConditionTag.
        :type value: str
        """
        self._value = value

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
        if not isinstance(other, HitConditionTag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
