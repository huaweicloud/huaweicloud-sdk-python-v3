# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateNodePoolStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'current_node': 'int',
        'creating_node': 'int',
        'deleting_node': 'int',
        'phase': 'str',
        'conditions': 'list[NodePoolCondition]'
    }

    attribute_map = {
        'current_node': 'currentNode',
        'creating_node': 'creatingNode',
        'deleting_node': 'deletingNode',
        'phase': 'phase',
        'conditions': 'conditions'
    }

    def __init__(self, current_node=None, creating_node=None, deleting_node=None, phase=None, conditions=None):
        """CreateNodePoolStatus

        The model defined in huaweicloud sdk

        :param current_node: 当前节点池中所有节点数量（不含删除中的节点）。
        :type current_node: int
        :param creating_node: 当前节点池中处于创建流程中的节点数量。
        :type creating_node: int
        :param deleting_node: 当前节点池中删除中的节点数量。
        :type deleting_node: int
        :param phase: 节点池状态。 - 空值：可用（节点池当前节点数已达到预期，且无伸缩中的节点） - Synchronizing：伸缩中（节点池当前节点数未达到预期，且无伸缩中的节点） - Synchronized：伸缩等待中（节点池当前节点数未达到预期，或者存在伸缩中的节点） - SoldOut：节点池当前不可扩容（兼容字段，标记节点池资源售罄、资源配额不足等不可扩容状态） &gt; 上述节点池状态已废弃，仅兼容保留，不建议使用，替代感知方式如下： &gt; - 节点池扩缩状态：可通过currentNode/creatingNode/deletingNode节点状态统计信息，精确感知当前节点池扩缩状态。 &gt; - 节点池可扩容状态：可通过conditions感知节点池详细状态，其中\&quot;Scalable\&quot;可替代SoldOut语义。 - Deleting：删除中 - Error：错误 
        :type phase: str
        :param conditions: 节点池当前详细状态列表，详情参见Condition类型定义。 
        :type conditions: list[:class:`huaweicloudsdkcce.v3.NodePoolCondition`]
        """
        
        

        self._current_node = None
        self._creating_node = None
        self._deleting_node = None
        self._phase = None
        self._conditions = None
        self.discriminator = None

        if current_node is not None:
            self.current_node = current_node
        if creating_node is not None:
            self.creating_node = creating_node
        if deleting_node is not None:
            self.deleting_node = deleting_node
        if phase is not None:
            self.phase = phase
        if conditions is not None:
            self.conditions = conditions

    @property
    def current_node(self):
        """Gets the current_node of this CreateNodePoolStatus.

        当前节点池中所有节点数量（不含删除中的节点）。

        :return: The current_node of this CreateNodePoolStatus.
        :rtype: int
        """
        return self._current_node

    @current_node.setter
    def current_node(self, current_node):
        """Sets the current_node of this CreateNodePoolStatus.

        当前节点池中所有节点数量（不含删除中的节点）。

        :param current_node: The current_node of this CreateNodePoolStatus.
        :type current_node: int
        """
        self._current_node = current_node

    @property
    def creating_node(self):
        """Gets the creating_node of this CreateNodePoolStatus.

        当前节点池中处于创建流程中的节点数量。

        :return: The creating_node of this CreateNodePoolStatus.
        :rtype: int
        """
        return self._creating_node

    @creating_node.setter
    def creating_node(self, creating_node):
        """Sets the creating_node of this CreateNodePoolStatus.

        当前节点池中处于创建流程中的节点数量。

        :param creating_node: The creating_node of this CreateNodePoolStatus.
        :type creating_node: int
        """
        self._creating_node = creating_node

    @property
    def deleting_node(self):
        """Gets the deleting_node of this CreateNodePoolStatus.

        当前节点池中删除中的节点数量。

        :return: The deleting_node of this CreateNodePoolStatus.
        :rtype: int
        """
        return self._deleting_node

    @deleting_node.setter
    def deleting_node(self, deleting_node):
        """Sets the deleting_node of this CreateNodePoolStatus.

        当前节点池中删除中的节点数量。

        :param deleting_node: The deleting_node of this CreateNodePoolStatus.
        :type deleting_node: int
        """
        self._deleting_node = deleting_node

    @property
    def phase(self):
        """Gets the phase of this CreateNodePoolStatus.

        节点池状态。 - 空值：可用（节点池当前节点数已达到预期，且无伸缩中的节点） - Synchronizing：伸缩中（节点池当前节点数未达到预期，且无伸缩中的节点） - Synchronized：伸缩等待中（节点池当前节点数未达到预期，或者存在伸缩中的节点） - SoldOut：节点池当前不可扩容（兼容字段，标记节点池资源售罄、资源配额不足等不可扩容状态） > 上述节点池状态已废弃，仅兼容保留，不建议使用，替代感知方式如下： > - 节点池扩缩状态：可通过currentNode/creatingNode/deletingNode节点状态统计信息，精确感知当前节点池扩缩状态。 > - 节点池可扩容状态：可通过conditions感知节点池详细状态，其中\"Scalable\"可替代SoldOut语义。 - Deleting：删除中 - Error：错误 

        :return: The phase of this CreateNodePoolStatus.
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """Sets the phase of this CreateNodePoolStatus.

        节点池状态。 - 空值：可用（节点池当前节点数已达到预期，且无伸缩中的节点） - Synchronizing：伸缩中（节点池当前节点数未达到预期，且无伸缩中的节点） - Synchronized：伸缩等待中（节点池当前节点数未达到预期，或者存在伸缩中的节点） - SoldOut：节点池当前不可扩容（兼容字段，标记节点池资源售罄、资源配额不足等不可扩容状态） > 上述节点池状态已废弃，仅兼容保留，不建议使用，替代感知方式如下： > - 节点池扩缩状态：可通过currentNode/creatingNode/deletingNode节点状态统计信息，精确感知当前节点池扩缩状态。 > - 节点池可扩容状态：可通过conditions感知节点池详细状态，其中\"Scalable\"可替代SoldOut语义。 - Deleting：删除中 - Error：错误 

        :param phase: The phase of this CreateNodePoolStatus.
        :type phase: str
        """
        self._phase = phase

    @property
    def conditions(self):
        """Gets the conditions of this CreateNodePoolStatus.

        节点池当前详细状态列表，详情参见Condition类型定义。 

        :return: The conditions of this CreateNodePoolStatus.
        :rtype: list[:class:`huaweicloudsdkcce.v3.NodePoolCondition`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this CreateNodePoolStatus.

        节点池当前详细状态列表，详情参见Condition类型定义。 

        :param conditions: The conditions of this CreateNodePoolStatus.
        :type conditions: list[:class:`huaweicloudsdkcce.v3.NodePoolCondition`]
        """
        self._conditions = conditions

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
        if not isinstance(other, CreateNodePoolStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
