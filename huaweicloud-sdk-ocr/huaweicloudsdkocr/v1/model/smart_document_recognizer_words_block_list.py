# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SmartDocumentRecognizerWordsBlockList:

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
        'location': 'list[list[int]]',
        'confidence': 'float',
        'char_list': 'list[SmartDocumentRecognizerCharList]'
    }

    attribute_map = {
        'words': 'words',
        'location': 'location',
        'confidence': 'confidence',
        'char_list': 'char_list'
    }

    def __init__(self, words=None, location=None, confidence=None, char_list=None):
        r"""SmartDocumentRecognizerWordsBlockList

        The model defined in huaweicloud sdk

        :param words: 文字块识别结果。 
        :type words: str
        :param location: 文字块的区域位置信息，列表形式，包含文字区域四个顶点的二维坐标（x,y）;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 
        :type location: list[list[int]]
        :param confidence: 文字块识别结果的置信度。 
        :type confidence: float
        :param char_list: 当入参character_mode为True时返回该字段，表示当前文字块对应的单字符识别列表，输出顺序从左到右，先上后下。 
        :type char_list: list[:class:`huaweicloudsdkocr.v1.SmartDocumentRecognizerCharList`]
        """
        
        

        self._words = None
        self._location = None
        self._confidence = None
        self._char_list = None
        self.discriminator = None

        if words is not None:
            self.words = words
        if location is not None:
            self.location = location
        if confidence is not None:
            self.confidence = confidence
        if char_list is not None:
            self.char_list = char_list

    @property
    def words(self):
        r"""Gets the words of this SmartDocumentRecognizerWordsBlockList.

        文字块识别结果。 

        :return: The words of this SmartDocumentRecognizerWordsBlockList.
        :rtype: str
        """
        return self._words

    @words.setter
    def words(self, words):
        r"""Sets the words of this SmartDocumentRecognizerWordsBlockList.

        文字块识别结果。 

        :param words: The words of this SmartDocumentRecognizerWordsBlockList.
        :type words: str
        """
        self._words = words

    @property
    def location(self):
        r"""Gets the location of this SmartDocumentRecognizerWordsBlockList.

        文字块的区域位置信息，列表形式，包含文字区域四个顶点的二维坐标（x,y）;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :return: The location of this SmartDocumentRecognizerWordsBlockList.
        :rtype: list[list[int]]
        """
        return self._location

    @location.setter
    def location(self, location):
        r"""Sets the location of this SmartDocumentRecognizerWordsBlockList.

        文字块的区域位置信息，列表形式，包含文字区域四个顶点的二维坐标（x,y）;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :param location: The location of this SmartDocumentRecognizerWordsBlockList.
        :type location: list[list[int]]
        """
        self._location = location

    @property
    def confidence(self):
        r"""Gets the confidence of this SmartDocumentRecognizerWordsBlockList.

        文字块识别结果的置信度。 

        :return: The confidence of this SmartDocumentRecognizerWordsBlockList.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        r"""Sets the confidence of this SmartDocumentRecognizerWordsBlockList.

        文字块识别结果的置信度。 

        :param confidence: The confidence of this SmartDocumentRecognizerWordsBlockList.
        :type confidence: float
        """
        self._confidence = confidence

    @property
    def char_list(self):
        r"""Gets the char_list of this SmartDocumentRecognizerWordsBlockList.

        当入参character_mode为True时返回该字段，表示当前文字块对应的单字符识别列表，输出顺序从左到右，先上后下。 

        :return: The char_list of this SmartDocumentRecognizerWordsBlockList.
        :rtype: list[:class:`huaweicloudsdkocr.v1.SmartDocumentRecognizerCharList`]
        """
        return self._char_list

    @char_list.setter
    def char_list(self, char_list):
        r"""Sets the char_list of this SmartDocumentRecognizerWordsBlockList.

        当入参character_mode为True时返回该字段，表示当前文字块对应的单字符识别列表，输出顺序从左到右，先上后下。 

        :param char_list: The char_list of this SmartDocumentRecognizerWordsBlockList.
        :type char_list: list[:class:`huaweicloudsdkocr.v1.SmartDocumentRecognizerCharList`]
        """
        self._char_list = char_list

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SmartDocumentRecognizerWordsBlockList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
