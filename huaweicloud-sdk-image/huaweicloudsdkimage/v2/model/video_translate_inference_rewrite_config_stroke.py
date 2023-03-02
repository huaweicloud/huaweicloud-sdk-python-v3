# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VideoTranslateInferenceRewriteConfigStroke:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'stroke_color': 'list[int]',
        'font_color': 'list[int]',
        'stroke_ratio': 'float'
    }

    attribute_map = {
        'stroke_color': 'stroke_color',
        'font_color': 'font_color',
        'stroke_ratio': 'stroke_ratio'
    }

    def __init__(self, stroke_color=None, font_color=None, stroke_ratio=None):
        """VideoTranslateInferenceRewriteConfigStroke

        The model defined in huaweicloud sdk

        :param stroke_color: 文本描边颜色
        :type stroke_color: list[int]
        :param font_color: 文本字体颜色
        :type font_color: list[int]
        :param stroke_ratio: 描边宽度
        :type stroke_ratio: float
        """
        
        

        self._stroke_color = None
        self._font_color = None
        self._stroke_ratio = None
        self.discriminator = None

        if stroke_color is not None:
            self.stroke_color = stroke_color
        if font_color is not None:
            self.font_color = font_color
        if stroke_ratio is not None:
            self.stroke_ratio = stroke_ratio

    @property
    def stroke_color(self):
        """Gets the stroke_color of this VideoTranslateInferenceRewriteConfigStroke.

        文本描边颜色

        :return: The stroke_color of this VideoTranslateInferenceRewriteConfigStroke.
        :rtype: list[int]
        """
        return self._stroke_color

    @stroke_color.setter
    def stroke_color(self, stroke_color):
        """Sets the stroke_color of this VideoTranslateInferenceRewriteConfigStroke.

        文本描边颜色

        :param stroke_color: The stroke_color of this VideoTranslateInferenceRewriteConfigStroke.
        :type stroke_color: list[int]
        """
        self._stroke_color = stroke_color

    @property
    def font_color(self):
        """Gets the font_color of this VideoTranslateInferenceRewriteConfigStroke.

        文本字体颜色

        :return: The font_color of this VideoTranslateInferenceRewriteConfigStroke.
        :rtype: list[int]
        """
        return self._font_color

    @font_color.setter
    def font_color(self, font_color):
        """Sets the font_color of this VideoTranslateInferenceRewriteConfigStroke.

        文本字体颜色

        :param font_color: The font_color of this VideoTranslateInferenceRewriteConfigStroke.
        :type font_color: list[int]
        """
        self._font_color = font_color

    @property
    def stroke_ratio(self):
        """Gets the stroke_ratio of this VideoTranslateInferenceRewriteConfigStroke.

        描边宽度

        :return: The stroke_ratio of this VideoTranslateInferenceRewriteConfigStroke.
        :rtype: float
        """
        return self._stroke_ratio

    @stroke_ratio.setter
    def stroke_ratio(self, stroke_ratio):
        """Sets the stroke_ratio of this VideoTranslateInferenceRewriteConfigStroke.

        描边宽度

        :param stroke_ratio: The stroke_ratio of this VideoTranslateInferenceRewriteConfigStroke.
        :type stroke_ratio: float
        """
        self._stroke_ratio = stroke_ratio

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
        if not isinstance(other, VideoTranslateInferenceRewriteConfigStroke):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
