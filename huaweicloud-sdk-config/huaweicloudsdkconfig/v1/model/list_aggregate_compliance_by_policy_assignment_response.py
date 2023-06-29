# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAggregateComplianceByPolicyAssignmentResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'aggregate_policy_assignments': 'list[AggregatePolicyAssignments]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'aggregate_policy_assignments': 'aggregate_policy_assignments',
        'page_info': 'page_info'
    }

    def __init__(self, aggregate_policy_assignments=None, page_info=None):
        """ListAggregateComplianceByPolicyAssignmentResponse

        The model defined in huaweicloud sdk

        :param aggregate_policy_assignments: 聚合合规规则的列表。
        :type aggregate_policy_assignments: list[:class:`huaweicloudsdkconfig.v1.AggregatePolicyAssignments`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkconfig.v1.PageInfo`
        """
        
        super(ListAggregateComplianceByPolicyAssignmentResponse, self).__init__()

        self._aggregate_policy_assignments = None
        self._page_info = None
        self.discriminator = None

        if aggregate_policy_assignments is not None:
            self.aggregate_policy_assignments = aggregate_policy_assignments
        if page_info is not None:
            self.page_info = page_info

    @property
    def aggregate_policy_assignments(self):
        """Gets the aggregate_policy_assignments of this ListAggregateComplianceByPolicyAssignmentResponse.

        聚合合规规则的列表。

        :return: The aggregate_policy_assignments of this ListAggregateComplianceByPolicyAssignmentResponse.
        :rtype: list[:class:`huaweicloudsdkconfig.v1.AggregatePolicyAssignments`]
        """
        return self._aggregate_policy_assignments

    @aggregate_policy_assignments.setter
    def aggregate_policy_assignments(self, aggregate_policy_assignments):
        """Sets the aggregate_policy_assignments of this ListAggregateComplianceByPolicyAssignmentResponse.

        聚合合规规则的列表。

        :param aggregate_policy_assignments: The aggregate_policy_assignments of this ListAggregateComplianceByPolicyAssignmentResponse.
        :type aggregate_policy_assignments: list[:class:`huaweicloudsdkconfig.v1.AggregatePolicyAssignments`]
        """
        self._aggregate_policy_assignments = aggregate_policy_assignments

    @property
    def page_info(self):
        """Gets the page_info of this ListAggregateComplianceByPolicyAssignmentResponse.

        :return: The page_info of this ListAggregateComplianceByPolicyAssignmentResponse.
        :rtype: :class:`huaweicloudsdkconfig.v1.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListAggregateComplianceByPolicyAssignmentResponse.

        :param page_info: The page_info of this ListAggregateComplianceByPolicyAssignmentResponse.
        :type page_info: :class:`huaweicloudsdkconfig.v1.PageInfo`
        """
        self._page_info = page_info

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
        if not isinstance(other, ListAggregateComplianceByPolicyAssignmentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
