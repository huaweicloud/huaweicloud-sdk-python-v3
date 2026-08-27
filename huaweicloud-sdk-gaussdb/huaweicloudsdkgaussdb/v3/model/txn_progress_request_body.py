# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TxnProgressRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'transaction_ids': 'list[str]',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'action': 'action',
        'transaction_ids': 'transaction_ids',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, action=None, transaction_ids=None, limit=None, offset=None):
        r"""TxnProgressRequestBody

        The model defined in huaweicloud sdk

        :param action: **参数解释**： 指定查询的事务动作类型。  **约束限制**：  不涉及。 **取值范围**：  rollback：查询事务的回滚进度。  **默认取值**：   rollback。
        :type action: str
        :param transaction_ids: **参数解释**：   事务唯一标识列表。   - 列表为空/不传：将执行全量查询，并根据limit和offset分页参数返回当前所有处于执行中的事务信息。   - 列表不为空：将精确匹配并返回transaction_ids中指定的事务信息，此时分页参数（limit/offset）无效。 **约束限制**：   单次查询最多支持100个事务ID。 **取值范围**：   符合事务ID格式的字符串列表。
        :type transaction_ids: list[str]
        :param limit: **参数解释**：  查询记录数。  **约束限制**：  必须为整数，不能为负数。  **取值范围**：  1-100。  **默认取值**：  100。
        :type limit: int
        :param offset: **参数解释**：    索引位置，偏移量。从第一条数据偏移offset条数据后开始查询。    **约束限制**：    必须为整数，不能为负数。    **取值范围**：    ≥0。  **默认取值**：    0。
        :type offset: int
        """
        
        

        self._action = None
        self._transaction_ids = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.action = action
        if transaction_ids is not None:
            self.transaction_ids = transaction_ids
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def action(self):
        r"""Gets the action of this TxnProgressRequestBody.

        **参数解释**： 指定查询的事务动作类型。  **约束限制**：  不涉及。 **取值范围**：  rollback：查询事务的回滚进度。  **默认取值**：   rollback。

        :return: The action of this TxnProgressRequestBody.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this TxnProgressRequestBody.

        **参数解释**： 指定查询的事务动作类型。  **约束限制**：  不涉及。 **取值范围**：  rollback：查询事务的回滚进度。  **默认取值**：   rollback。

        :param action: The action of this TxnProgressRequestBody.
        :type action: str
        """
        self._action = action

    @property
    def transaction_ids(self):
        r"""Gets the transaction_ids of this TxnProgressRequestBody.

        **参数解释**：   事务唯一标识列表。   - 列表为空/不传：将执行全量查询，并根据limit和offset分页参数返回当前所有处于执行中的事务信息。   - 列表不为空：将精确匹配并返回transaction_ids中指定的事务信息，此时分页参数（limit/offset）无效。 **约束限制**：   单次查询最多支持100个事务ID。 **取值范围**：   符合事务ID格式的字符串列表。

        :return: The transaction_ids of this TxnProgressRequestBody.
        :rtype: list[str]
        """
        return self._transaction_ids

    @transaction_ids.setter
    def transaction_ids(self, transaction_ids):
        r"""Sets the transaction_ids of this TxnProgressRequestBody.

        **参数解释**：   事务唯一标识列表。   - 列表为空/不传：将执行全量查询，并根据limit和offset分页参数返回当前所有处于执行中的事务信息。   - 列表不为空：将精确匹配并返回transaction_ids中指定的事务信息，此时分页参数（limit/offset）无效。 **约束限制**：   单次查询最多支持100个事务ID。 **取值范围**：   符合事务ID格式的字符串列表。

        :param transaction_ids: The transaction_ids of this TxnProgressRequestBody.
        :type transaction_ids: list[str]
        """
        self._transaction_ids = transaction_ids

    @property
    def limit(self):
        r"""Gets the limit of this TxnProgressRequestBody.

        **参数解释**：  查询记录数。  **约束限制**：  必须为整数，不能为负数。  **取值范围**：  1-100。  **默认取值**：  100。

        :return: The limit of this TxnProgressRequestBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this TxnProgressRequestBody.

        **参数解释**：  查询记录数。  **约束限制**：  必须为整数，不能为负数。  **取值范围**：  1-100。  **默认取值**：  100。

        :param limit: The limit of this TxnProgressRequestBody.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this TxnProgressRequestBody.

        **参数解释**：    索引位置，偏移量。从第一条数据偏移offset条数据后开始查询。    **约束限制**：    必须为整数，不能为负数。    **取值范围**：    ≥0。  **默认取值**：    0。

        :return: The offset of this TxnProgressRequestBody.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this TxnProgressRequestBody.

        **参数解释**：    索引位置，偏移量。从第一条数据偏移offset条数据后开始查询。    **约束限制**：    必须为整数，不能为负数。    **取值范围**：    ≥0。  **默认取值**：    0。

        :param offset: The offset of this TxnProgressRequestBody.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, TxnProgressRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
