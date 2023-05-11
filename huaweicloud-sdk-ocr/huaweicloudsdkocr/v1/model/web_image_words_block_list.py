# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WebImageWordsBlockList:

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
        'confidence': 'float',
        'location': 'list[list[int]]',
        'font_list': 'list[str]',
        'font_scores': 'list[float]'
    }

    attribute_map = {
        'words': 'words',
        'confidence': 'confidence',
        'location': 'location',
        'font_list': 'font_list',
        'font_scores': 'font_scores'
    }

    def __init__(self, words=None, confidence=None, location=None, font_list=None, font_scores=None):
        """WebImageWordsBlockList

        The model defined in huaweicloud sdk

        :param words: 文字块识别结果。 
        :type words: str
        :param confidence: 相关字段的置信度信息，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。 置信度由算法给出，不直接等价于对应字段的准确率。 
        :type confidence: float
        :param location: 文字块的区域位置信息，列表形式，包含文字区域四个顶点的二维坐标（x,y）;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 
        :type location: list[list[int]]
        :param font_list: 文字块所属字体类型，列表形式，表示与文字块的文字最接近的字体类型。 
        :type font_list: list[str]
        :param font_scores: 文字块所属字体类型的概率，列表形式，与font_list一一对应，表示文字块的文字属于某种字体类型的概率。 
        :type font_scores: list[float]
        """
        
        

        self._words = None
        self._confidence = None
        self._location = None
        self._font_list = None
        self._font_scores = None
        self.discriminator = None

        if words is not None:
            self.words = words
        if confidence is not None:
            self.confidence = confidence
        if location is not None:
            self.location = location
        if font_list is not None:
            self.font_list = font_list
        if font_scores is not None:
            self.font_scores = font_scores

    @property
    def words(self):
        """Gets the words of this WebImageWordsBlockList.

        文字块识别结果。 

        :return: The words of this WebImageWordsBlockList.
        :rtype: str
        """
        return self._words

    @words.setter
    def words(self, words):
        """Sets the words of this WebImageWordsBlockList.

        文字块识别结果。 

        :param words: The words of this WebImageWordsBlockList.
        :type words: str
        """
        self._words = words

    @property
    def confidence(self):
        """Gets the confidence of this WebImageWordsBlockList.

        相关字段的置信度信息，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。 置信度由算法给出，不直接等价于对应字段的准确率。 

        :return: The confidence of this WebImageWordsBlockList.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this WebImageWordsBlockList.

        相关字段的置信度信息，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。 置信度由算法给出，不直接等价于对应字段的准确率。 

        :param confidence: The confidence of this WebImageWordsBlockList.
        :type confidence: float
        """
        self._confidence = confidence

    @property
    def location(self):
        """Gets the location of this WebImageWordsBlockList.

        文字块的区域位置信息，列表形式，包含文字区域四个顶点的二维坐标（x,y）;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :return: The location of this WebImageWordsBlockList.
        :rtype: list[list[int]]
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this WebImageWordsBlockList.

        文字块的区域位置信息，列表形式，包含文字区域四个顶点的二维坐标（x,y）;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :param location: The location of this WebImageWordsBlockList.
        :type location: list[list[int]]
        """
        self._location = location

    @property
    def font_list(self):
        """Gets the font_list of this WebImageWordsBlockList.

        文字块所属字体类型，列表形式，表示与文字块的文字最接近的字体类型。 

        :return: The font_list of this WebImageWordsBlockList.
        :rtype: list[str]
        """
        return self._font_list

    @font_list.setter
    def font_list(self, font_list):
        """Sets the font_list of this WebImageWordsBlockList.

        文字块所属字体类型，列表形式，表示与文字块的文字最接近的字体类型。 

        :param font_list: The font_list of this WebImageWordsBlockList.
        :type font_list: list[str]
        """
        self._font_list = font_list

    @property
    def font_scores(self):
        """Gets the font_scores of this WebImageWordsBlockList.

        文字块所属字体类型的概率，列表形式，与font_list一一对应，表示文字块的文字属于某种字体类型的概率。 

        :return: The font_scores of this WebImageWordsBlockList.
        :rtype: list[float]
        """
        return self._font_scores

    @font_scores.setter
    def font_scores(self, font_scores):
        """Sets the font_scores of this WebImageWordsBlockList.

        文字块所属字体类型的概率，列表形式，与font_list一一对应，表示文字块的文字属于某种字体类型的概率。 

        :param font_scores: The font_scores of this WebImageWordsBlockList.
        :type font_scores: list[float]
        """
        self._font_scores = font_scores

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
        if not isinstance(other, WebImageWordsBlockList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
