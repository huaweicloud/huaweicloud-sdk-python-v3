# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CollectPolicyAssignmentsStatesSummaryRequest:

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
        'resource_name': 'str'
    }

    attribute_map = {
        'policy_assignment_id': 'policy_assignment_id',
        'resource_name': 'resource_name'
    }

    def __init__(self, policy_assignment_id=None, resource_name=None):
        r"""CollectPolicyAssignmentsStatesSummaryRequest

        The model defined in huaweicloud sdk

        :param policy_assignment_id: 规则ID
        :type policy_assignment_id: str
        :param resource_name: 资源名称
        :type resource_name: str
        """
        
        

        self._policy_assignment_id = None
        self._resource_name = None
        self.discriminator = None

        self.policy_assignment_id = policy_assignment_id
        if resource_name is not None:
            self.resource_name = resource_name

    @property
    def policy_assignment_id(self):
        r"""Gets the policy_assignment_id of this CollectPolicyAssignmentsStatesSummaryRequest.

        规则ID

        :return: The policy_assignment_id of this CollectPolicyAssignmentsStatesSummaryRequest.
        :rtype: str
        """
        return self._policy_assignment_id

    @policy_assignment_id.setter
    def policy_assignment_id(self, policy_assignment_id):
        r"""Sets the policy_assignment_id of this CollectPolicyAssignmentsStatesSummaryRequest.

        规则ID

        :param policy_assignment_id: The policy_assignment_id of this CollectPolicyAssignmentsStatesSummaryRequest.
        :type policy_assignment_id: str
        """
        self._policy_assignment_id = policy_assignment_id

    @property
    def resource_name(self):
        r"""Gets the resource_name of this CollectPolicyAssignmentsStatesSummaryRequest.

        资源名称

        :return: The resource_name of this CollectPolicyAssignmentsStatesSummaryRequest.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this CollectPolicyAssignmentsStatesSummaryRequest.

        资源名称

        :param resource_name: The resource_name of this CollectPolicyAssignmentsStatesSummaryRequest.
        :type resource_name: str
        """
        self._resource_name = resource_name

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
        if not isinstance(other, CollectPolicyAssignmentsStatesSummaryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
