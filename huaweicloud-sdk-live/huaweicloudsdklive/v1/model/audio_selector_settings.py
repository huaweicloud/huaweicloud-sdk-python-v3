# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AudioSelectorSettings:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'audio_language_selection': 'AudioSelectorLangSelection',
        'audio_pid_selection': 'AudioSelectorPidSelection',
        'audio_hls_selection': 'AudioSelectorHlsSelection'
    }

    attribute_map = {
        'audio_language_selection': 'audio_language_selection',
        'audio_pid_selection': 'audio_pid_selection',
        'audio_hls_selection': 'audio_hls_selection'
    }

    def __init__(self, audio_language_selection=None, audio_pid_selection=None, audio_hls_selection=None):
        r"""AudioSelectorSettings

        The model defined in huaweicloud sdk

        :param audio_language_selection: 
        :type audio_language_selection: :class:`huaweicloudsdklive.v1.AudioSelectorLangSelection`
        :param audio_pid_selection: 
        :type audio_pid_selection: :class:`huaweicloudsdklive.v1.AudioSelectorPidSelection`
        :param audio_hls_selection: 
        :type audio_hls_selection: :class:`huaweicloudsdklive.v1.AudioSelectorHlsSelection`
        """
        
        

        self._audio_language_selection = None
        self._audio_pid_selection = None
        self._audio_hls_selection = None
        self.discriminator = None

        if audio_language_selection is not None:
            self.audio_language_selection = audio_language_selection
        if audio_pid_selection is not None:
            self.audio_pid_selection = audio_pid_selection
        if audio_hls_selection is not None:
            self.audio_hls_selection = audio_hls_selection

    @property
    def audio_language_selection(self):
        r"""Gets the audio_language_selection of this AudioSelectorSettings.

        :return: The audio_language_selection of this AudioSelectorSettings.
        :rtype: :class:`huaweicloudsdklive.v1.AudioSelectorLangSelection`
        """
        return self._audio_language_selection

    @audio_language_selection.setter
    def audio_language_selection(self, audio_language_selection):
        r"""Sets the audio_language_selection of this AudioSelectorSettings.

        :param audio_language_selection: The audio_language_selection of this AudioSelectorSettings.
        :type audio_language_selection: :class:`huaweicloudsdklive.v1.AudioSelectorLangSelection`
        """
        self._audio_language_selection = audio_language_selection

    @property
    def audio_pid_selection(self):
        r"""Gets the audio_pid_selection of this AudioSelectorSettings.

        :return: The audio_pid_selection of this AudioSelectorSettings.
        :rtype: :class:`huaweicloudsdklive.v1.AudioSelectorPidSelection`
        """
        return self._audio_pid_selection

    @audio_pid_selection.setter
    def audio_pid_selection(self, audio_pid_selection):
        r"""Sets the audio_pid_selection of this AudioSelectorSettings.

        :param audio_pid_selection: The audio_pid_selection of this AudioSelectorSettings.
        :type audio_pid_selection: :class:`huaweicloudsdklive.v1.AudioSelectorPidSelection`
        """
        self._audio_pid_selection = audio_pid_selection

    @property
    def audio_hls_selection(self):
        r"""Gets the audio_hls_selection of this AudioSelectorSettings.

        :return: The audio_hls_selection of this AudioSelectorSettings.
        :rtype: :class:`huaweicloudsdklive.v1.AudioSelectorHlsSelection`
        """
        return self._audio_hls_selection

    @audio_hls_selection.setter
    def audio_hls_selection(self, audio_hls_selection):
        r"""Sets the audio_hls_selection of this AudioSelectorSettings.

        :param audio_hls_selection: The audio_hls_selection of this AudioSelectorSettings.
        :type audio_hls_selection: :class:`huaweicloudsdklive.v1.AudioSelectorHlsSelection`
        """
        self._audio_hls_selection = audio_hls_selection

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
        if not isinstance(other, AudioSelectorSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
