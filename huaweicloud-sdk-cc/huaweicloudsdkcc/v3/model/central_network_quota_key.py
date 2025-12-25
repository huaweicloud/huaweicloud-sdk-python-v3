# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CentralNetworkQuotaKey:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'quota_key': 'str'
    }

    attribute_map = {
        'quota_key': 'quota_key'
    }

    def __init__(self, quota_key=None):
        r"""CentralNetworkQuotaKey

        The model defined in huaweicloud sdk

        :param quota_key: 中心网络配额类型。 - central_networks_per_account (每个账户的中心网数) - policy_versions_per_central_network (每个中心网的策略数) - size_of_document_per_central_network_policy_version (中心网络策略文档大小(KB)) - planes_per_central_network (每个中心网的平面数) - er_instances_per_region_per_central_network (每个中心网络每个区域的Er实例数) - connections_per_central_network (每个中心网的连接数) - attachments_per_central_network (每个中心网的附件数) - GDGW_attachments_per_region_per_central_network (每个中心网每个区域的GDGW附件数) - ER_ROUTE_TABLE_attachments_per_region_per_central_network (每个中心网每个区域的ER_ROUTE_TABLE附件数)
        :type quota_key: str
        """
        
        

        self._quota_key = None
        self.discriminator = None

        self.quota_key = quota_key

    @property
    def quota_key(self):
        r"""Gets the quota_key of this CentralNetworkQuotaKey.

        中心网络配额类型。 - central_networks_per_account (每个账户的中心网数) - policy_versions_per_central_network (每个中心网的策略数) - size_of_document_per_central_network_policy_version (中心网络策略文档大小(KB)) - planes_per_central_network (每个中心网的平面数) - er_instances_per_region_per_central_network (每个中心网络每个区域的Er实例数) - connections_per_central_network (每个中心网的连接数) - attachments_per_central_network (每个中心网的附件数) - GDGW_attachments_per_region_per_central_network (每个中心网每个区域的GDGW附件数) - ER_ROUTE_TABLE_attachments_per_region_per_central_network (每个中心网每个区域的ER_ROUTE_TABLE附件数)

        :return: The quota_key of this CentralNetworkQuotaKey.
        :rtype: str
        """
        return self._quota_key

    @quota_key.setter
    def quota_key(self, quota_key):
        r"""Sets the quota_key of this CentralNetworkQuotaKey.

        中心网络配额类型。 - central_networks_per_account (每个账户的中心网数) - policy_versions_per_central_network (每个中心网的策略数) - size_of_document_per_central_network_policy_version (中心网络策略文档大小(KB)) - planes_per_central_network (每个中心网的平面数) - er_instances_per_region_per_central_network (每个中心网络每个区域的Er实例数) - connections_per_central_network (每个中心网的连接数) - attachments_per_central_network (每个中心网的附件数) - GDGW_attachments_per_region_per_central_network (每个中心网每个区域的GDGW附件数) - ER_ROUTE_TABLE_attachments_per_region_per_central_network (每个中心网每个区域的ER_ROUTE_TABLE附件数)

        :param quota_key: The quota_key of this CentralNetworkQuotaKey.
        :type quota_key: str
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
        if not isinstance(other, CentralNetworkQuotaKey):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
