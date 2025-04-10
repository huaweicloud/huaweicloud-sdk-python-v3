# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SmartTextLayerConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'text_type': 'str',
        'text_context': 'str',
        'font_name': 'str',
        'font_size': 'int',
        'font_color': 'str',
        'display_duration': 'int'
    }

    attribute_map = {
        'text_type': 'text_type',
        'text_context': 'text_context',
        'font_name': 'font_name',
        'font_size': 'font_size',
        'font_color': 'font_color',
        'display_duration': 'display_duration'
    }

    def __init__(self, text_type=None, text_context=None, font_name=None, font_size=None, font_color=None, display_duration=None):
        r"""SmartTextLayerConfig

        The model defined in huaweicloud sdk

        :param text_type: **参数解释**： 文本类型。 * DYNAMIC：动态文本，需要进行关键字替换。 * STATIC：静态文本。
        :type text_type: str
        :param text_context: 文本。
        :type text_context: str
        :param font_name: **参数解释**： 字体。当前支持的字体： * HarmonyOS_Sans_SC_Black：鸿蒙粗体 * HarmonyOS_Sans_SC_Regular：鸿蒙常规 * HarmonyOS_Sans_SC_Thin：鸿蒙细体 * fzyouh：方正瘦体
        :type font_name: str
        :param font_size: **参数解释**： 字体大小（像素）。  业务取值范围：[4, 120]，请以业务取值范围为准。
        :type font_size: int
        :param font_color: **参数解释**： 字体颜色。RGB颜色值。
        :type font_color: str
        :param display_duration: **参数解释**： 文本显示时长，单位s。 显示时长规则为，若携带reply_texts、reply_audios，则与播放语音内容时长保持一致；若未携带，则与匹配的关键词语音内容时长保持一致。
        :type display_duration: int
        """
        
        

        self._text_type = None
        self._text_context = None
        self._font_name = None
        self._font_size = None
        self._font_color = None
        self._display_duration = None
        self.discriminator = None

        if text_type is not None:
            self.text_type = text_type
        if text_context is not None:
            self.text_context = text_context
        if font_name is not None:
            self.font_name = font_name
        if font_size is not None:
            self.font_size = font_size
        if font_color is not None:
            self.font_color = font_color
        if display_duration is not None:
            self.display_duration = display_duration

    @property
    def text_type(self):
        r"""Gets the text_type of this SmartTextLayerConfig.

        **参数解释**： 文本类型。 * DYNAMIC：动态文本，需要进行关键字替换。 * STATIC：静态文本。

        :return: The text_type of this SmartTextLayerConfig.
        :rtype: str
        """
        return self._text_type

    @text_type.setter
    def text_type(self, text_type):
        r"""Sets the text_type of this SmartTextLayerConfig.

        **参数解释**： 文本类型。 * DYNAMIC：动态文本，需要进行关键字替换。 * STATIC：静态文本。

        :param text_type: The text_type of this SmartTextLayerConfig.
        :type text_type: str
        """
        self._text_type = text_type

    @property
    def text_context(self):
        r"""Gets the text_context of this SmartTextLayerConfig.

        文本。

        :return: The text_context of this SmartTextLayerConfig.
        :rtype: str
        """
        return self._text_context

    @text_context.setter
    def text_context(self, text_context):
        r"""Sets the text_context of this SmartTextLayerConfig.

        文本。

        :param text_context: The text_context of this SmartTextLayerConfig.
        :type text_context: str
        """
        self._text_context = text_context

    @property
    def font_name(self):
        r"""Gets the font_name of this SmartTextLayerConfig.

        **参数解释**： 字体。当前支持的字体： * HarmonyOS_Sans_SC_Black：鸿蒙粗体 * HarmonyOS_Sans_SC_Regular：鸿蒙常规 * HarmonyOS_Sans_SC_Thin：鸿蒙细体 * fzyouh：方正瘦体

        :return: The font_name of this SmartTextLayerConfig.
        :rtype: str
        """
        return self._font_name

    @font_name.setter
    def font_name(self, font_name):
        r"""Sets the font_name of this SmartTextLayerConfig.

        **参数解释**： 字体。当前支持的字体： * HarmonyOS_Sans_SC_Black：鸿蒙粗体 * HarmonyOS_Sans_SC_Regular：鸿蒙常规 * HarmonyOS_Sans_SC_Thin：鸿蒙细体 * fzyouh：方正瘦体

        :param font_name: The font_name of this SmartTextLayerConfig.
        :type font_name: str
        """
        self._font_name = font_name

    @property
    def font_size(self):
        r"""Gets the font_size of this SmartTextLayerConfig.

        **参数解释**： 字体大小（像素）。  业务取值范围：[4, 120]，请以业务取值范围为准。

        :return: The font_size of this SmartTextLayerConfig.
        :rtype: int
        """
        return self._font_size

    @font_size.setter
    def font_size(self, font_size):
        r"""Sets the font_size of this SmartTextLayerConfig.

        **参数解释**： 字体大小（像素）。  业务取值范围：[4, 120]，请以业务取值范围为准。

        :param font_size: The font_size of this SmartTextLayerConfig.
        :type font_size: int
        """
        self._font_size = font_size

    @property
    def font_color(self):
        r"""Gets the font_color of this SmartTextLayerConfig.

        **参数解释**： 字体颜色。RGB颜色值。

        :return: The font_color of this SmartTextLayerConfig.
        :rtype: str
        """
        return self._font_color

    @font_color.setter
    def font_color(self, font_color):
        r"""Sets the font_color of this SmartTextLayerConfig.

        **参数解释**： 字体颜色。RGB颜色值。

        :param font_color: The font_color of this SmartTextLayerConfig.
        :type font_color: str
        """
        self._font_color = font_color

    @property
    def display_duration(self):
        r"""Gets the display_duration of this SmartTextLayerConfig.

        **参数解释**： 文本显示时长，单位s。 显示时长规则为，若携带reply_texts、reply_audios，则与播放语音内容时长保持一致；若未携带，则与匹配的关键词语音内容时长保持一致。

        :return: The display_duration of this SmartTextLayerConfig.
        :rtype: int
        """
        return self._display_duration

    @display_duration.setter
    def display_duration(self, display_duration):
        r"""Sets the display_duration of this SmartTextLayerConfig.

        **参数解释**： 文本显示时长，单位s。 显示时长规则为，若携带reply_texts、reply_audios，则与播放语音内容时长保持一致；若未携带，则与匹配的关键词语音内容时长保持一致。

        :param display_duration: The display_duration of this SmartTextLayerConfig.
        :type display_duration: int
        """
        self._display_duration = display_duration

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
        if not isinstance(other, SmartTextLayerConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
