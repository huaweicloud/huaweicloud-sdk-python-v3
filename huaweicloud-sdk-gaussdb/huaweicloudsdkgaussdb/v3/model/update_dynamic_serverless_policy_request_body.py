# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDynamicServerlessPolicyRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'min_vcpus': 'str',
        'max_vcpus': 'str',
        'need_update_nodes_compute_ability': 'bool'
    }

    attribute_map = {
        'min_vcpus': 'min_vcpus',
        'max_vcpus': 'max_vcpus',
        'need_update_nodes_compute_ability': 'need_update_nodes_compute_ability'
    }

    def __init__(self, min_vcpus=None, max_vcpus=None, need_update_nodes_compute_ability=None):
        r"""UpdateDynamicServerlessPolicyRequestBody

        The model defined in huaweicloud sdk

        :param min_vcpus: **参数解释**：   最小动态Serverless算力。  **取值范围**：  取值范围可根据[查询动态Serverless算力策略](https://support.huaweicloud.com/api-taurusdb/ShowDynamicServerlessPolicy.html)接口获取，并且小于等于max_vcpus。
        :type min_vcpus: str
        :param max_vcpus: **参数解释**：   最大动态Serverless算力。  **取值范围**：  取值范围可根据[查询动态Serverless算力策略](https://support.huaweicloud.com/api-taurusdb/ShowDynamicServerlessPolicy.html)接口获取，并且大于等于min_vcpus。
        :type max_vcpus: str
        :param need_update_nodes_compute_ability: **参数解释**：  节点算力同步，修改算力范围的同时，是否将小于最小算力的节点的当前算力同步至最小算力。  **约束限制**：  不涉及。  **取值范围**： - true: 节点算力同步。 - false: 节点算力不同步。  **默认取值**：  false。
        :type need_update_nodes_compute_ability: bool
        """
        
        

        self._min_vcpus = None
        self._max_vcpus = None
        self._need_update_nodes_compute_ability = None
        self.discriminator = None

        self.min_vcpus = min_vcpus
        self.max_vcpus = max_vcpus
        if need_update_nodes_compute_ability is not None:
            self.need_update_nodes_compute_ability = need_update_nodes_compute_ability

    @property
    def min_vcpus(self):
        r"""Gets the min_vcpus of this UpdateDynamicServerlessPolicyRequestBody.

        **参数解释**：   最小动态Serverless算力。  **取值范围**：  取值范围可根据[查询动态Serverless算力策略](https://support.huaweicloud.com/api-taurusdb/ShowDynamicServerlessPolicy.html)接口获取，并且小于等于max_vcpus。

        :return: The min_vcpus of this UpdateDynamicServerlessPolicyRequestBody.
        :rtype: str
        """
        return self._min_vcpus

    @min_vcpus.setter
    def min_vcpus(self, min_vcpus):
        r"""Sets the min_vcpus of this UpdateDynamicServerlessPolicyRequestBody.

        **参数解释**：   最小动态Serverless算力。  **取值范围**：  取值范围可根据[查询动态Serverless算力策略](https://support.huaweicloud.com/api-taurusdb/ShowDynamicServerlessPolicy.html)接口获取，并且小于等于max_vcpus。

        :param min_vcpus: The min_vcpus of this UpdateDynamicServerlessPolicyRequestBody.
        :type min_vcpus: str
        """
        self._min_vcpus = min_vcpus

    @property
    def max_vcpus(self):
        r"""Gets the max_vcpus of this UpdateDynamicServerlessPolicyRequestBody.

        **参数解释**：   最大动态Serverless算力。  **取值范围**：  取值范围可根据[查询动态Serverless算力策略](https://support.huaweicloud.com/api-taurusdb/ShowDynamicServerlessPolicy.html)接口获取，并且大于等于min_vcpus。

        :return: The max_vcpus of this UpdateDynamicServerlessPolicyRequestBody.
        :rtype: str
        """
        return self._max_vcpus

    @max_vcpus.setter
    def max_vcpus(self, max_vcpus):
        r"""Sets the max_vcpus of this UpdateDynamicServerlessPolicyRequestBody.

        **参数解释**：   最大动态Serverless算力。  **取值范围**：  取值范围可根据[查询动态Serverless算力策略](https://support.huaweicloud.com/api-taurusdb/ShowDynamicServerlessPolicy.html)接口获取，并且大于等于min_vcpus。

        :param max_vcpus: The max_vcpus of this UpdateDynamicServerlessPolicyRequestBody.
        :type max_vcpus: str
        """
        self._max_vcpus = max_vcpus

    @property
    def need_update_nodes_compute_ability(self):
        r"""Gets the need_update_nodes_compute_ability of this UpdateDynamicServerlessPolicyRequestBody.

        **参数解释**：  节点算力同步，修改算力范围的同时，是否将小于最小算力的节点的当前算力同步至最小算力。  **约束限制**：  不涉及。  **取值范围**： - true: 节点算力同步。 - false: 节点算力不同步。  **默认取值**：  false。

        :return: The need_update_nodes_compute_ability of this UpdateDynamicServerlessPolicyRequestBody.
        :rtype: bool
        """
        return self._need_update_nodes_compute_ability

    @need_update_nodes_compute_ability.setter
    def need_update_nodes_compute_ability(self, need_update_nodes_compute_ability):
        r"""Sets the need_update_nodes_compute_ability of this UpdateDynamicServerlessPolicyRequestBody.

        **参数解释**：  节点算力同步，修改算力范围的同时，是否将小于最小算力的节点的当前算力同步至最小算力。  **约束限制**：  不涉及。  **取值范围**： - true: 节点算力同步。 - false: 节点算力不同步。  **默认取值**：  false。

        :param need_update_nodes_compute_ability: The need_update_nodes_compute_ability of this UpdateDynamicServerlessPolicyRequestBody.
        :type need_update_nodes_compute_ability: bool
        """
        self._need_update_nodes_compute_ability = need_update_nodes_compute_ability

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
        if not isinstance(other, UpdateDynamicServerlessPolicyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
