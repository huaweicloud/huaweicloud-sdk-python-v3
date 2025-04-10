# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShootScriptAudioFiles:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'audio_file_url': 'list[ShootScriptAudioFileItem]'
    }

    attribute_map = {
        'audio_file_url': 'audio_file_url'
    }

    def __init__(self, audio_file_url=None):
        r"""ShootScriptAudioFiles

        The model defined in huaweicloud sdk

        :param audio_file_url: 用于语音驱动的音频文件上传URL。
        :type audio_file_url: list[:class:`huaweicloudsdkmetastudio.v1.ShootScriptAudioFileItem`]
        """
        
        

        self._audio_file_url = None
        self.discriminator = None

        if audio_file_url is not None:
            self.audio_file_url = audio_file_url

    @property
    def audio_file_url(self):
        r"""Gets the audio_file_url of this ShootScriptAudioFiles.

        用于语音驱动的音频文件上传URL。

        :return: The audio_file_url of this ShootScriptAudioFiles.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.ShootScriptAudioFileItem`]
        """
        return self._audio_file_url

    @audio_file_url.setter
    def audio_file_url(self, audio_file_url):
        r"""Sets the audio_file_url of this ShootScriptAudioFiles.

        用于语音驱动的音频文件上传URL。

        :param audio_file_url: The audio_file_url of this ShootScriptAudioFiles.
        :type audio_file_url: list[:class:`huaweicloudsdkmetastudio.v1.ShootScriptAudioFileItem`]
        """
        self._audio_file_url = audio_file_url

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
        if not isinstance(other, ShootScriptAudioFiles):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
