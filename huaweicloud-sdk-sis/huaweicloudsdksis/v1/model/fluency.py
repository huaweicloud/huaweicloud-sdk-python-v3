# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Fluency:

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
        'rhythm': 'float',
        'cohesion': 'float'
    }

    attribute_map = {
        'score': 'score',
        'rhythm': 'rhythm',
        'cohesion': 'cohesion'
    }

    def __init__(self, score=None, rhythm=None, cohesion=None):
        """Fluency

        The model defined in huaweicloud sdk

        :param score: 流利度综合得分 0-100
        :type score: float
        :param rhythm: 韵律得分 0-100 韵律指音素在单词和句子中的发音长度是否得当
        :type rhythm: float
        :param cohesion: 连贯性得分 0-100
        :type cohesion: float
        """
        
        

        self._score = None
        self._rhythm = None
        self._cohesion = None
        self.discriminator = None

        self.score = score
        self.rhythm = rhythm
        self.cohesion = cohesion

    @property
    def score(self):
        """Gets the score of this Fluency.

        流利度综合得分 0-100

        :return: The score of this Fluency.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this Fluency.

        流利度综合得分 0-100

        :param score: The score of this Fluency.
        :type score: float
        """
        self._score = score

    @property
    def rhythm(self):
        """Gets the rhythm of this Fluency.

        韵律得分 0-100 韵律指音素在单词和句子中的发音长度是否得当

        :return: The rhythm of this Fluency.
        :rtype: float
        """
        return self._rhythm

    @rhythm.setter
    def rhythm(self, rhythm):
        """Sets the rhythm of this Fluency.

        韵律得分 0-100 韵律指音素在单词和句子中的发音长度是否得当

        :param rhythm: The rhythm of this Fluency.
        :type rhythm: float
        """
        self._rhythm = rhythm

    @property
    def cohesion(self):
        """Gets the cohesion of this Fluency.

        连贯性得分 0-100

        :return: The cohesion of this Fluency.
        :rtype: float
        """
        return self._cohesion

    @cohesion.setter
    def cohesion(self, cohesion):
        """Sets the cohesion of this Fluency.

        连贯性得分 0-100

        :param cohesion: The cohesion of this Fluency.
        :type cohesion: float
        """
        self._cohesion = cohesion

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
        if not isinstance(other, Fluency):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
