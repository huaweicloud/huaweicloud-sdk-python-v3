# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoliciesDisplayAdaptiveBitrateControlOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'peak_bandwidth_suppression_enable': 'bool',
        'expected_average_network_latency': 'int',
        'network_latency_threshold1': 'int',
        'network_latency_threshold2': 'int',
        'min_dynamic_frame_rate': 'int',
        'min_dynamic_frame_rate_lv1': 'int',
        'min_dynamic_frame_rate_lv2': 'int',
        'rtt_threshold': 'int',
        'min_add_framerate': 'int',
        'max_add_framerate': 'int',
        'sub_framerate': 'int',
        'adaptive_bandwidth_lower_limit': 'int',
        'adaptive_compression_quality_lower_limit': 'int',
        'adaptive_compression_quality_upper_limit': 'int',
        'adaptive_compression_quality_increase_limit': 'int',
        'adaptive_compression_quality_decrease_limit': 'int',
        'adaptive_average_quality_lower_limit': 'int',
        'adaptive_average_quality_upper_limit': 'int',
        'adaptive_average_quality_increase_limit': 'int',
        'adaptive_average_quality_decrease_limit': 'int',
        'adaptive_min_quality_lower_limit': 'int',
        'adaptive_min_quality_upper_limit': 'int',
        'adaptive_min_quality_increase_limit': 'int',
        'adaptive_min_quality_decrease_limit': 'int'
    }

    attribute_map = {
        'peak_bandwidth_suppression_enable': 'peak_bandwidth_suppression_enable',
        'expected_average_network_latency': 'expected_average_network_latency',
        'network_latency_threshold1': 'network_latency_threshold1',
        'network_latency_threshold2': 'network_latency_threshold2',
        'min_dynamic_frame_rate': 'min_dynamic_frame_rate',
        'min_dynamic_frame_rate_lv1': 'min_dynamic_frame_rate_lv1',
        'min_dynamic_frame_rate_lv2': 'min_dynamic_frame_rate_lv2',
        'rtt_threshold': 'rtt_threshold',
        'min_add_framerate': 'min_add_framerate',
        'max_add_framerate': 'max_add_framerate',
        'sub_framerate': 'sub_framerate',
        'adaptive_bandwidth_lower_limit': 'adaptive_bandwidth_lower_limit',
        'adaptive_compression_quality_lower_limit': 'adaptive_compression_quality_lower_limit',
        'adaptive_compression_quality_upper_limit': 'adaptive_compression_quality_upper_limit',
        'adaptive_compression_quality_increase_limit': 'adaptive_compression_quality_increase_limit',
        'adaptive_compression_quality_decrease_limit': 'adaptive_compression_quality_decrease_limit',
        'adaptive_average_quality_lower_limit': 'adaptive_average_quality_lower_limit',
        'adaptive_average_quality_upper_limit': 'adaptive_average_quality_upper_limit',
        'adaptive_average_quality_increase_limit': 'adaptive_average_quality_increase_limit',
        'adaptive_average_quality_decrease_limit': 'adaptive_average_quality_decrease_limit',
        'adaptive_min_quality_lower_limit': 'adaptive_min_quality_lower_limit',
        'adaptive_min_quality_upper_limit': 'adaptive_min_quality_upper_limit',
        'adaptive_min_quality_increase_limit': 'adaptive_min_quality_increase_limit',
        'adaptive_min_quality_decrease_limit': 'adaptive_min_quality_decrease_limit'
    }

    def __init__(self, peak_bandwidth_suppression_enable=None, expected_average_network_latency=None, network_latency_threshold1=None, network_latency_threshold2=None, min_dynamic_frame_rate=None, min_dynamic_frame_rate_lv1=None, min_dynamic_frame_rate_lv2=None, rtt_threshold=None, min_add_framerate=None, max_add_framerate=None, sub_framerate=None, adaptive_bandwidth_lower_limit=None, adaptive_compression_quality_lower_limit=None, adaptive_compression_quality_upper_limit=None, adaptive_compression_quality_increase_limit=None, adaptive_compression_quality_decrease_limit=None, adaptive_average_quality_lower_limit=None, adaptive_average_quality_upper_limit=None, adaptive_average_quality_increase_limit=None, adaptive_average_quality_decrease_limit=None, adaptive_min_quality_lower_limit=None, adaptive_min_quality_upper_limit=None, adaptive_min_quality_increase_limit=None, adaptive_min_quality_decrease_limit=None):
        r"""PoliciesDisplayAdaptiveBitrateControlOptions

        The model defined in huaweicloud sdk

        :param peak_bandwidth_suppression_enable: 峰值带宽抑制：取值为： false：表示关闭。 true：表示开启。
        :type peak_bandwidth_suppression_enable: bool
        :param expected_average_network_latency: 网络平均期望延时。取值范围为[1-2000]。默认：160。
        :type expected_average_network_latency: int
        :param network_latency_threshold1: 网络延时阈值1（ms）。取值范围为[1-2000]。默认：160。
        :type network_latency_threshold1: int
        :param network_latency_threshold2: 网络延时阈值2（ms）。取值范围为[1-2000]。默认：300。
        :type network_latency_threshold2: int
        :param min_dynamic_frame_rate: 最小动态帧率（fps）。取值范围为[1-60]。默认：17。
        :type min_dynamic_frame_rate: int
        :param min_dynamic_frame_rate_lv1: 最小动态帧率Lv1（fps）。取值范围为[1-60]。默认：17。
        :type min_dynamic_frame_rate_lv1: int
        :param min_dynamic_frame_rate_lv2: 最小动态帧率Lv2（fps）。取值范围为[1-60]。默认：10。
        :type min_dynamic_frame_rate_lv2: int
        :param rtt_threshold: 帧率控制参数1。取值范围为[0-1000]。默认：20。
        :type rtt_threshold: int
        :param min_add_framerate: 帧率控制参数2。取值范围为[0-120]。默认：8。
        :type min_add_framerate: int
        :param max_add_framerate: 帧率控制参数3。取值范围为[0-120]。默认：20。
        :type max_add_framerate: int
        :param sub_framerate: 帧率控制参数4。取值范围为[0-120]。默认：25。
        :type sub_framerate: int
        :param adaptive_bandwidth_lower_limit: 自适应带宽下限。取值范围为[100-20000]。默认：500。
        :type adaptive_bandwidth_lower_limit: int
        :param adaptive_compression_quality_lower_limit: 自适应有损压缩质量下限。取值范围为[1-100]。默认：60。
        :type adaptive_compression_quality_lower_limit: int
        :param adaptive_compression_quality_upper_limit: 自适应有损压缩质量上限。取值范围为[1-100]。默认：85。
        :type adaptive_compression_quality_upper_limit: int
        :param adaptive_compression_quality_increase_limit: 自适应有损压缩质量增限。取值范围为[1-100]。默认：5。
        :type adaptive_compression_quality_increase_limit: int
        :param adaptive_compression_quality_decrease_limit: 自适应有损压缩质量减限。取值范围为[1-100]。默认：10。
        :type adaptive_compression_quality_decrease_limit: int
        :param adaptive_average_quality_lower_limit: 自适应视频平均质量下限。取值范围为[5-50]。默认：15。
        :type adaptive_average_quality_lower_limit: int
        :param adaptive_average_quality_upper_limit: 自适应视频平均质量上限。取值范围为[5-50]。默认：25。
        :type adaptive_average_quality_upper_limit: int
        :param adaptive_average_quality_increase_limit: 自适应视频平均质量增限。取值范围为[1-50]。默认：3。
        :type adaptive_average_quality_increase_limit: int
        :param adaptive_average_quality_decrease_limit: 自适应视频平均质量减限。取值范围为[1-50]。默认：1。
        :type adaptive_average_quality_decrease_limit: int
        :param adaptive_min_quality_lower_limit: 自适应视频最低质量下限。取值范围为[5-69]。默认：25。
        :type adaptive_min_quality_lower_limit: int
        :param adaptive_min_quality_upper_limit: 自适应视频最低质量上限。取值范围为[5-69]。默认：30。
        :type adaptive_min_quality_upper_limit: int
        :param adaptive_min_quality_increase_limit: 自适应视频最低质量增限。取值范围为[1-50]。默认：3。
        :type adaptive_min_quality_increase_limit: int
        :param adaptive_min_quality_decrease_limit: 自适应视频最低质量减限。取值范围为[1-50]。默认：1。
        :type adaptive_min_quality_decrease_limit: int
        """
        
        

        self._peak_bandwidth_suppression_enable = None
        self._expected_average_network_latency = None
        self._network_latency_threshold1 = None
        self._network_latency_threshold2 = None
        self._min_dynamic_frame_rate = None
        self._min_dynamic_frame_rate_lv1 = None
        self._min_dynamic_frame_rate_lv2 = None
        self._rtt_threshold = None
        self._min_add_framerate = None
        self._max_add_framerate = None
        self._sub_framerate = None
        self._adaptive_bandwidth_lower_limit = None
        self._adaptive_compression_quality_lower_limit = None
        self._adaptive_compression_quality_upper_limit = None
        self._adaptive_compression_quality_increase_limit = None
        self._adaptive_compression_quality_decrease_limit = None
        self._adaptive_average_quality_lower_limit = None
        self._adaptive_average_quality_upper_limit = None
        self._adaptive_average_quality_increase_limit = None
        self._adaptive_average_quality_decrease_limit = None
        self._adaptive_min_quality_lower_limit = None
        self._adaptive_min_quality_upper_limit = None
        self._adaptive_min_quality_increase_limit = None
        self._adaptive_min_quality_decrease_limit = None
        self.discriminator = None

        if peak_bandwidth_suppression_enable is not None:
            self.peak_bandwidth_suppression_enable = peak_bandwidth_suppression_enable
        if expected_average_network_latency is not None:
            self.expected_average_network_latency = expected_average_network_latency
        if network_latency_threshold1 is not None:
            self.network_latency_threshold1 = network_latency_threshold1
        if network_latency_threshold2 is not None:
            self.network_latency_threshold2 = network_latency_threshold2
        if min_dynamic_frame_rate is not None:
            self.min_dynamic_frame_rate = min_dynamic_frame_rate
        if min_dynamic_frame_rate_lv1 is not None:
            self.min_dynamic_frame_rate_lv1 = min_dynamic_frame_rate_lv1
        if min_dynamic_frame_rate_lv2 is not None:
            self.min_dynamic_frame_rate_lv2 = min_dynamic_frame_rate_lv2
        if rtt_threshold is not None:
            self.rtt_threshold = rtt_threshold
        if min_add_framerate is not None:
            self.min_add_framerate = min_add_framerate
        if max_add_framerate is not None:
            self.max_add_framerate = max_add_framerate
        if sub_framerate is not None:
            self.sub_framerate = sub_framerate
        if adaptive_bandwidth_lower_limit is not None:
            self.adaptive_bandwidth_lower_limit = adaptive_bandwidth_lower_limit
        if adaptive_compression_quality_lower_limit is not None:
            self.adaptive_compression_quality_lower_limit = adaptive_compression_quality_lower_limit
        if adaptive_compression_quality_upper_limit is not None:
            self.adaptive_compression_quality_upper_limit = adaptive_compression_quality_upper_limit
        if adaptive_compression_quality_increase_limit is not None:
            self.adaptive_compression_quality_increase_limit = adaptive_compression_quality_increase_limit
        if adaptive_compression_quality_decrease_limit is not None:
            self.adaptive_compression_quality_decrease_limit = adaptive_compression_quality_decrease_limit
        if adaptive_average_quality_lower_limit is not None:
            self.adaptive_average_quality_lower_limit = adaptive_average_quality_lower_limit
        if adaptive_average_quality_upper_limit is not None:
            self.adaptive_average_quality_upper_limit = adaptive_average_quality_upper_limit
        if adaptive_average_quality_increase_limit is not None:
            self.adaptive_average_quality_increase_limit = adaptive_average_quality_increase_limit
        if adaptive_average_quality_decrease_limit is not None:
            self.adaptive_average_quality_decrease_limit = adaptive_average_quality_decrease_limit
        if adaptive_min_quality_lower_limit is not None:
            self.adaptive_min_quality_lower_limit = adaptive_min_quality_lower_limit
        if adaptive_min_quality_upper_limit is not None:
            self.adaptive_min_quality_upper_limit = adaptive_min_quality_upper_limit
        if adaptive_min_quality_increase_limit is not None:
            self.adaptive_min_quality_increase_limit = adaptive_min_quality_increase_limit
        if adaptive_min_quality_decrease_limit is not None:
            self.adaptive_min_quality_decrease_limit = adaptive_min_quality_decrease_limit

    @property
    def peak_bandwidth_suppression_enable(self):
        r"""Gets the peak_bandwidth_suppression_enable of this PoliciesDisplayAdaptiveBitrateControlOptions.

        峰值带宽抑制：取值为： false：表示关闭。 true：表示开启。

        :return: The peak_bandwidth_suppression_enable of this PoliciesDisplayAdaptiveBitrateControlOptions.
        :rtype: bool
        """
        return self._peak_bandwidth_suppression_enable

    @peak_bandwidth_suppression_enable.setter
    def peak_bandwidth_suppression_enable(self, peak_bandwidth_suppression_enable):
        r"""Sets the peak_bandwidth_suppression_enable of this PoliciesDisplayAdaptiveBitrateControlOptions.

        峰值带宽抑制：取值为： false：表示关闭。 true：表示开启。

        :param peak_bandwidth_suppression_enable: The peak_bandwidth_suppression_enable of this PoliciesDisplayAdaptiveBitrateControlOptions.
        :type peak_bandwidth_suppression_enable: bool
        """
        self._peak_bandwidth_suppression_enable = peak_bandwidth_suppression_enable

    @property
    def expected_average_network_latency(self):
        r"""Gets the expected_average_network_latency of this PoliciesDisplayAdaptiveBitrateControlOptions.

        网络平均期望延时。取值范围为[1-2000]。默认：160。

        :return: The expected_average_network_latency of this PoliciesDisplayAdaptiveBitrateControlOptions.
        :rtype: int
        """
        return self._expected_average_network_latency

    @expected_average_network_latency.setter
    def expected_average_network_latency(self, expected_average_network_latency):
        r"""Sets the expected_average_network_latency of this PoliciesDisplayAdaptiveBitrateControlOptions.

        网络平均期望延时。取值范围为[1-2000]。默认：160。

        :param expected_average_network_latency: The expected_average_network_latency of this PoliciesDisplayAdaptiveBitrateControlOptions.
        :type expected_average_network_latency: int
        """
        self._expected_average_network_latency = expected_average_network_latency

    @property
    def network_latency_threshold1(self):
        r"""Gets the network_latency_threshold1 of this PoliciesDisplayAdaptiveBitrateControlOptions.

        网络延时阈值1（ms）。取值范围为[1-2000]。默认：160。

        :return: The network_latency_threshold1 of this PoliciesDisplayAdaptiveBitrateControlOptions.
        :rtype: int
        """
        return self._network_latency_threshold1

    @network_latency_threshold1.setter
    def network_latency_threshold1(self, network_latency_threshold1):
        r"""Sets the network_latency_threshold1 of this PoliciesDisplayAdaptiveBitrateControlOptions.

        网络延时阈值1（ms）。取值范围为[1-2000]。默认：160。

        :param network_latency_threshold1: The network_latency_threshold1 of this PoliciesDisplayAdaptiveBitrateControlOptions.
        :type network_latency_threshold1: int
        """
        self._network_latency_threshold1 = network_latency_threshold1

    @property
    def network_latency_threshold2(self):
        r"""Gets the network_latency_threshold2 of this PoliciesDisplayAdaptiveBitrateControlOptions.

        网络延时阈值2（ms）。取值范围为[1-2000]。默认：300。

        :return: The network_latency_threshold2 of this PoliciesDisplayAdaptiveBitrateControlOptions.
        :rtype: int
        """
        return self._network_latency_threshold2

    @network_latency_threshold2.setter
    def network_latency_threshold2(self, network_latency_threshold2):
        r"""Sets the network_latency_threshold2 of this PoliciesDisplayAdaptiveBitrateControlOptions.

        网络延时阈值2（ms）。取值范围为[1-2000]。默认：300。

        :param network_latency_threshold2: The network_latency_threshold2 of this PoliciesDisplayAdaptiveBitrateControlOptions.
        :type network_latency_threshold2: int
        """
        self._network_latency_threshold2 = network_latency_threshold2

    @property
    def min_dynamic_frame_rate(self):
        r"""Gets the min_dynamic_frame_rate of this PoliciesDisplayAdaptiveBitrateControlOptions.

        最小动态帧率（fps）。取值范围为[1-60]。默认：17。

        :return: The min_dynamic_frame_rate of this PoliciesDisplayAdaptiveBitrateControlOptions.
        :rtype: int
        """
        return self._min_dynamic_frame_rate

    @min_dynamic_frame_rate.setter
    def min_dynamic_frame_rate(self, min_dynamic_frame_rate):
        r"""Sets the min_dynamic_frame_rate of this PoliciesDisplayAdaptiveBitrateControlOptions.

        最小动态帧率（fps）。取值范围为[1-60]。默认：17。

        :param min_dynamic_frame_rate: The min_dynamic_frame_rate of this PoliciesDisplayAdaptiveBitrateControlOptions.
        :type min_dynamic_frame_rate: int
        """
        self._min_dynamic_frame_rate = min_dynamic_frame_rate

    @property
    def min_dynamic_frame_rate_lv1(self):
        r"""Gets the min_dynamic_frame_rate_lv1 of this PoliciesDisplayAdaptiveBitrateControlOptions.

        最小动态帧率Lv1（fps）。取值范围为[1-60]。默认：17。

        :return: The min_dynamic_frame_rate_lv1 of this PoliciesDisplayAdaptiveBitrateControlOptions.
        :rtype: int
        """
        return self._min_dynamic_frame_rate_lv1

    @min_dynamic_frame_rate_lv1.setter
    def min_dynamic_frame_rate_lv1(self, min_dynamic_frame_rate_lv1):
        r"""Sets the min_dynamic_frame_rate_lv1 of this PoliciesDisplayAdaptiveBitrateControlOptions.

        最小动态帧率Lv1（fps）。取值范围为[1-60]。默认：17。

        :param min_dynamic_frame_rate_lv1: The min_dynamic_frame_rate_lv1 of this PoliciesDisplayAdaptiveBitrateControlOptions.
        :type min_dynamic_frame_rate_lv1: int
        """
        self._min_dynamic_frame_rate_lv1 = min_dynamic_frame_rate_lv1

    @property
    def min_dynamic_frame_rate_lv2(self):
        r"""Gets the min_dynamic_frame_rate_lv2 of this PoliciesDisplayAdaptiveBitrateControlOptions.

        最小动态帧率Lv2（fps）。取值范围为[1-60]。默认：10。

        :return: The min_dynamic_frame_rate_lv2 of this PoliciesDisplayAdaptiveBitrateControlOptions.
        :rtype: int
        """
        return self._min_dynamic_frame_rate_lv2

    @min_dynamic_frame_rate_lv2.setter
    def min_dynamic_frame_rate_lv2(self, min_dynamic_frame_rate_lv2):
        r"""Sets the min_dynamic_frame_rate_lv2 of this PoliciesDisplayAdaptiveBitrateControlOptions.

        最小动态帧率Lv2（fps）。取值范围为[1-60]。默认：10。

        :param min_dynamic_frame_rate_lv2: The min_dynamic_frame_rate_lv2 of this PoliciesDisplayAdaptiveBitrateControlOptions.
        :type min_dynamic_frame_rate_lv2: int
        """
        self._min_dynamic_frame_rate_lv2 = min_dynamic_frame_rate_lv2

    @property
    def rtt_threshold(self):
        r"""Gets the rtt_threshold of this PoliciesDisplayAdaptiveBitrateControlOptions.

        帧率控制参数1。取值范围为[0-1000]。默认：20。

        :return: The rtt_threshold of this PoliciesDisplayAdaptiveBitrateControlOptions.
        :rtype: int
        """
        return self._rtt_threshold

    @rtt_threshold.setter
    def rtt_threshold(self, rtt_threshold):
        r"""Sets the rtt_threshold of this PoliciesDisplayAdaptiveBitrateControlOptions.

        帧率控制参数1。取值范围为[0-1000]。默认：20。

        :param rtt_threshold: The rtt_threshold of this PoliciesDisplayAdaptiveBitrateControlOptions.
        :type rtt_threshold: int
        """
        self._rtt_threshold = rtt_threshold

    @property
    def min_add_framerate(self):
        r"""Gets the min_add_framerate of this PoliciesDisplayAdaptiveBitrateControlOptions.

        帧率控制参数2。取值范围为[0-120]。默认：8。

        :return: The min_add_framerate of this PoliciesDisplayAdaptiveBitrateControlOptions.
        :rtype: int
        """
        return self._min_add_framerate

    @min_add_framerate.setter
    def min_add_framerate(self, min_add_framerate):
        r"""Sets the min_add_framerate of this PoliciesDisplayAdaptiveBitrateControlOptions.

        帧率控制参数2。取值范围为[0-120]。默认：8。

        :param min_add_framerate: The min_add_framerate of this PoliciesDisplayAdaptiveBitrateControlOptions.
        :type min_add_framerate: int
        """
        self._min_add_framerate = min_add_framerate

    @property
    def max_add_framerate(self):
        r"""Gets the max_add_framerate of this PoliciesDisplayAdaptiveBitrateControlOptions.

        帧率控制参数3。取值范围为[0-120]。默认：20。

        :return: The max_add_framerate of this PoliciesDisplayAdaptiveBitrateControlOptions.
        :rtype: int
        """
        return self._max_add_framerate

    @max_add_framerate.setter
    def max_add_framerate(self, max_add_framerate):
        r"""Sets the max_add_framerate of this PoliciesDisplayAdaptiveBitrateControlOptions.

        帧率控制参数3。取值范围为[0-120]。默认：20。

        :param max_add_framerate: The max_add_framerate of this PoliciesDisplayAdaptiveBitrateControlOptions.
        :type max_add_framerate: int
        """
        self._max_add_framerate = max_add_framerate

    @property
    def sub_framerate(self):
        r"""Gets the sub_framerate of this PoliciesDisplayAdaptiveBitrateControlOptions.

        帧率控制参数4。取值范围为[0-120]。默认：25。

        :return: The sub_framerate of this PoliciesDisplayAdaptiveBitrateControlOptions.
        :rtype: int
        """
        return self._sub_framerate

    @sub_framerate.setter
    def sub_framerate(self, sub_framerate):
        r"""Sets the sub_framerate of this PoliciesDisplayAdaptiveBitrateControlOptions.

        帧率控制参数4。取值范围为[0-120]。默认：25。

        :param sub_framerate: The sub_framerate of this PoliciesDisplayAdaptiveBitrateControlOptions.
        :type sub_framerate: int
        """
        self._sub_framerate = sub_framerate

    @property
    def adaptive_bandwidth_lower_limit(self):
        r"""Gets the adaptive_bandwidth_lower_limit of this PoliciesDisplayAdaptiveBitrateControlOptions.

        自适应带宽下限。取值范围为[100-20000]。默认：500。

        :return: The adaptive_bandwidth_lower_limit of this PoliciesDisplayAdaptiveBitrateControlOptions.
        :rtype: int
        """
        return self._adaptive_bandwidth_lower_limit

    @adaptive_bandwidth_lower_limit.setter
    def adaptive_bandwidth_lower_limit(self, adaptive_bandwidth_lower_limit):
        r"""Sets the adaptive_bandwidth_lower_limit of this PoliciesDisplayAdaptiveBitrateControlOptions.

        自适应带宽下限。取值范围为[100-20000]。默认：500。

        :param adaptive_bandwidth_lower_limit: The adaptive_bandwidth_lower_limit of this PoliciesDisplayAdaptiveBitrateControlOptions.
        :type adaptive_bandwidth_lower_limit: int
        """
        self._adaptive_bandwidth_lower_limit = adaptive_bandwidth_lower_limit

    @property
    def adaptive_compression_quality_lower_limit(self):
        r"""Gets the adaptive_compression_quality_lower_limit of this PoliciesDisplayAdaptiveBitrateControlOptions.

        自适应有损压缩质量下限。取值范围为[1-100]。默认：60。

        :return: The adaptive_compression_quality_lower_limit of this PoliciesDisplayAdaptiveBitrateControlOptions.
        :rtype: int
        """
        return self._adaptive_compression_quality_lower_limit

    @adaptive_compression_quality_lower_limit.setter
    def adaptive_compression_quality_lower_limit(self, adaptive_compression_quality_lower_limit):
        r"""Sets the adaptive_compression_quality_lower_limit of this PoliciesDisplayAdaptiveBitrateControlOptions.

        自适应有损压缩质量下限。取值范围为[1-100]。默认：60。

        :param adaptive_compression_quality_lower_limit: The adaptive_compression_quality_lower_limit of this PoliciesDisplayAdaptiveBitrateControlOptions.
        :type adaptive_compression_quality_lower_limit: int
        """
        self._adaptive_compression_quality_lower_limit = adaptive_compression_quality_lower_limit

    @property
    def adaptive_compression_quality_upper_limit(self):
        r"""Gets the adaptive_compression_quality_upper_limit of this PoliciesDisplayAdaptiveBitrateControlOptions.

        自适应有损压缩质量上限。取值范围为[1-100]。默认：85。

        :return: The adaptive_compression_quality_upper_limit of this PoliciesDisplayAdaptiveBitrateControlOptions.
        :rtype: int
        """
        return self._adaptive_compression_quality_upper_limit

    @adaptive_compression_quality_upper_limit.setter
    def adaptive_compression_quality_upper_limit(self, adaptive_compression_quality_upper_limit):
        r"""Sets the adaptive_compression_quality_upper_limit of this PoliciesDisplayAdaptiveBitrateControlOptions.

        自适应有损压缩质量上限。取值范围为[1-100]。默认：85。

        :param adaptive_compression_quality_upper_limit: The adaptive_compression_quality_upper_limit of this PoliciesDisplayAdaptiveBitrateControlOptions.
        :type adaptive_compression_quality_upper_limit: int
        """
        self._adaptive_compression_quality_upper_limit = adaptive_compression_quality_upper_limit

    @property
    def adaptive_compression_quality_increase_limit(self):
        r"""Gets the adaptive_compression_quality_increase_limit of this PoliciesDisplayAdaptiveBitrateControlOptions.

        自适应有损压缩质量增限。取值范围为[1-100]。默认：5。

        :return: The adaptive_compression_quality_increase_limit of this PoliciesDisplayAdaptiveBitrateControlOptions.
        :rtype: int
        """
        return self._adaptive_compression_quality_increase_limit

    @adaptive_compression_quality_increase_limit.setter
    def adaptive_compression_quality_increase_limit(self, adaptive_compression_quality_increase_limit):
        r"""Sets the adaptive_compression_quality_increase_limit of this PoliciesDisplayAdaptiveBitrateControlOptions.

        自适应有损压缩质量增限。取值范围为[1-100]。默认：5。

        :param adaptive_compression_quality_increase_limit: The adaptive_compression_quality_increase_limit of this PoliciesDisplayAdaptiveBitrateControlOptions.
        :type adaptive_compression_quality_increase_limit: int
        """
        self._adaptive_compression_quality_increase_limit = adaptive_compression_quality_increase_limit

    @property
    def adaptive_compression_quality_decrease_limit(self):
        r"""Gets the adaptive_compression_quality_decrease_limit of this PoliciesDisplayAdaptiveBitrateControlOptions.

        自适应有损压缩质量减限。取值范围为[1-100]。默认：10。

        :return: The adaptive_compression_quality_decrease_limit of this PoliciesDisplayAdaptiveBitrateControlOptions.
        :rtype: int
        """
        return self._adaptive_compression_quality_decrease_limit

    @adaptive_compression_quality_decrease_limit.setter
    def adaptive_compression_quality_decrease_limit(self, adaptive_compression_quality_decrease_limit):
        r"""Sets the adaptive_compression_quality_decrease_limit of this PoliciesDisplayAdaptiveBitrateControlOptions.

        自适应有损压缩质量减限。取值范围为[1-100]。默认：10。

        :param adaptive_compression_quality_decrease_limit: The adaptive_compression_quality_decrease_limit of this PoliciesDisplayAdaptiveBitrateControlOptions.
        :type adaptive_compression_quality_decrease_limit: int
        """
        self._adaptive_compression_quality_decrease_limit = adaptive_compression_quality_decrease_limit

    @property
    def adaptive_average_quality_lower_limit(self):
        r"""Gets the adaptive_average_quality_lower_limit of this PoliciesDisplayAdaptiveBitrateControlOptions.

        自适应视频平均质量下限。取值范围为[5-50]。默认：15。

        :return: The adaptive_average_quality_lower_limit of this PoliciesDisplayAdaptiveBitrateControlOptions.
        :rtype: int
        """
        return self._adaptive_average_quality_lower_limit

    @adaptive_average_quality_lower_limit.setter
    def adaptive_average_quality_lower_limit(self, adaptive_average_quality_lower_limit):
        r"""Sets the adaptive_average_quality_lower_limit of this PoliciesDisplayAdaptiveBitrateControlOptions.

        自适应视频平均质量下限。取值范围为[5-50]。默认：15。

        :param adaptive_average_quality_lower_limit: The adaptive_average_quality_lower_limit of this PoliciesDisplayAdaptiveBitrateControlOptions.
        :type adaptive_average_quality_lower_limit: int
        """
        self._adaptive_average_quality_lower_limit = adaptive_average_quality_lower_limit

    @property
    def adaptive_average_quality_upper_limit(self):
        r"""Gets the adaptive_average_quality_upper_limit of this PoliciesDisplayAdaptiveBitrateControlOptions.

        自适应视频平均质量上限。取值范围为[5-50]。默认：25。

        :return: The adaptive_average_quality_upper_limit of this PoliciesDisplayAdaptiveBitrateControlOptions.
        :rtype: int
        """
        return self._adaptive_average_quality_upper_limit

    @adaptive_average_quality_upper_limit.setter
    def adaptive_average_quality_upper_limit(self, adaptive_average_quality_upper_limit):
        r"""Sets the adaptive_average_quality_upper_limit of this PoliciesDisplayAdaptiveBitrateControlOptions.

        自适应视频平均质量上限。取值范围为[5-50]。默认：25。

        :param adaptive_average_quality_upper_limit: The adaptive_average_quality_upper_limit of this PoliciesDisplayAdaptiveBitrateControlOptions.
        :type adaptive_average_quality_upper_limit: int
        """
        self._adaptive_average_quality_upper_limit = adaptive_average_quality_upper_limit

    @property
    def adaptive_average_quality_increase_limit(self):
        r"""Gets the adaptive_average_quality_increase_limit of this PoliciesDisplayAdaptiveBitrateControlOptions.

        自适应视频平均质量增限。取值范围为[1-50]。默认：3。

        :return: The adaptive_average_quality_increase_limit of this PoliciesDisplayAdaptiveBitrateControlOptions.
        :rtype: int
        """
        return self._adaptive_average_quality_increase_limit

    @adaptive_average_quality_increase_limit.setter
    def adaptive_average_quality_increase_limit(self, adaptive_average_quality_increase_limit):
        r"""Sets the adaptive_average_quality_increase_limit of this PoliciesDisplayAdaptiveBitrateControlOptions.

        自适应视频平均质量增限。取值范围为[1-50]。默认：3。

        :param adaptive_average_quality_increase_limit: The adaptive_average_quality_increase_limit of this PoliciesDisplayAdaptiveBitrateControlOptions.
        :type adaptive_average_quality_increase_limit: int
        """
        self._adaptive_average_quality_increase_limit = adaptive_average_quality_increase_limit

    @property
    def adaptive_average_quality_decrease_limit(self):
        r"""Gets the adaptive_average_quality_decrease_limit of this PoliciesDisplayAdaptiveBitrateControlOptions.

        自适应视频平均质量减限。取值范围为[1-50]。默认：1。

        :return: The adaptive_average_quality_decrease_limit of this PoliciesDisplayAdaptiveBitrateControlOptions.
        :rtype: int
        """
        return self._adaptive_average_quality_decrease_limit

    @adaptive_average_quality_decrease_limit.setter
    def adaptive_average_quality_decrease_limit(self, adaptive_average_quality_decrease_limit):
        r"""Sets the adaptive_average_quality_decrease_limit of this PoliciesDisplayAdaptiveBitrateControlOptions.

        自适应视频平均质量减限。取值范围为[1-50]。默认：1。

        :param adaptive_average_quality_decrease_limit: The adaptive_average_quality_decrease_limit of this PoliciesDisplayAdaptiveBitrateControlOptions.
        :type adaptive_average_quality_decrease_limit: int
        """
        self._adaptive_average_quality_decrease_limit = adaptive_average_quality_decrease_limit

    @property
    def adaptive_min_quality_lower_limit(self):
        r"""Gets the adaptive_min_quality_lower_limit of this PoliciesDisplayAdaptiveBitrateControlOptions.

        自适应视频最低质量下限。取值范围为[5-69]。默认：25。

        :return: The adaptive_min_quality_lower_limit of this PoliciesDisplayAdaptiveBitrateControlOptions.
        :rtype: int
        """
        return self._adaptive_min_quality_lower_limit

    @adaptive_min_quality_lower_limit.setter
    def adaptive_min_quality_lower_limit(self, adaptive_min_quality_lower_limit):
        r"""Sets the adaptive_min_quality_lower_limit of this PoliciesDisplayAdaptiveBitrateControlOptions.

        自适应视频最低质量下限。取值范围为[5-69]。默认：25。

        :param adaptive_min_quality_lower_limit: The adaptive_min_quality_lower_limit of this PoliciesDisplayAdaptiveBitrateControlOptions.
        :type adaptive_min_quality_lower_limit: int
        """
        self._adaptive_min_quality_lower_limit = adaptive_min_quality_lower_limit

    @property
    def adaptive_min_quality_upper_limit(self):
        r"""Gets the adaptive_min_quality_upper_limit of this PoliciesDisplayAdaptiveBitrateControlOptions.

        自适应视频最低质量上限。取值范围为[5-69]。默认：30。

        :return: The adaptive_min_quality_upper_limit of this PoliciesDisplayAdaptiveBitrateControlOptions.
        :rtype: int
        """
        return self._adaptive_min_quality_upper_limit

    @adaptive_min_quality_upper_limit.setter
    def adaptive_min_quality_upper_limit(self, adaptive_min_quality_upper_limit):
        r"""Sets the adaptive_min_quality_upper_limit of this PoliciesDisplayAdaptiveBitrateControlOptions.

        自适应视频最低质量上限。取值范围为[5-69]。默认：30。

        :param adaptive_min_quality_upper_limit: The adaptive_min_quality_upper_limit of this PoliciesDisplayAdaptiveBitrateControlOptions.
        :type adaptive_min_quality_upper_limit: int
        """
        self._adaptive_min_quality_upper_limit = adaptive_min_quality_upper_limit

    @property
    def adaptive_min_quality_increase_limit(self):
        r"""Gets the adaptive_min_quality_increase_limit of this PoliciesDisplayAdaptiveBitrateControlOptions.

        自适应视频最低质量增限。取值范围为[1-50]。默认：3。

        :return: The adaptive_min_quality_increase_limit of this PoliciesDisplayAdaptiveBitrateControlOptions.
        :rtype: int
        """
        return self._adaptive_min_quality_increase_limit

    @adaptive_min_quality_increase_limit.setter
    def adaptive_min_quality_increase_limit(self, adaptive_min_quality_increase_limit):
        r"""Sets the adaptive_min_quality_increase_limit of this PoliciesDisplayAdaptiveBitrateControlOptions.

        自适应视频最低质量增限。取值范围为[1-50]。默认：3。

        :param adaptive_min_quality_increase_limit: The adaptive_min_quality_increase_limit of this PoliciesDisplayAdaptiveBitrateControlOptions.
        :type adaptive_min_quality_increase_limit: int
        """
        self._adaptive_min_quality_increase_limit = adaptive_min_quality_increase_limit

    @property
    def adaptive_min_quality_decrease_limit(self):
        r"""Gets the adaptive_min_quality_decrease_limit of this PoliciesDisplayAdaptiveBitrateControlOptions.

        自适应视频最低质量减限。取值范围为[1-50]。默认：1。

        :return: The adaptive_min_quality_decrease_limit of this PoliciesDisplayAdaptiveBitrateControlOptions.
        :rtype: int
        """
        return self._adaptive_min_quality_decrease_limit

    @adaptive_min_quality_decrease_limit.setter
    def adaptive_min_quality_decrease_limit(self, adaptive_min_quality_decrease_limit):
        r"""Sets the adaptive_min_quality_decrease_limit of this PoliciesDisplayAdaptiveBitrateControlOptions.

        自适应视频最低质量减限。取值范围为[1-50]。默认：1。

        :param adaptive_min_quality_decrease_limit: The adaptive_min_quality_decrease_limit of this PoliciesDisplayAdaptiveBitrateControlOptions.
        :type adaptive_min_quality_decrease_limit: int
        """
        self._adaptive_min_quality_decrease_limit = adaptive_min_quality_decrease_limit

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
        if not isinstance(other, PoliciesDisplayAdaptiveBitrateControlOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
