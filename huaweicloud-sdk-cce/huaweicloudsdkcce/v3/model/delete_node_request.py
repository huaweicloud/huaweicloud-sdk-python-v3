# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteNodeRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'node_id': 'str',
        'nodepool_scale_down': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'node_id': 'node_id',
        'nodepool_scale_down': 'nodepoolScaleDown'
    }

    def __init__(self, cluster_id=None, node_id=None, nodepool_scale_down=None):
        """DeleteNodeRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 集群ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。
        :type cluster_id: str
        :param node_id: 节点ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。
        :type node_id: str
        :param nodepool_scale_down: 标明是否为nodepool下发的请求。若不为“NoScaleDown”将自动更新对应节点池的实例数
        :type nodepool_scale_down: str
        """
        
        

        self._cluster_id = None
        self._node_id = None
        self._nodepool_scale_down = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.node_id = node_id
        if nodepool_scale_down is not None:
            self.nodepool_scale_down = nodepool_scale_down

    @property
    def cluster_id(self):
        """Gets the cluster_id of this DeleteNodeRequest.

        集群ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。

        :return: The cluster_id of this DeleteNodeRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this DeleteNodeRequest.

        集群ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。

        :param cluster_id: The cluster_id of this DeleteNodeRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def node_id(self):
        """Gets the node_id of this DeleteNodeRequest.

        节点ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。

        :return: The node_id of this DeleteNodeRequest.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this DeleteNodeRequest.

        节点ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。

        :param node_id: The node_id of this DeleteNodeRequest.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def nodepool_scale_down(self):
        """Gets the nodepool_scale_down of this DeleteNodeRequest.

        标明是否为nodepool下发的请求。若不为“NoScaleDown”将自动更新对应节点池的实例数

        :return: The nodepool_scale_down of this DeleteNodeRequest.
        :rtype: str
        """
        return self._nodepool_scale_down

    @nodepool_scale_down.setter
    def nodepool_scale_down(self, nodepool_scale_down):
        """Sets the nodepool_scale_down of this DeleteNodeRequest.

        标明是否为nodepool下发的请求。若不为“NoScaleDown”将自动更新对应节点池的实例数

        :param nodepool_scale_down: The nodepool_scale_down of this DeleteNodeRequest.
        :type nodepool_scale_down: str
        """
        self._nodepool_scale_down = nodepool_scale_down

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
        if not isinstance(other, DeleteNodeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
