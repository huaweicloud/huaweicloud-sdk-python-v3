# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackupVaultLockInfoRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'lock_retention_days': 'int',
        'lock_policy': 'bool'
    }

    attribute_map = {
        'lock_retention_days': 'lock_retention_days',
        'lock_policy': 'lock_policy'
    }

    def __init__(self, lock_retention_days=None, lock_policy=None):
        r"""BackupVaultLockInfoRequest

        The model defined in huaweicloud sdk

        :param lock_retention_days: **参数解释**：  合规锁保留期，单位是天。  **约束限制**：  仅支持按天配置。  **取值范围**：  1-36500。  **默认取值**：  1。
        :type lock_retention_days: int
        :param lock_policy: **参数解释**：  合规锁配置策略。  **约束限制**：  不涉及。  **取值范围**：  当前仅支持设置为true，表示开启或延期合规锁。  **默认取值**：  true。
        :type lock_policy: bool
        """
        
        

        self._lock_retention_days = None
        self._lock_policy = None
        self.discriminator = None

        self.lock_retention_days = lock_retention_days
        self.lock_policy = lock_policy

    @property
    def lock_retention_days(self):
        r"""Gets the lock_retention_days of this BackupVaultLockInfoRequest.

        **参数解释**：  合规锁保留期，单位是天。  **约束限制**：  仅支持按天配置。  **取值范围**：  1-36500。  **默认取值**：  1。

        :return: The lock_retention_days of this BackupVaultLockInfoRequest.
        :rtype: int
        """
        return self._lock_retention_days

    @lock_retention_days.setter
    def lock_retention_days(self, lock_retention_days):
        r"""Sets the lock_retention_days of this BackupVaultLockInfoRequest.

        **参数解释**：  合规锁保留期，单位是天。  **约束限制**：  仅支持按天配置。  **取值范围**：  1-36500。  **默认取值**：  1。

        :param lock_retention_days: The lock_retention_days of this BackupVaultLockInfoRequest.
        :type lock_retention_days: int
        """
        self._lock_retention_days = lock_retention_days

    @property
    def lock_policy(self):
        r"""Gets the lock_policy of this BackupVaultLockInfoRequest.

        **参数解释**：  合规锁配置策略。  **约束限制**：  不涉及。  **取值范围**：  当前仅支持设置为true，表示开启或延期合规锁。  **默认取值**：  true。

        :return: The lock_policy of this BackupVaultLockInfoRequest.
        :rtype: bool
        """
        return self._lock_policy

    @lock_policy.setter
    def lock_policy(self, lock_policy):
        r"""Sets the lock_policy of this BackupVaultLockInfoRequest.

        **参数解释**：  合规锁配置策略。  **约束限制**：  不涉及。  **取值范围**：  当前仅支持设置为true，表示开启或延期合规锁。  **默认取值**：  true。

        :param lock_policy: The lock_policy of this BackupVaultLockInfoRequest.
        :type lock_policy: bool
        """
        self._lock_policy = lock_policy

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
        if not isinstance(other, BackupVaultLockInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
