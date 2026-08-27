# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OnlineDDLInfoItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'table': 'str',
        'sql': 'str'
    }

    attribute_map = {
        'table': 'table',
        'sql': 'sql'
    }

    def __init__(self, table=None, sql=None):
        r"""OnlineDDLInfoItem

        The model defined in huaweicloud sdk

        :param table: **参数解释**：   无锁变更的目标表。  **取值范围**：  不涉及。  
        :type table: str
        :param sql: **参数解释**：  无锁变更的具体执行SQL。  **取值范围**：   不涉及。
        :type sql: str
        """
        
        

        self._table = None
        self._sql = None
        self.discriminator = None

        if table is not None:
            self.table = table
        if sql is not None:
            self.sql = sql

    @property
    def table(self):
        r"""Gets the table of this OnlineDDLInfoItem.

        **参数解释**：   无锁变更的目标表。  **取值范围**：  不涉及。  

        :return: The table of this OnlineDDLInfoItem.
        :rtype: str
        """
        return self._table

    @table.setter
    def table(self, table):
        r"""Sets the table of this OnlineDDLInfoItem.

        **参数解释**：   无锁变更的目标表。  **取值范围**：  不涉及。  

        :param table: The table of this OnlineDDLInfoItem.
        :type table: str
        """
        self._table = table

    @property
    def sql(self):
        r"""Gets the sql of this OnlineDDLInfoItem.

        **参数解释**：  无锁变更的具体执行SQL。  **取值范围**：   不涉及。

        :return: The sql of this OnlineDDLInfoItem.
        :rtype: str
        """
        return self._sql

    @sql.setter
    def sql(self, sql):
        r"""Sets the sql of this OnlineDDLInfoItem.

        **参数解释**：  无锁变更的具体执行SQL。  **取值范围**：   不涉及。

        :param sql: The sql of this OnlineDDLInfoItem.
        :type sql: str
        """
        self._sql = sql

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
        if not isinstance(other, OnlineDDLInfoItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
