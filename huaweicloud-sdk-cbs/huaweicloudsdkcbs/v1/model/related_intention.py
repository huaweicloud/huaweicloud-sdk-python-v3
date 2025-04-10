# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RelatedIntention:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'intention': 'str',
        'confidence': 'float'
    }

    attribute_map = {
        'intention': 'intention',
        'confidence': 'confidence'
    }

    def __init__(self, intention=None, confidence=None):
        r"""RelatedIntention

        The model defined in huaweicloud sdk

        :param intention: 意图名称。
        :type intention: str
        :param confidence: 意图置信度。
        :type confidence: float
        """
        
        

        self._intention = None
        self._confidence = None
        self.discriminator = None

        self.intention = intention
        if confidence is not None:
            self.confidence = confidence

    @property
    def intention(self):
        r"""Gets the intention of this RelatedIntention.

        意图名称。

        :return: The intention of this RelatedIntention.
        :rtype: str
        """
        return self._intention

    @intention.setter
    def intention(self, intention):
        r"""Sets the intention of this RelatedIntention.

        意图名称。

        :param intention: The intention of this RelatedIntention.
        :type intention: str
        """
        self._intention = intention

    @property
    def confidence(self):
        r"""Gets the confidence of this RelatedIntention.

        意图置信度。

        :return: The confidence of this RelatedIntention.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        r"""Sets the confidence of this RelatedIntention.

        意图置信度。

        :param confidence: The confidence of this RelatedIntention.
        :type confidence: float
        """
        self._confidence = confidence

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
        if not isinstance(other, RelatedIntention):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
