# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HttpAccessControlRuleCondition:

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
        r"""HttpAccessControlRuleCondition

        The model defined in huaweicloud sdk

        :param category: 字段类型。可选值为：url、custom_asn、custom_geoip、robot、user-agent、ip、params、cookie、referer、header、method、request_line、request、response_code、response_length、response_time、response_header、response_body
        :type category: str
        :param index: 子字段：  - 字段类型为url、custom_asn、custom_geoip、robot、user-agent、referer、request_line、method、request、response_code、response_length、response_time、response_body时，不需要传index参数    - 字段类型为params、cookie、header、response_header并且子字段为自定义时，index的值为自定义子字段
        :type index: str
        :param contents: 内容列表
        :type contents: list[str]
        :param logic_operation: 处理逻辑
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

        if category is not None:
            self.category = category
        if index is not None:
            self.index = index
        if contents is not None:
            self.contents = contents
        if logic_operation is not None:
            self.logic_operation = logic_operation
        if value_list_id is not None:
            self.value_list_id = value_list_id
        if size is not None:
            self.size = size
        if check_all_indexes_logic is not None:
            self.check_all_indexes_logic = check_all_indexes_logic

    @property
    def category(self):
        r"""Gets the category of this HttpAccessControlRuleCondition.

        字段类型。可选值为：url、custom_asn、custom_geoip、robot、user-agent、ip、params、cookie、referer、header、method、request_line、request、response_code、response_length、response_time、response_header、response_body

        :return: The category of this HttpAccessControlRuleCondition.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this HttpAccessControlRuleCondition.

        字段类型。可选值为：url、custom_asn、custom_geoip、robot、user-agent、ip、params、cookie、referer、header、method、request_line、request、response_code、response_length、response_time、response_header、response_body

        :param category: The category of this HttpAccessControlRuleCondition.
        :type category: str
        """
        self._category = category

    @property
    def index(self):
        r"""Gets the index of this HttpAccessControlRuleCondition.

        子字段：  - 字段类型为url、custom_asn、custom_geoip、robot、user-agent、referer、request_line、method、request、response_code、response_length、response_time、response_body时，不需要传index参数    - 字段类型为params、cookie、header、response_header并且子字段为自定义时，index的值为自定义子字段

        :return: The index of this HttpAccessControlRuleCondition.
        :rtype: str
        """
        return self._index

    @index.setter
    def index(self, index):
        r"""Sets the index of this HttpAccessControlRuleCondition.

        子字段：  - 字段类型为url、custom_asn、custom_geoip、robot、user-agent、referer、request_line、method、request、response_code、response_length、response_time、response_body时，不需要传index参数    - 字段类型为params、cookie、header、response_header并且子字段为自定义时，index的值为自定义子字段

        :param index: The index of this HttpAccessControlRuleCondition.
        :type index: str
        """
        self._index = index

    @property
    def contents(self):
        r"""Gets the contents of this HttpAccessControlRuleCondition.

        内容列表

        :return: The contents of this HttpAccessControlRuleCondition.
        :rtype: list[str]
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        r"""Sets the contents of this HttpAccessControlRuleCondition.

        内容列表

        :param contents: The contents of this HttpAccessControlRuleCondition.
        :type contents: list[str]
        """
        self._contents = contents

    @property
    def logic_operation(self):
        r"""Gets the logic_operation of this HttpAccessControlRuleCondition.

        处理逻辑

        :return: The logic_operation of this HttpAccessControlRuleCondition.
        :rtype: str
        """
        return self._logic_operation

    @logic_operation.setter
    def logic_operation(self, logic_operation):
        r"""Sets the logic_operation of this HttpAccessControlRuleCondition.

        处理逻辑

        :param logic_operation: The logic_operation of this HttpAccessControlRuleCondition.
        :type logic_operation: str
        """
        self._logic_operation = logic_operation

    @property
    def value_list_id(self):
        r"""Gets the value_list_id of this HttpAccessControlRuleCondition.

        引用表id

        :return: The value_list_id of this HttpAccessControlRuleCondition.
        :rtype: str
        """
        return self._value_list_id

    @value_list_id.setter
    def value_list_id(self, value_list_id):
        r"""Sets the value_list_id of this HttpAccessControlRuleCondition.

        引用表id

        :param value_list_id: The value_list_id of this HttpAccessControlRuleCondition.
        :type value_list_id: str
        """
        self._value_list_id = value_list_id

    @property
    def size(self):
        r"""Gets the size of this HttpAccessControlRuleCondition.

        若防护规则涉及阈值，即使用该字段

        :return: The size of this HttpAccessControlRuleCondition.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this HttpAccessControlRuleCondition.

        若防护规则涉及阈值，即使用该字段

        :param size: The size of this HttpAccessControlRuleCondition.
        :type size: int
        """
        self._size = size

    @property
    def check_all_indexes_logic(self):
        r"""Gets the check_all_indexes_logic of this HttpAccessControlRuleCondition.

        1.所有子字段/2.任意子字段

        :return: The check_all_indexes_logic of this HttpAccessControlRuleCondition.
        :rtype: int
        """
        return self._check_all_indexes_logic

    @check_all_indexes_logic.setter
    def check_all_indexes_logic(self, check_all_indexes_logic):
        r"""Sets the check_all_indexes_logic of this HttpAccessControlRuleCondition.

        1.所有子字段/2.任意子字段

        :param check_all_indexes_logic: The check_all_indexes_logic of this HttpAccessControlRuleCondition.
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
        if not isinstance(other, HttpAccessControlRuleCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
