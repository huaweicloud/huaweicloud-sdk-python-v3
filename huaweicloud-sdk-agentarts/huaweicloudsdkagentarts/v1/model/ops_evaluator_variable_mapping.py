# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsEvaluatorVariableMapping:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source': 'str',
        'field_name': 'str'
    }

    attribute_map = {
        'source': 'source',
        'field_name': 'field_name'
    }

    def __init__(self, source=None, field_name=None):
        r"""OpsEvaluatorVariableMapping

        The model defined in huaweicloud sdk

        :param source: **参数解释：** 指定评估器变量的数据来源。 **约束限制：** 1到36字符。 **取值范围：** dataset, agent_output。 **默认取值：** 不涉及。 
        :type source: str
        :param field_name: **参数解释：** 数据源对应的具体字段名。 **约束限制：** 1到200字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 
        :type field_name: str
        """
        
        

        self._source = None
        self._field_name = None
        self.discriminator = None

        self.source = source
        if field_name is not None:
            self.field_name = field_name

    @property
    def source(self):
        r"""Gets the source of this OpsEvaluatorVariableMapping.

        **参数解释：** 指定评估器变量的数据来源。 **约束限制：** 1到36字符。 **取值范围：** dataset, agent_output。 **默认取值：** 不涉及。 

        :return: The source of this OpsEvaluatorVariableMapping.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this OpsEvaluatorVariableMapping.

        **参数解释：** 指定评估器变量的数据来源。 **约束限制：** 1到36字符。 **取值范围：** dataset, agent_output。 **默认取值：** 不涉及。 

        :param source: The source of this OpsEvaluatorVariableMapping.
        :type source: str
        """
        self._source = source

    @property
    def field_name(self):
        r"""Gets the field_name of this OpsEvaluatorVariableMapping.

        **参数解释：** 数据源对应的具体字段名。 **约束限制：** 1到200字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :return: The field_name of this OpsEvaluatorVariableMapping.
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        r"""Sets the field_name of this OpsEvaluatorVariableMapping.

        **参数解释：** 数据源对应的具体字段名。 **约束限制：** 1到200字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :param field_name: The field_name of this OpsEvaluatorVariableMapping.
        :type field_name: str
        """
        self._field_name = field_name

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
        if not isinstance(other, OpsEvaluatorVariableMapping):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
