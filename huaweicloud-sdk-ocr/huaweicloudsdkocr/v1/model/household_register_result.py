# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HouseholdRegisterResult:

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
        'location': 'list[list[int]]',
        'content': 'HouseholdRegisterContent',
        'confidence': 'dict(str, float)'
    }

    attribute_map = {
        'type': 'type',
        'location': 'location',
        'content': 'content',
        'confidence': 'confidence'
    }

    def __init__(self, type=None, location=None, content=None, confidence=None):
        r"""HouseholdRegisterResult

        The model defined in huaweicloud sdk

        :param type: 类型。参数为“首页”或“登记页”。 
        :type type: str
        :param location: 户口本证件位置信息，列表形式，包含证件位置四个顶点的二维坐标（x,y）;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 
        :type location: list[list[int]]
        :param content: 
        :type content: :class:`huaweicloudsdkocr.v1.HouseholdRegisterContent`
        :param confidence: content中各个字段的置信度，取值范围0~1。置信度越大，本次识别的字段的可靠性越高，在统计意义上，置信度越大，准确率越高。置信度由算法给出，不直接等价于字段的准确率。 
        :type confidence: dict(str, float)
        """
        
        

        self._type = None
        self._location = None
        self._content = None
        self._confidence = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if location is not None:
            self.location = location
        if content is not None:
            self.content = content
        if confidence is not None:
            self.confidence = confidence

    @property
    def type(self):
        r"""Gets the type of this HouseholdRegisterResult.

        类型。参数为“首页”或“登记页”。 

        :return: The type of this HouseholdRegisterResult.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this HouseholdRegisterResult.

        类型。参数为“首页”或“登记页”。 

        :param type: The type of this HouseholdRegisterResult.
        :type type: str
        """
        self._type = type

    @property
    def location(self):
        r"""Gets the location of this HouseholdRegisterResult.

        户口本证件位置信息，列表形式，包含证件位置四个顶点的二维坐标（x,y）;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :return: The location of this HouseholdRegisterResult.
        :rtype: list[list[int]]
        """
        return self._location

    @location.setter
    def location(self, location):
        r"""Sets the location of this HouseholdRegisterResult.

        户口本证件位置信息，列表形式，包含证件位置四个顶点的二维坐标（x,y）;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :param location: The location of this HouseholdRegisterResult.
        :type location: list[list[int]]
        """
        self._location = location

    @property
    def content(self):
        r"""Gets the content of this HouseholdRegisterResult.

        :return: The content of this HouseholdRegisterResult.
        :rtype: :class:`huaweicloudsdkocr.v1.HouseholdRegisterContent`
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this HouseholdRegisterResult.

        :param content: The content of this HouseholdRegisterResult.
        :type content: :class:`huaweicloudsdkocr.v1.HouseholdRegisterContent`
        """
        self._content = content

    @property
    def confidence(self):
        r"""Gets the confidence of this HouseholdRegisterResult.

        content中各个字段的置信度，取值范围0~1。置信度越大，本次识别的字段的可靠性越高，在统计意义上，置信度越大，准确率越高。置信度由算法给出，不直接等价于字段的准确率。 

        :return: The confidence of this HouseholdRegisterResult.
        :rtype: dict(str, float)
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        r"""Sets the confidence of this HouseholdRegisterResult.

        content中各个字段的置信度，取值范围0~1。置信度越大，本次识别的字段的可靠性越高，在统计意义上，置信度越大，准确率越高。置信度由算法给出，不直接等价于字段的准确率。 

        :param confidence: The confidence of this HouseholdRegisterResult.
        :type confidence: dict(str, float)
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
        if not isinstance(other, HouseholdRegisterResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
