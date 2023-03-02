# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VideoTranslateInferenceRewriteConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'font_type': 'str',
        'rewrite_row_interval': 'float',
        'stroke': 'VideoTranslateInferenceRewriteConfigStroke',
        'background': 'VideoTranslateInferenceRewriteConfigBackground'
    }

    attribute_map = {
        'font_type': 'font_type',
        'rewrite_row_interval': 'rewrite_row_interval',
        'stroke': 'stroke',
        'background': 'background'
    }

    def __init__(self, font_type=None, rewrite_row_interval=None, stroke=None, background=None):
        """VideoTranslateInferenceRewriteConfig

        The model defined in huaweicloud sdk

        :param font_type: 字体类型
        :type font_type: str
        :param rewrite_row_interval: 字幕字体行间距
        :type rewrite_row_interval: float
        :param stroke: 
        :type stroke: :class:`huaweicloudsdkimage.v2.VideoTranslateInferenceRewriteConfigStroke`
        :param background: 
        :type background: :class:`huaweicloudsdkimage.v2.VideoTranslateInferenceRewriteConfigBackground`
        """
        
        

        self._font_type = None
        self._rewrite_row_interval = None
        self._stroke = None
        self._background = None
        self.discriminator = None

        if font_type is not None:
            self.font_type = font_type
        if rewrite_row_interval is not None:
            self.rewrite_row_interval = rewrite_row_interval
        if stroke is not None:
            self.stroke = stroke
        if background is not None:
            self.background = background

    @property
    def font_type(self):
        """Gets the font_type of this VideoTranslateInferenceRewriteConfig.

        字体类型

        :return: The font_type of this VideoTranslateInferenceRewriteConfig.
        :rtype: str
        """
        return self._font_type

    @font_type.setter
    def font_type(self, font_type):
        """Sets the font_type of this VideoTranslateInferenceRewriteConfig.

        字体类型

        :param font_type: The font_type of this VideoTranslateInferenceRewriteConfig.
        :type font_type: str
        """
        self._font_type = font_type

    @property
    def rewrite_row_interval(self):
        """Gets the rewrite_row_interval of this VideoTranslateInferenceRewriteConfig.

        字幕字体行间距

        :return: The rewrite_row_interval of this VideoTranslateInferenceRewriteConfig.
        :rtype: float
        """
        return self._rewrite_row_interval

    @rewrite_row_interval.setter
    def rewrite_row_interval(self, rewrite_row_interval):
        """Sets the rewrite_row_interval of this VideoTranslateInferenceRewriteConfig.

        字幕字体行间距

        :param rewrite_row_interval: The rewrite_row_interval of this VideoTranslateInferenceRewriteConfig.
        :type rewrite_row_interval: float
        """
        self._rewrite_row_interval = rewrite_row_interval

    @property
    def stroke(self):
        """Gets the stroke of this VideoTranslateInferenceRewriteConfig.

        :return: The stroke of this VideoTranslateInferenceRewriteConfig.
        :rtype: :class:`huaweicloudsdkimage.v2.VideoTranslateInferenceRewriteConfigStroke`
        """
        return self._stroke

    @stroke.setter
    def stroke(self, stroke):
        """Sets the stroke of this VideoTranslateInferenceRewriteConfig.

        :param stroke: The stroke of this VideoTranslateInferenceRewriteConfig.
        :type stroke: :class:`huaweicloudsdkimage.v2.VideoTranslateInferenceRewriteConfigStroke`
        """
        self._stroke = stroke

    @property
    def background(self):
        """Gets the background of this VideoTranslateInferenceRewriteConfig.

        :return: The background of this VideoTranslateInferenceRewriteConfig.
        :rtype: :class:`huaweicloudsdkimage.v2.VideoTranslateInferenceRewriteConfigBackground`
        """
        return self._background

    @background.setter
    def background(self, background):
        """Sets the background of this VideoTranslateInferenceRewriteConfig.

        :param background: The background of this VideoTranslateInferenceRewriteConfig.
        :type background: :class:`huaweicloudsdkimage.v2.VideoTranslateInferenceRewriteConfigBackground`
        """
        self._background = background

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
        if not isinstance(other, VideoTranslateInferenceRewriteConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
