# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SiteNetworkSpecificationEnum:
    """
    allowed enum values
    """
    SITE_NETWORK_IS_SUPPORT = "site-network.is-support"
    SITE_NETWORK_IS_SUPPORT_ENTERPRISE_PROJECT = "site-network.is-support-enterprise-project"
    SITE_NETWORK_IS_SUPPORT_TAG = "site-network.is-support-tag"
    SITE_NETWORK_IS_SUPPORT_INTRA_REGION = "site-network.is-support-intra-region"
    SITE_NETWORK_SUPPORT_TOPOLOGIES = "site-network.support-topologies"
    SITE_NETWORK_SUPPORT_REGIONS = "site-network.support-regions"
    SITE_NETWORK_SUPPORT_DSCP_REGIONS = "site-network.support-dscp-regions"
    SITE_NETWORK_SUPPORT_FREEZE_REGIONS = "site-network.support-freeze-regions"
    SITE_NETWORK_SUPPORT_LOCATIONS = "site-network.support-locations"
    SITE_CONNECTION_BANDWIDTH_SIZE_RANGE = "site-connection-bandwidth.size-range"
    SITE_CONNECTION_BANDWIDTH_CHARGE_MODE = "site-connection-bandwidth.charge-mode"
    SITE_CONNECTION_BANDWIDTH_FREE_LINE = "site-connection-bandwidth.free-line"
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
    }

    attribute_map = {
    }

    def __init__(self):
        r"""SiteNetworkSpecificationEnum

        The model defined in huaweicloud sdk

        """
        
        
        self.discriminator = None

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
        if not isinstance(other, SiteNetworkSpecificationEnum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
