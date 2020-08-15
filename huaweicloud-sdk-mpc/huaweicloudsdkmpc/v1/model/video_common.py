# coding: utf-8

import pprint
import re

import six





class VideoCommon:


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
        'profile': 'int',
        'level': 'int',
        'preset': 'int',
        'ref_frames_count': 'int',
        'max_iframes_interval': 'int',
        'bframes_count': 'int',
        'frame_rate': 'int',
        'sync_timestamp': 'bool',
        'aspect_ratio': 'int',
        'black_cut': 'int',
        'gop_structure': 'bool',
        'sr_factor': 'str'
    }

    attribute_map = {
        'output_policy': 'output_policy',
        'codec': 'codec',
        'profile': 'profile',
        'level': 'level',
        'preset': 'preset',
        'ref_frames_count': 'ref_frames_count',
        'max_iframes_interval': 'max_iframes_interval',
        'bframes_count': 'bframes_count',
        'frame_rate': 'frame_rate',
        'sync_timestamp': 'sync_timestamp',
        'aspect_ratio': 'aspect_ratio',
        'black_cut': 'black_cut',
        'gop_structure': 'GOP_structure',
        'sr_factor': 'sr_factor'
    }

    def __init__(self, output_policy='transcode', codec=None, profile=None, level=15, preset=None, ref_frames_count=4, max_iframes_interval=5, bframes_count=None, frame_rate=None, sync_timestamp=False, aspect_ratio=None, black_cut=None, gop_structure=False, sr_factor=None):
        """VideoCommon - a model defined in huaweicloud sdk"""
        
        

        self._output_policy = None
        self._codec = None
        self._profile = None
        self._level = None
        self._preset = None
        self._ref_frames_count = None
        self._max_iframes_interval = None
        self._bframes_count = None
        self._frame_rate = None
        self._sync_timestamp = None
        self._aspect_ratio = None
        self._black_cut = None
        self._gop_structure = None
        self._sr_factor = None
        self.discriminator = None

        if output_policy is not None:
            self.output_policy = output_policy
        if codec is not None:
            self.codec = codec
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
        if sync_timestamp is not None:
            self.sync_timestamp = sync_timestamp
        if aspect_ratio is not None:
            self.aspect_ratio = aspect_ratio
        if black_cut is not None:
            self.black_cut = black_cut
        if gop_structure is not None:
            self.gop_structure = gop_structure
        if sr_factor is not None:
            self.sr_factor = sr_factor

    @property
    def output_policy(self):
        """Gets the output_policy of this VideoCommon.

        输出策略。  取值如下： - discard - transcode  >- 当视频参数中的“output_policy”为\"discard\"，且音频参数中的“output_policy”为“transcode”时，表示只输出音频。 >- 当视频参数中的“output_policy”为\"transcode\"，且音频参数中的“output_policy”为“discard”时，表示只输出视频。 >- 同时为\"discard\"时不合法。 >- 同时为“transcode”时，表示输出音视频。 

        :return: The output_policy of this VideoCommon.
        :rtype: str
        """
        return self._output_policy

    @output_policy.setter
    def output_policy(self, output_policy):
        """Sets the output_policy of this VideoCommon.

        输出策略。  取值如下： - discard - transcode  >- 当视频参数中的“output_policy”为\"discard\"，且音频参数中的“output_policy”为“transcode”时，表示只输出音频。 >- 当视频参数中的“output_policy”为\"transcode\"，且音频参数中的“output_policy”为“discard”时，表示只输出视频。 >- 同时为\"discard\"时不合法。 >- 同时为“transcode”时，表示输出音视频。 

        :param output_policy: The output_policy of this VideoCommon.
        :type: str
        """
        self._output_policy = output_policy

    @property
    def codec(self):
        """Gets the codec of this VideoCommon.

        视频编码格式。  取值如下： - 1：表示H.264。 - 2：表示H.265。 

        :return: The codec of this VideoCommon.
        :rtype: int
        """
        return self._codec

    @codec.setter
    def codec(self, codec):
        """Sets the codec of this VideoCommon.

        视频编码格式。  取值如下： - 1：表示H.264。 - 2：表示H.265。 

        :param codec: The codec of this VideoCommon.
        :type: int
        """
        self._codec = codec

    @property
    def profile(self):
        """Gets the profile of this VideoCommon.

        编码档次，建议设为3。  取值如下： - 1：VIDEO_PROFILE_H264_BASE - 2：VIDEO_PROFILE_H264_MAIN - 3：VIDEO_PROFILE_H264_HIGH - 4：VIDEO_PROFILE_H265_MAIN 

        :return: The profile of this VideoCommon.
        :rtype: int
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """Sets the profile of this VideoCommon.

        编码档次，建议设为3。  取值如下： - 1：VIDEO_PROFILE_H264_BASE - 2：VIDEO_PROFILE_H264_MAIN - 3：VIDEO_PROFILE_H264_HIGH - 4：VIDEO_PROFILE_H265_MAIN 

        :param profile: The profile of this VideoCommon.
        :type: int
        """
        self._profile = profile

    @property
    def level(self):
        """Gets the level of this VideoCommon.

        编码级别。  取值如下： - 1：VIDEO_LEVEL_1_0 - 2：VIDEO_LEVEL_1_1 - 3：VIDEO_LEVEL_1_2 - 4：VIDEO_LEVEL_1_3 - 5：VIDEO_LEVEL_2_0 - 6：VIDEO_LEVEL_2_1 - 7：VIDEO_LEVEL_2_2 - 8：VIDEO_LEVEL_3_0 - 9：VIDEO_LEVEL_3_1 - 10：VIDEO_LEVEL_3_2 - 11：VIDEO_LEVEL_4_0 - 12：VIDEO_LEVEL_4_1 - 13：VIDEO_LEVEL_4_2 - 14：VIDEO_LEVEL_5_0 - 15：VIDEO_LEVEL_5_1 

        :return: The level of this VideoCommon.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this VideoCommon.

        编码级别。  取值如下： - 1：VIDEO_LEVEL_1_0 - 2：VIDEO_LEVEL_1_1 - 3：VIDEO_LEVEL_1_2 - 4：VIDEO_LEVEL_1_3 - 5：VIDEO_LEVEL_2_0 - 6：VIDEO_LEVEL_2_1 - 7：VIDEO_LEVEL_2_2 - 8：VIDEO_LEVEL_3_0 - 9：VIDEO_LEVEL_3_1 - 10：VIDEO_LEVEL_3_2 - 11：VIDEO_LEVEL_4_0 - 12：VIDEO_LEVEL_4_1 - 13：VIDEO_LEVEL_4_2 - 14：VIDEO_LEVEL_5_0 - 15：VIDEO_LEVEL_5_1 

        :param level: The level of this VideoCommon.
        :type: int
        """
        self._level = level

    @property
    def preset(self):
        """Gets the preset of this VideoCommon.

        编码质量等级。  取值如下： - 1：VIDEO_PRESET_HSPEED2 - 2：VIDEO_PRESET_HSPEED - 3：VIDEO_PRESET_NORMAL > 值越大，表示编码的质量越高，转码耗时也越长。 

        :return: The preset of this VideoCommon.
        :rtype: int
        """
        return self._preset

    @preset.setter
    def preset(self, preset):
        """Sets the preset of this VideoCommon.

        编码质量等级。  取值如下： - 1：VIDEO_PRESET_HSPEED2 - 2：VIDEO_PRESET_HSPEED - 3：VIDEO_PRESET_NORMAL > 值越大，表示编码的质量越高，转码耗时也越长。 

        :param preset: The preset of this VideoCommon.
        :type: int
        """
        self._preset = preset

    @property
    def ref_frames_count(self):
        """Gets the ref_frames_count of this VideoCommon.

        最大参考帧数。  取值范围： - H264：[1，8]，默认值为4 。 - H265：固定值4。  单位：帧。 

        :return: The ref_frames_count of this VideoCommon.
        :rtype: int
        """
        return self._ref_frames_count

    @ref_frames_count.setter
    def ref_frames_count(self, ref_frames_count):
        """Sets the ref_frames_count of this VideoCommon.

        最大参考帧数。  取值范围： - H264：[1，8]，默认值为4 。 - H265：固定值4。  单位：帧。 

        :param ref_frames_count: The ref_frames_count of this VideoCommon.
        :type: int
        """
        self._ref_frames_count = ref_frames_count

    @property
    def max_iframes_interval(self):
        """Gets the max_iframes_interval of this VideoCommon.

        I帧最大间隔  取值范围：[2，10]。  默认值：5。  单位：秒。 

        :return: The max_iframes_interval of this VideoCommon.
        :rtype: int
        """
        return self._max_iframes_interval

    @max_iframes_interval.setter
    def max_iframes_interval(self, max_iframes_interval):
        """Sets the max_iframes_interval of this VideoCommon.

        I帧最大间隔  取值范围：[2，10]。  默认值：5。  单位：秒。 

        :param max_iframes_interval: The max_iframes_interval of this VideoCommon.
        :type: int
        """
        self._max_iframes_interval = max_iframes_interval

    @property
    def bframes_count(self):
        """Gets the bframes_count of this VideoCommon.

        最大B帧间隔。  取值范围： - H264：[0，7]，默认值为4。 - H265：[0，7]，默认值为7。  单位：帧。 

        :return: The bframes_count of this VideoCommon.
        :rtype: int
        """
        return self._bframes_count

    @bframes_count.setter
    def bframes_count(self, bframes_count):
        """Sets the bframes_count of this VideoCommon.

        最大B帧间隔。  取值范围： - H264：[0，7]，默认值为4。 - H265：[0，7]，默认值为7。  单位：帧。 

        :param bframes_count: The bframes_count of this VideoCommon.
        :type: int
        """
        self._bframes_count = bframes_count

    @property
    def frame_rate(self):
        """Gets the frame_rate of this VideoCommon.

        帧率  取值范围：0或[5,60]之间的整数，0表示自适应  单位：帧每秒 

        :return: The frame_rate of this VideoCommon.
        :rtype: int
        """
        return self._frame_rate

    @frame_rate.setter
    def frame_rate(self, frame_rate):
        """Sets the frame_rate of this VideoCommon.

        帧率  取值范围：0或[5,60]之间的整数，0表示自适应  单位：帧每秒 

        :param frame_rate: The frame_rate of this VideoCommon.
        :type: int
        """
        self._frame_rate = frame_rate

    @property
    def sync_timestamp(self):
        """Gets the sync_timestamp of this VideoCommon.

        降帧率时是否同步调整时间戳 在配置降帧率场景下有效。 取值如下： - false：不调整时间戳； - true：根据 frame_rate 配置的帧率，重新计算时间戳。 

        :return: The sync_timestamp of this VideoCommon.
        :rtype: bool
        """
        return self._sync_timestamp

    @sync_timestamp.setter
    def sync_timestamp(self, sync_timestamp):
        """Sets the sync_timestamp of this VideoCommon.

        降帧率时是否同步调整时间戳 在配置降帧率场景下有效。 取值如下： - false：不调整时间戳； - true：根据 frame_rate 配置的帧率，重新计算时间戳。 

        :param sync_timestamp: The sync_timestamp of this VideoCommon.
        :type: bool
        """
        self._sync_timestamp = sync_timestamp

    @property
    def aspect_ratio(self):
        """Gets the aspect_ratio of this VideoCommon.

        纵横比，图像缩放方式 

        :return: The aspect_ratio of this VideoCommon.
        :rtype: int
        """
        return self._aspect_ratio

    @aspect_ratio.setter
    def aspect_ratio(self, aspect_ratio):
        """Sets the aspect_ratio of this VideoCommon.

        纵横比，图像缩放方式 

        :param aspect_ratio: The aspect_ratio of this VideoCommon.
        :type: int
        """
        self._aspect_ratio = aspect_ratio

    @property
    def black_cut(self):
        """Gets the black_cut of this VideoCommon.

        黑边剪裁类型  取值如下： - 0：不开启黑边剪裁 - 1：开启黑边剪裁，低复杂度算法，针对长视频（>5分钟） - 2：开启黑边剪裁，高复杂度算法，针对短视频（<=5分钟） 

        :return: The black_cut of this VideoCommon.
        :rtype: int
        """
        return self._black_cut

    @black_cut.setter
    def black_cut(self, black_cut):
        """Sets the black_cut of this VideoCommon.

        黑边剪裁类型  取值如下： - 0：不开启黑边剪裁 - 1：开启黑边剪裁，低复杂度算法，针对长视频（>5分钟） - 2：开启黑边剪裁，高复杂度算法，针对短视频（<=5分钟） 

        :param black_cut: The black_cut of this VideoCommon.
        :type: int
        """
        self._black_cut = black_cut

    @property
    def gop_structure(self):
        """Gets the gop_structure of this VideoCommon.

        GOP类型（暂不开放） 0: Closed (Default) 1:Open 

        :return: The gop_structure of this VideoCommon.
        :rtype: bool
        """
        return self._gop_structure

    @gop_structure.setter
    def gop_structure(self, gop_structure):
        """Sets the gop_structure of this VideoCommon.

        GOP类型（暂不开放） 0: Closed (Default) 1:Open 

        :param gop_structure: The gop_structure of this VideoCommon.
        :type: bool
        """
        self._gop_structure = gop_structure

    @property
    def sr_factor(self):
        """Gets the sr_factor of this VideoCommon.

        超分倍数  取值如下： - 2：两倍超分 

        :return: The sr_factor of this VideoCommon.
        :rtype: str
        """
        return self._sr_factor

    @sr_factor.setter
    def sr_factor(self, sr_factor):
        """Sets the sr_factor of this VideoCommon.

        超分倍数  取值如下： - 2：两倍超分 

        :param sr_factor: The sr_factor of this VideoCommon.
        :type: str
        """
        self._sr_factor = sr_factor

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, VideoCommon):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
