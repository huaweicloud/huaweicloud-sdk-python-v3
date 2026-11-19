# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RetainedBackupInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'backup_id': 'str',
        'instance_id': 'str',
        'status': 'str',
        'backup_name': 'str',
        'size': 'int',
        'begin_time': 'str',
        'end_time': 'str',
        'backup_type': 'str',
        'backup_level': 'str'
    }

    attribute_map = {
        'backup_id': 'backup_id',
        'instance_id': 'instance_id',
        'status': 'status',
        'backup_name': 'backup_name',
        'size': 'size',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'backup_type': 'backup_type',
        'backup_level': 'backup_level'
    }

    def __init__(self, backup_id=None, instance_id=None, status=None, backup_name=None, size=None, begin_time=None, end_time=None, backup_type=None, backup_level=None):
        r"""RetainedBackupInfo

        The model defined in huaweicloud sdk

        :param backup_id: **参数解释**：  备份ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type backup_id: str
        :param instance_id: **参数解释**：  源实例ID（已释放实例）。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type instance_id: str
        :param status: **参数解释**：  备份状态。  **约束限制**：  不涉及。  **取值范围**：  Active：可用。  **默认取值**：  不涉及。
        :type status: str
        :param backup_name: **参数解释**：  备份名称。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type backup_name: str
        :param size: **参数解释**：  备份大小，单位MB。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type size: int
        :param begin_time: **参数解释**：  备份开始时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type begin_time: str
        :param end_time: **参数解释**：  备份结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”，且大于备份开始时间。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type end_time: str
        :param backup_type: **参数解释**：  备份类型。  **约束限制**：  不涉及。  **取值范围**：  - auto：自动全量备份。 - manual：手动全量备份。 - differential：差量备份。 - sparse：稀疏备份。 - recycle: 回收站备份。  **默认取值**：  不涉及。
        :type backup_type: str
        :param backup_level: **参数解释**：  备份级别，即备份位置。  **约束限制**：  不涉及。  **取值范围**：  - 1：一级备份。 - 2：二级备份。  **默认取值**：  不涉及。
        :type backup_level: str
        """
        
        

        self._backup_id = None
        self._instance_id = None
        self._status = None
        self._backup_name = None
        self._size = None
        self._begin_time = None
        self._end_time = None
        self._backup_type = None
        self._backup_level = None
        self.discriminator = None

        if backup_id is not None:
            self.backup_id = backup_id
        if instance_id is not None:
            self.instance_id = instance_id
        if status is not None:
            self.status = status
        if backup_name is not None:
            self.backup_name = backup_name
        if size is not None:
            self.size = size
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if backup_type is not None:
            self.backup_type = backup_type
        if backup_level is not None:
            self.backup_level = backup_level

    @property
    def backup_id(self):
        r"""Gets the backup_id of this RetainedBackupInfo.

        **参数解释**：  备份ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The backup_id of this RetainedBackupInfo.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        r"""Sets the backup_id of this RetainedBackupInfo.

        **参数解释**：  备份ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param backup_id: The backup_id of this RetainedBackupInfo.
        :type backup_id: str
        """
        self._backup_id = backup_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this RetainedBackupInfo.

        **参数解释**：  源实例ID（已释放实例）。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The instance_id of this RetainedBackupInfo.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this RetainedBackupInfo.

        **参数解释**：  源实例ID（已释放实例）。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param instance_id: The instance_id of this RetainedBackupInfo.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def status(self):
        r"""Gets the status of this RetainedBackupInfo.

        **参数解释**：  备份状态。  **约束限制**：  不涉及。  **取值范围**：  Active：可用。  **默认取值**：  不涉及。

        :return: The status of this RetainedBackupInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this RetainedBackupInfo.

        **参数解释**：  备份状态。  **约束限制**：  不涉及。  **取值范围**：  Active：可用。  **默认取值**：  不涉及。

        :param status: The status of this RetainedBackupInfo.
        :type status: str
        """
        self._status = status

    @property
    def backup_name(self):
        r"""Gets the backup_name of this RetainedBackupInfo.

        **参数解释**：  备份名称。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The backup_name of this RetainedBackupInfo.
        :rtype: str
        """
        return self._backup_name

    @backup_name.setter
    def backup_name(self, backup_name):
        r"""Sets the backup_name of this RetainedBackupInfo.

        **参数解释**：  备份名称。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param backup_name: The backup_name of this RetainedBackupInfo.
        :type backup_name: str
        """
        self._backup_name = backup_name

    @property
    def size(self):
        r"""Gets the size of this RetainedBackupInfo.

        **参数解释**：  备份大小，单位MB。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The size of this RetainedBackupInfo.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this RetainedBackupInfo.

        **参数解释**：  备份大小，单位MB。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param size: The size of this RetainedBackupInfo.
        :type size: int
        """
        self._size = size

    @property
    def begin_time(self):
        r"""Gets the begin_time of this RetainedBackupInfo.

        **参数解释**：  备份开始时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The begin_time of this RetainedBackupInfo.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this RetainedBackupInfo.

        **参数解释**：  备份开始时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param begin_time: The begin_time of this RetainedBackupInfo.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this RetainedBackupInfo.

        **参数解释**：  备份结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”，且大于备份开始时间。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The end_time of this RetainedBackupInfo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this RetainedBackupInfo.

        **参数解释**：  备份结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”，且大于备份开始时间。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param end_time: The end_time of this RetainedBackupInfo.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def backup_type(self):
        r"""Gets the backup_type of this RetainedBackupInfo.

        **参数解释**：  备份类型。  **约束限制**：  不涉及。  **取值范围**：  - auto：自动全量备份。 - manual：手动全量备份。 - differential：差量备份。 - sparse：稀疏备份。 - recycle: 回收站备份。  **默认取值**：  不涉及。

        :return: The backup_type of this RetainedBackupInfo.
        :rtype: str
        """
        return self._backup_type

    @backup_type.setter
    def backup_type(self, backup_type):
        r"""Sets the backup_type of this RetainedBackupInfo.

        **参数解释**：  备份类型。  **约束限制**：  不涉及。  **取值范围**：  - auto：自动全量备份。 - manual：手动全量备份。 - differential：差量备份。 - sparse：稀疏备份。 - recycle: 回收站备份。  **默认取值**：  不涉及。

        :param backup_type: The backup_type of this RetainedBackupInfo.
        :type backup_type: str
        """
        self._backup_type = backup_type

    @property
    def backup_level(self):
        r"""Gets the backup_level of this RetainedBackupInfo.

        **参数解释**：  备份级别，即备份位置。  **约束限制**：  不涉及。  **取值范围**：  - 1：一级备份。 - 2：二级备份。  **默认取值**：  不涉及。

        :return: The backup_level of this RetainedBackupInfo.
        :rtype: str
        """
        return self._backup_level

    @backup_level.setter
    def backup_level(self, backup_level):
        r"""Sets the backup_level of this RetainedBackupInfo.

        **参数解释**：  备份级别，即备份位置。  **约束限制**：  不涉及。  **取值范围**：  - 1：一级备份。 - 2：二级备份。  **默认取值**：  不涉及。

        :param backup_level: The backup_level of this RetainedBackupInfo.
        :type backup_level: str
        """
        self._backup_level = backup_level

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
        if not isinstance(other, RetainedBackupInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
