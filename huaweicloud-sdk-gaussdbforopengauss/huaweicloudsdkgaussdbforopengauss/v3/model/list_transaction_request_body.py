# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTransactionRequestBody:

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
        'component_id': 'str',
        'limit': 'int',
        'offset': 'int',
        'transaction_query_option': 'ListTransactionRequestBodyTransactionQueryOption'
    }

    attribute_map = {
        'node_id': 'node_id',
        'component_id': 'component_id',
        'limit': 'limit',
        'offset': 'offset',
        'transaction_query_option': 'transaction_query_option'
    }

    def __init__(self, node_id=None, component_id=None, limit=None, offset=None, transaction_query_option=None):
        r"""ListTransactionRequestBody

        The model defined in huaweicloud sdk

        :param node_id: **参数解释**: 节点ID，仅支持非日志类型的CN或DN节点。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type node_id: str
        :param component_id: **参数解释**: 组件ID，仅支持非日志类型的CN或DN节点。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type component_id: str
        :param limit: **参数解释**: 查询结果的事务最大个数。 **约束限制**: 不涉及。 **取值范围**: [1，100]。 **默认取值**: 默认为10。
        :type limit: int
        :param offset: **参数解释**: 查询结果的事务起始页码。 **约束限制**: 不涉及。 **取值范围**: [0，2^31-1]。 **默认取值**: 默认为0（偏移0条数据，表示从第一条数据开始查询）。
        :type offset: int
        :param transaction_query_option: 
        :type transaction_query_option: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListTransactionRequestBodyTransactionQueryOption`
        """
        
        

        self._node_id = None
        self._component_id = None
        self._limit = None
        self._offset = None
        self._transaction_query_option = None
        self.discriminator = None

        self.node_id = node_id
        self.component_id = component_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if transaction_query_option is not None:
            self.transaction_query_option = transaction_query_option

    @property
    def node_id(self):
        r"""Gets the node_id of this ListTransactionRequestBody.

        **参数解释**: 节点ID，仅支持非日志类型的CN或DN节点。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The node_id of this ListTransactionRequestBody.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this ListTransactionRequestBody.

        **参数解释**: 节点ID，仅支持非日志类型的CN或DN节点。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param node_id: The node_id of this ListTransactionRequestBody.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def component_id(self):
        r"""Gets the component_id of this ListTransactionRequestBody.

        **参数解释**: 组件ID，仅支持非日志类型的CN或DN节点。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The component_id of this ListTransactionRequestBody.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        r"""Sets the component_id of this ListTransactionRequestBody.

        **参数解释**: 组件ID，仅支持非日志类型的CN或DN节点。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param component_id: The component_id of this ListTransactionRequestBody.
        :type component_id: str
        """
        self._component_id = component_id

    @property
    def limit(self):
        r"""Gets the limit of this ListTransactionRequestBody.

        **参数解释**: 查询结果的事务最大个数。 **约束限制**: 不涉及。 **取值范围**: [1，100]。 **默认取值**: 默认为10。

        :return: The limit of this ListTransactionRequestBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListTransactionRequestBody.

        **参数解释**: 查询结果的事务最大个数。 **约束限制**: 不涉及。 **取值范围**: [1，100]。 **默认取值**: 默认为10。

        :param limit: The limit of this ListTransactionRequestBody.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListTransactionRequestBody.

        **参数解释**: 查询结果的事务起始页码。 **约束限制**: 不涉及。 **取值范围**: [0，2^31-1]。 **默认取值**: 默认为0（偏移0条数据，表示从第一条数据开始查询）。

        :return: The offset of this ListTransactionRequestBody.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListTransactionRequestBody.

        **参数解释**: 查询结果的事务起始页码。 **约束限制**: 不涉及。 **取值范围**: [0，2^31-1]。 **默认取值**: 默认为0（偏移0条数据，表示从第一条数据开始查询）。

        :param offset: The offset of this ListTransactionRequestBody.
        :type offset: int
        """
        self._offset = offset

    @property
    def transaction_query_option(self):
        r"""Gets the transaction_query_option of this ListTransactionRequestBody.

        :return: The transaction_query_option of this ListTransactionRequestBody.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListTransactionRequestBodyTransactionQueryOption`
        """
        return self._transaction_query_option

    @transaction_query_option.setter
    def transaction_query_option(self, transaction_query_option):
        r"""Sets the transaction_query_option of this ListTransactionRequestBody.

        :param transaction_query_option: The transaction_query_option of this ListTransactionRequestBody.
        :type transaction_query_option: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListTransactionRequestBodyTransactionQueryOption`
        """
        self._transaction_query_option = transaction_query_option

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
        if not isinstance(other, ListTransactionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
