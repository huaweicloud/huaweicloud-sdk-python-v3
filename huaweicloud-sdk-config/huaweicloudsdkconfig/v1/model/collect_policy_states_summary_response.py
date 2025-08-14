# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CollectPolicyStatesSummaryResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'results': 'PolicyComplianceSummaryResults',
        'policy_assignments': 'list[PolicyAssignmentComplianceSummary]'
    }

    attribute_map = {
        'results': 'results',
        'policy_assignments': 'policy_assignments'
    }

    def __init__(self, results=None, policy_assignments=None):
        r"""CollectPolicyStatesSummaryResponse

        The model defined in huaweicloud sdk

        :param results: 
        :type results: :class:`huaweicloudsdkconfig.v1.PolicyComplianceSummaryResults`
        :param policy_assignments: 规则合规总结列表
        :type policy_assignments: list[:class:`huaweicloudsdkconfig.v1.PolicyAssignmentComplianceSummary`]
        """
        
        super(CollectPolicyStatesSummaryResponse, self).__init__()

        self._results = None
        self._policy_assignments = None
        self.discriminator = None

        if results is not None:
            self.results = results
        if policy_assignments is not None:
            self.policy_assignments = policy_assignments

    @property
    def results(self):
        r"""Gets the results of this CollectPolicyStatesSummaryResponse.

        :return: The results of this CollectPolicyStatesSummaryResponse.
        :rtype: :class:`huaweicloudsdkconfig.v1.PolicyComplianceSummaryResults`
        """
        return self._results

    @results.setter
    def results(self, results):
        r"""Sets the results of this CollectPolicyStatesSummaryResponse.

        :param results: The results of this CollectPolicyStatesSummaryResponse.
        :type results: :class:`huaweicloudsdkconfig.v1.PolicyComplianceSummaryResults`
        """
        self._results = results

    @property
    def policy_assignments(self):
        r"""Gets the policy_assignments of this CollectPolicyStatesSummaryResponse.

        规则合规总结列表

        :return: The policy_assignments of this CollectPolicyStatesSummaryResponse.
        :rtype: list[:class:`huaweicloudsdkconfig.v1.PolicyAssignmentComplianceSummary`]
        """
        return self._policy_assignments

    @policy_assignments.setter
    def policy_assignments(self, policy_assignments):
        r"""Sets the policy_assignments of this CollectPolicyStatesSummaryResponse.

        规则合规总结列表

        :param policy_assignments: The policy_assignments of this CollectPolicyStatesSummaryResponse.
        :type policy_assignments: list[:class:`huaweicloudsdkconfig.v1.PolicyAssignmentComplianceSummary`]
        """
        self._policy_assignments = policy_assignments

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
        if not isinstance(other, CollectPolicyStatesSummaryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
