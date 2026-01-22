# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCesHierarchyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dimensions': 'list[ShowCeshierarchyRespDimensions]',
        'instance_ids': 'list[ShowCesHierarchyRespInstanceIds]',
        'nodes': 'list[ShowCesHierarchyRespNodes]',
        'topics': 'list[ShowCeshierarchyRespTopics]',
        'dlq': 'list[ShowCeshierarchyRespDlq]',
        'groups': 'list[ShowCeshierarchyRespGroups]'
    }

    attribute_map = {
        'dimensions': 'dimensions',
        'instance_ids': 'instance_ids',
        'nodes': 'nodes',
        'topics': 'topics',
        'dlq': 'dlq',
        'groups': 'groups'
    }

    def __init__(self, dimensions=None, instance_ids=None, nodes=None, topics=None, dlq=None, groups=None):
        r"""ShowCesHierarchyResponse

        The model defined in huaweicloud sdk

        :param dimensions: **参数解释**： 监控维度。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type dimensions: list[:class:`huaweicloudsdkrocketmq.v2.ShowCeshierarchyRespDimensions`]
        :param instance_ids: **参数解释**： 实例信息。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type instance_ids: list[:class:`huaweicloudsdkrocketmq.v2.ShowCesHierarchyRespInstanceIds`]
        :param nodes: **参数解释**： 节点信息。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type nodes: list[:class:`huaweicloudsdkrocketmq.v2.ShowCesHierarchyRespNodes`]
        :param topics: **参数解释**： 队列信息。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type topics: list[:class:`huaweicloudsdkrocketmq.v2.ShowCeshierarchyRespTopics`]
        :param dlq: **参数解释**： 死信队列。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type dlq: list[:class:`huaweicloudsdkrocketmq.v2.ShowCeshierarchyRespDlq`]
        :param groups: **参数解释**： 消费组信息。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type groups: list[:class:`huaweicloudsdkrocketmq.v2.ShowCeshierarchyRespGroups`]
        """
        
        super().__init__()

        self._dimensions = None
        self._instance_ids = None
        self._nodes = None
        self._topics = None
        self._dlq = None
        self._groups = None
        self.discriminator = None

        if dimensions is not None:
            self.dimensions = dimensions
        if instance_ids is not None:
            self.instance_ids = instance_ids
        if nodes is not None:
            self.nodes = nodes
        if topics is not None:
            self.topics = topics
        if dlq is not None:
            self.dlq = dlq
        if groups is not None:
            self.groups = groups

    @property
    def dimensions(self):
        r"""Gets the dimensions of this ShowCesHierarchyResponse.

        **参数解释**： 监控维度。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The dimensions of this ShowCesHierarchyResponse.
        :rtype: list[:class:`huaweicloudsdkrocketmq.v2.ShowCeshierarchyRespDimensions`]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        r"""Sets the dimensions of this ShowCesHierarchyResponse.

        **参数解释**： 监控维度。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param dimensions: The dimensions of this ShowCesHierarchyResponse.
        :type dimensions: list[:class:`huaweicloudsdkrocketmq.v2.ShowCeshierarchyRespDimensions`]
        """
        self._dimensions = dimensions

    @property
    def instance_ids(self):
        r"""Gets the instance_ids of this ShowCesHierarchyResponse.

        **参数解释**： 实例信息。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The instance_ids of this ShowCesHierarchyResponse.
        :rtype: list[:class:`huaweicloudsdkrocketmq.v2.ShowCesHierarchyRespInstanceIds`]
        """
        return self._instance_ids

    @instance_ids.setter
    def instance_ids(self, instance_ids):
        r"""Sets the instance_ids of this ShowCesHierarchyResponse.

        **参数解释**： 实例信息。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param instance_ids: The instance_ids of this ShowCesHierarchyResponse.
        :type instance_ids: list[:class:`huaweicloudsdkrocketmq.v2.ShowCesHierarchyRespInstanceIds`]
        """
        self._instance_ids = instance_ids

    @property
    def nodes(self):
        r"""Gets the nodes of this ShowCesHierarchyResponse.

        **参数解释**： 节点信息。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The nodes of this ShowCesHierarchyResponse.
        :rtype: list[:class:`huaweicloudsdkrocketmq.v2.ShowCesHierarchyRespNodes`]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        r"""Sets the nodes of this ShowCesHierarchyResponse.

        **参数解释**： 节点信息。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param nodes: The nodes of this ShowCesHierarchyResponse.
        :type nodes: list[:class:`huaweicloudsdkrocketmq.v2.ShowCesHierarchyRespNodes`]
        """
        self._nodes = nodes

    @property
    def topics(self):
        r"""Gets the topics of this ShowCesHierarchyResponse.

        **参数解释**： 队列信息。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The topics of this ShowCesHierarchyResponse.
        :rtype: list[:class:`huaweicloudsdkrocketmq.v2.ShowCeshierarchyRespTopics`]
        """
        return self._topics

    @topics.setter
    def topics(self, topics):
        r"""Sets the topics of this ShowCesHierarchyResponse.

        **参数解释**： 队列信息。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param topics: The topics of this ShowCesHierarchyResponse.
        :type topics: list[:class:`huaweicloudsdkrocketmq.v2.ShowCeshierarchyRespTopics`]
        """
        self._topics = topics

    @property
    def dlq(self):
        r"""Gets the dlq of this ShowCesHierarchyResponse.

        **参数解释**： 死信队列。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The dlq of this ShowCesHierarchyResponse.
        :rtype: list[:class:`huaweicloudsdkrocketmq.v2.ShowCeshierarchyRespDlq`]
        """
        return self._dlq

    @dlq.setter
    def dlq(self, dlq):
        r"""Sets the dlq of this ShowCesHierarchyResponse.

        **参数解释**： 死信队列。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param dlq: The dlq of this ShowCesHierarchyResponse.
        :type dlq: list[:class:`huaweicloudsdkrocketmq.v2.ShowCeshierarchyRespDlq`]
        """
        self._dlq = dlq

    @property
    def groups(self):
        r"""Gets the groups of this ShowCesHierarchyResponse.

        **参数解释**： 消费组信息。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The groups of this ShowCesHierarchyResponse.
        :rtype: list[:class:`huaweicloudsdkrocketmq.v2.ShowCeshierarchyRespGroups`]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        r"""Sets the groups of this ShowCesHierarchyResponse.

        **参数解释**： 消费组信息。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param groups: The groups of this ShowCesHierarchyResponse.
        :type groups: list[:class:`huaweicloudsdkrocketmq.v2.ShowCeshierarchyRespGroups`]
        """
        self._groups = groups

    def to_dict(self):
        import warnings
        warnings.warn("ShowCesHierarchyResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowCesHierarchyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
