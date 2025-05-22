# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateLogicalClusterInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'logical_cluster_name': 'str',
        'cluster_rings': 'list[ClusterRing]'
    }

    attribute_map = {
        'logical_cluster_name': 'logical_cluster_name',
        'cluster_rings': 'cluster_rings'
    }

    def __init__(self, logical_cluster_name=None, cluster_rings=None):
        r"""CreateLogicalClusterInfo

        The model defined in huaweicloud sdk

        :param logical_cluster_name: **参数解释**： 逻辑集群名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type logical_cluster_name: str
        :param cluster_rings: **参数解释**： 逻辑集群环信息。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type cluster_rings: list[:class:`huaweicloudsdkdws.v2.ClusterRing`]
        """
        
        

        self._logical_cluster_name = None
        self._cluster_rings = None
        self.discriminator = None

        self.logical_cluster_name = logical_cluster_name
        self.cluster_rings = cluster_rings

    @property
    def logical_cluster_name(self):
        r"""Gets the logical_cluster_name of this CreateLogicalClusterInfo.

        **参数解释**： 逻辑集群名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The logical_cluster_name of this CreateLogicalClusterInfo.
        :rtype: str
        """
        return self._logical_cluster_name

    @logical_cluster_name.setter
    def logical_cluster_name(self, logical_cluster_name):
        r"""Sets the logical_cluster_name of this CreateLogicalClusterInfo.

        **参数解释**： 逻辑集群名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param logical_cluster_name: The logical_cluster_name of this CreateLogicalClusterInfo.
        :type logical_cluster_name: str
        """
        self._logical_cluster_name = logical_cluster_name

    @property
    def cluster_rings(self):
        r"""Gets the cluster_rings of this CreateLogicalClusterInfo.

        **参数解释**： 逻辑集群环信息。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The cluster_rings of this CreateLogicalClusterInfo.
        :rtype: list[:class:`huaweicloudsdkdws.v2.ClusterRing`]
        """
        return self._cluster_rings

    @cluster_rings.setter
    def cluster_rings(self, cluster_rings):
        r"""Sets the cluster_rings of this CreateLogicalClusterInfo.

        **参数解释**： 逻辑集群环信息。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param cluster_rings: The cluster_rings of this CreateLogicalClusterInfo.
        :type cluster_rings: list[:class:`huaweicloudsdkdws.v2.ClusterRing`]
        """
        self._cluster_rings = cluster_rings

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
        if not isinstance(other, CreateLogicalClusterInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
