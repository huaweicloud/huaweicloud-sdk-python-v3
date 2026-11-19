# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMigrateInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rds_instance_id': 'str',
        'rds_status': 'str',
        'rds_instance_name': 'str',
        'drs_job_id': 'str',
        'drs_status': 'str',
        'rds_readwrite_mode': 'str',
        'taurus_readwrite_mode': 'str',
        'migration_direction': 'str'
    }

    attribute_map = {
        'rds_instance_id': 'rds_instance_id',
        'rds_status': 'rds_status',
        'rds_instance_name': 'rds_instance_name',
        'drs_job_id': 'drs_job_id',
        'drs_status': 'drs_status',
        'rds_readwrite_mode': 'rds_readwrite_mode',
        'taurus_readwrite_mode': 'taurus_readwrite_mode',
        'migration_direction': 'migration_direction'
    }

    def __init__(self, rds_instance_id=None, rds_status=None, rds_instance_name=None, drs_job_id=None, drs_status=None, rds_readwrite_mode=None, taurus_readwrite_mode=None, migration_direction=None):
        r"""ShowMigrateInfoResponse

        The model defined in huaweicloud sdk

        :param rds_instance_id: **参数解释**：  源实例ID。  **取值范围**：  只能由英文字母、数字组成，长度为36个字符。
        :type rds_instance_id: str
        :param rds_status: **参数解释**：  源实例状态。  **取值范围**：  不涉及。
        :type rds_status: str
        :param rds_instance_name: **参数解释**：  源实例名称。  **取值范围**：  不涉及。
        :type rds_instance_name: str
        :param drs_job_id: **参数解释**：  迁移任务ID。  **取值范围**：  不涉及。
        :type drs_job_id: str
        :param drs_status: **参数解释**：  迁移任务状态。  **取值范围**：  不涉及。
        :type drs_status: str
        :param rds_readwrite_mode: **参数解释**：  源实例读写状态。  **取值范围**：  - ON：读写状态。 - OFF：只读状态。
        :type rds_readwrite_mode: str
        :param taurus_readwrite_mode: **参数解释**：  目标实例读写状态。  **取值范围**：  - ON：读写状态。 - OFF：只读状态。
        :type taurus_readwrite_mode: str
        :param migration_direction: **参数解释**：G  迁移方向。  **取值范围**：  - up：源实例到TaurusDB实例。 - down：TaurusDB实例到源实例。
        :type migration_direction: str
        """
        
        super().__init__()

        self._rds_instance_id = None
        self._rds_status = None
        self._rds_instance_name = None
        self._drs_job_id = None
        self._drs_status = None
        self._rds_readwrite_mode = None
        self._taurus_readwrite_mode = None
        self._migration_direction = None
        self.discriminator = None

        if rds_instance_id is not None:
            self.rds_instance_id = rds_instance_id
        if rds_status is not None:
            self.rds_status = rds_status
        if rds_instance_name is not None:
            self.rds_instance_name = rds_instance_name
        if drs_job_id is not None:
            self.drs_job_id = drs_job_id
        if drs_status is not None:
            self.drs_status = drs_status
        if rds_readwrite_mode is not None:
            self.rds_readwrite_mode = rds_readwrite_mode
        if taurus_readwrite_mode is not None:
            self.taurus_readwrite_mode = taurus_readwrite_mode
        if migration_direction is not None:
            self.migration_direction = migration_direction

    @property
    def rds_instance_id(self):
        r"""Gets the rds_instance_id of this ShowMigrateInfoResponse.

        **参数解释**：  源实例ID。  **取值范围**：  只能由英文字母、数字组成，长度为36个字符。

        :return: The rds_instance_id of this ShowMigrateInfoResponse.
        :rtype: str
        """
        return self._rds_instance_id

    @rds_instance_id.setter
    def rds_instance_id(self, rds_instance_id):
        r"""Sets the rds_instance_id of this ShowMigrateInfoResponse.

        **参数解释**：  源实例ID。  **取值范围**：  只能由英文字母、数字组成，长度为36个字符。

        :param rds_instance_id: The rds_instance_id of this ShowMigrateInfoResponse.
        :type rds_instance_id: str
        """
        self._rds_instance_id = rds_instance_id

    @property
    def rds_status(self):
        r"""Gets the rds_status of this ShowMigrateInfoResponse.

        **参数解释**：  源实例状态。  **取值范围**：  不涉及。

        :return: The rds_status of this ShowMigrateInfoResponse.
        :rtype: str
        """
        return self._rds_status

    @rds_status.setter
    def rds_status(self, rds_status):
        r"""Sets the rds_status of this ShowMigrateInfoResponse.

        **参数解释**：  源实例状态。  **取值范围**：  不涉及。

        :param rds_status: The rds_status of this ShowMigrateInfoResponse.
        :type rds_status: str
        """
        self._rds_status = rds_status

    @property
    def rds_instance_name(self):
        r"""Gets the rds_instance_name of this ShowMigrateInfoResponse.

        **参数解释**：  源实例名称。  **取值范围**：  不涉及。

        :return: The rds_instance_name of this ShowMigrateInfoResponse.
        :rtype: str
        """
        return self._rds_instance_name

    @rds_instance_name.setter
    def rds_instance_name(self, rds_instance_name):
        r"""Sets the rds_instance_name of this ShowMigrateInfoResponse.

        **参数解释**：  源实例名称。  **取值范围**：  不涉及。

        :param rds_instance_name: The rds_instance_name of this ShowMigrateInfoResponse.
        :type rds_instance_name: str
        """
        self._rds_instance_name = rds_instance_name

    @property
    def drs_job_id(self):
        r"""Gets the drs_job_id of this ShowMigrateInfoResponse.

        **参数解释**：  迁移任务ID。  **取值范围**：  不涉及。

        :return: The drs_job_id of this ShowMigrateInfoResponse.
        :rtype: str
        """
        return self._drs_job_id

    @drs_job_id.setter
    def drs_job_id(self, drs_job_id):
        r"""Sets the drs_job_id of this ShowMigrateInfoResponse.

        **参数解释**：  迁移任务ID。  **取值范围**：  不涉及。

        :param drs_job_id: The drs_job_id of this ShowMigrateInfoResponse.
        :type drs_job_id: str
        """
        self._drs_job_id = drs_job_id

    @property
    def drs_status(self):
        r"""Gets the drs_status of this ShowMigrateInfoResponse.

        **参数解释**：  迁移任务状态。  **取值范围**：  不涉及。

        :return: The drs_status of this ShowMigrateInfoResponse.
        :rtype: str
        """
        return self._drs_status

    @drs_status.setter
    def drs_status(self, drs_status):
        r"""Sets the drs_status of this ShowMigrateInfoResponse.

        **参数解释**：  迁移任务状态。  **取值范围**：  不涉及。

        :param drs_status: The drs_status of this ShowMigrateInfoResponse.
        :type drs_status: str
        """
        self._drs_status = drs_status

    @property
    def rds_readwrite_mode(self):
        r"""Gets the rds_readwrite_mode of this ShowMigrateInfoResponse.

        **参数解释**：  源实例读写状态。  **取值范围**：  - ON：读写状态。 - OFF：只读状态。

        :return: The rds_readwrite_mode of this ShowMigrateInfoResponse.
        :rtype: str
        """
        return self._rds_readwrite_mode

    @rds_readwrite_mode.setter
    def rds_readwrite_mode(self, rds_readwrite_mode):
        r"""Sets the rds_readwrite_mode of this ShowMigrateInfoResponse.

        **参数解释**：  源实例读写状态。  **取值范围**：  - ON：读写状态。 - OFF：只读状态。

        :param rds_readwrite_mode: The rds_readwrite_mode of this ShowMigrateInfoResponse.
        :type rds_readwrite_mode: str
        """
        self._rds_readwrite_mode = rds_readwrite_mode

    @property
    def taurus_readwrite_mode(self):
        r"""Gets the taurus_readwrite_mode of this ShowMigrateInfoResponse.

        **参数解释**：  目标实例读写状态。  **取值范围**：  - ON：读写状态。 - OFF：只读状态。

        :return: The taurus_readwrite_mode of this ShowMigrateInfoResponse.
        :rtype: str
        """
        return self._taurus_readwrite_mode

    @taurus_readwrite_mode.setter
    def taurus_readwrite_mode(self, taurus_readwrite_mode):
        r"""Sets the taurus_readwrite_mode of this ShowMigrateInfoResponse.

        **参数解释**：  目标实例读写状态。  **取值范围**：  - ON：读写状态。 - OFF：只读状态。

        :param taurus_readwrite_mode: The taurus_readwrite_mode of this ShowMigrateInfoResponse.
        :type taurus_readwrite_mode: str
        """
        self._taurus_readwrite_mode = taurus_readwrite_mode

    @property
    def migration_direction(self):
        r"""Gets the migration_direction of this ShowMigrateInfoResponse.

        **参数解释**：G  迁移方向。  **取值范围**：  - up：源实例到TaurusDB实例。 - down：TaurusDB实例到源实例。

        :return: The migration_direction of this ShowMigrateInfoResponse.
        :rtype: str
        """
        return self._migration_direction

    @migration_direction.setter
    def migration_direction(self, migration_direction):
        r"""Sets the migration_direction of this ShowMigrateInfoResponse.

        **参数解释**：G  迁移方向。  **取值范围**：  - up：源实例到TaurusDB实例。 - down：TaurusDB实例到源实例。

        :param migration_direction: The migration_direction of this ShowMigrateInfoResponse.
        :type migration_direction: str
        """
        self._migration_direction = migration_direction

    def to_dict(self):
        import warnings
        warnings.warn("ShowMigrateInfoResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowMigrateInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
