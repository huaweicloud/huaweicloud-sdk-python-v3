# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CancelColdTableWaitingTask:

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
        'type': 'str'
    }

    attribute_map = {
        'db_name': 'db_name',
        'table_name': 'table_name',
        'partition_name': 'partition_name',
        'type': 'type'
    }

    def __init__(self, db_name=None, table_name=None, partition_name=None, type=None):
        r"""CancelColdTableWaitingTask

        The model defined in huaweicloud sdk

        :param db_name: **参数解释**：  数据库名。  获取方法请参见[查询冷热分离待下发任务列表](https://support.huaweicloud.com/api-taurusdb/ListColdTableWaitingTasks.html)。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type db_name: str
        :param table_name: **参数解释**：  表名。 获取方法请参见[查询冷热分离待下发任务列表](https://support.huaweicloud.com/api-taurusdb/ListColdTableWaitingTasks.html)。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type table_name: str
        :param partition_name: **参数解释**：  分区名。  获取方法请参见[查询冷热分离待下发任务列表](https://support.huaweicloud.com/api-taurusdb/ListColdTableWaitingTasks.html)。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type partition_name: str
        :param type: **参数解释**：  任务类型。  **约束限制**：  不涉及。  **取值范围**：  - waiting_archive：待归档。 - waiting_unarchive：待回迁。  **默认取值**：  不涉及。
        :type type: str
        """
        
        

        self._db_name = None
        self._table_name = None
        self._partition_name = None
        self._type = None
        self.discriminator = None

        self.db_name = db_name
        self.table_name = table_name
        if partition_name is not None:
            self.partition_name = partition_name
        self.type = type

    @property
    def db_name(self):
        r"""Gets the db_name of this CancelColdTableWaitingTask.

        **参数解释**：  数据库名。  获取方法请参见[查询冷热分离待下发任务列表](https://support.huaweicloud.com/api-taurusdb/ListColdTableWaitingTasks.html)。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The db_name of this CancelColdTableWaitingTask.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this CancelColdTableWaitingTask.

        **参数解释**：  数据库名。  获取方法请参见[查询冷热分离待下发任务列表](https://support.huaweicloud.com/api-taurusdb/ListColdTableWaitingTasks.html)。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param db_name: The db_name of this CancelColdTableWaitingTask.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def table_name(self):
        r"""Gets the table_name of this CancelColdTableWaitingTask.

        **参数解释**：  表名。 获取方法请参见[查询冷热分离待下发任务列表](https://support.huaweicloud.com/api-taurusdb/ListColdTableWaitingTasks.html)。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The table_name of this CancelColdTableWaitingTask.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this CancelColdTableWaitingTask.

        **参数解释**：  表名。 获取方法请参见[查询冷热分离待下发任务列表](https://support.huaweicloud.com/api-taurusdb/ListColdTableWaitingTasks.html)。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param table_name: The table_name of this CancelColdTableWaitingTask.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def partition_name(self):
        r"""Gets the partition_name of this CancelColdTableWaitingTask.

        **参数解释**：  分区名。  获取方法请参见[查询冷热分离待下发任务列表](https://support.huaweicloud.com/api-taurusdb/ListColdTableWaitingTasks.html)。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The partition_name of this CancelColdTableWaitingTask.
        :rtype: str
        """
        return self._partition_name

    @partition_name.setter
    def partition_name(self, partition_name):
        r"""Sets the partition_name of this CancelColdTableWaitingTask.

        **参数解释**：  分区名。  获取方法请参见[查询冷热分离待下发任务列表](https://support.huaweicloud.com/api-taurusdb/ListColdTableWaitingTasks.html)。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param partition_name: The partition_name of this CancelColdTableWaitingTask.
        :type partition_name: str
        """
        self._partition_name = partition_name

    @property
    def type(self):
        r"""Gets the type of this CancelColdTableWaitingTask.

        **参数解释**：  任务类型。  **约束限制**：  不涉及。  **取值范围**：  - waiting_archive：待归档。 - waiting_unarchive：待回迁。  **默认取值**：  不涉及。

        :return: The type of this CancelColdTableWaitingTask.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CancelColdTableWaitingTask.

        **参数解释**：  任务类型。  **约束限制**：  不涉及。  **取值范围**：  - waiting_archive：待归档。 - waiting_unarchive：待回迁。  **默认取值**：  不涉及。

        :param type: The type of this CancelColdTableWaitingTask.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, CancelColdTableWaitingTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
