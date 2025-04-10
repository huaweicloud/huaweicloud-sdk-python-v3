# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AggregatePolicyAssignmentsFilters:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'account_id': 'str',
        'compliance_state': 'str',
        'policy_assignment_name': 'str'
    }

    attribute_map = {
        'account_id': 'account_id',
        'compliance_state': 'compliance_state',
        'policy_assignment_name': 'policy_assignment_name'
    }

    def __init__(self, account_id=None, compliance_state=None, policy_assignment_name=None):
        r"""AggregatePolicyAssignmentsFilters

        The model defined in huaweicloud sdk

        :param account_id: 源帐号ID。
        :type account_id: str
        :param compliance_state: 合规结果。
        :type compliance_state: str
        :param policy_assignment_name: 合规规则名称
        :type policy_assignment_name: str
        """
        
        

        self._account_id = None
        self._compliance_state = None
        self._policy_assignment_name = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if compliance_state is not None:
            self.compliance_state = compliance_state
        if policy_assignment_name is not None:
            self.policy_assignment_name = policy_assignment_name

    @property
    def account_id(self):
        r"""Gets the account_id of this AggregatePolicyAssignmentsFilters.

        源帐号ID。

        :return: The account_id of this AggregatePolicyAssignmentsFilters.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        r"""Sets the account_id of this AggregatePolicyAssignmentsFilters.

        源帐号ID。

        :param account_id: The account_id of this AggregatePolicyAssignmentsFilters.
        :type account_id: str
        """
        self._account_id = account_id

    @property
    def compliance_state(self):
        r"""Gets the compliance_state of this AggregatePolicyAssignmentsFilters.

        合规结果。

        :return: The compliance_state of this AggregatePolicyAssignmentsFilters.
        :rtype: str
        """
        return self._compliance_state

    @compliance_state.setter
    def compliance_state(self, compliance_state):
        r"""Sets the compliance_state of this AggregatePolicyAssignmentsFilters.

        合规结果。

        :param compliance_state: The compliance_state of this AggregatePolicyAssignmentsFilters.
        :type compliance_state: str
        """
        self._compliance_state = compliance_state

    @property
    def policy_assignment_name(self):
        r"""Gets the policy_assignment_name of this AggregatePolicyAssignmentsFilters.

        合规规则名称

        :return: The policy_assignment_name of this AggregatePolicyAssignmentsFilters.
        :rtype: str
        """
        return self._policy_assignment_name

    @policy_assignment_name.setter
    def policy_assignment_name(self, policy_assignment_name):
        r"""Sets the policy_assignment_name of this AggregatePolicyAssignmentsFilters.

        合规规则名称

        :param policy_assignment_name: The policy_assignment_name of this AggregatePolicyAssignmentsFilters.
        :type policy_assignment_name: str
        """
        self._policy_assignment_name = policy_assignment_name

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
        if not isinstance(other, AggregatePolicyAssignmentsFilters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
