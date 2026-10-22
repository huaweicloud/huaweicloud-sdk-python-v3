# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAiguardTemplateRuleRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_id': 'str',
        'x_language': 'str',
        'body': 'CreateAiguardTemplateRuleRequestBody'
    }

    attribute_map = {
        'policy_id': 'policy_id',
        'x_language': 'X-Language',
        'body': 'body'
    }

    def __init__(self, policy_id=None, x_language=None, body=None):
        r"""CreateAiguardTemplateRuleRequest

        The model defined in huaweicloud sdk

        :param policy_id: **参数解释：** 策略ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type policy_id: str
        :param x_language: **参数解释：** 语言 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** en-us
        :type x_language: str
        :param body: Body of the CreateAiguardTemplateRuleRequest
        :type body: :class:`huaweicloudsdkwaf.v1.CreateAiguardTemplateRuleRequestBody`
        """
        
        

        self._policy_id = None
        self._x_language = None
        self._body = None
        self.discriminator = None

        self.policy_id = policy_id
        if x_language is not None:
            self.x_language = x_language
        if body is not None:
            self.body = body

    @property
    def policy_id(self):
        r"""Gets the policy_id of this CreateAiguardTemplateRuleRequest.

        **参数解释：** 策略ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The policy_id of this CreateAiguardTemplateRuleRequest.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this CreateAiguardTemplateRuleRequest.

        **参数解释：** 策略ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param policy_id: The policy_id of this CreateAiguardTemplateRuleRequest.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def x_language(self):
        r"""Gets the x_language of this CreateAiguardTemplateRuleRequest.

        **参数解释：** 语言 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** en-us

        :return: The x_language of this CreateAiguardTemplateRuleRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this CreateAiguardTemplateRuleRequest.

        **参数解释：** 语言 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** en-us

        :param x_language: The x_language of this CreateAiguardTemplateRuleRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def body(self):
        r"""Gets the body of this CreateAiguardTemplateRuleRequest.

        :return: The body of this CreateAiguardTemplateRuleRequest.
        :rtype: :class:`huaweicloudsdkwaf.v1.CreateAiguardTemplateRuleRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CreateAiguardTemplateRuleRequest.

        :param body: The body of this CreateAiguardTemplateRuleRequest.
        :type body: :class:`huaweicloudsdkwaf.v1.CreateAiguardTemplateRuleRequestBody`
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
        if not isinstance(other, CreateAiguardTemplateRuleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
