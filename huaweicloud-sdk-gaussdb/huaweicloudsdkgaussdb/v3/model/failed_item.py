# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FailedItem:

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
        'reason': 'str'
    }

    attribute_map = {
        'db_name': 'db_name',
        'table_name': 'table_name',
        'partition_name': 'partition_name',
        'reason': 'reason'
    }

    def __init__(self, db_name=None, table_name=None, partition_name=None, reason=None):
        r"""FailedItem

        The model defined in huaweicloud sdk

        :param db_name: **参数解释**：  数据库名。  **取值范围**：  不涉及。
        :type db_name: str
        :param table_name: **参数解释**：  表名。  **取值范围**：  不涉及。
        :type table_name: str
        :param partition_name: **参数解释**：  分区名。  **取值范围**：  不涉及。
        :type partition_name: str
        :param reason: **参数解释**：  失败原因。  **取值范围**：  - restricted：内核限制无法下发。 - incorrect：库名、表名、分区名有误。 - duplicate：该表正在进行其他操作（待归档、待回迁、归档中、回迁中、已归档、已回迁）。
        :type reason: str
        """
        
        

        self._db_name = None
        self._table_name = None
        self._partition_name = None
        self._reason = None
        self.discriminator = None

        self.db_name = db_name
        self.table_name = table_name
        if partition_name is not None:
            self.partition_name = partition_name
        self.reason = reason

    @property
    def db_name(self):
        r"""Gets the db_name of this FailedItem.

        **参数解释**：  数据库名。  **取值范围**：  不涉及。

        :return: The db_name of this FailedItem.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this FailedItem.

        **参数解释**：  数据库名。  **取值范围**：  不涉及。

        :param db_name: The db_name of this FailedItem.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def table_name(self):
        r"""Gets the table_name of this FailedItem.

        **参数解释**：  表名。  **取值范围**：  不涉及。

        :return: The table_name of this FailedItem.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this FailedItem.

        **参数解释**：  表名。  **取值范围**：  不涉及。

        :param table_name: The table_name of this FailedItem.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def partition_name(self):
        r"""Gets the partition_name of this FailedItem.

        **参数解释**：  分区名。  **取值范围**：  不涉及。

        :return: The partition_name of this FailedItem.
        :rtype: str
        """
        return self._partition_name

    @partition_name.setter
    def partition_name(self, partition_name):
        r"""Sets the partition_name of this FailedItem.

        **参数解释**：  分区名。  **取值范围**：  不涉及。

        :param partition_name: The partition_name of this FailedItem.
        :type partition_name: str
        """
        self._partition_name = partition_name

    @property
    def reason(self):
        r"""Gets the reason of this FailedItem.

        **参数解释**：  失败原因。  **取值范围**：  - restricted：内核限制无法下发。 - incorrect：库名、表名、分区名有误。 - duplicate：该表正在进行其他操作（待归档、待回迁、归档中、回迁中、已归档、已回迁）。

        :return: The reason of this FailedItem.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this FailedItem.

        **参数解释**：  失败原因。  **取值范围**：  - restricted：内核限制无法下发。 - incorrect：库名、表名、分区名有误。 - duplicate：该表正在进行其他操作（待归档、待回迁、归档中、回迁中、已归档、已回迁）。

        :param reason: The reason of this FailedItem.
        :type reason: str
        """
        self._reason = reason

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
        if not isinstance(other, FailedItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
