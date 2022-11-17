# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunModerationAudioResponseBodyResultDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'text': 'object',
        'audio': 'RunModerationAudioResponseBodyResultDetailAudio'
    }

    attribute_map = {
        'text': 'text',
        'audio': 'audio'
    }

    def __init__(self, text=None, audio=None):
        """RunModerationAudioResponseBodyResultDetail

        The model defined in huaweicloud sdk

        :param text: 返回的语音转文本后审核结果详细信息： ● politics：涉政敏感词列表。 ● porn：涉黄敏感词列表。 ● ad：广告敏感词列表。 ● abuse：辱骂敏感词列表。 ● contraband：违禁品敏感词列表 
        :type text: object
        :param audio: 
        :type audio: :class:`huaweicloudsdkmoderation.v2.RunModerationAudioResponseBodyResultDetailAudio`
        """
        
        

        self._text = None
        self._audio = None
        self.discriminator = None

        if text is not None:
            self.text = text
        if audio is not None:
            self.audio = audio

    @property
    def text(self):
        """Gets the text of this RunModerationAudioResponseBodyResultDetail.

        返回的语音转文本后审核结果详细信息： ● politics：涉政敏感词列表。 ● porn：涉黄敏感词列表。 ● ad：广告敏感词列表。 ● abuse：辱骂敏感词列表。 ● contraband：违禁品敏感词列表 

        :return: The text of this RunModerationAudioResponseBodyResultDetail.
        :rtype: object
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this RunModerationAudioResponseBodyResultDetail.

        返回的语音转文本后审核结果详细信息： ● politics：涉政敏感词列表。 ● porn：涉黄敏感词列表。 ● ad：广告敏感词列表。 ● abuse：辱骂敏感词列表。 ● contraband：违禁品敏感词列表 

        :param text: The text of this RunModerationAudioResponseBodyResultDetail.
        :type text: object
        """
        self._text = text

    @property
    def audio(self):
        """Gets the audio of this RunModerationAudioResponseBodyResultDetail.

        :return: The audio of this RunModerationAudioResponseBodyResultDetail.
        :rtype: :class:`huaweicloudsdkmoderation.v2.RunModerationAudioResponseBodyResultDetailAudio`
        """
        return self._audio

    @audio.setter
    def audio(self, audio):
        """Sets the audio of this RunModerationAudioResponseBodyResultDetail.

        :param audio: The audio of this RunModerationAudioResponseBodyResultDetail.
        :type audio: :class:`huaweicloudsdkmoderation.v2.RunModerationAudioResponseBodyResultDetailAudio`
        """
        self._audio = audio

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
        if not isinstance(other, RunModerationAudioResponseBodyResultDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
