# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomizeResourceTag:

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
        r"""CustomizeResourceTag

        The model defined in huaweicloud sdk

        :param key: **参数解释：** Key值。 **约束限制：** 不涉及 **取值范围：** - 不能为空且首尾不能包含空格，最多支持128个字符 - 可用UTF-8格式表示的任意语种字母、数字和空格 - 支持部分特殊字符：_.:&#x3D;+-@ - 不能以\&quot;\\_sys\\_\&quot;开头  **默认取值：** 不涉及 
        :type key: str
        :param values: **参数解释：** Value值列表。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及 
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
        r"""Gets the key of this CustomizeResourceTag.

        **参数解释：** Key值。 **约束限制：** 不涉及 **取值范围：** - 不能为空且首尾不能包含空格，最多支持128个字符 - 可用UTF-8格式表示的任意语种字母、数字和空格 - 支持部分特殊字符：_.:=+-@ - 不能以\"\\_sys\\_\"开头  **默认取值：** 不涉及 

        :return: The key of this CustomizeResourceTag.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this CustomizeResourceTag.

        **参数解释：** Key值。 **约束限制：** 不涉及 **取值范围：** - 不能为空且首尾不能包含空格，最多支持128个字符 - 可用UTF-8格式表示的任意语种字母、数字和空格 - 支持部分特殊字符：_.:=+-@ - 不能以\"\\_sys\\_\"开头  **默认取值：** 不涉及 

        :param key: The key of this CustomizeResourceTag.
        :type key: str
        """
        self._key = key

    @property
    def values(self):
        r"""Gets the values of this CustomizeResourceTag.

        **参数解释：** Value值列表。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及 

        :return: The values of this CustomizeResourceTag.
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        r"""Sets the values of this CustomizeResourceTag.

        **参数解释：** Value值列表。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及 

        :param values: The values of this CustomizeResourceTag.
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
        if not isinstance(other, CustomizeResourceTag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
