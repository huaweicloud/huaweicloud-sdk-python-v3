# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNodePoolNodesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pool_name': 'str',
        'nodepool_name': 'str',
        '_continue': 'str',
        'limit': 'str'
    }

    attribute_map = {
        'pool_name': 'pool_name',
        'nodepool_name': 'nodepool_name',
        '_continue': 'continue',
        'limit': 'limit'
    }

    def __init__(self, pool_name=None, nodepool_name=None, _continue=None, limit=None):
        r"""ListNodePoolNodesRequest

        The model defined in huaweicloud sdk

        :param pool_name: **参数解释**：资源池名称。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type pool_name: str
        :param nodepool_name: **参数解释**：节点池名称。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type nodepool_name: str
        :param _continue: **参数解释**：分页查询时上一页位置。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type _continue: str
        :param limit: **参数解释**：分页单次查询返回数。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type limit: str
        """
        
        

        self._pool_name = None
        self._nodepool_name = None
        self.__continue = None
        self._limit = None
        self.discriminator = None

        self.pool_name = pool_name
        self.nodepool_name = nodepool_name
        if _continue is not None:
            self._continue = _continue
        if limit is not None:
            self.limit = limit

    @property
    def pool_name(self):
        r"""Gets the pool_name of this ListNodePoolNodesRequest.

        **参数解释**：资源池名称。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The pool_name of this ListNodePoolNodesRequest.
        :rtype: str
        """
        return self._pool_name

    @pool_name.setter
    def pool_name(self, pool_name):
        r"""Sets the pool_name of this ListNodePoolNodesRequest.

        **参数解释**：资源池名称。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param pool_name: The pool_name of this ListNodePoolNodesRequest.
        :type pool_name: str
        """
        self._pool_name = pool_name

    @property
    def nodepool_name(self):
        r"""Gets the nodepool_name of this ListNodePoolNodesRequest.

        **参数解释**：节点池名称。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The nodepool_name of this ListNodePoolNodesRequest.
        :rtype: str
        """
        return self._nodepool_name

    @nodepool_name.setter
    def nodepool_name(self, nodepool_name):
        r"""Sets the nodepool_name of this ListNodePoolNodesRequest.

        **参数解释**：节点池名称。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param nodepool_name: The nodepool_name of this ListNodePoolNodesRequest.
        :type nodepool_name: str
        """
        self._nodepool_name = nodepool_name

    @property
    def _continue(self):
        r"""Gets the _continue of this ListNodePoolNodesRequest.

        **参数解释**：分页查询时上一页位置。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The _continue of this ListNodePoolNodesRequest.
        :rtype: str
        """
        return self.__continue

    @_continue.setter
    def _continue(self, _continue):
        r"""Sets the _continue of this ListNodePoolNodesRequest.

        **参数解释**：分页查询时上一页位置。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param _continue: The _continue of this ListNodePoolNodesRequest.
        :type _continue: str
        """
        self.__continue = _continue

    @property
    def limit(self):
        r"""Gets the limit of this ListNodePoolNodesRequest.

        **参数解释**：分页单次查询返回数。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The limit of this ListNodePoolNodesRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListNodePoolNodesRequest.

        **参数解释**：分页单次查询返回数。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param limit: The limit of this ListNodePoolNodesRequest.
        :type limit: str
        """
        self._limit = limit

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
        if not isinstance(other, ListNodePoolNodesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
