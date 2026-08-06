# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateKeyPolicyRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'keyspace_id': 'str',
        'policy_name': 'str',
        'policy': 'str',
        'description': 'str'
    }

    attribute_map = {
        'keyspace_id': 'keyspace_id',
        'policy_name': 'policy_name',
        'policy': 'policy',
        'description': 'description'
    }

    def __init__(self, keyspace_id=None, policy_name=None, policy=None, description=None):
        r"""CreateKeyPolicyRequestBody

        The model defined in huaweicloud sdk

        :param keyspace_id: **参数解释：** 密钥策略归属的可信密钥空间ID **约束限制：** 满足正则表达式^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$ **取值范围：** 不涉及 **默认取值：** 不涉及
        :type keyspace_id: str
        :param policy_name: **参数解释：** 策略策略名称 **约束限制：** 满足正则表达式^[a-zA-Z0-9:/_-]{1,255}$ **取值范围：** 1-255 **默认取值：** 不涉及
        :type policy_name: str
        :param policy: **参数解释：** 密钥策略 **约束限制：** 转移后的JSON字符串 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type policy: str
        :param description: **参数解释：** 密钥策略描述信息 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type description: str
        """
        
        

        self._keyspace_id = None
        self._policy_name = None
        self._policy = None
        self._description = None
        self.discriminator = None

        self.keyspace_id = keyspace_id
        self.policy_name = policy_name
        self.policy = policy
        if description is not None:
            self.description = description

    @property
    def keyspace_id(self):
        r"""Gets the keyspace_id of this CreateKeyPolicyRequestBody.

        **参数解释：** 密钥策略归属的可信密钥空间ID **约束限制：** 满足正则表达式^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$ **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The keyspace_id of this CreateKeyPolicyRequestBody.
        :rtype: str
        """
        return self._keyspace_id

    @keyspace_id.setter
    def keyspace_id(self, keyspace_id):
        r"""Sets the keyspace_id of this CreateKeyPolicyRequestBody.

        **参数解释：** 密钥策略归属的可信密钥空间ID **约束限制：** 满足正则表达式^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$ **取值范围：** 不涉及 **默认取值：** 不涉及

        :param keyspace_id: The keyspace_id of this CreateKeyPolicyRequestBody.
        :type keyspace_id: str
        """
        self._keyspace_id = keyspace_id

    @property
    def policy_name(self):
        r"""Gets the policy_name of this CreateKeyPolicyRequestBody.

        **参数解释：** 策略策略名称 **约束限制：** 满足正则表达式^[a-zA-Z0-9:/_-]{1,255}$ **取值范围：** 1-255 **默认取值：** 不涉及

        :return: The policy_name of this CreateKeyPolicyRequestBody.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this CreateKeyPolicyRequestBody.

        **参数解释：** 策略策略名称 **约束限制：** 满足正则表达式^[a-zA-Z0-9:/_-]{1,255}$ **取值范围：** 1-255 **默认取值：** 不涉及

        :param policy_name: The policy_name of this CreateKeyPolicyRequestBody.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def policy(self):
        r"""Gets the policy of this CreateKeyPolicyRequestBody.

        **参数解释：** 密钥策略 **约束限制：** 转移后的JSON字符串 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The policy of this CreateKeyPolicyRequestBody.
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        r"""Sets the policy of this CreateKeyPolicyRequestBody.

        **参数解释：** 密钥策略 **约束限制：** 转移后的JSON字符串 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param policy: The policy of this CreateKeyPolicyRequestBody.
        :type policy: str
        """
        self._policy = policy

    @property
    def description(self):
        r"""Gets the description of this CreateKeyPolicyRequestBody.

        **参数解释：** 密钥策略描述信息 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The description of this CreateKeyPolicyRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateKeyPolicyRequestBody.

        **参数解释：** 密钥策略描述信息 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param description: The description of this CreateKeyPolicyRequestBody.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, CreateKeyPolicyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
