# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VideoCreateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data': 'VideoCreateRequestData',
        'event_type': 'str',
        'image_categories': 'list[str]',
        'audio_categories': 'list[str]',
        'param_callback': 'str'
    }

    attribute_map = {
        'data': 'data',
        'event_type': 'event_type',
        'image_categories': 'image_categories',
        'audio_categories': 'audio_categories',
        'param_callback': 'callback'
    }

    def __init__(self, data=None, event_type=None, image_categories=None, audio_categories=None, param_callback=None):
        """VideoCreateRequest

        The model defined in huaweicloud sdk

        :param data: 
        :type data: :class:`huaweicloudsdkmoderation.v3.VideoCreateRequestData`
        :param event_type: 事件类型，可选值如下： default：默认事件
        :type event_type: str
        :param image_categories: 视频中画面需要检测的风险类型，列表不能为空。 terrorism：涉政暴恐内容的检测 porn：鉴黄内容的检测 politics：政治敏感人物内容的检测 image_text：图文违规内容的检测（检测图片中出现的广告、色情、暴恐、涉政的文字违规内容以及二维码内容）
        :type image_categories: list[str]
        :param audio_categories: 视频中音频需要检测的风险类型，不传或为空时表示不审核音频维度。 politics: 涉政检测 porn：涉黄检测 ad: 广告检测 moan: 娇喘检测 abuse: 辱骂检测
        :type audio_categories: list[str]
        :param param_callback: 回调http接口：当该字段非空时，服务将根据该字段回调通知用户审核结果。
        :type param_callback: str
        """
        
        

        self._data = None
        self._event_type = None
        self._image_categories = None
        self._audio_categories = None
        self._param_callback = None
        self.discriminator = None

        self.data = data
        self.event_type = event_type
        self.image_categories = image_categories
        if audio_categories is not None:
            self.audio_categories = audio_categories
        if param_callback is not None:
            self.param_callback = param_callback

    @property
    def data(self):
        """Gets the data of this VideoCreateRequest.

        :return: The data of this VideoCreateRequest.
        :rtype: :class:`huaweicloudsdkmoderation.v3.VideoCreateRequestData`
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this VideoCreateRequest.

        :param data: The data of this VideoCreateRequest.
        :type data: :class:`huaweicloudsdkmoderation.v3.VideoCreateRequestData`
        """
        self._data = data

    @property
    def event_type(self):
        """Gets the event_type of this VideoCreateRequest.

        事件类型，可选值如下： default：默认事件

        :return: The event_type of this VideoCreateRequest.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this VideoCreateRequest.

        事件类型，可选值如下： default：默认事件

        :param event_type: The event_type of this VideoCreateRequest.
        :type event_type: str
        """
        self._event_type = event_type

    @property
    def image_categories(self):
        """Gets the image_categories of this VideoCreateRequest.

        视频中画面需要检测的风险类型，列表不能为空。 terrorism：涉政暴恐内容的检测 porn：鉴黄内容的检测 politics：政治敏感人物内容的检测 image_text：图文违规内容的检测（检测图片中出现的广告、色情、暴恐、涉政的文字违规内容以及二维码内容）

        :return: The image_categories of this VideoCreateRequest.
        :rtype: list[str]
        """
        return self._image_categories

    @image_categories.setter
    def image_categories(self, image_categories):
        """Sets the image_categories of this VideoCreateRequest.

        视频中画面需要检测的风险类型，列表不能为空。 terrorism：涉政暴恐内容的检测 porn：鉴黄内容的检测 politics：政治敏感人物内容的检测 image_text：图文违规内容的检测（检测图片中出现的广告、色情、暴恐、涉政的文字违规内容以及二维码内容）

        :param image_categories: The image_categories of this VideoCreateRequest.
        :type image_categories: list[str]
        """
        self._image_categories = image_categories

    @property
    def audio_categories(self):
        """Gets the audio_categories of this VideoCreateRequest.

        视频中音频需要检测的风险类型，不传或为空时表示不审核音频维度。 politics: 涉政检测 porn：涉黄检测 ad: 广告检测 moan: 娇喘检测 abuse: 辱骂检测

        :return: The audio_categories of this VideoCreateRequest.
        :rtype: list[str]
        """
        return self._audio_categories

    @audio_categories.setter
    def audio_categories(self, audio_categories):
        """Sets the audio_categories of this VideoCreateRequest.

        视频中音频需要检测的风险类型，不传或为空时表示不审核音频维度。 politics: 涉政检测 porn：涉黄检测 ad: 广告检测 moan: 娇喘检测 abuse: 辱骂检测

        :param audio_categories: The audio_categories of this VideoCreateRequest.
        :type audio_categories: list[str]
        """
        self._audio_categories = audio_categories

    @property
    def param_callback(self):
        """Gets the param_callback of this VideoCreateRequest.

        回调http接口：当该字段非空时，服务将根据该字段回调通知用户审核结果。

        :return: The param_callback of this VideoCreateRequest.
        :rtype: str
        """
        return self._param_callback

    @param_callback.setter
    def param_callback(self, param_callback):
        """Sets the param_callback of this VideoCreateRequest.

        回调http接口：当该字段非空时，服务将根据该字段回调通知用户审核结果。

        :param param_callback: The param_callback of this VideoCreateRequest.
        :type param_callback: str
        """
        self._param_callback = param_callback

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
        if not isinstance(other, VideoCreateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
