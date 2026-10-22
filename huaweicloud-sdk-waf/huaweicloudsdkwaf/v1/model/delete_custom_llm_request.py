# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteCustomLlmRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'llm_id': 'str'
    }

    attribute_map = {
        'llm_id': 'llmId'
    }

    def __init__(self, llm_id=None):
        r"""DeleteCustomLlmRequest

        The model defined in huaweicloud sdk

        :param llm_id: **参数解释：** 自定义大模型ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type llm_id: str
        """
        
        

        self._llm_id = None
        self.discriminator = None

        self.llm_id = llm_id

    @property
    def llm_id(self):
        r"""Gets the llm_id of this DeleteCustomLlmRequest.

        **参数解释：** 自定义大模型ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The llm_id of this DeleteCustomLlmRequest.
        :rtype: str
        """
        return self._llm_id

    @llm_id.setter
    def llm_id(self, llm_id):
        r"""Sets the llm_id of this DeleteCustomLlmRequest.

        **参数解释：** 自定义大模型ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param llm_id: The llm_id of this DeleteCustomLlmRequest.
        :type llm_id: str
        """
        self._llm_id = llm_id

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
        if not isinstance(other, DeleteCustomLlmRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
