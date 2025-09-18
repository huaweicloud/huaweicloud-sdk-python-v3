# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CloudConnectionCapabilityKeyEnum:
    """
    allowed enum values
    """
    V2 = "v2"
    V3 = "v3"
    BILLING_MODE_PERIOD_REDUCE = "billing_mode_period_reduce"
    BILLING_MODE_DEMAND = "billing_mode_demand"
    BWP95 = "bwp95"
    BWP95AVG = "bwp95Avg"
    NETWORK_QUALITY = "network-quality"
    ER = "er"
    DOMAIN_BANDWIDTH = "domain_bandwidth"
    IPV6 = "ipv6"
    IPV6_SUPPORT_REGIONS = "ipv6_support_regions"
    ENTERPRISE_CLOUD_CONNECTION_IS_SUPPORT = "enterprise-cloud-connection.is-support"
    ENTERPRISE_CLOUD_CONNECTION_SUPPORT_SITES = "enterprise-cloud-connection.support-sites"
    ENTERPRISE_CLOUD_CONNECTION_SEGMENT_IS_SUPPORT = "enterprise-cloud-connection-segment.is-support"
    ENTERPRISE_CLOUD_CONNECTION_DC_ATTACHMENT_IS_SUPPORT = "enterprise-cloud-connection-dc-attachment.is-support"
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
        r"""CloudConnectionCapabilityKeyEnum

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
        if not isinstance(other, CloudConnectionCapabilityKeyEnum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
