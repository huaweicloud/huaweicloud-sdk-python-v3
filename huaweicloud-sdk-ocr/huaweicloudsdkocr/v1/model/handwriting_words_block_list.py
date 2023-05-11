# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HandwritingWordsBlockList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'words': 'str',
        'type': 'str',
        'confidence': 'float',
        'location': 'list[list[int]]'
    }

    attribute_map = {
        'words': 'words',
        'type': 'type',
        'confidence': 'confidence',
        'location': 'location'
    }

    def __init__(self, words=None, type=None, confidence=None, location=None):
        """HandwritingWordsBlockList

        The model defined in huaweicloud sdk

        :param words: 文字块识别结果。 
        :type words: str
        :param type: 说明该识别结果所属类型，例如：handwriting。 
        :type type: str
        :param confidence: 文字块words的置信度。 
        :type confidence: float
        :param location: 文字块words的区域位置信息，列表形式，分别表示文字块顶点的x, y坐标;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 
        :type location: list[list[int]]
        """
        
        

        self._words = None
        self._type = None
        self._confidence = None
        self._location = None
        self.discriminator = None

        if words is not None:
            self.words = words
        if type is not None:
            self.type = type
        if confidence is not None:
            self.confidence = confidence
        if location is not None:
            self.location = location

    @property
    def words(self):
        """Gets the words of this HandwritingWordsBlockList.

        文字块识别结果。 

        :return: The words of this HandwritingWordsBlockList.
        :rtype: str
        """
        return self._words

    @words.setter
    def words(self, words):
        """Sets the words of this HandwritingWordsBlockList.

        文字块识别结果。 

        :param words: The words of this HandwritingWordsBlockList.
        :type words: str
        """
        self._words = words

    @property
    def type(self):
        """Gets the type of this HandwritingWordsBlockList.

        说明该识别结果所属类型，例如：handwriting。 

        :return: The type of this HandwritingWordsBlockList.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this HandwritingWordsBlockList.

        说明该识别结果所属类型，例如：handwriting。 

        :param type: The type of this HandwritingWordsBlockList.
        :type type: str
        """
        self._type = type

    @property
    def confidence(self):
        """Gets the confidence of this HandwritingWordsBlockList.

        文字块words的置信度。 

        :return: The confidence of this HandwritingWordsBlockList.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this HandwritingWordsBlockList.

        文字块words的置信度。 

        :param confidence: The confidence of this HandwritingWordsBlockList.
        :type confidence: float
        """
        self._confidence = confidence

    @property
    def location(self):
        """Gets the location of this HandwritingWordsBlockList.

        文字块words的区域位置信息，列表形式，分别表示文字块顶点的x, y坐标;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :return: The location of this HandwritingWordsBlockList.
        :rtype: list[list[int]]
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this HandwritingWordsBlockList.

        文字块words的区域位置信息，列表形式，分别表示文字块顶点的x, y坐标;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :param location: The location of this HandwritingWordsBlockList.
        :type location: list[list[int]]
        """
        self._location = location

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
        if not isinstance(other, HandwritingWordsBlockList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
