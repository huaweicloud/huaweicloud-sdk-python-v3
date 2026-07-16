# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServiceCreateRequestTags:

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
        r"""ServiceCreateRequestTags

        The model defined in huaweicloud sdk

        :param key: **参数解释：** 标签键字段。 **约束限制：** 不涉及。 **取值范围：** 长度为1~128，标签的键可以包含任意语种字母、数字、空格，以及_ . : &#x3D; + - @特殊字符，但首尾不能含有空格，不能以_sys_开头。 **默认取值：** 不涉及。
        :type key: str
        :param value: **参数解释：** 标签value值。 **约束限制：** 最大长度为256。 **取值范围：** 任意数量的字母、数字、空格、下划线、点、冒号、斜杠、等号、加号、减号、@等字符开始和结束的字符串。 **默认取值：** 不涉及。
        :type value: str
        """
        
        

        self._key = None
        self._value = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if value is not None:
            self.value = value

    @property
    def key(self):
        r"""Gets the key of this ServiceCreateRequestTags.

        **参数解释：** 标签键字段。 **约束限制：** 不涉及。 **取值范围：** 长度为1~128，标签的键可以包含任意语种字母、数字、空格，以及_ . : = + - @特殊字符，但首尾不能含有空格，不能以_sys_开头。 **默认取值：** 不涉及。

        :return: The key of this ServiceCreateRequestTags.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this ServiceCreateRequestTags.

        **参数解释：** 标签键字段。 **约束限制：** 不涉及。 **取值范围：** 长度为1~128，标签的键可以包含任意语种字母、数字、空格，以及_ . : = + - @特殊字符，但首尾不能含有空格，不能以_sys_开头。 **默认取值：** 不涉及。

        :param key: The key of this ServiceCreateRequestTags.
        :type key: str
        """
        self._key = key

    @property
    def value(self):
        r"""Gets the value of this ServiceCreateRequestTags.

        **参数解释：** 标签value值。 **约束限制：** 最大长度为256。 **取值范围：** 任意数量的字母、数字、空格、下划线、点、冒号、斜杠、等号、加号、减号、@等字符开始和结束的字符串。 **默认取值：** 不涉及。

        :return: The value of this ServiceCreateRequestTags.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this ServiceCreateRequestTags.

        **参数解释：** 标签value值。 **约束限制：** 最大长度为256。 **取值范围：** 任意数量的字母、数字、空格、下划线、点、冒号、斜杠、等号、加号、减号、@等字符开始和结束的字符串。 **默认取值：** 不涉及。

        :param value: The value of this ServiceCreateRequestTags.
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
        if not isinstance(other, ServiceCreateRequestTags):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
