# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsTasksTagForTMS:

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
        r"""OpsTasksTagForTMS

        The model defined in huaweicloud sdk

        :param key: **参数解释：** 标签键，标识资源的分类维度。  **约束限制：** 不能为空或者空字符串，不能为空格，校验和使用之前先trim前后半角空格。最大长度128个unicode字符。  **取值范围：** 最大长度128个unicode字符。  **默认取值：** 无
        :type key: str
        :param value: **参数解释：** 标签值，具体的分类值。  **约束限制：** 不校验字符集范围。  **取值范围：** 不校验字符集范围。每个值最大长度255个unicode字符。  **默认取值：** 无
        :type value: str
        """
        
        

        self._key = None
        self._value = None
        self.discriminator = None

        self.key = key
        self.value = value

    @property
    def key(self):
        r"""Gets the key of this OpsTasksTagForTMS.

        **参数解释：** 标签键，标识资源的分类维度。  **约束限制：** 不能为空或者空字符串，不能为空格，校验和使用之前先trim前后半角空格。最大长度128个unicode字符。  **取值范围：** 最大长度128个unicode字符。  **默认取值：** 无

        :return: The key of this OpsTasksTagForTMS.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this OpsTasksTagForTMS.

        **参数解释：** 标签键，标识资源的分类维度。  **约束限制：** 不能为空或者空字符串，不能为空格，校验和使用之前先trim前后半角空格。最大长度128个unicode字符。  **取值范围：** 最大长度128个unicode字符。  **默认取值：** 无

        :param key: The key of this OpsTasksTagForTMS.
        :type key: str
        """
        self._key = key

    @property
    def value(self):
        r"""Gets the value of this OpsTasksTagForTMS.

        **参数解释：** 标签值，具体的分类值。  **约束限制：** 不校验字符集范围。  **取值范围：** 不校验字符集范围。每个值最大长度255个unicode字符。  **默认取值：** 无

        :return: The value of this OpsTasksTagForTMS.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this OpsTasksTagForTMS.

        **参数解释：** 标签值，具体的分类值。  **约束限制：** 不校验字符集范围。  **取值范围：** 不校验字符集范围。每个值最大长度255个unicode字符。  **默认取值：** 无

        :param value: The value of this OpsTasksTagForTMS.
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
        if not isinstance(other, OpsTasksTagForTMS):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
