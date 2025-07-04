# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShrinkLogicalClusterRequest:

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
        'logical_cluster_id': 'str',
        'body': 'ShrinkLogicalClusterRequestBody'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'logical_cluster_id': 'logical_cluster_id',
        'body': 'body'
    }

    def __init__(self, cluster_id=None, logical_cluster_id=None, body=None):
        r"""ShrinkLogicalClusterRequest

        The model defined in huaweicloud sdk

        :param cluster_id: **参数解释**： 集群ID。获取方法请参见[获取集群ID](dws_02_00068.xml)。 **约束限制**： 必须是有效的dws集群ID。 **取值范围**： 36位UUID。 **默认取值**： 不涉及。
        :type cluster_id: str
        :param logical_cluster_id: **参数解释**： 逻辑集群id。  **约束限制**： 必须是有效的dws逻辑集群ID。  **取值范围**：  36位UUID。  **默认取值**：  不涉及。
        :type logical_cluster_id: str
        :param body: Body of the ShrinkLogicalClusterRequest
        :type body: :class:`huaweicloudsdkdws.v2.ShrinkLogicalClusterRequestBody`
        """
        
        

        self._cluster_id = None
        self._logical_cluster_id = None
        self._body = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.logical_cluster_id = logical_cluster_id
        if body is not None:
            self.body = body

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ShrinkLogicalClusterRequest.

        **参数解释**： 集群ID。获取方法请参见[获取集群ID](dws_02_00068.xml)。 **约束限制**： 必须是有效的dws集群ID。 **取值范围**： 36位UUID。 **默认取值**： 不涉及。

        :return: The cluster_id of this ShrinkLogicalClusterRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ShrinkLogicalClusterRequest.

        **参数解释**： 集群ID。获取方法请参见[获取集群ID](dws_02_00068.xml)。 **约束限制**： 必须是有效的dws集群ID。 **取值范围**： 36位UUID。 **默认取值**： 不涉及。

        :param cluster_id: The cluster_id of this ShrinkLogicalClusterRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def logical_cluster_id(self):
        r"""Gets the logical_cluster_id of this ShrinkLogicalClusterRequest.

        **参数解释**： 逻辑集群id。  **约束限制**： 必须是有效的dws逻辑集群ID。  **取值范围**：  36位UUID。  **默认取值**：  不涉及。

        :return: The logical_cluster_id of this ShrinkLogicalClusterRequest.
        :rtype: str
        """
        return self._logical_cluster_id

    @logical_cluster_id.setter
    def logical_cluster_id(self, logical_cluster_id):
        r"""Sets the logical_cluster_id of this ShrinkLogicalClusterRequest.

        **参数解释**： 逻辑集群id。  **约束限制**： 必须是有效的dws逻辑集群ID。  **取值范围**：  36位UUID。  **默认取值**：  不涉及。

        :param logical_cluster_id: The logical_cluster_id of this ShrinkLogicalClusterRequest.
        :type logical_cluster_id: str
        """
        self._logical_cluster_id = logical_cluster_id

    @property
    def body(self):
        r"""Gets the body of this ShrinkLogicalClusterRequest.

        :return: The body of this ShrinkLogicalClusterRequest.
        :rtype: :class:`huaweicloudsdkdws.v2.ShrinkLogicalClusterRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ShrinkLogicalClusterRequest.

        :param body: The body of this ShrinkLogicalClusterRequest.
        :type body: :class:`huaweicloudsdkdws.v2.ShrinkLogicalClusterRequestBody`
        """
        self._body = body

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
        if not isinstance(other, ShrinkLogicalClusterRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
