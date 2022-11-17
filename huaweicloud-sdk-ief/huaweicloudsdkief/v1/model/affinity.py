# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Affinity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_affinity': 'AffinityNodeAffinity',
        'pod_affinity': 'AffinityPodAffinity',
        'pod_anti_affinity': 'AffinityPodAntiAffinity'
    }

    attribute_map = {
        'node_affinity': 'nodeAffinity',
        'pod_affinity': 'podAffinity',
        'pod_anti_affinity': 'podAntiAffinity'
    }

    def __init__(self, node_affinity=None, pod_affinity=None, pod_anti_affinity=None):
        """Affinity

        The model defined in huaweicloud sdk

        :param node_affinity: 
        :type node_affinity: :class:`huaweicloudsdkief.v1.AffinityNodeAffinity`
        :param pod_affinity: 
        :type pod_affinity: :class:`huaweicloudsdkief.v1.AffinityPodAffinity`
        :param pod_anti_affinity: 
        :type pod_anti_affinity: :class:`huaweicloudsdkief.v1.AffinityPodAntiAffinity`
        """
        
        

        self._node_affinity = None
        self._pod_affinity = None
        self._pod_anti_affinity = None
        self.discriminator = None

        if node_affinity is not None:
            self.node_affinity = node_affinity
        if pod_affinity is not None:
            self.pod_affinity = pod_affinity
        if pod_anti_affinity is not None:
            self.pod_anti_affinity = pod_anti_affinity

    @property
    def node_affinity(self):
        """Gets the node_affinity of this Affinity.

        :return: The node_affinity of this Affinity.
        :rtype: :class:`huaweicloudsdkief.v1.AffinityNodeAffinity`
        """
        return self._node_affinity

    @node_affinity.setter
    def node_affinity(self, node_affinity):
        """Sets the node_affinity of this Affinity.

        :param node_affinity: The node_affinity of this Affinity.
        :type node_affinity: :class:`huaweicloudsdkief.v1.AffinityNodeAffinity`
        """
        self._node_affinity = node_affinity

    @property
    def pod_affinity(self):
        """Gets the pod_affinity of this Affinity.

        :return: The pod_affinity of this Affinity.
        :rtype: :class:`huaweicloudsdkief.v1.AffinityPodAffinity`
        """
        return self._pod_affinity

    @pod_affinity.setter
    def pod_affinity(self, pod_affinity):
        """Sets the pod_affinity of this Affinity.

        :param pod_affinity: The pod_affinity of this Affinity.
        :type pod_affinity: :class:`huaweicloudsdkief.v1.AffinityPodAffinity`
        """
        self._pod_affinity = pod_affinity

    @property
    def pod_anti_affinity(self):
        """Gets the pod_anti_affinity of this Affinity.

        :return: The pod_anti_affinity of this Affinity.
        :rtype: :class:`huaweicloudsdkief.v1.AffinityPodAntiAffinity`
        """
        return self._pod_anti_affinity

    @pod_anti_affinity.setter
    def pod_anti_affinity(self, pod_anti_affinity):
        """Sets the pod_anti_affinity of this Affinity.

        :param pod_anti_affinity: The pod_anti_affinity of this Affinity.
        :type pod_anti_affinity: :class:`huaweicloudsdkief.v1.AffinityPodAntiAffinity`
        """
        self._pod_anti_affinity = pod_anti_affinity

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
        if not isinstance(other, Affinity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
