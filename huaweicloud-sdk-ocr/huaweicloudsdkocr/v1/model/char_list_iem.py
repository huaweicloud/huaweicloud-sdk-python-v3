# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CharListIem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'char': 'str',
        'char_confidence': 'float',
        'char_location': 'list[list[int]]'
    }

    attribute_map = {
        'char': 'char',
        'char_confidence': 'char_confidence',
        'char_location': 'char_location'
    }

    def __init__(self, char=None, char_confidence=None, char_location=None):
        """CharListIem

        The model defined in huaweicloud sdk

        :param char: 单字符识别结果。 
        :type char: str
        :param char_confidence: 单字符的置信度，置信度越大，表示本次识别的文字的可靠性越高，在统计意义上，置信度越大，准确率越高。置信度由算法给出，不直接等价于对应字段的准确率。 
        :type char_confidence: float
        :param char_location: 单字符的位置信息，列表形式，分别表示文字块4个顶点的x, y坐标;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 
        :type char_location: list[list[int]]
        """
        
        

        self._char = None
        self._char_confidence = None
        self._char_location = None
        self.discriminator = None

        if char is not None:
            self.char = char
        if char_confidence is not None:
            self.char_confidence = char_confidence
        if char_location is not None:
            self.char_location = char_location

    @property
    def char(self):
        """Gets the char of this CharListIem.

        单字符识别结果。 

        :return: The char of this CharListIem.
        :rtype: str
        """
        return self._char

    @char.setter
    def char(self, char):
        """Sets the char of this CharListIem.

        单字符识别结果。 

        :param char: The char of this CharListIem.
        :type char: str
        """
        self._char = char

    @property
    def char_confidence(self):
        """Gets the char_confidence of this CharListIem.

        单字符的置信度，置信度越大，表示本次识别的文字的可靠性越高，在统计意义上，置信度越大，准确率越高。置信度由算法给出，不直接等价于对应字段的准确率。 

        :return: The char_confidence of this CharListIem.
        :rtype: float
        """
        return self._char_confidence

    @char_confidence.setter
    def char_confidence(self, char_confidence):
        """Sets the char_confidence of this CharListIem.

        单字符的置信度，置信度越大，表示本次识别的文字的可靠性越高，在统计意义上，置信度越大，准确率越高。置信度由算法给出，不直接等价于对应字段的准确率。 

        :param char_confidence: The char_confidence of this CharListIem.
        :type char_confidence: float
        """
        self._char_confidence = char_confidence

    @property
    def char_location(self):
        """Gets the char_location of this CharListIem.

        单字符的位置信息，列表形式，分别表示文字块4个顶点的x, y坐标;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :return: The char_location of this CharListIem.
        :rtype: list[list[int]]
        """
        return self._char_location

    @char_location.setter
    def char_location(self, char_location):
        """Sets the char_location of this CharListIem.

        单字符的位置信息，列表形式，分别表示文字块4个顶点的x, y坐标;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :param char_location: The char_location of this CharListIem.
        :type char_location: list[list[int]]
        """
        self._char_location = char_location

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
        if not isinstance(other, CharListIem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
