# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAutoScalingPolicyRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'monitor_cycle': 'int',
        'silence_cycle': 'int',
        'enlarge_threshold': 'int',
        'max_flavor': 'str',
        'reduce_enabled': 'bool',
        'max_read_only_count': 'int',
        'read_only_weight': 'int',
        'scaling_strategy': 'ScalingStrategyReqInfo'
    }

    attribute_map = {
        'status': 'status',
        'monitor_cycle': 'monitor_cycle',
        'silence_cycle': 'silence_cycle',
        'enlarge_threshold': 'enlarge_threshold',
        'max_flavor': 'max_flavor',
        'reduce_enabled': 'reduce_enabled',
        'max_read_only_count': 'max_read_only_count',
        'read_only_weight': 'read_only_weight',
        'scaling_strategy': 'scaling_strategy'
    }

    def __init__(self, status=None, monitor_cycle=None, silence_cycle=None, enlarge_threshold=None, max_flavor=None, reduce_enabled=None, max_read_only_count=None, read_only_weight=None, scaling_strategy=None):
        r"""UpdateAutoScalingPolicyRequestBody

        The model defined in huaweicloud sdk

        :param status: 自动变配开关状态。  取值：  - ON：开启。 - OFF：关闭。
        :type status: str
        :param monitor_cycle: 监测周期（单位：秒）。 在整个观测窗口期内，若CPU平均使用率大于等于设定值，则在观测窗口结束后，进行扩容。  取值范围：300、600、900、1800。  status为ON时必填。
        :type monitor_cycle: int
        :param silence_cycle: 静默周期（单位：秒）。 两次自动扩容或自动回缩的最小间隔时间。  取值范围：300、600、1800、3600、7200、10800、86400、604800。  status为ON时必填。
        :type silence_cycle: int
        :param enlarge_threshold: CPU平均使用率（百分比数值）。  取值范围：50-100。  status为ON时必填。
        :type enlarge_threshold: int
        :param max_flavor: 扩容规格上限。开启扩缩规格时必填。
        :type max_flavor: str
        :param reduce_enabled: 是否开启自动回缩。开启自动变配时必填。 - true：是。 - false：否。
        :type reduce_enabled: bool
        :param max_read_only_count: 只读节点数量上限。开启增删只读节点时必填。
        :type max_read_only_count: int
        :param read_only_weight: 只读节点读写分离权重。开启增删只读节点时必填。
        :type read_only_weight: int
        :param scaling_strategy: 
        :type scaling_strategy: :class:`huaweicloudsdkgaussdb.v3.ScalingStrategyReqInfo`
        """
        
        

        self._status = None
        self._monitor_cycle = None
        self._silence_cycle = None
        self._enlarge_threshold = None
        self._max_flavor = None
        self._reduce_enabled = None
        self._max_read_only_count = None
        self._read_only_weight = None
        self._scaling_strategy = None
        self.discriminator = None

        self.status = status
        if monitor_cycle is not None:
            self.monitor_cycle = monitor_cycle
        if silence_cycle is not None:
            self.silence_cycle = silence_cycle
        if enlarge_threshold is not None:
            self.enlarge_threshold = enlarge_threshold
        if max_flavor is not None:
            self.max_flavor = max_flavor
        if reduce_enabled is not None:
            self.reduce_enabled = reduce_enabled
        if max_read_only_count is not None:
            self.max_read_only_count = max_read_only_count
        if read_only_weight is not None:
            self.read_only_weight = read_only_weight
        self.scaling_strategy = scaling_strategy

    @property
    def status(self):
        r"""Gets the status of this UpdateAutoScalingPolicyRequestBody.

        自动变配开关状态。  取值：  - ON：开启。 - OFF：关闭。

        :return: The status of this UpdateAutoScalingPolicyRequestBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UpdateAutoScalingPolicyRequestBody.

        自动变配开关状态。  取值：  - ON：开启。 - OFF：关闭。

        :param status: The status of this UpdateAutoScalingPolicyRequestBody.
        :type status: str
        """
        self._status = status

    @property
    def monitor_cycle(self):
        r"""Gets the monitor_cycle of this UpdateAutoScalingPolicyRequestBody.

        监测周期（单位：秒）。 在整个观测窗口期内，若CPU平均使用率大于等于设定值，则在观测窗口结束后，进行扩容。  取值范围：300、600、900、1800。  status为ON时必填。

        :return: The monitor_cycle of this UpdateAutoScalingPolicyRequestBody.
        :rtype: int
        """
        return self._monitor_cycle

    @monitor_cycle.setter
    def monitor_cycle(self, monitor_cycle):
        r"""Sets the monitor_cycle of this UpdateAutoScalingPolicyRequestBody.

        监测周期（单位：秒）。 在整个观测窗口期内，若CPU平均使用率大于等于设定值，则在观测窗口结束后，进行扩容。  取值范围：300、600、900、1800。  status为ON时必填。

        :param monitor_cycle: The monitor_cycle of this UpdateAutoScalingPolicyRequestBody.
        :type monitor_cycle: int
        """
        self._monitor_cycle = monitor_cycle

    @property
    def silence_cycle(self):
        r"""Gets the silence_cycle of this UpdateAutoScalingPolicyRequestBody.

        静默周期（单位：秒）。 两次自动扩容或自动回缩的最小间隔时间。  取值范围：300、600、1800、3600、7200、10800、86400、604800。  status为ON时必填。

        :return: The silence_cycle of this UpdateAutoScalingPolicyRequestBody.
        :rtype: int
        """
        return self._silence_cycle

    @silence_cycle.setter
    def silence_cycle(self, silence_cycle):
        r"""Sets the silence_cycle of this UpdateAutoScalingPolicyRequestBody.

        静默周期（单位：秒）。 两次自动扩容或自动回缩的最小间隔时间。  取值范围：300、600、1800、3600、7200、10800、86400、604800。  status为ON时必填。

        :param silence_cycle: The silence_cycle of this UpdateAutoScalingPolicyRequestBody.
        :type silence_cycle: int
        """
        self._silence_cycle = silence_cycle

    @property
    def enlarge_threshold(self):
        r"""Gets the enlarge_threshold of this UpdateAutoScalingPolicyRequestBody.

        CPU平均使用率（百分比数值）。  取值范围：50-100。  status为ON时必填。

        :return: The enlarge_threshold of this UpdateAutoScalingPolicyRequestBody.
        :rtype: int
        """
        return self._enlarge_threshold

    @enlarge_threshold.setter
    def enlarge_threshold(self, enlarge_threshold):
        r"""Sets the enlarge_threshold of this UpdateAutoScalingPolicyRequestBody.

        CPU平均使用率（百分比数值）。  取值范围：50-100。  status为ON时必填。

        :param enlarge_threshold: The enlarge_threshold of this UpdateAutoScalingPolicyRequestBody.
        :type enlarge_threshold: int
        """
        self._enlarge_threshold = enlarge_threshold

    @property
    def max_flavor(self):
        r"""Gets the max_flavor of this UpdateAutoScalingPolicyRequestBody.

        扩容规格上限。开启扩缩规格时必填。

        :return: The max_flavor of this UpdateAutoScalingPolicyRequestBody.
        :rtype: str
        """
        return self._max_flavor

    @max_flavor.setter
    def max_flavor(self, max_flavor):
        r"""Sets the max_flavor of this UpdateAutoScalingPolicyRequestBody.

        扩容规格上限。开启扩缩规格时必填。

        :param max_flavor: The max_flavor of this UpdateAutoScalingPolicyRequestBody.
        :type max_flavor: str
        """
        self._max_flavor = max_flavor

    @property
    def reduce_enabled(self):
        r"""Gets the reduce_enabled of this UpdateAutoScalingPolicyRequestBody.

        是否开启自动回缩。开启自动变配时必填。 - true：是。 - false：否。

        :return: The reduce_enabled of this UpdateAutoScalingPolicyRequestBody.
        :rtype: bool
        """
        return self._reduce_enabled

    @reduce_enabled.setter
    def reduce_enabled(self, reduce_enabled):
        r"""Sets the reduce_enabled of this UpdateAutoScalingPolicyRequestBody.

        是否开启自动回缩。开启自动变配时必填。 - true：是。 - false：否。

        :param reduce_enabled: The reduce_enabled of this UpdateAutoScalingPolicyRequestBody.
        :type reduce_enabled: bool
        """
        self._reduce_enabled = reduce_enabled

    @property
    def max_read_only_count(self):
        r"""Gets the max_read_only_count of this UpdateAutoScalingPolicyRequestBody.

        只读节点数量上限。开启增删只读节点时必填。

        :return: The max_read_only_count of this UpdateAutoScalingPolicyRequestBody.
        :rtype: int
        """
        return self._max_read_only_count

    @max_read_only_count.setter
    def max_read_only_count(self, max_read_only_count):
        r"""Sets the max_read_only_count of this UpdateAutoScalingPolicyRequestBody.

        只读节点数量上限。开启增删只读节点时必填。

        :param max_read_only_count: The max_read_only_count of this UpdateAutoScalingPolicyRequestBody.
        :type max_read_only_count: int
        """
        self._max_read_only_count = max_read_only_count

    @property
    def read_only_weight(self):
        r"""Gets the read_only_weight of this UpdateAutoScalingPolicyRequestBody.

        只读节点读写分离权重。开启增删只读节点时必填。

        :return: The read_only_weight of this UpdateAutoScalingPolicyRequestBody.
        :rtype: int
        """
        return self._read_only_weight

    @read_only_weight.setter
    def read_only_weight(self, read_only_weight):
        r"""Sets the read_only_weight of this UpdateAutoScalingPolicyRequestBody.

        只读节点读写分离权重。开启增删只读节点时必填。

        :param read_only_weight: The read_only_weight of this UpdateAutoScalingPolicyRequestBody.
        :type read_only_weight: int
        """
        self._read_only_weight = read_only_weight

    @property
    def scaling_strategy(self):
        r"""Gets the scaling_strategy of this UpdateAutoScalingPolicyRequestBody.

        :return: The scaling_strategy of this UpdateAutoScalingPolicyRequestBody.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ScalingStrategyReqInfo`
        """
        return self._scaling_strategy

    @scaling_strategy.setter
    def scaling_strategy(self, scaling_strategy):
        r"""Sets the scaling_strategy of this UpdateAutoScalingPolicyRequestBody.

        :param scaling_strategy: The scaling_strategy of this UpdateAutoScalingPolicyRequestBody.
        :type scaling_strategy: :class:`huaweicloudsdkgaussdb.v3.ScalingStrategyReqInfo`
        """
        self._scaling_strategy = scaling_strategy

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
        if not isinstance(other, UpdateAutoScalingPolicyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
