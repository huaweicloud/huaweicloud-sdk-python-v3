# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoliciesDisplayRenderingAccelerationOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'video_acceleration_enhancement_enable': 'bool',
        'video_optimization_enable': 'bool',
        'gpu_color_optimization_enable': 'bool',
        'video_recognition_threshold': 'int',
        'frame_rate_statistical_length': 'int',
        'image_quality_threshold': 'int',
        'refresh_frequency_threshold': 'int',
        'exiting_video_area_threshold': 'int',
        'min_video_width': 'int',
        'min_video_length': 'int',
        'single_frame_natural_percentage': 'str',
        'cyclical_natural_images_number': 'int',
        'non_natural_image_percentage': 'str',
        'non_natural_images_number': 'int'
    }

    attribute_map = {
        'video_acceleration_enhancement_enable': 'video_acceleration_enhancement_enable',
        'video_optimization_enable': 'video_optimization_enable',
        'gpu_color_optimization_enable': 'gpu_color_optimization_enable',
        'video_recognition_threshold': 'video_recognition_threshold',
        'frame_rate_statistical_length': 'frame_rate_statistical_length',
        'image_quality_threshold': 'image_quality_threshold',
        'refresh_frequency_threshold': 'refresh_frequency_threshold',
        'exiting_video_area_threshold': 'exiting_video_area_threshold',
        'min_video_width': 'min_video_width',
        'min_video_length': 'min_video_length',
        'single_frame_natural_percentage': 'single_frame_natural_percentage',
        'cyclical_natural_images_number': 'cyclical_natural_images_number',
        'non_natural_image_percentage': 'non_natural_image_percentage',
        'non_natural_images_number': 'non_natural_images_number'
    }

    def __init__(self, video_acceleration_enhancement_enable=None, video_optimization_enable=None, gpu_color_optimization_enable=None, video_recognition_threshold=None, frame_rate_statistical_length=None, image_quality_threshold=None, refresh_frequency_threshold=None, exiting_video_area_threshold=None, min_video_width=None, min_video_length=None, single_frame_natural_percentage=None, cyclical_natural_images_number=None, non_natural_image_percentage=None, non_natural_images_number=None):
        r"""PoliciesDisplayRenderingAccelerationOptions

        The model defined in huaweicloud sdk

        :param video_acceleration_enhancement_enable: 视频加速增强配置。取值为： false：表示关闭。 true：表示开启。
        :type video_acceleration_enhancement_enable: bool
        :param video_optimization_enable: 是否开启视频场景优化。取值为： false：表示关闭。 true：表示开启。
        :type video_optimization_enable: bool
        :param gpu_color_optimization_enable: 是否开启GPU色彩优化。取值为： false：表示关闭。 true：表示开启。
        :type gpu_color_optimization_enable: bool
        :param video_recognition_threshold: 视频识别阈值。取值范围为[0-500]。默认：10。
        :type video_recognition_threshold: int
        :param frame_rate_statistical_length: 帧率统计长度。取值范围为[2-100]。默认：4。
        :type frame_rate_statistical_length: int
        :param image_quality_threshold: 图像质量阈值。取值范围为[0-100]。默认：0。
        :type image_quality_threshold: int
        :param refresh_frequency_threshold: 刷新率阈值。取值范围为[1-100]。默认：3。
        :type refresh_frequency_threshold: int
        :param exiting_video_area_threshold: 退出视频区域阈值。取值范围为[0-100]。默认：8。
        :type exiting_video_area_threshold: int
        :param min_video_width: 识别为视频的最小宽。取值范围为[0-1280]。默认：191。
        :type min_video_width: int
        :param min_video_length: 识别为视频的最小高。取值范围为[0-1280]。默认：191。
        :type min_video_length: int
        :param single_frame_natural_percentage: 单帧自然图像块占比阈值。取值范围为[0.000001-1]。默认：0.3。
        :type single_frame_natural_percentage: str
        :param cyclical_natural_images_number: 周期自然图像数目占比阈值。取值范围为[0-100]。默认：2。
        :type cyclical_natural_images_number: int
        :param non_natural_image_percentage: 非自然图面积占比阈值。取值范围为[0.000001-1]。默认：0.85。
        :type non_natural_image_percentage: str
        :param non_natural_images_number: 非自然图数目占比阈值。取值范围为[0-100]。默认：25。
        :type non_natural_images_number: int
        """
        
        

        self._video_acceleration_enhancement_enable = None
        self._video_optimization_enable = None
        self._gpu_color_optimization_enable = None
        self._video_recognition_threshold = None
        self._frame_rate_statistical_length = None
        self._image_quality_threshold = None
        self._refresh_frequency_threshold = None
        self._exiting_video_area_threshold = None
        self._min_video_width = None
        self._min_video_length = None
        self._single_frame_natural_percentage = None
        self._cyclical_natural_images_number = None
        self._non_natural_image_percentage = None
        self._non_natural_images_number = None
        self.discriminator = None

        if video_acceleration_enhancement_enable is not None:
            self.video_acceleration_enhancement_enable = video_acceleration_enhancement_enable
        if video_optimization_enable is not None:
            self.video_optimization_enable = video_optimization_enable
        if gpu_color_optimization_enable is not None:
            self.gpu_color_optimization_enable = gpu_color_optimization_enable
        if video_recognition_threshold is not None:
            self.video_recognition_threshold = video_recognition_threshold
        if frame_rate_statistical_length is not None:
            self.frame_rate_statistical_length = frame_rate_statistical_length
        if image_quality_threshold is not None:
            self.image_quality_threshold = image_quality_threshold
        if refresh_frequency_threshold is not None:
            self.refresh_frequency_threshold = refresh_frequency_threshold
        if exiting_video_area_threshold is not None:
            self.exiting_video_area_threshold = exiting_video_area_threshold
        if min_video_width is not None:
            self.min_video_width = min_video_width
        if min_video_length is not None:
            self.min_video_length = min_video_length
        if single_frame_natural_percentage is not None:
            self.single_frame_natural_percentage = single_frame_natural_percentage
        if cyclical_natural_images_number is not None:
            self.cyclical_natural_images_number = cyclical_natural_images_number
        if non_natural_image_percentage is not None:
            self.non_natural_image_percentage = non_natural_image_percentage
        if non_natural_images_number is not None:
            self.non_natural_images_number = non_natural_images_number

    @property
    def video_acceleration_enhancement_enable(self):
        r"""Gets the video_acceleration_enhancement_enable of this PoliciesDisplayRenderingAccelerationOptions.

        视频加速增强配置。取值为： false：表示关闭。 true：表示开启。

        :return: The video_acceleration_enhancement_enable of this PoliciesDisplayRenderingAccelerationOptions.
        :rtype: bool
        """
        return self._video_acceleration_enhancement_enable

    @video_acceleration_enhancement_enable.setter
    def video_acceleration_enhancement_enable(self, video_acceleration_enhancement_enable):
        r"""Sets the video_acceleration_enhancement_enable of this PoliciesDisplayRenderingAccelerationOptions.

        视频加速增强配置。取值为： false：表示关闭。 true：表示开启。

        :param video_acceleration_enhancement_enable: The video_acceleration_enhancement_enable of this PoliciesDisplayRenderingAccelerationOptions.
        :type video_acceleration_enhancement_enable: bool
        """
        self._video_acceleration_enhancement_enable = video_acceleration_enhancement_enable

    @property
    def video_optimization_enable(self):
        r"""Gets the video_optimization_enable of this PoliciesDisplayRenderingAccelerationOptions.

        是否开启视频场景优化。取值为： false：表示关闭。 true：表示开启。

        :return: The video_optimization_enable of this PoliciesDisplayRenderingAccelerationOptions.
        :rtype: bool
        """
        return self._video_optimization_enable

    @video_optimization_enable.setter
    def video_optimization_enable(self, video_optimization_enable):
        r"""Sets the video_optimization_enable of this PoliciesDisplayRenderingAccelerationOptions.

        是否开启视频场景优化。取值为： false：表示关闭。 true：表示开启。

        :param video_optimization_enable: The video_optimization_enable of this PoliciesDisplayRenderingAccelerationOptions.
        :type video_optimization_enable: bool
        """
        self._video_optimization_enable = video_optimization_enable

    @property
    def gpu_color_optimization_enable(self):
        r"""Gets the gpu_color_optimization_enable of this PoliciesDisplayRenderingAccelerationOptions.

        是否开启GPU色彩优化。取值为： false：表示关闭。 true：表示开启。

        :return: The gpu_color_optimization_enable of this PoliciesDisplayRenderingAccelerationOptions.
        :rtype: bool
        """
        return self._gpu_color_optimization_enable

    @gpu_color_optimization_enable.setter
    def gpu_color_optimization_enable(self, gpu_color_optimization_enable):
        r"""Sets the gpu_color_optimization_enable of this PoliciesDisplayRenderingAccelerationOptions.

        是否开启GPU色彩优化。取值为： false：表示关闭。 true：表示开启。

        :param gpu_color_optimization_enable: The gpu_color_optimization_enable of this PoliciesDisplayRenderingAccelerationOptions.
        :type gpu_color_optimization_enable: bool
        """
        self._gpu_color_optimization_enable = gpu_color_optimization_enable

    @property
    def video_recognition_threshold(self):
        r"""Gets the video_recognition_threshold of this PoliciesDisplayRenderingAccelerationOptions.

        视频识别阈值。取值范围为[0-500]。默认：10。

        :return: The video_recognition_threshold of this PoliciesDisplayRenderingAccelerationOptions.
        :rtype: int
        """
        return self._video_recognition_threshold

    @video_recognition_threshold.setter
    def video_recognition_threshold(self, video_recognition_threshold):
        r"""Sets the video_recognition_threshold of this PoliciesDisplayRenderingAccelerationOptions.

        视频识别阈值。取值范围为[0-500]。默认：10。

        :param video_recognition_threshold: The video_recognition_threshold of this PoliciesDisplayRenderingAccelerationOptions.
        :type video_recognition_threshold: int
        """
        self._video_recognition_threshold = video_recognition_threshold

    @property
    def frame_rate_statistical_length(self):
        r"""Gets the frame_rate_statistical_length of this PoliciesDisplayRenderingAccelerationOptions.

        帧率统计长度。取值范围为[2-100]。默认：4。

        :return: The frame_rate_statistical_length of this PoliciesDisplayRenderingAccelerationOptions.
        :rtype: int
        """
        return self._frame_rate_statistical_length

    @frame_rate_statistical_length.setter
    def frame_rate_statistical_length(self, frame_rate_statistical_length):
        r"""Sets the frame_rate_statistical_length of this PoliciesDisplayRenderingAccelerationOptions.

        帧率统计长度。取值范围为[2-100]。默认：4。

        :param frame_rate_statistical_length: The frame_rate_statistical_length of this PoliciesDisplayRenderingAccelerationOptions.
        :type frame_rate_statistical_length: int
        """
        self._frame_rate_statistical_length = frame_rate_statistical_length

    @property
    def image_quality_threshold(self):
        r"""Gets the image_quality_threshold of this PoliciesDisplayRenderingAccelerationOptions.

        图像质量阈值。取值范围为[0-100]。默认：0。

        :return: The image_quality_threshold of this PoliciesDisplayRenderingAccelerationOptions.
        :rtype: int
        """
        return self._image_quality_threshold

    @image_quality_threshold.setter
    def image_quality_threshold(self, image_quality_threshold):
        r"""Sets the image_quality_threshold of this PoliciesDisplayRenderingAccelerationOptions.

        图像质量阈值。取值范围为[0-100]。默认：0。

        :param image_quality_threshold: The image_quality_threshold of this PoliciesDisplayRenderingAccelerationOptions.
        :type image_quality_threshold: int
        """
        self._image_quality_threshold = image_quality_threshold

    @property
    def refresh_frequency_threshold(self):
        r"""Gets the refresh_frequency_threshold of this PoliciesDisplayRenderingAccelerationOptions.

        刷新率阈值。取值范围为[1-100]。默认：3。

        :return: The refresh_frequency_threshold of this PoliciesDisplayRenderingAccelerationOptions.
        :rtype: int
        """
        return self._refresh_frequency_threshold

    @refresh_frequency_threshold.setter
    def refresh_frequency_threshold(self, refresh_frequency_threshold):
        r"""Sets the refresh_frequency_threshold of this PoliciesDisplayRenderingAccelerationOptions.

        刷新率阈值。取值范围为[1-100]。默认：3。

        :param refresh_frequency_threshold: The refresh_frequency_threshold of this PoliciesDisplayRenderingAccelerationOptions.
        :type refresh_frequency_threshold: int
        """
        self._refresh_frequency_threshold = refresh_frequency_threshold

    @property
    def exiting_video_area_threshold(self):
        r"""Gets the exiting_video_area_threshold of this PoliciesDisplayRenderingAccelerationOptions.

        退出视频区域阈值。取值范围为[0-100]。默认：8。

        :return: The exiting_video_area_threshold of this PoliciesDisplayRenderingAccelerationOptions.
        :rtype: int
        """
        return self._exiting_video_area_threshold

    @exiting_video_area_threshold.setter
    def exiting_video_area_threshold(self, exiting_video_area_threshold):
        r"""Sets the exiting_video_area_threshold of this PoliciesDisplayRenderingAccelerationOptions.

        退出视频区域阈值。取值范围为[0-100]。默认：8。

        :param exiting_video_area_threshold: The exiting_video_area_threshold of this PoliciesDisplayRenderingAccelerationOptions.
        :type exiting_video_area_threshold: int
        """
        self._exiting_video_area_threshold = exiting_video_area_threshold

    @property
    def min_video_width(self):
        r"""Gets the min_video_width of this PoliciesDisplayRenderingAccelerationOptions.

        识别为视频的最小宽。取值范围为[0-1280]。默认：191。

        :return: The min_video_width of this PoliciesDisplayRenderingAccelerationOptions.
        :rtype: int
        """
        return self._min_video_width

    @min_video_width.setter
    def min_video_width(self, min_video_width):
        r"""Sets the min_video_width of this PoliciesDisplayRenderingAccelerationOptions.

        识别为视频的最小宽。取值范围为[0-1280]。默认：191。

        :param min_video_width: The min_video_width of this PoliciesDisplayRenderingAccelerationOptions.
        :type min_video_width: int
        """
        self._min_video_width = min_video_width

    @property
    def min_video_length(self):
        r"""Gets the min_video_length of this PoliciesDisplayRenderingAccelerationOptions.

        识别为视频的最小高。取值范围为[0-1280]。默认：191。

        :return: The min_video_length of this PoliciesDisplayRenderingAccelerationOptions.
        :rtype: int
        """
        return self._min_video_length

    @min_video_length.setter
    def min_video_length(self, min_video_length):
        r"""Sets the min_video_length of this PoliciesDisplayRenderingAccelerationOptions.

        识别为视频的最小高。取值范围为[0-1280]。默认：191。

        :param min_video_length: The min_video_length of this PoliciesDisplayRenderingAccelerationOptions.
        :type min_video_length: int
        """
        self._min_video_length = min_video_length

    @property
    def single_frame_natural_percentage(self):
        r"""Gets the single_frame_natural_percentage of this PoliciesDisplayRenderingAccelerationOptions.

        单帧自然图像块占比阈值。取值范围为[0.000001-1]。默认：0.3。

        :return: The single_frame_natural_percentage of this PoliciesDisplayRenderingAccelerationOptions.
        :rtype: str
        """
        return self._single_frame_natural_percentage

    @single_frame_natural_percentage.setter
    def single_frame_natural_percentage(self, single_frame_natural_percentage):
        r"""Sets the single_frame_natural_percentage of this PoliciesDisplayRenderingAccelerationOptions.

        单帧自然图像块占比阈值。取值范围为[0.000001-1]。默认：0.3。

        :param single_frame_natural_percentage: The single_frame_natural_percentage of this PoliciesDisplayRenderingAccelerationOptions.
        :type single_frame_natural_percentage: str
        """
        self._single_frame_natural_percentage = single_frame_natural_percentage

    @property
    def cyclical_natural_images_number(self):
        r"""Gets the cyclical_natural_images_number of this PoliciesDisplayRenderingAccelerationOptions.

        周期自然图像数目占比阈值。取值范围为[0-100]。默认：2。

        :return: The cyclical_natural_images_number of this PoliciesDisplayRenderingAccelerationOptions.
        :rtype: int
        """
        return self._cyclical_natural_images_number

    @cyclical_natural_images_number.setter
    def cyclical_natural_images_number(self, cyclical_natural_images_number):
        r"""Sets the cyclical_natural_images_number of this PoliciesDisplayRenderingAccelerationOptions.

        周期自然图像数目占比阈值。取值范围为[0-100]。默认：2。

        :param cyclical_natural_images_number: The cyclical_natural_images_number of this PoliciesDisplayRenderingAccelerationOptions.
        :type cyclical_natural_images_number: int
        """
        self._cyclical_natural_images_number = cyclical_natural_images_number

    @property
    def non_natural_image_percentage(self):
        r"""Gets the non_natural_image_percentage of this PoliciesDisplayRenderingAccelerationOptions.

        非自然图面积占比阈值。取值范围为[0.000001-1]。默认：0.85。

        :return: The non_natural_image_percentage of this PoliciesDisplayRenderingAccelerationOptions.
        :rtype: str
        """
        return self._non_natural_image_percentage

    @non_natural_image_percentage.setter
    def non_natural_image_percentage(self, non_natural_image_percentage):
        r"""Sets the non_natural_image_percentage of this PoliciesDisplayRenderingAccelerationOptions.

        非自然图面积占比阈值。取值范围为[0.000001-1]。默认：0.85。

        :param non_natural_image_percentage: The non_natural_image_percentage of this PoliciesDisplayRenderingAccelerationOptions.
        :type non_natural_image_percentage: str
        """
        self._non_natural_image_percentage = non_natural_image_percentage

    @property
    def non_natural_images_number(self):
        r"""Gets the non_natural_images_number of this PoliciesDisplayRenderingAccelerationOptions.

        非自然图数目占比阈值。取值范围为[0-100]。默认：25。

        :return: The non_natural_images_number of this PoliciesDisplayRenderingAccelerationOptions.
        :rtype: int
        """
        return self._non_natural_images_number

    @non_natural_images_number.setter
    def non_natural_images_number(self, non_natural_images_number):
        r"""Sets the non_natural_images_number of this PoliciesDisplayRenderingAccelerationOptions.

        非自然图数目占比阈值。取值范围为[0-100]。默认：25。

        :param non_natural_images_number: The non_natural_images_number of this PoliciesDisplayRenderingAccelerationOptions.
        :type non_natural_images_number: int
        """
        self._non_natural_images_number = non_natural_images_number

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
        if not isinstance(other, PoliciesDisplayRenderingAccelerationOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
