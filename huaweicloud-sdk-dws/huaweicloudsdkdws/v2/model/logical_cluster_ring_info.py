# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LogicalClusterRingInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ring_hosts': 'list[RingHost]'
    }

    attribute_map = {
        'ring_hosts': 'ring_hosts'
    }

    def __init__(self, ring_hosts=None):
        r"""LogicalClusterRingInfo

        The model defined in huaweicloud sdk

        :param ring_hosts: **参数解释**： 集群实例环信息。 **取值范围**： 不涉及。
        :type ring_hosts: list[:class:`huaweicloudsdkdws.v2.RingHost`]
        """
        
        

        self._ring_hosts = None
        self.discriminator = None

        if ring_hosts is not None:
            self.ring_hosts = ring_hosts

    @property
    def ring_hosts(self):
        r"""Gets the ring_hosts of this LogicalClusterRingInfo.

        **参数解释**： 集群实例环信息。 **取值范围**： 不涉及。

        :return: The ring_hosts of this LogicalClusterRingInfo.
        :rtype: list[:class:`huaweicloudsdkdws.v2.RingHost`]
        """
        return self._ring_hosts

    @ring_hosts.setter
    def ring_hosts(self, ring_hosts):
        r"""Sets the ring_hosts of this LogicalClusterRingInfo.

        **参数解释**： 集群实例环信息。 **取值范围**： 不涉及。

        :param ring_hosts: The ring_hosts of this LogicalClusterRingInfo.
        :type ring_hosts: list[:class:`huaweicloudsdkdws.v2.RingHost`]
        """
        self._ring_hosts = ring_hosts

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
        if not isinstance(other, LogicalClusterRingInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
