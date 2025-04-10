# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AggregatePolicyAssignments:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_assignment_id': 'str',
        'policy_assignment_name': 'str',
        'compliance': 'Compliance',
        'account_id': 'str',
        'account_name': 'str'
    }

    attribute_map = {
        'policy_assignment_id': 'policy_assignment_id',
        'policy_assignment_name': 'policy_assignment_name',
        'compliance': 'compliance',
        'account_id': 'account_id',
        'account_name': 'account_name'
    }

    def __init__(self, policy_assignment_id=None, policy_assignment_name=None, compliance=None, account_id=None, account_name=None):
        r"""AggregatePolicyAssignments

        The model defined in huaweicloud sdk

        :param policy_assignment_id: 合规规则ID
        :type policy_assignment_id: str
        :param policy_assignment_name: 合规规则名称
        :type policy_assignment_name: str
        :param compliance: 
        :type compliance: :class:`huaweicloudsdkconfig.v1.Compliance`
        :param account_id: 源帐号ID。
        :type account_id: str
        :param account_name: 帐户名称
        :type account_name: str
        """
        
        

        self._policy_assignment_id = None
        self._policy_assignment_name = None
        self._compliance = None
        self._account_id = None
        self._account_name = None
        self.discriminator = None

        if policy_assignment_id is not None:
            self.policy_assignment_id = policy_assignment_id
        if policy_assignment_name is not None:
            self.policy_assignment_name = policy_assignment_name
        if compliance is not None:
            self.compliance = compliance
        if account_id is not None:
            self.account_id = account_id
        if account_name is not None:
            self.account_name = account_name

    @property
    def policy_assignment_id(self):
        r"""Gets the policy_assignment_id of this AggregatePolicyAssignments.

        合规规则ID

        :return: The policy_assignment_id of this AggregatePolicyAssignments.
        :rtype: str
        """
        return self._policy_assignment_id

    @policy_assignment_id.setter
    def policy_assignment_id(self, policy_assignment_id):
        r"""Sets the policy_assignment_id of this AggregatePolicyAssignments.

        合规规则ID

        :param policy_assignment_id: The policy_assignment_id of this AggregatePolicyAssignments.
        :type policy_assignment_id: str
        """
        self._policy_assignment_id = policy_assignment_id

    @property
    def policy_assignment_name(self):
        r"""Gets the policy_assignment_name of this AggregatePolicyAssignments.

        合规规则名称

        :return: The policy_assignment_name of this AggregatePolicyAssignments.
        :rtype: str
        """
        return self._policy_assignment_name

    @policy_assignment_name.setter
    def policy_assignment_name(self, policy_assignment_name):
        r"""Sets the policy_assignment_name of this AggregatePolicyAssignments.

        合规规则名称

        :param policy_assignment_name: The policy_assignment_name of this AggregatePolicyAssignments.
        :type policy_assignment_name: str
        """
        self._policy_assignment_name = policy_assignment_name

    @property
    def compliance(self):
        r"""Gets the compliance of this AggregatePolicyAssignments.

        :return: The compliance of this AggregatePolicyAssignments.
        :rtype: :class:`huaweicloudsdkconfig.v1.Compliance`
        """
        return self._compliance

    @compliance.setter
    def compliance(self, compliance):
        r"""Sets the compliance of this AggregatePolicyAssignments.

        :param compliance: The compliance of this AggregatePolicyAssignments.
        :type compliance: :class:`huaweicloudsdkconfig.v1.Compliance`
        """
        self._compliance = compliance

    @property
    def account_id(self):
        r"""Gets the account_id of this AggregatePolicyAssignments.

        源帐号ID。

        :return: The account_id of this AggregatePolicyAssignments.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        r"""Sets the account_id of this AggregatePolicyAssignments.

        源帐号ID。

        :param account_id: The account_id of this AggregatePolicyAssignments.
        :type account_id: str
        """
        self._account_id = account_id

    @property
    def account_name(self):
        r"""Gets the account_name of this AggregatePolicyAssignments.

        帐户名称

        :return: The account_name of this AggregatePolicyAssignments.
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        r"""Sets the account_name of this AggregatePolicyAssignments.

        帐户名称

        :param account_name: The account_name of this AggregatePolicyAssignments.
        :type account_name: str
        """
        self._account_name = account_name

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
        if not isinstance(other, AggregatePolicyAssignments):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
