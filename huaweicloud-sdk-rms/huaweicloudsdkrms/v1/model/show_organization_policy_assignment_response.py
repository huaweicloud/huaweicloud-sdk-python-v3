# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOrganizationPolicyAssignmentResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'owner_id': 'str',
        'organization_id': 'str',
        'organization_policy_assignment_urn': 'str',
        'organization_policy_assignment_id': 'str',
        'organization_policy_assignment_name': 'str',
        'excluded_accounts': 'list[str]',
        'description': 'str',
        'period': 'str',
        'policy_filter': 'PolicyFilterDefinition',
        'parameters': 'dict(str, PolicyParameterValue)',
        'policy_definition_id': 'str',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'owner_id': 'owner_id',
        'organization_id': 'organization_id',
        'organization_policy_assignment_urn': 'organization_policy_assignment_urn',
        'organization_policy_assignment_id': 'organization_policy_assignment_id',
        'organization_policy_assignment_name': 'organization_policy_assignment_name',
        'excluded_accounts': 'excluded_accounts',
        'description': 'description',
        'period': 'period',
        'policy_filter': 'policy_filter',
        'parameters': 'parameters',
        'policy_definition_id': 'policy_definition_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, owner_id=None, organization_id=None, organization_policy_assignment_urn=None, organization_policy_assignment_id=None, organization_policy_assignment_name=None, excluded_accounts=None, description=None, period=None, policy_filter=None, parameters=None, policy_definition_id=None, created_at=None, updated_at=None):
        r"""ShowOrganizationPolicyAssignmentResponse

        The model defined in huaweicloud sdk

        :param owner_id: 组织合规规则创建者。
        :type owner_id: str
        :param organization_id: 组织ID。
        :type organization_id: str
        :param organization_policy_assignment_urn: 组织合规规则资源唯一标识。
        :type organization_policy_assignment_urn: str
        :param organization_policy_assignment_id: 组织合规规则ID。
        :type organization_policy_assignment_id: str
        :param organization_policy_assignment_name: 组织合规规则名称。
        :type organization_policy_assignment_name: str
        :param excluded_accounts: 排除配置规则的帐号。
        :type excluded_accounts: list[str]
        :param description: 描述信息。
        :type description: str
        :param period: 触发周期。
        :type period: str
        :param policy_filter: 
        :type policy_filter: :class:`huaweicloudsdkrms.v1.PolicyFilterDefinition`
        :param parameters: 规则参数。
        :type parameters: dict(str, PolicyParameterValue)
        :param policy_definition_id: 策略ID。
        :type policy_definition_id: str
        :param created_at: 创建时间。
        :type created_at: str
        :param updated_at: 更新时间。
        :type updated_at: str
        """
        
        super(ShowOrganizationPolicyAssignmentResponse, self).__init__()

        self._owner_id = None
        self._organization_id = None
        self._organization_policy_assignment_urn = None
        self._organization_policy_assignment_id = None
        self._organization_policy_assignment_name = None
        self._excluded_accounts = None
        self._description = None
        self._period = None
        self._policy_filter = None
        self._parameters = None
        self._policy_definition_id = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if owner_id is not None:
            self.owner_id = owner_id
        if organization_id is not None:
            self.organization_id = organization_id
        if organization_policy_assignment_urn is not None:
            self.organization_policy_assignment_urn = organization_policy_assignment_urn
        if organization_policy_assignment_id is not None:
            self.organization_policy_assignment_id = organization_policy_assignment_id
        if organization_policy_assignment_name is not None:
            self.organization_policy_assignment_name = organization_policy_assignment_name
        if excluded_accounts is not None:
            self.excluded_accounts = excluded_accounts
        if description is not None:
            self.description = description
        if period is not None:
            self.period = period
        if policy_filter is not None:
            self.policy_filter = policy_filter
        if parameters is not None:
            self.parameters = parameters
        if policy_definition_id is not None:
            self.policy_definition_id = policy_definition_id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def owner_id(self):
        r"""Gets the owner_id of this ShowOrganizationPolicyAssignmentResponse.

        组织合规规则创建者。

        :return: The owner_id of this ShowOrganizationPolicyAssignmentResponse.
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        r"""Sets the owner_id of this ShowOrganizationPolicyAssignmentResponse.

        组织合规规则创建者。

        :param owner_id: The owner_id of this ShowOrganizationPolicyAssignmentResponse.
        :type owner_id: str
        """
        self._owner_id = owner_id

    @property
    def organization_id(self):
        r"""Gets the organization_id of this ShowOrganizationPolicyAssignmentResponse.

        组织ID。

        :return: The organization_id of this ShowOrganizationPolicyAssignmentResponse.
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        r"""Sets the organization_id of this ShowOrganizationPolicyAssignmentResponse.

        组织ID。

        :param organization_id: The organization_id of this ShowOrganizationPolicyAssignmentResponse.
        :type organization_id: str
        """
        self._organization_id = organization_id

    @property
    def organization_policy_assignment_urn(self):
        r"""Gets the organization_policy_assignment_urn of this ShowOrganizationPolicyAssignmentResponse.

        组织合规规则资源唯一标识。

        :return: The organization_policy_assignment_urn of this ShowOrganizationPolicyAssignmentResponse.
        :rtype: str
        """
        return self._organization_policy_assignment_urn

    @organization_policy_assignment_urn.setter
    def organization_policy_assignment_urn(self, organization_policy_assignment_urn):
        r"""Sets the organization_policy_assignment_urn of this ShowOrganizationPolicyAssignmentResponse.

        组织合规规则资源唯一标识。

        :param organization_policy_assignment_urn: The organization_policy_assignment_urn of this ShowOrganizationPolicyAssignmentResponse.
        :type organization_policy_assignment_urn: str
        """
        self._organization_policy_assignment_urn = organization_policy_assignment_urn

    @property
    def organization_policy_assignment_id(self):
        r"""Gets the organization_policy_assignment_id of this ShowOrganizationPolicyAssignmentResponse.

        组织合规规则ID。

        :return: The organization_policy_assignment_id of this ShowOrganizationPolicyAssignmentResponse.
        :rtype: str
        """
        return self._organization_policy_assignment_id

    @organization_policy_assignment_id.setter
    def organization_policy_assignment_id(self, organization_policy_assignment_id):
        r"""Sets the organization_policy_assignment_id of this ShowOrganizationPolicyAssignmentResponse.

        组织合规规则ID。

        :param organization_policy_assignment_id: The organization_policy_assignment_id of this ShowOrganizationPolicyAssignmentResponse.
        :type organization_policy_assignment_id: str
        """
        self._organization_policy_assignment_id = organization_policy_assignment_id

    @property
    def organization_policy_assignment_name(self):
        r"""Gets the organization_policy_assignment_name of this ShowOrganizationPolicyAssignmentResponse.

        组织合规规则名称。

        :return: The organization_policy_assignment_name of this ShowOrganizationPolicyAssignmentResponse.
        :rtype: str
        """
        return self._organization_policy_assignment_name

    @organization_policy_assignment_name.setter
    def organization_policy_assignment_name(self, organization_policy_assignment_name):
        r"""Sets the organization_policy_assignment_name of this ShowOrganizationPolicyAssignmentResponse.

        组织合规规则名称。

        :param organization_policy_assignment_name: The organization_policy_assignment_name of this ShowOrganizationPolicyAssignmentResponse.
        :type organization_policy_assignment_name: str
        """
        self._organization_policy_assignment_name = organization_policy_assignment_name

    @property
    def excluded_accounts(self):
        r"""Gets the excluded_accounts of this ShowOrganizationPolicyAssignmentResponse.

        排除配置规则的帐号。

        :return: The excluded_accounts of this ShowOrganizationPolicyAssignmentResponse.
        :rtype: list[str]
        """
        return self._excluded_accounts

    @excluded_accounts.setter
    def excluded_accounts(self, excluded_accounts):
        r"""Sets the excluded_accounts of this ShowOrganizationPolicyAssignmentResponse.

        排除配置规则的帐号。

        :param excluded_accounts: The excluded_accounts of this ShowOrganizationPolicyAssignmentResponse.
        :type excluded_accounts: list[str]
        """
        self._excluded_accounts = excluded_accounts

    @property
    def description(self):
        r"""Gets the description of this ShowOrganizationPolicyAssignmentResponse.

        描述信息。

        :return: The description of this ShowOrganizationPolicyAssignmentResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowOrganizationPolicyAssignmentResponse.

        描述信息。

        :param description: The description of this ShowOrganizationPolicyAssignmentResponse.
        :type description: str
        """
        self._description = description

    @property
    def period(self):
        r"""Gets the period of this ShowOrganizationPolicyAssignmentResponse.

        触发周期。

        :return: The period of this ShowOrganizationPolicyAssignmentResponse.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        r"""Sets the period of this ShowOrganizationPolicyAssignmentResponse.

        触发周期。

        :param period: The period of this ShowOrganizationPolicyAssignmentResponse.
        :type period: str
        """
        self._period = period

    @property
    def policy_filter(self):
        r"""Gets the policy_filter of this ShowOrganizationPolicyAssignmentResponse.

        :return: The policy_filter of this ShowOrganizationPolicyAssignmentResponse.
        :rtype: :class:`huaweicloudsdkrms.v1.PolicyFilterDefinition`
        """
        return self._policy_filter

    @policy_filter.setter
    def policy_filter(self, policy_filter):
        r"""Sets the policy_filter of this ShowOrganizationPolicyAssignmentResponse.

        :param policy_filter: The policy_filter of this ShowOrganizationPolicyAssignmentResponse.
        :type policy_filter: :class:`huaweicloudsdkrms.v1.PolicyFilterDefinition`
        """
        self._policy_filter = policy_filter

    @property
    def parameters(self):
        r"""Gets the parameters of this ShowOrganizationPolicyAssignmentResponse.

        规则参数。

        :return: The parameters of this ShowOrganizationPolicyAssignmentResponse.
        :rtype: dict(str, PolicyParameterValue)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        r"""Sets the parameters of this ShowOrganizationPolicyAssignmentResponse.

        规则参数。

        :param parameters: The parameters of this ShowOrganizationPolicyAssignmentResponse.
        :type parameters: dict(str, PolicyParameterValue)
        """
        self._parameters = parameters

    @property
    def policy_definition_id(self):
        r"""Gets the policy_definition_id of this ShowOrganizationPolicyAssignmentResponse.

        策略ID。

        :return: The policy_definition_id of this ShowOrganizationPolicyAssignmentResponse.
        :rtype: str
        """
        return self._policy_definition_id

    @policy_definition_id.setter
    def policy_definition_id(self, policy_definition_id):
        r"""Sets the policy_definition_id of this ShowOrganizationPolicyAssignmentResponse.

        策略ID。

        :param policy_definition_id: The policy_definition_id of this ShowOrganizationPolicyAssignmentResponse.
        :type policy_definition_id: str
        """
        self._policy_definition_id = policy_definition_id

    @property
    def created_at(self):
        r"""Gets the created_at of this ShowOrganizationPolicyAssignmentResponse.

        创建时间。

        :return: The created_at of this ShowOrganizationPolicyAssignmentResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ShowOrganizationPolicyAssignmentResponse.

        创建时间。

        :param created_at: The created_at of this ShowOrganizationPolicyAssignmentResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ShowOrganizationPolicyAssignmentResponse.

        更新时间。

        :return: The updated_at of this ShowOrganizationPolicyAssignmentResponse.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ShowOrganizationPolicyAssignmentResponse.

        更新时间。

        :param updated_at: The updated_at of this ShowOrganizationPolicyAssignmentResponse.
        :type updated_at: str
        """
        self._updated_at = updated_at

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
        if not isinstance(other, ShowOrganizationPolicyAssignmentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
