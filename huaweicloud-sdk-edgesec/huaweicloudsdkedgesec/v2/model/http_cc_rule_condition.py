# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HttpCcRuleCondition:

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
        r"""HttpCcRuleCondition

        The model defined in huaweicloud sdk

        :param category: 防护规则字段
        :type category: str
        :param index: 子字段，当字段类型（category）选择“params”、“cookie”、“header”时，请根据实际需求配置子字段且该参数必填。
        :type index: str
        :param contents: 条件列表逻辑匹配内容。当logic_operation参数不以any或者all结尾时，需要传该参数。
        :type contents: list[str]
        :param logic_operation: 条件列表匹配逻辑。   -  如果字段类型category是url， 匹配逻辑可以为：contain、 not_contain、 equal、 not_equal、 prefix、 not_prefix、 suffix、 not_suffix、 contain_any、 not_contain_all、 equal_any、 not_equal_all、 equal_any、 not_equal_all、 prefix_any、 not_prefix_all、 suffix_any、 not_suffix_all、 len_greater、 len_less、len_equal或者len_not_equal   - 如果字段类型category是ip或者ipv6，匹配逻辑可以为： equal、not_equal、equal_any或者not_equal_all   - 如果字段类型category是params、cookie或者header, 匹配逻辑可以为：contain、 not_contain、 equal、 not_equal、 prefix、 not_prefix、 suffix、 not_suffix、 contain_any、 not_contain_all、 equal_any、not_equal_all、 equal_any、 not_equal_all、 prefix_any、 not_prefix_all、 suffix_any、 not_suffix_all、 len_greater、 len_less、len_equal、len_not_equal、、num_greater、num_less、num_equal、num_not_equal、exist或者not_exist
        :type logic_operation: str
        :param value_list_id: 引用表id。当logic_operation参数以any或者all结尾时，需要传该参数。此外，引用表类型要与category类型保持一致。
        :type value_list_id: str
        :param size: 若防护规则涉及阈值，即使用该字段
        :type size: int
        :param check_all_indexes_logic: - 1：所有子字段 - 2：任意子字段 
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
        if contents is not None:
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
        r"""Gets the category of this HttpCcRuleCondition.

        防护规则字段

        :return: The category of this HttpCcRuleCondition.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this HttpCcRuleCondition.

        防护规则字段

        :param category: The category of this HttpCcRuleCondition.
        :type category: str
        """
        self._category = category

    @property
    def index(self):
        r"""Gets the index of this HttpCcRuleCondition.

        子字段，当字段类型（category）选择“params”、“cookie”、“header”时，请根据实际需求配置子字段且该参数必填。

        :return: The index of this HttpCcRuleCondition.
        :rtype: str
        """
        return self._index

    @index.setter
    def index(self, index):
        r"""Sets the index of this HttpCcRuleCondition.

        子字段，当字段类型（category）选择“params”、“cookie”、“header”时，请根据实际需求配置子字段且该参数必填。

        :param index: The index of this HttpCcRuleCondition.
        :type index: str
        """
        self._index = index

    @property
    def contents(self):
        r"""Gets the contents of this HttpCcRuleCondition.

        条件列表逻辑匹配内容。当logic_operation参数不以any或者all结尾时，需要传该参数。

        :return: The contents of this HttpCcRuleCondition.
        :rtype: list[str]
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        r"""Sets the contents of this HttpCcRuleCondition.

        条件列表逻辑匹配内容。当logic_operation参数不以any或者all结尾时，需要传该参数。

        :param contents: The contents of this HttpCcRuleCondition.
        :type contents: list[str]
        """
        self._contents = contents

    @property
    def logic_operation(self):
        r"""Gets the logic_operation of this HttpCcRuleCondition.

        条件列表匹配逻辑。   -  如果字段类型category是url， 匹配逻辑可以为：contain、 not_contain、 equal、 not_equal、 prefix、 not_prefix、 suffix、 not_suffix、 contain_any、 not_contain_all、 equal_any、 not_equal_all、 equal_any、 not_equal_all、 prefix_any、 not_prefix_all、 suffix_any、 not_suffix_all、 len_greater、 len_less、len_equal或者len_not_equal   - 如果字段类型category是ip或者ipv6，匹配逻辑可以为： equal、not_equal、equal_any或者not_equal_all   - 如果字段类型category是params、cookie或者header, 匹配逻辑可以为：contain、 not_contain、 equal、 not_equal、 prefix、 not_prefix、 suffix、 not_suffix、 contain_any、 not_contain_all、 equal_any、not_equal_all、 equal_any、 not_equal_all、 prefix_any、 not_prefix_all、 suffix_any、 not_suffix_all、 len_greater、 len_less、len_equal、len_not_equal、、num_greater、num_less、num_equal、num_not_equal、exist或者not_exist

        :return: The logic_operation of this HttpCcRuleCondition.
        :rtype: str
        """
        return self._logic_operation

    @logic_operation.setter
    def logic_operation(self, logic_operation):
        r"""Sets the logic_operation of this HttpCcRuleCondition.

        条件列表匹配逻辑。   -  如果字段类型category是url， 匹配逻辑可以为：contain、 not_contain、 equal、 not_equal、 prefix、 not_prefix、 suffix、 not_suffix、 contain_any、 not_contain_all、 equal_any、 not_equal_all、 equal_any、 not_equal_all、 prefix_any、 not_prefix_all、 suffix_any、 not_suffix_all、 len_greater、 len_less、len_equal或者len_not_equal   - 如果字段类型category是ip或者ipv6，匹配逻辑可以为： equal、not_equal、equal_any或者not_equal_all   - 如果字段类型category是params、cookie或者header, 匹配逻辑可以为：contain、 not_contain、 equal、 not_equal、 prefix、 not_prefix、 suffix、 not_suffix、 contain_any、 not_contain_all、 equal_any、not_equal_all、 equal_any、 not_equal_all、 prefix_any、 not_prefix_all、 suffix_any、 not_suffix_all、 len_greater、 len_less、len_equal、len_not_equal、、num_greater、num_less、num_equal、num_not_equal、exist或者not_exist

        :param logic_operation: The logic_operation of this HttpCcRuleCondition.
        :type logic_operation: str
        """
        self._logic_operation = logic_operation

    @property
    def value_list_id(self):
        r"""Gets the value_list_id of this HttpCcRuleCondition.

        引用表id。当logic_operation参数以any或者all结尾时，需要传该参数。此外，引用表类型要与category类型保持一致。

        :return: The value_list_id of this HttpCcRuleCondition.
        :rtype: str
        """
        return self._value_list_id

    @value_list_id.setter
    def value_list_id(self, value_list_id):
        r"""Sets the value_list_id of this HttpCcRuleCondition.

        引用表id。当logic_operation参数以any或者all结尾时，需要传该参数。此外，引用表类型要与category类型保持一致。

        :param value_list_id: The value_list_id of this HttpCcRuleCondition.
        :type value_list_id: str
        """
        self._value_list_id = value_list_id

    @property
    def size(self):
        r"""Gets the size of this HttpCcRuleCondition.

        若防护规则涉及阈值，即使用该字段

        :return: The size of this HttpCcRuleCondition.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this HttpCcRuleCondition.

        若防护规则涉及阈值，即使用该字段

        :param size: The size of this HttpCcRuleCondition.
        :type size: int
        """
        self._size = size

    @property
    def check_all_indexes_logic(self):
        r"""Gets the check_all_indexes_logic of this HttpCcRuleCondition.

        - 1：所有子字段 - 2：任意子字段 

        :return: The check_all_indexes_logic of this HttpCcRuleCondition.
        :rtype: int
        """
        return self._check_all_indexes_logic

    @check_all_indexes_logic.setter
    def check_all_indexes_logic(self, check_all_indexes_logic):
        r"""Sets the check_all_indexes_logic of this HttpCcRuleCondition.

        - 1：所有子字段 - 2：任意子字段 

        :param check_all_indexes_logic: The check_all_indexes_logic of this HttpCcRuleCondition.
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
        if not isinstance(other, HttpCcRuleCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
