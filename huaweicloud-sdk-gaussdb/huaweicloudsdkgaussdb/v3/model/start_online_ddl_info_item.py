# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StartOnlineDDLInfoItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sql': 'str'
    }

    attribute_map = {
        'sql': 'sql'
    }

    def __init__(self, sql=None):
        r"""StartOnlineDDLInfoItem

        The model defined in huaweicloud sdk

        :param sql: **参数解释**：  无锁变更的具体执行SQL。  **约束限制**:  满足ALTER TABLE Statement语法形式，多条SQL需要以英文分号隔开。  **取值范围**：   不涉及。  **默认取值**：   不涉及。
        :type sql: str
        """
        
        

        self._sql = None
        self.discriminator = None

        self.sql = sql

    @property
    def sql(self):
        r"""Gets the sql of this StartOnlineDDLInfoItem.

        **参数解释**：  无锁变更的具体执行SQL。  **约束限制**:  满足ALTER TABLE Statement语法形式，多条SQL需要以英文分号隔开。  **取值范围**：   不涉及。  **默认取值**：   不涉及。

        :return: The sql of this StartOnlineDDLInfoItem.
        :rtype: str
        """
        return self._sql

    @sql.setter
    def sql(self, sql):
        r"""Sets the sql of this StartOnlineDDLInfoItem.

        **参数解释**：  无锁变更的具体执行SQL。  **约束限制**:  满足ALTER TABLE Statement语法形式，多条SQL需要以英文分号隔开。  **取值范围**：   不涉及。  **默认取值**：   不涉及。

        :param sql: The sql of this StartOnlineDDLInfoItem.
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
        if not isinstance(other, StartOnlineDDLInfoItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
