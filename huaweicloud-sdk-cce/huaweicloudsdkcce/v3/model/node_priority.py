# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodePriority:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_selector': 'NodeSelector',
        'priority': 'int'
    }

    attribute_map = {
        'node_selector': 'nodeSelector',
        'priority': 'priority'
    }

    def __init__(self, node_selector=None, priority=None):
        """NodePriority

        The model defined in huaweicloud sdk

        :param node_selector: 
        :type node_selector: :class:`huaweicloudsdkcce.v3.NodeSelector`
        :param priority: 该批次节点的优先级，默认值为0，优先级最低，数值越大优先级越高
        :type priority: int
        """
        
        

        self._node_selector = None
        self._priority = None
        self.discriminator = None

        self.node_selector = node_selector
        self.priority = priority

    @property
    def node_selector(self):
        """Gets the node_selector of this NodePriority.

        :return: The node_selector of this NodePriority.
        :rtype: :class:`huaweicloudsdkcce.v3.NodeSelector`
        """
        return self._node_selector

    @node_selector.setter
    def node_selector(self, node_selector):
        """Sets the node_selector of this NodePriority.

        :param node_selector: The node_selector of this NodePriority.
        :type node_selector: :class:`huaweicloudsdkcce.v3.NodeSelector`
        """
        self._node_selector = node_selector

    @property
    def priority(self):
        """Gets the priority of this NodePriority.

        该批次节点的优先级，默认值为0，优先级最低，数值越大优先级越高

        :return: The priority of this NodePriority.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this NodePriority.

        该批次节点的优先级，默认值为0，优先级最低，数值越大优先级越高

        :param priority: The priority of this NodePriority.
        :type priority: int
        """
        self._priority = priority

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
        if not isinstance(other, NodePriority):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
