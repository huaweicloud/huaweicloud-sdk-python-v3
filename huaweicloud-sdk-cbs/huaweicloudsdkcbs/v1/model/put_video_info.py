# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PutVideoInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tts_config': 'TtsConfig',
        'video_config': 'VideoConfig',
        'character_config': 'CharacterConfig',
        'read_config': 'ReadConfig'
    }

    attribute_map = {
        'tts_config': 'tts_config',
        'video_config': 'video_config',
        'character_config': 'character_config',
        'read_config': 'read_config'
    }

    def __init__(self, tts_config=None, video_config=None, character_config=None, read_config=None):
        """PutVideoInfo

        The model defined in huaweicloud sdk

        :param tts_config: 
        :type tts_config: :class:`huaweicloudsdkcbs.v1.TtsConfig`
        :param video_config: 
        :type video_config: :class:`huaweicloudsdkcbs.v1.VideoConfig`
        :param character_config: 
        :type character_config: :class:`huaweicloudsdkcbs.v1.CharacterConfig`
        :param read_config: 
        :type read_config: :class:`huaweicloudsdkcbs.v1.ReadConfig`
        """
        
        

        self._tts_config = None
        self._video_config = None
        self._character_config = None
        self._read_config = None
        self.discriminator = None

        self.tts_config = tts_config
        self.video_config = video_config
        self.character_config = character_config
        self.read_config = read_config

    @property
    def tts_config(self):
        """Gets the tts_config of this PutVideoInfo.

        :return: The tts_config of this PutVideoInfo.
        :rtype: :class:`huaweicloudsdkcbs.v1.TtsConfig`
        """
        return self._tts_config

    @tts_config.setter
    def tts_config(self, tts_config):
        """Sets the tts_config of this PutVideoInfo.

        :param tts_config: The tts_config of this PutVideoInfo.
        :type tts_config: :class:`huaweicloudsdkcbs.v1.TtsConfig`
        """
        self._tts_config = tts_config

    @property
    def video_config(self):
        """Gets the video_config of this PutVideoInfo.

        :return: The video_config of this PutVideoInfo.
        :rtype: :class:`huaweicloudsdkcbs.v1.VideoConfig`
        """
        return self._video_config

    @video_config.setter
    def video_config(self, video_config):
        """Sets the video_config of this PutVideoInfo.

        :param video_config: The video_config of this PutVideoInfo.
        :type video_config: :class:`huaweicloudsdkcbs.v1.VideoConfig`
        """
        self._video_config = video_config

    @property
    def character_config(self):
        """Gets the character_config of this PutVideoInfo.

        :return: The character_config of this PutVideoInfo.
        :rtype: :class:`huaweicloudsdkcbs.v1.CharacterConfig`
        """
        return self._character_config

    @character_config.setter
    def character_config(self, character_config):
        """Sets the character_config of this PutVideoInfo.

        :param character_config: The character_config of this PutVideoInfo.
        :type character_config: :class:`huaweicloudsdkcbs.v1.CharacterConfig`
        """
        self._character_config = character_config

    @property
    def read_config(self):
        """Gets the read_config of this PutVideoInfo.

        :return: The read_config of this PutVideoInfo.
        :rtype: :class:`huaweicloudsdkcbs.v1.ReadConfig`
        """
        return self._read_config

    @read_config.setter
    def read_config(self, read_config):
        """Sets the read_config of this PutVideoInfo.

        :param read_config: The read_config of this PutVideoInfo.
        :type read_config: :class:`huaweicloudsdkcbs.v1.ReadConfig`
        """
        self._read_config = read_config

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
        if not isinstance(other, PutVideoInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
