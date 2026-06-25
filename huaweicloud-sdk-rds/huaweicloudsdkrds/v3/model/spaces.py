# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Spaces:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'obs': 'float',
        'snapshot': 'float',
        'obs_free': 'float',
        'snapshot_free': 'float'
    }

    attribute_map = {
        'obs': 'obs',
        'snapshot': 'snapshot',
        'obs_free': 'obs_free',
        'snapshot_free': 'snapshot_free'
    }

    def __init__(self, obs=None, snapshot=None, obs_free=None, snapshot_free=None):
        r"""Spaces

        The model defined in huaweicloud sdk

        :param obs: **参数解释**：  日志备份用量，单位MB。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type obs: float
        :param snapshot: **参数解释**：  rds侧快照备份用量，单位MB。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type snapshot: float
        :param obs_free: **参数解释**：  日志备份赠送空间，单位GB。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type obs_free: float
        :param snapshot_free: **参数解释**：  快照备份赠送空间，单位GB。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type snapshot_free: float
        """
        
        

        self._obs = None
        self._snapshot = None
        self._obs_free = None
        self._snapshot_free = None
        self.discriminator = None

        if obs is not None:
            self.obs = obs
        if snapshot is not None:
            self.snapshot = snapshot
        if obs_free is not None:
            self.obs_free = obs_free
        if snapshot_free is not None:
            self.snapshot_free = snapshot_free

    @property
    def obs(self):
        r"""Gets the obs of this Spaces.

        **参数解释**：  日志备份用量，单位MB。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The obs of this Spaces.
        :rtype: float
        """
        return self._obs

    @obs.setter
    def obs(self, obs):
        r"""Sets the obs of this Spaces.

        **参数解释**：  日志备份用量，单位MB。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param obs: The obs of this Spaces.
        :type obs: float
        """
        self._obs = obs

    @property
    def snapshot(self):
        r"""Gets the snapshot of this Spaces.

        **参数解释**：  rds侧快照备份用量，单位MB。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The snapshot of this Spaces.
        :rtype: float
        """
        return self._snapshot

    @snapshot.setter
    def snapshot(self, snapshot):
        r"""Sets the snapshot of this Spaces.

        **参数解释**：  rds侧快照备份用量，单位MB。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param snapshot: The snapshot of this Spaces.
        :type snapshot: float
        """
        self._snapshot = snapshot

    @property
    def obs_free(self):
        r"""Gets the obs_free of this Spaces.

        **参数解释**：  日志备份赠送空间，单位GB。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The obs_free of this Spaces.
        :rtype: float
        """
        return self._obs_free

    @obs_free.setter
    def obs_free(self, obs_free):
        r"""Sets the obs_free of this Spaces.

        **参数解释**：  日志备份赠送空间，单位GB。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param obs_free: The obs_free of this Spaces.
        :type obs_free: float
        """
        self._obs_free = obs_free

    @property
    def snapshot_free(self):
        r"""Gets the snapshot_free of this Spaces.

        **参数解释**：  快照备份赠送空间，单位GB。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The snapshot_free of this Spaces.
        :rtype: float
        """
        return self._snapshot_free

    @snapshot_free.setter
    def snapshot_free(self, snapshot_free):
        r"""Sets the snapshot_free of this Spaces.

        **参数解释**：  快照备份赠送空间，单位GB。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param snapshot_free: The snapshot_free of this Spaces.
        :type snapshot_free: float
        """
        self._snapshot_free = snapshot_free

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
        if not isinstance(other, Spaces):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
