# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FindingDetails:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'external_access_details': 'ExternalAccessDetails',
        'privilege_escalation_details': 'PrivilegeEscalationDetails',
        'unused_iam_user_access_key_details': 'UnusedIamUserAccessKeyDetails',
        'unused_iam_user_password_details': 'UnusedIamUserPasswordDetails',
        'unused_permission_details': 'UnusedPermissionDetails',
        'unused_iam_agency_details': 'UnusedIamAgencyDetails',
        'iam_bp_root_user_has_access_key_details': 'IamBpRootUserHasAccessKeyDetails',
        'iam_bp_access_api_with_password_details': 'IamBpAccessApiWithPasswordDetails',
        'iam_bp_login_protection_disabled_details': 'IamBpLoginProtectionDisabledDetails',
        'iam_bp_mfa_unconfigured_details': 'IamBpMfaUnconfiguredDetails',
        'iam_bp_assign_high_risk_sys_policy_or_role_to_user_details': 'IamBpAssignHighRiskSysPolicyOrRoleToUserDetails',
        'iam_bp_attach_high_risk_sys_identity_policy_to_user_details': 'IamBpAttachHighRiskSysIdentityPolicyToUserDetails',
        'iam_bp_assign_high_risk_sys_policy_or_role_to_agency_details': 'IamBpAssignHighRiskSysPolicyOrRoleToAgencyDetails',
        'iam_bp_attach_high_risk_sys_identity_policy_to_agency_details': 'IamBpAttachHighRiskSysIdentityPolicyToAgencyDetails'
    }

    attribute_map = {
        'external_access_details': 'external_access_details',
        'privilege_escalation_details': 'privilege_escalation_details',
        'unused_iam_user_access_key_details': 'unused_iam_user_access_key_details',
        'unused_iam_user_password_details': 'unused_iam_user_password_details',
        'unused_permission_details': 'unused_permission_details',
        'unused_iam_agency_details': 'unused_iam_agency_details',
        'iam_bp_root_user_has_access_key_details': 'iam_bp_root_user_has_access_key_details',
        'iam_bp_access_api_with_password_details': 'iam_bp_access_api_with_password_details',
        'iam_bp_login_protection_disabled_details': 'iam_bp_login_protection_disabled_details',
        'iam_bp_mfa_unconfigured_details': 'iam_bp_mfa_unconfigured_details',
        'iam_bp_assign_high_risk_sys_policy_or_role_to_user_details': 'iam_bp_assign_high_risk_sys_policy_or_role_to_user_details',
        'iam_bp_attach_high_risk_sys_identity_policy_to_user_details': 'iam_bp_attach_high_risk_sys_identity_policy_to_user_details',
        'iam_bp_assign_high_risk_sys_policy_or_role_to_agency_details': 'iam_bp_assign_high_risk_sys_policy_or_role_to_agency_details',
        'iam_bp_attach_high_risk_sys_identity_policy_to_agency_details': 'iam_bp_attach_high_risk_sys_identity_policy_to_agency_details'
    }

    def __init__(self, external_access_details=None, privilege_escalation_details=None, unused_iam_user_access_key_details=None, unused_iam_user_password_details=None, unused_permission_details=None, unused_iam_agency_details=None, iam_bp_root_user_has_access_key_details=None, iam_bp_access_api_with_password_details=None, iam_bp_login_protection_disabled_details=None, iam_bp_mfa_unconfigured_details=None, iam_bp_assign_high_risk_sys_policy_or_role_to_user_details=None, iam_bp_attach_high_risk_sys_identity_policy_to_user_details=None, iam_bp_assign_high_risk_sys_policy_or_role_to_agency_details=None, iam_bp_attach_high_risk_sys_identity_policy_to_agency_details=None):
        r"""FindingDetails

        The model defined in huaweicloud sdk

        :param external_access_details: 
        :type external_access_details: :class:`huaweicloudsdkiamaccessanalyzer.v1.ExternalAccessDetails`
        :param privilege_escalation_details: 
        :type privilege_escalation_details: :class:`huaweicloudsdkiamaccessanalyzer.v1.PrivilegeEscalationDetails`
        :param unused_iam_user_access_key_details: 
        :type unused_iam_user_access_key_details: :class:`huaweicloudsdkiamaccessanalyzer.v1.UnusedIamUserAccessKeyDetails`
        :param unused_iam_user_password_details: 
        :type unused_iam_user_password_details: :class:`huaweicloudsdkiamaccessanalyzer.v1.UnusedIamUserPasswordDetails`
        :param unused_permission_details: 
        :type unused_permission_details: :class:`huaweicloudsdkiamaccessanalyzer.v1.UnusedPermissionDetails`
        :param unused_iam_agency_details: 
        :type unused_iam_agency_details: :class:`huaweicloudsdkiamaccessanalyzer.v1.UnusedIamAgencyDetails`
        :param iam_bp_root_user_has_access_key_details: 
        :type iam_bp_root_user_has_access_key_details: :class:`huaweicloudsdkiamaccessanalyzer.v1.IamBpRootUserHasAccessKeyDetails`
        :param iam_bp_access_api_with_password_details: 
        :type iam_bp_access_api_with_password_details: :class:`huaweicloudsdkiamaccessanalyzer.v1.IamBpAccessApiWithPasswordDetails`
        :param iam_bp_login_protection_disabled_details: 
        :type iam_bp_login_protection_disabled_details: :class:`huaweicloudsdkiamaccessanalyzer.v1.IamBpLoginProtectionDisabledDetails`
        :param iam_bp_mfa_unconfigured_details: 
        :type iam_bp_mfa_unconfigured_details: :class:`huaweicloudsdkiamaccessanalyzer.v1.IamBpMfaUnconfiguredDetails`
        :param iam_bp_assign_high_risk_sys_policy_or_role_to_user_details: 
        :type iam_bp_assign_high_risk_sys_policy_or_role_to_user_details: :class:`huaweicloudsdkiamaccessanalyzer.v1.IamBpAssignHighRiskSysPolicyOrRoleToUserDetails`
        :param iam_bp_attach_high_risk_sys_identity_policy_to_user_details: 
        :type iam_bp_attach_high_risk_sys_identity_policy_to_user_details: :class:`huaweicloudsdkiamaccessanalyzer.v1.IamBpAttachHighRiskSysIdentityPolicyToUserDetails`
        :param iam_bp_assign_high_risk_sys_policy_or_role_to_agency_details: 
        :type iam_bp_assign_high_risk_sys_policy_or_role_to_agency_details: :class:`huaweicloudsdkiamaccessanalyzer.v1.IamBpAssignHighRiskSysPolicyOrRoleToAgencyDetails`
        :param iam_bp_attach_high_risk_sys_identity_policy_to_agency_details: 
        :type iam_bp_attach_high_risk_sys_identity_policy_to_agency_details: :class:`huaweicloudsdkiamaccessanalyzer.v1.IamBpAttachHighRiskSysIdentityPolicyToAgencyDetails`
        """
        
        

        self._external_access_details = None
        self._privilege_escalation_details = None
        self._unused_iam_user_access_key_details = None
        self._unused_iam_user_password_details = None
        self._unused_permission_details = None
        self._unused_iam_agency_details = None
        self._iam_bp_root_user_has_access_key_details = None
        self._iam_bp_access_api_with_password_details = None
        self._iam_bp_login_protection_disabled_details = None
        self._iam_bp_mfa_unconfigured_details = None
        self._iam_bp_assign_high_risk_sys_policy_or_role_to_user_details = None
        self._iam_bp_attach_high_risk_sys_identity_policy_to_user_details = None
        self._iam_bp_assign_high_risk_sys_policy_or_role_to_agency_details = None
        self._iam_bp_attach_high_risk_sys_identity_policy_to_agency_details = None
        self.discriminator = None

        if external_access_details is not None:
            self.external_access_details = external_access_details
        if privilege_escalation_details is not None:
            self.privilege_escalation_details = privilege_escalation_details
        if unused_iam_user_access_key_details is not None:
            self.unused_iam_user_access_key_details = unused_iam_user_access_key_details
        if unused_iam_user_password_details is not None:
            self.unused_iam_user_password_details = unused_iam_user_password_details
        if unused_permission_details is not None:
            self.unused_permission_details = unused_permission_details
        if unused_iam_agency_details is not None:
            self.unused_iam_agency_details = unused_iam_agency_details
        if iam_bp_root_user_has_access_key_details is not None:
            self.iam_bp_root_user_has_access_key_details = iam_bp_root_user_has_access_key_details
        if iam_bp_access_api_with_password_details is not None:
            self.iam_bp_access_api_with_password_details = iam_bp_access_api_with_password_details
        if iam_bp_login_protection_disabled_details is not None:
            self.iam_bp_login_protection_disabled_details = iam_bp_login_protection_disabled_details
        if iam_bp_mfa_unconfigured_details is not None:
            self.iam_bp_mfa_unconfigured_details = iam_bp_mfa_unconfigured_details
        if iam_bp_assign_high_risk_sys_policy_or_role_to_user_details is not None:
            self.iam_bp_assign_high_risk_sys_policy_or_role_to_user_details = iam_bp_assign_high_risk_sys_policy_or_role_to_user_details
        if iam_bp_attach_high_risk_sys_identity_policy_to_user_details is not None:
            self.iam_bp_attach_high_risk_sys_identity_policy_to_user_details = iam_bp_attach_high_risk_sys_identity_policy_to_user_details
        if iam_bp_assign_high_risk_sys_policy_or_role_to_agency_details is not None:
            self.iam_bp_assign_high_risk_sys_policy_or_role_to_agency_details = iam_bp_assign_high_risk_sys_policy_or_role_to_agency_details
        if iam_bp_attach_high_risk_sys_identity_policy_to_agency_details is not None:
            self.iam_bp_attach_high_risk_sys_identity_policy_to_agency_details = iam_bp_attach_high_risk_sys_identity_policy_to_agency_details

    @property
    def external_access_details(self):
        r"""Gets the external_access_details of this FindingDetails.

        :return: The external_access_details of this FindingDetails.
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.ExternalAccessDetails`
        """
        return self._external_access_details

    @external_access_details.setter
    def external_access_details(self, external_access_details):
        r"""Sets the external_access_details of this FindingDetails.

        :param external_access_details: The external_access_details of this FindingDetails.
        :type external_access_details: :class:`huaweicloudsdkiamaccessanalyzer.v1.ExternalAccessDetails`
        """
        self._external_access_details = external_access_details

    @property
    def privilege_escalation_details(self):
        r"""Gets the privilege_escalation_details of this FindingDetails.

        :return: The privilege_escalation_details of this FindingDetails.
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.PrivilegeEscalationDetails`
        """
        return self._privilege_escalation_details

    @privilege_escalation_details.setter
    def privilege_escalation_details(self, privilege_escalation_details):
        r"""Sets the privilege_escalation_details of this FindingDetails.

        :param privilege_escalation_details: The privilege_escalation_details of this FindingDetails.
        :type privilege_escalation_details: :class:`huaweicloudsdkiamaccessanalyzer.v1.PrivilegeEscalationDetails`
        """
        self._privilege_escalation_details = privilege_escalation_details

    @property
    def unused_iam_user_access_key_details(self):
        r"""Gets the unused_iam_user_access_key_details of this FindingDetails.

        :return: The unused_iam_user_access_key_details of this FindingDetails.
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.UnusedIamUserAccessKeyDetails`
        """
        return self._unused_iam_user_access_key_details

    @unused_iam_user_access_key_details.setter
    def unused_iam_user_access_key_details(self, unused_iam_user_access_key_details):
        r"""Sets the unused_iam_user_access_key_details of this FindingDetails.

        :param unused_iam_user_access_key_details: The unused_iam_user_access_key_details of this FindingDetails.
        :type unused_iam_user_access_key_details: :class:`huaweicloudsdkiamaccessanalyzer.v1.UnusedIamUserAccessKeyDetails`
        """
        self._unused_iam_user_access_key_details = unused_iam_user_access_key_details

    @property
    def unused_iam_user_password_details(self):
        r"""Gets the unused_iam_user_password_details of this FindingDetails.

        :return: The unused_iam_user_password_details of this FindingDetails.
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.UnusedIamUserPasswordDetails`
        """
        return self._unused_iam_user_password_details

    @unused_iam_user_password_details.setter
    def unused_iam_user_password_details(self, unused_iam_user_password_details):
        r"""Sets the unused_iam_user_password_details of this FindingDetails.

        :param unused_iam_user_password_details: The unused_iam_user_password_details of this FindingDetails.
        :type unused_iam_user_password_details: :class:`huaweicloudsdkiamaccessanalyzer.v1.UnusedIamUserPasswordDetails`
        """
        self._unused_iam_user_password_details = unused_iam_user_password_details

    @property
    def unused_permission_details(self):
        r"""Gets the unused_permission_details of this FindingDetails.

        :return: The unused_permission_details of this FindingDetails.
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.UnusedPermissionDetails`
        """
        return self._unused_permission_details

    @unused_permission_details.setter
    def unused_permission_details(self, unused_permission_details):
        r"""Sets the unused_permission_details of this FindingDetails.

        :param unused_permission_details: The unused_permission_details of this FindingDetails.
        :type unused_permission_details: :class:`huaweicloudsdkiamaccessanalyzer.v1.UnusedPermissionDetails`
        """
        self._unused_permission_details = unused_permission_details

    @property
    def unused_iam_agency_details(self):
        r"""Gets the unused_iam_agency_details of this FindingDetails.

        :return: The unused_iam_agency_details of this FindingDetails.
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.UnusedIamAgencyDetails`
        """
        return self._unused_iam_agency_details

    @unused_iam_agency_details.setter
    def unused_iam_agency_details(self, unused_iam_agency_details):
        r"""Sets the unused_iam_agency_details of this FindingDetails.

        :param unused_iam_agency_details: The unused_iam_agency_details of this FindingDetails.
        :type unused_iam_agency_details: :class:`huaweicloudsdkiamaccessanalyzer.v1.UnusedIamAgencyDetails`
        """
        self._unused_iam_agency_details = unused_iam_agency_details

    @property
    def iam_bp_root_user_has_access_key_details(self):
        r"""Gets the iam_bp_root_user_has_access_key_details of this FindingDetails.

        :return: The iam_bp_root_user_has_access_key_details of this FindingDetails.
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.IamBpRootUserHasAccessKeyDetails`
        """
        return self._iam_bp_root_user_has_access_key_details

    @iam_bp_root_user_has_access_key_details.setter
    def iam_bp_root_user_has_access_key_details(self, iam_bp_root_user_has_access_key_details):
        r"""Sets the iam_bp_root_user_has_access_key_details of this FindingDetails.

        :param iam_bp_root_user_has_access_key_details: The iam_bp_root_user_has_access_key_details of this FindingDetails.
        :type iam_bp_root_user_has_access_key_details: :class:`huaweicloudsdkiamaccessanalyzer.v1.IamBpRootUserHasAccessKeyDetails`
        """
        self._iam_bp_root_user_has_access_key_details = iam_bp_root_user_has_access_key_details

    @property
    def iam_bp_access_api_with_password_details(self):
        r"""Gets the iam_bp_access_api_with_password_details of this FindingDetails.

        :return: The iam_bp_access_api_with_password_details of this FindingDetails.
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.IamBpAccessApiWithPasswordDetails`
        """
        return self._iam_bp_access_api_with_password_details

    @iam_bp_access_api_with_password_details.setter
    def iam_bp_access_api_with_password_details(self, iam_bp_access_api_with_password_details):
        r"""Sets the iam_bp_access_api_with_password_details of this FindingDetails.

        :param iam_bp_access_api_with_password_details: The iam_bp_access_api_with_password_details of this FindingDetails.
        :type iam_bp_access_api_with_password_details: :class:`huaweicloudsdkiamaccessanalyzer.v1.IamBpAccessApiWithPasswordDetails`
        """
        self._iam_bp_access_api_with_password_details = iam_bp_access_api_with_password_details

    @property
    def iam_bp_login_protection_disabled_details(self):
        r"""Gets the iam_bp_login_protection_disabled_details of this FindingDetails.

        :return: The iam_bp_login_protection_disabled_details of this FindingDetails.
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.IamBpLoginProtectionDisabledDetails`
        """
        return self._iam_bp_login_protection_disabled_details

    @iam_bp_login_protection_disabled_details.setter
    def iam_bp_login_protection_disabled_details(self, iam_bp_login_protection_disabled_details):
        r"""Sets the iam_bp_login_protection_disabled_details of this FindingDetails.

        :param iam_bp_login_protection_disabled_details: The iam_bp_login_protection_disabled_details of this FindingDetails.
        :type iam_bp_login_protection_disabled_details: :class:`huaweicloudsdkiamaccessanalyzer.v1.IamBpLoginProtectionDisabledDetails`
        """
        self._iam_bp_login_protection_disabled_details = iam_bp_login_protection_disabled_details

    @property
    def iam_bp_mfa_unconfigured_details(self):
        r"""Gets the iam_bp_mfa_unconfigured_details of this FindingDetails.

        :return: The iam_bp_mfa_unconfigured_details of this FindingDetails.
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.IamBpMfaUnconfiguredDetails`
        """
        return self._iam_bp_mfa_unconfigured_details

    @iam_bp_mfa_unconfigured_details.setter
    def iam_bp_mfa_unconfigured_details(self, iam_bp_mfa_unconfigured_details):
        r"""Sets the iam_bp_mfa_unconfigured_details of this FindingDetails.

        :param iam_bp_mfa_unconfigured_details: The iam_bp_mfa_unconfigured_details of this FindingDetails.
        :type iam_bp_mfa_unconfigured_details: :class:`huaweicloudsdkiamaccessanalyzer.v1.IamBpMfaUnconfiguredDetails`
        """
        self._iam_bp_mfa_unconfigured_details = iam_bp_mfa_unconfigured_details

    @property
    def iam_bp_assign_high_risk_sys_policy_or_role_to_user_details(self):
        r"""Gets the iam_bp_assign_high_risk_sys_policy_or_role_to_user_details of this FindingDetails.

        :return: The iam_bp_assign_high_risk_sys_policy_or_role_to_user_details of this FindingDetails.
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.IamBpAssignHighRiskSysPolicyOrRoleToUserDetails`
        """
        return self._iam_bp_assign_high_risk_sys_policy_or_role_to_user_details

    @iam_bp_assign_high_risk_sys_policy_or_role_to_user_details.setter
    def iam_bp_assign_high_risk_sys_policy_or_role_to_user_details(self, iam_bp_assign_high_risk_sys_policy_or_role_to_user_details):
        r"""Sets the iam_bp_assign_high_risk_sys_policy_or_role_to_user_details of this FindingDetails.

        :param iam_bp_assign_high_risk_sys_policy_or_role_to_user_details: The iam_bp_assign_high_risk_sys_policy_or_role_to_user_details of this FindingDetails.
        :type iam_bp_assign_high_risk_sys_policy_or_role_to_user_details: :class:`huaweicloudsdkiamaccessanalyzer.v1.IamBpAssignHighRiskSysPolicyOrRoleToUserDetails`
        """
        self._iam_bp_assign_high_risk_sys_policy_or_role_to_user_details = iam_bp_assign_high_risk_sys_policy_or_role_to_user_details

    @property
    def iam_bp_attach_high_risk_sys_identity_policy_to_user_details(self):
        r"""Gets the iam_bp_attach_high_risk_sys_identity_policy_to_user_details of this FindingDetails.

        :return: The iam_bp_attach_high_risk_sys_identity_policy_to_user_details of this FindingDetails.
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.IamBpAttachHighRiskSysIdentityPolicyToUserDetails`
        """
        return self._iam_bp_attach_high_risk_sys_identity_policy_to_user_details

    @iam_bp_attach_high_risk_sys_identity_policy_to_user_details.setter
    def iam_bp_attach_high_risk_sys_identity_policy_to_user_details(self, iam_bp_attach_high_risk_sys_identity_policy_to_user_details):
        r"""Sets the iam_bp_attach_high_risk_sys_identity_policy_to_user_details of this FindingDetails.

        :param iam_bp_attach_high_risk_sys_identity_policy_to_user_details: The iam_bp_attach_high_risk_sys_identity_policy_to_user_details of this FindingDetails.
        :type iam_bp_attach_high_risk_sys_identity_policy_to_user_details: :class:`huaweicloudsdkiamaccessanalyzer.v1.IamBpAttachHighRiskSysIdentityPolicyToUserDetails`
        """
        self._iam_bp_attach_high_risk_sys_identity_policy_to_user_details = iam_bp_attach_high_risk_sys_identity_policy_to_user_details

    @property
    def iam_bp_assign_high_risk_sys_policy_or_role_to_agency_details(self):
        r"""Gets the iam_bp_assign_high_risk_sys_policy_or_role_to_agency_details of this FindingDetails.

        :return: The iam_bp_assign_high_risk_sys_policy_or_role_to_agency_details of this FindingDetails.
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.IamBpAssignHighRiskSysPolicyOrRoleToAgencyDetails`
        """
        return self._iam_bp_assign_high_risk_sys_policy_or_role_to_agency_details

    @iam_bp_assign_high_risk_sys_policy_or_role_to_agency_details.setter
    def iam_bp_assign_high_risk_sys_policy_or_role_to_agency_details(self, iam_bp_assign_high_risk_sys_policy_or_role_to_agency_details):
        r"""Sets the iam_bp_assign_high_risk_sys_policy_or_role_to_agency_details of this FindingDetails.

        :param iam_bp_assign_high_risk_sys_policy_or_role_to_agency_details: The iam_bp_assign_high_risk_sys_policy_or_role_to_agency_details of this FindingDetails.
        :type iam_bp_assign_high_risk_sys_policy_or_role_to_agency_details: :class:`huaweicloudsdkiamaccessanalyzer.v1.IamBpAssignHighRiskSysPolicyOrRoleToAgencyDetails`
        """
        self._iam_bp_assign_high_risk_sys_policy_or_role_to_agency_details = iam_bp_assign_high_risk_sys_policy_or_role_to_agency_details

    @property
    def iam_bp_attach_high_risk_sys_identity_policy_to_agency_details(self):
        r"""Gets the iam_bp_attach_high_risk_sys_identity_policy_to_agency_details of this FindingDetails.

        :return: The iam_bp_attach_high_risk_sys_identity_policy_to_agency_details of this FindingDetails.
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.IamBpAttachHighRiskSysIdentityPolicyToAgencyDetails`
        """
        return self._iam_bp_attach_high_risk_sys_identity_policy_to_agency_details

    @iam_bp_attach_high_risk_sys_identity_policy_to_agency_details.setter
    def iam_bp_attach_high_risk_sys_identity_policy_to_agency_details(self, iam_bp_attach_high_risk_sys_identity_policy_to_agency_details):
        r"""Sets the iam_bp_attach_high_risk_sys_identity_policy_to_agency_details of this FindingDetails.

        :param iam_bp_attach_high_risk_sys_identity_policy_to_agency_details: The iam_bp_attach_high_risk_sys_identity_policy_to_agency_details of this FindingDetails.
        :type iam_bp_attach_high_risk_sys_identity_policy_to_agency_details: :class:`huaweicloudsdkiamaccessanalyzer.v1.IamBpAttachHighRiskSysIdentityPolicyToAgencyDetails`
        """
        self._iam_bp_attach_high_risk_sys_identity_policy_to_agency_details = iam_bp_attach_high_risk_sys_identity_policy_to_agency_details

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
        if not isinstance(other, FindingDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
