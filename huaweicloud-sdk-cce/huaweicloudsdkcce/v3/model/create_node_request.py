# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateNodeRequest:

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
        'nodepool_scale_up': 'str',
        'body': 'NodeCreateRequest'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'nodepool_scale_up': 'nodepoolScaleUp',
        'body': 'body'
    }

    def __init__(self, cluster_id=None, nodepool_scale_up=None, body=None):
        r"""CreateNodeRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 集群ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。
        :type cluster_id: str
        :param nodepool_scale_up: **参数解释**： 标明是否为nodepool扩容下发的创建节点请求。若为“NodepoolScaleUp”将根据当前集群子网实际能支持的用户节点数自动更新本次创建节点的个数，比如集群子网仅能支持的用户节点个数为1，当请求创建节点的个数大于1时，将自动调整为创建1个节点。若不为“NodepoolScaleUp”将自动更新对应节点池的实例数。 **约束限制**： 不涉及 **取值范围**： - NodepoolScaleUp：表示节点池扩容创建节点  **默认取值**： 无
        :type nodepool_scale_up: str
        :param body: Body of the CreateNodeRequest
        :type body: :class:`huaweicloudsdkcce.v3.NodeCreateRequest`
        """
        
        

        self._cluster_id = None
        self._nodepool_scale_up = None
        self._body = None
        self.discriminator = None

        self.cluster_id = cluster_id
        if nodepool_scale_up is not None:
            self.nodepool_scale_up = nodepool_scale_up
        if body is not None:
            self.body = body

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this CreateNodeRequest.

        集群ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。

        :return: The cluster_id of this CreateNodeRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this CreateNodeRequest.

        集群ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。

        :param cluster_id: The cluster_id of this CreateNodeRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def nodepool_scale_up(self):
        r"""Gets the nodepool_scale_up of this CreateNodeRequest.

        **参数解释**： 标明是否为nodepool扩容下发的创建节点请求。若为“NodepoolScaleUp”将根据当前集群子网实际能支持的用户节点数自动更新本次创建节点的个数，比如集群子网仅能支持的用户节点个数为1，当请求创建节点的个数大于1时，将自动调整为创建1个节点。若不为“NodepoolScaleUp”将自动更新对应节点池的实例数。 **约束限制**： 不涉及 **取值范围**： - NodepoolScaleUp：表示节点池扩容创建节点  **默认取值**： 无

        :return: The nodepool_scale_up of this CreateNodeRequest.
        :rtype: str
        """
        return self._nodepool_scale_up

    @nodepool_scale_up.setter
    def nodepool_scale_up(self, nodepool_scale_up):
        r"""Sets the nodepool_scale_up of this CreateNodeRequest.

        **参数解释**： 标明是否为nodepool扩容下发的创建节点请求。若为“NodepoolScaleUp”将根据当前集群子网实际能支持的用户节点数自动更新本次创建节点的个数，比如集群子网仅能支持的用户节点个数为1，当请求创建节点的个数大于1时，将自动调整为创建1个节点。若不为“NodepoolScaleUp”将自动更新对应节点池的实例数。 **约束限制**： 不涉及 **取值范围**： - NodepoolScaleUp：表示节点池扩容创建节点  **默认取值**： 无

        :param nodepool_scale_up: The nodepool_scale_up of this CreateNodeRequest.
        :type nodepool_scale_up: str
        """
        self._nodepool_scale_up = nodepool_scale_up

    @property
    def body(self):
        r"""Gets the body of this CreateNodeRequest.

        :return: The body of this CreateNodeRequest.
        :rtype: :class:`huaweicloudsdkcce.v3.NodeCreateRequest`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CreateNodeRequest.

        :param body: The body of this CreateNodeRequest.
        :type body: :class:`huaweicloudsdkcce.v3.NodeCreateRequest`
        """
        self._body = body

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
        if not isinstance(other, CreateNodeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
