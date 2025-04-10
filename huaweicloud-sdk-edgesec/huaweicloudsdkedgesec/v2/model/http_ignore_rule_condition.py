# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HttpIgnoreRuleCondition:

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
        'index': 'str',
        'contents': 'list[str]',
        'logic_operation': 'str',
        'value_list_id': 'str',
        'size': 'int',
        'check_all_indexes_logic': 'int'
    }

    attribute_map = {
        'category': 'category',
        'index': 'index',
        'contents': 'contents',
        'logic_operation': 'logic_operation',
        'value_list_id': 'value_list_id',
        'size': 'size',
        'check_all_indexes_logic': 'check_all_indexes_logic'
    }

    def __init__(self, category=None, index=None, contents=None, logic_operation=None, value_list_id=None, size=None, check_all_indexes_logic=None):
        r"""HttpIgnoreRuleCondition

        The model defined in huaweicloud sdk

        :param category: 字段类型，可选值有ip、url、params、cookie、header
        :type category: str
        :param index: 字段类型为ip且子字段为客户端ip时，不需要传index参数；子字段类型为X-Forwarded-For时，值为x-forwarded-for；字段类型为params、header、cookie并且子字段为自定义时，index的值为自定义子字段
        :type index: str
        :param contents: 内容列表
        :type contents: list[str]
        :param logic_operation: 匹配逻辑，匹配逻辑根据字段类型变化，字段类型为ip时，匹配逻辑支持（equal：等于，not_equal：不等于），字段类型为url、header、params、cookie时，匹配逻辑支持（equal：等于，not_equal：不等于，contain：包含，not_contain：不包含，prefix：前缀为，not_prefix：前缀不为，suffix：后缀为，not_suffix：后缀不为，regular_match：正则匹配，regular_not_match：正则不匹配）
        :type logic_operation: str
        :param value_list_id: 引用表id
        :type value_list_id: str
        :param size: 若防护规则涉及阈值，即使用该字段
        :type size: int
        :param check_all_indexes_logic: 1.所有子字段/2.任意子字段
        :type check_all_indexes_logic: int
        """
        
        

        self._category = None
        self._index = None
        self._contents = None
        self._logic_operation = None
        self._value_list_id = None
        self._size = None
        self._check_all_indexes_logic = None
        self.discriminator = None

        self.category = category
        if index is not None:
            self.index = index
        self.contents = contents
        self.logic_operation = logic_operation
        if value_list_id is not None:
            self.value_list_id = value_list_id
        if size is not None:
            self.size = size
        if check_all_indexes_logic is not None:
            self.check_all_indexes_logic = check_all_indexes_logic

    @property
    def category(self):
        r"""Gets the category of this HttpIgnoreRuleCondition.

        字段类型，可选值有ip、url、params、cookie、header

        :return: The category of this HttpIgnoreRuleCondition.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this HttpIgnoreRuleCondition.

        字段类型，可选值有ip、url、params、cookie、header

        :param category: The category of this HttpIgnoreRuleCondition.
        :type category: str
        """
        self._category = category

    @property
    def index(self):
        r"""Gets the index of this HttpIgnoreRuleCondition.

        字段类型为ip且子字段为客户端ip时，不需要传index参数；子字段类型为X-Forwarded-For时，值为x-forwarded-for；字段类型为params、header、cookie并且子字段为自定义时，index的值为自定义子字段

        :return: The index of this HttpIgnoreRuleCondition.
        :rtype: str
        """
        return self._index

    @index.setter
    def index(self, index):
        r"""Sets the index of this HttpIgnoreRuleCondition.

        字段类型为ip且子字段为客户端ip时，不需要传index参数；子字段类型为X-Forwarded-For时，值为x-forwarded-for；字段类型为params、header、cookie并且子字段为自定义时，index的值为自定义子字段

        :param index: The index of this HttpIgnoreRuleCondition.
        :type index: str
        """
        self._index = index

    @property
    def contents(self):
        r"""Gets the contents of this HttpIgnoreRuleCondition.

        内容列表

        :return: The contents of this HttpIgnoreRuleCondition.
        :rtype: list[str]
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        r"""Sets the contents of this HttpIgnoreRuleCondition.

        内容列表

        :param contents: The contents of this HttpIgnoreRuleCondition.
        :type contents: list[str]
        """
        self._contents = contents

    @property
    def logic_operation(self):
        r"""Gets the logic_operation of this HttpIgnoreRuleCondition.

        匹配逻辑，匹配逻辑根据字段类型变化，字段类型为ip时，匹配逻辑支持（equal：等于，not_equal：不等于），字段类型为url、header、params、cookie时，匹配逻辑支持（equal：等于，not_equal：不等于，contain：包含，not_contain：不包含，prefix：前缀为，not_prefix：前缀不为，suffix：后缀为，not_suffix：后缀不为，regular_match：正则匹配，regular_not_match：正则不匹配）

        :return: The logic_operation of this HttpIgnoreRuleCondition.
        :rtype: str
        """
        return self._logic_operation

    @logic_operation.setter
    def logic_operation(self, logic_operation):
        r"""Sets the logic_operation of this HttpIgnoreRuleCondition.

        匹配逻辑，匹配逻辑根据字段类型变化，字段类型为ip时，匹配逻辑支持（equal：等于，not_equal：不等于），字段类型为url、header、params、cookie时，匹配逻辑支持（equal：等于，not_equal：不等于，contain：包含，not_contain：不包含，prefix：前缀为，not_prefix：前缀不为，suffix：后缀为，not_suffix：后缀不为，regular_match：正则匹配，regular_not_match：正则不匹配）

        :param logic_operation: The logic_operation of this HttpIgnoreRuleCondition.
        :type logic_operation: str
        """
        self._logic_operation = logic_operation

    @property
    def value_list_id(self):
        r"""Gets the value_list_id of this HttpIgnoreRuleCondition.

        引用表id

        :return: The value_list_id of this HttpIgnoreRuleCondition.
        :rtype: str
        """
        return self._value_list_id

    @value_list_id.setter
    def value_list_id(self, value_list_id):
        r"""Sets the value_list_id of this HttpIgnoreRuleCondition.

        引用表id

        :param value_list_id: The value_list_id of this HttpIgnoreRuleCondition.
        :type value_list_id: str
        """
        self._value_list_id = value_list_id

    @property
    def size(self):
        r"""Gets the size of this HttpIgnoreRuleCondition.

        若防护规则涉及阈值，即使用该字段

        :return: The size of this HttpIgnoreRuleCondition.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this HttpIgnoreRuleCondition.

        若防护规则涉及阈值，即使用该字段

        :param size: The size of this HttpIgnoreRuleCondition.
        :type size: int
        """
        self._size = size

    @property
    def check_all_indexes_logic(self):
        r"""Gets the check_all_indexes_logic of this HttpIgnoreRuleCondition.

        1.所有子字段/2.任意子字段

        :return: The check_all_indexes_logic of this HttpIgnoreRuleCondition.
        :rtype: int
        """
        return self._check_all_indexes_logic

    @check_all_indexes_logic.setter
    def check_all_indexes_logic(self, check_all_indexes_logic):
        r"""Sets the check_all_indexes_logic of this HttpIgnoreRuleCondition.

        1.所有子字段/2.任意子字段

        :param check_all_indexes_logic: The check_all_indexes_logic of this HttpIgnoreRuleCondition.
        :type check_all_indexes_logic: int
        """
        self._check_all_indexes_logic = check_all_indexes_logic

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
        if not isinstance(other, HttpIgnoreRuleCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
