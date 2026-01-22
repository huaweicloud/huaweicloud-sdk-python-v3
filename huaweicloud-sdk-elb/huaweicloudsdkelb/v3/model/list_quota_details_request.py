# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListQuotaDetailsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'quota_key': 'list[str]'
    }

    attribute_map = {
        'quota_key': 'quota_key'
    }

    def __init__(self, quota_key=None):
        r"""ListQuotaDetailsRequest

        The model defined in huaweicloud sdk

        :param quota_key: **参数解释**：配额类型。支持多值查询，查询条件格式：quota_key&#x3D;xxx&amp;quota_key&#x3D;xxx。  **约束限制**：不涉及  **取值范围**： - loadbalancer：负载均衡器配额。 - listener：监听器配额。 - ipgroup：IP地址组配额。 - pool：后端服务器组配额。 - member：后端服务器配额。 - healthmonitor：健康检查配额。 - l7policy：转发策略配额。 - certificate：证书配额。 - security_policy：自定义安全策略配额。 - listeners_per_loadbalancer：单个LB实例下的监听器配额。 - listeners_per_pool：单个pool关联的监听器配额。 - members_per_pool：单个pool下的member的配额。 - condition_per_policy：单个转发策略下所有转发规则的condition总数配额。 - ipgroup_bindings：单个IP地址组可以关联的监听器数量配额。 - ipgroup_max_length：单个监听器下关联的所有IP地址组的ip列表中的IP总数不能超过ipgroup_max_length。 - ipgroups_per_listener：单个监听器下的IP地址组配额。 - pools_per_l7policy：单个转发策略下的后端服务器组配额。 - l7policies_per_listener：单个监听器下的转发策略配额。 - free_instance_members_per_pool：单个pool实例下的免费member配额。 - free_instance_listeners_per_loadbalancer：单个LB实例下的免费监听器配额。  **默认取值**：不涉及
        :type quota_key: list[str]
        """
        
        

        self._quota_key = None
        self.discriminator = None

        if quota_key is not None:
            self.quota_key = quota_key

    @property
    def quota_key(self):
        r"""Gets the quota_key of this ListQuotaDetailsRequest.

        **参数解释**：配额类型。支持多值查询，查询条件格式：quota_key=xxx&quota_key=xxx。  **约束限制**：不涉及  **取值范围**： - loadbalancer：负载均衡器配额。 - listener：监听器配额。 - ipgroup：IP地址组配额。 - pool：后端服务器组配额。 - member：后端服务器配额。 - healthmonitor：健康检查配额。 - l7policy：转发策略配额。 - certificate：证书配额。 - security_policy：自定义安全策略配额。 - listeners_per_loadbalancer：单个LB实例下的监听器配额。 - listeners_per_pool：单个pool关联的监听器配额。 - members_per_pool：单个pool下的member的配额。 - condition_per_policy：单个转发策略下所有转发规则的condition总数配额。 - ipgroup_bindings：单个IP地址组可以关联的监听器数量配额。 - ipgroup_max_length：单个监听器下关联的所有IP地址组的ip列表中的IP总数不能超过ipgroup_max_length。 - ipgroups_per_listener：单个监听器下的IP地址组配额。 - pools_per_l7policy：单个转发策略下的后端服务器组配额。 - l7policies_per_listener：单个监听器下的转发策略配额。 - free_instance_members_per_pool：单个pool实例下的免费member配额。 - free_instance_listeners_per_loadbalancer：单个LB实例下的免费监听器配额。  **默认取值**：不涉及

        :return: The quota_key of this ListQuotaDetailsRequest.
        :rtype: list[str]
        """
        return self._quota_key

    @quota_key.setter
    def quota_key(self, quota_key):
        r"""Sets the quota_key of this ListQuotaDetailsRequest.

        **参数解释**：配额类型。支持多值查询，查询条件格式：quota_key=xxx&quota_key=xxx。  **约束限制**：不涉及  **取值范围**： - loadbalancer：负载均衡器配额。 - listener：监听器配额。 - ipgroup：IP地址组配额。 - pool：后端服务器组配额。 - member：后端服务器配额。 - healthmonitor：健康检查配额。 - l7policy：转发策略配额。 - certificate：证书配额。 - security_policy：自定义安全策略配额。 - listeners_per_loadbalancer：单个LB实例下的监听器配额。 - listeners_per_pool：单个pool关联的监听器配额。 - members_per_pool：单个pool下的member的配额。 - condition_per_policy：单个转发策略下所有转发规则的condition总数配额。 - ipgroup_bindings：单个IP地址组可以关联的监听器数量配额。 - ipgroup_max_length：单个监听器下关联的所有IP地址组的ip列表中的IP总数不能超过ipgroup_max_length。 - ipgroups_per_listener：单个监听器下的IP地址组配额。 - pools_per_l7policy：单个转发策略下的后端服务器组配额。 - l7policies_per_listener：单个监听器下的转发策略配额。 - free_instance_members_per_pool：单个pool实例下的免费member配额。 - free_instance_listeners_per_loadbalancer：单个LB实例下的免费监听器配额。  **默认取值**：不涉及

        :param quota_key: The quota_key of this ListQuotaDetailsRequest.
        :type quota_key: list[str]
        """
        self._quota_key = quota_key

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
        if not isinstance(other, ListQuotaDetailsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
