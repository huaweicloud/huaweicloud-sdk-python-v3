# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateKeyPolicyResponse(SdkResponse):

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
        'policy': 'UpdateKeyPolicyResponseBodyPolicy',
        'description': 'str',
        'last_modify_time': 'str'
    }

    attribute_map = {
        'policy_id': 'policy_id',
        'policy': 'policy',
        'description': 'description',
        'last_modify_time': 'last_modify_time'
    }

    def __init__(self, policy_id=None, policy=None, description=None, last_modify_time=None):
        r"""UpdateKeyPolicyResponse

        The model defined in huaweicloud sdk

        :param policy_id: **参数解释：** 密钥策略ID **取值范围：** 不涉及
        :type policy_id: str
        :param policy: 
        :type policy: :class:`huaweicloudsdkkms.v2.UpdateKeyPolicyResponseBodyPolicy`
        :param description: **参数解释：** 密钥策略描述信息 **取值范围：** 不涉及
        :type description: str
        :param last_modify_time: **参数解释：** 密钥策略最近更新时间 **取值范围：** 不涉及
        :type last_modify_time: str
        """
        
        super().__init__()

        self._policy_id = None
        self._policy = None
        self._description = None
        self._last_modify_time = None
        self.discriminator = None

        if policy_id is not None:
            self.policy_id = policy_id
        if policy is not None:
            self.policy = policy
        if description is not None:
            self.description = description
        if last_modify_time is not None:
            self.last_modify_time = last_modify_time

    @property
    def policy_id(self):
        r"""Gets the policy_id of this UpdateKeyPolicyResponse.

        **参数解释：** 密钥策略ID **取值范围：** 不涉及

        :return: The policy_id of this UpdateKeyPolicyResponse.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this UpdateKeyPolicyResponse.

        **参数解释：** 密钥策略ID **取值范围：** 不涉及

        :param policy_id: The policy_id of this UpdateKeyPolicyResponse.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def policy(self):
        r"""Gets the policy of this UpdateKeyPolicyResponse.

        :return: The policy of this UpdateKeyPolicyResponse.
        :rtype: :class:`huaweicloudsdkkms.v2.UpdateKeyPolicyResponseBodyPolicy`
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        r"""Sets the policy of this UpdateKeyPolicyResponse.

        :param policy: The policy of this UpdateKeyPolicyResponse.
        :type policy: :class:`huaweicloudsdkkms.v2.UpdateKeyPolicyResponseBodyPolicy`
        """
        self._policy = policy

    @property
    def description(self):
        r"""Gets the description of this UpdateKeyPolicyResponse.

        **参数解释：** 密钥策略描述信息 **取值范围：** 不涉及

        :return: The description of this UpdateKeyPolicyResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateKeyPolicyResponse.

        **参数解释：** 密钥策略描述信息 **取值范围：** 不涉及

        :param description: The description of this UpdateKeyPolicyResponse.
        :type description: str
        """
        self._description = description

    @property
    def last_modify_time(self):
        r"""Gets the last_modify_time of this UpdateKeyPolicyResponse.

        **参数解释：** 密钥策略最近更新时间 **取值范围：** 不涉及

        :return: The last_modify_time of this UpdateKeyPolicyResponse.
        :rtype: str
        """
        return self._last_modify_time

    @last_modify_time.setter
    def last_modify_time(self, last_modify_time):
        r"""Sets the last_modify_time of this UpdateKeyPolicyResponse.

        **参数解释：** 密钥策略最近更新时间 **取值范围：** 不涉及

        :param last_modify_time: The last_modify_time of this UpdateKeyPolicyResponse.
        :type last_modify_time: str
        """
        self._last_modify_time = last_modify_time

    def to_dict(self):
        import warnings
        warnings.warn("UpdateKeyPolicyResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, UpdateKeyPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
