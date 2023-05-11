# coding: utf-8

import six

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
        """AnticrawlerCondition

        The model defined in huaweicloud sdk

        :param category: 字段类型
        :type category: str
        :param logic_operation: 条件列表匹配逻辑, 包括：contain、not_contain、equal、not_equal、prefix、not_prefix、suffix、not_suffix、contain_any、not_contain_all、equal_any、not_equal_all、prefix_any、not_prefix_all、suffix_any、not_suffix_all
        :type logic_operation: str
        :param contents: 条件列表逻辑匹配内容。当logic_operation参数不以any或者all结尾时，需要传该参数。
        :type contents: list[str]
        :param value_list_id: 引用表id。当logic_operation参数以any或者all结尾时，需要传该参数。此外，引用表类型要与category类型保持一致。
        :type value_list_id: str
        """
        
        

        self._category = None
        self._logic_operation = None
        self._contents = None
        self._value_list_id = None
        self.discriminator = None

        if category is not None:
            self.category = category
        if logic_operation is not None:
            self.logic_operation = logic_operation
        if contents is not None:
            self.contents = contents
        if value_list_id is not None:
            self.value_list_id = value_list_id

    @property
    def category(self):
        """Gets the category of this AnticrawlerCondition.

        字段类型

        :return: The category of this AnticrawlerCondition.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this AnticrawlerCondition.

        字段类型

        :param category: The category of this AnticrawlerCondition.
        :type category: str
        """
        self._category = category

    @property
    def logic_operation(self):
        """Gets the logic_operation of this AnticrawlerCondition.

        条件列表匹配逻辑, 包括：contain、not_contain、equal、not_equal、prefix、not_prefix、suffix、not_suffix、contain_any、not_contain_all、equal_any、not_equal_all、prefix_any、not_prefix_all、suffix_any、not_suffix_all

        :return: The logic_operation of this AnticrawlerCondition.
        :rtype: str
        """
        return self._logic_operation

    @logic_operation.setter
    def logic_operation(self, logic_operation):
        """Sets the logic_operation of this AnticrawlerCondition.

        条件列表匹配逻辑, 包括：contain、not_contain、equal、not_equal、prefix、not_prefix、suffix、not_suffix、contain_any、not_contain_all、equal_any、not_equal_all、prefix_any、not_prefix_all、suffix_any、not_suffix_all

        :param logic_operation: The logic_operation of this AnticrawlerCondition.
        :type logic_operation: str
        """
        self._logic_operation = logic_operation

    @property
    def contents(self):
        """Gets the contents of this AnticrawlerCondition.

        条件列表逻辑匹配内容。当logic_operation参数不以any或者all结尾时，需要传该参数。

        :return: The contents of this AnticrawlerCondition.
        :rtype: list[str]
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        """Sets the contents of this AnticrawlerCondition.

        条件列表逻辑匹配内容。当logic_operation参数不以any或者all结尾时，需要传该参数。

        :param contents: The contents of this AnticrawlerCondition.
        :type contents: list[str]
        """
        self._contents = contents

    @property
    def value_list_id(self):
        """Gets the value_list_id of this AnticrawlerCondition.

        引用表id。当logic_operation参数以any或者all结尾时，需要传该参数。此外，引用表类型要与category类型保持一致。

        :return: The value_list_id of this AnticrawlerCondition.
        :rtype: str
        """
        return self._value_list_id

    @value_list_id.setter
    def value_list_id(self, value_list_id):
        """Sets the value_list_id of this AnticrawlerCondition.

        引用表id。当logic_operation参数以any或者all结尾时，需要传该参数。此外，引用表类型要与category类型保持一致。

        :param value_list_id: The value_list_id of this AnticrawlerCondition.
        :type value_list_id: str
        """
        self._value_list_id = value_list_id

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
        if not isinstance(other, AnticrawlerCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
