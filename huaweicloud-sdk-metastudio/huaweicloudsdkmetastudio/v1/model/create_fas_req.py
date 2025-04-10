# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateFASReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'audio_file_download_url': 'str',
        'frame_rate': 'int',
        'emotion': 'int'
    }

    attribute_map = {
        'audio_file_download_url': 'audio_file_download_url',
        'frame_rate': 'frame_rate',
        'emotion': 'emotion'
    }

    def __init__(self, audio_file_download_url=None, frame_rate=None, emotion=None):
        r"""CreateFASReq

        The model defined in huaweicloud sdk

        :param audio_file_download_url: 语音驱动音频文件下载URL，格式为AAC或者MP3
        :type audio_file_download_url: str
        :param frame_rate: 期望的输出帧率
        :type frame_rate: int
        :param emotion: 情绪： 0：平静（默认） 1：开心 2：哀伤 3：愤怒
        :type emotion: int
        """
        
        

        self._audio_file_download_url = None
        self._frame_rate = None
        self._emotion = None
        self.discriminator = None

        self.audio_file_download_url = audio_file_download_url
        self.frame_rate = frame_rate
        if emotion is not None:
            self.emotion = emotion

    @property
    def audio_file_download_url(self):
        r"""Gets the audio_file_download_url of this CreateFASReq.

        语音驱动音频文件下载URL，格式为AAC或者MP3

        :return: The audio_file_download_url of this CreateFASReq.
        :rtype: str
        """
        return self._audio_file_download_url

    @audio_file_download_url.setter
    def audio_file_download_url(self, audio_file_download_url):
        r"""Sets the audio_file_download_url of this CreateFASReq.

        语音驱动音频文件下载URL，格式为AAC或者MP3

        :param audio_file_download_url: The audio_file_download_url of this CreateFASReq.
        :type audio_file_download_url: str
        """
        self._audio_file_download_url = audio_file_download_url

    @property
    def frame_rate(self):
        r"""Gets the frame_rate of this CreateFASReq.

        期望的输出帧率

        :return: The frame_rate of this CreateFASReq.
        :rtype: int
        """
        return self._frame_rate

    @frame_rate.setter
    def frame_rate(self, frame_rate):
        r"""Sets the frame_rate of this CreateFASReq.

        期望的输出帧率

        :param frame_rate: The frame_rate of this CreateFASReq.
        :type frame_rate: int
        """
        self._frame_rate = frame_rate

    @property
    def emotion(self):
        r"""Gets the emotion of this CreateFASReq.

        情绪： 0：平静（默认） 1：开心 2：哀伤 3：愤怒

        :return: The emotion of this CreateFASReq.
        :rtype: int
        """
        return self._emotion

    @emotion.setter
    def emotion(self, emotion):
        r"""Sets the emotion of this CreateFASReq.

        情绪： 0：平静（默认） 1：开心 2：哀伤 3：愤怒

        :param emotion: The emotion of this CreateFASReq.
        :type emotion: int
        """
        self._emotion = emotion

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
        if not isinstance(other, CreateFASReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
