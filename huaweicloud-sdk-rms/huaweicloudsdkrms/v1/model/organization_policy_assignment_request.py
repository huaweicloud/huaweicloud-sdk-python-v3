# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OrganizationPolicyAssignmentRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'excluded_accounts': 'list[str]',
        'organization_policy_assignment_name': 'str',
        'managed_policy_assignment_metadata': 'ManagedPolicyAssignmentMetadata'
    }

    attribute_map = {
        'excluded_accounts': 'excluded_accounts',
        'organization_policy_assignment_name': 'organization_policy_assignment_name',
        'managed_policy_assignment_metadata': 'managed_policy_assignment_metadata'
    }

    def __init__(self, excluded_accounts=None, organization_policy_assignment_name=None, managed_policy_assignment_metadata=None):
        r"""OrganizationPolicyAssignmentRequest

        The model defined in huaweicloud sdk

        :param excluded_accounts: 需要排除配置规则的帐号。
        :type excluded_accounts: list[str]
        :param organization_policy_assignment_name: 组织合规规则名称。
        :type organization_policy_assignment_name: str
        :param managed_policy_assignment_metadata: 
        :type managed_policy_assignment_metadata: :class:`huaweicloudsdkrms.v1.ManagedPolicyAssignmentMetadata`
        """
        
        

        self._excluded_accounts = None
        self._organization_policy_assignment_name = None
        self._managed_policy_assignment_metadata = None
        self.discriminator = None

        if excluded_accounts is not None:
            self.excluded_accounts = excluded_accounts
        self.organization_policy_assignment_name = organization_policy_assignment_name
        if managed_policy_assignment_metadata is not None:
            self.managed_policy_assignment_metadata = managed_policy_assignment_metadata

    @property
    def excluded_accounts(self):
        r"""Gets the excluded_accounts of this OrganizationPolicyAssignmentRequest.

        需要排除配置规则的帐号。

        :return: The excluded_accounts of this OrganizationPolicyAssignmentRequest.
        :rtype: list[str]
        """
        return self._excluded_accounts

    @excluded_accounts.setter
    def excluded_accounts(self, excluded_accounts):
        r"""Sets the excluded_accounts of this OrganizationPolicyAssignmentRequest.

        需要排除配置规则的帐号。

        :param excluded_accounts: The excluded_accounts of this OrganizationPolicyAssignmentRequest.
        :type excluded_accounts: list[str]
        """
        self._excluded_accounts = excluded_accounts

    @property
    def organization_policy_assignment_name(self):
        r"""Gets the organization_policy_assignment_name of this OrganizationPolicyAssignmentRequest.

        组织合规规则名称。

        :return: The organization_policy_assignment_name of this OrganizationPolicyAssignmentRequest.
        :rtype: str
        """
        return self._organization_policy_assignment_name

    @organization_policy_assignment_name.setter
    def organization_policy_assignment_name(self, organization_policy_assignment_name):
        r"""Sets the organization_policy_assignment_name of this OrganizationPolicyAssignmentRequest.

        组织合规规则名称。

        :param organization_policy_assignment_name: The organization_policy_assignment_name of this OrganizationPolicyAssignmentRequest.
        :type organization_policy_assignment_name: str
        """
        self._organization_policy_assignment_name = organization_policy_assignment_name

    @property
    def managed_policy_assignment_metadata(self):
        r"""Gets the managed_policy_assignment_metadata of this OrganizationPolicyAssignmentRequest.

        :return: The managed_policy_assignment_metadata of this OrganizationPolicyAssignmentRequest.
        :rtype: :class:`huaweicloudsdkrms.v1.ManagedPolicyAssignmentMetadata`
        """
        return self._managed_policy_assignment_metadata

    @managed_policy_assignment_metadata.setter
    def managed_policy_assignment_metadata(self, managed_policy_assignment_metadata):
        r"""Sets the managed_policy_assignment_metadata of this OrganizationPolicyAssignmentRequest.

        :param managed_policy_assignment_metadata: The managed_policy_assignment_metadata of this OrganizationPolicyAssignmentRequest.
        :type managed_policy_assignment_metadata: :class:`huaweicloudsdkrms.v1.ManagedPolicyAssignmentMetadata`
        """
        self._managed_policy_assignment_metadata = managed_policy_assignment_metadata

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
        if not isinstance(other, OrganizationPolicyAssignmentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
