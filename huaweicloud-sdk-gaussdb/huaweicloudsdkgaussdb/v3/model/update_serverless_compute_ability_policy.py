# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateServerlessComputeAbilityPolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'min_vcpus': 'int',
        'max_vcpus': 'int',
        'need_update_nodes_compute_ability': 'bool',
        'scale_out_switch': 'bool',
        'max_readonly_node_count': 'int',
        'min_readonly_node_count': 'int'
    }

    attribute_map = {
        'min_vcpus': 'min_vcpus',
        'max_vcpus': 'max_vcpus',
        'need_update_nodes_compute_ability': 'need_update_nodes_compute_ability',
        'scale_out_switch': 'scale_out_switch',
        'max_readonly_node_count': 'max_readonly_node_count',
        'min_readonly_node_count': 'min_readonly_node_count'
    }

    def __init__(self, min_vcpus=None, max_vcpus=None, need_update_nodes_compute_ability=None, scale_out_switch=None, max_readonly_node_count=None, min_readonly_node_count=None):
        r"""UpdateServerlessComputeAbilityPolicy

        The model defined in huaweicloud sdk

        :param min_vcpus: **参数解释**：  单节点VCPUs伸缩下限。  **约束限制**：  不涉及。  **取值范围**：  取值范围可根据[查询数据库规格](https://support.huaweicloud.com/api-taurusdb/ShowGaussMySqlFlavors.html)接口获取。  **默认取值**：  不涉及。
        :type min_vcpus: int
        :param max_vcpus: **参数解释**：  单节点VCPUs伸缩上限。  **约束限制**：  不涉及。  **取值范围**：  ≥4。取值范围可根据[查询数据库规格](https://support.huaweicloud.com/api-taurusdb/ShowGaussMySqlFlavors.html)接口获取。  **默认取值**：  不涉及。
        :type max_vcpus: int
        :param need_update_nodes_compute_ability: **参数解释**：  节点算力同步，修改算力范围的同时，是否将小于最小算力的节点的当前算力同步至最小算力。  **约束限制**：  不涉及。  **取值范围**： - true: 节点算力同步。 - false: 节点算力不同步。  **默认取值**： false。
        :type need_update_nodes_compute_ability: bool
        :param scale_out_switch: **参数解释**：  是否增删只读节点。  **约束限制**：  - 存在数据库代理时，才可以使用增删只读节点功能。  - 使用增删节点功能时，避免使用读内网地址连接应用。  - 打开增删只读节点后，数据库代理的路由模式会变为负载均衡模式。  **取值范围**： - true: 开启增删只读节点。 - false: 不开启增删只读节点。  **默认取值**：  false。
        :type scale_out_switch: bool
        :param max_readonly_node_count: **参数解释**：  只读节点数量上限。  **约束限制**：  开启增删只读节点时才会生效, 且开启增删只读节点时该参数必选。  **取值范围**：  2-7。  **默认取值**：  不涉及。
        :type max_readonly_node_count: int
        :param min_readonly_node_count: **参数解释**：  只读节点数量上限。  **约束限制**：  开启增删只读节点时才会生效, 且开启增删只读节点时该参数必选。  **取值范围**：  1-6。  **默认取值**：  不涉及。
        :type min_readonly_node_count: int
        """
        
        

        self._min_vcpus = None
        self._max_vcpus = None
        self._need_update_nodes_compute_ability = None
        self._scale_out_switch = None
        self._max_readonly_node_count = None
        self._min_readonly_node_count = None
        self.discriminator = None

        self.min_vcpus = min_vcpus
        self.max_vcpus = max_vcpus
        if need_update_nodes_compute_ability is not None:
            self.need_update_nodes_compute_ability = need_update_nodes_compute_ability
        if scale_out_switch is not None:
            self.scale_out_switch = scale_out_switch
        if max_readonly_node_count is not None:
            self.max_readonly_node_count = max_readonly_node_count
        if min_readonly_node_count is not None:
            self.min_readonly_node_count = min_readonly_node_count

    @property
    def min_vcpus(self):
        r"""Gets the min_vcpus of this UpdateServerlessComputeAbilityPolicy.

        **参数解释**：  单节点VCPUs伸缩下限。  **约束限制**：  不涉及。  **取值范围**：  取值范围可根据[查询数据库规格](https://support.huaweicloud.com/api-taurusdb/ShowGaussMySqlFlavors.html)接口获取。  **默认取值**：  不涉及。

        :return: The min_vcpus of this UpdateServerlessComputeAbilityPolicy.
        :rtype: int
        """
        return self._min_vcpus

    @min_vcpus.setter
    def min_vcpus(self, min_vcpus):
        r"""Sets the min_vcpus of this UpdateServerlessComputeAbilityPolicy.

        **参数解释**：  单节点VCPUs伸缩下限。  **约束限制**：  不涉及。  **取值范围**：  取值范围可根据[查询数据库规格](https://support.huaweicloud.com/api-taurusdb/ShowGaussMySqlFlavors.html)接口获取。  **默认取值**：  不涉及。

        :param min_vcpus: The min_vcpus of this UpdateServerlessComputeAbilityPolicy.
        :type min_vcpus: int
        """
        self._min_vcpus = min_vcpus

    @property
    def max_vcpus(self):
        r"""Gets the max_vcpus of this UpdateServerlessComputeAbilityPolicy.

        **参数解释**：  单节点VCPUs伸缩上限。  **约束限制**：  不涉及。  **取值范围**：  ≥4。取值范围可根据[查询数据库规格](https://support.huaweicloud.com/api-taurusdb/ShowGaussMySqlFlavors.html)接口获取。  **默认取值**：  不涉及。

        :return: The max_vcpus of this UpdateServerlessComputeAbilityPolicy.
        :rtype: int
        """
        return self._max_vcpus

    @max_vcpus.setter
    def max_vcpus(self, max_vcpus):
        r"""Sets the max_vcpus of this UpdateServerlessComputeAbilityPolicy.

        **参数解释**：  单节点VCPUs伸缩上限。  **约束限制**：  不涉及。  **取值范围**：  ≥4。取值范围可根据[查询数据库规格](https://support.huaweicloud.com/api-taurusdb/ShowGaussMySqlFlavors.html)接口获取。  **默认取值**：  不涉及。

        :param max_vcpus: The max_vcpus of this UpdateServerlessComputeAbilityPolicy.
        :type max_vcpus: int
        """
        self._max_vcpus = max_vcpus

    @property
    def need_update_nodes_compute_ability(self):
        r"""Gets the need_update_nodes_compute_ability of this UpdateServerlessComputeAbilityPolicy.

        **参数解释**：  节点算力同步，修改算力范围的同时，是否将小于最小算力的节点的当前算力同步至最小算力。  **约束限制**：  不涉及。  **取值范围**： - true: 节点算力同步。 - false: 节点算力不同步。  **默认取值**： false。

        :return: The need_update_nodes_compute_ability of this UpdateServerlessComputeAbilityPolicy.
        :rtype: bool
        """
        return self._need_update_nodes_compute_ability

    @need_update_nodes_compute_ability.setter
    def need_update_nodes_compute_ability(self, need_update_nodes_compute_ability):
        r"""Sets the need_update_nodes_compute_ability of this UpdateServerlessComputeAbilityPolicy.

        **参数解释**：  节点算力同步，修改算力范围的同时，是否将小于最小算力的节点的当前算力同步至最小算力。  **约束限制**：  不涉及。  **取值范围**： - true: 节点算力同步。 - false: 节点算力不同步。  **默认取值**： false。

        :param need_update_nodes_compute_ability: The need_update_nodes_compute_ability of this UpdateServerlessComputeAbilityPolicy.
        :type need_update_nodes_compute_ability: bool
        """
        self._need_update_nodes_compute_ability = need_update_nodes_compute_ability

    @property
    def scale_out_switch(self):
        r"""Gets the scale_out_switch of this UpdateServerlessComputeAbilityPolicy.

        **参数解释**：  是否增删只读节点。  **约束限制**：  - 存在数据库代理时，才可以使用增删只读节点功能。  - 使用增删节点功能时，避免使用读内网地址连接应用。  - 打开增删只读节点后，数据库代理的路由模式会变为负载均衡模式。  **取值范围**： - true: 开启增删只读节点。 - false: 不开启增删只读节点。  **默认取值**：  false。

        :return: The scale_out_switch of this UpdateServerlessComputeAbilityPolicy.
        :rtype: bool
        """
        return self._scale_out_switch

    @scale_out_switch.setter
    def scale_out_switch(self, scale_out_switch):
        r"""Sets the scale_out_switch of this UpdateServerlessComputeAbilityPolicy.

        **参数解释**：  是否增删只读节点。  **约束限制**：  - 存在数据库代理时，才可以使用增删只读节点功能。  - 使用增删节点功能时，避免使用读内网地址连接应用。  - 打开增删只读节点后，数据库代理的路由模式会变为负载均衡模式。  **取值范围**： - true: 开启增删只读节点。 - false: 不开启增删只读节点。  **默认取值**：  false。

        :param scale_out_switch: The scale_out_switch of this UpdateServerlessComputeAbilityPolicy.
        :type scale_out_switch: bool
        """
        self._scale_out_switch = scale_out_switch

    @property
    def max_readonly_node_count(self):
        r"""Gets the max_readonly_node_count of this UpdateServerlessComputeAbilityPolicy.

        **参数解释**：  只读节点数量上限。  **约束限制**：  开启增删只读节点时才会生效, 且开启增删只读节点时该参数必选。  **取值范围**：  2-7。  **默认取值**：  不涉及。

        :return: The max_readonly_node_count of this UpdateServerlessComputeAbilityPolicy.
        :rtype: int
        """
        return self._max_readonly_node_count

    @max_readonly_node_count.setter
    def max_readonly_node_count(self, max_readonly_node_count):
        r"""Sets the max_readonly_node_count of this UpdateServerlessComputeAbilityPolicy.

        **参数解释**：  只读节点数量上限。  **约束限制**：  开启增删只读节点时才会生效, 且开启增删只读节点时该参数必选。  **取值范围**：  2-7。  **默认取值**：  不涉及。

        :param max_readonly_node_count: The max_readonly_node_count of this UpdateServerlessComputeAbilityPolicy.
        :type max_readonly_node_count: int
        """
        self._max_readonly_node_count = max_readonly_node_count

    @property
    def min_readonly_node_count(self):
        r"""Gets the min_readonly_node_count of this UpdateServerlessComputeAbilityPolicy.

        **参数解释**：  只读节点数量上限。  **约束限制**：  开启增删只读节点时才会生效, 且开启增删只读节点时该参数必选。  **取值范围**：  1-6。  **默认取值**：  不涉及。

        :return: The min_readonly_node_count of this UpdateServerlessComputeAbilityPolicy.
        :rtype: int
        """
        return self._min_readonly_node_count

    @min_readonly_node_count.setter
    def min_readonly_node_count(self, min_readonly_node_count):
        r"""Sets the min_readonly_node_count of this UpdateServerlessComputeAbilityPolicy.

        **参数解释**：  只读节点数量上限。  **约束限制**：  开启增删只读节点时才会生效, 且开启增删只读节点时该参数必选。  **取值范围**：  1-6。  **默认取值**：  不涉及。

        :param min_readonly_node_count: The min_readonly_node_count of this UpdateServerlessComputeAbilityPolicy.
        :type min_readonly_node_count: int
        """
        self._min_readonly_node_count = min_readonly_node_count

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
        if not isinstance(other, UpdateServerlessComputeAbilityPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
