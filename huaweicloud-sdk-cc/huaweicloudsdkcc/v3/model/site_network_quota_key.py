# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SiteNetworkQuotaKey:

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
        r"""SiteNetworkQuotaKey

        The model defined in huaweicloud sdk

        :param quota_key: 分支网络配额类型。 - site_networks_per_account (每个账户的分支网络数) - sites_per_mesh_site_network (网状分支网络的分支数) - spoke_sites_per_star_site_network (星状分支网络的Spoke分支数) - sites_per_hybrid_site_network (混合分支网络的分支数)
        :type quota_key: str
        """
        
        

        self._quota_key = None
        self.discriminator = None

        self.quota_key = quota_key

    @property
    def quota_key(self):
        r"""Gets the quota_key of this SiteNetworkQuotaKey.

        分支网络配额类型。 - site_networks_per_account (每个账户的分支网络数) - sites_per_mesh_site_network (网状分支网络的分支数) - spoke_sites_per_star_site_network (星状分支网络的Spoke分支数) - sites_per_hybrid_site_network (混合分支网络的分支数)

        :return: The quota_key of this SiteNetworkQuotaKey.
        :rtype: str
        """
        return self._quota_key

    @quota_key.setter
    def quota_key(self, quota_key):
        r"""Sets the quota_key of this SiteNetworkQuotaKey.

        分支网络配额类型。 - site_networks_per_account (每个账户的分支网络数) - sites_per_mesh_site_network (网状分支网络的分支数) - spoke_sites_per_star_site_network (星状分支网络的Spoke分支数) - sites_per_hybrid_site_network (混合分支网络的分支数)

        :param quota_key: The quota_key of this SiteNetworkQuotaKey.
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
        if not isinstance(other, SiteNetworkQuotaKey):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
