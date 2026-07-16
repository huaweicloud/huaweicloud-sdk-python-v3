# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoreToolsTag:

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
        r"""CoreToolsTag

        The model defined in huaweicloud sdk

        :param key: **参数解释：** 标签键。 **约束限制：** 不能为空，且单个资源标签键不能重复。 **取值范围：** 符合规则^((?!\\s)(?!_sys_)[\\p{L}\\p{Z}\\p{N}_.:/&#x3D;+\\-@]*)(?&lt;!\\s)$，即可以包含任意语种的字母、数字和空格，以及_.:&#x3D;+-@字符，但首尾不能包含空格，且不能以_sys_开头，且长度在1到128之间。 **默认取值：** 不涉及。
        :type key: str
        :param value: **参数解释：** 标签值。 **约束限制：** 不涉及。 **取值范围：** 符合规则^([\\p{L}\\p{Z}\\p{N}_.:/&#x3D;+\\-@]*)$，即可以包含任意语种的字母、数字和空格，以及_.:/&#x3D;+-@字符，且长度不能超过255个字符。 **默认取值：** 不涉及
        :type value: str
        """
        
        

        self._key = None
        self._value = None
        self.discriminator = None

        self.key = key
        self.value = value

    @property
    def key(self):
        r"""Gets the key of this CoreToolsTag.

        **参数解释：** 标签键。 **约束限制：** 不能为空，且单个资源标签键不能重复。 **取值范围：** 符合规则^((?!\\s)(?!_sys_)[\\p{L}\\p{Z}\\p{N}_.:/=+\\-@]*)(?<!\\s)$，即可以包含任意语种的字母、数字和空格，以及_.:=+-@字符，但首尾不能包含空格，且不能以_sys_开头，且长度在1到128之间。 **默认取值：** 不涉及。

        :return: The key of this CoreToolsTag.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this CoreToolsTag.

        **参数解释：** 标签键。 **约束限制：** 不能为空，且单个资源标签键不能重复。 **取值范围：** 符合规则^((?!\\s)(?!_sys_)[\\p{L}\\p{Z}\\p{N}_.:/=+\\-@]*)(?<!\\s)$，即可以包含任意语种的字母、数字和空格，以及_.:=+-@字符，但首尾不能包含空格，且不能以_sys_开头，且长度在1到128之间。 **默认取值：** 不涉及。

        :param key: The key of this CoreToolsTag.
        :type key: str
        """
        self._key = key

    @property
    def value(self):
        r"""Gets the value of this CoreToolsTag.

        **参数解释：** 标签值。 **约束限制：** 不涉及。 **取值范围：** 符合规则^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-@]*)$，即可以包含任意语种的字母、数字和空格，以及_.:/=+-@字符，且长度不能超过255个字符。 **默认取值：** 不涉及

        :return: The value of this CoreToolsTag.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this CoreToolsTag.

        **参数解释：** 标签值。 **约束限制：** 不涉及。 **取值范围：** 符合规则^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-@]*)$，即可以包含任意语种的字母、数字和空格，以及_.:/=+-@字符，且长度不能超过255个字符。 **默认取值：** 不涉及

        :param value: The value of this CoreToolsTag.
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
        if not isinstance(other, CoreToolsTag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
