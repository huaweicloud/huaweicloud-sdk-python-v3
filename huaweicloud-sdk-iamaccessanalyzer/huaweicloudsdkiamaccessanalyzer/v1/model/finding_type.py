# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FindingType:
    """
    allowed enum values
    """
    EXTERNAL_ACCESS = "external_access"
    PRIVILEGE_ESCALATION = "privilege_escalation"
    UNUSED_IAM_USER_ACCESS_KEY = "unused_iam_user_access_key"
    UNUSED_IAM_USER_PASSWORD = "unused_iam_user_password"
    UNUSED_PERMISSION = "unused_permission"
    UNUSED_IAM_AGENCY = "unused_iam_agency"
    IAM_BP_ROOT_USER_HAS_ACCESS_KEY = "iam_bp_root_user_has_access_key"
    IAM_BP_ACCESS_API_WITH_PASSWORD = "iam_bp_access_api_with_password"
    IAM_BP_LOGIN_PROTECTION_DISABLED = "iam_bp_login_protection_disabled"
    IAM_BP_MFA_UNCONFIGURED = "iam_bp_mfa_unconfigured"
    IAM_BP_ASSIGN_HIGH_RISK_SYS_POLICY_OR_ROLE_TO_USER = "iam_bp_assign_high_risk_sys_policy_or_role_to_user"
    IAM_BP_ATTACH_HIGH_RISK_SYS_IDENTITY_POLICY_TO_USER = "iam_bp_attach_high_risk_sys_identity_policy_to_user"
    IAM_BP_ASSIGN_HIGH_RISK_SYS_POLICY_OR_ROLE_TO_AGENCY = "iam_bp_assign_high_risk_sys_policy_or_role_to_agency"
    IAM_BP_ATTACH_HIGH_RISK_SYS_IDENTITY_POLICY_TO_AGENCY = "iam_bp_attach_high_risk_sys_identity_policy_to_agency"
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
        r"""FindingType

        The model defined in huaweicloud sdk

        """
        
        
        self.discriminator = None

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
        if not isinstance(other, FindingType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
