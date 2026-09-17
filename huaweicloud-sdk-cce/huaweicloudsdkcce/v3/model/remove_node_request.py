# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RemoveNodeRequest:

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
        'remove_node_system_security_group': 'bool',
        'body': 'RemoveNodesTask'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'remove_node_system_security_group': 'removeNodeSystemSecurityGroup',
        'body': 'body'
    }

    def __init__(self, cluster_id=None, remove_node_system_security_group=None, body=None):
        r"""RemoveNodeRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 集群ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。
        :type cluster_id: str
        :param remove_node_system_security_group: **参数解释**： 移除节点时是否解绑节点默认安全组。 **约束限制**： 不涉及 **取值范围**： - false：移除节点时保留节点默认安全组 - true：移除节点时解绑节点默认安全组  **默认取值**： false
        :type remove_node_system_security_group: bool
        :param body: Body of the RemoveNodeRequest
        :type body: :class:`huaweicloudsdkcce.v3.RemoveNodesTask`
        """
        
        

        self._cluster_id = None
        self._remove_node_system_security_group = None
        self._body = None
        self.discriminator = None

        self.cluster_id = cluster_id
        if remove_node_system_security_group is not None:
            self.remove_node_system_security_group = remove_node_system_security_group
        if body is not None:
            self.body = body

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this RemoveNodeRequest.

        集群ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。

        :return: The cluster_id of this RemoveNodeRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this RemoveNodeRequest.

        集群ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。

        :param cluster_id: The cluster_id of this RemoveNodeRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def remove_node_system_security_group(self):
        r"""Gets the remove_node_system_security_group of this RemoveNodeRequest.

        **参数解释**： 移除节点时是否解绑节点默认安全组。 **约束限制**： 不涉及 **取值范围**： - false：移除节点时保留节点默认安全组 - true：移除节点时解绑节点默认安全组  **默认取值**： false

        :return: The remove_node_system_security_group of this RemoveNodeRequest.
        :rtype: bool
        """
        return self._remove_node_system_security_group

    @remove_node_system_security_group.setter
    def remove_node_system_security_group(self, remove_node_system_security_group):
        r"""Sets the remove_node_system_security_group of this RemoveNodeRequest.

        **参数解释**： 移除节点时是否解绑节点默认安全组。 **约束限制**： 不涉及 **取值范围**： - false：移除节点时保留节点默认安全组 - true：移除节点时解绑节点默认安全组  **默认取值**： false

        :param remove_node_system_security_group: The remove_node_system_security_group of this RemoveNodeRequest.
        :type remove_node_system_security_group: bool
        """
        self._remove_node_system_security_group = remove_node_system_security_group

    @property
    def body(self):
        r"""Gets the body of this RemoveNodeRequest.

        :return: The body of this RemoveNodeRequest.
        :rtype: :class:`huaweicloudsdkcce.v3.RemoveNodesTask`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this RemoveNodeRequest.

        :param body: The body of this RemoveNodeRequest.
        :type body: :class:`huaweicloudsdkcce.v3.RemoveNodesTask`
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
        if not isinstance(other, RemoveNodeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
