# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAutoScalingPolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'instance_id': 'str',
        'instance_name': 'str',
        'status': 'str',
        'monitor_cycle': 'int',
        'silence_cycle': 'int',
        'enlarge_threshold': 'int',
        'max_flavor': 'str',
        'reduce_enabled': 'bool',
        'min_flavor': 'str',
        'silence_start_at': 'str',
        'scaling_strategy': 'ScalingStrategyInfo',
        'max_read_only_count': 'int',
        'min_read_only_count': 'int',
        'read_only_weight': 'int'
    }

    attribute_map = {
        'id': 'id',
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'status': 'status',
        'monitor_cycle': 'monitor_cycle',
        'silence_cycle': 'silence_cycle',
        'enlarge_threshold': 'enlarge_threshold',
        'max_flavor': 'max_flavor',
        'reduce_enabled': 'reduce_enabled',
        'min_flavor': 'min_flavor',
        'silence_start_at': 'silence_start_at',
        'scaling_strategy': 'scaling_strategy',
        'max_read_only_count': 'max_read_only_count',
        'min_read_only_count': 'min_read_only_count',
        'read_only_weight': 'read_only_weight'
    }

    def __init__(self, id=None, instance_id=None, instance_name=None, status=None, monitor_cycle=None, silence_cycle=None, enlarge_threshold=None, max_flavor=None, reduce_enabled=None, min_flavor=None, silence_start_at=None, scaling_strategy=None, max_read_only_count=None, min_read_only_count=None, read_only_weight=None):
        """ShowAutoScalingPolicyResponse

        The model defined in huaweicloud sdk

        :param id: 自动变配策略ID。
        :type id: str
        :param instance_id: 实例ID。
        :type instance_id: str
        :param instance_name: 实例名称。
        :type instance_name: str
        :param status: 自动变配开关状态。  取值：  - ON：已开启 - OFF：已关闭
        :type status: str
        :param monitor_cycle: 监测周期（单位：秒）。 在整个观测窗口期内，若CPU平均使用率大于等于设定值，则在观测窗口结束后，进行扩容。
        :type monitor_cycle: int
        :param silence_cycle: 静默周期（单位：秒）。 两次自动扩容或自动回缩的最小间隔时间。
        :type silence_cycle: int
        :param enlarge_threshold: 扩容阈值（百分比数值），指CPU平均使用率。
        :type enlarge_threshold: int
        :param max_flavor: 扩容规格上限。
        :type max_flavor: str
        :param reduce_enabled: 自动回缩开关状态。  取值：  - true：已开启 - false：已关闭
        :type reduce_enabled: bool
        :param min_flavor: 缩容规格下限。
        :type min_flavor: str
        :param silence_start_at: 静默期开始时间（上一次变更结束时间）。  格式为\&quot;yyyy-mm-ddThh:mm:ssZ\&quot;。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type silence_start_at: str
        :param scaling_strategy: 
        :type scaling_strategy: :class:`huaweicloudsdkgaussdb.v3.ScalingStrategyInfo`
        :param max_read_only_count: 只读节点数量上限。
        :type max_read_only_count: int
        :param min_read_only_count: 只读节点数量下限。
        :type min_read_only_count: int
        :param read_only_weight: 只读节点读写分离权重。
        :type read_only_weight: int
        """
        
        super(ShowAutoScalingPolicyResponse, self).__init__()

        self._id = None
        self._instance_id = None
        self._instance_name = None
        self._status = None
        self._monitor_cycle = None
        self._silence_cycle = None
        self._enlarge_threshold = None
        self._max_flavor = None
        self._reduce_enabled = None
        self._min_flavor = None
        self._silence_start_at = None
        self._scaling_strategy = None
        self._max_read_only_count = None
        self._min_read_only_count = None
        self._read_only_weight = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if status is not None:
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
        if min_flavor is not None:
            self.min_flavor = min_flavor
        if silence_start_at is not None:
            self.silence_start_at = silence_start_at
        if scaling_strategy is not None:
            self.scaling_strategy = scaling_strategy
        if max_read_only_count is not None:
            self.max_read_only_count = max_read_only_count
        if min_read_only_count is not None:
            self.min_read_only_count = min_read_only_count
        if read_only_weight is not None:
            self.read_only_weight = read_only_weight

    @property
    def id(self):
        """Gets the id of this ShowAutoScalingPolicyResponse.

        自动变配策略ID。

        :return: The id of this ShowAutoScalingPolicyResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowAutoScalingPolicyResponse.

        自动变配策略ID。

        :param id: The id of this ShowAutoScalingPolicyResponse.
        :type id: str
        """
        self._id = id

    @property
    def instance_id(self):
        """Gets the instance_id of this ShowAutoScalingPolicyResponse.

        实例ID。

        :return: The instance_id of this ShowAutoScalingPolicyResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ShowAutoScalingPolicyResponse.

        实例ID。

        :param instance_id: The instance_id of this ShowAutoScalingPolicyResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        """Gets the instance_name of this ShowAutoScalingPolicyResponse.

        实例名称。

        :return: The instance_name of this ShowAutoScalingPolicyResponse.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this ShowAutoScalingPolicyResponse.

        实例名称。

        :param instance_name: The instance_name of this ShowAutoScalingPolicyResponse.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def status(self):
        """Gets the status of this ShowAutoScalingPolicyResponse.

        自动变配开关状态。  取值：  - ON：已开启 - OFF：已关闭

        :return: The status of this ShowAutoScalingPolicyResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowAutoScalingPolicyResponse.

        自动变配开关状态。  取值：  - ON：已开启 - OFF：已关闭

        :param status: The status of this ShowAutoScalingPolicyResponse.
        :type status: str
        """
        self._status = status

    @property
    def monitor_cycle(self):
        """Gets the monitor_cycle of this ShowAutoScalingPolicyResponse.

        监测周期（单位：秒）。 在整个观测窗口期内，若CPU平均使用率大于等于设定值，则在观测窗口结束后，进行扩容。

        :return: The monitor_cycle of this ShowAutoScalingPolicyResponse.
        :rtype: int
        """
        return self._monitor_cycle

    @monitor_cycle.setter
    def monitor_cycle(self, monitor_cycle):
        """Sets the monitor_cycle of this ShowAutoScalingPolicyResponse.

        监测周期（单位：秒）。 在整个观测窗口期内，若CPU平均使用率大于等于设定值，则在观测窗口结束后，进行扩容。

        :param monitor_cycle: The monitor_cycle of this ShowAutoScalingPolicyResponse.
        :type monitor_cycle: int
        """
        self._monitor_cycle = monitor_cycle

    @property
    def silence_cycle(self):
        """Gets the silence_cycle of this ShowAutoScalingPolicyResponse.

        静默周期（单位：秒）。 两次自动扩容或自动回缩的最小间隔时间。

        :return: The silence_cycle of this ShowAutoScalingPolicyResponse.
        :rtype: int
        """
        return self._silence_cycle

    @silence_cycle.setter
    def silence_cycle(self, silence_cycle):
        """Sets the silence_cycle of this ShowAutoScalingPolicyResponse.

        静默周期（单位：秒）。 两次自动扩容或自动回缩的最小间隔时间。

        :param silence_cycle: The silence_cycle of this ShowAutoScalingPolicyResponse.
        :type silence_cycle: int
        """
        self._silence_cycle = silence_cycle

    @property
    def enlarge_threshold(self):
        """Gets the enlarge_threshold of this ShowAutoScalingPolicyResponse.

        扩容阈值（百分比数值），指CPU平均使用率。

        :return: The enlarge_threshold of this ShowAutoScalingPolicyResponse.
        :rtype: int
        """
        return self._enlarge_threshold

    @enlarge_threshold.setter
    def enlarge_threshold(self, enlarge_threshold):
        """Sets the enlarge_threshold of this ShowAutoScalingPolicyResponse.

        扩容阈值（百分比数值），指CPU平均使用率。

        :param enlarge_threshold: The enlarge_threshold of this ShowAutoScalingPolicyResponse.
        :type enlarge_threshold: int
        """
        self._enlarge_threshold = enlarge_threshold

    @property
    def max_flavor(self):
        """Gets the max_flavor of this ShowAutoScalingPolicyResponse.

        扩容规格上限。

        :return: The max_flavor of this ShowAutoScalingPolicyResponse.
        :rtype: str
        """
        return self._max_flavor

    @max_flavor.setter
    def max_flavor(self, max_flavor):
        """Sets the max_flavor of this ShowAutoScalingPolicyResponse.

        扩容规格上限。

        :param max_flavor: The max_flavor of this ShowAutoScalingPolicyResponse.
        :type max_flavor: str
        """
        self._max_flavor = max_flavor

    @property
    def reduce_enabled(self):
        """Gets the reduce_enabled of this ShowAutoScalingPolicyResponse.

        自动回缩开关状态。  取值：  - true：已开启 - false：已关闭

        :return: The reduce_enabled of this ShowAutoScalingPolicyResponse.
        :rtype: bool
        """
        return self._reduce_enabled

    @reduce_enabled.setter
    def reduce_enabled(self, reduce_enabled):
        """Sets the reduce_enabled of this ShowAutoScalingPolicyResponse.

        自动回缩开关状态。  取值：  - true：已开启 - false：已关闭

        :param reduce_enabled: The reduce_enabled of this ShowAutoScalingPolicyResponse.
        :type reduce_enabled: bool
        """
        self._reduce_enabled = reduce_enabled

    @property
    def min_flavor(self):
        """Gets the min_flavor of this ShowAutoScalingPolicyResponse.

        缩容规格下限。

        :return: The min_flavor of this ShowAutoScalingPolicyResponse.
        :rtype: str
        """
        return self._min_flavor

    @min_flavor.setter
    def min_flavor(self, min_flavor):
        """Sets the min_flavor of this ShowAutoScalingPolicyResponse.

        缩容规格下限。

        :param min_flavor: The min_flavor of this ShowAutoScalingPolicyResponse.
        :type min_flavor: str
        """
        self._min_flavor = min_flavor

    @property
    def silence_start_at(self):
        """Gets the silence_start_at of this ShowAutoScalingPolicyResponse.

        静默期开始时间（上一次变更结束时间）。  格式为\"yyyy-mm-ddThh:mm:ssZ\"。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The silence_start_at of this ShowAutoScalingPolicyResponse.
        :rtype: str
        """
        return self._silence_start_at

    @silence_start_at.setter
    def silence_start_at(self, silence_start_at):
        """Sets the silence_start_at of this ShowAutoScalingPolicyResponse.

        静默期开始时间（上一次变更结束时间）。  格式为\"yyyy-mm-ddThh:mm:ssZ\"。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param silence_start_at: The silence_start_at of this ShowAutoScalingPolicyResponse.
        :type silence_start_at: str
        """
        self._silence_start_at = silence_start_at

    @property
    def scaling_strategy(self):
        """Gets the scaling_strategy of this ShowAutoScalingPolicyResponse.

        :return: The scaling_strategy of this ShowAutoScalingPolicyResponse.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ScalingStrategyInfo`
        """
        return self._scaling_strategy

    @scaling_strategy.setter
    def scaling_strategy(self, scaling_strategy):
        """Sets the scaling_strategy of this ShowAutoScalingPolicyResponse.

        :param scaling_strategy: The scaling_strategy of this ShowAutoScalingPolicyResponse.
        :type scaling_strategy: :class:`huaweicloudsdkgaussdb.v3.ScalingStrategyInfo`
        """
        self._scaling_strategy = scaling_strategy

    @property
    def max_read_only_count(self):
        """Gets the max_read_only_count of this ShowAutoScalingPolicyResponse.

        只读节点数量上限。

        :return: The max_read_only_count of this ShowAutoScalingPolicyResponse.
        :rtype: int
        """
        return self._max_read_only_count

    @max_read_only_count.setter
    def max_read_only_count(self, max_read_only_count):
        """Sets the max_read_only_count of this ShowAutoScalingPolicyResponse.

        只读节点数量上限。

        :param max_read_only_count: The max_read_only_count of this ShowAutoScalingPolicyResponse.
        :type max_read_only_count: int
        """
        self._max_read_only_count = max_read_only_count

    @property
    def min_read_only_count(self):
        """Gets the min_read_only_count of this ShowAutoScalingPolicyResponse.

        只读节点数量下限。

        :return: The min_read_only_count of this ShowAutoScalingPolicyResponse.
        :rtype: int
        """
        return self._min_read_only_count

    @min_read_only_count.setter
    def min_read_only_count(self, min_read_only_count):
        """Sets the min_read_only_count of this ShowAutoScalingPolicyResponse.

        只读节点数量下限。

        :param min_read_only_count: The min_read_only_count of this ShowAutoScalingPolicyResponse.
        :type min_read_only_count: int
        """
        self._min_read_only_count = min_read_only_count

    @property
    def read_only_weight(self):
        """Gets the read_only_weight of this ShowAutoScalingPolicyResponse.

        只读节点读写分离权重。

        :return: The read_only_weight of this ShowAutoScalingPolicyResponse.
        :rtype: int
        """
        return self._read_only_weight

    @read_only_weight.setter
    def read_only_weight(self, read_only_weight):
        """Sets the read_only_weight of this ShowAutoScalingPolicyResponse.

        只读节点读写分离权重。

        :param read_only_weight: The read_only_weight of this ShowAutoScalingPolicyResponse.
        :type read_only_weight: int
        """
        self._read_only_weight = read_only_weight

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
        if not isinstance(other, ShowAutoScalingPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
