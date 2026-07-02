# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackupVaultLockInfo:

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
        'lock_policy': 'bool',
        'lock_start_time': 'int',
        'lock_end_time': 'int'
    }

    attribute_map = {
        'lock_retention_days': 'lock_retention_days',
        'lock_policy': 'lock_policy',
        'lock_start_time': 'lock_start_time',
        'lock_end_time': 'lock_end_time'
    }

    def __init__(self, lock_retention_days=None, lock_policy=None, lock_start_time=None, lock_end_time=None):
        r"""BackupVaultLockInfo

        The model defined in huaweicloud sdk

        :param lock_retention_days: **参数解释**：  合规锁保留期，单位是天。  **取值范围**：  1-36500。
        :type lock_retention_days: int
        :param lock_policy: **参数解释**：  合规锁配置策略。  **取值范围**：  - true：已开启合规锁配置。 - false: 未开启合规锁配置。
        :type lock_policy: bool
        :param lock_start_time: **参数解释**：  合规锁开始时间，时间戳格式。  **取值范围**：  不涉及。
        :type lock_start_time: int
        :param lock_end_time: **参数解释**：  合规锁结束时间，时间戳格式。  **取值范围**：  不涉及。
        :type lock_end_time: int
        """
        
        

        self._lock_retention_days = None
        self._lock_policy = None
        self._lock_start_time = None
        self._lock_end_time = None
        self.discriminator = None

        self.lock_retention_days = lock_retention_days
        self.lock_policy = lock_policy
        self.lock_start_time = lock_start_time
        self.lock_end_time = lock_end_time

    @property
    def lock_retention_days(self):
        r"""Gets the lock_retention_days of this BackupVaultLockInfo.

        **参数解释**：  合规锁保留期，单位是天。  **取值范围**：  1-36500。

        :return: The lock_retention_days of this BackupVaultLockInfo.
        :rtype: int
        """
        return self._lock_retention_days

    @lock_retention_days.setter
    def lock_retention_days(self, lock_retention_days):
        r"""Sets the lock_retention_days of this BackupVaultLockInfo.

        **参数解释**：  合规锁保留期，单位是天。  **取值范围**：  1-36500。

        :param lock_retention_days: The lock_retention_days of this BackupVaultLockInfo.
        :type lock_retention_days: int
        """
        self._lock_retention_days = lock_retention_days

    @property
    def lock_policy(self):
        r"""Gets the lock_policy of this BackupVaultLockInfo.

        **参数解释**：  合规锁配置策略。  **取值范围**：  - true：已开启合规锁配置。 - false: 未开启合规锁配置。

        :return: The lock_policy of this BackupVaultLockInfo.
        :rtype: bool
        """
        return self._lock_policy

    @lock_policy.setter
    def lock_policy(self, lock_policy):
        r"""Sets the lock_policy of this BackupVaultLockInfo.

        **参数解释**：  合规锁配置策略。  **取值范围**：  - true：已开启合规锁配置。 - false: 未开启合规锁配置。

        :param lock_policy: The lock_policy of this BackupVaultLockInfo.
        :type lock_policy: bool
        """
        self._lock_policy = lock_policy

    @property
    def lock_start_time(self):
        r"""Gets the lock_start_time of this BackupVaultLockInfo.

        **参数解释**：  合规锁开始时间，时间戳格式。  **取值范围**：  不涉及。

        :return: The lock_start_time of this BackupVaultLockInfo.
        :rtype: int
        """
        return self._lock_start_time

    @lock_start_time.setter
    def lock_start_time(self, lock_start_time):
        r"""Sets the lock_start_time of this BackupVaultLockInfo.

        **参数解释**：  合规锁开始时间，时间戳格式。  **取值范围**：  不涉及。

        :param lock_start_time: The lock_start_time of this BackupVaultLockInfo.
        :type lock_start_time: int
        """
        self._lock_start_time = lock_start_time

    @property
    def lock_end_time(self):
        r"""Gets the lock_end_time of this BackupVaultLockInfo.

        **参数解释**：  合规锁结束时间，时间戳格式。  **取值范围**：  不涉及。

        :return: The lock_end_time of this BackupVaultLockInfo.
        :rtype: int
        """
        return self._lock_end_time

    @lock_end_time.setter
    def lock_end_time(self, lock_end_time):
        r"""Sets the lock_end_time of this BackupVaultLockInfo.

        **参数解释**：  合规锁结束时间，时间戳格式。  **取值范围**：  不涉及。

        :param lock_end_time: The lock_end_time of this BackupVaultLockInfo.
        :type lock_end_time: int
        """
        self._lock_end_time = lock_end_time

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
        if not isinstance(other, BackupVaultLockInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
