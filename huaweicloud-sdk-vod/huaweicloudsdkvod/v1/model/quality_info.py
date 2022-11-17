# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QualityInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'video': 'VideoTemplateInfo',
        'audio': 'AudioTemplateInfo',
        'format': 'str'
    }

    attribute_map = {
        'video': 'video',
        'audio': 'audio',
        'format': 'format'
    }

    def __init__(self, video=None, audio=None, format=None):
        """QualityInfo

        The model defined in huaweicloud sdk

        :param video: 
        :type video: :class:`huaweicloudsdkvod.v1.VideoTemplateInfo`
        :param audio: 
        :type audio: :class:`huaweicloudsdkvod.v1.AudioTemplateInfo`
        :param format: 格式。
        :type format: str
        """
        
        

        self._video = None
        self._audio = None
        self._format = None
        self.discriminator = None

        if video is not None:
            self.video = video
        if audio is not None:
            self.audio = audio
        self.format = format

    @property
    def video(self):
        """Gets the video of this QualityInfo.

        :return: The video of this QualityInfo.
        :rtype: :class:`huaweicloudsdkvod.v1.VideoTemplateInfo`
        """
        return self._video

    @video.setter
    def video(self, video):
        """Sets the video of this QualityInfo.

        :param video: The video of this QualityInfo.
        :type video: :class:`huaweicloudsdkvod.v1.VideoTemplateInfo`
        """
        self._video = video

    @property
    def audio(self):
        """Gets the audio of this QualityInfo.

        :return: The audio of this QualityInfo.
        :rtype: :class:`huaweicloudsdkvod.v1.AudioTemplateInfo`
        """
        return self._audio

    @audio.setter
    def audio(self, audio):
        """Sets the audio of this QualityInfo.

        :param audio: The audio of this QualityInfo.
        :type audio: :class:`huaweicloudsdkvod.v1.AudioTemplateInfo`
        """
        self._audio = audio

    @property
    def format(self):
        """Gets the format of this QualityInfo.

        格式。

        :return: The format of this QualityInfo.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this QualityInfo.

        格式。

        :param format: The format of this QualityInfo.
        :type format: str
        """
        self._format = format

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
        if not isinstance(other, QualityInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
