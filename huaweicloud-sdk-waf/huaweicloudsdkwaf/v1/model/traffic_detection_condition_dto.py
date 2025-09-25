# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TrafficDetectionConditionDTO:

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
        'match_field': 'str',
        'match_field_index': 'str',
        'logical_operator': 'str',
        'match_contents': 'list[str]',
        'value_list_res': 'str'
    }

    attribute_map = {
        'id': 'id',
        'match_field': 'match_field',
        'match_field_index': 'match_field_index',
        'logical_operator': 'logical_operator',
        'match_contents': 'match_contents',
        'value_list_res': 'value_list_res'
    }

    def __init__(self, id=None, match_field=None, match_field_index=None, logical_operator=None, match_contents=None, value_list_res=None):
        r"""TrafficDetectionConditionDTO

        The model defined in huaweicloud sdk

        :param id: **参数解释：** Id，唯一标识当前流量检测条件。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type id: str
        :param match_field: **参数解释：** 匹配字段（类别），标识流量筛选的字段类型（如url表示URL路径）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type match_field: str
        :param match_field_index: **参数解释：** 子字段，匹配字段的细分维度（如无则不填）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type match_field_index: str
        :param logical_operator: **参数解释：** 逻辑运算符，标识匹配条件的逻辑关系（如contain表示包含）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type logical_operator: str
        :param match_contents: **参数解释：** 匹配内容，符合筛选条件的具体值列表（如特定URL路径）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type match_contents: list[str]
        :param value_list_res: **参数解释：** 引用表Id，关联预设的匹配内容列表ID（如无则不填）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type value_list_res: str
        """
        
        

        self._id = None
        self._match_field = None
        self._match_field_index = None
        self._logical_operator = None
        self._match_contents = None
        self._value_list_res = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if match_field is not None:
            self.match_field = match_field
        if match_field_index is not None:
            self.match_field_index = match_field_index
        if logical_operator is not None:
            self.logical_operator = logical_operator
        if match_contents is not None:
            self.match_contents = match_contents
        if value_list_res is not None:
            self.value_list_res = value_list_res

    @property
    def id(self):
        r"""Gets the id of this TrafficDetectionConditionDTO.

        **参数解释：** Id，唯一标识当前流量检测条件。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The id of this TrafficDetectionConditionDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this TrafficDetectionConditionDTO.

        **参数解释：** Id，唯一标识当前流量检测条件。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param id: The id of this TrafficDetectionConditionDTO.
        :type id: str
        """
        self._id = id

    @property
    def match_field(self):
        r"""Gets the match_field of this TrafficDetectionConditionDTO.

        **参数解释：** 匹配字段（类别），标识流量筛选的字段类型（如url表示URL路径）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The match_field of this TrafficDetectionConditionDTO.
        :rtype: str
        """
        return self._match_field

    @match_field.setter
    def match_field(self, match_field):
        r"""Sets the match_field of this TrafficDetectionConditionDTO.

        **参数解释：** 匹配字段（类别），标识流量筛选的字段类型（如url表示URL路径）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param match_field: The match_field of this TrafficDetectionConditionDTO.
        :type match_field: str
        """
        self._match_field = match_field

    @property
    def match_field_index(self):
        r"""Gets the match_field_index of this TrafficDetectionConditionDTO.

        **参数解释：** 子字段，匹配字段的细分维度（如无则不填）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The match_field_index of this TrafficDetectionConditionDTO.
        :rtype: str
        """
        return self._match_field_index

    @match_field_index.setter
    def match_field_index(self, match_field_index):
        r"""Sets the match_field_index of this TrafficDetectionConditionDTO.

        **参数解释：** 子字段，匹配字段的细分维度（如无则不填）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param match_field_index: The match_field_index of this TrafficDetectionConditionDTO.
        :type match_field_index: str
        """
        self._match_field_index = match_field_index

    @property
    def logical_operator(self):
        r"""Gets the logical_operator of this TrafficDetectionConditionDTO.

        **参数解释：** 逻辑运算符，标识匹配条件的逻辑关系（如contain表示包含）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The logical_operator of this TrafficDetectionConditionDTO.
        :rtype: str
        """
        return self._logical_operator

    @logical_operator.setter
    def logical_operator(self, logical_operator):
        r"""Sets the logical_operator of this TrafficDetectionConditionDTO.

        **参数解释：** 逻辑运算符，标识匹配条件的逻辑关系（如contain表示包含）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param logical_operator: The logical_operator of this TrafficDetectionConditionDTO.
        :type logical_operator: str
        """
        self._logical_operator = logical_operator

    @property
    def match_contents(self):
        r"""Gets the match_contents of this TrafficDetectionConditionDTO.

        **参数解释：** 匹配内容，符合筛选条件的具体值列表（如特定URL路径）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The match_contents of this TrafficDetectionConditionDTO.
        :rtype: list[str]
        """
        return self._match_contents

    @match_contents.setter
    def match_contents(self, match_contents):
        r"""Sets the match_contents of this TrafficDetectionConditionDTO.

        **参数解释：** 匹配内容，符合筛选条件的具体值列表（如特定URL路径）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param match_contents: The match_contents of this TrafficDetectionConditionDTO.
        :type match_contents: list[str]
        """
        self._match_contents = match_contents

    @property
    def value_list_res(self):
        r"""Gets the value_list_res of this TrafficDetectionConditionDTO.

        **参数解释：** 引用表Id，关联预设的匹配内容列表ID（如无则不填）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The value_list_res of this TrafficDetectionConditionDTO.
        :rtype: str
        """
        return self._value_list_res

    @value_list_res.setter
    def value_list_res(self, value_list_res):
        r"""Sets the value_list_res of this TrafficDetectionConditionDTO.

        **参数解释：** 引用表Id，关联预设的匹配内容列表ID（如无则不填）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param value_list_res: The value_list_res of this TrafficDetectionConditionDTO.
        :type value_list_res: str
        """
        self._value_list_res = value_list_res

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
        if not isinstance(other, TrafficDetectionConditionDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
