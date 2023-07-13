# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodePoolSpecUpdate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_template': 'NodeSpecUpdate',
        'initial_node_count': 'int',
        'autoscaling': 'NodePoolNodeAutoscaling'
    }

    attribute_map = {
        'node_template': 'nodeTemplate',
        'initial_node_count': 'initialNodeCount',
        'autoscaling': 'autoscaling'
    }

    def __init__(self, node_template=None, initial_node_count=None, autoscaling=None):
        """NodePoolSpecUpdate

        The model defined in huaweicloud sdk

        :param node_template: 
        :type node_template: :class:`huaweicloudsdkcce.v3.NodeSpecUpdate`
        :param initial_node_count: 节点池初始化节点个数。查询时为节点池目标节点数量。默认值为0。
        :type initial_node_count: int
        :param autoscaling: 
        :type autoscaling: :class:`huaweicloudsdkcce.v3.NodePoolNodeAutoscaling`
        """
        
        

        self._node_template = None
        self._initial_node_count = None
        self._autoscaling = None
        self.discriminator = None

        self.node_template = node_template
        self.initial_node_count = initial_node_count
        self.autoscaling = autoscaling

    @property
    def node_template(self):
        """Gets the node_template of this NodePoolSpecUpdate.

        :return: The node_template of this NodePoolSpecUpdate.
        :rtype: :class:`huaweicloudsdkcce.v3.NodeSpecUpdate`
        """
        return self._node_template

    @node_template.setter
    def node_template(self, node_template):
        """Sets the node_template of this NodePoolSpecUpdate.

        :param node_template: The node_template of this NodePoolSpecUpdate.
        :type node_template: :class:`huaweicloudsdkcce.v3.NodeSpecUpdate`
        """
        self._node_template = node_template

    @property
    def initial_node_count(self):
        """Gets the initial_node_count of this NodePoolSpecUpdate.

        节点池初始化节点个数。查询时为节点池目标节点数量。默认值为0。

        :return: The initial_node_count of this NodePoolSpecUpdate.
        :rtype: int
        """
        return self._initial_node_count

    @initial_node_count.setter
    def initial_node_count(self, initial_node_count):
        """Sets the initial_node_count of this NodePoolSpecUpdate.

        节点池初始化节点个数。查询时为节点池目标节点数量。默认值为0。

        :param initial_node_count: The initial_node_count of this NodePoolSpecUpdate.
        :type initial_node_count: int
        """
        self._initial_node_count = initial_node_count

    @property
    def autoscaling(self):
        """Gets the autoscaling of this NodePoolSpecUpdate.

        :return: The autoscaling of this NodePoolSpecUpdate.
        :rtype: :class:`huaweicloudsdkcce.v3.NodePoolNodeAutoscaling`
        """
        return self._autoscaling

    @autoscaling.setter
    def autoscaling(self, autoscaling):
        """Sets the autoscaling of this NodePoolSpecUpdate.

        :param autoscaling: The autoscaling of this NodePoolSpecUpdate.
        :type autoscaling: :class:`huaweicloudsdkcce.v3.NodePoolNodeAutoscaling`
        """
        self._autoscaling = autoscaling

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
        if not isinstance(other, NodePoolSpecUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
