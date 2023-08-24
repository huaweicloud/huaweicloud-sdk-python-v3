# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TtsConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'audio_format': 'str',
        'sample_rate': 'str',
        '_property': 'str',
        'speed': 'int',
        'pitch': 'int',
        'volume': 'int'
    }

    attribute_map = {
        'audio_format': 'audio_format',
        'sample_rate': 'sample_rate',
        '_property': 'property',
        'speed': 'speed',
        'pitch': 'pitch',
        'volume': 'volume'
    }

    def __init__(self, audio_format=None, sample_rate=None, _property=None, speed=None, pitch=None, volume=None):
        """TtsConfig

        The model defined in huaweicloud sdk

        :param audio_format: 语音格式头：wav、mp3、pcm。 默认：wav
        :type audio_format: str
        :param sample_rate: 采样率：16000、8000 默认：8000
        :type sample_rate: str
        :param _property: 语音合成特征字符串，组成形式为{language}_{speaker}_{domain}，即“语种_人员标识_领域”。发音人分为普通发音人和精品发音人。  普通发音人每100字计一次调用，取值范围如下：   chinese_xiaoqi_common  小琪，标准女声发音人。  chinese_xiaoyu_common  小宇，标准男声发音人。  chinese_xiaoyan_common  小燕，温柔女声发音人。  chinese_xiaowang_common  小王，童声发音人。  chinese_xiaowen_common   小雯，柔美女声发音人。  chinese_xiaojing_common 小婧，俏皮女声发音人。  chinese_xiaosong_common  小宋，激昂男声发音人。  chinese_xiaoxia_common   小夏，热情女声发音人。  chinese_xiaodai_common   小呆，呆萌童声发音人。  chinese_xiaoqian_common  小倩，成熟女声发音人。  english_cameal_common    cameal，柔美女声英文发音人。   精品发音人每50字计一次调用，区域仅支持cn-north-4，cn-east-3，暂时不支持音高调节，取值范围如下：  chinese_huaxiaoxia_common  华小夏，热情女声发音人。  chinese_huaxiaogang_common  华晓刚，利落男声发音人。  chinese_huaxiaolu_common  华小璐，知性女声发音人。  chinese_huaxiaoshu_common  华小舒，舒缓女声发音人。  chinese_huaxiaowei_common  华小唯，嗲柔女声发音人。  chinese_huaxiaoliang_common  华小靓，嘹亮女声发音人。  chinese_huaxiaodong_common  华晓东，成熟男声发音人。  chinese_huaxiaoyan_common  华小颜，严厉女声发音人。  chinese_huaxiaoxuan_common  华小萱，台湾女声发音人。  chinese_huaxiaowen_common  华小雯，柔美女声发音人。  chinese_huaxiaoyang_common  华晓阳，朝气男声发音人。  chinese_huaxiaomin_common  华小闽，闽南女声发音人。  chinese_huanvxia_literature 华女侠，武侠女生发音人，只支持16k的采样率。  chinese_huaxiaoxuan_literature 华晓悬，悬疑男声发音人，只支持16k的采样率。  chinese_huaxiaomei_common 华小美，温柔女声发音人。  chinese_huaxiaofei_common 华小飞，朝气男声发音人。  chinese_huaxiaolong_common 华小龙，朝气男声发音人。  chinese_huaxiaorui_common 华小蕊，知性女声发音人。  chinese_huaxiaoru_common 华小汝，柔美女声发音人(中英混)。  chinese_huaxiaohan_common 华小涵，知性女声发音人(中英混)。  chinese_huaxiaoning_common 华小宁，沉稳男声发言人(中英混)。  chinese_huaxiaozhen_common 华小珍，温柔女声发音人(中英混)。  chinese_huaxiaoman_common 华小曼，温柔女声发音人(中英混)。  chinese_huaxiaofang_common 华小芳，朝气女声发音人(中英混)。  chinese_huaxiaojun_common 华小筠，成熟女声发音人(中英混)。  english_alvin_common alvin，成熟男声纯英文发音人。  english_amy_common amy amy，成熟女声纯英文发音人。  默认：chinese_xiaoyan_common
        :type _property: str
        :param speed: 语速。 取值范围：[-500,500]  默认值：0
        :type speed: int
        :param pitch: 音高。 取值范围： [-500,500]  默认值：0
        :type pitch: int
        :param volume: 音量。 取值范围：[0, 100]  默认值：50
        :type volume: int
        """
        
        

        self._audio_format = None
        self._sample_rate = None
        self.__property = None
        self._speed = None
        self._pitch = None
        self._volume = None
        self.discriminator = None

        if audio_format is not None:
            self.audio_format = audio_format
        if sample_rate is not None:
            self.sample_rate = sample_rate
        if _property is not None:
            self._property = _property
        if speed is not None:
            self.speed = speed
        if pitch is not None:
            self.pitch = pitch
        if volume is not None:
            self.volume = volume

    @property
    def audio_format(self):
        """Gets the audio_format of this TtsConfig.

        语音格式头：wav、mp3、pcm。 默认：wav

        :return: The audio_format of this TtsConfig.
        :rtype: str
        """
        return self._audio_format

    @audio_format.setter
    def audio_format(self, audio_format):
        """Sets the audio_format of this TtsConfig.

        语音格式头：wav、mp3、pcm。 默认：wav

        :param audio_format: The audio_format of this TtsConfig.
        :type audio_format: str
        """
        self._audio_format = audio_format

    @property
    def sample_rate(self):
        """Gets the sample_rate of this TtsConfig.

        采样率：16000、8000 默认：8000

        :return: The sample_rate of this TtsConfig.
        :rtype: str
        """
        return self._sample_rate

    @sample_rate.setter
    def sample_rate(self, sample_rate):
        """Sets the sample_rate of this TtsConfig.

        采样率：16000、8000 默认：8000

        :param sample_rate: The sample_rate of this TtsConfig.
        :type sample_rate: str
        """
        self._sample_rate = sample_rate

    @property
    def _property(self):
        """Gets the _property of this TtsConfig.

        语音合成特征字符串，组成形式为{language}_{speaker}_{domain}，即“语种_人员标识_领域”。发音人分为普通发音人和精品发音人。  普通发音人每100字计一次调用，取值范围如下：   chinese_xiaoqi_common  小琪，标准女声发音人。  chinese_xiaoyu_common  小宇，标准男声发音人。  chinese_xiaoyan_common  小燕，温柔女声发音人。  chinese_xiaowang_common  小王，童声发音人。  chinese_xiaowen_common   小雯，柔美女声发音人。  chinese_xiaojing_common 小婧，俏皮女声发音人。  chinese_xiaosong_common  小宋，激昂男声发音人。  chinese_xiaoxia_common   小夏，热情女声发音人。  chinese_xiaodai_common   小呆，呆萌童声发音人。  chinese_xiaoqian_common  小倩，成熟女声发音人。  english_cameal_common    cameal，柔美女声英文发音人。   精品发音人每50字计一次调用，区域仅支持cn-north-4，cn-east-3，暂时不支持音高调节，取值范围如下：  chinese_huaxiaoxia_common  华小夏，热情女声发音人。  chinese_huaxiaogang_common  华晓刚，利落男声发音人。  chinese_huaxiaolu_common  华小璐，知性女声发音人。  chinese_huaxiaoshu_common  华小舒，舒缓女声发音人。  chinese_huaxiaowei_common  华小唯，嗲柔女声发音人。  chinese_huaxiaoliang_common  华小靓，嘹亮女声发音人。  chinese_huaxiaodong_common  华晓东，成熟男声发音人。  chinese_huaxiaoyan_common  华小颜，严厉女声发音人。  chinese_huaxiaoxuan_common  华小萱，台湾女声发音人。  chinese_huaxiaowen_common  华小雯，柔美女声发音人。  chinese_huaxiaoyang_common  华晓阳，朝气男声发音人。  chinese_huaxiaomin_common  华小闽，闽南女声发音人。  chinese_huanvxia_literature 华女侠，武侠女生发音人，只支持16k的采样率。  chinese_huaxiaoxuan_literature 华晓悬，悬疑男声发音人，只支持16k的采样率。  chinese_huaxiaomei_common 华小美，温柔女声发音人。  chinese_huaxiaofei_common 华小飞，朝气男声发音人。  chinese_huaxiaolong_common 华小龙，朝气男声发音人。  chinese_huaxiaorui_common 华小蕊，知性女声发音人。  chinese_huaxiaoru_common 华小汝，柔美女声发音人(中英混)。  chinese_huaxiaohan_common 华小涵，知性女声发音人(中英混)。  chinese_huaxiaoning_common 华小宁，沉稳男声发言人(中英混)。  chinese_huaxiaozhen_common 华小珍，温柔女声发音人(中英混)。  chinese_huaxiaoman_common 华小曼，温柔女声发音人(中英混)。  chinese_huaxiaofang_common 华小芳，朝气女声发音人(中英混)。  chinese_huaxiaojun_common 华小筠，成熟女声发音人(中英混)。  english_alvin_common alvin，成熟男声纯英文发音人。  english_amy_common amy amy，成熟女声纯英文发音人。  默认：chinese_xiaoyan_common

        :return: The _property of this TtsConfig.
        :rtype: str
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        """Sets the _property of this TtsConfig.

        语音合成特征字符串，组成形式为{language}_{speaker}_{domain}，即“语种_人员标识_领域”。发音人分为普通发音人和精品发音人。  普通发音人每100字计一次调用，取值范围如下：   chinese_xiaoqi_common  小琪，标准女声发音人。  chinese_xiaoyu_common  小宇，标准男声发音人。  chinese_xiaoyan_common  小燕，温柔女声发音人。  chinese_xiaowang_common  小王，童声发音人。  chinese_xiaowen_common   小雯，柔美女声发音人。  chinese_xiaojing_common 小婧，俏皮女声发音人。  chinese_xiaosong_common  小宋，激昂男声发音人。  chinese_xiaoxia_common   小夏，热情女声发音人。  chinese_xiaodai_common   小呆，呆萌童声发音人。  chinese_xiaoqian_common  小倩，成熟女声发音人。  english_cameal_common    cameal，柔美女声英文发音人。   精品发音人每50字计一次调用，区域仅支持cn-north-4，cn-east-3，暂时不支持音高调节，取值范围如下：  chinese_huaxiaoxia_common  华小夏，热情女声发音人。  chinese_huaxiaogang_common  华晓刚，利落男声发音人。  chinese_huaxiaolu_common  华小璐，知性女声发音人。  chinese_huaxiaoshu_common  华小舒，舒缓女声发音人。  chinese_huaxiaowei_common  华小唯，嗲柔女声发音人。  chinese_huaxiaoliang_common  华小靓，嘹亮女声发音人。  chinese_huaxiaodong_common  华晓东，成熟男声发音人。  chinese_huaxiaoyan_common  华小颜，严厉女声发音人。  chinese_huaxiaoxuan_common  华小萱，台湾女声发音人。  chinese_huaxiaowen_common  华小雯，柔美女声发音人。  chinese_huaxiaoyang_common  华晓阳，朝气男声发音人。  chinese_huaxiaomin_common  华小闽，闽南女声发音人。  chinese_huanvxia_literature 华女侠，武侠女生发音人，只支持16k的采样率。  chinese_huaxiaoxuan_literature 华晓悬，悬疑男声发音人，只支持16k的采样率。  chinese_huaxiaomei_common 华小美，温柔女声发音人。  chinese_huaxiaofei_common 华小飞，朝气男声发音人。  chinese_huaxiaolong_common 华小龙，朝气男声发音人。  chinese_huaxiaorui_common 华小蕊，知性女声发音人。  chinese_huaxiaoru_common 华小汝，柔美女声发音人(中英混)。  chinese_huaxiaohan_common 华小涵，知性女声发音人(中英混)。  chinese_huaxiaoning_common 华小宁，沉稳男声发言人(中英混)。  chinese_huaxiaozhen_common 华小珍，温柔女声发音人(中英混)。  chinese_huaxiaoman_common 华小曼，温柔女声发音人(中英混)。  chinese_huaxiaofang_common 华小芳，朝气女声发音人(中英混)。  chinese_huaxiaojun_common 华小筠，成熟女声发音人(中英混)。  english_alvin_common alvin，成熟男声纯英文发音人。  english_amy_common amy amy，成熟女声纯英文发音人。  默认：chinese_xiaoyan_common

        :param _property: The _property of this TtsConfig.
        :type _property: str
        """
        self.__property = _property

    @property
    def speed(self):
        """Gets the speed of this TtsConfig.

        语速。 取值范围：[-500,500]  默认值：0

        :return: The speed of this TtsConfig.
        :rtype: int
        """
        return self._speed

    @speed.setter
    def speed(self, speed):
        """Sets the speed of this TtsConfig.

        语速。 取值范围：[-500,500]  默认值：0

        :param speed: The speed of this TtsConfig.
        :type speed: int
        """
        self._speed = speed

    @property
    def pitch(self):
        """Gets the pitch of this TtsConfig.

        音高。 取值范围： [-500,500]  默认值：0

        :return: The pitch of this TtsConfig.
        :rtype: int
        """
        return self._pitch

    @pitch.setter
    def pitch(self, pitch):
        """Sets the pitch of this TtsConfig.

        音高。 取值范围： [-500,500]  默认值：0

        :param pitch: The pitch of this TtsConfig.
        :type pitch: int
        """
        self._pitch = pitch

    @property
    def volume(self):
        """Gets the volume of this TtsConfig.

        音量。 取值范围：[0, 100]  默认值：50

        :return: The volume of this TtsConfig.
        :rtype: int
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this TtsConfig.

        音量。 取值范围：[0, 100]  默认值：50

        :param volume: The volume of this TtsConfig.
        :type volume: int
        """
        self._volume = volume

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
        if not isinstance(other, TtsConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
