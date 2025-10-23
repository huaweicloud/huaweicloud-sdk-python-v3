# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TemplateItemEnum:
    """
    allowed enum values
    """
    TASK_STATUS_PIE = "task-status-pie"
    TASK_TYPE_PIE = "task-type-pie"
    TASK_STATUS_REGION_COLUMN = "task-status-region-column"
    TASK_TYPE_REGION_COLUMN = "task-type-region-column"
    TASK_STATUS_TYPE_COLUMN = "task-status-type-column"
    TASK_STATUS_RESOURCE_COLUMN = "task-status-resource-column"
    TASK_TREND_CURVE = "task-trend-curve"
    TASK_DETAILS = "task-details"
    RESOURCE_PROTECTION_PIE = "resource-protection-pie"
    RESOURCE_COMPLIANCE_PIE = "resource-compliance-pie"
    RESOURCE_PROTECTION_REGION_COLUMN = "resource-protection-region-column"
    RESOURCE_COMPLIANCE_REGION_COLUMN = "resource-compliance-region-column"
    RESOURCE_PROTECTION_TYPE_COLUMN = "resource-protection-type-column"
    RESOURCE_COMPLIANCE_TYPE_COLUMN = "resource-compliance-type-column"
    RESOURCE_COMPLIANCE_PROTECTION_COLUMN = "resource-compliance-protection-column"
    PROTECTED_RESOURCE_COMPLIANCE_TREND_CURVE = "protected-resource-compliance-trend-curve"
    UNPROTECTED_RESOURCE_COMPLIANCE_TREND_CURVE = "unprotected-resource-compliance-trend-curve"
    RESOURCE_TREND_CURVE = "resource-trend-curve"
    RESOURCE_DETAILS = "resource-details"
    VAULT_CAPACITY_PIE = "vault-capacity-pie"
    VAULT_TYPE_PIE = "vault-type-pie"
    VAULT_CAPACITY_REGION_COLUMN = "vault-capacity-region-column"
    VAULT_TYPE_REGION_COLUMN = "vault-type-region-column"
    VAULT_CAPACITY_TYPE_COLUMN = "vault-capacity-type-column"
    VAULT_USAGE_TREND_CURVE = "vault-usage-trend-curve"
    VAULT_DETAILS = "vault-details"
    BACKUP_STATUS_PIE = "backup-status-pie"
    BACKUP_TYPE_PIE = "backup-type-pie"
    BACKUP_TYPE_REGION_COLUMN = "backup-type-region-column"
    BACKUP_STATUS_REGION_COLUMN = "backup-status-region-column"
    BACKUP_STATUS_TYPE_COLUMN = "backup-status-type-column"
    BACKUP_TREND_CURVE = "backup-trend-curve"
    BACKUP_DETAILS = "backup-details"
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
        r"""TemplateItemEnum

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
        if not isinstance(other, TemplateItemEnum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
