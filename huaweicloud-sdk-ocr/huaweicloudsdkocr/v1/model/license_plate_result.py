# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LicensePlateResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'plate_number': 'str',
        'plate_color': 'str',
        'plate_location': 'list[list[int]]',
        'confidence': 'float'
    }

    attribute_map = {
        'plate_number': 'plate_number',
        'plate_color': 'plate_color',
        'plate_location': 'plate_location',
        'confidence': 'confidence'
    }

    def __init__(self, plate_number=None, plate_color=None, plate_location=None, confidence=None):
        """LicensePlateResult

        The model defined in huaweicloud sdk

        :param plate_number: 车牌内容。 
        :type plate_number: str
        :param plate_color: 当前版本支持的车牌底色类型：  - blue: 蓝色  - green: 绿色（小型新能源车牌）  - black: 黑色  - white: 白色  - yellow: 黄色  - yellow_green: 黄绿（大型新能源车牌） 
        :type plate_color: str
        :param plate_location: 车牌的区域位置信息，列表形式，包含文字区域四个顶点的二维坐标（x,y）;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 
        :type plate_location: list[list[int]]
        :param confidence: 相关字段的置信度信息，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。 置信度由算法给出，不直接等价于对应字段的准确率。 
        :type confidence: float
        """
        
        

        self._plate_number = None
        self._plate_color = None
        self._plate_location = None
        self._confidence = None
        self.discriminator = None

        self.plate_number = plate_number
        self.plate_color = plate_color
        self.plate_location = plate_location
        self.confidence = confidence

    @property
    def plate_number(self):
        """Gets the plate_number of this LicensePlateResult.

        车牌内容。 

        :return: The plate_number of this LicensePlateResult.
        :rtype: str
        """
        return self._plate_number

    @plate_number.setter
    def plate_number(self, plate_number):
        """Sets the plate_number of this LicensePlateResult.

        车牌内容。 

        :param plate_number: The plate_number of this LicensePlateResult.
        :type plate_number: str
        """
        self._plate_number = plate_number

    @property
    def plate_color(self):
        """Gets the plate_color of this LicensePlateResult.

        当前版本支持的车牌底色类型：  - blue: 蓝色  - green: 绿色（小型新能源车牌）  - black: 黑色  - white: 白色  - yellow: 黄色  - yellow_green: 黄绿（大型新能源车牌） 

        :return: The plate_color of this LicensePlateResult.
        :rtype: str
        """
        return self._plate_color

    @plate_color.setter
    def plate_color(self, plate_color):
        """Sets the plate_color of this LicensePlateResult.

        当前版本支持的车牌底色类型：  - blue: 蓝色  - green: 绿色（小型新能源车牌）  - black: 黑色  - white: 白色  - yellow: 黄色  - yellow_green: 黄绿（大型新能源车牌） 

        :param plate_color: The plate_color of this LicensePlateResult.
        :type plate_color: str
        """
        self._plate_color = plate_color

    @property
    def plate_location(self):
        """Gets the plate_location of this LicensePlateResult.

        车牌的区域位置信息，列表形式，包含文字区域四个顶点的二维坐标（x,y）;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :return: The plate_location of this LicensePlateResult.
        :rtype: list[list[int]]
        """
        return self._plate_location

    @plate_location.setter
    def plate_location(self, plate_location):
        """Sets the plate_location of this LicensePlateResult.

        车牌的区域位置信息，列表形式，包含文字区域四个顶点的二维坐标（x,y）;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :param plate_location: The plate_location of this LicensePlateResult.
        :type plate_location: list[list[int]]
        """
        self._plate_location = plate_location

    @property
    def confidence(self):
        """Gets the confidence of this LicensePlateResult.

        相关字段的置信度信息，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。 置信度由算法给出，不直接等价于对应字段的准确率。 

        :return: The confidence of this LicensePlateResult.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this LicensePlateResult.

        相关字段的置信度信息，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。 置信度由算法给出，不直接等价于对应字段的准确率。 

        :param confidence: The confidence of this LicensePlateResult.
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
        if not isinstance(other, LicensePlateResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
