# coding: utf-8

import re
import six



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
        'common': 'Common'
    }

    attribute_map = {
        'video': 'video',
        'audio': 'audio',
        'common': 'common'
    }

    def __init__(self, video=None, audio=None, common=None):
        """AvParameters

        The model defined in huaweicloud sdk

        :param video: 
        :type video: :class:`huaweicloudsdkmpc.v1.VideoParameters`
        :param audio: 
        :type audio: :class:`huaweicloudsdkmpc.v1.Audio`
        :param common: 
        :type common: :class:`huaweicloudsdkmpc.v1.Common`
        """
        
        

        self._video = None
        self._audio = None
        self._common = None
        self.discriminator = None

        if video is not None:
            self.video = video
        if audio is not None:
            self.audio = audio
        self.common = common

    @property
    def video(self):
        """Gets the video of this AvParameters.


        :return: The video of this AvParameters.
        :rtype: :class:`huaweicloudsdkmpc.v1.VideoParameters`
        """
        return self._video

    @video.setter
    def video(self, video):
        """Sets the video of this AvParameters.


        :param video: The video of this AvParameters.
        :type video: :class:`huaweicloudsdkmpc.v1.VideoParameters`
        """
        self._video = video

    @property
    def audio(self):
        """Gets the audio of this AvParameters.


        :return: The audio of this AvParameters.
        :rtype: :class:`huaweicloudsdkmpc.v1.Audio`
        """
        return self._audio

    @audio.setter
    def audio(self, audio):
        """Sets the audio of this AvParameters.


        :param audio: The audio of this AvParameters.
        :type audio: :class:`huaweicloudsdkmpc.v1.Audio`
        """
        self._audio = audio

    @property
    def common(self):
        """Gets the common of this AvParameters.


        :return: The common of this AvParameters.
        :rtype: :class:`huaweicloudsdkmpc.v1.Common`
        """
        return self._common

    @common.setter
    def common(self, common):
        """Sets the common of this AvParameters.


        :param common: The common of this AvParameters.
        :type common: :class:`huaweicloudsdkmpc.v1.Common`
        """
        self._common = common

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
        if not isinstance(other, AvParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
