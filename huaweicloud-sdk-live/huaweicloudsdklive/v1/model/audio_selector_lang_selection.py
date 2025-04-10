# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AudioSelectorLangSelection:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'language_code': 'str',
        'language_selection_policy': 'str'
    }

    attribute_map = {
        'language_code': 'language_code',
        'language_selection_policy': 'language_selection_policy'
    }

    def __init__(self, language_code=None, language_selection_policy=None):
        r"""AudioSelectorLangSelection

        The model defined in huaweicloud sdk

        :param language_code: 语言简称，输入2或3个小写字母的语言代码。
        :type language_code: str
        :param language_selection_policy: 语言输出策略。  取值如下： - LOOSE：宽松匹配，示例“eng”会优先匹配源流中语言为English的音轨，如果匹配不到，则选择PID最小的音轨。 - STRICT：严格匹配，示例“eng”会严格匹配源流中语言为English的音轨，如果匹配不到，媒体直播服务会自动补齐一个静音分片，当终端使用此音频选择器播放视频时，会静音播放。
        :type language_selection_policy: str
        """
        
        

        self._language_code = None
        self._language_selection_policy = None
        self.discriminator = None

        self.language_code = language_code
        if language_selection_policy is not None:
            self.language_selection_policy = language_selection_policy

    @property
    def language_code(self):
        r"""Gets the language_code of this AudioSelectorLangSelection.

        语言简称，输入2或3个小写字母的语言代码。

        :return: The language_code of this AudioSelectorLangSelection.
        :rtype: str
        """
        return self._language_code

    @language_code.setter
    def language_code(self, language_code):
        r"""Sets the language_code of this AudioSelectorLangSelection.

        语言简称，输入2或3个小写字母的语言代码。

        :param language_code: The language_code of this AudioSelectorLangSelection.
        :type language_code: str
        """
        self._language_code = language_code

    @property
    def language_selection_policy(self):
        r"""Gets the language_selection_policy of this AudioSelectorLangSelection.

        语言输出策略。  取值如下： - LOOSE：宽松匹配，示例“eng”会优先匹配源流中语言为English的音轨，如果匹配不到，则选择PID最小的音轨。 - STRICT：严格匹配，示例“eng”会严格匹配源流中语言为English的音轨，如果匹配不到，媒体直播服务会自动补齐一个静音分片，当终端使用此音频选择器播放视频时，会静音播放。

        :return: The language_selection_policy of this AudioSelectorLangSelection.
        :rtype: str
        """
        return self._language_selection_policy

    @language_selection_policy.setter
    def language_selection_policy(self, language_selection_policy):
        r"""Sets the language_selection_policy of this AudioSelectorLangSelection.

        语言输出策略。  取值如下： - LOOSE：宽松匹配，示例“eng”会优先匹配源流中语言为English的音轨，如果匹配不到，则选择PID最小的音轨。 - STRICT：严格匹配，示例“eng”会严格匹配源流中语言为English的音轨，如果匹配不到，媒体直播服务会自动补齐一个静音分片，当终端使用此音频选择器播放视频时，会静音播放。

        :param language_selection_policy: The language_selection_policy of this AudioSelectorLangSelection.
        :type language_selection_policy: str
        """
        self._language_selection_policy = language_selection_policy

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
        if not isinstance(other, AudioSelectorLangSelection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
