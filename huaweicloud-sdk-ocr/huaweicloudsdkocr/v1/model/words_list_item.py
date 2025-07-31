# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WordsListItem:

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
        'char_list': 'list[CharListItem]'
    }

    attribute_map = {
        'words': 'words',
        'confidence': 'confidence',
        'location': 'location',
        'char_list': 'char_list'
    }

    def __init__(self, words=None, confidence=None, location=None, char_list=None):
        r"""WordsListItem

        The model defined in huaweicloud sdk

        :param words: 文字块识别结果。 
        :type words: str
        :param confidence: 字段的平均置信度，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。置信度由算法给出，不直接等价于对应字段的准确率。 
        :type confidence: float
        :param location: 文字块位置信息，列表形式，分别表示文字块4个顶点的x, y坐标;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 
        :type location: list[list[int]]
        :param char_list: 单元格内文字段列表。输出顺序从左到右，从上到下。仅当入参\&quot;return_text_location\&quot;和\&quot;return_char_location\&quot;同时为true时存在。 
        :type char_list: list[:class:`huaweicloudsdkocr.v1.CharListItem`]
        """
        
        

        self._words = None
        self._confidence = None
        self._location = None
        self._char_list = None
        self.discriminator = None

        if words is not None:
            self.words = words
        if confidence is not None:
            self.confidence = confidence
        if location is not None:
            self.location = location
        if char_list is not None:
            self.char_list = char_list

    @property
    def words(self):
        r"""Gets the words of this WordsListItem.

        文字块识别结果。 

        :return: The words of this WordsListItem.
        :rtype: str
        """
        return self._words

    @words.setter
    def words(self, words):
        r"""Sets the words of this WordsListItem.

        文字块识别结果。 

        :param words: The words of this WordsListItem.
        :type words: str
        """
        self._words = words

    @property
    def confidence(self):
        r"""Gets the confidence of this WordsListItem.

        字段的平均置信度，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。置信度由算法给出，不直接等价于对应字段的准确率。 

        :return: The confidence of this WordsListItem.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        r"""Sets the confidence of this WordsListItem.

        字段的平均置信度，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。置信度由算法给出，不直接等价于对应字段的准确率。 

        :param confidence: The confidence of this WordsListItem.
        :type confidence: float
        """
        self._confidence = confidence

    @property
    def location(self):
        r"""Gets the location of this WordsListItem.

        文字块位置信息，列表形式，分别表示文字块4个顶点的x, y坐标;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :return: The location of this WordsListItem.
        :rtype: list[list[int]]
        """
        return self._location

    @location.setter
    def location(self, location):
        r"""Sets the location of this WordsListItem.

        文字块位置信息，列表形式，分别表示文字块4个顶点的x, y坐标;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :param location: The location of this WordsListItem.
        :type location: list[list[int]]
        """
        self._location = location

    @property
    def char_list(self):
        r"""Gets the char_list of this WordsListItem.

        单元格内文字段列表。输出顺序从左到右，从上到下。仅当入参\"return_text_location\"和\"return_char_location\"同时为true时存在。 

        :return: The char_list of this WordsListItem.
        :rtype: list[:class:`huaweicloudsdkocr.v1.CharListItem`]
        """
        return self._char_list

    @char_list.setter
    def char_list(self, char_list):
        r"""Sets the char_list of this WordsListItem.

        单元格内文字段列表。输出顺序从左到右，从上到下。仅当入参\"return_text_location\"和\"return_char_location\"同时为true时存在。 

        :param char_list: The char_list of this WordsListItem.
        :type char_list: list[:class:`huaweicloudsdkocr.v1.CharListItem`]
        """
        self._char_list = char_list

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
        if not isinstance(other, WordsListItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
