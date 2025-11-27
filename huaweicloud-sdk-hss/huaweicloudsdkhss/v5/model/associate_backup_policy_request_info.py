# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssociateBackupPolicyRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vault_id': 'str',
        'policy_id': 'str'
    }

    attribute_map = {
        'vault_id': 'vault_id',
        'policy_id': 'policy_id'
    }

    def __init__(self, vault_id=None, policy_id=None):
        r"""AssociateBackupPolicyRequestInfo

        The model defined in huaweicloud sdk

        :param vault_id: **参数解释**: 需要绑定的存储库id **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 
        :type vault_id: str
        :param policy_id: **参数解释**: 需要绑定的策略id **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 
        :type policy_id: str
        """
        
        

        self._vault_id = None
        self._policy_id = None
        self.discriminator = None

        if vault_id is not None:
            self.vault_id = vault_id
        if policy_id is not None:
            self.policy_id = policy_id

    @property
    def vault_id(self):
        r"""Gets the vault_id of this AssociateBackupPolicyRequestInfo.

        **参数解释**: 需要绑定的存储库id **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :return: The vault_id of this AssociateBackupPolicyRequestInfo.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        r"""Sets the vault_id of this AssociateBackupPolicyRequestInfo.

        **参数解释**: 需要绑定的存储库id **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :param vault_id: The vault_id of this AssociateBackupPolicyRequestInfo.
        :type vault_id: str
        """
        self._vault_id = vault_id

    @property
    def policy_id(self):
        r"""Gets the policy_id of this AssociateBackupPolicyRequestInfo.

        **参数解释**: 需要绑定的策略id **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :return: The policy_id of this AssociateBackupPolicyRequestInfo.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this AssociateBackupPolicyRequestInfo.

        **参数解释**: 需要绑定的策略id **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :param policy_id: The policy_id of this AssociateBackupPolicyRequestInfo.
        :type policy_id: str
        """
        self._policy_id = policy_id

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
        if not isinstance(other, AssociateBackupPolicyRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
