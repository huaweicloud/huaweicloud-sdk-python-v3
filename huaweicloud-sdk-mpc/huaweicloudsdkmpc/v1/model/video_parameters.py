# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VideoParameters:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'output_policy': 'str',
        'codec': 'int',
        'crf': 'object',
        'max_bitrate': 'int',
        'bitrate': 'int',
        'profile': 'int',
        'level': 'int',
        'preset': 'int',
        'max_iframes_interval': 'int',
        'bframes_count': 'int',
        'frame_rate': 'int',
        'width': 'int',
        'height': 'int',
        'black_cut': 'int',
        'stream_name': 'str'
    }

    attribute_map = {
        'output_policy': 'output_policy',
        'codec': 'codec',
        'crf': 'crf',
        'max_bitrate': 'max_bitrate',
        'bitrate': 'bitrate',
        'profile': 'profile',
        'level': 'level',
        'preset': 'preset',
        'max_iframes_interval': 'max_iframes_interval',
        'bframes_count': 'bframes_count',
        'frame_rate': 'frame_rate',
        'width': 'width',
        'height': 'height',
        'black_cut': 'black_cut',
        'stream_name': 'stream_name'
    }

    def __init__(self, output_policy=None, codec=None, crf=None, max_bitrate=None, bitrate=None, profile=None, level=None, preset=None, max_iframes_interval=None, bframes_count=None, frame_rate=None, width=None, height=None, black_cut=None, stream_name=None):
        r"""VideoParameters

        The model defined in huaweicloud sdk

        :param output_policy: 输出策略。  取值如下： - discard - transcode  &gt;- 当视频参数中的“output_policy”为\&quot;discard\&quot;，且音频参数中的“output_policy”为“transcode”时，表示只输出音频。 &gt;- 当视频参数中的“output_policy”为\&quot;transcode\&quot;，且音频参数中的“output_policy”为“discard”时，表示只输出视频。 &gt;- 同时为\&quot;discard\&quot;时不合法。 &gt;- 同时为“transcode”时，表示输出音视频。 
        :type output_policy: str
        :param codec: 视频编码格式。  取值如下： - 1：VIDEO_CODEC_H264 - 2：VIDEO_CODEC_H265 
        :type codec: int
        :param crf: 视频恒定码率控制因子。  取值范围为[0, 51] 
        :type crf: object
        :param max_bitrate: 输出最大码率  单位：kbit/s  带crf时使用，参考原片的平均码率进行设置（一般为1.5倍） 
        :type max_bitrate: int
        :param bitrate: 输出平均码率。  取值范围：0或[40,30000]之间的整数。  单位：kbit/s  若设置为0，则输出平均码率为自适应值。 
        :type bitrate: int
        :param profile: 编码档次  取值如下： - 1：VIDEO_PROFILE_H264_BASE - 2：VIDEO_PROFILE_H264_MAIN - 3：VIDEO_PROFILE_H264_HIGH - 4：VIDEO_PROFILE_H265_MAIN 
        :type profile: int
        :param level: 编码级别  取值如下： - 1：VIDEO_LEVEL_1_0 - 2：VIDEO_LEVEL_1_1 - 3：VIDEO_LEVEL_1_2 - 4：VIDEO_LEVEL_1_3 - 5：VIDEO_LEVEL_2_0 - 6：VIDEO_LEVEL_2_1 - 7：VIDEO_LEVEL_2_2 - 8：VIDEO_LEVEL_3_0 - 9：VIDEO_LEVEL_3_1 - 10：VIDEO_LEVEL_3_2 - 11：VIDEO_LEVEL_4_0 - 12：VIDEO_LEVEL_4_1 - 13：VIDEO_LEVEL_4_2 - 14：VIDEO_LEVEL_5_0 - 15：VIDEO_LEVEL_5_1 - 16：VIDEO_LEVEL_x_x 
        :type level: int
        :param preset: 编码质量等级  取值如下： - 1：VIDEO_PRESET_HSPEED2 (只用于h.265, h.265 default) - 2：VIDEO_PRESET_HSPEED (只用于h.265) - 3：VIDEO_PRESET_NORMAL (h264/h.265可用，h.264 default) 
        :type preset: int
        :param max_iframes_interval: I帧最大间隔  取值范围：[2，10]。  默认值：5。  单位：秒。 
        :type max_iframes_interval: int
        :param bframes_count: 最大B帧间隔。  取值范围： - H264：[0，7]，默认值为4。 - H265：[0，7]，默认值为7。  单位：帧。 
        :type bframes_count: int
        :param frame_rate: 帧率。  取值范围：0或[5,60]，0表示自适应。  单位：帧每秒。  &gt; 若设置的帧率不在取值范围内，则自动调整为0，若设置的帧率高于片源帧率，则自动调整为片源帧率。 
        :type frame_rate: int
        :param width: 视频宽度（单位：像素）  - H264：范围[32,4096]，必须为2的倍数 - H265：范围[320,4096]，必须是4的倍数 
        :type width: int
        :param height: 视频高度（单位：像素）  - H264：范围[32,2880]，必须为2的倍数 - H265：范围[240,2880] ，必须是4的倍数 
        :type height: int
        :param black_cut: 黑边剪裁类型  - 0：不开启黑边剪裁 - 1：开启黑边剪裁，低复杂度算法，针对长视频（&gt;5分钟） - 2：开启黑边剪裁，高复杂度算法，针对短视频（&lt;&#x3D;5分钟） 
        :type black_cut: int
        :param stream_name: 流名称 
        :type stream_name: str
        """
        
        

        self._output_policy = None
        self._codec = None
        self._crf = None
        self._max_bitrate = None
        self._bitrate = None
        self._profile = None
        self._level = None
        self._preset = None
        self._max_iframes_interval = None
        self._bframes_count = None
        self._frame_rate = None
        self._width = None
        self._height = None
        self._black_cut = None
        self._stream_name = None
        self.discriminator = None

        if output_policy is not None:
            self.output_policy = output_policy
        if codec is not None:
            self.codec = codec
        if crf is not None:
            self.crf = crf
        if max_bitrate is not None:
            self.max_bitrate = max_bitrate
        if bitrate is not None:
            self.bitrate = bitrate
        if profile is not None:
            self.profile = profile
        if level is not None:
            self.level = level
        if preset is not None:
            self.preset = preset
        if max_iframes_interval is not None:
            self.max_iframes_interval = max_iframes_interval
        if bframes_count is not None:
            self.bframes_count = bframes_count
        if frame_rate is not None:
            self.frame_rate = frame_rate
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if black_cut is not None:
            self.black_cut = black_cut
        if stream_name is not None:
            self.stream_name = stream_name

    @property
    def output_policy(self):
        r"""Gets the output_policy of this VideoParameters.

        输出策略。  取值如下： - discard - transcode  >- 当视频参数中的“output_policy”为\"discard\"，且音频参数中的“output_policy”为“transcode”时，表示只输出音频。 >- 当视频参数中的“output_policy”为\"transcode\"，且音频参数中的“output_policy”为“discard”时，表示只输出视频。 >- 同时为\"discard\"时不合法。 >- 同时为“transcode”时，表示输出音视频。 

        :return: The output_policy of this VideoParameters.
        :rtype: str
        """
        return self._output_policy

    @output_policy.setter
    def output_policy(self, output_policy):
        r"""Sets the output_policy of this VideoParameters.

        输出策略。  取值如下： - discard - transcode  >- 当视频参数中的“output_policy”为\"discard\"，且音频参数中的“output_policy”为“transcode”时，表示只输出音频。 >- 当视频参数中的“output_policy”为\"transcode\"，且音频参数中的“output_policy”为“discard”时，表示只输出视频。 >- 同时为\"discard\"时不合法。 >- 同时为“transcode”时，表示输出音视频。 

        :param output_policy: The output_policy of this VideoParameters.
        :type output_policy: str
        """
        self._output_policy = output_policy

    @property
    def codec(self):
        r"""Gets the codec of this VideoParameters.

        视频编码格式。  取值如下： - 1：VIDEO_CODEC_H264 - 2：VIDEO_CODEC_H265 

        :return: The codec of this VideoParameters.
        :rtype: int
        """
        return self._codec

    @codec.setter
    def codec(self, codec):
        r"""Sets the codec of this VideoParameters.

        视频编码格式。  取值如下： - 1：VIDEO_CODEC_H264 - 2：VIDEO_CODEC_H265 

        :param codec: The codec of this VideoParameters.
        :type codec: int
        """
        self._codec = codec

    @property
    def crf(self):
        r"""Gets the crf of this VideoParameters.

        视频恒定码率控制因子。  取值范围为[0, 51] 

        :return: The crf of this VideoParameters.
        :rtype: object
        """
        return self._crf

    @crf.setter
    def crf(self, crf):
        r"""Sets the crf of this VideoParameters.

        视频恒定码率控制因子。  取值范围为[0, 51] 

        :param crf: The crf of this VideoParameters.
        :type crf: object
        """
        self._crf = crf

    @property
    def max_bitrate(self):
        r"""Gets the max_bitrate of this VideoParameters.

        输出最大码率  单位：kbit/s  带crf时使用，参考原片的平均码率进行设置（一般为1.5倍） 

        :return: The max_bitrate of this VideoParameters.
        :rtype: int
        """
        return self._max_bitrate

    @max_bitrate.setter
    def max_bitrate(self, max_bitrate):
        r"""Sets the max_bitrate of this VideoParameters.

        输出最大码率  单位：kbit/s  带crf时使用，参考原片的平均码率进行设置（一般为1.5倍） 

        :param max_bitrate: The max_bitrate of this VideoParameters.
        :type max_bitrate: int
        """
        self._max_bitrate = max_bitrate

    @property
    def bitrate(self):
        r"""Gets the bitrate of this VideoParameters.

        输出平均码率。  取值范围：0或[40,30000]之间的整数。  单位：kbit/s  若设置为0，则输出平均码率为自适应值。 

        :return: The bitrate of this VideoParameters.
        :rtype: int
        """
        return self._bitrate

    @bitrate.setter
    def bitrate(self, bitrate):
        r"""Sets the bitrate of this VideoParameters.

        输出平均码率。  取值范围：0或[40,30000]之间的整数。  单位：kbit/s  若设置为0，则输出平均码率为自适应值。 

        :param bitrate: The bitrate of this VideoParameters.
        :type bitrate: int
        """
        self._bitrate = bitrate

    @property
    def profile(self):
        r"""Gets the profile of this VideoParameters.

        编码档次  取值如下： - 1：VIDEO_PROFILE_H264_BASE - 2：VIDEO_PROFILE_H264_MAIN - 3：VIDEO_PROFILE_H264_HIGH - 4：VIDEO_PROFILE_H265_MAIN 

        :return: The profile of this VideoParameters.
        :rtype: int
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        r"""Sets the profile of this VideoParameters.

        编码档次  取值如下： - 1：VIDEO_PROFILE_H264_BASE - 2：VIDEO_PROFILE_H264_MAIN - 3：VIDEO_PROFILE_H264_HIGH - 4：VIDEO_PROFILE_H265_MAIN 

        :param profile: The profile of this VideoParameters.
        :type profile: int
        """
        self._profile = profile

    @property
    def level(self):
        r"""Gets the level of this VideoParameters.

        编码级别  取值如下： - 1：VIDEO_LEVEL_1_0 - 2：VIDEO_LEVEL_1_1 - 3：VIDEO_LEVEL_1_2 - 4：VIDEO_LEVEL_1_3 - 5：VIDEO_LEVEL_2_0 - 6：VIDEO_LEVEL_2_1 - 7：VIDEO_LEVEL_2_2 - 8：VIDEO_LEVEL_3_0 - 9：VIDEO_LEVEL_3_1 - 10：VIDEO_LEVEL_3_2 - 11：VIDEO_LEVEL_4_0 - 12：VIDEO_LEVEL_4_1 - 13：VIDEO_LEVEL_4_2 - 14：VIDEO_LEVEL_5_0 - 15：VIDEO_LEVEL_5_1 - 16：VIDEO_LEVEL_x_x 

        :return: The level of this VideoParameters.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this VideoParameters.

        编码级别  取值如下： - 1：VIDEO_LEVEL_1_0 - 2：VIDEO_LEVEL_1_1 - 3：VIDEO_LEVEL_1_2 - 4：VIDEO_LEVEL_1_3 - 5：VIDEO_LEVEL_2_0 - 6：VIDEO_LEVEL_2_1 - 7：VIDEO_LEVEL_2_2 - 8：VIDEO_LEVEL_3_0 - 9：VIDEO_LEVEL_3_1 - 10：VIDEO_LEVEL_3_2 - 11：VIDEO_LEVEL_4_0 - 12：VIDEO_LEVEL_4_1 - 13：VIDEO_LEVEL_4_2 - 14：VIDEO_LEVEL_5_0 - 15：VIDEO_LEVEL_5_1 - 16：VIDEO_LEVEL_x_x 

        :param level: The level of this VideoParameters.
        :type level: int
        """
        self._level = level

    @property
    def preset(self):
        r"""Gets the preset of this VideoParameters.

        编码质量等级  取值如下： - 1：VIDEO_PRESET_HSPEED2 (只用于h.265, h.265 default) - 2：VIDEO_PRESET_HSPEED (只用于h.265) - 3：VIDEO_PRESET_NORMAL (h264/h.265可用，h.264 default) 

        :return: The preset of this VideoParameters.
        :rtype: int
        """
        return self._preset

    @preset.setter
    def preset(self, preset):
        r"""Sets the preset of this VideoParameters.

        编码质量等级  取值如下： - 1：VIDEO_PRESET_HSPEED2 (只用于h.265, h.265 default) - 2：VIDEO_PRESET_HSPEED (只用于h.265) - 3：VIDEO_PRESET_NORMAL (h264/h.265可用，h.264 default) 

        :param preset: The preset of this VideoParameters.
        :type preset: int
        """
        self._preset = preset

    @property
    def max_iframes_interval(self):
        r"""Gets the max_iframes_interval of this VideoParameters.

        I帧最大间隔  取值范围：[2，10]。  默认值：5。  单位：秒。 

        :return: The max_iframes_interval of this VideoParameters.
        :rtype: int
        """
        return self._max_iframes_interval

    @max_iframes_interval.setter
    def max_iframes_interval(self, max_iframes_interval):
        r"""Sets the max_iframes_interval of this VideoParameters.

        I帧最大间隔  取值范围：[2，10]。  默认值：5。  单位：秒。 

        :param max_iframes_interval: The max_iframes_interval of this VideoParameters.
        :type max_iframes_interval: int
        """
        self._max_iframes_interval = max_iframes_interval

    @property
    def bframes_count(self):
        r"""Gets the bframes_count of this VideoParameters.

        最大B帧间隔。  取值范围： - H264：[0，7]，默认值为4。 - H265：[0，7]，默认值为7。  单位：帧。 

        :return: The bframes_count of this VideoParameters.
        :rtype: int
        """
        return self._bframes_count

    @bframes_count.setter
    def bframes_count(self, bframes_count):
        r"""Sets the bframes_count of this VideoParameters.

        最大B帧间隔。  取值范围： - H264：[0，7]，默认值为4。 - H265：[0，7]，默认值为7。  单位：帧。 

        :param bframes_count: The bframes_count of this VideoParameters.
        :type bframes_count: int
        """
        self._bframes_count = bframes_count

    @property
    def frame_rate(self):
        r"""Gets the frame_rate of this VideoParameters.

        帧率。  取值范围：0或[5,60]，0表示自适应。  单位：帧每秒。  > 若设置的帧率不在取值范围内，则自动调整为0，若设置的帧率高于片源帧率，则自动调整为片源帧率。 

        :return: The frame_rate of this VideoParameters.
        :rtype: int
        """
        return self._frame_rate

    @frame_rate.setter
    def frame_rate(self, frame_rate):
        r"""Sets the frame_rate of this VideoParameters.

        帧率。  取值范围：0或[5,60]，0表示自适应。  单位：帧每秒。  > 若设置的帧率不在取值范围内，则自动调整为0，若设置的帧率高于片源帧率，则自动调整为片源帧率。 

        :param frame_rate: The frame_rate of this VideoParameters.
        :type frame_rate: int
        """
        self._frame_rate = frame_rate

    @property
    def width(self):
        r"""Gets the width of this VideoParameters.

        视频宽度（单位：像素）  - H264：范围[32,4096]，必须为2的倍数 - H265：范围[320,4096]，必须是4的倍数 

        :return: The width of this VideoParameters.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        r"""Sets the width of this VideoParameters.

        视频宽度（单位：像素）  - H264：范围[32,4096]，必须为2的倍数 - H265：范围[320,4096]，必须是4的倍数 

        :param width: The width of this VideoParameters.
        :type width: int
        """
        self._width = width

    @property
    def height(self):
        r"""Gets the height of this VideoParameters.

        视频高度（单位：像素）  - H264：范围[32,2880]，必须为2的倍数 - H265：范围[240,2880] ，必须是4的倍数 

        :return: The height of this VideoParameters.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        r"""Sets the height of this VideoParameters.

        视频高度（单位：像素）  - H264：范围[32,2880]，必须为2的倍数 - H265：范围[240,2880] ，必须是4的倍数 

        :param height: The height of this VideoParameters.
        :type height: int
        """
        self._height = height

    @property
    def black_cut(self):
        r"""Gets the black_cut of this VideoParameters.

        黑边剪裁类型  - 0：不开启黑边剪裁 - 1：开启黑边剪裁，低复杂度算法，针对长视频（>5分钟） - 2：开启黑边剪裁，高复杂度算法，针对短视频（<=5分钟） 

        :return: The black_cut of this VideoParameters.
        :rtype: int
        """
        return self._black_cut

    @black_cut.setter
    def black_cut(self, black_cut):
        r"""Sets the black_cut of this VideoParameters.

        黑边剪裁类型  - 0：不开启黑边剪裁 - 1：开启黑边剪裁，低复杂度算法，针对长视频（>5分钟） - 2：开启黑边剪裁，高复杂度算法，针对短视频（<=5分钟） 

        :param black_cut: The black_cut of this VideoParameters.
        :type black_cut: int
        """
        self._black_cut = black_cut

    @property
    def stream_name(self):
        r"""Gets the stream_name of this VideoParameters.

        流名称 

        :return: The stream_name of this VideoParameters.
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        r"""Sets the stream_name of this VideoParameters.

        流名称 

        :param stream_name: The stream_name of this VideoParameters.
        :type stream_name: str
        """
        self._stream_name = stream_name

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
        if not isinstance(other, VideoParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
