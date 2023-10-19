# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CentralNetworkQuotaKeyEnum:
    """
    allowed enum values
    """
    CENTRAL_NETWORKS_PER_ACCOUNT = "central_networks_per_account"
    POLICY_VERSIONS_PER_CENTRAL_NETWORK = "policy_versions_per_central_network"
    SIZE_OF_DOCUMENT_PER_CENTRAL_NETWORK_POLICY_VERSION = "size_of_document_per_central_network_policy_version"
    PLANES_PER_CENTRAL_NETWORK = "planes_per_central_network"
    ER_INSTANCES_PER_REGION_PER_CENTRAL_NETWORK = "er_instances_per_region_per_central_network"
    CONNECTIONS_PER_CENTRAL_NETWORK = "connections_per_central_network"
    ATTACHMENTS_PER_CENTRAL_NETWORK = "attachments_per_central_network"
    GDGW_ATTACHMENTS_PER_REGION_PER_CENTRAL_NETWORK = "GDGW_attachments_per_region_per_central_network"
    ER_ROUTE_TABLE_ATTACHMENTS_PER_REGION_PER_CENTRAL_NETWORK = "ER_ROUTE_TABLE_attachments_per_region_per_central_network"
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
        """CentralNetworkQuotaKeyEnum

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
        if not isinstance(other, CentralNetworkQuotaKeyEnum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
