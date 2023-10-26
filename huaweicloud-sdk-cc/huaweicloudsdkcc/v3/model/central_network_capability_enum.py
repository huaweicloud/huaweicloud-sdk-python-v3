# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CentralNetworkCapabilityEnum:
    """
    allowed enum values
    """
    CENTRAL_NETWORK_IS_SUPPORT = "central-network.is-support"
    CENTRAL_NETWORK_IS_SUPPORT_ENTERPRISE_PROJECT = "central-network.is-support-enterprise-project"
    CENTRAL_NETWORK_IS_SUPPORT_TAG = "central-network.is-support-tag"
    CONNECTION_BANDWIDTH_SIZE_RANGE = "connection-bandwidth.size-range"
    CONNECTION_BANDWIDTH_CHARGE_MODE = "connection-bandwidth.charge-mode"
    ER_INSTANCE_SUPPORT_REGIONS = "er-instance.support-regions"
    ER_INSTANCE_SUPPORT_IPV6_REGIONS = "er-instance.support-ipv6-regions"
    ER_INSTANCE_SUPPORT_DSCP_REGIONS = "er-instance.support-dscp-regions"
    ER_INSTANCE_SUPPORT_SITES = "er-instance.support-sites"
    GDGW_ATTACHMENT_IS_SUPPORT = "gdgw-attachment.is-support"
    GDGW_ATTACHMENT_SUPPORT_REGIONS = "gdgw-attachment.support-regions"
    GDGW_ATTACHMENT_SUPPORT_SITES = "gdgw-attachment.support-sites"
    ER_ROUTE_TABLE_ATTACHMENT_IS_SUPPORT = "er-route-table-attachment.is-support"
    ER_ROUTE_TABLE_ATTACHMENT_SUPPORT_REGIONS = "er-route-table-attachment.support-regions"
    ER_ROUTE_TABLE_ATTACHMENT_SUPPORT_SITES = "er-route-table-attachment.support-sites"
    CLOUD_ALLIANCE_SUPPORT_REGIONS = "cloud-alliance.support-regions"
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
        """CentralNetworkCapabilityEnum

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
        if not isinstance(other, CentralNetworkCapabilityEnum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
