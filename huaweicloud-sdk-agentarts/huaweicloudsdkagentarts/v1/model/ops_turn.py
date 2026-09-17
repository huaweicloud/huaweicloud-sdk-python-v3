# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsTurn:

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
        'fields': 'dict(str, OpsFieldValue)'
    }

    attribute_map = {
        'turn_id': 'turn_id',
        'fields': 'fields'
    }

    def __init__(self, turn_id=None, fields=None):
        r"""OpsTurn

        The model defined in huaweicloud sdk

        :param turn_id: **参数解释：** 轮次的唯一标识符。 **约束限制：** 不涉及。 **取值范围：** 不涉及。
        :type turn_id: str
        :param fields: **参数解释：** 该轮次中具体字段的键值对集合。 **取值范围：** Map 结构，Value 参考OpsFieldValue定义。
        :type fields: dict(str, OpsFieldValue)
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
        r"""Gets the turn_id of this OpsTurn.

        **参数解释：** 轮次的唯一标识符。 **约束限制：** 不涉及。 **取值范围：** 不涉及。

        :return: The turn_id of this OpsTurn.
        :rtype: str
        """
        return self._turn_id

    @turn_id.setter
    def turn_id(self, turn_id):
        r"""Sets the turn_id of this OpsTurn.

        **参数解释：** 轮次的唯一标识符。 **约束限制：** 不涉及。 **取值范围：** 不涉及。

        :param turn_id: The turn_id of this OpsTurn.
        :type turn_id: str
        """
        self._turn_id = turn_id

    @property
    def fields(self):
        r"""Gets the fields of this OpsTurn.

        **参数解释：** 该轮次中具体字段的键值对集合。 **取值范围：** Map 结构，Value 参考OpsFieldValue定义。

        :return: The fields of this OpsTurn.
        :rtype: dict(str, OpsFieldValue)
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        r"""Sets the fields of this OpsTurn.

        **参数解释：** 该轮次中具体字段的键值对集合。 **取值范围：** Map 结构，Value 参考OpsFieldValue定义。

        :param fields: The fields of this OpsTurn.
        :type fields: dict(str, OpsFieldValue)
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
        if not isinstance(other, OpsTurn):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
