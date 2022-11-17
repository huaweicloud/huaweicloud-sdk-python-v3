# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MultiModalConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'video_format': 'str',
        'language': 'str',
        'mode': 'str'
    }

    attribute_map = {
        'video_format': 'video_format',
        'language': 'language',
        'mode': 'mode'
    }

    def __init__(self, video_format=None, language=None, mode=None):
        """MultiModalConfig

        The model defined in huaweicloud sdk

        :param video_format: 视频的封装格式。不填写此字段，则默认为auto。注意不论何种格式，均要求帧率在25fps以上，清晰度在240*240以上。   auto  自动判断，系统会自动判断视频封装格式。  avi  avi封装格式。  mp4  mp4封装格式。  webm  webm封装格式。  mkv  mkv封装格式。  flv  flv封装格式。 
        :type video_format: str
        :param language: 评测语言和口音。  en_gb 英语-英式口音。
        :type language: str
        :param mode: 评测模式。  word 单词模式。  sentence 句子模式。
        :type mode: str
        """
        
        

        self._video_format = None
        self._language = None
        self._mode = None
        self.discriminator = None

        if video_format is not None:
            self.video_format = video_format
        self.language = language
        self.mode = mode

    @property
    def video_format(self):
        """Gets the video_format of this MultiModalConfig.

        视频的封装格式。不填写此字段，则默认为auto。注意不论何种格式，均要求帧率在25fps以上，清晰度在240*240以上。   auto  自动判断，系统会自动判断视频封装格式。  avi  avi封装格式。  mp4  mp4封装格式。  webm  webm封装格式。  mkv  mkv封装格式。  flv  flv封装格式。 

        :return: The video_format of this MultiModalConfig.
        :rtype: str
        """
        return self._video_format

    @video_format.setter
    def video_format(self, video_format):
        """Sets the video_format of this MultiModalConfig.

        视频的封装格式。不填写此字段，则默认为auto。注意不论何种格式，均要求帧率在25fps以上，清晰度在240*240以上。   auto  自动判断，系统会自动判断视频封装格式。  avi  avi封装格式。  mp4  mp4封装格式。  webm  webm封装格式。  mkv  mkv封装格式。  flv  flv封装格式。 

        :param video_format: The video_format of this MultiModalConfig.
        :type video_format: str
        """
        self._video_format = video_format

    @property
    def language(self):
        """Gets the language of this MultiModalConfig.

        评测语言和口音。  en_gb 英语-英式口音。

        :return: The language of this MultiModalConfig.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this MultiModalConfig.

        评测语言和口音。  en_gb 英语-英式口音。

        :param language: The language of this MultiModalConfig.
        :type language: str
        """
        self._language = language

    @property
    def mode(self):
        """Gets the mode of this MultiModalConfig.

        评测模式。  word 单词模式。  sentence 句子模式。

        :return: The mode of this MultiModalConfig.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this MultiModalConfig.

        评测模式。  word 单词模式。  sentence 句子模式。

        :param mode: The mode of this MultiModalConfig.
        :type mode: str
        """
        self._mode = mode

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
        if not isinstance(other, MultiModalConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
