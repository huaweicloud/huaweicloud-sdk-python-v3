# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HealthCodeWordsBlockList:

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
        'confidence': 'float'
    }

    attribute_map = {
        'words': 'words',
        'location': 'location',
        'confidence': 'confidence'
    }

    def __init__(self, words=None, location=None, confidence=None):
        """HealthCodeWordsBlockList

        The model defined in huaweicloud sdk

        :param words: 文字块识别结果。 
        :type words: str
        :param location: 识别到的文字块的区域位置信息，列表形式，分别表示文字块4个顶点的（x,y）坐标。采用图像坐标系，图像坐标原点为图像左上角，x轴沿水平方向，y轴沿竖直方向。 
        :type location: list[list[int]]
        :param confidence: 各个字段的置信度 
        :type confidence: float
        """
        
        

        self._words = None
        self._location = None
        self._confidence = None
        self.discriminator = None

        if words is not None:
            self.words = words
        if location is not None:
            self.location = location
        if confidence is not None:
            self.confidence = confidence

    @property
    def words(self):
        """Gets the words of this HealthCodeWordsBlockList.

        文字块识别结果。 

        :return: The words of this HealthCodeWordsBlockList.
        :rtype: str
        """
        return self._words

    @words.setter
    def words(self, words):
        """Sets the words of this HealthCodeWordsBlockList.

        文字块识别结果。 

        :param words: The words of this HealthCodeWordsBlockList.
        :type words: str
        """
        self._words = words

    @property
    def location(self):
        """Gets the location of this HealthCodeWordsBlockList.

        识别到的文字块的区域位置信息，列表形式，分别表示文字块4个顶点的（x,y）坐标。采用图像坐标系，图像坐标原点为图像左上角，x轴沿水平方向，y轴沿竖直方向。 

        :return: The location of this HealthCodeWordsBlockList.
        :rtype: list[list[int]]
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this HealthCodeWordsBlockList.

        识别到的文字块的区域位置信息，列表形式，分别表示文字块4个顶点的（x,y）坐标。采用图像坐标系，图像坐标原点为图像左上角，x轴沿水平方向，y轴沿竖直方向。 

        :param location: The location of this HealthCodeWordsBlockList.
        :type location: list[list[int]]
        """
        self._location = location

    @property
    def confidence(self):
        """Gets the confidence of this HealthCodeWordsBlockList.

        各个字段的置信度 

        :return: The confidence of this HealthCodeWordsBlockList.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this HealthCodeWordsBlockList.

        各个字段的置信度 

        :param confidence: The confidence of this HealthCodeWordsBlockList.
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
        if not isinstance(other, HealthCodeWordsBlockList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
