# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TagsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'value': 'str'
    }

    attribute_map = {
        'key': 'key',
        'value': 'value'
    }

    def __init__(self, key=None, value=None):
        r"""TagsRequestBody

        The model defined in huaweicloud sdk

        :param key: **参数解释：** 标签键。 **约束限制：** - 标签键名称不可重复。 - 标签是以键值对（key-value）的形式表示，key和value为一一对应关系。 **取值范围：** 标签键可以包含任意语种的字母、数字和空格，以及_.:&#x3D;+-@字符，但首尾不能包含空格，且不能以_sys_开头；长度不能超过128个字符。 **默认取值：** 不涉及。
        :type key: str
        :param value: **参数解释：** 标签值。 **约束限制：** 标签是以键值对（key-value）的形式表示，key和value为一一对应关系。 **取值范围：** - 标签值可以包含任意语种的字母、数字和空格，以及_.:&#x3D;+-@字符。 - 标签值长度不能超过255个字符。 **默认取值：** 不涉及。
        :type value: str
        """
        
        

        self._key = None
        self._value = None
        self.discriminator = None

        self.key = key
        if value is not None:
            self.value = value

    @property
    def key(self):
        r"""Gets the key of this TagsRequestBody.

        **参数解释：** 标签键。 **约束限制：** - 标签键名称不可重复。 - 标签是以键值对（key-value）的形式表示，key和value为一一对应关系。 **取值范围：** 标签键可以包含任意语种的字母、数字和空格，以及_.:=+-@字符，但首尾不能包含空格，且不能以_sys_开头；长度不能超过128个字符。 **默认取值：** 不涉及。

        :return: The key of this TagsRequestBody.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this TagsRequestBody.

        **参数解释：** 标签键。 **约束限制：** - 标签键名称不可重复。 - 标签是以键值对（key-value）的形式表示，key和value为一一对应关系。 **取值范围：** 标签键可以包含任意语种的字母、数字和空格，以及_.:=+-@字符，但首尾不能包含空格，且不能以_sys_开头；长度不能超过128个字符。 **默认取值：** 不涉及。

        :param key: The key of this TagsRequestBody.
        :type key: str
        """
        self._key = key

    @property
    def value(self):
        r"""Gets the value of this TagsRequestBody.

        **参数解释：** 标签值。 **约束限制：** 标签是以键值对（key-value）的形式表示，key和value为一一对应关系。 **取值范围：** - 标签值可以包含任意语种的字母、数字和空格，以及_.:=+-@字符。 - 标签值长度不能超过255个字符。 **默认取值：** 不涉及。

        :return: The value of this TagsRequestBody.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this TagsRequestBody.

        **参数解释：** 标签值。 **约束限制：** 标签是以键值对（key-value）的形式表示，key和value为一一对应关系。 **取值范围：** - 标签值可以包含任意语种的字母、数字和空格，以及_.:=+-@字符。 - 标签值长度不能超过255个字符。 **默认取值：** 不涉及。

        :param value: The value of this TagsRequestBody.
        :type value: str
        """
        self._value = value

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
        if not isinstance(other, TagsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
