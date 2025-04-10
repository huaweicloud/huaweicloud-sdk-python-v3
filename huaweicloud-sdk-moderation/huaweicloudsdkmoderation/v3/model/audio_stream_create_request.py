# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AudioStreamCreateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data': 'AudioStreamCreateRequestData',
        'event_type': 'str',
        'categories': 'list[str]',
        'param_callback': 'str',
        'seed': 'str'
    }

    attribute_map = {
        'data': 'data',
        'event_type': 'event_type',
        'categories': 'categories',
        'param_callback': 'callback',
        'seed': 'seed'
    }

    def __init__(self, data=None, event_type=None, categories=None, param_callback=None, seed=None):
        r"""AudioStreamCreateRequest

        The model defined in huaweicloud sdk

        :param data: 
        :type data: :class:`huaweicloudsdkmoderation.v3.AudioStreamCreateRequestData`
        :param event_type: 事件类型，可选值如下： default：默认事件 audiobook：有声书 education：教育音频 game：游戏语音房 live：秀场直播 ecommerce：电商直播 voiceroom：交友语音房 private：私密语音聊天
        :type event_type: str
        :param categories: 需要检测的风险类型，列表不能为空。 porn：涉黄检测 politics: 涉政检测 abuse: 辱骂检测 ad: 广告检测 moan: 娇喘检测
        :type categories: list[str]
        :param param_callback: 回调http接口，服务将根据该字段回调通知用户审核结果，流未结束时，回调审核违规内容，流结束时，审核片段违规或不违规都将回调客户端。 回调内容如下： &#x60;&#x60;&#x60; {     \&quot;job_id\&quot;:\&quot;xxxxxx\&quot;,     \&quot;status\&quot;:\&quot;running\&quot;, //running - 审核中，succeeded - 审核完成，failed - 审核失败     \&quot;request_id\&quot;:\&quot;2419446b1fe14203f64e4018d12db3dd\&quot;,     \&quot;create_time\&quot;:\&quot;2022-07-30T08:57:11.011Z\&quot;,     \&quot;update_time\&quot;:\&quot;2022-07-30T08:57:14.014Z\&quot;,     \&quot;result\&quot;:{         \&quot;suggestion\&quot;:\&quot;block\&quot;,         \&quot;details\&quot;:[             {                 \&quot;suggestion\&quot;:\&quot;block\&quot;,                 \&quot;label\&quot;:\&quot;politics\&quot;,                 \&quot;audio_text\&quot;:\&quot;xxxx\&quot;,                 \&quot;start_time\&quot;:\&quot;2022-07-30T08:57:11.011Z\&quot;, // 当前音频片段开始的绝对时间                 \&quot;end_time\&quot;:\&quot;2022-07-30T08:57:21.011Z\&quot;,     // 当前音频片段结束的绝对时间                 \&quot;segments\&quot;:[                     {                         \&quot;segment\&quot;:\&quot;xxx\&quot;                     },                     {                         \&quot;segment\&quot;:\&quot;xxx\&quot;                     },                     {                         \&quot;segment\&quot;:\&quot;xxx\&quot;                     }                 ]             }         ],         \&quot;request_params\&quot;:{             \&quot;event_type\&quot;:\&quot;default\&quot;,             \&quot;data\&quot;:{                 \&quot;url\&quot;:\&quot;rtmp://xxxx\&quot;             },             \&quot;callback\&quot;:\&quot;http://xxx\&quot;,             \&quot;categories\&quot;:[                 \&quot;porn\&quot;,                 \&quot;ad\&quot;             ]         }     } }
        :type param_callback: str
        :param seed: 用于回调通知时校验请求由华为云内容安全服务发起，由您自定义。随机字符串，由英文字母、数字、下划线组成，不超过64个字符。 说明：当seed非空时，headers中将包含X-Auth-Signature字段，字段的值使用HmacSHA256算法生成，待加密字符串由create_time、job_id、request_id、seed按照顺序拼接而成，密钥为seed。
        :type seed: str
        """
        
        

        self._data = None
        self._event_type = None
        self._categories = None
        self._param_callback = None
        self._seed = None
        self.discriminator = None

        self.data = data
        self.event_type = event_type
        self.categories = categories
        self.param_callback = param_callback
        if seed is not None:
            self.seed = seed

    @property
    def data(self):
        r"""Gets the data of this AudioStreamCreateRequest.

        :return: The data of this AudioStreamCreateRequest.
        :rtype: :class:`huaweicloudsdkmoderation.v3.AudioStreamCreateRequestData`
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this AudioStreamCreateRequest.

        :param data: The data of this AudioStreamCreateRequest.
        :type data: :class:`huaweicloudsdkmoderation.v3.AudioStreamCreateRequestData`
        """
        self._data = data

    @property
    def event_type(self):
        r"""Gets the event_type of this AudioStreamCreateRequest.

        事件类型，可选值如下： default：默认事件 audiobook：有声书 education：教育音频 game：游戏语音房 live：秀场直播 ecommerce：电商直播 voiceroom：交友语音房 private：私密语音聊天

        :return: The event_type of this AudioStreamCreateRequest.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        r"""Sets the event_type of this AudioStreamCreateRequest.

        事件类型，可选值如下： default：默认事件 audiobook：有声书 education：教育音频 game：游戏语音房 live：秀场直播 ecommerce：电商直播 voiceroom：交友语音房 private：私密语音聊天

        :param event_type: The event_type of this AudioStreamCreateRequest.
        :type event_type: str
        """
        self._event_type = event_type

    @property
    def categories(self):
        r"""Gets the categories of this AudioStreamCreateRequest.

        需要检测的风险类型，列表不能为空。 porn：涉黄检测 politics: 涉政检测 abuse: 辱骂检测 ad: 广告检测 moan: 娇喘检测

        :return: The categories of this AudioStreamCreateRequest.
        :rtype: list[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        r"""Sets the categories of this AudioStreamCreateRequest.

        需要检测的风险类型，列表不能为空。 porn：涉黄检测 politics: 涉政检测 abuse: 辱骂检测 ad: 广告检测 moan: 娇喘检测

        :param categories: The categories of this AudioStreamCreateRequest.
        :type categories: list[str]
        """
        self._categories = categories

    @property
    def param_callback(self):
        r"""Gets the param_callback of this AudioStreamCreateRequest.

        回调http接口，服务将根据该字段回调通知用户审核结果，流未结束时，回调审核违规内容，流结束时，审核片段违规或不违规都将回调客户端。 回调内容如下： ``` {     \"job_id\":\"xxxxxx\",     \"status\":\"running\", //running - 审核中，succeeded - 审核完成，failed - 审核失败     \"request_id\":\"2419446b1fe14203f64e4018d12db3dd\",     \"create_time\":\"2022-07-30T08:57:11.011Z\",     \"update_time\":\"2022-07-30T08:57:14.014Z\",     \"result\":{         \"suggestion\":\"block\",         \"details\":[             {                 \"suggestion\":\"block\",                 \"label\":\"politics\",                 \"audio_text\":\"xxxx\",                 \"start_time\":\"2022-07-30T08:57:11.011Z\", // 当前音频片段开始的绝对时间                 \"end_time\":\"2022-07-30T08:57:21.011Z\",     // 当前音频片段结束的绝对时间                 \"segments\":[                     {                         \"segment\":\"xxx\"                     },                     {                         \"segment\":\"xxx\"                     },                     {                         \"segment\":\"xxx\"                     }                 ]             }         ],         \"request_params\":{             \"event_type\":\"default\",             \"data\":{                 \"url\":\"rtmp://xxxx\"             },             \"callback\":\"http://xxx\",             \"categories\":[                 \"porn\",                 \"ad\"             ]         }     } }

        :return: The param_callback of this AudioStreamCreateRequest.
        :rtype: str
        """
        return self._param_callback

    @param_callback.setter
    def param_callback(self, param_callback):
        r"""Sets the param_callback of this AudioStreamCreateRequest.

        回调http接口，服务将根据该字段回调通知用户审核结果，流未结束时，回调审核违规内容，流结束时，审核片段违规或不违规都将回调客户端。 回调内容如下： ``` {     \"job_id\":\"xxxxxx\",     \"status\":\"running\", //running - 审核中，succeeded - 审核完成，failed - 审核失败     \"request_id\":\"2419446b1fe14203f64e4018d12db3dd\",     \"create_time\":\"2022-07-30T08:57:11.011Z\",     \"update_time\":\"2022-07-30T08:57:14.014Z\",     \"result\":{         \"suggestion\":\"block\",         \"details\":[             {                 \"suggestion\":\"block\",                 \"label\":\"politics\",                 \"audio_text\":\"xxxx\",                 \"start_time\":\"2022-07-30T08:57:11.011Z\", // 当前音频片段开始的绝对时间                 \"end_time\":\"2022-07-30T08:57:21.011Z\",     // 当前音频片段结束的绝对时间                 \"segments\":[                     {                         \"segment\":\"xxx\"                     },                     {                         \"segment\":\"xxx\"                     },                     {                         \"segment\":\"xxx\"                     }                 ]             }         ],         \"request_params\":{             \"event_type\":\"default\",             \"data\":{                 \"url\":\"rtmp://xxxx\"             },             \"callback\":\"http://xxx\",             \"categories\":[                 \"porn\",                 \"ad\"             ]         }     } }

        :param param_callback: The param_callback of this AudioStreamCreateRequest.
        :type param_callback: str
        """
        self._param_callback = param_callback

    @property
    def seed(self):
        r"""Gets the seed of this AudioStreamCreateRequest.

        用于回调通知时校验请求由华为云内容安全服务发起，由您自定义。随机字符串，由英文字母、数字、下划线组成，不超过64个字符。 说明：当seed非空时，headers中将包含X-Auth-Signature字段，字段的值使用HmacSHA256算法生成，待加密字符串由create_time、job_id、request_id、seed按照顺序拼接而成，密钥为seed。

        :return: The seed of this AudioStreamCreateRequest.
        :rtype: str
        """
        return self._seed

    @seed.setter
    def seed(self, seed):
        r"""Sets the seed of this AudioStreamCreateRequest.

        用于回调通知时校验请求由华为云内容安全服务发起，由您自定义。随机字符串，由英文字母、数字、下划线组成，不超过64个字符。 说明：当seed非空时，headers中将包含X-Auth-Signature字段，字段的值使用HmacSHA256算法生成，待加密字符串由create_time、job_id、request_id、seed按照顺序拼接而成，密钥为seed。

        :param seed: The seed of this AudioStreamCreateRequest.
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
        if not isinstance(other, AudioStreamCreateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
