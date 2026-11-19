# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ColdTableWaitingTask:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'db_name': 'str',
        'table_name': 'str',
        'partition_name': 'str',
        'status': 'str',
        'create_at': 'int'
    }

    attribute_map = {
        'db_name': 'db_name',
        'table_name': 'table_name',
        'partition_name': 'partition_name',
        'status': 'status',
        'create_at': 'create_at'
    }

    def __init__(self, db_name=None, table_name=None, partition_name=None, status=None, create_at=None):
        r"""ColdTableWaitingTask

        The model defined in huaweicloud sdk

        :param db_name: **参数解释**：  数据库名。  **取值范围**：  不涉及。
        :type db_name: str
        :param table_name: **参数解释**：  表名。  **取值范围**：  不涉及。
        :type table_name: str
        :param partition_name: **参数解释**：  分区名。  **取值范围**：  不涉及。
        :type partition_name: str
        :param status: **参数解释**：  任务状态。  **取值范围**：  - waiting_archive：等待归档。 - waiting_unarchive：等待回迁。
        :type status: str
        :param create_at: **参数解释**：  任务创建时间，13位毫秒级时间戳。  **取值范围**：  非负整数。
        :type create_at: int
        """
        
        

        self._db_name = None
        self._table_name = None
        self._partition_name = None
        self._status = None
        self._create_at = None
        self.discriminator = None

        if db_name is not None:
            self.db_name = db_name
        if table_name is not None:
            self.table_name = table_name
        if partition_name is not None:
            self.partition_name = partition_name
        if status is not None:
            self.status = status
        if create_at is not None:
            self.create_at = create_at

    @property
    def db_name(self):
        r"""Gets the db_name of this ColdTableWaitingTask.

        **参数解释**：  数据库名。  **取值范围**：  不涉及。

        :return: The db_name of this ColdTableWaitingTask.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this ColdTableWaitingTask.

        **参数解释**：  数据库名。  **取值范围**：  不涉及。

        :param db_name: The db_name of this ColdTableWaitingTask.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def table_name(self):
        r"""Gets the table_name of this ColdTableWaitingTask.

        **参数解释**：  表名。  **取值范围**：  不涉及。

        :return: The table_name of this ColdTableWaitingTask.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this ColdTableWaitingTask.

        **参数解释**：  表名。  **取值范围**：  不涉及。

        :param table_name: The table_name of this ColdTableWaitingTask.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def partition_name(self):
        r"""Gets the partition_name of this ColdTableWaitingTask.

        **参数解释**：  分区名。  **取值范围**：  不涉及。

        :return: The partition_name of this ColdTableWaitingTask.
        :rtype: str
        """
        return self._partition_name

    @partition_name.setter
    def partition_name(self, partition_name):
        r"""Sets the partition_name of this ColdTableWaitingTask.

        **参数解释**：  分区名。  **取值范围**：  不涉及。

        :param partition_name: The partition_name of this ColdTableWaitingTask.
        :type partition_name: str
        """
        self._partition_name = partition_name

    @property
    def status(self):
        r"""Gets the status of this ColdTableWaitingTask.

        **参数解释**：  任务状态。  **取值范围**：  - waiting_archive：等待归档。 - waiting_unarchive：等待回迁。

        :return: The status of this ColdTableWaitingTask.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ColdTableWaitingTask.

        **参数解释**：  任务状态。  **取值范围**：  - waiting_archive：等待归档。 - waiting_unarchive：等待回迁。

        :param status: The status of this ColdTableWaitingTask.
        :type status: str
        """
        self._status = status

    @property
    def create_at(self):
        r"""Gets the create_at of this ColdTableWaitingTask.

        **参数解释**：  任务创建时间，13位毫秒级时间戳。  **取值范围**：  非负整数。

        :return: The create_at of this ColdTableWaitingTask.
        :rtype: int
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this ColdTableWaitingTask.

        **参数解释**：  任务创建时间，13位毫秒级时间戳。  **取值范围**：  非负整数。

        :param create_at: The create_at of this ColdTableWaitingTask.
        :type create_at: int
        """
        self._create_at = create_at

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
        if not isinstance(other, ColdTableWaitingTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
