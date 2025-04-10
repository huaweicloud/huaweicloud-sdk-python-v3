# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttributesExpression:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'probability': 'float'
    }

    attribute_map = {
        'type': 'type',
        'probability': 'probability'
    }

    def __init__(self, type=None, probability=None):
        r"""AttributesExpression

        The model defined in huaweicloud sdk

        :param type: 人脸表情类型： • neutral：中性 • happy：高兴 • fear：害怕 • surprise：惊讶 • sad：伤心 • angry：生气 • disgust：厌恶 • unknown：图片质量问题导致未识别
        :type type: str
        :param probability: 表情置信度，取值范围[0-1]。
        :type probability: float
        """
        
        

        self._type = None
        self._probability = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if probability is not None:
            self.probability = probability

    @property
    def type(self):
        r"""Gets the type of this AttributesExpression.

        人脸表情类型： • neutral：中性 • happy：高兴 • fear：害怕 • surprise：惊讶 • sad：伤心 • angry：生气 • disgust：厌恶 • unknown：图片质量问题导致未识别

        :return: The type of this AttributesExpression.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this AttributesExpression.

        人脸表情类型： • neutral：中性 • happy：高兴 • fear：害怕 • surprise：惊讶 • sad：伤心 • angry：生气 • disgust：厌恶 • unknown：图片质量问题导致未识别

        :param type: The type of this AttributesExpression.
        :type type: str
        """
        self._type = type

    @property
    def probability(self):
        r"""Gets the probability of this AttributesExpression.

        表情置信度，取值范围[0-1]。

        :return: The probability of this AttributesExpression.
        :rtype: float
        """
        return self._probability

    @probability.setter
    def probability(self, probability):
        r"""Sets the probability of this AttributesExpression.

        表情置信度，取值范围[0-1]。

        :param probability: The probability of this AttributesExpression.
        :type probability: float
        """
        self._probability = probability

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
        if not isinstance(other, AttributesExpression):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
