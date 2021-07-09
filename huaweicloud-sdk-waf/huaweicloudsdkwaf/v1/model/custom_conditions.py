# coding: utf-8

import re
import six





class CustomConditions:


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
        'logic': 'int',
        'contents': 'list[str]',
        'value_list_id': 'str'
    }

    attribute_map = {
        'category': 'category',
        'index': 'index',
        'logic': 'logic',
        'contents': 'contents',
        'value_list_id': 'value_list_id'
    }

    def __init__(self, category=None, index=None, logic=None, contents=None, value_list_id=None):
        """CustomConditions - a model defined in huaweicloud sdk"""
        
        

        self._category = None
        self._index = None
        self._logic = None
        self._contents = None
        self._value_list_id = None
        self.discriminator = None

        if category is not None:
            self.category = category
        if index is not None:
            self.index = index
        if logic is not None:
            self.logic = logic
        if contents is not None:
            self.contents = contents
        if value_list_id is not None:
            self.value_list_id = value_list_id

    @property
    def category(self):
        """Gets the category of this CustomConditions.

        条件类型 固定值path、user-agent、ip、params、cookie、referer、header

        :return: The category of this CustomConditions.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this CustomConditions.

        条件类型 固定值path、user-agent、ip、params、cookie、referer、header

        :param category: The category of this CustomConditions.
        :type: str
        """
        self._category = category

    @property
    def index(self):
        """Gets the index of this CustomConditions.

        当“category”为“cookie”时，index表示cookie name。当“category”为“params”时，index表示param name。当“category”为“header”时，index表示header中的选项。

        :return: The index of this CustomConditions.
        :rtype: str
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this CustomConditions.

        当“category”为“cookie”时，index表示cookie name。当“category”为“params”时，index表示param name。当“category”为“header”时，index表示header中的选项。

        :param index: The index of this CustomConditions.
        :type: str
        """
        self._index = index

    @property
    def logic(self):
        """Gets the logic of this CustomConditions.

        “contain”，“not_contain”，“equal”,“not_equal”,“prefix”，“not_prefix”，“suffix”，“not_suffix”分别代表包含、不包含、等于、不等于、前缀为、前缀不为、后缀为、后缀不为。当条件类型“category”为ip时，“logic”只能为“equal”或者“not_equal”。

        :return: The logic of this CustomConditions.
        :rtype: int
        """
        return self._logic

    @logic.setter
    def logic(self, logic):
        """Sets the logic of this CustomConditions.

        “contain”，“not_contain”，“equal”,“not_equal”,“prefix”，“not_prefix”，“suffix”，“not_suffix”分别代表包含、不包含、等于、不等于、前缀为、前缀不为、后缀为、后缀不为。当条件类型“category”为ip时，“logic”只能为“equal”或者“not_equal”。

        :param logic: The logic of this CustomConditions.
        :type: int
        """
        self._logic = logic

    @property
    def contents(self):
        """Gets the contents of this CustomConditions.

        条件匹配的内容

        :return: The contents of this CustomConditions.
        :rtype: list[str]
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        """Sets the contents of this CustomConditions.

        条件匹配的内容

        :param contents: The contents of this CustomConditions.
        :type: list[str]
        """
        self._contents = contents

    @property
    def value_list_id(self):
        """Gets the value_list_id of this CustomConditions.

        引用表的id

        :return: The value_list_id of this CustomConditions.
        :rtype: str
        """
        return self._value_list_id

    @value_list_id.setter
    def value_list_id(self, value_list_id):
        """Sets the value_list_id of this CustomConditions.

        引用表的id

        :param value_list_id: The value_list_id of this CustomConditions.
        :type: str
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
        import simplejson as json
        return json.dumps(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CustomConditions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
