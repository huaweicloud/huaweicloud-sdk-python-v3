# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Condition:

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
        'contents': 'list[str]',
        'logic_operation': 'str',
        'check_all_indexes_logic': 'int',
        'index': 'str'
    }

    attribute_map = {
        'category': 'category',
        'contents': 'contents',
        'logic_operation': 'logic_operation',
        'check_all_indexes_logic': 'check_all_indexes_logic',
        'index': 'index'
    }

    def __init__(self, category=None, contents=None, logic_operation=None, check_all_indexes_logic=None, index=None):
        """Condition

        The model defined in huaweicloud sdk

        :param category: 字段类型，可选值有ip、url、params、cookie、header
        :type category: str
        :param contents: 内容,数组长度限制为1，内容格式根据字段类型变化，例如，字段类型为ip时，contents内容格式需为ip地址或ip地址段；字段类型为url时，contents内容格式需为标准url格式；字段类型为params、cookie、header时，内容的格式不做限制
        :type contents: list[str]
        :param logic_operation: 匹配逻辑，匹配逻辑根据字段类型变化，字段类型为ip时，匹配逻辑支持（equal：等于，not_equal：不等于），字段类型为url、header、params、cookie时，匹配逻辑支持（equal：等于，not_equal：不等于，contain：包含，not_contain：不包含，prefix：前缀为，not_prefix：前缀不为，suffix：后缀为，not_suffix：后缀不为，regular_match：正则匹配，regular_not_match：正则不匹配）
        :type logic_operation: str
        :param check_all_indexes_logic: 字段类型为url或ip时不存在check_all_indexes_logic字段，其它情况下（1：检查所有子字段，2：检查任意子字段，null：使用自定义子字段）
        :type check_all_indexes_logic: int
        :param index: 字段类型为ip且子字段为客户端ip时，不存在index参数；子字段类型为X-Forwarded-For时，值为x-forwarded-for，字段类型为params、header、cookie并且子字段为自定义时，index的值为自定义子字段
        :type index: str
        """
        
        

        self._category = None
        self._contents = None
        self._logic_operation = None
        self._check_all_indexes_logic = None
        self._index = None
        self.discriminator = None

        if category is not None:
            self.category = category
        if contents is not None:
            self.contents = contents
        if logic_operation is not None:
            self.logic_operation = logic_operation
        if check_all_indexes_logic is not None:
            self.check_all_indexes_logic = check_all_indexes_logic
        if index is not None:
            self.index = index

    @property
    def category(self):
        """Gets the category of this Condition.

        字段类型，可选值有ip、url、params、cookie、header

        :return: The category of this Condition.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this Condition.

        字段类型，可选值有ip、url、params、cookie、header

        :param category: The category of this Condition.
        :type category: str
        """
        self._category = category

    @property
    def contents(self):
        """Gets the contents of this Condition.

        内容,数组长度限制为1，内容格式根据字段类型变化，例如，字段类型为ip时，contents内容格式需为ip地址或ip地址段；字段类型为url时，contents内容格式需为标准url格式；字段类型为params、cookie、header时，内容的格式不做限制

        :return: The contents of this Condition.
        :rtype: list[str]
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        """Sets the contents of this Condition.

        内容,数组长度限制为1，内容格式根据字段类型变化，例如，字段类型为ip时，contents内容格式需为ip地址或ip地址段；字段类型为url时，contents内容格式需为标准url格式；字段类型为params、cookie、header时，内容的格式不做限制

        :param contents: The contents of this Condition.
        :type contents: list[str]
        """
        self._contents = contents

    @property
    def logic_operation(self):
        """Gets the logic_operation of this Condition.

        匹配逻辑，匹配逻辑根据字段类型变化，字段类型为ip时，匹配逻辑支持（equal：等于，not_equal：不等于），字段类型为url、header、params、cookie时，匹配逻辑支持（equal：等于，not_equal：不等于，contain：包含，not_contain：不包含，prefix：前缀为，not_prefix：前缀不为，suffix：后缀为，not_suffix：后缀不为，regular_match：正则匹配，regular_not_match：正则不匹配）

        :return: The logic_operation of this Condition.
        :rtype: str
        """
        return self._logic_operation

    @logic_operation.setter
    def logic_operation(self, logic_operation):
        """Sets the logic_operation of this Condition.

        匹配逻辑，匹配逻辑根据字段类型变化，字段类型为ip时，匹配逻辑支持（equal：等于，not_equal：不等于），字段类型为url、header、params、cookie时，匹配逻辑支持（equal：等于，not_equal：不等于，contain：包含，not_contain：不包含，prefix：前缀为，not_prefix：前缀不为，suffix：后缀为，not_suffix：后缀不为，regular_match：正则匹配，regular_not_match：正则不匹配）

        :param logic_operation: The logic_operation of this Condition.
        :type logic_operation: str
        """
        self._logic_operation = logic_operation

    @property
    def check_all_indexes_logic(self):
        """Gets the check_all_indexes_logic of this Condition.

        字段类型为url或ip时不存在check_all_indexes_logic字段，其它情况下（1：检查所有子字段，2：检查任意子字段，null：使用自定义子字段）

        :return: The check_all_indexes_logic of this Condition.
        :rtype: int
        """
        return self._check_all_indexes_logic

    @check_all_indexes_logic.setter
    def check_all_indexes_logic(self, check_all_indexes_logic):
        """Sets the check_all_indexes_logic of this Condition.

        字段类型为url或ip时不存在check_all_indexes_logic字段，其它情况下（1：检查所有子字段，2：检查任意子字段，null：使用自定义子字段）

        :param check_all_indexes_logic: The check_all_indexes_logic of this Condition.
        :type check_all_indexes_logic: int
        """
        self._check_all_indexes_logic = check_all_indexes_logic

    @property
    def index(self):
        """Gets the index of this Condition.

        字段类型为ip且子字段为客户端ip时，不存在index参数；子字段类型为X-Forwarded-For时，值为x-forwarded-for，字段类型为params、header、cookie并且子字段为自定义时，index的值为自定义子字段

        :return: The index of this Condition.
        :rtype: str
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this Condition.

        字段类型为ip且子字段为客户端ip时，不存在index参数；子字段类型为X-Forwarded-For时，值为x-forwarded-for，字段类型为params、header、cookie并且子字段为自定义时，index的值为自定义子字段

        :param index: The index of this Condition.
        :type index: str
        """
        self._index = index

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
        if not isinstance(other, Condition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
