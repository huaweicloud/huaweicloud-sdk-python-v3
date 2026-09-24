# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Space:

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
        'auditlog': 'float',
        'snapshot': 'float',
        'cbr_snapshot': 'float',
        'obs_free': 'float',
        'snapshot_free': 'float',
        'db': 'float',
        'log': 'float'
    }

    attribute_map = {
        'obs': 'obs',
        'auditlog': 'auditlog',
        'snapshot': 'snapshot',
        'cbr_snapshot': 'cbr_snapshot',
        'obs_free': 'obs_free',
        'snapshot_free': 'snapshot_free',
        'db': 'db',
        'log': 'log'
    }

    def __init__(self, obs=None, auditlog=None, snapshot=None, cbr_snapshot=None, obs_free=None, snapshot_free=None, db=None, log=None):
        r"""Space

        The model defined in huaweicloud sdk

        :param obs: **参数解释**：  日志备份用量，单位MB。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type obs: float
        :param auditlog: **参数解释**：  审计日志用量，单位MB。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type auditlog: float
        :param snapshot: **参数解释**：  rds侧快照备份用量，单位MB。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type snapshot: float
        :param cbr_snapshot: **参数解释**：  rds侧CBR快照备份用量，单位MB。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type cbr_snapshot: float
        :param obs_free: **参数解释**：  日志备份赠送空间，单位GB。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type obs_free: float
        :param snapshot_free: **参数解释**：  快照备份赠送空间，单位GB。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type snapshot_free: float
        :param db: **参数解释**：  全量备份大小，单位MB。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type db: float
        :param log: **参数解释**：  增量备份大小，单位MB。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type log: float
        """
        
        

        self._obs = None
        self._auditlog = None
        self._snapshot = None
        self._cbr_snapshot = None
        self._obs_free = None
        self._snapshot_free = None
        self._db = None
        self._log = None
        self.discriminator = None

        if obs is not None:
            self.obs = obs
        if auditlog is not None:
            self.auditlog = auditlog
        if snapshot is not None:
            self.snapshot = snapshot
        if cbr_snapshot is not None:
            self.cbr_snapshot = cbr_snapshot
        if obs_free is not None:
            self.obs_free = obs_free
        if snapshot_free is not None:
            self.snapshot_free = snapshot_free
        if db is not None:
            self.db = db
        if log is not None:
            self.log = log

    @property
    def obs(self):
        r"""Gets the obs of this Space.

        **参数解释**：  日志备份用量，单位MB。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The obs of this Space.
        :rtype: float
        """
        return self._obs

    @obs.setter
    def obs(self, obs):
        r"""Sets the obs of this Space.

        **参数解释**：  日志备份用量，单位MB。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param obs: The obs of this Space.
        :type obs: float
        """
        self._obs = obs

    @property
    def auditlog(self):
        r"""Gets the auditlog of this Space.

        **参数解释**：  审计日志用量，单位MB。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The auditlog of this Space.
        :rtype: float
        """
        return self._auditlog

    @auditlog.setter
    def auditlog(self, auditlog):
        r"""Sets the auditlog of this Space.

        **参数解释**：  审计日志用量，单位MB。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param auditlog: The auditlog of this Space.
        :type auditlog: float
        """
        self._auditlog = auditlog

    @property
    def snapshot(self):
        r"""Gets the snapshot of this Space.

        **参数解释**：  rds侧快照备份用量，单位MB。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The snapshot of this Space.
        :rtype: float
        """
        return self._snapshot

    @snapshot.setter
    def snapshot(self, snapshot):
        r"""Sets the snapshot of this Space.

        **参数解释**：  rds侧快照备份用量，单位MB。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param snapshot: The snapshot of this Space.
        :type snapshot: float
        """
        self._snapshot = snapshot

    @property
    def cbr_snapshot(self):
        r"""Gets the cbr_snapshot of this Space.

        **参数解释**：  rds侧CBR快照备份用量，单位MB。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The cbr_snapshot of this Space.
        :rtype: float
        """
        return self._cbr_snapshot

    @cbr_snapshot.setter
    def cbr_snapshot(self, cbr_snapshot):
        r"""Sets the cbr_snapshot of this Space.

        **参数解释**：  rds侧CBR快照备份用量，单位MB。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param cbr_snapshot: The cbr_snapshot of this Space.
        :type cbr_snapshot: float
        """
        self._cbr_snapshot = cbr_snapshot

    @property
    def obs_free(self):
        r"""Gets the obs_free of this Space.

        **参数解释**：  日志备份赠送空间，单位GB。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The obs_free of this Space.
        :rtype: float
        """
        return self._obs_free

    @obs_free.setter
    def obs_free(self, obs_free):
        r"""Sets the obs_free of this Space.

        **参数解释**：  日志备份赠送空间，单位GB。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param obs_free: The obs_free of this Space.
        :type obs_free: float
        """
        self._obs_free = obs_free

    @property
    def snapshot_free(self):
        r"""Gets the snapshot_free of this Space.

        **参数解释**：  快照备份赠送空间，单位GB。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The snapshot_free of this Space.
        :rtype: float
        """
        return self._snapshot_free

    @snapshot_free.setter
    def snapshot_free(self, snapshot_free):
        r"""Sets the snapshot_free of this Space.

        **参数解释**：  快照备份赠送空间，单位GB。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param snapshot_free: The snapshot_free of this Space.
        :type snapshot_free: float
        """
        self._snapshot_free = snapshot_free

    @property
    def db(self):
        r"""Gets the db of this Space.

        **参数解释**：  全量备份大小，单位MB。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The db of this Space.
        :rtype: float
        """
        return self._db

    @db.setter
    def db(self, db):
        r"""Sets the db of this Space.

        **参数解释**：  全量备份大小，单位MB。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param db: The db of this Space.
        :type db: float
        """
        self._db = db

    @property
    def log(self):
        r"""Gets the log of this Space.

        **参数解释**：  增量备份大小，单位MB。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The log of this Space.
        :rtype: float
        """
        return self._log

    @log.setter
    def log(self, log):
        r"""Sets the log of this Space.

        **参数解释**：  增量备份大小，单位MB。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param log: The log of this Space.
        :type log: float
        """
        self._log = log

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
        if not isinstance(other, Space):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
