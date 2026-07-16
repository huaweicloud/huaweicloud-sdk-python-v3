# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOpsSynthesisTaskRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'synthesis_id': 'str'
    }

    attribute_map = {
        'synthesis_id': 'synthesis_id'
    }

    def __init__(self, synthesis_id=None):
        r"""ShowOpsSynthesisTaskRequest

        The model defined in huaweicloud sdk

        :param synthesis_id: **参数解释：** 合成任务的唯一标识符（ID），该参数用于在路径中指定特定的合成任务，以便执行查询、停止或删除等操作。 **约束限制：** 字符串长度限制为1到64个字符。通常采用标准 UUID格式。 **取值范围：** 1-64位字符。 **默认取值：** 不涉及。 
        :type synthesis_id: str
        """
        
        

        self._synthesis_id = None
        self.discriminator = None

        self.synthesis_id = synthesis_id

    @property
    def synthesis_id(self):
        r"""Gets the synthesis_id of this ShowOpsSynthesisTaskRequest.

        **参数解释：** 合成任务的唯一标识符（ID），该参数用于在路径中指定特定的合成任务，以便执行查询、停止或删除等操作。 **约束限制：** 字符串长度限制为1到64个字符。通常采用标准 UUID格式。 **取值范围：** 1-64位字符。 **默认取值：** 不涉及。 

        :return: The synthesis_id of this ShowOpsSynthesisTaskRequest.
        :rtype: str
        """
        return self._synthesis_id

    @synthesis_id.setter
    def synthesis_id(self, synthesis_id):
        r"""Sets the synthesis_id of this ShowOpsSynthesisTaskRequest.

        **参数解释：** 合成任务的唯一标识符（ID），该参数用于在路径中指定特定的合成任务，以便执行查询、停止或删除等操作。 **约束限制：** 字符串长度限制为1到64个字符。通常采用标准 UUID格式。 **取值范围：** 1-64位字符。 **默认取值：** 不涉及。 

        :param synthesis_id: The synthesis_id of this ShowOpsSynthesisTaskRequest.
        :type synthesis_id: str
        """
        self._synthesis_id = synthesis_id

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
        if not isinstance(other, ShowOpsSynthesisTaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
