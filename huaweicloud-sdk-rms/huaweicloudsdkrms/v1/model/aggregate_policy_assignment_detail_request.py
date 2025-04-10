# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AggregatePolicyAssignmentDetailRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'aggregator_id': 'str',
        'account_id': 'str',
        'policy_assignment_id': 'str'
    }

    attribute_map = {
        'aggregator_id': 'aggregator_id',
        'account_id': 'account_id',
        'policy_assignment_id': 'policy_assignment_id'
    }

    def __init__(self, aggregator_id=None, account_id=None, policy_assignment_id=None):
        r"""AggregatePolicyAssignmentDetailRequest

        The model defined in huaweicloud sdk

        :param aggregator_id: 资源聚合器ID
        :type aggregator_id: str
        :param account_id: 租户ID
        :type account_id: str
        :param policy_assignment_id: 合规规则ID
        :type policy_assignment_id: str
        """
        
        

        self._aggregator_id = None
        self._account_id = None
        self._policy_assignment_id = None
        self.discriminator = None

        self.aggregator_id = aggregator_id
        self.account_id = account_id
        self.policy_assignment_id = policy_assignment_id

    @property
    def aggregator_id(self):
        r"""Gets the aggregator_id of this AggregatePolicyAssignmentDetailRequest.

        资源聚合器ID

        :return: The aggregator_id of this AggregatePolicyAssignmentDetailRequest.
        :rtype: str
        """
        return self._aggregator_id

    @aggregator_id.setter
    def aggregator_id(self, aggregator_id):
        r"""Sets the aggregator_id of this AggregatePolicyAssignmentDetailRequest.

        资源聚合器ID

        :param aggregator_id: The aggregator_id of this AggregatePolicyAssignmentDetailRequest.
        :type aggregator_id: str
        """
        self._aggregator_id = aggregator_id

    @property
    def account_id(self):
        r"""Gets the account_id of this AggregatePolicyAssignmentDetailRequest.

        租户ID

        :return: The account_id of this AggregatePolicyAssignmentDetailRequest.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        r"""Sets the account_id of this AggregatePolicyAssignmentDetailRequest.

        租户ID

        :param account_id: The account_id of this AggregatePolicyAssignmentDetailRequest.
        :type account_id: str
        """
        self._account_id = account_id

    @property
    def policy_assignment_id(self):
        r"""Gets the policy_assignment_id of this AggregatePolicyAssignmentDetailRequest.

        合规规则ID

        :return: The policy_assignment_id of this AggregatePolicyAssignmentDetailRequest.
        :rtype: str
        """
        return self._policy_assignment_id

    @policy_assignment_id.setter
    def policy_assignment_id(self, policy_assignment_id):
        r"""Sets the policy_assignment_id of this AggregatePolicyAssignmentDetailRequest.

        合规规则ID

        :param policy_assignment_id: The policy_assignment_id of this AggregatePolicyAssignmentDetailRequest.
        :type policy_assignment_id: str
        """
        self._policy_assignment_id = policy_assignment_id

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
        if not isinstance(other, AggregatePolicyAssignmentDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
