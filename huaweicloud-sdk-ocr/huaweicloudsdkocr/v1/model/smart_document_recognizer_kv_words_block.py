# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SmartDocumentRecognizerKVWordsBlock:

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
        'type': 'str'
    }

    attribute_map = {
        'words': 'words',
        'location': 'location',
        'type': 'type'
    }

    def __init__(self, words=None, location=None, type=None):
        r"""SmartDocumentRecognizerKVWordsBlock

        The model defined in huaweicloud sdk

        :param words: 文字块识别结果。       
        :type words: str
        :param location: 文字块的区域位置信息，列表形式，包含文字区域四个顶点的二维坐标（x,y）;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 
        :type location: list[list[int]]
        :param type: 类型。 
        :type type: str
        """
        
        

        self._words = None
        self._location = None
        self._type = None
        self.discriminator = None

        if words is not None:
            self.words = words
        if location is not None:
            self.location = location
        if type is not None:
            self.type = type

    @property
    def words(self):
        r"""Gets the words of this SmartDocumentRecognizerKVWordsBlock.

        文字块识别结果。       

        :return: The words of this SmartDocumentRecognizerKVWordsBlock.
        :rtype: str
        """
        return self._words

    @words.setter
    def words(self, words):
        r"""Sets the words of this SmartDocumentRecognizerKVWordsBlock.

        文字块识别结果。       

        :param words: The words of this SmartDocumentRecognizerKVWordsBlock.
        :type words: str
        """
        self._words = words

    @property
    def location(self):
        r"""Gets the location of this SmartDocumentRecognizerKVWordsBlock.

        文字块的区域位置信息，列表形式，包含文字区域四个顶点的二维坐标（x,y）;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :return: The location of this SmartDocumentRecognizerKVWordsBlock.
        :rtype: list[list[int]]
        """
        return self._location

    @location.setter
    def location(self, location):
        r"""Sets the location of this SmartDocumentRecognizerKVWordsBlock.

        文字块的区域位置信息，列表形式，包含文字区域四个顶点的二维坐标（x,y）;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :param location: The location of this SmartDocumentRecognizerKVWordsBlock.
        :type location: list[list[int]]
        """
        self._location = location

    @property
    def type(self):
        r"""Gets the type of this SmartDocumentRecognizerKVWordsBlock.

        类型。 

        :return: The type of this SmartDocumentRecognizerKVWordsBlock.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this SmartDocumentRecognizerKVWordsBlock.

        类型。 

        :param type: The type of this SmartDocumentRecognizerKVWordsBlock.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, SmartDocumentRecognizerKVWordsBlock):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
