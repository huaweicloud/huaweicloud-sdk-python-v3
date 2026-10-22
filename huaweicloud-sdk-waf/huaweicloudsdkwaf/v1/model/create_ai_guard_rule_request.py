# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAiGuardRuleRequest:

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
        'detect_type': 'str',
        'body': 'CreateAiGuardRuleRequestBody'
    }

    attribute_map = {
        'policy_id': 'policy_id',
        'detect_type': 'detect_type',
        'body': 'body'
    }

    def __init__(self, policy_id=None, detect_type=None, body=None):
        r"""CreateAiGuardRuleRequest

        The model defined in huaweicloud sdk

        :param policy_id: **参数解释：** 策略ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type policy_id: str
        :param detect_type: **参数解释：** 检测类型 **约束限制：** 不涉及 **取值范围：** text(文本), image(图片) **默认取值：** 不涉及
        :type detect_type: str
        :param body: Body of the CreateAiGuardRuleRequest
        :type body: :class:`huaweicloudsdkwaf.v1.CreateAiGuardRuleRequestBody`
        """
        
        

        self._policy_id = None
        self._detect_type = None
        self._body = None
        self.discriminator = None

        self.policy_id = policy_id
        if detect_type is not None:
            self.detect_type = detect_type
        if body is not None:
            self.body = body

    @property
    def policy_id(self):
        r"""Gets the policy_id of this CreateAiGuardRuleRequest.

        **参数解释：** 策略ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The policy_id of this CreateAiGuardRuleRequest.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this CreateAiGuardRuleRequest.

        **参数解释：** 策略ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param policy_id: The policy_id of this CreateAiGuardRuleRequest.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def detect_type(self):
        r"""Gets the detect_type of this CreateAiGuardRuleRequest.

        **参数解释：** 检测类型 **约束限制：** 不涉及 **取值范围：** text(文本), image(图片) **默认取值：** 不涉及

        :return: The detect_type of this CreateAiGuardRuleRequest.
        :rtype: str
        """
        return self._detect_type

    @detect_type.setter
    def detect_type(self, detect_type):
        r"""Sets the detect_type of this CreateAiGuardRuleRequest.

        **参数解释：** 检测类型 **约束限制：** 不涉及 **取值范围：** text(文本), image(图片) **默认取值：** 不涉及

        :param detect_type: The detect_type of this CreateAiGuardRuleRequest.
        :type detect_type: str
        """
        self._detect_type = detect_type

    @property
    def body(self):
        r"""Gets the body of this CreateAiGuardRuleRequest.

        :return: The body of this CreateAiGuardRuleRequest.
        :rtype: :class:`huaweicloudsdkwaf.v1.CreateAiGuardRuleRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CreateAiGuardRuleRequest.

        :param body: The body of this CreateAiGuardRuleRequest.
        :type body: :class:`huaweicloudsdkwaf.v1.CreateAiGuardRuleRequestBody`
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
        if not isinstance(other, CreateAiGuardRuleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
