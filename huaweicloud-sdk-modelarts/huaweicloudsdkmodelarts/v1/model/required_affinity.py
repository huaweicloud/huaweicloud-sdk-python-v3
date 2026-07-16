# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RequiredAffinity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'affinity_type': 'str',
        'job_level': 'str',
        'affinity_group_size': 'int',
        'affinity_group_level': 'str',
        'node_affinity': 'NodeSelector'
    }

    attribute_map = {
        'affinity_type': 'affinity_type',
        'job_level': 'job_level',
        'affinity_group_size': 'affinity_group_size',
        'affinity_group_level': 'affinity_group_level',
        'node_affinity': 'node_affinity'
    }

    def __init__(self, affinity_type=None, job_level=None, affinity_group_size=None, affinity_group_level=None, node_affinity=None):
        r"""RequiredAffinity

        The model defined in huaweicloud sdk

        :param affinity_type: **参数解释**：亲和调度策略。 **约束限制**：不涉及。 **取值范围**： - cabinet：强整柜调度 - hyperinstance：超节点亲和调度 - networkTopology: 网络拓扑亲和调度  **默认取值**：不涉及。
        :type affinity_type: str
        :param job_level: **参数解释**：作业整体的网络拓扑约束。 **约束限制**：affinity_type为networkTopology时有效，系统会将作业的所有task调度至不高于job_level层的节点组中。 用户向超节点资源池投递训练作业，如果未设置作业整体的网络拓扑约束，系统会默认赋值为cluster。 **取值范围**： - cluster：资源池级 - hyperinstanceGroup: 超节点级  **默认取值**：默认值cluster。
        :type job_level: str
        :param affinity_group_size: **参数解释**：亲和组大小。 **约束限制**：affinity_type为hyperinstance或networkTopology时必填，系统会将affinity_group_size个task调度到一个超节点内组成亲和组。affinity_group_size的大小不能超过超节点的步长。 用户向超节点资源池投递训练作业，如果未设置亲和组大小，系统会默认赋值为1。 **取值范围**：不涉及。 **默认取值**：默认值1。
        :type affinity_group_size: int
        :param affinity_group_level: **参数解释**：亲和组的网络拓扑约束。 **约束限制**：affinity_type为networkTopology时有效，系统会将affinity_group_size个task组成的亲和组调度至不高于affinity_group_level层的节点组中。 用户向超节点资源池投递训练作业，如果未设置亲和组的网络拓扑约束，系统会默认赋值为hyperinstanceGroup。 **取值范围**： - hyperinstance：超节点级 - slice: 柜级  **默认取值**：默认值hyperinstanceGroup。
        :type affinity_group_level: str
        :param node_affinity: 
        :type node_affinity: :class:`huaweicloudsdkmodelarts.v1.NodeSelector`
        """
        
        

        self._affinity_type = None
        self._job_level = None
        self._affinity_group_size = None
        self._affinity_group_level = None
        self._node_affinity = None
        self.discriminator = None

        if affinity_type is not None:
            self.affinity_type = affinity_type
        if job_level is not None:
            self.job_level = job_level
        if affinity_group_size is not None:
            self.affinity_group_size = affinity_group_size
        if affinity_group_level is not None:
            self.affinity_group_level = affinity_group_level
        if node_affinity is not None:
            self.node_affinity = node_affinity

    @property
    def affinity_type(self):
        r"""Gets the affinity_type of this RequiredAffinity.

        **参数解释**：亲和调度策略。 **约束限制**：不涉及。 **取值范围**： - cabinet：强整柜调度 - hyperinstance：超节点亲和调度 - networkTopology: 网络拓扑亲和调度  **默认取值**：不涉及。

        :return: The affinity_type of this RequiredAffinity.
        :rtype: str
        """
        return self._affinity_type

    @affinity_type.setter
    def affinity_type(self, affinity_type):
        r"""Sets the affinity_type of this RequiredAffinity.

        **参数解释**：亲和调度策略。 **约束限制**：不涉及。 **取值范围**： - cabinet：强整柜调度 - hyperinstance：超节点亲和调度 - networkTopology: 网络拓扑亲和调度  **默认取值**：不涉及。

        :param affinity_type: The affinity_type of this RequiredAffinity.
        :type affinity_type: str
        """
        self._affinity_type = affinity_type

    @property
    def job_level(self):
        r"""Gets the job_level of this RequiredAffinity.

        **参数解释**：作业整体的网络拓扑约束。 **约束限制**：affinity_type为networkTopology时有效，系统会将作业的所有task调度至不高于job_level层的节点组中。 用户向超节点资源池投递训练作业，如果未设置作业整体的网络拓扑约束，系统会默认赋值为cluster。 **取值范围**： - cluster：资源池级 - hyperinstanceGroup: 超节点级  **默认取值**：默认值cluster。

        :return: The job_level of this RequiredAffinity.
        :rtype: str
        """
        return self._job_level

    @job_level.setter
    def job_level(self, job_level):
        r"""Sets the job_level of this RequiredAffinity.

        **参数解释**：作业整体的网络拓扑约束。 **约束限制**：affinity_type为networkTopology时有效，系统会将作业的所有task调度至不高于job_level层的节点组中。 用户向超节点资源池投递训练作业，如果未设置作业整体的网络拓扑约束，系统会默认赋值为cluster。 **取值范围**： - cluster：资源池级 - hyperinstanceGroup: 超节点级  **默认取值**：默认值cluster。

        :param job_level: The job_level of this RequiredAffinity.
        :type job_level: str
        """
        self._job_level = job_level

    @property
    def affinity_group_size(self):
        r"""Gets the affinity_group_size of this RequiredAffinity.

        **参数解释**：亲和组大小。 **约束限制**：affinity_type为hyperinstance或networkTopology时必填，系统会将affinity_group_size个task调度到一个超节点内组成亲和组。affinity_group_size的大小不能超过超节点的步长。 用户向超节点资源池投递训练作业，如果未设置亲和组大小，系统会默认赋值为1。 **取值范围**：不涉及。 **默认取值**：默认值1。

        :return: The affinity_group_size of this RequiredAffinity.
        :rtype: int
        """
        return self._affinity_group_size

    @affinity_group_size.setter
    def affinity_group_size(self, affinity_group_size):
        r"""Sets the affinity_group_size of this RequiredAffinity.

        **参数解释**：亲和组大小。 **约束限制**：affinity_type为hyperinstance或networkTopology时必填，系统会将affinity_group_size个task调度到一个超节点内组成亲和组。affinity_group_size的大小不能超过超节点的步长。 用户向超节点资源池投递训练作业，如果未设置亲和组大小，系统会默认赋值为1。 **取值范围**：不涉及。 **默认取值**：默认值1。

        :param affinity_group_size: The affinity_group_size of this RequiredAffinity.
        :type affinity_group_size: int
        """
        self._affinity_group_size = affinity_group_size

    @property
    def affinity_group_level(self):
        r"""Gets the affinity_group_level of this RequiredAffinity.

        **参数解释**：亲和组的网络拓扑约束。 **约束限制**：affinity_type为networkTopology时有效，系统会将affinity_group_size个task组成的亲和组调度至不高于affinity_group_level层的节点组中。 用户向超节点资源池投递训练作业，如果未设置亲和组的网络拓扑约束，系统会默认赋值为hyperinstanceGroup。 **取值范围**： - hyperinstance：超节点级 - slice: 柜级  **默认取值**：默认值hyperinstanceGroup。

        :return: The affinity_group_level of this RequiredAffinity.
        :rtype: str
        """
        return self._affinity_group_level

    @affinity_group_level.setter
    def affinity_group_level(self, affinity_group_level):
        r"""Sets the affinity_group_level of this RequiredAffinity.

        **参数解释**：亲和组的网络拓扑约束。 **约束限制**：affinity_type为networkTopology时有效，系统会将affinity_group_size个task组成的亲和组调度至不高于affinity_group_level层的节点组中。 用户向超节点资源池投递训练作业，如果未设置亲和组的网络拓扑约束，系统会默认赋值为hyperinstanceGroup。 **取值范围**： - hyperinstance：超节点级 - slice: 柜级  **默认取值**：默认值hyperinstanceGroup。

        :param affinity_group_level: The affinity_group_level of this RequiredAffinity.
        :type affinity_group_level: str
        """
        self._affinity_group_level = affinity_group_level

    @property
    def node_affinity(self):
        r"""Gets the node_affinity of this RequiredAffinity.

        :return: The node_affinity of this RequiredAffinity.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.NodeSelector`
        """
        return self._node_affinity

    @node_affinity.setter
    def node_affinity(self, node_affinity):
        r"""Sets the node_affinity of this RequiredAffinity.

        :param node_affinity: The node_affinity of this RequiredAffinity.
        :type node_affinity: :class:`huaweicloudsdkmodelarts.v1.NodeSelector`
        """
        self._node_affinity = node_affinity

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
        if not isinstance(other, RequiredAffinity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
