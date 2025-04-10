# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CommonInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pvc': 'bool',
        'video_codec': 'str',
        'audio_codec': 'str',
        'is_black_cut': 'bool',
        'format': 'str',
        'hls_interval': 'int',
        'upsample': 'bool',
        'adaptation': 'str',
        'preset': 'int',
        'max_iframes_interval': 'int',
        'hls_audio_separate': 'bool',
        'hls_segment_type': 'str'
    }

    attribute_map = {
        'pvc': 'pvc',
        'video_codec': 'video_codec',
        'audio_codec': 'audio_codec',
        'is_black_cut': 'is_black_cut',
        'format': 'format',
        'hls_interval': 'hls_interval',
        'upsample': 'upsample',
        'adaptation': 'adaptation',
        'preset': 'preset',
        'max_iframes_interval': 'max_iframes_interval',
        'hls_audio_separate': 'hls_audio_separate',
        'hls_segment_type': 'hls_segment_type'
    }

    def __init__(self, pvc=None, video_codec=None, audio_codec=None, is_black_cut=None, format=None, hls_interval=None, upsample=None, adaptation=None, preset=None, max_iframes_interval=None, hls_audio_separate=None, hls_segment_type=None):
        r"""CommonInfo

        The model defined in huaweicloud sdk

        :param pvc: 高清低码开关&lt;br/&gt; 
        :type pvc: bool
        :param video_codec: 视频编码格式&lt;br/&gt; 
        :type video_codec: str
        :param audio_codec: 音频编码格式&lt;br/&gt; AAC：AAC格式 (default)&lt;br/&gt; HEAAC1：HEAAC1格式&lt;br/&gt; HEAAC2：HEAAC2格式&lt;br/&gt; MP3：MP3格式&lt;br/&gt; 
        :type audio_codec: str
        :param is_black_cut: 黑边剪裁类型&lt;br/&gt; 
        :type is_black_cut: bool
        :param format: 格式&lt;br/&gt; 
        :type format: str
        :param hls_interval: 分片时长(默认为5秒)&lt;br/&gt; 
        :type hls_interval: int
        :param upsample: 上采样&lt;br/&gt; 
        :type upsample: bool
        :param adaptation: SHORT：短边自适应&lt;br/&gt; LONG：长边自适应&lt;br/&gt; NONE：宽高自适应&lt;br/&gt; 
        :type adaptation: str
        :param preset: 编码质量等级，取值[0,2] 0表示当前现网方式默认方式，1表示转码效率优先，2表示转码质量优先。&lt;br/&gt; 
        :type preset: int
        :param max_iframes_interval: I帧最大间隔，取值范围：[2，10]。默认值：5，单位秒。&lt;br/&gt; 
        :type max_iframes_interval: int
        :param hls_audio_separate: 转码后音频是否独立存储。&lt;br/&gt; 
        :type hls_audio_separate: bool
        :param hls_segment_type: 分片的封装格式，目前支持TS和FMP4，默认TS格式。 
        :type hls_segment_type: str
        """
        
        

        self._pvc = None
        self._video_codec = None
        self._audio_codec = None
        self._is_black_cut = None
        self._format = None
        self._hls_interval = None
        self._upsample = None
        self._adaptation = None
        self._preset = None
        self._max_iframes_interval = None
        self._hls_audio_separate = None
        self._hls_segment_type = None
        self.discriminator = None

        if pvc is not None:
            self.pvc = pvc
        if video_codec is not None:
            self.video_codec = video_codec
        if audio_codec is not None:
            self.audio_codec = audio_codec
        if is_black_cut is not None:
            self.is_black_cut = is_black_cut
        self.format = format
        if hls_interval is not None:
            self.hls_interval = hls_interval
        if upsample is not None:
            self.upsample = upsample
        if adaptation is not None:
            self.adaptation = adaptation
        if preset is not None:
            self.preset = preset
        if max_iframes_interval is not None:
            self.max_iframes_interval = max_iframes_interval
        if hls_audio_separate is not None:
            self.hls_audio_separate = hls_audio_separate
        if hls_segment_type is not None:
            self.hls_segment_type = hls_segment_type

    @property
    def pvc(self):
        r"""Gets the pvc of this CommonInfo.

        高清低码开关<br/> 

        :return: The pvc of this CommonInfo.
        :rtype: bool
        """
        return self._pvc

    @pvc.setter
    def pvc(self, pvc):
        r"""Sets the pvc of this CommonInfo.

        高清低码开关<br/> 

        :param pvc: The pvc of this CommonInfo.
        :type pvc: bool
        """
        self._pvc = pvc

    @property
    def video_codec(self):
        r"""Gets the video_codec of this CommonInfo.

        视频编码格式<br/> 

        :return: The video_codec of this CommonInfo.
        :rtype: str
        """
        return self._video_codec

    @video_codec.setter
    def video_codec(self, video_codec):
        r"""Sets the video_codec of this CommonInfo.

        视频编码格式<br/> 

        :param video_codec: The video_codec of this CommonInfo.
        :type video_codec: str
        """
        self._video_codec = video_codec

    @property
    def audio_codec(self):
        r"""Gets the audio_codec of this CommonInfo.

        音频编码格式<br/> AAC：AAC格式 (default)<br/> HEAAC1：HEAAC1格式<br/> HEAAC2：HEAAC2格式<br/> MP3：MP3格式<br/> 

        :return: The audio_codec of this CommonInfo.
        :rtype: str
        """
        return self._audio_codec

    @audio_codec.setter
    def audio_codec(self, audio_codec):
        r"""Sets the audio_codec of this CommonInfo.

        音频编码格式<br/> AAC：AAC格式 (default)<br/> HEAAC1：HEAAC1格式<br/> HEAAC2：HEAAC2格式<br/> MP3：MP3格式<br/> 

        :param audio_codec: The audio_codec of this CommonInfo.
        :type audio_codec: str
        """
        self._audio_codec = audio_codec

    @property
    def is_black_cut(self):
        r"""Gets the is_black_cut of this CommonInfo.

        黑边剪裁类型<br/> 

        :return: The is_black_cut of this CommonInfo.
        :rtype: bool
        """
        return self._is_black_cut

    @is_black_cut.setter
    def is_black_cut(self, is_black_cut):
        r"""Sets the is_black_cut of this CommonInfo.

        黑边剪裁类型<br/> 

        :param is_black_cut: The is_black_cut of this CommonInfo.
        :type is_black_cut: bool
        """
        self._is_black_cut = is_black_cut

    @property
    def format(self):
        r"""Gets the format of this CommonInfo.

        格式<br/> 

        :return: The format of this CommonInfo.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        r"""Sets the format of this CommonInfo.

        格式<br/> 

        :param format: The format of this CommonInfo.
        :type format: str
        """
        self._format = format

    @property
    def hls_interval(self):
        r"""Gets the hls_interval of this CommonInfo.

        分片时长(默认为5秒)<br/> 

        :return: The hls_interval of this CommonInfo.
        :rtype: int
        """
        return self._hls_interval

    @hls_interval.setter
    def hls_interval(self, hls_interval):
        r"""Sets the hls_interval of this CommonInfo.

        分片时长(默认为5秒)<br/> 

        :param hls_interval: The hls_interval of this CommonInfo.
        :type hls_interval: int
        """
        self._hls_interval = hls_interval

    @property
    def upsample(self):
        r"""Gets the upsample of this CommonInfo.

        上采样<br/> 

        :return: The upsample of this CommonInfo.
        :rtype: bool
        """
        return self._upsample

    @upsample.setter
    def upsample(self, upsample):
        r"""Sets the upsample of this CommonInfo.

        上采样<br/> 

        :param upsample: The upsample of this CommonInfo.
        :type upsample: bool
        """
        self._upsample = upsample

    @property
    def adaptation(self):
        r"""Gets the adaptation of this CommonInfo.

        SHORT：短边自适应<br/> LONG：长边自适应<br/> NONE：宽高自适应<br/> 

        :return: The adaptation of this CommonInfo.
        :rtype: str
        """
        return self._adaptation

    @adaptation.setter
    def adaptation(self, adaptation):
        r"""Sets the adaptation of this CommonInfo.

        SHORT：短边自适应<br/> LONG：长边自适应<br/> NONE：宽高自适应<br/> 

        :param adaptation: The adaptation of this CommonInfo.
        :type adaptation: str
        """
        self._adaptation = adaptation

    @property
    def preset(self):
        r"""Gets the preset of this CommonInfo.

        编码质量等级，取值[0,2] 0表示当前现网方式默认方式，1表示转码效率优先，2表示转码质量优先。<br/> 

        :return: The preset of this CommonInfo.
        :rtype: int
        """
        return self._preset

    @preset.setter
    def preset(self, preset):
        r"""Sets the preset of this CommonInfo.

        编码质量等级，取值[0,2] 0表示当前现网方式默认方式，1表示转码效率优先，2表示转码质量优先。<br/> 

        :param preset: The preset of this CommonInfo.
        :type preset: int
        """
        self._preset = preset

    @property
    def max_iframes_interval(self):
        r"""Gets the max_iframes_interval of this CommonInfo.

        I帧最大间隔，取值范围：[2，10]。默认值：5，单位秒。<br/> 

        :return: The max_iframes_interval of this CommonInfo.
        :rtype: int
        """
        return self._max_iframes_interval

    @max_iframes_interval.setter
    def max_iframes_interval(self, max_iframes_interval):
        r"""Sets the max_iframes_interval of this CommonInfo.

        I帧最大间隔，取值范围：[2，10]。默认值：5，单位秒。<br/> 

        :param max_iframes_interval: The max_iframes_interval of this CommonInfo.
        :type max_iframes_interval: int
        """
        self._max_iframes_interval = max_iframes_interval

    @property
    def hls_audio_separate(self):
        r"""Gets the hls_audio_separate of this CommonInfo.

        转码后音频是否独立存储。<br/> 

        :return: The hls_audio_separate of this CommonInfo.
        :rtype: bool
        """
        return self._hls_audio_separate

    @hls_audio_separate.setter
    def hls_audio_separate(self, hls_audio_separate):
        r"""Sets the hls_audio_separate of this CommonInfo.

        转码后音频是否独立存储。<br/> 

        :param hls_audio_separate: The hls_audio_separate of this CommonInfo.
        :type hls_audio_separate: bool
        """
        self._hls_audio_separate = hls_audio_separate

    @property
    def hls_segment_type(self):
        r"""Gets the hls_segment_type of this CommonInfo.

        分片的封装格式，目前支持TS和FMP4，默认TS格式。 

        :return: The hls_segment_type of this CommonInfo.
        :rtype: str
        """
        return self._hls_segment_type

    @hls_segment_type.setter
    def hls_segment_type(self, hls_segment_type):
        r"""Sets the hls_segment_type of this CommonInfo.

        分片的封装格式，目前支持TS和FMP4，默认TS格式。 

        :param hls_segment_type: The hls_segment_type of this CommonInfo.
        :type hls_segment_type: str
        """
        self._hls_segment_type = hls_segment_type

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
        if not isinstance(other, CommonInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
