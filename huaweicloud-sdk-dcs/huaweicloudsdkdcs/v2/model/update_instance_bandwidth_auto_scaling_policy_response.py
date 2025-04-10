# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateInstanceBandwidthAutoScalingPolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'window_size': 'int',
        'bandwidth_usage_upper_threshold': 'int',
        'scale_out_cooldown': 'int',
        'scale_in_enabled': 'bool',
        'bandwidth_usage_lower_threshold': 'int',
        'scale_in_cooldown': 'int'
    }

    attribute_map = {
        'window_size': 'window_size',
        'bandwidth_usage_upper_threshold': 'bandwidth_usage_upper_threshold',
        'scale_out_cooldown': 'scale_out_cooldown',
        'scale_in_enabled': 'scale_in_enabled',
        'bandwidth_usage_lower_threshold': 'bandwidth_usage_lower_threshold',
        'scale_in_cooldown': 'scale_in_cooldown'
    }

    def __init__(self, window_size=None, bandwidth_usage_upper_threshold=None, scale_out_cooldown=None, scale_in_enabled=None, bandwidth_usage_lower_threshold=None, scale_in_cooldown=None):
        r"""UpdateInstanceBandwidthAutoScalingPolicyResponse

        The model defined in huaweicloud sdk

        :param window_size: 带宽弹性的观测窗口，单位：分钟。支持的取值：1、5、10、15、30。
        :type window_size: int
        :param bandwidth_usage_upper_threshold: 触发带宽自动扩展的带宽平均使用率阈值，单位：百分比。支持的取值：50、60、70、80、90、95。
        :type bandwidth_usage_upper_threshold: int
        :param scale_out_cooldown: 带宽扩展操作的静默时间（两次带宽扩展操作之间的最小间隔时间），单位：秒。 默认值：0。取值范围：0~86400。 
        :type scale_out_cooldown: int
        :param scale_in_enabled: 是否启用带宽自动回缩。默认值：false。该参数暂未启用。
        :type scale_in_enabled: bool
        :param bandwidth_usage_lower_threshold: 触发带宽自动回缩的带宽平均使用率阈值，单位：百分比。支持的取值：10、20、30。该参数暂未启用。
        :type bandwidth_usage_lower_threshold: int
        :param scale_in_cooldown: 带宽回缩操作的静默时间（两次带宽回缩操作之间的最小间隔时间），单位：秒。该参数暂未启用。 默认值：300。取值范围：0~86400。 
        :type scale_in_cooldown: int
        """
        
        super(UpdateInstanceBandwidthAutoScalingPolicyResponse, self).__init__()

        self._window_size = None
        self._bandwidth_usage_upper_threshold = None
        self._scale_out_cooldown = None
        self._scale_in_enabled = None
        self._bandwidth_usage_lower_threshold = None
        self._scale_in_cooldown = None
        self.discriminator = None

        self.window_size = window_size
        self.bandwidth_usage_upper_threshold = bandwidth_usage_upper_threshold
        self.scale_out_cooldown = scale_out_cooldown
        if scale_in_enabled is not None:
            self.scale_in_enabled = scale_in_enabled
        if bandwidth_usage_lower_threshold is not None:
            self.bandwidth_usage_lower_threshold = bandwidth_usage_lower_threshold
        if scale_in_cooldown is not None:
            self.scale_in_cooldown = scale_in_cooldown

    @property
    def window_size(self):
        r"""Gets the window_size of this UpdateInstanceBandwidthAutoScalingPolicyResponse.

        带宽弹性的观测窗口，单位：分钟。支持的取值：1、5、10、15、30。

        :return: The window_size of this UpdateInstanceBandwidthAutoScalingPolicyResponse.
        :rtype: int
        """
        return self._window_size

    @window_size.setter
    def window_size(self, window_size):
        r"""Sets the window_size of this UpdateInstanceBandwidthAutoScalingPolicyResponse.

        带宽弹性的观测窗口，单位：分钟。支持的取值：1、5、10、15、30。

        :param window_size: The window_size of this UpdateInstanceBandwidthAutoScalingPolicyResponse.
        :type window_size: int
        """
        self._window_size = window_size

    @property
    def bandwidth_usage_upper_threshold(self):
        r"""Gets the bandwidth_usage_upper_threshold of this UpdateInstanceBandwidthAutoScalingPolicyResponse.

        触发带宽自动扩展的带宽平均使用率阈值，单位：百分比。支持的取值：50、60、70、80、90、95。

        :return: The bandwidth_usage_upper_threshold of this UpdateInstanceBandwidthAutoScalingPolicyResponse.
        :rtype: int
        """
        return self._bandwidth_usage_upper_threshold

    @bandwidth_usage_upper_threshold.setter
    def bandwidth_usage_upper_threshold(self, bandwidth_usage_upper_threshold):
        r"""Sets the bandwidth_usage_upper_threshold of this UpdateInstanceBandwidthAutoScalingPolicyResponse.

        触发带宽自动扩展的带宽平均使用率阈值，单位：百分比。支持的取值：50、60、70、80、90、95。

        :param bandwidth_usage_upper_threshold: The bandwidth_usage_upper_threshold of this UpdateInstanceBandwidthAutoScalingPolicyResponse.
        :type bandwidth_usage_upper_threshold: int
        """
        self._bandwidth_usage_upper_threshold = bandwidth_usage_upper_threshold

    @property
    def scale_out_cooldown(self):
        r"""Gets the scale_out_cooldown of this UpdateInstanceBandwidthAutoScalingPolicyResponse.

        带宽扩展操作的静默时间（两次带宽扩展操作之间的最小间隔时间），单位：秒。 默认值：0。取值范围：0~86400。 

        :return: The scale_out_cooldown of this UpdateInstanceBandwidthAutoScalingPolicyResponse.
        :rtype: int
        """
        return self._scale_out_cooldown

    @scale_out_cooldown.setter
    def scale_out_cooldown(self, scale_out_cooldown):
        r"""Sets the scale_out_cooldown of this UpdateInstanceBandwidthAutoScalingPolicyResponse.

        带宽扩展操作的静默时间（两次带宽扩展操作之间的最小间隔时间），单位：秒。 默认值：0。取值范围：0~86400。 

        :param scale_out_cooldown: The scale_out_cooldown of this UpdateInstanceBandwidthAutoScalingPolicyResponse.
        :type scale_out_cooldown: int
        """
        self._scale_out_cooldown = scale_out_cooldown

    @property
    def scale_in_enabled(self):
        r"""Gets the scale_in_enabled of this UpdateInstanceBandwidthAutoScalingPolicyResponse.

        是否启用带宽自动回缩。默认值：false。该参数暂未启用。

        :return: The scale_in_enabled of this UpdateInstanceBandwidthAutoScalingPolicyResponse.
        :rtype: bool
        """
        return self._scale_in_enabled

    @scale_in_enabled.setter
    def scale_in_enabled(self, scale_in_enabled):
        r"""Sets the scale_in_enabled of this UpdateInstanceBandwidthAutoScalingPolicyResponse.

        是否启用带宽自动回缩。默认值：false。该参数暂未启用。

        :param scale_in_enabled: The scale_in_enabled of this UpdateInstanceBandwidthAutoScalingPolicyResponse.
        :type scale_in_enabled: bool
        """
        self._scale_in_enabled = scale_in_enabled

    @property
    def bandwidth_usage_lower_threshold(self):
        r"""Gets the bandwidth_usage_lower_threshold of this UpdateInstanceBandwidthAutoScalingPolicyResponse.

        触发带宽自动回缩的带宽平均使用率阈值，单位：百分比。支持的取值：10、20、30。该参数暂未启用。

        :return: The bandwidth_usage_lower_threshold of this UpdateInstanceBandwidthAutoScalingPolicyResponse.
        :rtype: int
        """
        return self._bandwidth_usage_lower_threshold

    @bandwidth_usage_lower_threshold.setter
    def bandwidth_usage_lower_threshold(self, bandwidth_usage_lower_threshold):
        r"""Sets the bandwidth_usage_lower_threshold of this UpdateInstanceBandwidthAutoScalingPolicyResponse.

        触发带宽自动回缩的带宽平均使用率阈值，单位：百分比。支持的取值：10、20、30。该参数暂未启用。

        :param bandwidth_usage_lower_threshold: The bandwidth_usage_lower_threshold of this UpdateInstanceBandwidthAutoScalingPolicyResponse.
        :type bandwidth_usage_lower_threshold: int
        """
        self._bandwidth_usage_lower_threshold = bandwidth_usage_lower_threshold

    @property
    def scale_in_cooldown(self):
        r"""Gets the scale_in_cooldown of this UpdateInstanceBandwidthAutoScalingPolicyResponse.

        带宽回缩操作的静默时间（两次带宽回缩操作之间的最小间隔时间），单位：秒。该参数暂未启用。 默认值：300。取值范围：0~86400。 

        :return: The scale_in_cooldown of this UpdateInstanceBandwidthAutoScalingPolicyResponse.
        :rtype: int
        """
        return self._scale_in_cooldown

    @scale_in_cooldown.setter
    def scale_in_cooldown(self, scale_in_cooldown):
        r"""Sets the scale_in_cooldown of this UpdateInstanceBandwidthAutoScalingPolicyResponse.

        带宽回缩操作的静默时间（两次带宽回缩操作之间的最小间隔时间），单位：秒。该参数暂未启用。 默认值：300。取值范围：0~86400。 

        :param scale_in_cooldown: The scale_in_cooldown of this UpdateInstanceBandwidthAutoScalingPolicyResponse.
        :type scale_in_cooldown: int
        """
        self._scale_in_cooldown = scale_in_cooldown

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
        if not isinstance(other, UpdateInstanceBandwidthAutoScalingPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
