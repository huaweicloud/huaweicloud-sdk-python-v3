# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VideoStreamCreateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data': 'VideoStreamCreateRequestData',
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
        """VideoStreamCreateRequest

        The model defined in huaweicloud sdk

        :param data: 
        :type data: :class:`huaweicloudsdkmoderation.v3.VideoStreamCreateRequestData`
        :param event_type: 事件类型，可选值如下： default：默认事件
        :type event_type: str
        :param image_categories: 视频流中画面需要检测的风险类型，列表不能为空。 porn：鉴黄内容的检测 terrorism：涉政暴恐内容的检测 politics：政治敏感人物内容的检测 image_text：图文违规内容的检测（检测图片中出现的广告、色情、暴恐、涉政的文字违规内容以及二维码内容）
        :type image_categories: list[str]
        :param audio_categories: 视频流中音频需要检测的风险类型，不传或为空时表示不审核音频维度。 porn：涉黄检测 politics: 涉政检测 abuse: 辱骂检测 ad: 广告检测 moan: 娇喘检测
        :type audio_categories: list[str]
        :param param_callback: 回调http接口，回调内容如下： &#x60;&#x60;&#x60;{     \&quot;job_id\&quot;:\&quot;xxxxxx\&quot;,     \&quot;status\&quot;:\&quot;running\&quot;, //running - 审核中，succeeded - 审核完成，failed - 审核失败     \&quot;request_id\&quot;:\&quot;2419446b1fe14203f64e4018d12db3dd\&quot;,     \&quot;craete_time\&quot;:\&quot;2022-07-30T08:57:11.011Z\&quot;,     \&quot;update_time\&quot;:\&quot;2022-07-30T08:57:14.014Z\&quot;,     \&quot;result\&quot;:{         \&quot;suggestion\&quot;:\&quot;block\&quot;,         \&quot;audio_detail\&quot;:[             {                 \&quot;suggestion\&quot;:\&quot;block\&quot;,                 \&quot;label\&quot;:\&quot;politics\&quot;,                 \&quot;audio_text\&quot;:\&quot;xxxx\&quot;,                 \&quot;detail\&quot;:[                     {                         \&quot;confidence\&quot;:1,                         \&quot;suggestion\&quot;:\&quot;block\&quot;,                         \&quot;label\&quot;:\&quot;politics\&quot;,                         \&quot;segments\&quot;:[                             {                                 \&quot;segment\&quot;:\&quot;xxx\&quot;                             },                             {                                 \&quot;segment\&quot;:\&quot;xxx\&quot;                             },                             {                                 \&quot;segment\&quot;:\&quot;xxx\&quot;                             }                         ]                     }                 ]             }         ],         \&quot;image_detail\&quot;:[             {                 \&quot;suggestion\&quot;:\&quot;block\&quot;,                 \&quot;category\&quot;:\&quot;xxx\&quot;,                 \&quot;time\&quot;:\&quot;xxx\&quot;, // 视频流截帧图片发生的绝对时间                 \&quot;detail\&quot;:[                     {                         \&quot;face_location\&quot;:{                             \&quot;bottom_right_x\&quot;:247,                             \&quot;bottom_right_y\&quot;:191,                             \&quot;top_left_y\&quot;:79,                             \&quot;top_left_x\&quot;:160                         },                         \&quot;confidence\&quot;:1,                         \&quot;suggestion\&quot;:\&quot;block\&quot;,                         \&quot;label\&quot;:\&quot;xxx\&quot;,                         \&quot;category\&quot;:\&quot;xxx\&quot;                     },                     {                         \&quot;qr_content\&quot;:\&quot;xxx\&quot;,                         \&quot;confidence\&quot;:\&quot;xxx\&quot;,                         \&quot;suggestion\&quot;:\&quot;xxx\&quot;,                         \&quot;label\&quot;:\&quot;xxx\&quot;,                         \&quot;category\&quot;:\&quot;xxx\&quot;,                         \&quot;qr_location\&quot;:{                             \&quot;bottom_right_x\&quot;:554,                             \&quot;bottom_right_y\&quot;:842,                             \&quot;top_left_y\&quot;:426,                             \&quot;top_left_x\&quot;:140                         }                     },                     {                         \&quot;confidence\&quot;:1,                         \&quot;suggestion\&quot;:\&quot;block\&quot;,                         \&quot;label\&quot;:\&quot;politics\&quot;,                         \&quot;category\&quot;:\&quot;image_text\&quot;,                         \&quot;segments\&quot;:[                             {                                 \&quot;segment\&quot;:\&quot;x\&quot;                             },                             {                                 \&quot;segment\&quot;:\&quot;xxx\&quot;                             },                             {                                 \&quot;segment\&quot;:\&quot;xx\&quot;                             },                             {                                 \&quot;segment\&quot;:\&quot;x\&quot;                             },                             {                                 \&quot;segment\&quot;:\&quot;xxxx\&quot;                             }                         ]                     }                 ]             }         ]     },     \&quot;request_params\&quot;:{         \&quot;data\&quot;:{             \&quot;url\&quot;:\&quot;rtmp://xxxx\&quot;,             \&quot;frame_interval\&quot;:3         },         \&quot;event_type\&quot;:\&quot;default\&quot;,         \&quot;image_categories\&quot;:[             \&quot;politics\&quot;,             \&quot;porn\&quot;,             \&quot;image_text\&quot;,             \&quot;terrorism\&quot;         ],         \&quot;audio_categories\&quot;:[             \&quot;porn\&quot;,             \&quot;ad\&quot;,             \&quot;politics\&quot;,             \&quot;moan\&quot;,             \&quot;abuse\&quot;         ],         \&quot;callback\&quot;:\&quot;http://xxx/callback\&quot;     } }
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
        self.param_callback = param_callback

    @property
    def data(self):
        """Gets the data of this VideoStreamCreateRequest.

        :return: The data of this VideoStreamCreateRequest.
        :rtype: :class:`huaweicloudsdkmoderation.v3.VideoStreamCreateRequestData`
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this VideoStreamCreateRequest.

        :param data: The data of this VideoStreamCreateRequest.
        :type data: :class:`huaweicloudsdkmoderation.v3.VideoStreamCreateRequestData`
        """
        self._data = data

    @property
    def event_type(self):
        """Gets the event_type of this VideoStreamCreateRequest.

        事件类型，可选值如下： default：默认事件

        :return: The event_type of this VideoStreamCreateRequest.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this VideoStreamCreateRequest.

        事件类型，可选值如下： default：默认事件

        :param event_type: The event_type of this VideoStreamCreateRequest.
        :type event_type: str
        """
        self._event_type = event_type

    @property
    def image_categories(self):
        """Gets the image_categories of this VideoStreamCreateRequest.

        视频流中画面需要检测的风险类型，列表不能为空。 porn：鉴黄内容的检测 terrorism：涉政暴恐内容的检测 politics：政治敏感人物内容的检测 image_text：图文违规内容的检测（检测图片中出现的广告、色情、暴恐、涉政的文字违规内容以及二维码内容）

        :return: The image_categories of this VideoStreamCreateRequest.
        :rtype: list[str]
        """
        return self._image_categories

    @image_categories.setter
    def image_categories(self, image_categories):
        """Sets the image_categories of this VideoStreamCreateRequest.

        视频流中画面需要检测的风险类型，列表不能为空。 porn：鉴黄内容的检测 terrorism：涉政暴恐内容的检测 politics：政治敏感人物内容的检测 image_text：图文违规内容的检测（检测图片中出现的广告、色情、暴恐、涉政的文字违规内容以及二维码内容）

        :param image_categories: The image_categories of this VideoStreamCreateRequest.
        :type image_categories: list[str]
        """
        self._image_categories = image_categories

    @property
    def audio_categories(self):
        """Gets the audio_categories of this VideoStreamCreateRequest.

        视频流中音频需要检测的风险类型，不传或为空时表示不审核音频维度。 porn：涉黄检测 politics: 涉政检测 abuse: 辱骂检测 ad: 广告检测 moan: 娇喘检测

        :return: The audio_categories of this VideoStreamCreateRequest.
        :rtype: list[str]
        """
        return self._audio_categories

    @audio_categories.setter
    def audio_categories(self, audio_categories):
        """Sets the audio_categories of this VideoStreamCreateRequest.

        视频流中音频需要检测的风险类型，不传或为空时表示不审核音频维度。 porn：涉黄检测 politics: 涉政检测 abuse: 辱骂检测 ad: 广告检测 moan: 娇喘检测

        :param audio_categories: The audio_categories of this VideoStreamCreateRequest.
        :type audio_categories: list[str]
        """
        self._audio_categories = audio_categories

    @property
    def param_callback(self):
        """Gets the param_callback of this VideoStreamCreateRequest.

        回调http接口，回调内容如下： ```{     \"job_id\":\"xxxxxx\",     \"status\":\"running\", //running - 审核中，succeeded - 审核完成，failed - 审核失败     \"request_id\":\"2419446b1fe14203f64e4018d12db3dd\",     \"craete_time\":\"2022-07-30T08:57:11.011Z\",     \"update_time\":\"2022-07-30T08:57:14.014Z\",     \"result\":{         \"suggestion\":\"block\",         \"audio_detail\":[             {                 \"suggestion\":\"block\",                 \"label\":\"politics\",                 \"audio_text\":\"xxxx\",                 \"detail\":[                     {                         \"confidence\":1,                         \"suggestion\":\"block\",                         \"label\":\"politics\",                         \"segments\":[                             {                                 \"segment\":\"xxx\"                             },                             {                                 \"segment\":\"xxx\"                             },                             {                                 \"segment\":\"xxx\"                             }                         ]                     }                 ]             }         ],         \"image_detail\":[             {                 \"suggestion\":\"block\",                 \"category\":\"xxx\",                 \"time\":\"xxx\", // 视频流截帧图片发生的绝对时间                 \"detail\":[                     {                         \"face_location\":{                             \"bottom_right_x\":247,                             \"bottom_right_y\":191,                             \"top_left_y\":79,                             \"top_left_x\":160                         },                         \"confidence\":1,                         \"suggestion\":\"block\",                         \"label\":\"xxx\",                         \"category\":\"xxx\"                     },                     {                         \"qr_content\":\"xxx\",                         \"confidence\":\"xxx\",                         \"suggestion\":\"xxx\",                         \"label\":\"xxx\",                         \"category\":\"xxx\",                         \"qr_location\":{                             \"bottom_right_x\":554,                             \"bottom_right_y\":842,                             \"top_left_y\":426,                             \"top_left_x\":140                         }                     },                     {                         \"confidence\":1,                         \"suggestion\":\"block\",                         \"label\":\"politics\",                         \"category\":\"image_text\",                         \"segments\":[                             {                                 \"segment\":\"x\"                             },                             {                                 \"segment\":\"xxx\"                             },                             {                                 \"segment\":\"xx\"                             },                             {                                 \"segment\":\"x\"                             },                             {                                 \"segment\":\"xxxx\"                             }                         ]                     }                 ]             }         ]     },     \"request_params\":{         \"data\":{             \"url\":\"rtmp://xxxx\",             \"frame_interval\":3         },         \"event_type\":\"default\",         \"image_categories\":[             \"politics\",             \"porn\",             \"image_text\",             \"terrorism\"         ],         \"audio_categories\":[             \"porn\",             \"ad\",             \"politics\",             \"moan\",             \"abuse\"         ],         \"callback\":\"http://xxx/callback\"     } }

        :return: The param_callback of this VideoStreamCreateRequest.
        :rtype: str
        """
        return self._param_callback

    @param_callback.setter
    def param_callback(self, param_callback):
        """Sets the param_callback of this VideoStreamCreateRequest.

        回调http接口，回调内容如下： ```{     \"job_id\":\"xxxxxx\",     \"status\":\"running\", //running - 审核中，succeeded - 审核完成，failed - 审核失败     \"request_id\":\"2419446b1fe14203f64e4018d12db3dd\",     \"craete_time\":\"2022-07-30T08:57:11.011Z\",     \"update_time\":\"2022-07-30T08:57:14.014Z\",     \"result\":{         \"suggestion\":\"block\",         \"audio_detail\":[             {                 \"suggestion\":\"block\",                 \"label\":\"politics\",                 \"audio_text\":\"xxxx\",                 \"detail\":[                     {                         \"confidence\":1,                         \"suggestion\":\"block\",                         \"label\":\"politics\",                         \"segments\":[                             {                                 \"segment\":\"xxx\"                             },                             {                                 \"segment\":\"xxx\"                             },                             {                                 \"segment\":\"xxx\"                             }                         ]                     }                 ]             }         ],         \"image_detail\":[             {                 \"suggestion\":\"block\",                 \"category\":\"xxx\",                 \"time\":\"xxx\", // 视频流截帧图片发生的绝对时间                 \"detail\":[                     {                         \"face_location\":{                             \"bottom_right_x\":247,                             \"bottom_right_y\":191,                             \"top_left_y\":79,                             \"top_left_x\":160                         },                         \"confidence\":1,                         \"suggestion\":\"block\",                         \"label\":\"xxx\",                         \"category\":\"xxx\"                     },                     {                         \"qr_content\":\"xxx\",                         \"confidence\":\"xxx\",                         \"suggestion\":\"xxx\",                         \"label\":\"xxx\",                         \"category\":\"xxx\",                         \"qr_location\":{                             \"bottom_right_x\":554,                             \"bottom_right_y\":842,                             \"top_left_y\":426,                             \"top_left_x\":140                         }                     },                     {                         \"confidence\":1,                         \"suggestion\":\"block\",                         \"label\":\"politics\",                         \"category\":\"image_text\",                         \"segments\":[                             {                                 \"segment\":\"x\"                             },                             {                                 \"segment\":\"xxx\"                             },                             {                                 \"segment\":\"xx\"                             },                             {                                 \"segment\":\"x\"                             },                             {                                 \"segment\":\"xxxx\"                             }                         ]                     }                 ]             }         ]     },     \"request_params\":{         \"data\":{             \"url\":\"rtmp://xxxx\",             \"frame_interval\":3         },         \"event_type\":\"default\",         \"image_categories\":[             \"politics\",             \"porn\",             \"image_text\",             \"terrorism\"         ],         \"audio_categories\":[             \"porn\",             \"ad\",             \"politics\",             \"moan\",             \"abuse\"         ],         \"callback\":\"http://xxx/callback\"     } }

        :param param_callback: The param_callback of this VideoStreamCreateRequest.
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
        if not isinstance(other, VideoStreamCreateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
