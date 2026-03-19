# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AnticrawlerCondition:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'category': 'str',
        'logic_operation': 'str',
        'contents': 'list[str]',
        'value_list_id': 'str'
    }

    attribute_map = {
        'category': 'category',
        'logic_operation': 'logic_operation',
        'contents': 'contents',
        'value_list_id': 'value_list_id'
    }

    def __init__(self, category=None, logic_operation=None, contents=None, value_list_id=None):
        r"""AnticrawlerCondition

        The model defined in huaweicloud sdk

        :param category: **参数解释：** 字段类型 **约束限制：** 不涉及 **取值范围：**  - url  - user-agent **默认取值：** 不涉及
        :type category: str
        :param logic_operation: **参数解释：** 条件列表匹配逻辑 **约束限制：** 不涉及 **取值范围：** - contain_any: 包含任意一个 - not_contain_all: 不包含全部 - equal_any: 等于任意一个 - not_equal_all: 不等于全部 - prefix_any: 前缀匹配任意一个 - not_prefix_all: 前缀不匹配全部 - suffix_any: 后缀匹配任意一个 - not_suffix_all: 后缀不匹配全部 - contain: 包含 - not_contain: 不包含 - equal: 等于 - not_equal: 不等于 - prefix: 前缀匹配 - not_prefix: 前缀不匹配 - suffix: 后缀匹配 - not_suffix: 后缀不匹配 - len_equal: 长度等于 - len_not_equal: 长度不等于 - len_greater: 长度大于 - len_less: 长度小于 - len_greater_equal: 长度大于等于 - len_less_equal: 长度小于等于 - regular_match: 正则匹配 - regular_not_match: 正则不匹配 **默认取值：** 不涉及
        :type logic_operation: str
        :param contents: **参数解释：** 条件列表逻辑匹配内容 **约束限制：** 当logic_operation参数不以any或者all结尾时，需要传该参数；仅支持单个匹配内容 **取值范围：** 匹配内容字符串长度范围：[1, 4096] **默认取值：** 不涉及
        :type contents: list[str]
        :param value_list_id: **参数解释：** 引用表ID **约束限制：** 当logic_operation参数以any或者all结尾时，需要传该参数；引用表类型要与category类型保持一致 **取值范围：** 通过ListValueList接口获取引用表ID **默认取值：** 不涉及
        :type value_list_id: str
        """
        
        

        self._category = None
        self._logic_operation = None
        self._contents = None
        self._value_list_id = None
        self.discriminator = None

        self.category = category
        self.logic_operation = logic_operation
        if contents is not None:
            self.contents = contents
        if value_list_id is not None:
            self.value_list_id = value_list_id

    @property
    def category(self):
        r"""Gets the category of this AnticrawlerCondition.

        **参数解释：** 字段类型 **约束限制：** 不涉及 **取值范围：**  - url  - user-agent **默认取值：** 不涉及

        :return: The category of this AnticrawlerCondition.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this AnticrawlerCondition.

        **参数解释：** 字段类型 **约束限制：** 不涉及 **取值范围：**  - url  - user-agent **默认取值：** 不涉及

        :param category: The category of this AnticrawlerCondition.
        :type category: str
        """
        self._category = category

    @property
    def logic_operation(self):
        r"""Gets the logic_operation of this AnticrawlerCondition.

        **参数解释：** 条件列表匹配逻辑 **约束限制：** 不涉及 **取值范围：** - contain_any: 包含任意一个 - not_contain_all: 不包含全部 - equal_any: 等于任意一个 - not_equal_all: 不等于全部 - prefix_any: 前缀匹配任意一个 - not_prefix_all: 前缀不匹配全部 - suffix_any: 后缀匹配任意一个 - not_suffix_all: 后缀不匹配全部 - contain: 包含 - not_contain: 不包含 - equal: 等于 - not_equal: 不等于 - prefix: 前缀匹配 - not_prefix: 前缀不匹配 - suffix: 后缀匹配 - not_suffix: 后缀不匹配 - len_equal: 长度等于 - len_not_equal: 长度不等于 - len_greater: 长度大于 - len_less: 长度小于 - len_greater_equal: 长度大于等于 - len_less_equal: 长度小于等于 - regular_match: 正则匹配 - regular_not_match: 正则不匹配 **默认取值：** 不涉及

        :return: The logic_operation of this AnticrawlerCondition.
        :rtype: str
        """
        return self._logic_operation

    @logic_operation.setter
    def logic_operation(self, logic_operation):
        r"""Sets the logic_operation of this AnticrawlerCondition.

        **参数解释：** 条件列表匹配逻辑 **约束限制：** 不涉及 **取值范围：** - contain_any: 包含任意一个 - not_contain_all: 不包含全部 - equal_any: 等于任意一个 - not_equal_all: 不等于全部 - prefix_any: 前缀匹配任意一个 - not_prefix_all: 前缀不匹配全部 - suffix_any: 后缀匹配任意一个 - not_suffix_all: 后缀不匹配全部 - contain: 包含 - not_contain: 不包含 - equal: 等于 - not_equal: 不等于 - prefix: 前缀匹配 - not_prefix: 前缀不匹配 - suffix: 后缀匹配 - not_suffix: 后缀不匹配 - len_equal: 长度等于 - len_not_equal: 长度不等于 - len_greater: 长度大于 - len_less: 长度小于 - len_greater_equal: 长度大于等于 - len_less_equal: 长度小于等于 - regular_match: 正则匹配 - regular_not_match: 正则不匹配 **默认取值：** 不涉及

        :param logic_operation: The logic_operation of this AnticrawlerCondition.
        :type logic_operation: str
        """
        self._logic_operation = logic_operation

    @property
    def contents(self):
        r"""Gets the contents of this AnticrawlerCondition.

        **参数解释：** 条件列表逻辑匹配内容 **约束限制：** 当logic_operation参数不以any或者all结尾时，需要传该参数；仅支持单个匹配内容 **取值范围：** 匹配内容字符串长度范围：[1, 4096] **默认取值：** 不涉及

        :return: The contents of this AnticrawlerCondition.
        :rtype: list[str]
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        r"""Sets the contents of this AnticrawlerCondition.

        **参数解释：** 条件列表逻辑匹配内容 **约束限制：** 当logic_operation参数不以any或者all结尾时，需要传该参数；仅支持单个匹配内容 **取值范围：** 匹配内容字符串长度范围：[1, 4096] **默认取值：** 不涉及

        :param contents: The contents of this AnticrawlerCondition.
        :type contents: list[str]
        """
        self._contents = contents

    @property
    def value_list_id(self):
        r"""Gets the value_list_id of this AnticrawlerCondition.

        **参数解释：** 引用表ID **约束限制：** 当logic_operation参数以any或者all结尾时，需要传该参数；引用表类型要与category类型保持一致 **取值范围：** 通过ListValueList接口获取引用表ID **默认取值：** 不涉及

        :return: The value_list_id of this AnticrawlerCondition.
        :rtype: str
        """
        return self._value_list_id

    @value_list_id.setter
    def value_list_id(self, value_list_id):
        r"""Sets the value_list_id of this AnticrawlerCondition.

        **参数解释：** 引用表ID **约束限制：** 当logic_operation参数以any或者all结尾时，需要传该参数；引用表类型要与category类型保持一致 **取值范围：** 通过ListValueList接口获取引用表ID **默认取值：** 不涉及

        :param value_list_id: The value_list_id of this AnticrawlerCondition.
        :type value_list_id: str
        """
        self._value_list_id = value_list_id

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
        if not isinstance(other, AnticrawlerCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
