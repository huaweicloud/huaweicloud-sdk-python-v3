# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WeightPodAffinityTerms:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pod_affinity_term': 'WeightPodAffinityTermsPodAffinityTerm',
        'weight': 'int'
    }

    attribute_map = {
        'pod_affinity_term': 'podAffinityTerm',
        'weight': 'weight'
    }

    def __init__(self, pod_affinity_term=None, weight=None):
        """WeightPodAffinityTerms

        The model defined in huaweicloud sdk

        :param pod_affinity_term: 
        :type pod_affinity_term: :class:`huaweicloudsdkief.v1.WeightPodAffinityTermsPodAffinityTerm`
        :param weight: 权重，范围为1-100
        :type weight: int
        """
        
        

        self._pod_affinity_term = None
        self._weight = None
        self.discriminator = None

        if pod_affinity_term is not None:
            self.pod_affinity_term = pod_affinity_term
        if weight is not None:
            self.weight = weight

    @property
    def pod_affinity_term(self):
        """Gets the pod_affinity_term of this WeightPodAffinityTerms.

        :return: The pod_affinity_term of this WeightPodAffinityTerms.
        :rtype: :class:`huaweicloudsdkief.v1.WeightPodAffinityTermsPodAffinityTerm`
        """
        return self._pod_affinity_term

    @pod_affinity_term.setter
    def pod_affinity_term(self, pod_affinity_term):
        """Sets the pod_affinity_term of this WeightPodAffinityTerms.

        :param pod_affinity_term: The pod_affinity_term of this WeightPodAffinityTerms.
        :type pod_affinity_term: :class:`huaweicloudsdkief.v1.WeightPodAffinityTermsPodAffinityTerm`
        """
        self._pod_affinity_term = pod_affinity_term

    @property
    def weight(self):
        """Gets the weight of this WeightPodAffinityTerms.

        权重，范围为1-100

        :return: The weight of this WeightPodAffinityTerms.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this WeightPodAffinityTerms.

        权重，范围为1-100

        :param weight: The weight of this WeightPodAffinityTerms.
        :type weight: int
        """
        self._weight = weight

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
        if not isinstance(other, WeightPodAffinityTerms):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
