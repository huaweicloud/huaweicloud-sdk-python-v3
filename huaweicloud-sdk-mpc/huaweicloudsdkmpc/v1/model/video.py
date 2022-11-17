# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Video:

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
        'bitrate': 'int',
        'profile': 'int',
        'level': 'int',
        'preset': 'int',
        'ref_frames_count': 'int',
        'max_iframes_interval': 'int',
        'bframes_count': 'int',
        'frame_rate': 'int',
        'width': 'int',
        'height': 'int',
        'black_cut': 'int'
    }

    attribute_map = {
        'output_policy': 'output_policy',
        'codec': 'codec',
        'bitrate': 'bitrate',
        'profile': 'profile',
        'level': 'level',
        'preset': 'preset',
        'ref_frames_count': 'ref_frames_count',
        'max_iframes_interval': 'max_iframes_interval',
        'bframes_count': 'bframes_count',
        'frame_rate': 'frame_rate',
        'width': 'width',
        'height': 'height',
        'black_cut': 'black_cut'
    }

    def __init__(self, output_policy=None, codec=None, bitrate=None, profile=None, level=None, preset=None, ref_frames_count=None, max_iframes_interval=None, bframes_count=None, frame_rate=None, width=None, height=None, black_cut=None):
        """Video

        The model defined in huaweicloud sdk

        :param output_policy: 输出策略。  取值如下： - discard - transcode  &gt;- 当视频参数中的“output_policy”为\&quot;discard\&quot;，且音频参数中的“output_policy”为“transcode”时，表示只输出音频。 &gt;- 当视频参数中的“output_policy”为\&quot;transcode\&quot;，且音频参数中的“output_policy”为“discard”时，表示只输出视频。 &gt;- 同时为\&quot;discard\&quot;时不合法。 &gt;- 同时为“transcode”时，表示输出音视频。 
        :type output_policy: str
        :param codec: 视频编码格式。  取值如下：  - 1：表示H.264。 - 2：表示H.265。 
        :type codec: int
        :param bitrate: 输出平均码率。  取值范围：0或[40,30000]之间的整数。  单位：kbit/s  若设置为0，则输出平均码率为自适应值。 
        :type bitrate: int
        :param profile: 编码档次，建议设为3。  取值如下： - 1：VIDEO_PROFILE_H264_BASE - 2：VIDEO_PROFILE_H264_MAIN - 3：VIDEO_PROFILE_H264_HIGH - 4：VIDEO_PROFILE_H265_MAIN 
        :type profile: int
        :param level: 编码级别。  取值如下： - 1：VIDEO_LEVEL_1_0 - 2：VIDEO_LEVEL_1_1 - 3：VIDEO_LEVEL_1_2 - 4：VIDEO_LEVEL_1_3 - 5：VIDEO_LEVEL_2_0 - 6：VIDEO_LEVEL_2_1 - 7：VIDEO_LEVEL_2_2 - 8：VIDEO_LEVEL_3_0 - 9：VIDEO_LEVEL_3_1 - 10：VIDEO_LEVEL_3_2 - 11：VIDEO_LEVEL_4_0 - 12：VIDEO_LEVEL_4_1 - 13：VIDEO_LEVEL_4_2 - 14：VIDEO_LEVEL_5_0 - 15：VIDEO_LEVEL_5_1 
        :type level: int
        :param preset: 编码质量等级。  取值如下： - 1：VIDEO_PRESET_HSPEED2 - 2：VIDEO_PRESET_HSPEED - 3：VIDEO_PRESET_NORMAL &gt; 值越大，表示编码的质量越高，转码耗时也越长。 
        :type preset: int
        :param ref_frames_count: 最大参考帧数。  取值范围： - H264：[1，8] - H265：固定值4  单位：帧。 
        :type ref_frames_count: int
        :param max_iframes_interval: I帧最大间隔  取值范围：[2，10]。  默认值：5。  单位：秒。 
        :type max_iframes_interval: int
        :param bframes_count: 最大B帧间隔。  取值范围： - H264：[0，7]，默认值为4。 - H265：[0，7]，默认值为7。  单位：帧。 
        :type bframes_count: int
        :param frame_rate: 帧率。  取值范围：0或[5,60]之间的整数。  单位：帧每秒。  &gt; 若设置的帧率不在取值范围内，则自动调整为0，若设置的帧率高于片源帧率，则自动调整为片源帧率。 
        :type frame_rate: int
        :param width: 视频宽度。  取值范围： - H.264：0或[32,4096]间2的倍数。 - H.265：0或[160,4096]间4的倍数。  单位：像素。  说明：若视频宽度设置为0，则视频宽度值自适应。 
        :type width: int
        :param height: 视频高度。 - H.264：0或[32,2880]且必须为2的倍数。 - H.265：0或[96,2880]且必须为4的倍数。  单位：像素。  说明：若视频高度设置为0，则视频高度值自适应。 
        :type height: int
        :param black_cut: 黑边剪裁类型。  取值如下： - 0：不开启黑边剪裁。 - 1：开启黑边剪裁，低复杂度算法，针对长视频（&gt;5分钟）。 - 2：开启黑边剪裁，高复杂度算法，针对短视频（&lt;&#x3D;5分钟）。 
        :type black_cut: int
        """
        
        

        self._output_policy = None
        self._codec = None
        self._bitrate = None
        self._profile = None
        self._level = None
        self._preset = None
        self._ref_frames_count = None
        self._max_iframes_interval = None
        self._bframes_count = None
        self._frame_rate = None
        self._width = None
        self._height = None
        self._black_cut = None
        self.discriminator = None

        if output_policy is not None:
            self.output_policy = output_policy
        if codec is not None:
            self.codec = codec
        if bitrate is not None:
            self.bitrate = bitrate
        if profile is not None:
            self.profile = profile
        if level is not None:
            self.level = level
        if preset is not None:
            self.preset = preset
        if ref_frames_count is not None:
            self.ref_frames_count = ref_frames_count
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

    @property
    def output_policy(self):
        """Gets the output_policy of this Video.

        输出策略。  取值如下： - discard - transcode  >- 当视频参数中的“output_policy”为\"discard\"，且音频参数中的“output_policy”为“transcode”时，表示只输出音频。 >- 当视频参数中的“output_policy”为\"transcode\"，且音频参数中的“output_policy”为“discard”时，表示只输出视频。 >- 同时为\"discard\"时不合法。 >- 同时为“transcode”时，表示输出音视频。 

        :return: The output_policy of this Video.
        :rtype: str
        """
        return self._output_policy

    @output_policy.setter
    def output_policy(self, output_policy):
        """Sets the output_policy of this Video.

        输出策略。  取值如下： - discard - transcode  >- 当视频参数中的“output_policy”为\"discard\"，且音频参数中的“output_policy”为“transcode”时，表示只输出音频。 >- 当视频参数中的“output_policy”为\"transcode\"，且音频参数中的“output_policy”为“discard”时，表示只输出视频。 >- 同时为\"discard\"时不合法。 >- 同时为“transcode”时，表示输出音视频。 

        :param output_policy: The output_policy of this Video.
        :type output_policy: str
        """
        self._output_policy = output_policy

    @property
    def codec(self):
        """Gets the codec of this Video.

        视频编码格式。  取值如下：  - 1：表示H.264。 - 2：表示H.265。 

        :return: The codec of this Video.
        :rtype: int
        """
        return self._codec

    @codec.setter
    def codec(self, codec):
        """Sets the codec of this Video.

        视频编码格式。  取值如下：  - 1：表示H.264。 - 2：表示H.265。 

        :param codec: The codec of this Video.
        :type codec: int
        """
        self._codec = codec

    @property
    def bitrate(self):
        """Gets the bitrate of this Video.

        输出平均码率。  取值范围：0或[40,30000]之间的整数。  单位：kbit/s  若设置为0，则输出平均码率为自适应值。 

        :return: The bitrate of this Video.
        :rtype: int
        """
        return self._bitrate

    @bitrate.setter
    def bitrate(self, bitrate):
        """Sets the bitrate of this Video.

        输出平均码率。  取值范围：0或[40,30000]之间的整数。  单位：kbit/s  若设置为0，则输出平均码率为自适应值。 

        :param bitrate: The bitrate of this Video.
        :type bitrate: int
        """
        self._bitrate = bitrate

    @property
    def profile(self):
        """Gets the profile of this Video.

        编码档次，建议设为3。  取值如下： - 1：VIDEO_PROFILE_H264_BASE - 2：VIDEO_PROFILE_H264_MAIN - 3：VIDEO_PROFILE_H264_HIGH - 4：VIDEO_PROFILE_H265_MAIN 

        :return: The profile of this Video.
        :rtype: int
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """Sets the profile of this Video.

        编码档次，建议设为3。  取值如下： - 1：VIDEO_PROFILE_H264_BASE - 2：VIDEO_PROFILE_H264_MAIN - 3：VIDEO_PROFILE_H264_HIGH - 4：VIDEO_PROFILE_H265_MAIN 

        :param profile: The profile of this Video.
        :type profile: int
        """
        self._profile = profile

    @property
    def level(self):
        """Gets the level of this Video.

        编码级别。  取值如下： - 1：VIDEO_LEVEL_1_0 - 2：VIDEO_LEVEL_1_1 - 3：VIDEO_LEVEL_1_2 - 4：VIDEO_LEVEL_1_3 - 5：VIDEO_LEVEL_2_0 - 6：VIDEO_LEVEL_2_1 - 7：VIDEO_LEVEL_2_2 - 8：VIDEO_LEVEL_3_0 - 9：VIDEO_LEVEL_3_1 - 10：VIDEO_LEVEL_3_2 - 11：VIDEO_LEVEL_4_0 - 12：VIDEO_LEVEL_4_1 - 13：VIDEO_LEVEL_4_2 - 14：VIDEO_LEVEL_5_0 - 15：VIDEO_LEVEL_5_1 

        :return: The level of this Video.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this Video.

        编码级别。  取值如下： - 1：VIDEO_LEVEL_1_0 - 2：VIDEO_LEVEL_1_1 - 3：VIDEO_LEVEL_1_2 - 4：VIDEO_LEVEL_1_3 - 5：VIDEO_LEVEL_2_0 - 6：VIDEO_LEVEL_2_1 - 7：VIDEO_LEVEL_2_2 - 8：VIDEO_LEVEL_3_0 - 9：VIDEO_LEVEL_3_1 - 10：VIDEO_LEVEL_3_2 - 11：VIDEO_LEVEL_4_0 - 12：VIDEO_LEVEL_4_1 - 13：VIDEO_LEVEL_4_2 - 14：VIDEO_LEVEL_5_0 - 15：VIDEO_LEVEL_5_1 

        :param level: The level of this Video.
        :type level: int
        """
        self._level = level

    @property
    def preset(self):
        """Gets the preset of this Video.

        编码质量等级。  取值如下： - 1：VIDEO_PRESET_HSPEED2 - 2：VIDEO_PRESET_HSPEED - 3：VIDEO_PRESET_NORMAL > 值越大，表示编码的质量越高，转码耗时也越长。 

        :return: The preset of this Video.
        :rtype: int
        """
        return self._preset

    @preset.setter
    def preset(self, preset):
        """Sets the preset of this Video.

        编码质量等级。  取值如下： - 1：VIDEO_PRESET_HSPEED2 - 2：VIDEO_PRESET_HSPEED - 3：VIDEO_PRESET_NORMAL > 值越大，表示编码的质量越高，转码耗时也越长。 

        :param preset: The preset of this Video.
        :type preset: int
        """
        self._preset = preset

    @property
    def ref_frames_count(self):
        """Gets the ref_frames_count of this Video.

        最大参考帧数。  取值范围： - H264：[1，8] - H265：固定值4  单位：帧。 

        :return: The ref_frames_count of this Video.
        :rtype: int
        """
        return self._ref_frames_count

    @ref_frames_count.setter
    def ref_frames_count(self, ref_frames_count):
        """Sets the ref_frames_count of this Video.

        最大参考帧数。  取值范围： - H264：[1，8] - H265：固定值4  单位：帧。 

        :param ref_frames_count: The ref_frames_count of this Video.
        :type ref_frames_count: int
        """
        self._ref_frames_count = ref_frames_count

    @property
    def max_iframes_interval(self):
        """Gets the max_iframes_interval of this Video.

        I帧最大间隔  取值范围：[2，10]。  默认值：5。  单位：秒。 

        :return: The max_iframes_interval of this Video.
        :rtype: int
        """
        return self._max_iframes_interval

    @max_iframes_interval.setter
    def max_iframes_interval(self, max_iframes_interval):
        """Sets the max_iframes_interval of this Video.

        I帧最大间隔  取值范围：[2，10]。  默认值：5。  单位：秒。 

        :param max_iframes_interval: The max_iframes_interval of this Video.
        :type max_iframes_interval: int
        """
        self._max_iframes_interval = max_iframes_interval

    @property
    def bframes_count(self):
        """Gets the bframes_count of this Video.

        最大B帧间隔。  取值范围： - H264：[0，7]，默认值为4。 - H265：[0，7]，默认值为7。  单位：帧。 

        :return: The bframes_count of this Video.
        :rtype: int
        """
        return self._bframes_count

    @bframes_count.setter
    def bframes_count(self, bframes_count):
        """Sets the bframes_count of this Video.

        最大B帧间隔。  取值范围： - H264：[0，7]，默认值为4。 - H265：[0，7]，默认值为7。  单位：帧。 

        :param bframes_count: The bframes_count of this Video.
        :type bframes_count: int
        """
        self._bframes_count = bframes_count

    @property
    def frame_rate(self):
        """Gets the frame_rate of this Video.

        帧率。  取值范围：0或[5,60]之间的整数。  单位：帧每秒。  > 若设置的帧率不在取值范围内，则自动调整为0，若设置的帧率高于片源帧率，则自动调整为片源帧率。 

        :return: The frame_rate of this Video.
        :rtype: int
        """
        return self._frame_rate

    @frame_rate.setter
    def frame_rate(self, frame_rate):
        """Sets the frame_rate of this Video.

        帧率。  取值范围：0或[5,60]之间的整数。  单位：帧每秒。  > 若设置的帧率不在取值范围内，则自动调整为0，若设置的帧率高于片源帧率，则自动调整为片源帧率。 

        :param frame_rate: The frame_rate of this Video.
        :type frame_rate: int
        """
        self._frame_rate = frame_rate

    @property
    def width(self):
        """Gets the width of this Video.

        视频宽度。  取值范围： - H.264：0或[32,4096]间2的倍数。 - H.265：0或[160,4096]间4的倍数。  单位：像素。  说明：若视频宽度设置为0，则视频宽度值自适应。 

        :return: The width of this Video.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this Video.

        视频宽度。  取值范围： - H.264：0或[32,4096]间2的倍数。 - H.265：0或[160,4096]间4的倍数。  单位：像素。  说明：若视频宽度设置为0，则视频宽度值自适应。 

        :param width: The width of this Video.
        :type width: int
        """
        self._width = width

    @property
    def height(self):
        """Gets the height of this Video.

        视频高度。 - H.264：0或[32,2880]且必须为2的倍数。 - H.265：0或[96,2880]且必须为4的倍数。  单位：像素。  说明：若视频高度设置为0，则视频高度值自适应。 

        :return: The height of this Video.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this Video.

        视频高度。 - H.264：0或[32,2880]且必须为2的倍数。 - H.265：0或[96,2880]且必须为4的倍数。  单位：像素。  说明：若视频高度设置为0，则视频高度值自适应。 

        :param height: The height of this Video.
        :type height: int
        """
        self._height = height

    @property
    def black_cut(self):
        """Gets the black_cut of this Video.

        黑边剪裁类型。  取值如下： - 0：不开启黑边剪裁。 - 1：开启黑边剪裁，低复杂度算法，针对长视频（>5分钟）。 - 2：开启黑边剪裁，高复杂度算法，针对短视频（<=5分钟）。 

        :return: The black_cut of this Video.
        :rtype: int
        """
        return self._black_cut

    @black_cut.setter
    def black_cut(self, black_cut):
        """Sets the black_cut of this Video.

        黑边剪裁类型。  取值如下： - 0：不开启黑边剪裁。 - 1：开启黑边剪裁，低复杂度算法，针对长视频（>5分钟）。 - 2：开启黑边剪裁，高复杂度算法，针对短视频（<=5分钟）。 

        :param black_cut: The black_cut of this Video.
        :type black_cut: int
        """
        self._black_cut = black_cut

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
        if not isinstance(other, Video):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
