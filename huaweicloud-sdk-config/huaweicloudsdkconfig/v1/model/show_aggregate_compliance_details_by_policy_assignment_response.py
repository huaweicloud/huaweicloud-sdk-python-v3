# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAggregateComplianceDetailsByPolicyAssignmentResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_states': 'list[PolicyState]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'policy_states': 'policy_states',
        'page_info': 'page_info'
    }

    def __init__(self, policy_states=None, page_info=None):
        """ShowAggregateComplianceDetailsByPolicyAssignmentResponse

        The model defined in huaweicloud sdk

        :param policy_states: 合规结果查询返回值
        :type policy_states: list[:class:`huaweicloudsdkconfig.v1.PolicyState`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkconfig.v1.PageInfo`
        """
        
        super(ShowAggregateComplianceDetailsByPolicyAssignmentResponse, self).__init__()

        self._policy_states = None
        self._page_info = None
        self.discriminator = None

        if policy_states is not None:
            self.policy_states = policy_states
        if page_info is not None:
            self.page_info = page_info

    @property
    def policy_states(self):
        """Gets the policy_states of this ShowAggregateComplianceDetailsByPolicyAssignmentResponse.

        合规结果查询返回值

        :return: The policy_states of this ShowAggregateComplianceDetailsByPolicyAssignmentResponse.
        :rtype: list[:class:`huaweicloudsdkconfig.v1.PolicyState`]
        """
        return self._policy_states

    @policy_states.setter
    def policy_states(self, policy_states):
        """Sets the policy_states of this ShowAggregateComplianceDetailsByPolicyAssignmentResponse.

        合规结果查询返回值

        :param policy_states: The policy_states of this ShowAggregateComplianceDetailsByPolicyAssignmentResponse.
        :type policy_states: list[:class:`huaweicloudsdkconfig.v1.PolicyState`]
        """
        self._policy_states = policy_states

    @property
    def page_info(self):
        """Gets the page_info of this ShowAggregateComplianceDetailsByPolicyAssignmentResponse.

        :return: The page_info of this ShowAggregateComplianceDetailsByPolicyAssignmentResponse.
        :rtype: :class:`huaweicloudsdkconfig.v1.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ShowAggregateComplianceDetailsByPolicyAssignmentResponse.

        :param page_info: The page_info of this ShowAggregateComplianceDetailsByPolicyAssignmentResponse.
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
        if not isinstance(other, ShowAggregateComplianceDetailsByPolicyAssignmentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
