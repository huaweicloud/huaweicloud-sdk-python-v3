# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SealList:

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
        'seal_image': 'str',
        'confidence': 'float',
        'location': 'list[list[int]]',
        'words_block_list': 'list[SealWordsBlockList]'
    }

    attribute_map = {
        'type': 'type',
        'seal_image': 'seal_image',
        'confidence': 'confidence',
        'location': 'location',
        'words_block_list': 'words_block_list'
    }

    def __init__(self, type=None, seal_image=None, confidence=None, location=None, words_block_list=None):
        r"""SealList

        The model defined in huaweicloud sdk

        :param type: 印章类型，当前支持circle（圆形章）、ellipse（椭圆章）、rectangle（方形章）、triangle（三角章）、rhombus（菱形章）五种。 
        :type type: str
        :param seal_image: 提取的单个印章base64编码图片。 
        :type seal_image: str
        :param confidence: 印章位置的置信度。 
        :type confidence: float
        :param location: 印章位置，列表形式，包含印章区域四个顶点的二维坐标（x,y），坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 
        :type location: list[list[int]]
        :param words_block_list: 印章文本块列表。 
        :type words_block_list: list[:class:`huaweicloudsdkocr.v1.SealWordsBlockList`]
        """
        
        

        self._type = None
        self._seal_image = None
        self._confidence = None
        self._location = None
        self._words_block_list = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if seal_image is not None:
            self.seal_image = seal_image
        if confidence is not None:
            self.confidence = confidence
        if location is not None:
            self.location = location
        if words_block_list is not None:
            self.words_block_list = words_block_list

    @property
    def type(self):
        r"""Gets the type of this SealList.

        印章类型，当前支持circle（圆形章）、ellipse（椭圆章）、rectangle（方形章）、triangle（三角章）、rhombus（菱形章）五种。 

        :return: The type of this SealList.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this SealList.

        印章类型，当前支持circle（圆形章）、ellipse（椭圆章）、rectangle（方形章）、triangle（三角章）、rhombus（菱形章）五种。 

        :param type: The type of this SealList.
        :type type: str
        """
        self._type = type

    @property
    def seal_image(self):
        r"""Gets the seal_image of this SealList.

        提取的单个印章base64编码图片。 

        :return: The seal_image of this SealList.
        :rtype: str
        """
        return self._seal_image

    @seal_image.setter
    def seal_image(self, seal_image):
        r"""Sets the seal_image of this SealList.

        提取的单个印章base64编码图片。 

        :param seal_image: The seal_image of this SealList.
        :type seal_image: str
        """
        self._seal_image = seal_image

    @property
    def confidence(self):
        r"""Gets the confidence of this SealList.

        印章位置的置信度。 

        :return: The confidence of this SealList.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        r"""Sets the confidence of this SealList.

        印章位置的置信度。 

        :param confidence: The confidence of this SealList.
        :type confidence: float
        """
        self._confidence = confidence

    @property
    def location(self):
        r"""Gets the location of this SealList.

        印章位置，列表形式，包含印章区域四个顶点的二维坐标（x,y），坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :return: The location of this SealList.
        :rtype: list[list[int]]
        """
        return self._location

    @location.setter
    def location(self, location):
        r"""Sets the location of this SealList.

        印章位置，列表形式，包含印章区域四个顶点的二维坐标（x,y），坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :param location: The location of this SealList.
        :type location: list[list[int]]
        """
        self._location = location

    @property
    def words_block_list(self):
        r"""Gets the words_block_list of this SealList.

        印章文本块列表。 

        :return: The words_block_list of this SealList.
        :rtype: list[:class:`huaweicloudsdkocr.v1.SealWordsBlockList`]
        """
        return self._words_block_list

    @words_block_list.setter
    def words_block_list(self, words_block_list):
        r"""Sets the words_block_list of this SealList.

        印章文本块列表。 

        :param words_block_list: The words_block_list of this SealList.
        :type words_block_list: list[:class:`huaweicloudsdkocr.v1.SealWordsBlockList`]
        """
        self._words_block_list = words_block_list

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
        if not isinstance(other, SealList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
