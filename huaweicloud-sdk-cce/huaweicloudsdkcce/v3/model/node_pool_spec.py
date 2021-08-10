# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodePoolSpec:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'node_template': 'NodeSpec',
        'initial_node_count': 'int',
        'autoscaling': 'NodePoolNodeAutoscaling',
        'node_management': 'NodeManagement'
    }

    attribute_map = {
        'type': 'type',
        'node_template': 'nodeTemplate',
        'initial_node_count': 'initialNodeCount',
        'autoscaling': 'autoscaling',
        'node_management': 'nodeManagement'
    }

    def __init__(self, type=None, node_template=None, initial_node_count=None, autoscaling=None, node_management=None):
        """NodePoolSpec - a model defined in huaweicloud sdk"""
        
        

        self._type = None
        self._node_template = None
        self._initial_node_count = None
        self._autoscaling = None
        self._node_management = None
        self.discriminator = None

        if type is not None:
            self.type = type
        self.node_template = node_template
        if initial_node_count is not None:
            self.initial_node_count = initial_node_count
        if autoscaling is not None:
            self.autoscaling = autoscaling
        if node_management is not None:
            self.node_management = node_management

    @property
    def type(self):
        """Gets the type of this NodePoolSpec.

        节点池类型。不填写时默认为vm。  - vm：弹性云服务器 - ElasticBMS：C6型弹性裸金属通用计算增强型云服务器，规格示例：c6.22xlarge.2.physical 

        :return: The type of this NodePoolSpec.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NodePoolSpec.

        节点池类型。不填写时默认为vm。  - vm：弹性云服务器 - ElasticBMS：C6型弹性裸金属通用计算增强型云服务器，规格示例：c6.22xlarge.2.physical 

        :param type: The type of this NodePoolSpec.
        :type: str
        """
        self._type = type

    @property
    def node_template(self):
        """Gets the node_template of this NodePoolSpec.


        :return: The node_template of this NodePoolSpec.
        :rtype: NodeSpec
        """
        return self._node_template

    @node_template.setter
    def node_template(self, node_template):
        """Sets the node_template of this NodePoolSpec.


        :param node_template: The node_template of this NodePoolSpec.
        :type: NodeSpec
        """
        self._node_template = node_template

    @property
    def initial_node_count(self):
        """Gets the initial_node_count of this NodePoolSpec.

        节点池初始化节点个数。

        :return: The initial_node_count of this NodePoolSpec.
        :rtype: int
        """
        return self._initial_node_count

    @initial_node_count.setter
    def initial_node_count(self, initial_node_count):
        """Sets the initial_node_count of this NodePoolSpec.

        节点池初始化节点个数。

        :param initial_node_count: The initial_node_count of this NodePoolSpec.
        :type: int
        """
        self._initial_node_count = initial_node_count

    @property
    def autoscaling(self):
        """Gets the autoscaling of this NodePoolSpec.


        :return: The autoscaling of this NodePoolSpec.
        :rtype: NodePoolNodeAutoscaling
        """
        return self._autoscaling

    @autoscaling.setter
    def autoscaling(self, autoscaling):
        """Sets the autoscaling of this NodePoolSpec.


        :param autoscaling: The autoscaling of this NodePoolSpec.
        :type: NodePoolNodeAutoscaling
        """
        self._autoscaling = autoscaling

    @property
    def node_management(self):
        """Gets the node_management of this NodePoolSpec.


        :return: The node_management of this NodePoolSpec.
        :rtype: NodeManagement
        """
        return self._node_management

    @node_management.setter
    def node_management(self, node_management):
        """Sets the node_management of this NodePoolSpec.


        :param node_management: The node_management of this NodePoolSpec.
        :type: NodeManagement
        """
        self._node_management = node_management

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
        if not isinstance(other, NodePoolSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
