# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowServerlessComputeAbilityPolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'current_vcpus': 'str',
        'min_vcpus': 'str',
        'max_vcpus': 'str',
        'scale_out_switch': 'bool',
        'max_readonly_node_count': 'int',
        'min_readonly_node_count': 'int'
    }

    attribute_map = {
        'current_vcpus': 'current_vcpus',
        'min_vcpus': 'min_vcpus',
        'max_vcpus': 'max_vcpus',
        'scale_out_switch': 'scale_out_switch',
        'max_readonly_node_count': 'max_readonly_node_count',
        'min_readonly_node_count': 'min_readonly_node_count'
    }

    def __init__(self, current_vcpus=None, min_vcpus=None, max_vcpus=None, scale_out_switch=None, max_readonly_node_count=None, min_readonly_node_count=None):
        r"""ShowServerlessComputeAbilityPolicyResponse

        The model defined in huaweicloud sdk

        :param current_vcpus: **参数描述**：  当前算力。  **取值范围**：  介于最大算力和最小算力之间。
        :type current_vcpus: str
        :param min_vcpus: **参数解释**：  最小算力。  **取值范围**：  ≥0.5。
        :type min_vcpus: str
        :param max_vcpus: **参数解释**：  最大算力。  **取值范围**：  ≥4。
        :type max_vcpus: str
        :param scale_out_switch: **参数解释**:  增删只读节点开关。  **取值范围**： - true: 开启增删只读节点。 - false: 关闭增删只读节点。
        :type scale_out_switch: bool
        :param max_readonly_node_count: **参数解释**：  最大只读节点个数。  **取值范围**：  ≥2。
        :type max_readonly_node_count: int
        :param min_readonly_node_count: **参数解释**：  最小只读节点个数。  **取值范围**：  ≥1。    
        :type min_readonly_node_count: int
        """
        
        super().__init__()

        self._current_vcpus = None
        self._min_vcpus = None
        self._max_vcpus = None
        self._scale_out_switch = None
        self._max_readonly_node_count = None
        self._min_readonly_node_count = None
        self.discriminator = None

        if current_vcpus is not None:
            self.current_vcpus = current_vcpus
        if min_vcpus is not None:
            self.min_vcpus = min_vcpus
        if max_vcpus is not None:
            self.max_vcpus = max_vcpus
        if scale_out_switch is not None:
            self.scale_out_switch = scale_out_switch
        if max_readonly_node_count is not None:
            self.max_readonly_node_count = max_readonly_node_count
        if min_readonly_node_count is not None:
            self.min_readonly_node_count = min_readonly_node_count

    @property
    def current_vcpus(self):
        r"""Gets the current_vcpus of this ShowServerlessComputeAbilityPolicyResponse.

        **参数描述**：  当前算力。  **取值范围**：  介于最大算力和最小算力之间。

        :return: The current_vcpus of this ShowServerlessComputeAbilityPolicyResponse.
        :rtype: str
        """
        return self._current_vcpus

    @current_vcpus.setter
    def current_vcpus(self, current_vcpus):
        r"""Sets the current_vcpus of this ShowServerlessComputeAbilityPolicyResponse.

        **参数描述**：  当前算力。  **取值范围**：  介于最大算力和最小算力之间。

        :param current_vcpus: The current_vcpus of this ShowServerlessComputeAbilityPolicyResponse.
        :type current_vcpus: str
        """
        self._current_vcpus = current_vcpus

    @property
    def min_vcpus(self):
        r"""Gets the min_vcpus of this ShowServerlessComputeAbilityPolicyResponse.

        **参数解释**：  最小算力。  **取值范围**：  ≥0.5。

        :return: The min_vcpus of this ShowServerlessComputeAbilityPolicyResponse.
        :rtype: str
        """
        return self._min_vcpus

    @min_vcpus.setter
    def min_vcpus(self, min_vcpus):
        r"""Sets the min_vcpus of this ShowServerlessComputeAbilityPolicyResponse.

        **参数解释**：  最小算力。  **取值范围**：  ≥0.5。

        :param min_vcpus: The min_vcpus of this ShowServerlessComputeAbilityPolicyResponse.
        :type min_vcpus: str
        """
        self._min_vcpus = min_vcpus

    @property
    def max_vcpus(self):
        r"""Gets the max_vcpus of this ShowServerlessComputeAbilityPolicyResponse.

        **参数解释**：  最大算力。  **取值范围**：  ≥4。

        :return: The max_vcpus of this ShowServerlessComputeAbilityPolicyResponse.
        :rtype: str
        """
        return self._max_vcpus

    @max_vcpus.setter
    def max_vcpus(self, max_vcpus):
        r"""Sets the max_vcpus of this ShowServerlessComputeAbilityPolicyResponse.

        **参数解释**：  最大算力。  **取值范围**：  ≥4。

        :param max_vcpus: The max_vcpus of this ShowServerlessComputeAbilityPolicyResponse.
        :type max_vcpus: str
        """
        self._max_vcpus = max_vcpus

    @property
    def scale_out_switch(self):
        r"""Gets the scale_out_switch of this ShowServerlessComputeAbilityPolicyResponse.

        **参数解释**:  增删只读节点开关。  **取值范围**： - true: 开启增删只读节点。 - false: 关闭增删只读节点。

        :return: The scale_out_switch of this ShowServerlessComputeAbilityPolicyResponse.
        :rtype: bool
        """
        return self._scale_out_switch

    @scale_out_switch.setter
    def scale_out_switch(self, scale_out_switch):
        r"""Sets the scale_out_switch of this ShowServerlessComputeAbilityPolicyResponse.

        **参数解释**:  增删只读节点开关。  **取值范围**： - true: 开启增删只读节点。 - false: 关闭增删只读节点。

        :param scale_out_switch: The scale_out_switch of this ShowServerlessComputeAbilityPolicyResponse.
        :type scale_out_switch: bool
        """
        self._scale_out_switch = scale_out_switch

    @property
    def max_readonly_node_count(self):
        r"""Gets the max_readonly_node_count of this ShowServerlessComputeAbilityPolicyResponse.

        **参数解释**：  最大只读节点个数。  **取值范围**：  ≥2。

        :return: The max_readonly_node_count of this ShowServerlessComputeAbilityPolicyResponse.
        :rtype: int
        """
        return self._max_readonly_node_count

    @max_readonly_node_count.setter
    def max_readonly_node_count(self, max_readonly_node_count):
        r"""Sets the max_readonly_node_count of this ShowServerlessComputeAbilityPolicyResponse.

        **参数解释**：  最大只读节点个数。  **取值范围**：  ≥2。

        :param max_readonly_node_count: The max_readonly_node_count of this ShowServerlessComputeAbilityPolicyResponse.
        :type max_readonly_node_count: int
        """
        self._max_readonly_node_count = max_readonly_node_count

    @property
    def min_readonly_node_count(self):
        r"""Gets the min_readonly_node_count of this ShowServerlessComputeAbilityPolicyResponse.

        **参数解释**：  最小只读节点个数。  **取值范围**：  ≥1。    

        :return: The min_readonly_node_count of this ShowServerlessComputeAbilityPolicyResponse.
        :rtype: int
        """
        return self._min_readonly_node_count

    @min_readonly_node_count.setter
    def min_readonly_node_count(self, min_readonly_node_count):
        r"""Sets the min_readonly_node_count of this ShowServerlessComputeAbilityPolicyResponse.

        **参数解释**：  最小只读节点个数。  **取值范围**：  ≥1。    

        :param min_readonly_node_count: The min_readonly_node_count of this ShowServerlessComputeAbilityPolicyResponse.
        :type min_readonly_node_count: int
        """
        self._min_readonly_node_count = min_readonly_node_count

    def to_dict(self):
        import warnings
        warnings.warn("ShowServerlessComputeAbilityPolicyResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowServerlessComputeAbilityPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
