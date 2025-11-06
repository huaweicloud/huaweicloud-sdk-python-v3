# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAutoScalingPolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'status': 'str',
        'monitor_cycle': 'int',
        'silence_cycle': 'int',
        'enlarge_threshold': 'int',
        'max_flavor': 'str',
        'reduce_enabled': 'str',
        'reduce_threshold': 'int',
        'min_flavor': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'status': 'status',
        'monitor_cycle': 'monitor_cycle',
        'silence_cycle': 'silence_cycle',
        'enlarge_threshold': 'enlarge_threshold',
        'max_flavor': 'max_flavor',
        'reduce_enabled': 'reduce_enabled',
        'reduce_threshold': 'reduce_threshold',
        'min_flavor': 'min_flavor'
    }

    def __init__(self, instance_id=None, status=None, monitor_cycle=None, silence_cycle=None, enlarge_threshold=None, max_flavor=None, reduce_enabled=None, reduce_threshold=None, min_flavor=None):
        r"""ListAutoScalingPolicyResponse

        The model defined in huaweicloud sdk

        :param instance_id: **参数解释**：  实例ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type instance_id: str
        :param status: **参数解释**：  是否开启autoScaling，OFF为关闭，ON为开启  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type status: str
        :param monitor_cycle: **参数解释**：  观察窗口，单位秒  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type monitor_cycle: int
        :param silence_cycle: **参数解释**：  静默期，单位秒  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type silence_cycle: int
        :param enlarge_threshold: **参数解释**：  自动升配触发阈值，单位百分比  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type enlarge_threshold: int
        :param max_flavor: **参数解释**：  最大变配规格上限  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type max_flavor: str
        :param reduce_enabled: **参数解释**：  自动降配状态，on为自动降配开启；off为关闭  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type reduce_enabled: str
        :param reduce_threshold: **参数解释**：  自动降配触发阈值  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type reduce_threshold: int
        :param min_flavor: **参数解释**：  最大变配规格下限  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type min_flavor: str
        """
        
        super().__init__()

        self._instance_id = None
        self._status = None
        self._monitor_cycle = None
        self._silence_cycle = None
        self._enlarge_threshold = None
        self._max_flavor = None
        self._reduce_enabled = None
        self._reduce_threshold = None
        self._min_flavor = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
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
        if reduce_threshold is not None:
            self.reduce_threshold = reduce_threshold
        if min_flavor is not None:
            self.min_flavor = min_flavor

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListAutoScalingPolicyResponse.

        **参数解释**：  实例ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The instance_id of this ListAutoScalingPolicyResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListAutoScalingPolicyResponse.

        **参数解释**：  实例ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param instance_id: The instance_id of this ListAutoScalingPolicyResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def status(self):
        r"""Gets the status of this ListAutoScalingPolicyResponse.

        **参数解释**：  是否开启autoScaling，OFF为关闭，ON为开启  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The status of this ListAutoScalingPolicyResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListAutoScalingPolicyResponse.

        **参数解释**：  是否开启autoScaling，OFF为关闭，ON为开启  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param status: The status of this ListAutoScalingPolicyResponse.
        :type status: str
        """
        self._status = status

    @property
    def monitor_cycle(self):
        r"""Gets the monitor_cycle of this ListAutoScalingPolicyResponse.

        **参数解释**：  观察窗口，单位秒  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The monitor_cycle of this ListAutoScalingPolicyResponse.
        :rtype: int
        """
        return self._monitor_cycle

    @monitor_cycle.setter
    def monitor_cycle(self, monitor_cycle):
        r"""Sets the monitor_cycle of this ListAutoScalingPolicyResponse.

        **参数解释**：  观察窗口，单位秒  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param monitor_cycle: The monitor_cycle of this ListAutoScalingPolicyResponse.
        :type monitor_cycle: int
        """
        self._monitor_cycle = monitor_cycle

    @property
    def silence_cycle(self):
        r"""Gets the silence_cycle of this ListAutoScalingPolicyResponse.

        **参数解释**：  静默期，单位秒  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The silence_cycle of this ListAutoScalingPolicyResponse.
        :rtype: int
        """
        return self._silence_cycle

    @silence_cycle.setter
    def silence_cycle(self, silence_cycle):
        r"""Sets the silence_cycle of this ListAutoScalingPolicyResponse.

        **参数解释**：  静默期，单位秒  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param silence_cycle: The silence_cycle of this ListAutoScalingPolicyResponse.
        :type silence_cycle: int
        """
        self._silence_cycle = silence_cycle

    @property
    def enlarge_threshold(self):
        r"""Gets the enlarge_threshold of this ListAutoScalingPolicyResponse.

        **参数解释**：  自动升配触发阈值，单位百分比  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The enlarge_threshold of this ListAutoScalingPolicyResponse.
        :rtype: int
        """
        return self._enlarge_threshold

    @enlarge_threshold.setter
    def enlarge_threshold(self, enlarge_threshold):
        r"""Sets the enlarge_threshold of this ListAutoScalingPolicyResponse.

        **参数解释**：  自动升配触发阈值，单位百分比  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param enlarge_threshold: The enlarge_threshold of this ListAutoScalingPolicyResponse.
        :type enlarge_threshold: int
        """
        self._enlarge_threshold = enlarge_threshold

    @property
    def max_flavor(self):
        r"""Gets the max_flavor of this ListAutoScalingPolicyResponse.

        **参数解释**：  最大变配规格上限  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The max_flavor of this ListAutoScalingPolicyResponse.
        :rtype: str
        """
        return self._max_flavor

    @max_flavor.setter
    def max_flavor(self, max_flavor):
        r"""Sets the max_flavor of this ListAutoScalingPolicyResponse.

        **参数解释**：  最大变配规格上限  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param max_flavor: The max_flavor of this ListAutoScalingPolicyResponse.
        :type max_flavor: str
        """
        self._max_flavor = max_flavor

    @property
    def reduce_enabled(self):
        r"""Gets the reduce_enabled of this ListAutoScalingPolicyResponse.

        **参数解释**：  自动降配状态，on为自动降配开启；off为关闭  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The reduce_enabled of this ListAutoScalingPolicyResponse.
        :rtype: str
        """
        return self._reduce_enabled

    @reduce_enabled.setter
    def reduce_enabled(self, reduce_enabled):
        r"""Sets the reduce_enabled of this ListAutoScalingPolicyResponse.

        **参数解释**：  自动降配状态，on为自动降配开启；off为关闭  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param reduce_enabled: The reduce_enabled of this ListAutoScalingPolicyResponse.
        :type reduce_enabled: str
        """
        self._reduce_enabled = reduce_enabled

    @property
    def reduce_threshold(self):
        r"""Gets the reduce_threshold of this ListAutoScalingPolicyResponse.

        **参数解释**：  自动降配触发阈值  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The reduce_threshold of this ListAutoScalingPolicyResponse.
        :rtype: int
        """
        return self._reduce_threshold

    @reduce_threshold.setter
    def reduce_threshold(self, reduce_threshold):
        r"""Sets the reduce_threshold of this ListAutoScalingPolicyResponse.

        **参数解释**：  自动降配触发阈值  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param reduce_threshold: The reduce_threshold of this ListAutoScalingPolicyResponse.
        :type reduce_threshold: int
        """
        self._reduce_threshold = reduce_threshold

    @property
    def min_flavor(self):
        r"""Gets the min_flavor of this ListAutoScalingPolicyResponse.

        **参数解释**：  最大变配规格下限  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The min_flavor of this ListAutoScalingPolicyResponse.
        :rtype: str
        """
        return self._min_flavor

    @min_flavor.setter
    def min_flavor(self, min_flavor):
        r"""Sets the min_flavor of this ListAutoScalingPolicyResponse.

        **参数解释**：  最大变配规格下限  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param min_flavor: The min_flavor of this ListAutoScalingPolicyResponse.
        :type min_flavor: str
        """
        self._min_flavor = min_flavor

    def to_dict(self):
        import warnings
        warnings.warn("ListAutoScalingPolicyResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ListAutoScalingPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
