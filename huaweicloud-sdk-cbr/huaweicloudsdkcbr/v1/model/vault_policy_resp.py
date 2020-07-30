# coding: utf-8

import pprint
import re

import six





class VaultPolicyResp:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'destination_vault_id': 'str',
        'policy_id': 'str',
        'vault_id': 'str'
    }

    attribute_map = {
        'destination_vault_id': 'destination_vault_id',
        'policy_id': 'policy_id',
        'vault_id': 'vault_id'
    }

    def __init__(self, destination_vault_id=None, policy_id=None, vault_id=None):
        """VaultPolicyResp - a model defined in huaweicloud sdk"""
        
        

        self._destination_vault_id = None
        self._policy_id = None
        self._vault_id = None
        self.discriminator = None

        if destination_vault_id is not None:
            self.destination_vault_id = destination_vault_id
        self.policy_id = policy_id
        self.vault_id = vault_id

    @property
    def destination_vault_id(self):
        """Gets the destination_vault_id of this VaultPolicyResp.

        目标region的vault ID，仅设置复制策略时有。

        :return: The destination_vault_id of this VaultPolicyResp.
        :rtype: str
        """
        return self._destination_vault_id

    @destination_vault_id.setter
    def destination_vault_id(self, destination_vault_id):
        """Sets the destination_vault_id of this VaultPolicyResp.

        目标region的vault ID，仅设置复制策略时有。

        :param destination_vault_id: The destination_vault_id of this VaultPolicyResp.
        :type: str
        """
        self._destination_vault_id = destination_vault_id

    @property
    def policy_id(self):
        """Gets the policy_id of this VaultPolicyResp.

        设置的策略ID

        :return: The policy_id of this VaultPolicyResp.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """Sets the policy_id of this VaultPolicyResp.

        设置的策略ID

        :param policy_id: The policy_id of this VaultPolicyResp.
        :type: str
        """
        self._policy_id = policy_id

    @property
    def vault_id(self):
        """Gets the vault_id of this VaultPolicyResp.

        设置策略的vault ID

        :return: The vault_id of this VaultPolicyResp.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        """Sets the vault_id of this VaultPolicyResp.

        设置策略的vault ID

        :param vault_id: The vault_id of this VaultPolicyResp.
        :type: str
        """
        self._vault_id = vault_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, VaultPolicyResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
