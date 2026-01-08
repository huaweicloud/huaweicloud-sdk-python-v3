# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AvParameters:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'video': 'VideoParameters',
        'audio': 'Audio',
        'common': 'Common',
        'output': 'ObsObjInfo',
        'output_filename': 'str'
    }

    attribute_map = {
        'video': 'video',
        'audio': 'audio',
        'common': 'common',
        'output': 'output',
        'output_filename': 'output_filename'
    }

    def __init__(self, video=None, audio=None, common=None, output=None, output_filename=None):
        r"""AvParameters

        The model defined in huaweicloud sdk

        :param video: 
        :type video: :class:`huaweicloudsdkmpc.v1.VideoParameters`
        :param audio: 
        :type audio: :class:`huaweicloudsdkmpc.v1.Audio`
        :param common: 
        :type common: :class:`huaweicloudsdkmpc.v1.Common`
        :param output: 
        :type output: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        :param output_filename: 输出文件名 
        :type output_filename: str
        """
        
        

        self._video = None
        self._audio = None
        self._common = None
        self._output = None
        self._output_filename = None
        self.discriminator = None

        if video is not None:
            self.video = video
        if audio is not None:
            self.audio = audio
        self.common = common
        if output is not None:
            self.output = output
        if output_filename is not None:
            self.output_filename = output_filename

    @property
    def video(self):
        r"""Gets the video of this AvParameters.

        :return: The video of this AvParameters.
        :rtype: :class:`huaweicloudsdkmpc.v1.VideoParameters`
        """
        return self._video

    @video.setter
    def video(self, video):
        r"""Sets the video of this AvParameters.

        :param video: The video of this AvParameters.
        :type video: :class:`huaweicloudsdkmpc.v1.VideoParameters`
        """
        self._video = video

    @property
    def audio(self):
        r"""Gets the audio of this AvParameters.

        :return: The audio of this AvParameters.
        :rtype: :class:`huaweicloudsdkmpc.v1.Audio`
        """
        return self._audio

    @audio.setter
    def audio(self, audio):
        r"""Sets the audio of this AvParameters.

        :param audio: The audio of this AvParameters.
        :type audio: :class:`huaweicloudsdkmpc.v1.Audio`
        """
        self._audio = audio

    @property
    def common(self):
        r"""Gets the common of this AvParameters.

        :return: The common of this AvParameters.
        :rtype: :class:`huaweicloudsdkmpc.v1.Common`
        """
        return self._common

    @common.setter
    def common(self, common):
        r"""Sets the common of this AvParameters.

        :param common: The common of this AvParameters.
        :type common: :class:`huaweicloudsdkmpc.v1.Common`
        """
        self._common = common

    @property
    def output(self):
        r"""Gets the output of this AvParameters.

        :return: The output of this AvParameters.
        :rtype: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        return self._output

    @output.setter
    def output(self, output):
        r"""Sets the output of this AvParameters.

        :param output: The output of this AvParameters.
        :type output: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        self._output = output

    @property
    def output_filename(self):
        r"""Gets the output_filename of this AvParameters.

        输出文件名 

        :return: The output_filename of this AvParameters.
        :rtype: str
        """
        return self._output_filename

    @output_filename.setter
    def output_filename(self, output_filename):
        r"""Sets the output_filename of this AvParameters.

        输出文件名 

        :param output_filename: The output_filename of this AvParameters.
        :type output_filename: str
        """
        self._output_filename = output_filename

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AvParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
