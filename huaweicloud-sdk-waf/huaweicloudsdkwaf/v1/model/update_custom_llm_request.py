# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateCustomLlmRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'llm_id': 'str',
        'body': 'AiguardCustomLlmUpdateBody'
    }

    attribute_map = {
        'llm_id': 'llmId',
        'body': 'body'
    }

    def __init__(self, llm_id=None, body=None):
        r"""UpdateCustomLlmRequest

        The model defined in huaweicloud sdk

        :param llm_id: **参数解释：** 自定义大模型ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type llm_id: str
        :param body: Body of the UpdateCustomLlmRequest
        :type body: :class:`huaweicloudsdkwaf.v1.AiguardCustomLlmUpdateBody`
        """
        
        

        self._llm_id = None
        self._body = None
        self.discriminator = None

        self.llm_id = llm_id
        if body is not None:
            self.body = body

    @property
    def llm_id(self):
        r"""Gets the llm_id of this UpdateCustomLlmRequest.

        **参数解释：** 自定义大模型ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The llm_id of this UpdateCustomLlmRequest.
        :rtype: str
        """
        return self._llm_id

    @llm_id.setter
    def llm_id(self, llm_id):
        r"""Sets the llm_id of this UpdateCustomLlmRequest.

        **参数解释：** 自定义大模型ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param llm_id: The llm_id of this UpdateCustomLlmRequest.
        :type llm_id: str
        """
        self._llm_id = llm_id

    @property
    def body(self):
        r"""Gets the body of this UpdateCustomLlmRequest.

        :return: The body of this UpdateCustomLlmRequest.
        :rtype: :class:`huaweicloudsdkwaf.v1.AiguardCustomLlmUpdateBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateCustomLlmRequest.

        :param body: The body of this UpdateCustomLlmRequest.
        :type body: :class:`huaweicloudsdkwaf.v1.AiguardCustomLlmUpdateBody`
        """
        self._body = body

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
        if not isinstance(other, UpdateCustomLlmRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
