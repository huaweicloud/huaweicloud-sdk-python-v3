# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SmartImageLayerConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_url': 'str',
        'display_duration': 'int'
    }

    attribute_map = {
        'image_url': 'image_url',
        'display_duration': 'display_duration'
    }

    def __init__(self, image_url=None, display_duration=None):
        r"""SmartImageLayerConfig

        The model defined in huaweicloud sdk

        :param image_url: 图片文件的URL。
        :type image_url: str
        :param display_duration: **参数解释**： 图片显示时长，单位s。  显示时长规则为，若携带reply_texts、reply_audios，则与播放语音内容时长保持一致。若未携带，则与匹配的关键词语音内容时长保持一致。
        :type display_duration: int
        """
        
        

        self._image_url = None
        self._display_duration = None
        self.discriminator = None

        self.image_url = image_url
        if display_duration is not None:
            self.display_duration = display_duration

    @property
    def image_url(self):
        r"""Gets the image_url of this SmartImageLayerConfig.

        图片文件的URL。

        :return: The image_url of this SmartImageLayerConfig.
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        r"""Sets the image_url of this SmartImageLayerConfig.

        图片文件的URL。

        :param image_url: The image_url of this SmartImageLayerConfig.
        :type image_url: str
        """
        self._image_url = image_url

    @property
    def display_duration(self):
        r"""Gets the display_duration of this SmartImageLayerConfig.

        **参数解释**： 图片显示时长，单位s。  显示时长规则为，若携带reply_texts、reply_audios，则与播放语音内容时长保持一致。若未携带，则与匹配的关键词语音内容时长保持一致。

        :return: The display_duration of this SmartImageLayerConfig.
        :rtype: int
        """
        return self._display_duration

    @display_duration.setter
    def display_duration(self, display_duration):
        r"""Sets the display_duration of this SmartImageLayerConfig.

        **参数解释**： 图片显示时长，单位s。  显示时长规则为，若携带reply_texts、reply_audios，则与播放语音内容时长保持一致。若未携带，则与匹配的关键词语音内容时长保持一致。

        :param display_duration: The display_duration of this SmartImageLayerConfig.
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
        if not isinstance(other, SmartImageLayerConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
