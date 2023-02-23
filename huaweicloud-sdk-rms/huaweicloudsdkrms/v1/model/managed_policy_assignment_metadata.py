# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ManagedPolicyAssignmentMetadata:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'period': 'str',
        'parameters': 'dict(str, PolicyParameterValue)',
        'policy_filter': 'PolicyFilterDefinition',
        'policy_definition_id': 'str'
    }

    attribute_map = {
        'description': 'description',
        'period': 'period',
        'parameters': 'parameters',
        'policy_filter': 'policy_filter',
        'policy_definition_id': 'policy_definition_id'
    }

    def __init__(self, description=None, period=None, parameters=None, policy_filter=None, policy_definition_id=None):
        """ManagedPolicyAssignmentMetadata

        The model defined in huaweicloud sdk

        :param description: 规则描述。
        :type description: str
        :param period: 触发周期。
        :type period: str
        :param parameters: 输入参数。
        :type parameters: dict(str, PolicyParameterValue)
        :param policy_filter: 
        :type policy_filter: :class:`huaweicloudsdkrms.v1.PolicyFilterDefinition`
        :param policy_definition_id: 预定义策略标识符。
        :type policy_definition_id: str
        """
        
        

        self._description = None
        self._period = None
        self._parameters = None
        self._policy_filter = None
        self._policy_definition_id = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if period is not None:
            self.period = period
        if parameters is not None:
            self.parameters = parameters
        if policy_filter is not None:
            self.policy_filter = policy_filter
        self.policy_definition_id = policy_definition_id

    @property
    def description(self):
        """Gets the description of this ManagedPolicyAssignmentMetadata.

        规则描述。

        :return: The description of this ManagedPolicyAssignmentMetadata.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ManagedPolicyAssignmentMetadata.

        规则描述。

        :param description: The description of this ManagedPolicyAssignmentMetadata.
        :type description: str
        """
        self._description = description

    @property
    def period(self):
        """Gets the period of this ManagedPolicyAssignmentMetadata.

        触发周期。

        :return: The period of this ManagedPolicyAssignmentMetadata.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this ManagedPolicyAssignmentMetadata.

        触发周期。

        :param period: The period of this ManagedPolicyAssignmentMetadata.
        :type period: str
        """
        self._period = period

    @property
    def parameters(self):
        """Gets the parameters of this ManagedPolicyAssignmentMetadata.

        输入参数。

        :return: The parameters of this ManagedPolicyAssignmentMetadata.
        :rtype: dict(str, PolicyParameterValue)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this ManagedPolicyAssignmentMetadata.

        输入参数。

        :param parameters: The parameters of this ManagedPolicyAssignmentMetadata.
        :type parameters: dict(str, PolicyParameterValue)
        """
        self._parameters = parameters

    @property
    def policy_filter(self):
        """Gets the policy_filter of this ManagedPolicyAssignmentMetadata.

        :return: The policy_filter of this ManagedPolicyAssignmentMetadata.
        :rtype: :class:`huaweicloudsdkrms.v1.PolicyFilterDefinition`
        """
        return self._policy_filter

    @policy_filter.setter
    def policy_filter(self, policy_filter):
        """Sets the policy_filter of this ManagedPolicyAssignmentMetadata.

        :param policy_filter: The policy_filter of this ManagedPolicyAssignmentMetadata.
        :type policy_filter: :class:`huaweicloudsdkrms.v1.PolicyFilterDefinition`
        """
        self._policy_filter = policy_filter

    @property
    def policy_definition_id(self):
        """Gets the policy_definition_id of this ManagedPolicyAssignmentMetadata.

        预定义策略标识符。

        :return: The policy_definition_id of this ManagedPolicyAssignmentMetadata.
        :rtype: str
        """
        return self._policy_definition_id

    @policy_definition_id.setter
    def policy_definition_id(self, policy_definition_id):
        """Sets the policy_definition_id of this ManagedPolicyAssignmentMetadata.

        预定义策略标识符。

        :param policy_definition_id: The policy_definition_id of this ManagedPolicyAssignmentMetadata.
        :type policy_definition_id: str
        """
        self._policy_definition_id = policy_definition_id

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
        if not isinstance(other, ManagedPolicyAssignmentMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
