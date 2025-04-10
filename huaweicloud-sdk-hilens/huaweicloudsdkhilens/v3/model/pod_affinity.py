# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PodAffinity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_affinity': 'list[MatchExpression]',
        'pod_affinity': 'list[MatchExpression]'
    }

    attribute_map = {
        'node_affinity': 'node_affinity',
        'pod_affinity': 'pod_affinity'
    }

    def __init__(self, node_affinity=None, pod_affinity=None):
        r"""PodAffinity

        The model defined in huaweicloud sdk

        :param node_affinity: 节点亲和规则
        :type node_affinity: list[:class:`huaweicloudsdkhilens.v3.MatchExpression`]
        :param pod_affinity: Pod亲和规则
        :type pod_affinity: list[:class:`huaweicloudsdkhilens.v3.MatchExpression`]
        """
        
        

        self._node_affinity = None
        self._pod_affinity = None
        self.discriminator = None

        if node_affinity is not None:
            self.node_affinity = node_affinity
        if pod_affinity is not None:
            self.pod_affinity = pod_affinity

    @property
    def node_affinity(self):
        r"""Gets the node_affinity of this PodAffinity.

        节点亲和规则

        :return: The node_affinity of this PodAffinity.
        :rtype: list[:class:`huaweicloudsdkhilens.v3.MatchExpression`]
        """
        return self._node_affinity

    @node_affinity.setter
    def node_affinity(self, node_affinity):
        r"""Sets the node_affinity of this PodAffinity.

        节点亲和规则

        :param node_affinity: The node_affinity of this PodAffinity.
        :type node_affinity: list[:class:`huaweicloudsdkhilens.v3.MatchExpression`]
        """
        self._node_affinity = node_affinity

    @property
    def pod_affinity(self):
        r"""Gets the pod_affinity of this PodAffinity.

        Pod亲和规则

        :return: The pod_affinity of this PodAffinity.
        :rtype: list[:class:`huaweicloudsdkhilens.v3.MatchExpression`]
        """
        return self._pod_affinity

    @pod_affinity.setter
    def pod_affinity(self, pod_affinity):
        r"""Sets the pod_affinity of this PodAffinity.

        Pod亲和规则

        :param pod_affinity: The pod_affinity of this PodAffinity.
        :type pod_affinity: list[:class:`huaweicloudsdkhilens.v3.MatchExpression`]
        """
        self._pod_affinity = pod_affinity

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
        if not isinstance(other, PodAffinity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
