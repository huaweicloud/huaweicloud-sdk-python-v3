# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EncoderSettingsExpand:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'audio_descriptions': 'list[EncoderSettingsExpandAudioDescriptions]',
        'video_descriptions': 'VideoDescriptions'
    }

    attribute_map = {
        'audio_descriptions': 'audio_descriptions',
        'video_descriptions': 'video_descriptions'
    }

    def __init__(self, audio_descriptions=None, video_descriptions=None):
        r"""EncoderSettingsExpand

        The model defined in huaweicloud sdk

        :param audio_descriptions: 音频输出配置的描述信息
        :type audio_descriptions: list[:class:`huaweicloudsdklive.v1.EncoderSettingsExpandAudioDescriptions`]
        :param video_descriptions: 
        :type video_descriptions: :class:`huaweicloudsdklive.v1.VideoDescriptions`
        """
        
        

        self._audio_descriptions = None
        self._video_descriptions = None
        self.discriminator = None

        if audio_descriptions is not None:
            self.audio_descriptions = audio_descriptions
        if video_descriptions is not None:
            self.video_descriptions = video_descriptions

    @property
    def audio_descriptions(self):
        r"""Gets the audio_descriptions of this EncoderSettingsExpand.

        音频输出配置的描述信息

        :return: The audio_descriptions of this EncoderSettingsExpand.
        :rtype: list[:class:`huaweicloudsdklive.v1.EncoderSettingsExpandAudioDescriptions`]
        """
        return self._audio_descriptions

    @audio_descriptions.setter
    def audio_descriptions(self, audio_descriptions):
        r"""Sets the audio_descriptions of this EncoderSettingsExpand.

        音频输出配置的描述信息

        :param audio_descriptions: The audio_descriptions of this EncoderSettingsExpand.
        :type audio_descriptions: list[:class:`huaweicloudsdklive.v1.EncoderSettingsExpandAudioDescriptions`]
        """
        self._audio_descriptions = audio_descriptions

    @property
    def video_descriptions(self):
        r"""Gets the video_descriptions of this EncoderSettingsExpand.

        :return: The video_descriptions of this EncoderSettingsExpand.
        :rtype: :class:`huaweicloudsdklive.v1.VideoDescriptions`
        """
        return self._video_descriptions

    @video_descriptions.setter
    def video_descriptions(self, video_descriptions):
        r"""Sets the video_descriptions of this EncoderSettingsExpand.

        :param video_descriptions: The video_descriptions of this EncoderSettingsExpand.
        :type video_descriptions: :class:`huaweicloudsdklive.v1.VideoDescriptions`
        """
        self._video_descriptions = video_descriptions

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
        if not isinstance(other, EncoderSettingsExpand):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
