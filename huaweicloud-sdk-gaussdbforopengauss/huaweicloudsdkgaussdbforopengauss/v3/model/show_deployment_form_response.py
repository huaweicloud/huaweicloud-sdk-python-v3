# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDeploymentFormResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'initial_node_num': 'int',
        'solution': 'str',
        'shard_num': 'int',
        'replica_num': 'int',
        'each_expand_nodes': 'int',
        'max_shard_count': 'int',
        'each_shard_num': 'int'
    }

    attribute_map = {
        'initial_node_num': 'initial_node_num',
        'solution': 'solution',
        'shard_num': 'shard_num',
        'replica_num': 'replica_num',
        'each_expand_nodes': 'each_expand_nodes',
        'max_shard_count': 'max_shard_count',
        'each_shard_num': 'each_shard_num'
    }

    def __init__(self, initial_node_num=None, solution=None, shard_num=None, replica_num=None, each_expand_nodes=None, max_shard_count=None, each_shard_num=None):
        r"""ShowDeploymentFormResponse

        The model defined in huaweicloud sdk

        :param initial_node_num: 初始节点数。
        :type initial_node_num: int
        :param solution: 解决方案模板名称。
        :type solution: str
        :param shard_num: 分片数。
        :type shard_num: int
        :param replica_num: 副本数。
        :type replica_num: int
        :param each_expand_nodes: **参数解释**: 每次扩容的最小节点数。 **取值范围**: 不涉及。
        :type each_expand_nodes: int
        :param max_shard_count: **参数解释**: 最大分片数。 **取值范围**: 不涉及。
        :type max_shard_count: int
        :param each_shard_num: **参数解释**: 每分片节点数。 **取值范围**: 不涉及。
        :type each_shard_num: int
        """
        
        super().__init__()

        self._initial_node_num = None
        self._solution = None
        self._shard_num = None
        self._replica_num = None
        self._each_expand_nodes = None
        self._max_shard_count = None
        self._each_shard_num = None
        self.discriminator = None

        if initial_node_num is not None:
            self.initial_node_num = initial_node_num
        if solution is not None:
            self.solution = solution
        if shard_num is not None:
            self.shard_num = shard_num
        if replica_num is not None:
            self.replica_num = replica_num
        if each_expand_nodes is not None:
            self.each_expand_nodes = each_expand_nodes
        if max_shard_count is not None:
            self.max_shard_count = max_shard_count
        if each_shard_num is not None:
            self.each_shard_num = each_shard_num

    @property
    def initial_node_num(self):
        r"""Gets the initial_node_num of this ShowDeploymentFormResponse.

        初始节点数。

        :return: The initial_node_num of this ShowDeploymentFormResponse.
        :rtype: int
        """
        return self._initial_node_num

    @initial_node_num.setter
    def initial_node_num(self, initial_node_num):
        r"""Sets the initial_node_num of this ShowDeploymentFormResponse.

        初始节点数。

        :param initial_node_num: The initial_node_num of this ShowDeploymentFormResponse.
        :type initial_node_num: int
        """
        self._initial_node_num = initial_node_num

    @property
    def solution(self):
        r"""Gets the solution of this ShowDeploymentFormResponse.

        解决方案模板名称。

        :return: The solution of this ShowDeploymentFormResponse.
        :rtype: str
        """
        return self._solution

    @solution.setter
    def solution(self, solution):
        r"""Sets the solution of this ShowDeploymentFormResponse.

        解决方案模板名称。

        :param solution: The solution of this ShowDeploymentFormResponse.
        :type solution: str
        """
        self._solution = solution

    @property
    def shard_num(self):
        r"""Gets the shard_num of this ShowDeploymentFormResponse.

        分片数。

        :return: The shard_num of this ShowDeploymentFormResponse.
        :rtype: int
        """
        return self._shard_num

    @shard_num.setter
    def shard_num(self, shard_num):
        r"""Sets the shard_num of this ShowDeploymentFormResponse.

        分片数。

        :param shard_num: The shard_num of this ShowDeploymentFormResponse.
        :type shard_num: int
        """
        self._shard_num = shard_num

    @property
    def replica_num(self):
        r"""Gets the replica_num of this ShowDeploymentFormResponse.

        副本数。

        :return: The replica_num of this ShowDeploymentFormResponse.
        :rtype: int
        """
        return self._replica_num

    @replica_num.setter
    def replica_num(self, replica_num):
        r"""Sets the replica_num of this ShowDeploymentFormResponse.

        副本数。

        :param replica_num: The replica_num of this ShowDeploymentFormResponse.
        :type replica_num: int
        """
        self._replica_num = replica_num

    @property
    def each_expand_nodes(self):
        r"""Gets the each_expand_nodes of this ShowDeploymentFormResponse.

        **参数解释**: 每次扩容的最小节点数。 **取值范围**: 不涉及。

        :return: The each_expand_nodes of this ShowDeploymentFormResponse.
        :rtype: int
        """
        return self._each_expand_nodes

    @each_expand_nodes.setter
    def each_expand_nodes(self, each_expand_nodes):
        r"""Sets the each_expand_nodes of this ShowDeploymentFormResponse.

        **参数解释**: 每次扩容的最小节点数。 **取值范围**: 不涉及。

        :param each_expand_nodes: The each_expand_nodes of this ShowDeploymentFormResponse.
        :type each_expand_nodes: int
        """
        self._each_expand_nodes = each_expand_nodes

    @property
    def max_shard_count(self):
        r"""Gets the max_shard_count of this ShowDeploymentFormResponse.

        **参数解释**: 最大分片数。 **取值范围**: 不涉及。

        :return: The max_shard_count of this ShowDeploymentFormResponse.
        :rtype: int
        """
        return self._max_shard_count

    @max_shard_count.setter
    def max_shard_count(self, max_shard_count):
        r"""Sets the max_shard_count of this ShowDeploymentFormResponse.

        **参数解释**: 最大分片数。 **取值范围**: 不涉及。

        :param max_shard_count: The max_shard_count of this ShowDeploymentFormResponse.
        :type max_shard_count: int
        """
        self._max_shard_count = max_shard_count

    @property
    def each_shard_num(self):
        r"""Gets the each_shard_num of this ShowDeploymentFormResponse.

        **参数解释**: 每分片节点数。 **取值范围**: 不涉及。

        :return: The each_shard_num of this ShowDeploymentFormResponse.
        :rtype: int
        """
        return self._each_shard_num

    @each_shard_num.setter
    def each_shard_num(self, each_shard_num):
        r"""Sets the each_shard_num of this ShowDeploymentFormResponse.

        **参数解释**: 每分片节点数。 **取值范围**: 不涉及。

        :param each_shard_num: The each_shard_num of this ShowDeploymentFormResponse.
        :type each_shard_num: int
        """
        self._each_shard_num = each_shard_num

    def to_dict(self):
        import warnings
        warnings.warn("ShowDeploymentFormResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowDeploymentFormResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
