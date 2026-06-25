# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBackupUsageResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'backup_use_space': 'float',
        'db_use_space': 'float',
        'rds_snapshot_use_space': 'float',
        'offsite_use_space': 'float'
    }

    attribute_map = {
        'backup_use_space': 'backup_use_space',
        'db_use_space': 'db_use_space',
        'rds_snapshot_use_space': 'rds_snapshot_use_space',
        'offsite_use_space': 'offsite_use_space'
    }

    def __init__(self, backup_use_space=None, db_use_space=None, rds_snapshot_use_space=None, offsite_use_space=None):
        r"""ShowBackupUsageResponse

        The model defined in huaweicloud sdk

        :param backup_use_space: **参数解释**：  备份总使用量，各类备份占用的备份总大小。 单位：MB  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type backup_use_space: float
        :param db_use_space: **参数解释**：  物理备份总使用量，包括本区域的物理全量备份，binlog日志备份，审计日志。 单位：MB  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type db_use_space: float
        :param rds_snapshot_use_space: **参数解释**：  由RDS计费的cbr快照备份总使用量， 单位MB  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type rds_snapshot_use_space: float
        :param offsite_use_space: **参数解释**：  跨区域备份总使用量，包括跨区域的物理全量备份，binlog日志备份， 单位：MB  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type offsite_use_space: float
        """
        
        super().__init__()

        self._backup_use_space = None
        self._db_use_space = None
        self._rds_snapshot_use_space = None
        self._offsite_use_space = None
        self.discriminator = None

        if backup_use_space is not None:
            self.backup_use_space = backup_use_space
        if db_use_space is not None:
            self.db_use_space = db_use_space
        if rds_snapshot_use_space is not None:
            self.rds_snapshot_use_space = rds_snapshot_use_space
        if offsite_use_space is not None:
            self.offsite_use_space = offsite_use_space

    @property
    def backup_use_space(self):
        r"""Gets the backup_use_space of this ShowBackupUsageResponse.

        **参数解释**：  备份总使用量，各类备份占用的备份总大小。 单位：MB  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The backup_use_space of this ShowBackupUsageResponse.
        :rtype: float
        """
        return self._backup_use_space

    @backup_use_space.setter
    def backup_use_space(self, backup_use_space):
        r"""Sets the backup_use_space of this ShowBackupUsageResponse.

        **参数解释**：  备份总使用量，各类备份占用的备份总大小。 单位：MB  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param backup_use_space: The backup_use_space of this ShowBackupUsageResponse.
        :type backup_use_space: float
        """
        self._backup_use_space = backup_use_space

    @property
    def db_use_space(self):
        r"""Gets the db_use_space of this ShowBackupUsageResponse.

        **参数解释**：  物理备份总使用量，包括本区域的物理全量备份，binlog日志备份，审计日志。 单位：MB  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The db_use_space of this ShowBackupUsageResponse.
        :rtype: float
        """
        return self._db_use_space

    @db_use_space.setter
    def db_use_space(self, db_use_space):
        r"""Sets the db_use_space of this ShowBackupUsageResponse.

        **参数解释**：  物理备份总使用量，包括本区域的物理全量备份，binlog日志备份，审计日志。 单位：MB  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param db_use_space: The db_use_space of this ShowBackupUsageResponse.
        :type db_use_space: float
        """
        self._db_use_space = db_use_space

    @property
    def rds_snapshot_use_space(self):
        r"""Gets the rds_snapshot_use_space of this ShowBackupUsageResponse.

        **参数解释**：  由RDS计费的cbr快照备份总使用量， 单位MB  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The rds_snapshot_use_space of this ShowBackupUsageResponse.
        :rtype: float
        """
        return self._rds_snapshot_use_space

    @rds_snapshot_use_space.setter
    def rds_snapshot_use_space(self, rds_snapshot_use_space):
        r"""Sets the rds_snapshot_use_space of this ShowBackupUsageResponse.

        **参数解释**：  由RDS计费的cbr快照备份总使用量， 单位MB  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param rds_snapshot_use_space: The rds_snapshot_use_space of this ShowBackupUsageResponse.
        :type rds_snapshot_use_space: float
        """
        self._rds_snapshot_use_space = rds_snapshot_use_space

    @property
    def offsite_use_space(self):
        r"""Gets the offsite_use_space of this ShowBackupUsageResponse.

        **参数解释**：  跨区域备份总使用量，包括跨区域的物理全量备份，binlog日志备份， 单位：MB  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The offsite_use_space of this ShowBackupUsageResponse.
        :rtype: float
        """
        return self._offsite_use_space

    @offsite_use_space.setter
    def offsite_use_space(self, offsite_use_space):
        r"""Sets the offsite_use_space of this ShowBackupUsageResponse.

        **参数解释**：  跨区域备份总使用量，包括跨区域的物理全量备份，binlog日志备份， 单位：MB  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param offsite_use_space: The offsite_use_space of this ShowBackupUsageResponse.
        :type offsite_use_space: float
        """
        self._offsite_use_space = offsite_use_space

    def to_dict(self):
        import warnings
        warnings.warn("ShowBackupUsageResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowBackupUsageResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
