# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReadOnlyScalingStrategy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'read_only_enlarge_enabled': 'str',
        'read_only_reduce_enabled': 'str',
        'read_only_monitor_cycle': 'str',
        'read_only_silence_cycle': 'str',
        'max_read_only_count': 'str',
        'read_only_enlarge_threshold': 'str',
        'read_only_flavor': 'str',
        'min_read_only_count': 'str',
        'read_only_reduce_threshold': 'str'
    }

    attribute_map = {
        'read_only_enlarge_enabled': 'read_only_enlarge_enabled',
        'read_only_reduce_enabled': 'read_only_reduce_enabled',
        'read_only_monitor_cycle': 'read_only_monitor_cycle',
        'read_only_silence_cycle': 'read_only_silence_cycle',
        'max_read_only_count': 'max_read_only_count',
        'read_only_enlarge_threshold': 'read_only_enlarge_threshold',
        'read_only_flavor': 'read_only_flavor',
        'min_read_only_count': 'min_read_only_count',
        'read_only_reduce_threshold': 'read_only_reduce_threshold'
    }

    def __init__(self, read_only_enlarge_enabled=None, read_only_reduce_enabled=None, read_only_monitor_cycle=None, read_only_silence_cycle=None, max_read_only_count=None, read_only_enlarge_threshold=None, read_only_flavor=None, min_read_only_count=None, read_only_reduce_threshold=None):
        r"""ReadOnlyScalingStrategy

        The model defined in huaweicloud sdk

        :param read_only_enlarge_enabled: **参数解释**：  只读扩容开关。  **约束限制**：  不涉及。  **取值范围**：  - ON：开启 - OFF：关闭  **默认取值**：  不涉及。
        :type read_only_enlarge_enabled: str
        :param read_only_reduce_enabled: **参数解释**：  只读缩容开关。  **约束限制**：  不涉及。  **取值范围**：  - ON：开启 - OFF：关闭  **默认取值**：  不涉及。
        :type read_only_reduce_enabled: str
        :param read_only_monitor_cycle: **参数解释**：  观测窗口时间，单位秒。  **约束限制**：  不涉及。  **取值范围**：  - 120 - 300 - 600 - 900 - 1800  **默认取值**：  不涉及。
        :type read_only_monitor_cycle: str
        :param read_only_silence_cycle: **参数解释**：  静默期，单位秒。  **约束限制**：  不涉及。  **取值范围**：  - 300 - 600 - 1800 - 3600 - 7200 - 10800 - 86400 - 604800  **默认取值**：  不涉及。
        :type read_only_silence_cycle: str
        :param max_read_only_count: **参数解释**：  只读最大节点数。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type max_read_only_count: str
        :param read_only_enlarge_threshold: **参数解释**：  只读扩容阈值。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type read_only_enlarge_threshold: str
        :param read_only_flavor: **参数解释**：  扩容新增只读规格。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type read_only_flavor: str
        :param min_read_only_count: **参数解释**：  只读最小节点数。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type min_read_only_count: str
        :param read_only_reduce_threshold: **参数解释**：  只读缩容阈值。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type read_only_reduce_threshold: str
        """
        
        

        self._read_only_enlarge_enabled = None
        self._read_only_reduce_enabled = None
        self._read_only_monitor_cycle = None
        self._read_only_silence_cycle = None
        self._max_read_only_count = None
        self._read_only_enlarge_threshold = None
        self._read_only_flavor = None
        self._min_read_only_count = None
        self._read_only_reduce_threshold = None
        self.discriminator = None

        if read_only_enlarge_enabled is not None:
            self.read_only_enlarge_enabled = read_only_enlarge_enabled
        if read_only_reduce_enabled is not None:
            self.read_only_reduce_enabled = read_only_reduce_enabled
        if read_only_monitor_cycle is not None:
            self.read_only_monitor_cycle = read_only_monitor_cycle
        if read_only_silence_cycle is not None:
            self.read_only_silence_cycle = read_only_silence_cycle
        if max_read_only_count is not None:
            self.max_read_only_count = max_read_only_count
        if read_only_enlarge_threshold is not None:
            self.read_only_enlarge_threshold = read_only_enlarge_threshold
        if read_only_flavor is not None:
            self.read_only_flavor = read_only_flavor
        if min_read_only_count is not None:
            self.min_read_only_count = min_read_only_count
        if read_only_reduce_threshold is not None:
            self.read_only_reduce_threshold = read_only_reduce_threshold

    @property
    def read_only_enlarge_enabled(self):
        r"""Gets the read_only_enlarge_enabled of this ReadOnlyScalingStrategy.

        **参数解释**：  只读扩容开关。  **约束限制**：  不涉及。  **取值范围**：  - ON：开启 - OFF：关闭  **默认取值**：  不涉及。

        :return: The read_only_enlarge_enabled of this ReadOnlyScalingStrategy.
        :rtype: str
        """
        return self._read_only_enlarge_enabled

    @read_only_enlarge_enabled.setter
    def read_only_enlarge_enabled(self, read_only_enlarge_enabled):
        r"""Sets the read_only_enlarge_enabled of this ReadOnlyScalingStrategy.

        **参数解释**：  只读扩容开关。  **约束限制**：  不涉及。  **取值范围**：  - ON：开启 - OFF：关闭  **默认取值**：  不涉及。

        :param read_only_enlarge_enabled: The read_only_enlarge_enabled of this ReadOnlyScalingStrategy.
        :type read_only_enlarge_enabled: str
        """
        self._read_only_enlarge_enabled = read_only_enlarge_enabled

    @property
    def read_only_reduce_enabled(self):
        r"""Gets the read_only_reduce_enabled of this ReadOnlyScalingStrategy.

        **参数解释**：  只读缩容开关。  **约束限制**：  不涉及。  **取值范围**：  - ON：开启 - OFF：关闭  **默认取值**：  不涉及。

        :return: The read_only_reduce_enabled of this ReadOnlyScalingStrategy.
        :rtype: str
        """
        return self._read_only_reduce_enabled

    @read_only_reduce_enabled.setter
    def read_only_reduce_enabled(self, read_only_reduce_enabled):
        r"""Sets the read_only_reduce_enabled of this ReadOnlyScalingStrategy.

        **参数解释**：  只读缩容开关。  **约束限制**：  不涉及。  **取值范围**：  - ON：开启 - OFF：关闭  **默认取值**：  不涉及。

        :param read_only_reduce_enabled: The read_only_reduce_enabled of this ReadOnlyScalingStrategy.
        :type read_only_reduce_enabled: str
        """
        self._read_only_reduce_enabled = read_only_reduce_enabled

    @property
    def read_only_monitor_cycle(self):
        r"""Gets the read_only_monitor_cycle of this ReadOnlyScalingStrategy.

        **参数解释**：  观测窗口时间，单位秒。  **约束限制**：  不涉及。  **取值范围**：  - 120 - 300 - 600 - 900 - 1800  **默认取值**：  不涉及。

        :return: The read_only_monitor_cycle of this ReadOnlyScalingStrategy.
        :rtype: str
        """
        return self._read_only_monitor_cycle

    @read_only_monitor_cycle.setter
    def read_only_monitor_cycle(self, read_only_monitor_cycle):
        r"""Sets the read_only_monitor_cycle of this ReadOnlyScalingStrategy.

        **参数解释**：  观测窗口时间，单位秒。  **约束限制**：  不涉及。  **取值范围**：  - 120 - 300 - 600 - 900 - 1800  **默认取值**：  不涉及。

        :param read_only_monitor_cycle: The read_only_monitor_cycle of this ReadOnlyScalingStrategy.
        :type read_only_monitor_cycle: str
        """
        self._read_only_monitor_cycle = read_only_monitor_cycle

    @property
    def read_only_silence_cycle(self):
        r"""Gets the read_only_silence_cycle of this ReadOnlyScalingStrategy.

        **参数解释**：  静默期，单位秒。  **约束限制**：  不涉及。  **取值范围**：  - 300 - 600 - 1800 - 3600 - 7200 - 10800 - 86400 - 604800  **默认取值**：  不涉及。

        :return: The read_only_silence_cycle of this ReadOnlyScalingStrategy.
        :rtype: str
        """
        return self._read_only_silence_cycle

    @read_only_silence_cycle.setter
    def read_only_silence_cycle(self, read_only_silence_cycle):
        r"""Sets the read_only_silence_cycle of this ReadOnlyScalingStrategy.

        **参数解释**：  静默期，单位秒。  **约束限制**：  不涉及。  **取值范围**：  - 300 - 600 - 1800 - 3600 - 7200 - 10800 - 86400 - 604800  **默认取值**：  不涉及。

        :param read_only_silence_cycle: The read_only_silence_cycle of this ReadOnlyScalingStrategy.
        :type read_only_silence_cycle: str
        """
        self._read_only_silence_cycle = read_only_silence_cycle

    @property
    def max_read_only_count(self):
        r"""Gets the max_read_only_count of this ReadOnlyScalingStrategy.

        **参数解释**：  只读最大节点数。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The max_read_only_count of this ReadOnlyScalingStrategy.
        :rtype: str
        """
        return self._max_read_only_count

    @max_read_only_count.setter
    def max_read_only_count(self, max_read_only_count):
        r"""Sets the max_read_only_count of this ReadOnlyScalingStrategy.

        **参数解释**：  只读最大节点数。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param max_read_only_count: The max_read_only_count of this ReadOnlyScalingStrategy.
        :type max_read_only_count: str
        """
        self._max_read_only_count = max_read_only_count

    @property
    def read_only_enlarge_threshold(self):
        r"""Gets the read_only_enlarge_threshold of this ReadOnlyScalingStrategy.

        **参数解释**：  只读扩容阈值。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The read_only_enlarge_threshold of this ReadOnlyScalingStrategy.
        :rtype: str
        """
        return self._read_only_enlarge_threshold

    @read_only_enlarge_threshold.setter
    def read_only_enlarge_threshold(self, read_only_enlarge_threshold):
        r"""Sets the read_only_enlarge_threshold of this ReadOnlyScalingStrategy.

        **参数解释**：  只读扩容阈值。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param read_only_enlarge_threshold: The read_only_enlarge_threshold of this ReadOnlyScalingStrategy.
        :type read_only_enlarge_threshold: str
        """
        self._read_only_enlarge_threshold = read_only_enlarge_threshold

    @property
    def read_only_flavor(self):
        r"""Gets the read_only_flavor of this ReadOnlyScalingStrategy.

        **参数解释**：  扩容新增只读规格。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The read_only_flavor of this ReadOnlyScalingStrategy.
        :rtype: str
        """
        return self._read_only_flavor

    @read_only_flavor.setter
    def read_only_flavor(self, read_only_flavor):
        r"""Sets the read_only_flavor of this ReadOnlyScalingStrategy.

        **参数解释**：  扩容新增只读规格。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param read_only_flavor: The read_only_flavor of this ReadOnlyScalingStrategy.
        :type read_only_flavor: str
        """
        self._read_only_flavor = read_only_flavor

    @property
    def min_read_only_count(self):
        r"""Gets the min_read_only_count of this ReadOnlyScalingStrategy.

        **参数解释**：  只读最小节点数。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The min_read_only_count of this ReadOnlyScalingStrategy.
        :rtype: str
        """
        return self._min_read_only_count

    @min_read_only_count.setter
    def min_read_only_count(self, min_read_only_count):
        r"""Sets the min_read_only_count of this ReadOnlyScalingStrategy.

        **参数解释**：  只读最小节点数。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param min_read_only_count: The min_read_only_count of this ReadOnlyScalingStrategy.
        :type min_read_only_count: str
        """
        self._min_read_only_count = min_read_only_count

    @property
    def read_only_reduce_threshold(self):
        r"""Gets the read_only_reduce_threshold of this ReadOnlyScalingStrategy.

        **参数解释**：  只读缩容阈值。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The read_only_reduce_threshold of this ReadOnlyScalingStrategy.
        :rtype: str
        """
        return self._read_only_reduce_threshold

    @read_only_reduce_threshold.setter
    def read_only_reduce_threshold(self, read_only_reduce_threshold):
        r"""Sets the read_only_reduce_threshold of this ReadOnlyScalingStrategy.

        **参数解释**：  只读缩容阈值。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param read_only_reduce_threshold: The read_only_reduce_threshold of this ReadOnlyScalingStrategy.
        :type read_only_reduce_threshold: str
        """
        self._read_only_reduce_threshold = read_only_reduce_threshold

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ReadOnlyScalingStrategy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
