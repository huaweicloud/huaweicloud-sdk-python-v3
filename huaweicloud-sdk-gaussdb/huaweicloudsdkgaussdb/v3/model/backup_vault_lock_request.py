# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackupVaultLockRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'backup_vaultlock_info': 'BackupVaultLockInfoRequest',
        'action': 'str'
    }

    attribute_map = {
        'backup_vaultlock_info': 'backup_vaultlock_info',
        'action': 'action'
    }

    def __init__(self, backup_vaultlock_info=None, action=None):
        r"""BackupVaultLockRequest

        The model defined in huaweicloud sdk

        :param backup_vaultlock_info: 
        :type backup_vaultlock_info: :class:`huaweicloudsdkgaussdb.v3.BackupVaultLockInfoRequest`
        :param action: **参数解释**：  操作类型。  **约束限制**：  当前只支持开启和延期。不区分大小写。  **取值范围**： - enable：开启。 - extend：延期。  **默认取值**：  enable。
        :type action: str
        """
        
        

        self._backup_vaultlock_info = None
        self._action = None
        self.discriminator = None

        self.backup_vaultlock_info = backup_vaultlock_info
        self.action = action

    @property
    def backup_vaultlock_info(self):
        r"""Gets the backup_vaultlock_info of this BackupVaultLockRequest.

        :return: The backup_vaultlock_info of this BackupVaultLockRequest.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.BackupVaultLockInfoRequest`
        """
        return self._backup_vaultlock_info

    @backup_vaultlock_info.setter
    def backup_vaultlock_info(self, backup_vaultlock_info):
        r"""Sets the backup_vaultlock_info of this BackupVaultLockRequest.

        :param backup_vaultlock_info: The backup_vaultlock_info of this BackupVaultLockRequest.
        :type backup_vaultlock_info: :class:`huaweicloudsdkgaussdb.v3.BackupVaultLockInfoRequest`
        """
        self._backup_vaultlock_info = backup_vaultlock_info

    @property
    def action(self):
        r"""Gets the action of this BackupVaultLockRequest.

        **参数解释**：  操作类型。  **约束限制**：  当前只支持开启和延期。不区分大小写。  **取值范围**： - enable：开启。 - extend：延期。  **默认取值**：  enable。

        :return: The action of this BackupVaultLockRequest.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this BackupVaultLockRequest.

        **参数解释**：  操作类型。  **约束限制**：  当前只支持开启和延期。不区分大小写。  **取值范围**： - enable：开启。 - extend：延期。  **默认取值**：  enable。

        :param action: The action of this BackupVaultLockRequest.
        :type action: str
        """
        self._action = action

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
        if not isinstance(other, BackupVaultLockRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
