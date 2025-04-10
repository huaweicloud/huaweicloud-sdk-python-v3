# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OutputSetting:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'format': 'str',
        'video': 'EditVideoInfo',
        'audio': 'EditAudioInfo',
        'hls': 'EditHlsInfo',
        'output': 'ObsObjInfo'
    }

    attribute_map = {
        'format': 'format',
        'video': 'video',
        'audio': 'audio',
        'hls': 'hls',
        'output': 'output'
    }

    def __init__(self, format=None, video=None, audio=None, hls=None, output=None):
        r"""OutputSetting

        The model defined in huaweicloud sdk

        :param format: 剪切或拼接的输出封装格式。
        :type format: str
        :param video: 
        :type video: :class:`huaweicloudsdkmpc.v1.EditVideoInfo`
        :param audio: 
        :type audio: :class:`huaweicloudsdkmpc.v1.EditAudioInfo`
        :param hls: 
        :type hls: :class:`huaweicloudsdkmpc.v1.EditHlsInfo`
        :param output: 
        :type output: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        
        

        self._format = None
        self._video = None
        self._audio = None
        self._hls = None
        self._output = None
        self.discriminator = None

        if format is not None:
            self.format = format
        if video is not None:
            self.video = video
        if audio is not None:
            self.audio = audio
        if hls is not None:
            self.hls = hls
        if output is not None:
            self.output = output

    @property
    def format(self):
        r"""Gets the format of this OutputSetting.

        剪切或拼接的输出封装格式。

        :return: The format of this OutputSetting.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        r"""Sets the format of this OutputSetting.

        剪切或拼接的输出封装格式。

        :param format: The format of this OutputSetting.
        :type format: str
        """
        self._format = format

    @property
    def video(self):
        r"""Gets the video of this OutputSetting.

        :return: The video of this OutputSetting.
        :rtype: :class:`huaweicloudsdkmpc.v1.EditVideoInfo`
        """
        return self._video

    @video.setter
    def video(self, video):
        r"""Sets the video of this OutputSetting.

        :param video: The video of this OutputSetting.
        :type video: :class:`huaweicloudsdkmpc.v1.EditVideoInfo`
        """
        self._video = video

    @property
    def audio(self):
        r"""Gets the audio of this OutputSetting.

        :return: The audio of this OutputSetting.
        :rtype: :class:`huaweicloudsdkmpc.v1.EditAudioInfo`
        """
        return self._audio

    @audio.setter
    def audio(self, audio):
        r"""Sets the audio of this OutputSetting.

        :param audio: The audio of this OutputSetting.
        :type audio: :class:`huaweicloudsdkmpc.v1.EditAudioInfo`
        """
        self._audio = audio

    @property
    def hls(self):
        r"""Gets the hls of this OutputSetting.

        :return: The hls of this OutputSetting.
        :rtype: :class:`huaweicloudsdkmpc.v1.EditHlsInfo`
        """
        return self._hls

    @hls.setter
    def hls(self, hls):
        r"""Sets the hls of this OutputSetting.

        :param hls: The hls of this OutputSetting.
        :type hls: :class:`huaweicloudsdkmpc.v1.EditHlsInfo`
        """
        self._hls = hls

    @property
    def output(self):
        r"""Gets the output of this OutputSetting.

        :return: The output of this OutputSetting.
        :rtype: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        return self._output

    @output.setter
    def output(self, output):
        r"""Sets the output of this OutputSetting.

        :param output: The output of this OutputSetting.
        :type output: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        self._output = output

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
        if not isinstance(other, OutputSetting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
