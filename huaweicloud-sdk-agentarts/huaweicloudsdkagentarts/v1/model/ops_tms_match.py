# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsTmsMatch:

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
        r"""OpsTmsMatch

        The model defined in huaweicloud sdk

        :param key: **参数解释：** 匹配字段名。支持以下值： - resource_name：按资源名称前缀模糊匹配（LIKE value%）。value为空字符串时精确匹配空串（多数资源名称非空，返回空列表）。 - resource_id：按资源ID精确匹配。value为空字符串时返回空列表。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type key: str
        :param value: **参数解释：** 匹配值。resource_name使用前缀模糊匹配，resource_id使用精确匹配。 **约束限制：** 不涉及。 **取值范围：** 长度0~255个字符。 **默认取值：** 不涉及。
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
        r"""Gets the key of this OpsTmsMatch.

        **参数解释：** 匹配字段名。支持以下值： - resource_name：按资源名称前缀模糊匹配（LIKE value%）。value为空字符串时精确匹配空串（多数资源名称非空，返回空列表）。 - resource_id：按资源ID精确匹配。value为空字符串时返回空列表。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The key of this OpsTmsMatch.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this OpsTmsMatch.

        **参数解释：** 匹配字段名。支持以下值： - resource_name：按资源名称前缀模糊匹配（LIKE value%）。value为空字符串时精确匹配空串（多数资源名称非空，返回空列表）。 - resource_id：按资源ID精确匹配。value为空字符串时返回空列表。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param key: The key of this OpsTmsMatch.
        :type key: str
        """
        self._key = key

    @property
    def value(self):
        r"""Gets the value of this OpsTmsMatch.

        **参数解释：** 匹配值。resource_name使用前缀模糊匹配，resource_id使用精确匹配。 **约束限制：** 不涉及。 **取值范围：** 长度0~255个字符。 **默认取值：** 不涉及。

        :return: The value of this OpsTmsMatch.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this OpsTmsMatch.

        **参数解释：** 匹配值。resource_name使用前缀模糊匹配，resource_id使用精确匹配。 **约束限制：** 不涉及。 **取值范围：** 长度0~255个字符。 **默认取值：** 不涉及。

        :param value: The value of this OpsTmsMatch.
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
        if not isinstance(other, OpsTmsMatch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
