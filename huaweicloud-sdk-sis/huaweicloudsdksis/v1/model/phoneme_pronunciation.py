# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PhonemePronunciation:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'score': 'float',
        'gop': 'float'
    }

    attribute_map = {
        'score': 'score',
        'gop': 'gop'
    }

    def __init__(self, score=None, gop=None):
        """PhonemePronunciation - a model defined in huaweicloud sdk"""
        
        

        self._score = None
        self._gop = None
        self.discriminator = None

        self.score = score
        self.gop = gop

    @property
    def score(self):
        """Gets the score of this PhonemePronunciation.

        

        :return: The score of this PhonemePronunciation.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this PhonemePronunciation.

        

        :param score: The score of this PhonemePronunciation.
        :type: float
        """
        self._score = score

    @property
    def gop(self):
        """Gets the gop of this PhonemePronunciation.

        

        :return: The gop of this PhonemePronunciation.
        :rtype: float
        """
        return self._gop

    @gop.setter
    def gop(self, gop):
        """Sets the gop of this PhonemePronunciation.

        

        :param gop: The gop of this PhonemePronunciation.
        :type: float
        """
        self._gop = gop

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
        if not isinstance(other, PhonemePronunciation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other