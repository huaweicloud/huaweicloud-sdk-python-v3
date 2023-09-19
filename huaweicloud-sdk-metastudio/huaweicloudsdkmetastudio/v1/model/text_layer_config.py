# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TextLayerConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'text_context': 'str',
        'font_name': 'str',
        'font_size': 'int',
        'font_color': 'str'
    }

    attribute_map = {
        'text_context': 'text_context',
        'font_name': 'font_name',
        'font_size': 'font_size',
        'font_color': 'font_color'
    }

    def __init__(self, text_context=None, font_name=None, font_size=None, font_color=None):
        """TextLayerConfig

        The model defined in huaweicloud sdk

        :param text_context: 文字水印内容，内容需做Base64编码，若类型为文字水印 (type字段为Text)，则此配置项不能为空  示例：若想添加文字水印“测试文字水印”，那么Content的值为：5rWL6K+V5paH5a2X5rC05Y2w
        :type text_context: str
        :param font_name: 字体，当前支持fzyouh
        :type font_name: str
        :param font_size: 字体大小。  取值范围：[4, 120]
        :type font_size: int
        :param font_color: 字体颜色。 目前颜色支持 black，blue，white，green，red，yellow，brown，gold，pink，orange，purple。
        :type font_color: str
        """
        
        

        self._text_context = None
        self._font_name = None
        self._font_size = None
        self._font_color = None
        self.discriminator = None

        if text_context is not None:
            self.text_context = text_context
        if font_name is not None:
            self.font_name = font_name
        if font_size is not None:
            self.font_size = font_size
        if font_color is not None:
            self.font_color = font_color

    @property
    def text_context(self):
        """Gets the text_context of this TextLayerConfig.

        文字水印内容，内容需做Base64编码，若类型为文字水印 (type字段为Text)，则此配置项不能为空  示例：若想添加文字水印“测试文字水印”，那么Content的值为：5rWL6K+V5paH5a2X5rC05Y2w

        :return: The text_context of this TextLayerConfig.
        :rtype: str
        """
        return self._text_context

    @text_context.setter
    def text_context(self, text_context):
        """Sets the text_context of this TextLayerConfig.

        文字水印内容，内容需做Base64编码，若类型为文字水印 (type字段为Text)，则此配置项不能为空  示例：若想添加文字水印“测试文字水印”，那么Content的值为：5rWL6K+V5paH5a2X5rC05Y2w

        :param text_context: The text_context of this TextLayerConfig.
        :type text_context: str
        """
        self._text_context = text_context

    @property
    def font_name(self):
        """Gets the font_name of this TextLayerConfig.

        字体，当前支持fzyouh

        :return: The font_name of this TextLayerConfig.
        :rtype: str
        """
        return self._font_name

    @font_name.setter
    def font_name(self, font_name):
        """Sets the font_name of this TextLayerConfig.

        字体，当前支持fzyouh

        :param font_name: The font_name of this TextLayerConfig.
        :type font_name: str
        """
        self._font_name = font_name

    @property
    def font_size(self):
        """Gets the font_size of this TextLayerConfig.

        字体大小。  取值范围：[4, 120]

        :return: The font_size of this TextLayerConfig.
        :rtype: int
        """
        return self._font_size

    @font_size.setter
    def font_size(self, font_size):
        """Sets the font_size of this TextLayerConfig.

        字体大小。  取值范围：[4, 120]

        :param font_size: The font_size of this TextLayerConfig.
        :type font_size: int
        """
        self._font_size = font_size

    @property
    def font_color(self):
        """Gets the font_color of this TextLayerConfig.

        字体颜色。 目前颜色支持 black，blue，white，green，red，yellow，brown，gold，pink，orange，purple。

        :return: The font_color of this TextLayerConfig.
        :rtype: str
        """
        return self._font_color

    @font_color.setter
    def font_color(self, font_color):
        """Sets the font_color of this TextLayerConfig.

        字体颜色。 目前颜色支持 black，blue，white，green，red，yellow，brown，gold，pink，orange，purple。

        :param font_color: The font_color of this TextLayerConfig.
        :type font_color: str
        """
        self._font_color = font_color

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
        if not isinstance(other, TextLayerConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
