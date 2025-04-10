# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TtsCallBackConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'callback_url': 'str'
    }

    attribute_map = {
        'callback_url': 'callback_url'
    }

    def __init__(self, callback_url=None):
        r"""TtsCallBackConfig

        The model defined in huaweicloud sdk

        :param callback_url: 回调URL。 回调请求body为json格式，带参数如下： status: FINISHED或ERROR或者WAITING job_id: 任务id audio_file_download_url: 音频文件路径 subtitle_file_download_url: 字幕文件路径 audio_duration: 音频时长（秒）
        :type callback_url: str
        """
        
        

        self._callback_url = None
        self.discriminator = None

        self.callback_url = callback_url

    @property
    def callback_url(self):
        r"""Gets the callback_url of this TtsCallBackConfig.

        回调URL。 回调请求body为json格式，带参数如下： status: FINISHED或ERROR或者WAITING job_id: 任务id audio_file_download_url: 音频文件路径 subtitle_file_download_url: 字幕文件路径 audio_duration: 音频时长（秒）

        :return: The callback_url of this TtsCallBackConfig.
        :rtype: str
        """
        return self._callback_url

    @callback_url.setter
    def callback_url(self, callback_url):
        r"""Sets the callback_url of this TtsCallBackConfig.

        回调URL。 回调请求body为json格式，带参数如下： status: FINISHED或ERROR或者WAITING job_id: 任务id audio_file_download_url: 音频文件路径 subtitle_file_download_url: 字幕文件路径 audio_duration: 音频时长（秒）

        :param callback_url: The callback_url of this TtsCallBackConfig.
        :type callback_url: str
        """
        self._callback_url = callback_url

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
        if not isinstance(other, TtsCallBackConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
