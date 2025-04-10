# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SmartVideoLayerConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'video_url': 'str',
        'video_cover_url': 'str',
        'display_duration': 'int'
    }

    attribute_map = {
        'video_url': 'video_url',
        'video_cover_url': 'video_cover_url',
        'display_duration': 'display_duration'
    }

    def __init__(self, video_url=None, video_cover_url=None, display_duration=None):
        r"""SmartVideoLayerConfig

        The model defined in huaweicloud sdk

        :param video_url: 视频文件的URL。
        :type video_url: str
        :param video_cover_url: 视频封面文件的URL。
        :type video_cover_url: str
        :param display_duration: **参数解释**： 图片显示时长，单位s。  显示时长规则为，若携带reply_texts、reply_audios，则与播放语音内容时长保持一致。若未携带，则与匹配的关键词语音内容时长保持一致。
        :type display_duration: int
        """
        
        

        self._video_url = None
        self._video_cover_url = None
        self._display_duration = None
        self.discriminator = None

        self.video_url = video_url
        if video_cover_url is not None:
            self.video_cover_url = video_cover_url
        if display_duration is not None:
            self.display_duration = display_duration

    @property
    def video_url(self):
        r"""Gets the video_url of this SmartVideoLayerConfig.

        视频文件的URL。

        :return: The video_url of this SmartVideoLayerConfig.
        :rtype: str
        """
        return self._video_url

    @video_url.setter
    def video_url(self, video_url):
        r"""Sets the video_url of this SmartVideoLayerConfig.

        视频文件的URL。

        :param video_url: The video_url of this SmartVideoLayerConfig.
        :type video_url: str
        """
        self._video_url = video_url

    @property
    def video_cover_url(self):
        r"""Gets the video_cover_url of this SmartVideoLayerConfig.

        视频封面文件的URL。

        :return: The video_cover_url of this SmartVideoLayerConfig.
        :rtype: str
        """
        return self._video_cover_url

    @video_cover_url.setter
    def video_cover_url(self, video_cover_url):
        r"""Sets the video_cover_url of this SmartVideoLayerConfig.

        视频封面文件的URL。

        :param video_cover_url: The video_cover_url of this SmartVideoLayerConfig.
        :type video_cover_url: str
        """
        self._video_cover_url = video_cover_url

    @property
    def display_duration(self):
        r"""Gets the display_duration of this SmartVideoLayerConfig.

        **参数解释**： 图片显示时长，单位s。  显示时长规则为，若携带reply_texts、reply_audios，则与播放语音内容时长保持一致。若未携带，则与匹配的关键词语音内容时长保持一致。

        :return: The display_duration of this SmartVideoLayerConfig.
        :rtype: int
        """
        return self._display_duration

    @display_duration.setter
    def display_duration(self, display_duration):
        r"""Sets the display_duration of this SmartVideoLayerConfig.

        **参数解释**： 图片显示时长，单位s。  显示时长规则为，若携带reply_texts、reply_audios，则与播放语音内容时长保持一致。若未携带，则与匹配的关键词语音内容时长保持一致。

        :param display_duration: The display_duration of this SmartVideoLayerConfig.
        :type display_duration: int
        """
        self._display_duration = display_duration

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
        if not isinstance(other, SmartVideoLayerConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
