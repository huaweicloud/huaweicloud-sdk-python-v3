# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDeadLockTopologyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'meta': 'ShowDeadLockTopologyGraphRespMeta',
        'transactions': 'list[ShowDeadLockTopologyGraphRespTransactions]',
        'locks': 'list[ShowDeadLockTopologyGraphRespLocks]',
        'edges': 'list[ShowDeadLockTopologyGraphRespEdges]',
        'conflict_groups': 'list[ShowDeadLockTopologyGraphRespConflictGroups]'
    }

    attribute_map = {
        'meta': 'meta',
        'transactions': 'transactions',
        'locks': 'locks',
        'edges': 'edges',
        'conflict_groups': 'conflict_groups'
    }

    def __init__(self, meta=None, transactions=None, locks=None, edges=None, conflict_groups=None):
        r"""ShowDeadLockTopologyResponse

        The model defined in huaweicloud sdk

        :param meta: 
        :type meta: :class:`huaweicloudsdkdas.v3.ShowDeadLockTopologyGraphRespMeta`
        :param transactions: 事务节点
        :type transactions: list[:class:`huaweicloudsdkdas.v3.ShowDeadLockTopologyGraphRespTransactions`]
        :param locks: 锁节点
        :type locks: list[:class:`huaweicloudsdkdas.v3.ShowDeadLockTopologyGraphRespLocks`]
        :param edges: 边，连接节点表达关系
        :type edges: list[:class:`huaweicloudsdkdas.v3.ShowDeadLockTopologyGraphRespEdges`]
        :param conflict_groups: 冲突组，每条 conflicts_with 边对应一个
        :type conflict_groups: list[:class:`huaweicloudsdkdas.v3.ShowDeadLockTopologyGraphRespConflictGroups`]
        """
        
        super().__init__()

        self._meta = None
        self._transactions = None
        self._locks = None
        self._edges = None
        self._conflict_groups = None
        self.discriminator = None

        if meta is not None:
            self.meta = meta
        if transactions is not None:
            self.transactions = transactions
        if locks is not None:
            self.locks = locks
        if edges is not None:
            self.edges = edges
        if conflict_groups is not None:
            self.conflict_groups = conflict_groups

    @property
    def meta(self):
        r"""Gets the meta of this ShowDeadLockTopologyResponse.

        :return: The meta of this ShowDeadLockTopologyResponse.
        :rtype: :class:`huaweicloudsdkdas.v3.ShowDeadLockTopologyGraphRespMeta`
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        r"""Sets the meta of this ShowDeadLockTopologyResponse.

        :param meta: The meta of this ShowDeadLockTopologyResponse.
        :type meta: :class:`huaweicloudsdkdas.v3.ShowDeadLockTopologyGraphRespMeta`
        """
        self._meta = meta

    @property
    def transactions(self):
        r"""Gets the transactions of this ShowDeadLockTopologyResponse.

        事务节点

        :return: The transactions of this ShowDeadLockTopologyResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.ShowDeadLockTopologyGraphRespTransactions`]
        """
        return self._transactions

    @transactions.setter
    def transactions(self, transactions):
        r"""Sets the transactions of this ShowDeadLockTopologyResponse.

        事务节点

        :param transactions: The transactions of this ShowDeadLockTopologyResponse.
        :type transactions: list[:class:`huaweicloudsdkdas.v3.ShowDeadLockTopologyGraphRespTransactions`]
        """
        self._transactions = transactions

    @property
    def locks(self):
        r"""Gets the locks of this ShowDeadLockTopologyResponse.

        锁节点

        :return: The locks of this ShowDeadLockTopologyResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.ShowDeadLockTopologyGraphRespLocks`]
        """
        return self._locks

    @locks.setter
    def locks(self, locks):
        r"""Sets the locks of this ShowDeadLockTopologyResponse.

        锁节点

        :param locks: The locks of this ShowDeadLockTopologyResponse.
        :type locks: list[:class:`huaweicloudsdkdas.v3.ShowDeadLockTopologyGraphRespLocks`]
        """
        self._locks = locks

    @property
    def edges(self):
        r"""Gets the edges of this ShowDeadLockTopologyResponse.

        边，连接节点表达关系

        :return: The edges of this ShowDeadLockTopologyResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.ShowDeadLockTopologyGraphRespEdges`]
        """
        return self._edges

    @edges.setter
    def edges(self, edges):
        r"""Sets the edges of this ShowDeadLockTopologyResponse.

        边，连接节点表达关系

        :param edges: The edges of this ShowDeadLockTopologyResponse.
        :type edges: list[:class:`huaweicloudsdkdas.v3.ShowDeadLockTopologyGraphRespEdges`]
        """
        self._edges = edges

    @property
    def conflict_groups(self):
        r"""Gets the conflict_groups of this ShowDeadLockTopologyResponse.

        冲突组，每条 conflicts_with 边对应一个

        :return: The conflict_groups of this ShowDeadLockTopologyResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.ShowDeadLockTopologyGraphRespConflictGroups`]
        """
        return self._conflict_groups

    @conflict_groups.setter
    def conflict_groups(self, conflict_groups):
        r"""Sets the conflict_groups of this ShowDeadLockTopologyResponse.

        冲突组，每条 conflicts_with 边对应一个

        :param conflict_groups: The conflict_groups of this ShowDeadLockTopologyResponse.
        :type conflict_groups: list[:class:`huaweicloudsdkdas.v3.ShowDeadLockTopologyGraphRespConflictGroups`]
        """
        self._conflict_groups = conflict_groups

    def to_dict(self):
        import warnings
        warnings.warn("ShowDeadLockTopologyResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowDeadLockTopologyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
