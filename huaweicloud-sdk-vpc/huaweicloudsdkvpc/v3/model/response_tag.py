# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResponseTag:

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
        r"""ResponseTag

        The model defined in huaweicloud sdk

        :param key: **参数解释**： 标签键。 **取值范围**：   - 最大长度128个unicode字符， key不能为空。   - 同一资源的key不能重复。   - 可以包含的字符范围：  - 英文字母     - 数字     - 特殊字符：下划线（_）、点（.）、冒号（:）、加号（+）、中划线（-）、等号（&#x3D;）     - 中文字符
        :type key: str
        :param value: **参数解释**： 标签值。 **取值范围**：   - 每个值最大长度255个unicode字符，value可以为空。   - 可以包含的字符范围：  - 英文字母     - 数字     - 特殊字符：下划线（_）、点（.）、冒号（:）、加号（+）、中划线（-）、等号（&#x3D;）     - 中文字符
        :type value: str
        """
        
        

        self._key = None
        self._value = None
        self.discriminator = None

        self.key = key
        self.value = value

    @property
    def key(self):
        r"""Gets the key of this ResponseTag.

        **参数解释**： 标签键。 **取值范围**：   - 最大长度128个unicode字符， key不能为空。   - 同一资源的key不能重复。   - 可以包含的字符范围：  - 英文字母     - 数字     - 特殊字符：下划线（_）、点（.）、冒号（:）、加号（+）、中划线（-）、等号（=）     - 中文字符

        :return: The key of this ResponseTag.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this ResponseTag.

        **参数解释**： 标签键。 **取值范围**：   - 最大长度128个unicode字符， key不能为空。   - 同一资源的key不能重复。   - 可以包含的字符范围：  - 英文字母     - 数字     - 特殊字符：下划线（_）、点（.）、冒号（:）、加号（+）、中划线（-）、等号（=）     - 中文字符

        :param key: The key of this ResponseTag.
        :type key: str
        """
        self._key = key

    @property
    def value(self):
        r"""Gets the value of this ResponseTag.

        **参数解释**： 标签值。 **取值范围**：   - 每个值最大长度255个unicode字符，value可以为空。   - 可以包含的字符范围：  - 英文字母     - 数字     - 特殊字符：下划线（_）、点（.）、冒号（:）、加号（+）、中划线（-）、等号（=）     - 中文字符

        :return: The value of this ResponseTag.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this ResponseTag.

        **参数解释**： 标签值。 **取值范围**：   - 每个值最大长度255个unicode字符，value可以为空。   - 可以包含的字符范围：  - 英文字母     - 数字     - 特殊字符：下划线（_）、点（.）、冒号（:）、加号（+）、中划线（-）、等号（=）     - 中文字符

        :param value: The value of this ResponseTag.
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
        if not isinstance(other, ResponseTag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
