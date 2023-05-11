# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterNodeConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'master_node_vip': 'str',
        'master_nodes': 'list[NodeConfig]',
        'work_nodes': 'list[NodeConfig]'
    }

    attribute_map = {
        'master_node_vip': 'master_node_vip',
        'master_nodes': 'master_nodes',
        'work_nodes': 'work_nodes'
    }

    def __init__(self, master_node_vip=None, master_nodes=None, work_nodes=None):
        """ClusterNodeConfig

        The model defined in huaweicloud sdk

        :param master_node_vip: master虚拟ip
        :type master_node_vip: str
        :param master_nodes: master节点数
        :type master_nodes: list[:class:`huaweicloudsdkiotedge.v3.NodeConfig`]
        :param work_nodes: work节点数
        :type work_nodes: list[:class:`huaweicloudsdkiotedge.v3.NodeConfig`]
        """
        
        

        self._master_node_vip = None
        self._master_nodes = None
        self._work_nodes = None
        self.discriminator = None

        if master_node_vip is not None:
            self.master_node_vip = master_node_vip
        if master_nodes is not None:
            self.master_nodes = master_nodes
        if work_nodes is not None:
            self.work_nodes = work_nodes

    @property
    def master_node_vip(self):
        """Gets the master_node_vip of this ClusterNodeConfig.

        master虚拟ip

        :return: The master_node_vip of this ClusterNodeConfig.
        :rtype: str
        """
        return self._master_node_vip

    @master_node_vip.setter
    def master_node_vip(self, master_node_vip):
        """Sets the master_node_vip of this ClusterNodeConfig.

        master虚拟ip

        :param master_node_vip: The master_node_vip of this ClusterNodeConfig.
        :type master_node_vip: str
        """
        self._master_node_vip = master_node_vip

    @property
    def master_nodes(self):
        """Gets the master_nodes of this ClusterNodeConfig.

        master节点数

        :return: The master_nodes of this ClusterNodeConfig.
        :rtype: list[:class:`huaweicloudsdkiotedge.v3.NodeConfig`]
        """
        return self._master_nodes

    @master_nodes.setter
    def master_nodes(self, master_nodes):
        """Sets the master_nodes of this ClusterNodeConfig.

        master节点数

        :param master_nodes: The master_nodes of this ClusterNodeConfig.
        :type master_nodes: list[:class:`huaweicloudsdkiotedge.v3.NodeConfig`]
        """
        self._master_nodes = master_nodes

    @property
    def work_nodes(self):
        """Gets the work_nodes of this ClusterNodeConfig.

        work节点数

        :return: The work_nodes of this ClusterNodeConfig.
        :rtype: list[:class:`huaweicloudsdkiotedge.v3.NodeConfig`]
        """
        return self._work_nodes

    @work_nodes.setter
    def work_nodes(self, work_nodes):
        """Sets the work_nodes of this ClusterNodeConfig.

        work节点数

        :param work_nodes: The work_nodes of this ClusterNodeConfig.
        :type work_nodes: list[:class:`huaweicloudsdkiotedge.v3.NodeConfig`]
        """
        self._work_nodes = work_nodes

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
        if not isinstance(other, ClusterNodeConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
