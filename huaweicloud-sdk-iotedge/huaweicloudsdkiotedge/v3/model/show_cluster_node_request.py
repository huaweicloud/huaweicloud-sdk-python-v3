# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowClusterNodeRequest:

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
        'node_name': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'node_name': 'node_name'
    }

    def __init__(self, cluster_id=None, node_name=None):
        r"""ShowClusterNodeRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 边缘集群ID
        :type cluster_id: str
        :param node_name: 节点名称
        :type node_name: str
        """
        
        

        self._cluster_id = None
        self._node_name = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.node_name = node_name

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ShowClusterNodeRequest.

        边缘集群ID

        :return: The cluster_id of this ShowClusterNodeRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ShowClusterNodeRequest.

        边缘集群ID

        :param cluster_id: The cluster_id of this ShowClusterNodeRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def node_name(self):
        r"""Gets the node_name of this ShowClusterNodeRequest.

        节点名称

        :return: The node_name of this ShowClusterNodeRequest.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        r"""Sets the node_name of this ShowClusterNodeRequest.

        节点名称

        :param node_name: The node_name of this ShowClusterNodeRequest.
        :type node_name: str
        """
        self._node_name = node_name

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
        if not isinstance(other, ShowClusterNodeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
