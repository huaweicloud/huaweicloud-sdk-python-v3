# coding: utf-8

import pprint
import re

import six





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
        'autoscaling': 'NodePoolNodeAutoscaling',
        'initial_node_count': 'int',
        'node_management': 'NodeManagement',
        'node_template': 'V3NodeSpec',
        'type': 'str'
    }

    attribute_map = {
        'autoscaling': 'autoscaling',
        'initial_node_count': 'initialNodeCount',
        'node_management': 'nodeManagement',
        'node_template': 'nodeTemplate',
        'type': 'type'
    }

    def __init__(self, autoscaling=None, initial_node_count=None, node_management=None, node_template=None, type=None):
        """NodePoolSpec - a model defined in huaweicloud sdk"""
        
        

        self._autoscaling = None
        self._initial_node_count = None
        self._node_management = None
        self._node_template = None
        self._type = None
        self.discriminator = None

        if autoscaling is not None:
            self.autoscaling = autoscaling
        if initial_node_count is not None:
            self.initial_node_count = initial_node_count
        if node_management is not None:
            self.node_management = node_management
        self.node_template = node_template
        if type is not None:
            self.type = type

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

    @property
    def node_template(self):
        """Gets the node_template of this NodePoolSpec.


        :return: The node_template of this NodePoolSpec.
        :rtype: V3NodeSpec
        """
        return self._node_template

    @node_template.setter
    def node_template(self, node_template):
        """Sets the node_template of this NodePoolSpec.


        :param node_template: The node_template of this NodePoolSpec.
        :type: V3NodeSpec
        """
        self._node_template = node_template

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NodePoolSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
