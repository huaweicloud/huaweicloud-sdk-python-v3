# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SysconfigInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'font_family': 'str',
        'font_size': 'str',
        'line_height': 'str'
    }

    attribute_map = {
        'font_family': 'font_family',
        'font_size': 'font_size',
        'line_height': 'line_height'
    }

    def __init__(self, font_family=None, font_size=None, line_height=None):
        r"""SysconfigInfo

        The model defined in huaweicloud sdk

        :param font_family: **参数解释**： 默认字体。 **约束限制**： 不涉及。 **取值范围**： [1-32]个字符。 **默认取值**： 不涉及。
        :type font_family: str
        :param font_size: **参数解释**： 字体大小。 **约束限制**： 不涉及。 **取值范围**： [1-10]个字符。 **默认取值**： 不涉及。
        :type font_size: str
        :param line_height: **参数解释**： 行间距。 **约束限制**： 不涉及。 **取值范围**： [1-10]个字符。 **默认取值**： 不涉及。
        :type line_height: str
        """
        
        

        self._font_family = None
        self._font_size = None
        self._line_height = None
        self.discriminator = None

        if font_family is not None:
            self.font_family = font_family
        if font_size is not None:
            self.font_size = font_size
        if line_height is not None:
            self.line_height = line_height

    @property
    def font_family(self):
        r"""Gets the font_family of this SysconfigInfo.

        **参数解释**： 默认字体。 **约束限制**： 不涉及。 **取值范围**： [1-32]个字符。 **默认取值**： 不涉及。

        :return: The font_family of this SysconfigInfo.
        :rtype: str
        """
        return self._font_family

    @font_family.setter
    def font_family(self, font_family):
        r"""Sets the font_family of this SysconfigInfo.

        **参数解释**： 默认字体。 **约束限制**： 不涉及。 **取值范围**： [1-32]个字符。 **默认取值**： 不涉及。

        :param font_family: The font_family of this SysconfigInfo.
        :type font_family: str
        """
        self._font_family = font_family

    @property
    def font_size(self):
        r"""Gets the font_size of this SysconfigInfo.

        **参数解释**： 字体大小。 **约束限制**： 不涉及。 **取值范围**： [1-10]个字符。 **默认取值**： 不涉及。

        :return: The font_size of this SysconfigInfo.
        :rtype: str
        """
        return self._font_size

    @font_size.setter
    def font_size(self, font_size):
        r"""Sets the font_size of this SysconfigInfo.

        **参数解释**： 字体大小。 **约束限制**： 不涉及。 **取值范围**： [1-10]个字符。 **默认取值**： 不涉及。

        :param font_size: The font_size of this SysconfigInfo.
        :type font_size: str
        """
        self._font_size = font_size

    @property
    def line_height(self):
        r"""Gets the line_height of this SysconfigInfo.

        **参数解释**： 行间距。 **约束限制**： 不涉及。 **取值范围**： [1-10]个字符。 **默认取值**： 不涉及。

        :return: The line_height of this SysconfigInfo.
        :rtype: str
        """
        return self._line_height

    @line_height.setter
    def line_height(self, line_height):
        r"""Sets the line_height of this SysconfigInfo.

        **参数解释**： 行间距。 **约束限制**： 不涉及。 **取值范围**： [1-10]个字符。 **默认取值**： 不涉及。

        :param line_height: The line_height of this SysconfigInfo.
        :type line_height: str
        """
        self._line_height = line_height

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
        if not isinstance(other, SysconfigInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
