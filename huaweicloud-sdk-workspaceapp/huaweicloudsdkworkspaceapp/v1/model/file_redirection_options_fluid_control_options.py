# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FileRedirectionOptionsFluidControlOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'good_network_latency': 'int',
        'normal_network_latency': 'int',
        'poor_network_latency': 'int',
        'reducing_step': 'int',
        'slow_increasing_step': 'int',
        'quick_increasing_step': 'int',
        'start_speed': 'int',
        'test_block_size': 'int',
        'test_time_gap': 'int'
    }

    attribute_map = {
        'good_network_latency': 'good_network_latency',
        'normal_network_latency': 'normal_network_latency',
        'poor_network_latency': 'poor_network_latency',
        'reducing_step': 'reducing_step',
        'slow_increasing_step': 'slow_increasing_step',
        'quick_increasing_step': 'quick_increasing_step',
        'start_speed': 'start_speed',
        'test_block_size': 'test_block_size',
        'test_time_gap': 'test_time_gap'
    }

    def __init__(self, good_network_latency=None, normal_network_latency=None, poor_network_latency=None, reducing_step=None, slow_increasing_step=None, quick_increasing_step=None, start_speed=None, test_block_size=None, test_time_gap=None):
        """FileRedirectionOptionsFluidControlOptions

        The model defined in huaweicloud sdk

        :param good_network_latency: 网络优的延时阈值（ms）。取值范围为[1-1000]。默认：30。
        :type good_network_latency: int
        :param normal_network_latency: 网络一般的延时阈值（ms）。取值范围为[1-1000]。默认：70。
        :type normal_network_latency: int
        :param poor_network_latency: 网络差的延时阈值（ms）。取值范围为[1-1000]。默认：100。
        :type poor_network_latency: int
        :param reducing_step: 降速步伐（KB）。取值范围为[1-100]。默认：20。
        :type reducing_step: int
        :param slow_increasing_step: 慢增速步伐（KB）。取值范围为[1-100]。默认：10。
        :type slow_increasing_step: int
        :param quick_increasing_step: 快增速步伐（KB）。取值范围为[1-100]。默认：20。
        :type quick_increasing_step: int
        :param start_speed: 传输初始速度（KB/s）。取值范围为[1-10240]。默认：1024。
        :type start_speed: int
        :param test_block_size: 测速块大小（KB）。取值范围为[64-1024]。默认：64。
        :type test_block_size: int
        :param test_time_gap: 测速块时间间隔（ms）。取值范围为[1000-100000]。默认：10000。
        :type test_time_gap: int
        """
        
        

        self._good_network_latency = None
        self._normal_network_latency = None
        self._poor_network_latency = None
        self._reducing_step = None
        self._slow_increasing_step = None
        self._quick_increasing_step = None
        self._start_speed = None
        self._test_block_size = None
        self._test_time_gap = None
        self.discriminator = None

        if good_network_latency is not None:
            self.good_network_latency = good_network_latency
        if normal_network_latency is not None:
            self.normal_network_latency = normal_network_latency
        if poor_network_latency is not None:
            self.poor_network_latency = poor_network_latency
        if reducing_step is not None:
            self.reducing_step = reducing_step
        if slow_increasing_step is not None:
            self.slow_increasing_step = slow_increasing_step
        if quick_increasing_step is not None:
            self.quick_increasing_step = quick_increasing_step
        if start_speed is not None:
            self.start_speed = start_speed
        if test_block_size is not None:
            self.test_block_size = test_block_size
        if test_time_gap is not None:
            self.test_time_gap = test_time_gap

    @property
    def good_network_latency(self):
        """Gets the good_network_latency of this FileRedirectionOptionsFluidControlOptions.

        网络优的延时阈值（ms）。取值范围为[1-1000]。默认：30。

        :return: The good_network_latency of this FileRedirectionOptionsFluidControlOptions.
        :rtype: int
        """
        return self._good_network_latency

    @good_network_latency.setter
    def good_network_latency(self, good_network_latency):
        """Sets the good_network_latency of this FileRedirectionOptionsFluidControlOptions.

        网络优的延时阈值（ms）。取值范围为[1-1000]。默认：30。

        :param good_network_latency: The good_network_latency of this FileRedirectionOptionsFluidControlOptions.
        :type good_network_latency: int
        """
        self._good_network_latency = good_network_latency

    @property
    def normal_network_latency(self):
        """Gets the normal_network_latency of this FileRedirectionOptionsFluidControlOptions.

        网络一般的延时阈值（ms）。取值范围为[1-1000]。默认：70。

        :return: The normal_network_latency of this FileRedirectionOptionsFluidControlOptions.
        :rtype: int
        """
        return self._normal_network_latency

    @normal_network_latency.setter
    def normal_network_latency(self, normal_network_latency):
        """Sets the normal_network_latency of this FileRedirectionOptionsFluidControlOptions.

        网络一般的延时阈值（ms）。取值范围为[1-1000]。默认：70。

        :param normal_network_latency: The normal_network_latency of this FileRedirectionOptionsFluidControlOptions.
        :type normal_network_latency: int
        """
        self._normal_network_latency = normal_network_latency

    @property
    def poor_network_latency(self):
        """Gets the poor_network_latency of this FileRedirectionOptionsFluidControlOptions.

        网络差的延时阈值（ms）。取值范围为[1-1000]。默认：100。

        :return: The poor_network_latency of this FileRedirectionOptionsFluidControlOptions.
        :rtype: int
        """
        return self._poor_network_latency

    @poor_network_latency.setter
    def poor_network_latency(self, poor_network_latency):
        """Sets the poor_network_latency of this FileRedirectionOptionsFluidControlOptions.

        网络差的延时阈值（ms）。取值范围为[1-1000]。默认：100。

        :param poor_network_latency: The poor_network_latency of this FileRedirectionOptionsFluidControlOptions.
        :type poor_network_latency: int
        """
        self._poor_network_latency = poor_network_latency

    @property
    def reducing_step(self):
        """Gets the reducing_step of this FileRedirectionOptionsFluidControlOptions.

        降速步伐（KB）。取值范围为[1-100]。默认：20。

        :return: The reducing_step of this FileRedirectionOptionsFluidControlOptions.
        :rtype: int
        """
        return self._reducing_step

    @reducing_step.setter
    def reducing_step(self, reducing_step):
        """Sets the reducing_step of this FileRedirectionOptionsFluidControlOptions.

        降速步伐（KB）。取值范围为[1-100]。默认：20。

        :param reducing_step: The reducing_step of this FileRedirectionOptionsFluidControlOptions.
        :type reducing_step: int
        """
        self._reducing_step = reducing_step

    @property
    def slow_increasing_step(self):
        """Gets the slow_increasing_step of this FileRedirectionOptionsFluidControlOptions.

        慢增速步伐（KB）。取值范围为[1-100]。默认：10。

        :return: The slow_increasing_step of this FileRedirectionOptionsFluidControlOptions.
        :rtype: int
        """
        return self._slow_increasing_step

    @slow_increasing_step.setter
    def slow_increasing_step(self, slow_increasing_step):
        """Sets the slow_increasing_step of this FileRedirectionOptionsFluidControlOptions.

        慢增速步伐（KB）。取值范围为[1-100]。默认：10。

        :param slow_increasing_step: The slow_increasing_step of this FileRedirectionOptionsFluidControlOptions.
        :type slow_increasing_step: int
        """
        self._slow_increasing_step = slow_increasing_step

    @property
    def quick_increasing_step(self):
        """Gets the quick_increasing_step of this FileRedirectionOptionsFluidControlOptions.

        快增速步伐（KB）。取值范围为[1-100]。默认：20。

        :return: The quick_increasing_step of this FileRedirectionOptionsFluidControlOptions.
        :rtype: int
        """
        return self._quick_increasing_step

    @quick_increasing_step.setter
    def quick_increasing_step(self, quick_increasing_step):
        """Sets the quick_increasing_step of this FileRedirectionOptionsFluidControlOptions.

        快增速步伐（KB）。取值范围为[1-100]。默认：20。

        :param quick_increasing_step: The quick_increasing_step of this FileRedirectionOptionsFluidControlOptions.
        :type quick_increasing_step: int
        """
        self._quick_increasing_step = quick_increasing_step

    @property
    def start_speed(self):
        """Gets the start_speed of this FileRedirectionOptionsFluidControlOptions.

        传输初始速度（KB/s）。取值范围为[1-10240]。默认：1024。

        :return: The start_speed of this FileRedirectionOptionsFluidControlOptions.
        :rtype: int
        """
        return self._start_speed

    @start_speed.setter
    def start_speed(self, start_speed):
        """Sets the start_speed of this FileRedirectionOptionsFluidControlOptions.

        传输初始速度（KB/s）。取值范围为[1-10240]。默认：1024。

        :param start_speed: The start_speed of this FileRedirectionOptionsFluidControlOptions.
        :type start_speed: int
        """
        self._start_speed = start_speed

    @property
    def test_block_size(self):
        """Gets the test_block_size of this FileRedirectionOptionsFluidControlOptions.

        测速块大小（KB）。取值范围为[64-1024]。默认：64。

        :return: The test_block_size of this FileRedirectionOptionsFluidControlOptions.
        :rtype: int
        """
        return self._test_block_size

    @test_block_size.setter
    def test_block_size(self, test_block_size):
        """Sets the test_block_size of this FileRedirectionOptionsFluidControlOptions.

        测速块大小（KB）。取值范围为[64-1024]。默认：64。

        :param test_block_size: The test_block_size of this FileRedirectionOptionsFluidControlOptions.
        :type test_block_size: int
        """
        self._test_block_size = test_block_size

    @property
    def test_time_gap(self):
        """Gets the test_time_gap of this FileRedirectionOptionsFluidControlOptions.

        测速块时间间隔（ms）。取值范围为[1000-100000]。默认：10000。

        :return: The test_time_gap of this FileRedirectionOptionsFluidControlOptions.
        :rtype: int
        """
        return self._test_time_gap

    @test_time_gap.setter
    def test_time_gap(self, test_time_gap):
        """Sets the test_time_gap of this FileRedirectionOptionsFluidControlOptions.

        测速块时间间隔（ms）。取值范围为[1000-100000]。默认：10000。

        :param test_time_gap: The test_time_gap of this FileRedirectionOptionsFluidControlOptions.
        :type test_time_gap: int
        """
        self._test_time_gap = test_time_gap

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
        if not isinstance(other, FileRedirectionOptionsFluidControlOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
