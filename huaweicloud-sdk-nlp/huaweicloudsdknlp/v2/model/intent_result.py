# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IntentResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'confidence': 'float',
        'label': 'str',
        'slots': 'list[Slot]',
        'text': 'str'
    }

    attribute_map = {
        'confidence': 'confidence',
        'label': 'label',
        'slots': 'slots',
        'text': 'text'
    }

    def __init__(self, confidence=None, label=None, slots=None, text=None):
        r"""IntentResult

        The model defined in huaweicloud sdk

        :param confidence: 标签label的置信度。
        :type confidence: float
        :param label: 文本的意图标签。标签共有以下9类，取值如下： weather：天气 time：报时 news：新闻 joke：笑话 translation：翻译 notification：提醒 alarm：闹钟 music：音乐 other：其它
        :type label: str
        :param slots: slot数据结构
        :type slots: list[:class:`huaweicloudsdknlp.v2.Slot`]
        :param text: 返回待分析文本。
        :type text: str
        """
        
        

        self._confidence = None
        self._label = None
        self._slots = None
        self._text = None
        self.discriminator = None

        self.confidence = confidence
        self.label = label
        self.slots = slots
        self.text = text

    @property
    def confidence(self):
        r"""Gets the confidence of this IntentResult.

        标签label的置信度。

        :return: The confidence of this IntentResult.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        r"""Sets the confidence of this IntentResult.

        标签label的置信度。

        :param confidence: The confidence of this IntentResult.
        :type confidence: float
        """
        self._confidence = confidence

    @property
    def label(self):
        r"""Gets the label of this IntentResult.

        文本的意图标签。标签共有以下9类，取值如下： weather：天气 time：报时 news：新闻 joke：笑话 translation：翻译 notification：提醒 alarm：闹钟 music：音乐 other：其它

        :return: The label of this IntentResult.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        r"""Sets the label of this IntentResult.

        文本的意图标签。标签共有以下9类，取值如下： weather：天气 time：报时 news：新闻 joke：笑话 translation：翻译 notification：提醒 alarm：闹钟 music：音乐 other：其它

        :param label: The label of this IntentResult.
        :type label: str
        """
        self._label = label

    @property
    def slots(self):
        r"""Gets the slots of this IntentResult.

        slot数据结构

        :return: The slots of this IntentResult.
        :rtype: list[:class:`huaweicloudsdknlp.v2.Slot`]
        """
        return self._slots

    @slots.setter
    def slots(self, slots):
        r"""Sets the slots of this IntentResult.

        slot数据结构

        :param slots: The slots of this IntentResult.
        :type slots: list[:class:`huaweicloudsdknlp.v2.Slot`]
        """
        self._slots = slots

    @property
    def text(self):
        r"""Gets the text of this IntentResult.

        返回待分析文本。

        :return: The text of this IntentResult.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        r"""Sets the text of this IntentResult.

        返回待分析文本。

        :param text: The text of this IntentResult.
        :type text: str
        """
        self._text = text

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
        if not isinstance(other, IntentResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
