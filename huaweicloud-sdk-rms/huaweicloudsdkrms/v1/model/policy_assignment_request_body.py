# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyAssignmentRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_assignment_type': 'str',
        'name': 'str',
        'description': 'str',
        'period': 'str',
        'policy_filter': 'PolicyFilterDefinition',
        'custom_policy': 'CustomPolicy',
        'policy_definition_id': 'str',
        'parameters': 'dict(str, PolicyParameterValue)'
    }

    attribute_map = {
        'policy_assignment_type': 'policy_assignment_type',
        'name': 'name',
        'description': 'description',
        'period': 'period',
        'policy_filter': 'policy_filter',
        'custom_policy': 'custom_policy',
        'policy_definition_id': 'policy_definition_id',
        'parameters': 'parameters'
    }

    def __init__(self, policy_assignment_type=None, name=None, description=None, period=None, policy_filter=None, custom_policy=None, policy_definition_id=None, parameters=None):
        """PolicyAssignmentRequestBody

        The model defined in huaweicloud sdk

        :param policy_assignment_type: 规则类型，包括预定义合规规则(builtin)和用户自定义合规规则(custom)
        :type policy_assignment_type: str
        :param name: 规则名字
        :type name: str
        :param description: 规则描述
        :type description: str
        :param period: 触发周期值，可选值：One_Hour, Three_Hours, Six_Hours, Twelve_Hours, TwentyFour_Hours
        :type period: str
        :param policy_filter: 
        :type policy_filter: :class:`huaweicloudsdkrms.v1.PolicyFilterDefinition`
        :param custom_policy: 
        :type custom_policy: :class:`huaweicloudsdkrms.v1.CustomPolicy`
        :param policy_definition_id: 策略定义ID
        :type policy_definition_id: str
        :param parameters: 规则参数
        :type parameters: dict(str, PolicyParameterValue)
        """
        
        

        self._policy_assignment_type = None
        self._name = None
        self._description = None
        self._period = None
        self._policy_filter = None
        self._custom_policy = None
        self._policy_definition_id = None
        self._parameters = None
        self.discriminator = None

        if policy_assignment_type is not None:
            self.policy_assignment_type = policy_assignment_type
        self.name = name
        if description is not None:
            self.description = description
        if period is not None:
            self.period = period
        if policy_filter is not None:
            self.policy_filter = policy_filter
        if custom_policy is not None:
            self.custom_policy = custom_policy
        if policy_definition_id is not None:
            self.policy_definition_id = policy_definition_id
        if parameters is not None:
            self.parameters = parameters

    @property
    def policy_assignment_type(self):
        """Gets the policy_assignment_type of this PolicyAssignmentRequestBody.

        规则类型，包括预定义合规规则(builtin)和用户自定义合规规则(custom)

        :return: The policy_assignment_type of this PolicyAssignmentRequestBody.
        :rtype: str
        """
        return self._policy_assignment_type

    @policy_assignment_type.setter
    def policy_assignment_type(self, policy_assignment_type):
        """Sets the policy_assignment_type of this PolicyAssignmentRequestBody.

        规则类型，包括预定义合规规则(builtin)和用户自定义合规规则(custom)

        :param policy_assignment_type: The policy_assignment_type of this PolicyAssignmentRequestBody.
        :type policy_assignment_type: str
        """
        self._policy_assignment_type = policy_assignment_type

    @property
    def name(self):
        """Gets the name of this PolicyAssignmentRequestBody.

        规则名字

        :return: The name of this PolicyAssignmentRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PolicyAssignmentRequestBody.

        规则名字

        :param name: The name of this PolicyAssignmentRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this PolicyAssignmentRequestBody.

        规则描述

        :return: The description of this PolicyAssignmentRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PolicyAssignmentRequestBody.

        规则描述

        :param description: The description of this PolicyAssignmentRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def period(self):
        """Gets the period of this PolicyAssignmentRequestBody.

        触发周期值，可选值：One_Hour, Three_Hours, Six_Hours, Twelve_Hours, TwentyFour_Hours

        :return: The period of this PolicyAssignmentRequestBody.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this PolicyAssignmentRequestBody.

        触发周期值，可选值：One_Hour, Three_Hours, Six_Hours, Twelve_Hours, TwentyFour_Hours

        :param period: The period of this PolicyAssignmentRequestBody.
        :type period: str
        """
        self._period = period

    @property
    def policy_filter(self):
        """Gets the policy_filter of this PolicyAssignmentRequestBody.

        :return: The policy_filter of this PolicyAssignmentRequestBody.
        :rtype: :class:`huaweicloudsdkrms.v1.PolicyFilterDefinition`
        """
        return self._policy_filter

    @policy_filter.setter
    def policy_filter(self, policy_filter):
        """Sets the policy_filter of this PolicyAssignmentRequestBody.

        :param policy_filter: The policy_filter of this PolicyAssignmentRequestBody.
        :type policy_filter: :class:`huaweicloudsdkrms.v1.PolicyFilterDefinition`
        """
        self._policy_filter = policy_filter

    @property
    def custom_policy(self):
        """Gets the custom_policy of this PolicyAssignmentRequestBody.

        :return: The custom_policy of this PolicyAssignmentRequestBody.
        :rtype: :class:`huaweicloudsdkrms.v1.CustomPolicy`
        """
        return self._custom_policy

    @custom_policy.setter
    def custom_policy(self, custom_policy):
        """Sets the custom_policy of this PolicyAssignmentRequestBody.

        :param custom_policy: The custom_policy of this PolicyAssignmentRequestBody.
        :type custom_policy: :class:`huaweicloudsdkrms.v1.CustomPolicy`
        """
        self._custom_policy = custom_policy

    @property
    def policy_definition_id(self):
        """Gets the policy_definition_id of this PolicyAssignmentRequestBody.

        策略定义ID

        :return: The policy_definition_id of this PolicyAssignmentRequestBody.
        :rtype: str
        """
        return self._policy_definition_id

    @policy_definition_id.setter
    def policy_definition_id(self, policy_definition_id):
        """Sets the policy_definition_id of this PolicyAssignmentRequestBody.

        策略定义ID

        :param policy_definition_id: The policy_definition_id of this PolicyAssignmentRequestBody.
        :type policy_definition_id: str
        """
        self._policy_definition_id = policy_definition_id

    @property
    def parameters(self):
        """Gets the parameters of this PolicyAssignmentRequestBody.

        规则参数

        :return: The parameters of this PolicyAssignmentRequestBody.
        :rtype: dict(str, PolicyParameterValue)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this PolicyAssignmentRequestBody.

        规则参数

        :param parameters: The parameters of this PolicyAssignmentRequestBody.
        :type parameters: dict(str, PolicyParameterValue)
        """
        self._parameters = parameters

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
        if not isinstance(other, PolicyAssignmentRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
