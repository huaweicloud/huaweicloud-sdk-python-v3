# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsTurnInput:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'fields': 'list[OpsFieldValueInput]'
    }

    attribute_map = {
        'fields': 'fields'
    }

    def __init__(self, fields=None):
        r"""OpsTurnInput

        The model defined in huaweicloud sdk

        :param fields: **参数解释：** 当前轮次中包含的具体数据字段（如Input、Output、Rationale 等）集合。 **约束限制：** 包含0到10000个字段项。 **取值范围：** 参考OpsFieldValueInput定义。 **默认取值：** 不涉及。 
        :type fields: list[:class:`huaweicloudsdkagentarts.v1.OpsFieldValueInput`]
        """
        
        

        self._fields = None
        self.discriminator = None

        self.fields = fields

    @property
    def fields(self):
        r"""Gets the fields of this OpsTurnInput.

        **参数解释：** 当前轮次中包含的具体数据字段（如Input、Output、Rationale 等）集合。 **约束限制：** 包含0到10000个字段项。 **取值范围：** 参考OpsFieldValueInput定义。 **默认取值：** 不涉及。 

        :return: The fields of this OpsTurnInput.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.OpsFieldValueInput`]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        r"""Sets the fields of this OpsTurnInput.

        **参数解释：** 当前轮次中包含的具体数据字段（如Input、Output、Rationale 等）集合。 **约束限制：** 包含0到10000个字段项。 **取值范围：** 参考OpsFieldValueInput定义。 **默认取值：** 不涉及。 

        :param fields: The fields of this OpsTurnInput.
        :type fields: list[:class:`huaweicloudsdkagentarts.v1.OpsFieldValueInput`]
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
        if not isinstance(other, OpsTurnInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
