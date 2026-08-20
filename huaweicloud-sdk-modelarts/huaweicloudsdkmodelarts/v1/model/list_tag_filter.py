# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTagFilter:

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
        'values': 'list[str]'
    }

    attribute_map = {
        'key': 'key',
        'values': 'values'
    }

    def __init__(self, key=None, values=None):
        r"""ListTagFilter

        The model defined in huaweicloud sdk

        :param key: **参数解释**：标签键。 **约束限制**：   - 必填；   - 长度 1~128；   - 首尾不可为空格；   - 仅支持字母、数字、空格及 &#x60;_ . : &#x3D; + - @&#x60;。 **取值范围**：符合标签键命名规范的字符串。 **默认取值**：不涉及。
        :type key: str
        :param values: **参数解释**：标签值列表，与 &#x60;key&#x60; 组合用于筛选作业。 **约束限制**：   - 非必填；   - 最多 10 个值；   - 单个值长度 0~255；   - 仅支持字母、数字、空格及 &#x60;_ . : / &#x3D; + - @&#x60;。 **取值范围**：   - 传具体值：匹配 &#x60;key&#x3D;value&#x60; 的作业；   - 不传、传空数组或空字符串：匹配带有该 &#x60;key&#x60; 的作业（不限 value）。 **默认取值**：不涉及。
        :type values: list[str]
        """
        
        

        self._key = None
        self._values = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if values is not None:
            self.values = values

    @property
    def key(self):
        r"""Gets the key of this ListTagFilter.

        **参数解释**：标签键。 **约束限制**：   - 必填；   - 长度 1~128；   - 首尾不可为空格；   - 仅支持字母、数字、空格及 `_ . : = + - @`。 **取值范围**：符合标签键命名规范的字符串。 **默认取值**：不涉及。

        :return: The key of this ListTagFilter.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this ListTagFilter.

        **参数解释**：标签键。 **约束限制**：   - 必填；   - 长度 1~128；   - 首尾不可为空格；   - 仅支持字母、数字、空格及 `_ . : = + - @`。 **取值范围**：符合标签键命名规范的字符串。 **默认取值**：不涉及。

        :param key: The key of this ListTagFilter.
        :type key: str
        """
        self._key = key

    @property
    def values(self):
        r"""Gets the values of this ListTagFilter.

        **参数解释**：标签值列表，与 `key` 组合用于筛选作业。 **约束限制**：   - 非必填；   - 最多 10 个值；   - 单个值长度 0~255；   - 仅支持字母、数字、空格及 `_ . : / = + - @`。 **取值范围**：   - 传具体值：匹配 `key=value` 的作业；   - 不传、传空数组或空字符串：匹配带有该 `key` 的作业（不限 value）。 **默认取值**：不涉及。

        :return: The values of this ListTagFilter.
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        r"""Sets the values of this ListTagFilter.

        **参数解释**：标签值列表，与 `key` 组合用于筛选作业。 **约束限制**：   - 非必填；   - 最多 10 个值；   - 单个值长度 0~255；   - 仅支持字母、数字、空格及 `_ . : / = + - @`。 **取值范围**：   - 传具体值：匹配 `key=value` 的作业；   - 不传、传空数组或空字符串：匹配带有该 `key` 的作业（不限 value）。 **默认取值**：不涉及。

        :param values: The values of this ListTagFilter.
        :type values: list[str]
        """
        self._values = values

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
        if not isinstance(other, ListTagFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
