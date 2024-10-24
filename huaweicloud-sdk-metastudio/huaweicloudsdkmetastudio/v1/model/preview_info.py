# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PreviewInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'text_sha256': 'str',
        'audio_file_download_url': 'str'
    }

    attribute_map = {
        'text_sha256': 'text_sha256',
        'audio_file_download_url': 'audio_file_download_url'
    }

    def __init__(self, text_sha256=None, audio_file_download_url=None):
        """PreviewInfo

        The model defined in huaweicloud sdk

        :param text_sha256: 文本内容hash值
        :type text_sha256: str
        :param audio_file_download_url: 文本对应音频文件下载链接
        :type audio_file_download_url: str
        """
        
        

        self._text_sha256 = None
        self._audio_file_download_url = None
        self.discriminator = None

        if text_sha256 is not None:
            self.text_sha256 = text_sha256
        if audio_file_download_url is not None:
            self.audio_file_download_url = audio_file_download_url

    @property
    def text_sha256(self):
        """Gets the text_sha256 of this PreviewInfo.

        文本内容hash值

        :return: The text_sha256 of this PreviewInfo.
        :rtype: str
        """
        return self._text_sha256

    @text_sha256.setter
    def text_sha256(self, text_sha256):
        """Sets the text_sha256 of this PreviewInfo.

        文本内容hash值

        :param text_sha256: The text_sha256 of this PreviewInfo.
        :type text_sha256: str
        """
        self._text_sha256 = text_sha256

    @property
    def audio_file_download_url(self):
        """Gets the audio_file_download_url of this PreviewInfo.

        文本对应音频文件下载链接

        :return: The audio_file_download_url of this PreviewInfo.
        :rtype: str
        """
        return self._audio_file_download_url

    @audio_file_download_url.setter
    def audio_file_download_url(self, audio_file_download_url):
        """Sets the audio_file_download_url of this PreviewInfo.

        文本对应音频文件下载链接

        :param audio_file_download_url: The audio_file_download_url of this PreviewInfo.
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
        if not isinstance(other, PreviewInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
