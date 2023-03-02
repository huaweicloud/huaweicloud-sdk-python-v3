# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VideoTranslateInferenceRewriteConfigBackground:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'box_color': 'list[int]',
        'background_font_color': 'list[int]'
    }

    attribute_map = {
        'box_color': 'box_color',
        'background_font_color': 'background_font_color'
    }

    def __init__(self, box_color=None, background_font_color=None):
        """VideoTranslateInferenceRewriteConfigBackground

        The model defined in huaweicloud sdk

        :param box_color: 文本背景框颜色
        :type box_color: list[int]
        :param background_font_color: 文本字体颜色
        :type background_font_color: list[int]
        """
        
        

        self._box_color = None
        self._background_font_color = None
        self.discriminator = None

        if box_color is not None:
            self.box_color = box_color
        if background_font_color is not None:
            self.background_font_color = background_font_color

    @property
    def box_color(self):
        """Gets the box_color of this VideoTranslateInferenceRewriteConfigBackground.

        文本背景框颜色

        :return: The box_color of this VideoTranslateInferenceRewriteConfigBackground.
        :rtype: list[int]
        """
        return self._box_color

    @box_color.setter
    def box_color(self, box_color):
        """Sets the box_color of this VideoTranslateInferenceRewriteConfigBackground.

        文本背景框颜色

        :param box_color: The box_color of this VideoTranslateInferenceRewriteConfigBackground.
        :type box_color: list[int]
        """
        self._box_color = box_color

    @property
    def background_font_color(self):
        """Gets the background_font_color of this VideoTranslateInferenceRewriteConfigBackground.

        文本字体颜色

        :return: The background_font_color of this VideoTranslateInferenceRewriteConfigBackground.
        :rtype: list[int]
        """
        return self._background_font_color

    @background_font_color.setter
    def background_font_color(self, background_font_color):
        """Sets the background_font_color of this VideoTranslateInferenceRewriteConfigBackground.

        文本字体颜色

        :param background_font_color: The background_font_color of this VideoTranslateInferenceRewriteConfigBackground.
        :type background_font_color: list[int]
        """
        self._background_font_color = background_font_color

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
        if not isinstance(other, VideoTranslateInferenceRewriteConfigBackground):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
