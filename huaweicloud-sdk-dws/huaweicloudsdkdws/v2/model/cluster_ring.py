# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterRing:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ring_hosts': 'list[RingHost]',
        'un_shrinkable_cluster_ring': 'bool'
    }

    attribute_map = {
        'ring_hosts': 'ring_hosts',
        'un_shrinkable_cluster_ring': 'un_shrinkable_cluster_ring'
    }

    def __init__(self, ring_hosts=None, un_shrinkable_cluster_ring=None):
        r"""ClusterRing

        The model defined in huaweicloud sdk

        :param ring_hosts: **参数解释**： 集群主机信息。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type ring_hosts: list[:class:`huaweicloudsdkdws.v2.RingHost`]
        :param un_shrinkable_cluster_ring: **参数解释**： 是否可以缩容。 **约束限制**： 不涉及。 **取值范围**： false|true。 **默认取值**： 不涉及。
        :type un_shrinkable_cluster_ring: bool
        """
        
        

        self._ring_hosts = None
        self._un_shrinkable_cluster_ring = None
        self.discriminator = None

        self.ring_hosts = ring_hosts
        if un_shrinkable_cluster_ring is not None:
            self.un_shrinkable_cluster_ring = un_shrinkable_cluster_ring

    @property
    def ring_hosts(self):
        r"""Gets the ring_hosts of this ClusterRing.

        **参数解释**： 集群主机信息。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The ring_hosts of this ClusterRing.
        :rtype: list[:class:`huaweicloudsdkdws.v2.RingHost`]
        """
        return self._ring_hosts

    @ring_hosts.setter
    def ring_hosts(self, ring_hosts):
        r"""Sets the ring_hosts of this ClusterRing.

        **参数解释**： 集群主机信息。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param ring_hosts: The ring_hosts of this ClusterRing.
        :type ring_hosts: list[:class:`huaweicloudsdkdws.v2.RingHost`]
        """
        self._ring_hosts = ring_hosts

    @property
    def un_shrinkable_cluster_ring(self):
        r"""Gets the un_shrinkable_cluster_ring of this ClusterRing.

        **参数解释**： 是否可以缩容。 **约束限制**： 不涉及。 **取值范围**： false|true。 **默认取值**： 不涉及。

        :return: The un_shrinkable_cluster_ring of this ClusterRing.
        :rtype: bool
        """
        return self._un_shrinkable_cluster_ring

    @un_shrinkable_cluster_ring.setter
    def un_shrinkable_cluster_ring(self, un_shrinkable_cluster_ring):
        r"""Sets the un_shrinkable_cluster_ring of this ClusterRing.

        **参数解释**： 是否可以缩容。 **约束限制**： 不涉及。 **取值范围**： false|true。 **默认取值**： 不涉及。

        :param un_shrinkable_cluster_ring: The un_shrinkable_cluster_ring of this ClusterRing.
        :type un_shrinkable_cluster_ring: bool
        """
        self._un_shrinkable_cluster_ring = un_shrinkable_cluster_ring

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
        if not isinstance(other, ClusterRing):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
