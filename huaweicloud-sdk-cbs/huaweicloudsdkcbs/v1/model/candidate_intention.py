# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CandidateIntention:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'candidate_intention': 'str',
        'candidate_confidence': 'float'
    }

    attribute_map = {
        'candidate_intention': 'candidate_intention',
        'candidate_confidence': 'candidate_confidence'
    }

    def __init__(self, candidate_intention=None, candidate_confidence=None):
        """CandidateIntention

        The model defined in huaweicloud sdk

        :param candidate_intention: 候选意图。
        :type candidate_intention: str
        :param candidate_confidence: 候选意图置信度。
        :type candidate_confidence: float
        """
        
        

        self._candidate_intention = None
        self._candidate_confidence = None
        self.discriminator = None

        self.candidate_intention = candidate_intention
        self.candidate_confidence = candidate_confidence

    @property
    def candidate_intention(self):
        """Gets the candidate_intention of this CandidateIntention.

        候选意图。

        :return: The candidate_intention of this CandidateIntention.
        :rtype: str
        """
        return self._candidate_intention

    @candidate_intention.setter
    def candidate_intention(self, candidate_intention):
        """Sets the candidate_intention of this CandidateIntention.

        候选意图。

        :param candidate_intention: The candidate_intention of this CandidateIntention.
        :type candidate_intention: str
        """
        self._candidate_intention = candidate_intention

    @property
    def candidate_confidence(self):
        """Gets the candidate_confidence of this CandidateIntention.

        候选意图置信度。

        :return: The candidate_confidence of this CandidateIntention.
        :rtype: float
        """
        return self._candidate_confidence

    @candidate_confidence.setter
    def candidate_confidence(self, candidate_confidence):
        """Sets the candidate_confidence of this CandidateIntention.

        候选意图置信度。

        :param candidate_confidence: The candidate_confidence of this CandidateIntention.
        :type candidate_confidence: float
        """
        self._candidate_confidence = candidate_confidence

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
        if not isinstance(other, CandidateIntention):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
