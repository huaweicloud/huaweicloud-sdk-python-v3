# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TextTranslationReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'text': 'str',
        '_from': 'str',
        'to': 'str',
        'scene': 'str'
    }

    attribute_map = {
        'text': 'text',
        '_from': 'from',
        'to': 'to',
        'scene': 'scene'
    }

    def __init__(self, text=None, _from=None, to=None, scene=None):
        """TextTranslationReq

        The model defined in huaweicloud sdk

        :param text: 待翻译文本，仅支持utf-8编码，长度不超过5000字符。
        :type text: str
        :param _from: 翻译原语言，具体取值见支持的语言列表: zh    中文 en    英文 ru    俄语 ja    日文 de    德文 fr    法文 es    西班牙文 ko    韩语 auto  自动检测输入语种并翻译成目标语种，您需要指定目标语种。
        :type _from: str
        :param to: 翻译原语言，具体取值见支持的语言列表: zh    中文 en    英文 ru    俄语 ja    日文 de    德文 fr    法文 es    西班牙文 ko    韩语
        :type to: str
        :param scene: 默认为“common”，当前只有通用场景
        :type scene: str
        """
        
        

        self._text = None
        self.__from = None
        self._to = None
        self._scene = None
        self.discriminator = None

        self.text = text
        self._from = _from
        self.to = to
        if scene is not None:
            self.scene = scene

    @property
    def text(self):
        """Gets the text of this TextTranslationReq.

        待翻译文本，仅支持utf-8编码，长度不超过5000字符。

        :return: The text of this TextTranslationReq.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this TextTranslationReq.

        待翻译文本，仅支持utf-8编码，长度不超过5000字符。

        :param text: The text of this TextTranslationReq.
        :type text: str
        """
        self._text = text

    @property
    def _from(self):
        """Gets the _from of this TextTranslationReq.

        翻译原语言，具体取值见支持的语言列表: zh    中文 en    英文 ru    俄语 ja    日文 de    德文 fr    法文 es    西班牙文 ko    韩语 auto  自动检测输入语种并翻译成目标语种，您需要指定目标语种。

        :return: The _from of this TextTranslationReq.
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this TextTranslationReq.

        翻译原语言，具体取值见支持的语言列表: zh    中文 en    英文 ru    俄语 ja    日文 de    德文 fr    法文 es    西班牙文 ko    韩语 auto  自动检测输入语种并翻译成目标语种，您需要指定目标语种。

        :param _from: The _from of this TextTranslationReq.
        :type _from: str
        """
        self.__from = _from

    @property
    def to(self):
        """Gets the to of this TextTranslationReq.

        翻译原语言，具体取值见支持的语言列表: zh    中文 en    英文 ru    俄语 ja    日文 de    德文 fr    法文 es    西班牙文 ko    韩语

        :return: The to of this TextTranslationReq.
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this TextTranslationReq.

        翻译原语言，具体取值见支持的语言列表: zh    中文 en    英文 ru    俄语 ja    日文 de    德文 fr    法文 es    西班牙文 ko    韩语

        :param to: The to of this TextTranslationReq.
        :type to: str
        """
        self._to = to

    @property
    def scene(self):
        """Gets the scene of this TextTranslationReq.

        默认为“common”，当前只有通用场景

        :return: The scene of this TextTranslationReq.
        :rtype: str
        """
        return self._scene

    @scene.setter
    def scene(self, scene):
        """Sets the scene of this TextTranslationReq.

        默认为“common”，当前只有通用场景

        :param scene: The scene of this TextTranslationReq.
        :type scene: str
        """
        self._scene = scene

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
        if not isinstance(other, TextTranslationReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
