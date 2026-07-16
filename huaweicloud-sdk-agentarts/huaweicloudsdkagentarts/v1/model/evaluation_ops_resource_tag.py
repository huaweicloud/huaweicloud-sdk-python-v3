# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EvaluationOpsResourceTag:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tag_id': 'str',
        'tag_type': 'str'
    }

    attribute_map = {
        'tag_id': 'tag_id',
        'tag_type': 'tag_type'
    }

    def __init__(self, tag_id=None, tag_type=None):
        r"""EvaluationOpsResourceTag

        The model defined in huaweicloud sdk

        :param tag_id: **参数解释：** 标签的键，标识类别。 **约束限制：** 字符串长度为1到256个字符，支持英文、数字、连字符（-）和下划线（_）。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type tag_id: str
        :param tag_type: **参数解释：** 标签的值，存储该标签键对应的具体内容或属性值。 **约束限制：** 字符串长度为1到512个字符，支持中英文、数字及特殊字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type tag_type: str
        """
        
        

        self._tag_id = None
        self._tag_type = None
        self.discriminator = None

        if tag_id is not None:
            self.tag_id = tag_id
        if tag_type is not None:
            self.tag_type = tag_type

    @property
    def tag_id(self):
        r"""Gets the tag_id of this EvaluationOpsResourceTag.

        **参数解释：** 标签的键，标识类别。 **约束限制：** 字符串长度为1到256个字符，支持英文、数字、连字符（-）和下划线（_）。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The tag_id of this EvaluationOpsResourceTag.
        :rtype: str
        """
        return self._tag_id

    @tag_id.setter
    def tag_id(self, tag_id):
        r"""Sets the tag_id of this EvaluationOpsResourceTag.

        **参数解释：** 标签的键，标识类别。 **约束限制：** 字符串长度为1到256个字符，支持英文、数字、连字符（-）和下划线（_）。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param tag_id: The tag_id of this EvaluationOpsResourceTag.
        :type tag_id: str
        """
        self._tag_id = tag_id

    @property
    def tag_type(self):
        r"""Gets the tag_type of this EvaluationOpsResourceTag.

        **参数解释：** 标签的值，存储该标签键对应的具体内容或属性值。 **约束限制：** 字符串长度为1到512个字符，支持中英文、数字及特殊字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The tag_type of this EvaluationOpsResourceTag.
        :rtype: str
        """
        return self._tag_type

    @tag_type.setter
    def tag_type(self, tag_type):
        r"""Sets the tag_type of this EvaluationOpsResourceTag.

        **参数解释：** 标签的值，存储该标签键对应的具体内容或属性值。 **约束限制：** 字符串长度为1到512个字符，支持中英文、数字及特殊字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param tag_type: The tag_type of this EvaluationOpsResourceTag.
        :type tag_type: str
        """
        self._tag_type = tag_type

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
        if not isinstance(other, EvaluationOpsResourceTag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
