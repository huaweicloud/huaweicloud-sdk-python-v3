# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShootScriptAudioFileItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sequence_no': 'int',
        'audio_file_upload_url': 'str',
        'audio_file_download_url': 'str'
    }

    attribute_map = {
        'sequence_no': 'sequence_no',
        'audio_file_upload_url': 'audio_file_upload_url',
        'audio_file_download_url': 'audio_file_download_url'
    }

    def __init__(self, sequence_no=None, audio_file_upload_url=None, audio_file_download_url=None):
        """ShootScriptAudioFileItem

        The model defined in huaweicloud sdk

        :param sequence_no: 剧本序号。
        :type sequence_no: int
        :param audio_file_upload_url: 语音驱动音频文件上传URL。创建和更新脚本时返回。单个文件最大100M。支持上传MP3/WAV/M4A文件。
        :type audio_file_upload_url: str
        :param audio_file_download_url: 语音驱动音频文件下载URL。查询脚本详情时返回。
        :type audio_file_download_url: str
        """
        
        

        self._sequence_no = None
        self._audio_file_upload_url = None
        self._audio_file_download_url = None
        self.discriminator = None

        self.sequence_no = sequence_no
        if audio_file_upload_url is not None:
            self.audio_file_upload_url = audio_file_upload_url
        if audio_file_download_url is not None:
            self.audio_file_download_url = audio_file_download_url

    @property
    def sequence_no(self):
        """Gets the sequence_no of this ShootScriptAudioFileItem.

        剧本序号。

        :return: The sequence_no of this ShootScriptAudioFileItem.
        :rtype: int
        """
        return self._sequence_no

    @sequence_no.setter
    def sequence_no(self, sequence_no):
        """Sets the sequence_no of this ShootScriptAudioFileItem.

        剧本序号。

        :param sequence_no: The sequence_no of this ShootScriptAudioFileItem.
        :type sequence_no: int
        """
        self._sequence_no = sequence_no

    @property
    def audio_file_upload_url(self):
        """Gets the audio_file_upload_url of this ShootScriptAudioFileItem.

        语音驱动音频文件上传URL。创建和更新脚本时返回。单个文件最大100M。支持上传MP3/WAV/M4A文件。

        :return: The audio_file_upload_url of this ShootScriptAudioFileItem.
        :rtype: str
        """
        return self._audio_file_upload_url

    @audio_file_upload_url.setter
    def audio_file_upload_url(self, audio_file_upload_url):
        """Sets the audio_file_upload_url of this ShootScriptAudioFileItem.

        语音驱动音频文件上传URL。创建和更新脚本时返回。单个文件最大100M。支持上传MP3/WAV/M4A文件。

        :param audio_file_upload_url: The audio_file_upload_url of this ShootScriptAudioFileItem.
        :type audio_file_upload_url: str
        """
        self._audio_file_upload_url = audio_file_upload_url

    @property
    def audio_file_download_url(self):
        """Gets the audio_file_download_url of this ShootScriptAudioFileItem.

        语音驱动音频文件下载URL。查询脚本详情时返回。

        :return: The audio_file_download_url of this ShootScriptAudioFileItem.
        :rtype: str
        """
        return self._audio_file_download_url

    @audio_file_download_url.setter
    def audio_file_download_url(self, audio_file_download_url):
        """Sets the audio_file_download_url of this ShootScriptAudioFileItem.

        语音驱动音频文件下载URL。查询脚本详情时返回。

        :param audio_file_download_url: The audio_file_download_url of this ShootScriptAudioFileItem.
        :type audio_file_download_url: str
        """
        self._audio_file_download_url = audio_file_download_url

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
        if not isinstance(other, ShootScriptAudioFileItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
