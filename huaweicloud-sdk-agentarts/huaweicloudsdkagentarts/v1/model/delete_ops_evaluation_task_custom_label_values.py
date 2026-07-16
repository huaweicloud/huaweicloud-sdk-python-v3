# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteOpsEvaluationTaskCustomLabelValues:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'item_id': 'str',
        'tag_id': 'str'
    }

    attribute_map = {
        'item_id': 'item_id',
        'tag_id': 'tag_id'
    }

    def __init__(self, item_id=None, tag_id=None):
        r"""DeleteOpsEvaluationTaskCustomLabelValues

        The model defined in huaweicloud sdk

        :param item_id: **参数解释：** 评测集条目的唯一标识符（ID）。 **约束限制：** 字符串长度为0到100个字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 
        :type item_id: str
        :param tag_id: **参数解释：** 标签的唯一标识符（ID）。 **约束限制：** 字符串长度为0到100个字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 
        :type tag_id: str
        """
        
        

        self._item_id = None
        self._tag_id = None
        self.discriminator = None

        self.item_id = item_id
        self.tag_id = tag_id

    @property
    def item_id(self):
        r"""Gets the item_id of this DeleteOpsEvaluationTaskCustomLabelValues.

        **参数解释：** 评测集条目的唯一标识符（ID）。 **约束限制：** 字符串长度为0到100个字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :return: The item_id of this DeleteOpsEvaluationTaskCustomLabelValues.
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        r"""Sets the item_id of this DeleteOpsEvaluationTaskCustomLabelValues.

        **参数解释：** 评测集条目的唯一标识符（ID）。 **约束限制：** 字符串长度为0到100个字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :param item_id: The item_id of this DeleteOpsEvaluationTaskCustomLabelValues.
        :type item_id: str
        """
        self._item_id = item_id

    @property
    def tag_id(self):
        r"""Gets the tag_id of this DeleteOpsEvaluationTaskCustomLabelValues.

        **参数解释：** 标签的唯一标识符（ID）。 **约束限制：** 字符串长度为0到100个字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :return: The tag_id of this DeleteOpsEvaluationTaskCustomLabelValues.
        :rtype: str
        """
        return self._tag_id

    @tag_id.setter
    def tag_id(self, tag_id):
        r"""Sets the tag_id of this DeleteOpsEvaluationTaskCustomLabelValues.

        **参数解释：** 标签的唯一标识符（ID）。 **约束限制：** 字符串长度为0到100个字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :param tag_id: The tag_id of this DeleteOpsEvaluationTaskCustomLabelValues.
        :type tag_id: str
        """
        self._tag_id = tag_id

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
        if not isinstance(other, DeleteOpsEvaluationTaskCustomLabelValues):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
