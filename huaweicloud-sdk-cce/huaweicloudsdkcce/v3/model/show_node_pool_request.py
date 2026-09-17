# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowNodePoolRequest:

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
        'nodepool_id': 'str',
        'advance_status': 'bool'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'nodepool_id': 'nodepool_id',
        'advance_status': 'advanceStatus'
    }

    def __init__(self, cluster_id=None, nodepool_id=None, advance_status=None):
        r"""ShowNodePoolRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 集群ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。
        :type cluster_id: str
        :param nodepool_id: 节点池ID
        :type nodepool_id: str
        :param advance_status: **参数解释：** 节点池conditions是否反映整个节点池整体状态。 **约束限制：** 不涉及 **取值范围：** - true: 节点池的conditions反映整个节点池整体状态。 - false: 节点池的conditions仅反映默认伸缩组的状态。  **默认取值：** 不指定时默认为false
        :type advance_status: bool
        """
        
        

        self._cluster_id = None
        self._nodepool_id = None
        self._advance_status = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.nodepool_id = nodepool_id
        if advance_status is not None:
            self.advance_status = advance_status

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ShowNodePoolRequest.

        集群ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。

        :return: The cluster_id of this ShowNodePoolRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ShowNodePoolRequest.

        集群ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。

        :param cluster_id: The cluster_id of this ShowNodePoolRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def nodepool_id(self):
        r"""Gets the nodepool_id of this ShowNodePoolRequest.

        节点池ID

        :return: The nodepool_id of this ShowNodePoolRequest.
        :rtype: str
        """
        return self._nodepool_id

    @nodepool_id.setter
    def nodepool_id(self, nodepool_id):
        r"""Sets the nodepool_id of this ShowNodePoolRequest.

        节点池ID

        :param nodepool_id: The nodepool_id of this ShowNodePoolRequest.
        :type nodepool_id: str
        """
        self._nodepool_id = nodepool_id

    @property
    def advance_status(self):
        r"""Gets the advance_status of this ShowNodePoolRequest.

        **参数解释：** 节点池conditions是否反映整个节点池整体状态。 **约束限制：** 不涉及 **取值范围：** - true: 节点池的conditions反映整个节点池整体状态。 - false: 节点池的conditions仅反映默认伸缩组的状态。  **默认取值：** 不指定时默认为false

        :return: The advance_status of this ShowNodePoolRequest.
        :rtype: bool
        """
        return self._advance_status

    @advance_status.setter
    def advance_status(self, advance_status):
        r"""Sets the advance_status of this ShowNodePoolRequest.

        **参数解释：** 节点池conditions是否反映整个节点池整体状态。 **约束限制：** 不涉及 **取值范围：** - true: 节点池的conditions反映整个节点池整体状态。 - false: 节点池的conditions仅反映默认伸缩组的状态。  **默认取值：** 不指定时默认为false

        :param advance_status: The advance_status of this ShowNodePoolRequest.
        :type advance_status: bool
        """
        self._advance_status = advance_status

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
        if not isinstance(other, ShowNodePoolRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
