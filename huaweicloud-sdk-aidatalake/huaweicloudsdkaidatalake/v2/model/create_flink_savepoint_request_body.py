# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateFlinkSavepointRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'format': 'FlinkSavepointFormat',
        'drain_mode_enabled': 'bool'
    }

    attribute_map = {
        'description': 'description',
        'format': 'format',
        'drain_mode_enabled': 'drain_mode_enabled'
    }

    def __init__(self, description=None, format=None, drain_mode_enabled=None):
        r"""CreateFlinkSavepointRequestBody

        The model defined in huaweicloud sdk

        :param description: **参数解释**：作业快照的描述信息。 **约束限制**：不涉及。 **取值范围**：0~512个字符。 **默认取值**：不涉及。 
        :type description: str
        :param format: 
        :type format: :class:`huaweicloudsdkaidatalake.v2.FlinkSavepointFormat`
        :param drain_mode_enabled: **参数解释**：是否启用Drain模式。启用后，触发Savepoint前将先发送Watermark到所有算子以触发窗口计算完成，然后再保存状态快照。 **约束限制**：不涉及。 **取值范围**：   - true：启用Drain模式。   - false：不启用Drain模式。 **默认取值**：false。 
        :type drain_mode_enabled: bool
        """
        
        

        self._description = None
        self._format = None
        self._drain_mode_enabled = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if format is not None:
            self.format = format
        if drain_mode_enabled is not None:
            self.drain_mode_enabled = drain_mode_enabled

    @property
    def description(self):
        r"""Gets the description of this CreateFlinkSavepointRequestBody.

        **参数解释**：作业快照的描述信息。 **约束限制**：不涉及。 **取值范围**：0~512个字符。 **默认取值**：不涉及。 

        :return: The description of this CreateFlinkSavepointRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateFlinkSavepointRequestBody.

        **参数解释**：作业快照的描述信息。 **约束限制**：不涉及。 **取值范围**：0~512个字符。 **默认取值**：不涉及。 

        :param description: The description of this CreateFlinkSavepointRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def format(self):
        r"""Gets the format of this CreateFlinkSavepointRequestBody.

        :return: The format of this CreateFlinkSavepointRequestBody.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.FlinkSavepointFormat`
        """
        return self._format

    @format.setter
    def format(self, format):
        r"""Sets the format of this CreateFlinkSavepointRequestBody.

        :param format: The format of this CreateFlinkSavepointRequestBody.
        :type format: :class:`huaweicloudsdkaidatalake.v2.FlinkSavepointFormat`
        """
        self._format = format

    @property
    def drain_mode_enabled(self):
        r"""Gets the drain_mode_enabled of this CreateFlinkSavepointRequestBody.

        **参数解释**：是否启用Drain模式。启用后，触发Savepoint前将先发送Watermark到所有算子以触发窗口计算完成，然后再保存状态快照。 **约束限制**：不涉及。 **取值范围**：   - true：启用Drain模式。   - false：不启用Drain模式。 **默认取值**：false。 

        :return: The drain_mode_enabled of this CreateFlinkSavepointRequestBody.
        :rtype: bool
        """
        return self._drain_mode_enabled

    @drain_mode_enabled.setter
    def drain_mode_enabled(self, drain_mode_enabled):
        r"""Sets the drain_mode_enabled of this CreateFlinkSavepointRequestBody.

        **参数解释**：是否启用Drain模式。启用后，触发Savepoint前将先发送Watermark到所有算子以触发窗口计算完成，然后再保存状态快照。 **约束限制**：不涉及。 **取值范围**：   - true：启用Drain模式。   - false：不启用Drain模式。 **默认取值**：false。 

        :param drain_mode_enabled: The drain_mode_enabled of this CreateFlinkSavepointRequestBody.
        :type drain_mode_enabled: bool
        """
        self._drain_mode_enabled = drain_mode_enabled

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
        if not isinstance(other, CreateFlinkSavepointRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
