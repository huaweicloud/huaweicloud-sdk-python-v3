# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EvaluationOpsTurn:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'turn_id': 'str',
        'fields': 'list[EvaluationOpsTurnField]'
    }

    attribute_map = {
        'turn_id': 'turn_id',
        'fields': 'fields'
    }

    def __init__(self, turn_id=None, fields=None):
        r"""EvaluationOpsTurn

        The model defined in huaweicloud sdk

        :param turn_id: **参数解释：** 单轮对话的唯一标识符（UUID）。 **约束限制：** 1-64个字符。 **取值范围：** 符合通用唯一识别码(UUID)标准的字符串。 **默认取值：** 不涉及。 
        :type turn_id: str
        :param fields: **参数解释：** 当前对话轮次中的具体数据字段列表（如角色、内容等）。 **约束限制：** 包含0-10个字段项。 **取值范围：** 参考EvaluationOpsTurnField。 **默认取值：** 不涉及。 
        :type fields: list[:class:`huaweicloudsdkagentarts.v1.EvaluationOpsTurnField`]
        """
        
        

        self._turn_id = None
        self._fields = None
        self.discriminator = None

        if turn_id is not None:
            self.turn_id = turn_id
        if fields is not None:
            self.fields = fields

    @property
    def turn_id(self):
        r"""Gets the turn_id of this EvaluationOpsTurn.

        **参数解释：** 单轮对话的唯一标识符（UUID）。 **约束限制：** 1-64个字符。 **取值范围：** 符合通用唯一识别码(UUID)标准的字符串。 **默认取值：** 不涉及。 

        :return: The turn_id of this EvaluationOpsTurn.
        :rtype: str
        """
        return self._turn_id

    @turn_id.setter
    def turn_id(self, turn_id):
        r"""Sets the turn_id of this EvaluationOpsTurn.

        **参数解释：** 单轮对话的唯一标识符（UUID）。 **约束限制：** 1-64个字符。 **取值范围：** 符合通用唯一识别码(UUID)标准的字符串。 **默认取值：** 不涉及。 

        :param turn_id: The turn_id of this EvaluationOpsTurn.
        :type turn_id: str
        """
        self._turn_id = turn_id

    @property
    def fields(self):
        r"""Gets the fields of this EvaluationOpsTurn.

        **参数解释：** 当前对话轮次中的具体数据字段列表（如角色、内容等）。 **约束限制：** 包含0-10个字段项。 **取值范围：** 参考EvaluationOpsTurnField。 **默认取值：** 不涉及。 

        :return: The fields of this EvaluationOpsTurn.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.EvaluationOpsTurnField`]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        r"""Sets the fields of this EvaluationOpsTurn.

        **参数解释：** 当前对话轮次中的具体数据字段列表（如角色、内容等）。 **约束限制：** 包含0-10个字段项。 **取值范围：** 参考EvaluationOpsTurnField。 **默认取值：** 不涉及。 

        :param fields: The fields of this EvaluationOpsTurn.
        :type fields: list[:class:`huaweicloudsdkagentarts.v1.EvaluationOpsTurnField`]
        """
        self._fields = fields

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
        if not isinstance(other, EvaluationOpsTurn):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
