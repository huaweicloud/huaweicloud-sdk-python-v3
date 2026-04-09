# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomPolicyAssignmentMetadata:

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
        'policy_filter_v2': 'PolicyFilterDefinitionV2',
        'function_urn': 'str'
    }

    attribute_map = {
        'description': 'description',
        'period': 'period',
        'parameters': 'parameters',
        'policy_filter': 'policy_filter',
        'policy_filter_v2': 'policy_filter_v2',
        'function_urn': 'function_urn'
    }

    def __init__(self, description=None, period=None, parameters=None, policy_filter=None, policy_filter_v2=None, function_urn=None):
        r"""CustomPolicyAssignmentMetadata

        The model defined in huaweicloud sdk

        :param description: 规则描述
        :type description: str
        :param period: 触发周期
        :type period: str
        :param parameters: 输入参数
        :type parameters: dict(str, PolicyParameterValue)
        :param policy_filter: 
        :type policy_filter: :class:`huaweicloudsdkconfig.v1.PolicyFilterDefinition`
        :param policy_filter_v2: 
        :type policy_filter_v2: :class:`huaweicloudsdkconfig.v1.PolicyFilterDefinitionV2`
        :param function_urn: 自定义函数的urn
        :type function_urn: str
        """
        
        

        self._description = None
        self._period = None
        self._parameters = None
        self._policy_filter = None
        self._policy_filter_v2 = None
        self._function_urn = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if period is not None:
            self.period = period
        if parameters is not None:
            self.parameters = parameters
        if policy_filter is not None:
            self.policy_filter = policy_filter
        if policy_filter_v2 is not None:
            self.policy_filter_v2 = policy_filter_v2
        self.function_urn = function_urn

    @property
    def description(self):
        r"""Gets the description of this CustomPolicyAssignmentMetadata.

        规则描述

        :return: The description of this CustomPolicyAssignmentMetadata.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CustomPolicyAssignmentMetadata.

        规则描述

        :param description: The description of this CustomPolicyAssignmentMetadata.
        :type description: str
        """
        self._description = description

    @property
    def period(self):
        r"""Gets the period of this CustomPolicyAssignmentMetadata.

        触发周期

        :return: The period of this CustomPolicyAssignmentMetadata.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        r"""Sets the period of this CustomPolicyAssignmentMetadata.

        触发周期

        :param period: The period of this CustomPolicyAssignmentMetadata.
        :type period: str
        """
        self._period = period

    @property
    def parameters(self):
        r"""Gets the parameters of this CustomPolicyAssignmentMetadata.

        输入参数

        :return: The parameters of this CustomPolicyAssignmentMetadata.
        :rtype: dict(str, PolicyParameterValue)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        r"""Sets the parameters of this CustomPolicyAssignmentMetadata.

        输入参数

        :param parameters: The parameters of this CustomPolicyAssignmentMetadata.
        :type parameters: dict(str, PolicyParameterValue)
        """
        self._parameters = parameters

    @property
    def policy_filter(self):
        r"""Gets the policy_filter of this CustomPolicyAssignmentMetadata.

        :return: The policy_filter of this CustomPolicyAssignmentMetadata.
        :rtype: :class:`huaweicloudsdkconfig.v1.PolicyFilterDefinition`
        """
        return self._policy_filter

    @policy_filter.setter
    def policy_filter(self, policy_filter):
        r"""Sets the policy_filter of this CustomPolicyAssignmentMetadata.

        :param policy_filter: The policy_filter of this CustomPolicyAssignmentMetadata.
        :type policy_filter: :class:`huaweicloudsdkconfig.v1.PolicyFilterDefinition`
        """
        self._policy_filter = policy_filter

    @property
    def policy_filter_v2(self):
        r"""Gets the policy_filter_v2 of this CustomPolicyAssignmentMetadata.

        :return: The policy_filter_v2 of this CustomPolicyAssignmentMetadata.
        :rtype: :class:`huaweicloudsdkconfig.v1.PolicyFilterDefinitionV2`
        """
        return self._policy_filter_v2

    @policy_filter_v2.setter
    def policy_filter_v2(self, policy_filter_v2):
        r"""Sets the policy_filter_v2 of this CustomPolicyAssignmentMetadata.

        :param policy_filter_v2: The policy_filter_v2 of this CustomPolicyAssignmentMetadata.
        :type policy_filter_v2: :class:`huaweicloudsdkconfig.v1.PolicyFilterDefinitionV2`
        """
        self._policy_filter_v2 = policy_filter_v2

    @property
    def function_urn(self):
        r"""Gets the function_urn of this CustomPolicyAssignmentMetadata.

        自定义函数的urn

        :return: The function_urn of this CustomPolicyAssignmentMetadata.
        :rtype: str
        """
        return self._function_urn

    @function_urn.setter
    def function_urn(self, function_urn):
        r"""Sets the function_urn of this CustomPolicyAssignmentMetadata.

        自定义函数的urn

        :param function_urn: The function_urn of this CustomPolicyAssignmentMetadata.
        :type function_urn: str
        """
        self._function_urn = function_urn

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CustomPolicyAssignmentMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
