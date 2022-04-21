# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OprecordCluster:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'cluster_type': 'str',
        'name': 'str',
        'cluster_id': 'str',
        'node_infos': 'list[NodeInfo]'
    }

    attribute_map = {
        'cluster_type': 'cluster_type',
        'name': 'name',
        'cluster_id': 'cluster_id',
        'node_infos': 'node_infos'
    }

    def __init__(self, cluster_type=None, name=None, cluster_id=None, node_infos=None):
        """OprecordCluster

        The model defined in huaweicloud sdk

        :param cluster_type: 集群类型
        :type cluster_type: str
        :param name: 集群名称
        :type name: str
        :param cluster_id: 集群ID
        :type cluster_id: str
        :param node_infos: 节点信息
        :type node_infos: list[:class:`huaweicloudsdkbcs.v2.NodeInfo`]
        """
        
        

        self._cluster_type = None
        self._name = None
        self._cluster_id = None
        self._node_infos = None
        self.discriminator = None

        if cluster_type is not None:
            self.cluster_type = cluster_type
        if name is not None:
            self.name = name
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if node_infos is not None:
            self.node_infos = node_infos

    @property
    def cluster_type(self):
        """Gets the cluster_type of this OprecordCluster.

        集群类型

        :return: The cluster_type of this OprecordCluster.
        :rtype: str
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        """Sets the cluster_type of this OprecordCluster.

        集群类型

        :param cluster_type: The cluster_type of this OprecordCluster.
        :type cluster_type: str
        """
        self._cluster_type = cluster_type

    @property
    def name(self):
        """Gets the name of this OprecordCluster.

        集群名称

        :return: The name of this OprecordCluster.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OprecordCluster.

        集群名称

        :param name: The name of this OprecordCluster.
        :type name: str
        """
        self._name = name

    @property
    def cluster_id(self):
        """Gets the cluster_id of this OprecordCluster.

        集群ID

        :return: The cluster_id of this OprecordCluster.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this OprecordCluster.

        集群ID

        :param cluster_id: The cluster_id of this OprecordCluster.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def node_infos(self):
        """Gets the node_infos of this OprecordCluster.

        节点信息

        :return: The node_infos of this OprecordCluster.
        :rtype: list[:class:`huaweicloudsdkbcs.v2.NodeInfo`]
        """
        return self._node_infos

    @node_infos.setter
    def node_infos(self, node_infos):
        """Sets the node_infos of this OprecordCluster.

        节点信息

        :param node_infos: The node_infos of this OprecordCluster.
        :type node_infos: list[:class:`huaweicloudsdkbcs.v2.NodeInfo`]
        """
        self._node_infos = node_infos

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
        if not isinstance(other, OprecordCluster):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
