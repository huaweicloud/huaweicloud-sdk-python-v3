# coding: utf-8

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
        'biz_type': 'str',
        'event_type': 'str',
        'image_categories': 'list[str]',
        'audio_categories': 'list[str]',
        'param_callback': 'str',
        'seed': 'str'
    }

    attribute_map = {
        'data': 'data',
        'biz_type': 'biz_type',
        'event_type': 'event_type',
        'image_categories': 'image_categories',
        'audio_categories': 'audio_categories',
        'param_callback': 'callback',
        'seed': 'seed'
    }

    def __init__(self, data=None, biz_type=None, event_type=None, image_categories=None, audio_categories=None, param_callback=None, seed=None):
        r"""VideoCreateRequest

        The model defined in huaweicloud sdk

        :param data: 
        :type data: :class:`huaweicloudsdkmoderation.v3.VideoCreateRequestData`
        :param biz_type: 用户在控制台界面创建的biz_type名称，如果请求参数中传了biz_type则优先使用biz_type；如果用户没传biz_type则event_type和image_categories必须传。
        :type biz_type: str
        :param event_type: 事件类型，可选值如下： default：默认事件
        :type event_type: str
        :param image_categories: 视频中画面需要检测的风险类型，列表不能为空。 terrorism：涉政暴恐内容的检测 porn：鉴黄内容的检测 politics：政治敏感人物内容的检测 image_text：图文违规内容的检测（检测图片中出现的广告、色情、暴恐、涉政的文字违规内容以及二维码内容）
        :type image_categories: list[str]
        :param audio_categories: 视频中音频需要检测的风险类型，不传或为空时表示不审核音频维度。 politics: 涉政检测 porn：涉黄检测 ad: 广告检测 moan: 娇喘检测 abuse: 辱骂检测
        :type audio_categories: list[str]
        :param param_callback: 回调http接口：当该字段非空时，服务将根据该字段回调通知用户审核结果。
        :type param_callback: str
        :param seed: 用于回调通知时校验请求由华为云内容安全服务发起，由您自定义。随机字符串，由英文字母、数字、下划线组成，不超过64个字符。 说明：当seed非空时，headers中将包含X-Auth-Signature字段，字段的值使用HmacSHA256算法生成，待加密字符串由create_time、job_id、request_id、seed按照顺序拼接而成，密钥为seed。
        :type seed: str
        """
        
        

        self._data = None
        self._biz_type = None
        self._event_type = None
        self._image_categories = None
        self._audio_categories = None
        self._param_callback = None
        self._seed = None
        self.discriminator = None

        self.data = data
        if biz_type is not None:
            self.biz_type = biz_type
        if event_type is not None:
            self.event_type = event_type
        if image_categories is not None:
            self.image_categories = image_categories
        if audio_categories is not None:
            self.audio_categories = audio_categories
        if param_callback is not None:
            self.param_callback = param_callback
        if seed is not None:
            self.seed = seed

    @property
    def data(self):
        r"""Gets the data of this VideoCreateRequest.

        :return: The data of this VideoCreateRequest.
        :rtype: :class:`huaweicloudsdkmoderation.v3.VideoCreateRequestData`
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this VideoCreateRequest.

        :param data: The data of this VideoCreateRequest.
        :type data: :class:`huaweicloudsdkmoderation.v3.VideoCreateRequestData`
        """
        self._data = data

    @property
    def biz_type(self):
        r"""Gets the biz_type of this VideoCreateRequest.

        用户在控制台界面创建的biz_type名称，如果请求参数中传了biz_type则优先使用biz_type；如果用户没传biz_type则event_type和image_categories必须传。

        :return: The biz_type of this VideoCreateRequest.
        :rtype: str
        """
        return self._biz_type

    @biz_type.setter
    def biz_type(self, biz_type):
        r"""Sets the biz_type of this VideoCreateRequest.

        用户在控制台界面创建的biz_type名称，如果请求参数中传了biz_type则优先使用biz_type；如果用户没传biz_type则event_type和image_categories必须传。

        :param biz_type: The biz_type of this VideoCreateRequest.
        :type biz_type: str
        """
        self._biz_type = biz_type

    @property
    def event_type(self):
        r"""Gets the event_type of this VideoCreateRequest.

        事件类型，可选值如下： default：默认事件

        :return: The event_type of this VideoCreateRequest.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        r"""Sets the event_type of this VideoCreateRequest.

        事件类型，可选值如下： default：默认事件

        :param event_type: The event_type of this VideoCreateRequest.
        :type event_type: str
        """
        self._event_type = event_type

    @property
    def image_categories(self):
        r"""Gets the image_categories of this VideoCreateRequest.

        视频中画面需要检测的风险类型，列表不能为空。 terrorism：涉政暴恐内容的检测 porn：鉴黄内容的检测 politics：政治敏感人物内容的检测 image_text：图文违规内容的检测（检测图片中出现的广告、色情、暴恐、涉政的文字违规内容以及二维码内容）

        :return: The image_categories of this VideoCreateRequest.
        :rtype: list[str]
        """
        return self._image_categories

    @image_categories.setter
    def image_categories(self, image_categories):
        r"""Sets the image_categories of this VideoCreateRequest.

        视频中画面需要检测的风险类型，列表不能为空。 terrorism：涉政暴恐内容的检测 porn：鉴黄内容的检测 politics：政治敏感人物内容的检测 image_text：图文违规内容的检测（检测图片中出现的广告、色情、暴恐、涉政的文字违规内容以及二维码内容）

        :param image_categories: The image_categories of this VideoCreateRequest.
        :type image_categories: list[str]
        """
        self._image_categories = image_categories

    @property
    def audio_categories(self):
        r"""Gets the audio_categories of this VideoCreateRequest.

        视频中音频需要检测的风险类型，不传或为空时表示不审核音频维度。 politics: 涉政检测 porn：涉黄检测 ad: 广告检测 moan: 娇喘检测 abuse: 辱骂检测

        :return: The audio_categories of this VideoCreateRequest.
        :rtype: list[str]
        """
        return self._audio_categories

    @audio_categories.setter
    def audio_categories(self, audio_categories):
        r"""Sets the audio_categories of this VideoCreateRequest.

        视频中音频需要检测的风险类型，不传或为空时表示不审核音频维度。 politics: 涉政检测 porn：涉黄检测 ad: 广告检测 moan: 娇喘检测 abuse: 辱骂检测

        :param audio_categories: The audio_categories of this VideoCreateRequest.
        :type audio_categories: list[str]
        """
        self._audio_categories = audio_categories

    @property
    def param_callback(self):
        r"""Gets the param_callback of this VideoCreateRequest.

        回调http接口：当该字段非空时，服务将根据该字段回调通知用户审核结果。

        :return: The param_callback of this VideoCreateRequest.
        :rtype: str
        """
        return self._param_callback

    @param_callback.setter
    def param_callback(self, param_callback):
        r"""Sets the param_callback of this VideoCreateRequest.

        回调http接口：当该字段非空时，服务将根据该字段回调通知用户审核结果。

        :param param_callback: The param_callback of this VideoCreateRequest.
        :type param_callback: str
        """
        self._param_callback = param_callback

    @property
    def seed(self):
        r"""Gets the seed of this VideoCreateRequest.

        用于回调通知时校验请求由华为云内容安全服务发起，由您自定义。随机字符串，由英文字母、数字、下划线组成，不超过64个字符。 说明：当seed非空时，headers中将包含X-Auth-Signature字段，字段的值使用HmacSHA256算法生成，待加密字符串由create_time、job_id、request_id、seed按照顺序拼接而成，密钥为seed。

        :return: The seed of this VideoCreateRequest.
        :rtype: str
        """
        return self._seed

    @seed.setter
    def seed(self, seed):
        r"""Sets the seed of this VideoCreateRequest.

        用于回调通知时校验请求由华为云内容安全服务发起，由您自定义。随机字符串，由英文字母、数字、下划线组成，不超过64个字符。 说明：当seed非空时，headers中将包含X-Auth-Signature字段，字段的值使用HmacSHA256算法生成，待加密字符串由create_time、job_id、request_id、seed按照顺序拼接而成，密钥为seed。

        :param seed: The seed of this VideoCreateRequest.
        :type seed: str
        """
        self._seed = seed

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
