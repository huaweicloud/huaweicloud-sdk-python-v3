# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EvaluationOpsSynthesisItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'turns': 'list[EvaluationOpsTurn]',
        'created_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'turns': 'turns',
        'created_at': 'created_at'
    }

    def __init__(self, id=None, turns=None, created_at=None):
        r"""EvaluationOpsSynthesisItem

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 合成条目的唯一标识符。在存储层对应MongoDB的ObjectID。 **约束限制：** 1-64个字符。 **取值范围：** 标准的ObjectID字符串格式。 **默认取值：** 不涉及。 
        :type id: str
        :param turns: **参数解释：** 条目对应的多轮对话或交互序列。 **约束限制：** 包含0-10个对话轮次。 **取值范围：** 参考EvaluationOpsTurn。 **默认取值：** 不涉及。 
        :type turns: list[:class:`huaweicloudsdkagentarts.v1.EvaluationOpsTurn`]
        :param created_at: **参数解释：** 该合成条目生成的精确时间戳。 **约束限制：** 符合ISO8601标准。 **取值范围：** 日期时间字符串。 **默认取值：** 不涉及。 
        :type created_at: datetime
        """
        
        

        self._id = None
        self._turns = None
        self._created_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if turns is not None:
            self.turns = turns
        if created_at is not None:
            self.created_at = created_at

    @property
    def id(self):
        r"""Gets the id of this EvaluationOpsSynthesisItem.

        **参数解释：** 合成条目的唯一标识符。在存储层对应MongoDB的ObjectID。 **约束限制：** 1-64个字符。 **取值范围：** 标准的ObjectID字符串格式。 **默认取值：** 不涉及。 

        :return: The id of this EvaluationOpsSynthesisItem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this EvaluationOpsSynthesisItem.

        **参数解释：** 合成条目的唯一标识符。在存储层对应MongoDB的ObjectID。 **约束限制：** 1-64个字符。 **取值范围：** 标准的ObjectID字符串格式。 **默认取值：** 不涉及。 

        :param id: The id of this EvaluationOpsSynthesisItem.
        :type id: str
        """
        self._id = id

    @property
    def turns(self):
        r"""Gets the turns of this EvaluationOpsSynthesisItem.

        **参数解释：** 条目对应的多轮对话或交互序列。 **约束限制：** 包含0-10个对话轮次。 **取值范围：** 参考EvaluationOpsTurn。 **默认取值：** 不涉及。 

        :return: The turns of this EvaluationOpsSynthesisItem.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.EvaluationOpsTurn`]
        """
        return self._turns

    @turns.setter
    def turns(self, turns):
        r"""Sets the turns of this EvaluationOpsSynthesisItem.

        **参数解释：** 条目对应的多轮对话或交互序列。 **约束限制：** 包含0-10个对话轮次。 **取值范围：** 参考EvaluationOpsTurn。 **默认取值：** 不涉及。 

        :param turns: The turns of this EvaluationOpsSynthesisItem.
        :type turns: list[:class:`huaweicloudsdkagentarts.v1.EvaluationOpsTurn`]
        """
        self._turns = turns

    @property
    def created_at(self):
        r"""Gets the created_at of this EvaluationOpsSynthesisItem.

        **参数解释：** 该合成条目生成的精确时间戳。 **约束限制：** 符合ISO8601标准。 **取值范围：** 日期时间字符串。 **默认取值：** 不涉及。 

        :return: The created_at of this EvaluationOpsSynthesisItem.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this EvaluationOpsSynthesisItem.

        **参数解释：** 该合成条目生成的精确时间戳。 **约束限制：** 符合ISO8601标准。 **取值范围：** 日期时间字符串。 **默认取值：** 不涉及。 

        :param created_at: The created_at of this EvaluationOpsSynthesisItem.
        :type created_at: datetime
        """
        self._created_at = created_at

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
        if not isinstance(other, EvaluationOpsSynthesisItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
