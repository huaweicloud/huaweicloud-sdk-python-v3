# coding: utf-8

import pprint
import re

import six





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
        'name': 'str',
        'description': 'str',
        'policy_filter': 'PolicyFilterDefinition',
        'policy_definition_id': 'str',
        'parameters': 'dict(str, PolicyParameterValue)'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'policy_filter': 'policy_filter',
        'policy_definition_id': 'policy_definition_id',
        'parameters': 'parameters'
    }

    def __init__(self, name=None, description=None, policy_filter=None, policy_definition_id=None, parameters=None):
        """PolicyAssignmentRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._description = None
        self._policy_filter = None
        self._policy_definition_id = None
        self._parameters = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if policy_filter is not None:
            self.policy_filter = policy_filter
        if policy_definition_id is not None:
            self.policy_definition_id = policy_definition_id
        if parameters is not None:
            self.parameters = parameters

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
        :type: str
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
        :type: str
        """
        self._description = description

    @property
    def policy_filter(self):
        """Gets the policy_filter of this PolicyAssignmentRequestBody.


        :return: The policy_filter of this PolicyAssignmentRequestBody.
        :rtype: PolicyFilterDefinition
        """
        return self._policy_filter

    @policy_filter.setter
    def policy_filter(self, policy_filter):
        """Sets the policy_filter of this PolicyAssignmentRequestBody.


        :param policy_filter: The policy_filter of this PolicyAssignmentRequestBody.
        :type: PolicyFilterDefinition
        """
        self._policy_filter = policy_filter

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
        :type: str
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
        :type: dict(str, PolicyParameterValue)
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PolicyAssignmentRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
