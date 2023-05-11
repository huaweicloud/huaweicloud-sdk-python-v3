# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AudioModerationResultResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'suggestion': 'str',
        'details': 'list[AudioModerationResultDetail]',
        'audio_text': 'str'
    }

    attribute_map = {
        'suggestion': 'suggestion',
        'details': 'details',
        'audio_text': 'audio_text'
    }

    def __init__(self, suggestion=None, details=None, audio_text=None):
        """AudioModerationResultResult

        The model defined in huaweicloud sdk

        :param suggestion: 音频审核结果是否通过。 block：包含敏感信息，不通过 pass：不包含敏感信息，通过 review：需要人工复检
        :type suggestion: str
        :param details: 审核详情
        :type details: list[:class:`huaweicloudsdkmoderation.v3.AudioModerationResultDetail`]
        :param audio_text: 音频文本内容
        :type audio_text: str
        """
        
        

        self._suggestion = None
        self._details = None
        self._audio_text = None
        self.discriminator = None

        if suggestion is not None:
            self.suggestion = suggestion
        if details is not None:
            self.details = details
        if audio_text is not None:
            self.audio_text = audio_text

    @property
    def suggestion(self):
        """Gets the suggestion of this AudioModerationResultResult.

        音频审核结果是否通过。 block：包含敏感信息，不通过 pass：不包含敏感信息，通过 review：需要人工复检

        :return: The suggestion of this AudioModerationResultResult.
        :rtype: str
        """
        return self._suggestion

    @suggestion.setter
    def suggestion(self, suggestion):
        """Sets the suggestion of this AudioModerationResultResult.

        音频审核结果是否通过。 block：包含敏感信息，不通过 pass：不包含敏感信息，通过 review：需要人工复检

        :param suggestion: The suggestion of this AudioModerationResultResult.
        :type suggestion: str
        """
        self._suggestion = suggestion

    @property
    def details(self):
        """Gets the details of this AudioModerationResultResult.

        审核详情

        :return: The details of this AudioModerationResultResult.
        :rtype: list[:class:`huaweicloudsdkmoderation.v3.AudioModerationResultDetail`]
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this AudioModerationResultResult.

        审核详情

        :param details: The details of this AudioModerationResultResult.
        :type details: list[:class:`huaweicloudsdkmoderation.v3.AudioModerationResultDetail`]
        """
        self._details = details

    @property
    def audio_text(self):
        """Gets the audio_text of this AudioModerationResultResult.

        音频文本内容

        :return: The audio_text of this AudioModerationResultResult.
        :rtype: str
        """
        return self._audio_text

    @audio_text.setter
    def audio_text(self, audio_text):
        """Sets the audio_text of this AudioModerationResultResult.

        音频文本内容

        :param audio_text: The audio_text of this AudioModerationResultResult.
        :type audio_text: str
        """
        self._audio_text = audio_text

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
        if not isinstance(other, AudioModerationResultResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
