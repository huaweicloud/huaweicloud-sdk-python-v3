# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SmartDocumentRecognizerFormulaBlock:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'formula': 'str',
        'location': 'list[list[int]]'
    }

    attribute_map = {
        'formula': 'formula',
        'location': 'location'
    }

    def __init__(self, formula=None, location=None):
        r"""SmartDocumentRecognizerFormulaBlock

        The model defined in huaweicloud sdk

        :param formula: 数学公式识别结果，以latex字符串表示。
        :type formula: str
        :param location: 数学公式位置信息，列表形式，分别表示4个顶点的x, y坐标；坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 
        :type location: list[list[int]]
        """
        
        

        self._formula = None
        self._location = None
        self.discriminator = None

        if formula is not None:
            self.formula = formula
        if location is not None:
            self.location = location

    @property
    def formula(self):
        r"""Gets the formula of this SmartDocumentRecognizerFormulaBlock.

        数学公式识别结果，以latex字符串表示。

        :return: The formula of this SmartDocumentRecognizerFormulaBlock.
        :rtype: str
        """
        return self._formula

    @formula.setter
    def formula(self, formula):
        r"""Sets the formula of this SmartDocumentRecognizerFormulaBlock.

        数学公式识别结果，以latex字符串表示。

        :param formula: The formula of this SmartDocumentRecognizerFormulaBlock.
        :type formula: str
        """
        self._formula = formula

    @property
    def location(self):
        r"""Gets the location of this SmartDocumentRecognizerFormulaBlock.

        数学公式位置信息，列表形式，分别表示4个顶点的x, y坐标；坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :return: The location of this SmartDocumentRecognizerFormulaBlock.
        :rtype: list[list[int]]
        """
        return self._location

    @location.setter
    def location(self, location):
        r"""Sets the location of this SmartDocumentRecognizerFormulaBlock.

        数学公式位置信息，列表形式，分别表示4个顶点的x, y坐标；坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :param location: The location of this SmartDocumentRecognizerFormulaBlock.
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
        if not isinstance(other, SmartDocumentRecognizerFormulaBlock):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
