# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExceededInstanceInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'obs_usage_gb': 'float',
        'obs_free_backup_space_gb': 'float',
        'snapshot_usage_gb': 'float',
        'snapshot_free_backup_space_gb': 'float'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'obs_usage_gb': 'obs_usage_gb',
        'obs_free_backup_space_gb': 'obs_free_backup_space_gb',
        'snapshot_usage_gb': 'snapshot_usage_gb',
        'snapshot_free_backup_space_gb': 'snapshot_free_backup_space_gb'
    }

    def __init__(self, instance_id=None, obs_usage_gb=None, obs_free_backup_space_gb=None, snapshot_usage_gb=None, snapshot_free_backup_space_gb=None):
        r"""ExceededInstanceInfo

        The model defined in huaweicloud sdk

        :param instance_id: **参数解释**：  实例ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type instance_id: str
        :param obs_usage_gb: **参数解释**：  日志备份空间使用量，单位GB。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type obs_usage_gb: float
        :param obs_free_backup_space_gb: **参数解释**：  日志备份免费备份空间额度，单位GB。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type obs_free_backup_space_gb: float
        :param snapshot_usage_gb: **参数解释**：  快照备份空间使用量，单位GB。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type snapshot_usage_gb: float
        :param snapshot_free_backup_space_gb: **参数解释**：  快照免费备份空间额度，单位GB。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type snapshot_free_backup_space_gb: float
        """
        
        

        self._instance_id = None
        self._obs_usage_gb = None
        self._obs_free_backup_space_gb = None
        self._snapshot_usage_gb = None
        self._snapshot_free_backup_space_gb = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if obs_usage_gb is not None:
            self.obs_usage_gb = obs_usage_gb
        if obs_free_backup_space_gb is not None:
            self.obs_free_backup_space_gb = obs_free_backup_space_gb
        if snapshot_usage_gb is not None:
            self.snapshot_usage_gb = snapshot_usage_gb
        if snapshot_free_backup_space_gb is not None:
            self.snapshot_free_backup_space_gb = snapshot_free_backup_space_gb

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ExceededInstanceInfo.

        **参数解释**：  实例ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The instance_id of this ExceededInstanceInfo.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ExceededInstanceInfo.

        **参数解释**：  实例ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param instance_id: The instance_id of this ExceededInstanceInfo.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def obs_usage_gb(self):
        r"""Gets the obs_usage_gb of this ExceededInstanceInfo.

        **参数解释**：  日志备份空间使用量，单位GB。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The obs_usage_gb of this ExceededInstanceInfo.
        :rtype: float
        """
        return self._obs_usage_gb

    @obs_usage_gb.setter
    def obs_usage_gb(self, obs_usage_gb):
        r"""Sets the obs_usage_gb of this ExceededInstanceInfo.

        **参数解释**：  日志备份空间使用量，单位GB。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param obs_usage_gb: The obs_usage_gb of this ExceededInstanceInfo.
        :type obs_usage_gb: float
        """
        self._obs_usage_gb = obs_usage_gb

    @property
    def obs_free_backup_space_gb(self):
        r"""Gets the obs_free_backup_space_gb of this ExceededInstanceInfo.

        **参数解释**：  日志备份免费备份空间额度，单位GB。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The obs_free_backup_space_gb of this ExceededInstanceInfo.
        :rtype: float
        """
        return self._obs_free_backup_space_gb

    @obs_free_backup_space_gb.setter
    def obs_free_backup_space_gb(self, obs_free_backup_space_gb):
        r"""Sets the obs_free_backup_space_gb of this ExceededInstanceInfo.

        **参数解释**：  日志备份免费备份空间额度，单位GB。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param obs_free_backup_space_gb: The obs_free_backup_space_gb of this ExceededInstanceInfo.
        :type obs_free_backup_space_gb: float
        """
        self._obs_free_backup_space_gb = obs_free_backup_space_gb

    @property
    def snapshot_usage_gb(self):
        r"""Gets the snapshot_usage_gb of this ExceededInstanceInfo.

        **参数解释**：  快照备份空间使用量，单位GB。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The snapshot_usage_gb of this ExceededInstanceInfo.
        :rtype: float
        """
        return self._snapshot_usage_gb

    @snapshot_usage_gb.setter
    def snapshot_usage_gb(self, snapshot_usage_gb):
        r"""Sets the snapshot_usage_gb of this ExceededInstanceInfo.

        **参数解释**：  快照备份空间使用量，单位GB。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param snapshot_usage_gb: The snapshot_usage_gb of this ExceededInstanceInfo.
        :type snapshot_usage_gb: float
        """
        self._snapshot_usage_gb = snapshot_usage_gb

    @property
    def snapshot_free_backup_space_gb(self):
        r"""Gets the snapshot_free_backup_space_gb of this ExceededInstanceInfo.

        **参数解释**：  快照免费备份空间额度，单位GB。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The snapshot_free_backup_space_gb of this ExceededInstanceInfo.
        :rtype: float
        """
        return self._snapshot_free_backup_space_gb

    @snapshot_free_backup_space_gb.setter
    def snapshot_free_backup_space_gb(self, snapshot_free_backup_space_gb):
        r"""Sets the snapshot_free_backup_space_gb of this ExceededInstanceInfo.

        **参数解释**：  快照免费备份空间额度，单位GB。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param snapshot_free_backup_space_gb: The snapshot_free_backup_space_gb of this ExceededInstanceInfo.
        :type snapshot_free_backup_space_gb: float
        """
        self._snapshot_free_backup_space_gb = snapshot_free_backup_space_gb

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
        if not isinstance(other, ExceededInstanceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
