# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DisplayOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'display_bandwidth': 'int',
        'frame_rate': 'int',
        'video_frame_rate': 'int',
        'min_image_cache': 'int',
        'smoothing_factor': 'int',
        'lossless_compression_mode': 'str',
        'deep_compression_options': 'DisplayOptionsDeepCompressionOptions',
        'lossy_compression_quality': 'int',
        'color_enhancement_enable': 'bool',
        'quality_bandwidth_first': 'str',
        'video_bit_rate_options': 'DisplayOptionsVideoBitRateOptions',
        'peak_video_bit_rate': 'int',
        'video_quality_options': 'DisplayOptionsVideoQualityOptions',
        'gop_size': 'int',
        'encoding_preset': 'str'
    }

    attribute_map = {
        'display_bandwidth': 'display_bandwidth',
        'frame_rate': 'frame_rate',
        'video_frame_rate': 'video_frame_rate',
        'min_image_cache': 'min_image_cache',
        'smoothing_factor': 'smoothing_factor',
        'lossless_compression_mode': 'lossless_compression_mode',
        'deep_compression_options': 'deep_compression_options',
        'lossy_compression_quality': 'lossy_compression_quality',
        'color_enhancement_enable': 'color_enhancement_enable',
        'quality_bandwidth_first': 'quality_bandwidth_first',
        'video_bit_rate_options': 'video_bit_rate_options',
        'peak_video_bit_rate': 'peak_video_bit_rate',
        'video_quality_options': 'video_quality_options',
        'gop_size': 'gop_size',
        'encoding_preset': 'encoding_preset'
    }

    def __init__(self, display_bandwidth=None, frame_rate=None, video_frame_rate=None, min_image_cache=None, smoothing_factor=None, lossless_compression_mode=None, deep_compression_options=None, lossy_compression_quality=None, color_enhancement_enable=None, quality_bandwidth_first=None, video_bit_rate_options=None, peak_video_bit_rate=None, video_quality_options=None, gop_size=None, encoding_preset=None):
        """DisplayOptions

        The model defined in huaweicloud sdk

        :param display_bandwidth: 带宽（Kbps）。取值范围为[256-25000]。默认：20000。
        :type display_bandwidth: int
        :param frame_rate: 帧率（fps）。取值范围为[1-60]。默认：25。
        :type frame_rate: int
        :param video_frame_rate: 视频帧率（fps）。取值范围为[1-60]。默认：30。
        :type video_frame_rate: int
        :param min_image_cache: 图像缓存最低容量（MB）。取值范围[0-300]，默认：200。
        :type min_image_cache: int
        :param smoothing_factor: 有损压缩识别阈值。取值范围为[0-255]。默认：60。
        :type smoothing_factor: int
        :param lossless_compression_mode: 无损压缩模式。取值为： Basic Compression：表示初级压缩。 Deep Compression：表示深度压缩。
        :type lossless_compression_mode: str
        :param deep_compression_options: 
        :type deep_compression_options: :class:`huaweicloudsdkworkspaceapp.v1.DisplayOptionsDeepCompressionOptions`
        :param lossy_compression_quality: 有损压缩质量。取值范围为[20-100]。默认：85。
        :type lossy_compression_quality: int
        :param color_enhancement_enable: 办公场景色彩增强：取值为： false：表示关闭。 true：表示开启。
        :type color_enhancement_enable: bool
        :param quality_bandwidth_first: 质量或带宽优先。取值为： Quality First：表示初级压缩。 Bandwidth First：表示深度压缩。
        :type quality_bandwidth_first: str
        :param video_bit_rate_options: 
        :type video_bit_rate_options: :class:`huaweicloudsdkworkspaceapp.v1.DisplayOptionsVideoBitRateOptions`
        :param peak_video_bit_rate: 视频峰值码率（Kbps）。取值范围为[256-100000]。默认：18000。
        :type peak_video_bit_rate: int
        :param video_quality_options: 
        :type video_quality_options: :class:`huaweicloudsdkworkspaceapp.v1.DisplayOptionsVideoQualityOptions`
        :param gop_size: GOP大小。取值范围为[0-65535]。默认：100。
        :type gop_size: int
        :param encoding_preset: 编码预置。取值为： 预置1：Preset 1。 预置2：Preset 2。 预置3：Preset 3。 预置4：Preset 4。 预置5：Preset 5。 预置6：Preset 6。 预置7：Preset 7。
        :type encoding_preset: str
        """
        
        

        self._display_bandwidth = None
        self._frame_rate = None
        self._video_frame_rate = None
        self._min_image_cache = None
        self._smoothing_factor = None
        self._lossless_compression_mode = None
        self._deep_compression_options = None
        self._lossy_compression_quality = None
        self._color_enhancement_enable = None
        self._quality_bandwidth_first = None
        self._video_bit_rate_options = None
        self._peak_video_bit_rate = None
        self._video_quality_options = None
        self._gop_size = None
        self._encoding_preset = None
        self.discriminator = None

        if display_bandwidth is not None:
            self.display_bandwidth = display_bandwidth
        if frame_rate is not None:
            self.frame_rate = frame_rate
        if video_frame_rate is not None:
            self.video_frame_rate = video_frame_rate
        if min_image_cache is not None:
            self.min_image_cache = min_image_cache
        if smoothing_factor is not None:
            self.smoothing_factor = smoothing_factor
        if lossless_compression_mode is not None:
            self.lossless_compression_mode = lossless_compression_mode
        if deep_compression_options is not None:
            self.deep_compression_options = deep_compression_options
        if lossy_compression_quality is not None:
            self.lossy_compression_quality = lossy_compression_quality
        if color_enhancement_enable is not None:
            self.color_enhancement_enable = color_enhancement_enable
        if quality_bandwidth_first is not None:
            self.quality_bandwidth_first = quality_bandwidth_first
        if video_bit_rate_options is not None:
            self.video_bit_rate_options = video_bit_rate_options
        if peak_video_bit_rate is not None:
            self.peak_video_bit_rate = peak_video_bit_rate
        if video_quality_options is not None:
            self.video_quality_options = video_quality_options
        if gop_size is not None:
            self.gop_size = gop_size
        if encoding_preset is not None:
            self.encoding_preset = encoding_preset

    @property
    def display_bandwidth(self):
        """Gets the display_bandwidth of this DisplayOptions.

        带宽（Kbps）。取值范围为[256-25000]。默认：20000。

        :return: The display_bandwidth of this DisplayOptions.
        :rtype: int
        """
        return self._display_bandwidth

    @display_bandwidth.setter
    def display_bandwidth(self, display_bandwidth):
        """Sets the display_bandwidth of this DisplayOptions.

        带宽（Kbps）。取值范围为[256-25000]。默认：20000。

        :param display_bandwidth: The display_bandwidth of this DisplayOptions.
        :type display_bandwidth: int
        """
        self._display_bandwidth = display_bandwidth

    @property
    def frame_rate(self):
        """Gets the frame_rate of this DisplayOptions.

        帧率（fps）。取值范围为[1-60]。默认：25。

        :return: The frame_rate of this DisplayOptions.
        :rtype: int
        """
        return self._frame_rate

    @frame_rate.setter
    def frame_rate(self, frame_rate):
        """Sets the frame_rate of this DisplayOptions.

        帧率（fps）。取值范围为[1-60]。默认：25。

        :param frame_rate: The frame_rate of this DisplayOptions.
        :type frame_rate: int
        """
        self._frame_rate = frame_rate

    @property
    def video_frame_rate(self):
        """Gets the video_frame_rate of this DisplayOptions.

        视频帧率（fps）。取值范围为[1-60]。默认：30。

        :return: The video_frame_rate of this DisplayOptions.
        :rtype: int
        """
        return self._video_frame_rate

    @video_frame_rate.setter
    def video_frame_rate(self, video_frame_rate):
        """Sets the video_frame_rate of this DisplayOptions.

        视频帧率（fps）。取值范围为[1-60]。默认：30。

        :param video_frame_rate: The video_frame_rate of this DisplayOptions.
        :type video_frame_rate: int
        """
        self._video_frame_rate = video_frame_rate

    @property
    def min_image_cache(self):
        """Gets the min_image_cache of this DisplayOptions.

        图像缓存最低容量（MB）。取值范围[0-300]，默认：200。

        :return: The min_image_cache of this DisplayOptions.
        :rtype: int
        """
        return self._min_image_cache

    @min_image_cache.setter
    def min_image_cache(self, min_image_cache):
        """Sets the min_image_cache of this DisplayOptions.

        图像缓存最低容量（MB）。取值范围[0-300]，默认：200。

        :param min_image_cache: The min_image_cache of this DisplayOptions.
        :type min_image_cache: int
        """
        self._min_image_cache = min_image_cache

    @property
    def smoothing_factor(self):
        """Gets the smoothing_factor of this DisplayOptions.

        有损压缩识别阈值。取值范围为[0-255]。默认：60。

        :return: The smoothing_factor of this DisplayOptions.
        :rtype: int
        """
        return self._smoothing_factor

    @smoothing_factor.setter
    def smoothing_factor(self, smoothing_factor):
        """Sets the smoothing_factor of this DisplayOptions.

        有损压缩识别阈值。取值范围为[0-255]。默认：60。

        :param smoothing_factor: The smoothing_factor of this DisplayOptions.
        :type smoothing_factor: int
        """
        self._smoothing_factor = smoothing_factor

    @property
    def lossless_compression_mode(self):
        """Gets the lossless_compression_mode of this DisplayOptions.

        无损压缩模式。取值为： Basic Compression：表示初级压缩。 Deep Compression：表示深度压缩。

        :return: The lossless_compression_mode of this DisplayOptions.
        :rtype: str
        """
        return self._lossless_compression_mode

    @lossless_compression_mode.setter
    def lossless_compression_mode(self, lossless_compression_mode):
        """Sets the lossless_compression_mode of this DisplayOptions.

        无损压缩模式。取值为： Basic Compression：表示初级压缩。 Deep Compression：表示深度压缩。

        :param lossless_compression_mode: The lossless_compression_mode of this DisplayOptions.
        :type lossless_compression_mode: str
        """
        self._lossless_compression_mode = lossless_compression_mode

    @property
    def deep_compression_options(self):
        """Gets the deep_compression_options of this DisplayOptions.

        :return: The deep_compression_options of this DisplayOptions.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.DisplayOptionsDeepCompressionOptions`
        """
        return self._deep_compression_options

    @deep_compression_options.setter
    def deep_compression_options(self, deep_compression_options):
        """Sets the deep_compression_options of this DisplayOptions.

        :param deep_compression_options: The deep_compression_options of this DisplayOptions.
        :type deep_compression_options: :class:`huaweicloudsdkworkspaceapp.v1.DisplayOptionsDeepCompressionOptions`
        """
        self._deep_compression_options = deep_compression_options

    @property
    def lossy_compression_quality(self):
        """Gets the lossy_compression_quality of this DisplayOptions.

        有损压缩质量。取值范围为[20-100]。默认：85。

        :return: The lossy_compression_quality of this DisplayOptions.
        :rtype: int
        """
        return self._lossy_compression_quality

    @lossy_compression_quality.setter
    def lossy_compression_quality(self, lossy_compression_quality):
        """Sets the lossy_compression_quality of this DisplayOptions.

        有损压缩质量。取值范围为[20-100]。默认：85。

        :param lossy_compression_quality: The lossy_compression_quality of this DisplayOptions.
        :type lossy_compression_quality: int
        """
        self._lossy_compression_quality = lossy_compression_quality

    @property
    def color_enhancement_enable(self):
        """Gets the color_enhancement_enable of this DisplayOptions.

        办公场景色彩增强：取值为： false：表示关闭。 true：表示开启。

        :return: The color_enhancement_enable of this DisplayOptions.
        :rtype: bool
        """
        return self._color_enhancement_enable

    @color_enhancement_enable.setter
    def color_enhancement_enable(self, color_enhancement_enable):
        """Sets the color_enhancement_enable of this DisplayOptions.

        办公场景色彩增强：取值为： false：表示关闭。 true：表示开启。

        :param color_enhancement_enable: The color_enhancement_enable of this DisplayOptions.
        :type color_enhancement_enable: bool
        """
        self._color_enhancement_enable = color_enhancement_enable

    @property
    def quality_bandwidth_first(self):
        """Gets the quality_bandwidth_first of this DisplayOptions.

        质量或带宽优先。取值为： Quality First：表示初级压缩。 Bandwidth First：表示深度压缩。

        :return: The quality_bandwidth_first of this DisplayOptions.
        :rtype: str
        """
        return self._quality_bandwidth_first

    @quality_bandwidth_first.setter
    def quality_bandwidth_first(self, quality_bandwidth_first):
        """Sets the quality_bandwidth_first of this DisplayOptions.

        质量或带宽优先。取值为： Quality First：表示初级压缩。 Bandwidth First：表示深度压缩。

        :param quality_bandwidth_first: The quality_bandwidth_first of this DisplayOptions.
        :type quality_bandwidth_first: str
        """
        self._quality_bandwidth_first = quality_bandwidth_first

    @property
    def video_bit_rate_options(self):
        """Gets the video_bit_rate_options of this DisplayOptions.

        :return: The video_bit_rate_options of this DisplayOptions.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.DisplayOptionsVideoBitRateOptions`
        """
        return self._video_bit_rate_options

    @video_bit_rate_options.setter
    def video_bit_rate_options(self, video_bit_rate_options):
        """Sets the video_bit_rate_options of this DisplayOptions.

        :param video_bit_rate_options: The video_bit_rate_options of this DisplayOptions.
        :type video_bit_rate_options: :class:`huaweicloudsdkworkspaceapp.v1.DisplayOptionsVideoBitRateOptions`
        """
        self._video_bit_rate_options = video_bit_rate_options

    @property
    def peak_video_bit_rate(self):
        """Gets the peak_video_bit_rate of this DisplayOptions.

        视频峰值码率（Kbps）。取值范围为[256-100000]。默认：18000。

        :return: The peak_video_bit_rate of this DisplayOptions.
        :rtype: int
        """
        return self._peak_video_bit_rate

    @peak_video_bit_rate.setter
    def peak_video_bit_rate(self, peak_video_bit_rate):
        """Sets the peak_video_bit_rate of this DisplayOptions.

        视频峰值码率（Kbps）。取值范围为[256-100000]。默认：18000。

        :param peak_video_bit_rate: The peak_video_bit_rate of this DisplayOptions.
        :type peak_video_bit_rate: int
        """
        self._peak_video_bit_rate = peak_video_bit_rate

    @property
    def video_quality_options(self):
        """Gets the video_quality_options of this DisplayOptions.

        :return: The video_quality_options of this DisplayOptions.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.DisplayOptionsVideoQualityOptions`
        """
        return self._video_quality_options

    @video_quality_options.setter
    def video_quality_options(self, video_quality_options):
        """Sets the video_quality_options of this DisplayOptions.

        :param video_quality_options: The video_quality_options of this DisplayOptions.
        :type video_quality_options: :class:`huaweicloudsdkworkspaceapp.v1.DisplayOptionsVideoQualityOptions`
        """
        self._video_quality_options = video_quality_options

    @property
    def gop_size(self):
        """Gets the gop_size of this DisplayOptions.

        GOP大小。取值范围为[0-65535]。默认：100。

        :return: The gop_size of this DisplayOptions.
        :rtype: int
        """
        return self._gop_size

    @gop_size.setter
    def gop_size(self, gop_size):
        """Sets the gop_size of this DisplayOptions.

        GOP大小。取值范围为[0-65535]。默认：100。

        :param gop_size: The gop_size of this DisplayOptions.
        :type gop_size: int
        """
        self._gop_size = gop_size

    @property
    def encoding_preset(self):
        """Gets the encoding_preset of this DisplayOptions.

        编码预置。取值为： 预置1：Preset 1。 预置2：Preset 2。 预置3：Preset 3。 预置4：Preset 4。 预置5：Preset 5。 预置6：Preset 6。 预置7：Preset 7。

        :return: The encoding_preset of this DisplayOptions.
        :rtype: str
        """
        return self._encoding_preset

    @encoding_preset.setter
    def encoding_preset(self, encoding_preset):
        """Sets the encoding_preset of this DisplayOptions.

        编码预置。取值为： 预置1：Preset 1。 预置2：Preset 2。 预置3：Preset 3。 预置4：Preset 4。 预置5：Preset 5。 预置6：Preset 6。 预置7：Preset 7。

        :param encoding_preset: The encoding_preset of this DisplayOptions.
        :type encoding_preset: str
        """
        self._encoding_preset = encoding_preset

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
        if not isinstance(other, DisplayOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
