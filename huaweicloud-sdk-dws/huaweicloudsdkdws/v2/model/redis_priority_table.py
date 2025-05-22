# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RedisPriorityTable:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'schema_name': 'str',
        'id': 'int',
        'table_name': 'str',
        'redis_order': 'int'
    }

    attribute_map = {
        'schema_name': 'schema_name',
        'id': 'id',
        'table_name': 'table_name',
        'redis_order': 'redis_order'
    }

    def __init__(self, schema_name=None, id=None, table_name=None, redis_order=None):
        r"""RedisPriorityTable

        The model defined in huaweicloud sdk

        :param schema_name: **参数解释**： 模式名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type schema_name: str
        :param id: **参数解释**： 表ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type id: int
        :param table_name: **参数解释**： 表名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type table_name: str
        :param redis_order: **参数解释**： 优先级。 **约束限制**： 不涉及。 **取值范围**： 1~1024 **默认取值**： 不涉及。
        :type redis_order: int
        """
        
        

        self._schema_name = None
        self._id = None
        self._table_name = None
        self._redis_order = None
        self.discriminator = None

        if schema_name is not None:
            self.schema_name = schema_name
        if id is not None:
            self.id = id
        if table_name is not None:
            self.table_name = table_name
        if redis_order is not None:
            self.redis_order = redis_order

    @property
    def schema_name(self):
        r"""Gets the schema_name of this RedisPriorityTable.

        **参数解释**： 模式名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The schema_name of this RedisPriorityTable.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        r"""Sets the schema_name of this RedisPriorityTable.

        **参数解释**： 模式名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param schema_name: The schema_name of this RedisPriorityTable.
        :type schema_name: str
        """
        self._schema_name = schema_name

    @property
    def id(self):
        r"""Gets the id of this RedisPriorityTable.

        **参数解释**： 表ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The id of this RedisPriorityTable.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this RedisPriorityTable.

        **参数解释**： 表ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param id: The id of this RedisPriorityTable.
        :type id: int
        """
        self._id = id

    @property
    def table_name(self):
        r"""Gets the table_name of this RedisPriorityTable.

        **参数解释**： 表名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The table_name of this RedisPriorityTable.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this RedisPriorityTable.

        **参数解释**： 表名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param table_name: The table_name of this RedisPriorityTable.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def redis_order(self):
        r"""Gets the redis_order of this RedisPriorityTable.

        **参数解释**： 优先级。 **约束限制**： 不涉及。 **取值范围**： 1~1024 **默认取值**： 不涉及。

        :return: The redis_order of this RedisPriorityTable.
        :rtype: int
        """
        return self._redis_order

    @redis_order.setter
    def redis_order(self, redis_order):
        r"""Sets the redis_order of this RedisPriorityTable.

        **参数解释**： 优先级。 **约束限制**： 不涉及。 **取值范围**： 1~1024 **默认取值**： 不涉及。

        :param redis_order: The redis_order of this RedisPriorityTable.
        :type redis_order: int
        """
        self._redis_order = redis_order

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RedisPriorityTable):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
