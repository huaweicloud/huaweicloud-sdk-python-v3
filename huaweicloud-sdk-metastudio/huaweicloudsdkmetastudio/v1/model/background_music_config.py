# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackgroundMusicConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'music_asset_id': 'str',
        'volume': 'int'
    }

    attribute_map = {
        'music_asset_id': 'music_asset_id',
        'volume': 'volume'
    }

    def __init__(self, music_asset_id=None, volume=None):
        """BackgroundMusicConfig

        The model defined in huaweicloud sdk

        :param music_asset_id: 音乐资产ID。
        :type music_asset_id: str
        :param volume: 音乐音量。如100，表示音量100%，50表示音量50%。  默认值100，最小值0，最大值100。
        :type volume: int
        """
        
        

        self._music_asset_id = None
        self._volume = None
        self.discriminator = None

        if music_asset_id is not None:
            self.music_asset_id = music_asset_id
        if volume is not None:
            self.volume = volume

    @property
    def music_asset_id(self):
        """Gets the music_asset_id of this BackgroundMusicConfig.

        音乐资产ID。

        :return: The music_asset_id of this BackgroundMusicConfig.
        :rtype: str
        """
        return self._music_asset_id

    @music_asset_id.setter
    def music_asset_id(self, music_asset_id):
        """Sets the music_asset_id of this BackgroundMusicConfig.

        音乐资产ID。

        :param music_asset_id: The music_asset_id of this BackgroundMusicConfig.
        :type music_asset_id: str
        """
        self._music_asset_id = music_asset_id

    @property
    def volume(self):
        """Gets the volume of this BackgroundMusicConfig.

        音乐音量。如100，表示音量100%，50表示音量50%。  默认值100，最小值0，最大值100。

        :return: The volume of this BackgroundMusicConfig.
        :rtype: int
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this BackgroundMusicConfig.

        音乐音量。如100，表示音量100%，50表示音量50%。  默认值100，最小值0，最大值100。

        :param volume: The volume of this BackgroundMusicConfig.
        :type volume: int
        """
        self._volume = volume

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
        if not isinstance(other, BackgroundMusicConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
