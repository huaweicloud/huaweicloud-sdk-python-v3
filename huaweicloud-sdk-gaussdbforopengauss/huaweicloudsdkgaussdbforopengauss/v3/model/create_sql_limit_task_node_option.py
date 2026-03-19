# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSqlLimitTaskNodeOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_id': 'str',
        'sql_ids': 'list[str]'
    }

    attribute_map = {
        'node_id': 'node_id',
        'sql_ids': 'sql_ids'
    }

    def __init__(self, node_id=None, sql_ids=None):
        r"""CreateSqlLimitTaskNodeOption

        The model defined in huaweicloud sdk

        :param node_id: **参数解释**: 节点ID。 **约束限制**: 必须是当前实例的某一个节点ID。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type node_id: str
        :param sql_ids: **参数解释**: 该节点执行的SQL语句ID。 **约束限制**: 每个节点最多可以下发的SQL ID数量不可以超过10。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type sql_ids: list[str]
        """
        
        

        self._node_id = None
        self._sql_ids = None
        self.discriminator = None

        self.node_id = node_id
        self.sql_ids = sql_ids

    @property
    def node_id(self):
        r"""Gets the node_id of this CreateSqlLimitTaskNodeOption.

        **参数解释**: 节点ID。 **约束限制**: 必须是当前实例的某一个节点ID。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The node_id of this CreateSqlLimitTaskNodeOption.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this CreateSqlLimitTaskNodeOption.

        **参数解释**: 节点ID。 **约束限制**: 必须是当前实例的某一个节点ID。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param node_id: The node_id of this CreateSqlLimitTaskNodeOption.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def sql_ids(self):
        r"""Gets the sql_ids of this CreateSqlLimitTaskNodeOption.

        **参数解释**: 该节点执行的SQL语句ID。 **约束限制**: 每个节点最多可以下发的SQL ID数量不可以超过10。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The sql_ids of this CreateSqlLimitTaskNodeOption.
        :rtype: list[str]
        """
        return self._sql_ids

    @sql_ids.setter
    def sql_ids(self, sql_ids):
        r"""Sets the sql_ids of this CreateSqlLimitTaskNodeOption.

        **参数解释**: 该节点执行的SQL语句ID。 **约束限制**: 每个节点最多可以下发的SQL ID数量不可以超过10。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param sql_ids: The sql_ids of this CreateSqlLimitTaskNodeOption.
        :type sql_ids: list[str]
        """
        self._sql_ids = sql_ids

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
        if not isinstance(other, CreateSqlLimitTaskNodeOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
